#!/bin/bash
# Channel47 Plugin Suite Validator
# Validates structural consistency and spec compliance for DTC plugins.
#
# Usage: bash validate.sh [plugin-name]
#   No args = validate all plugins
#   plugin-name = validate one plugin (e.g., "dtc-google-ads-playbook")

set -uo pipefail

REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
PLUGINS_DIR="$REPO_ROOT/plugins"
TARGET_PLUGIN="${1:-}"

# Colors (disabled in CI for clean logs)
if [ -n "${CI:-}" ]; then
  RED='' GREEN='' YELLOW='' CYAN='' BOLD='' NC=''
else
  RED='\033[0;31m'
  GREEN='\033[0;32m'
  YELLOW='\033[0;33m'
  CYAN='\033[0;36m'
  BOLD='\033[1m'
  NC='\033[0m'
fi

# Use temp files for counters so they work inside subshells
COUNTER_DIR=$(mktemp -d)
echo 0 > "$COUNTER_DIR/passes"
echo 0 > "$COUNTER_DIR/warnings"
echo 0 > "$COUNTER_DIR/errors"
trap 'rm -rf "$COUNTER_DIR"' EXIT

pass() {
  echo $(( $(cat "$COUNTER_DIR/passes") + 1 )) > "$COUNTER_DIR/passes"
  echo -e "  ${GREEN}ok${NC} $1"
}
warn() {
  echo $(( $(cat "$COUNTER_DIR/warnings") + 1 )) > "$COUNTER_DIR/warnings"
  echo -e "  ${YELLOW}!!${NC} $1"
}
fail() {
  echo $(( $(cat "$COUNTER_DIR/errors") + 1 )) > "$COUNTER_DIR/errors"
  echo -e "  ${RED}FAIL${NC} $1"
}
section() { echo -e "\n${CYAN}${BOLD}$1${NC}"; }

# Determine which plugins to validate (skip _archived)
if [ -n "$TARGET_PLUGIN" ]; then
  if [ ! -d "$PLUGINS_DIR/$TARGET_PLUGIN" ]; then
    echo -e "${RED}Plugin '$TARGET_PLUGIN' not found in $PLUGINS_DIR${NC}"
    exit 1
  fi
  PLUGIN_DIRS=("$PLUGINS_DIR/$TARGET_PLUGIN")
else
  PLUGIN_DIRS=()
  for d in "$PLUGINS_DIR"/*/; do
    [ -d "$d" ] || continue
    pname=$(basename "$d")
    [ "$pname" = "_archived" ] && continue
    PLUGIN_DIRS+=("${d%/}")
  done
fi

echo -e "${BOLD}Channel47 Plugin Validator${NC}"
echo "Validating ${#PLUGIN_DIRS[@]} plugin(s)..."

# ============================================================
# 1. MARKETPLACE REGISTRY CONSISTENCY
# ============================================================
section "Marketplace Registry"

MARKETPLACE="$REPO_ROOT/.claude-plugin/marketplace.json"
if [ ! -f "$MARKETPLACE" ]; then
  fail "marketplace.json not found at $MARKETPLACE"
else
  for plugin_dir in "${PLUGIN_DIRS[@]}"; do
    plugin_name=$(basename "$plugin_dir")
    if python3 -c "
import json, sys
with open('$MARKETPLACE') as f:
    data = json.load(f)
found = any(p['name'] == '$plugin_name' for p in data.get('plugins', []))
sys.exit(0 if found else 1)
" 2>/dev/null; then
      pass "$plugin_name listed in marketplace.json"
    else
      fail "$plugin_name missing from marketplace.json"
    fi
  done

  # Check version sync
  for plugin_dir in "${PLUGIN_DIRS[@]}"; do
    plugin_name=$(basename "$plugin_dir")
    plugin_json="$plugin_dir/.claude-plugin/plugin.json"
    if [ -f "$plugin_json" ]; then
      python3 -c "
import json, sys
with open('$MARKETPLACE') as f:
    mp = json.load(f)
with open('$plugin_json') as f:
    pj = json.load(f)
mp_entry = next((p for p in mp.get('plugins', []) if p['name'] == '$plugin_name'), None)
if mp_entry:
    if mp_entry.get('version') == pj.get('version'):
        print('MATCH')
    else:
        print(f'MISMATCH:{mp_entry.get(\"version\")}:{pj.get(\"version\")}')
else:
    print('MISSING')
" 2>/dev/null | while IFS=: read -r status mp_ver pj_ver; do
        if [ "$status" = "MATCH" ]; then
          pass "$plugin_name version synced (marketplace <-> plugin.json)"
        elif [ "$status" = "MISMATCH" ]; then
          fail "$plugin_name version mismatch: marketplace=$mp_ver, plugin.json=$pj_ver"
        fi
      done
    fi
  done
fi

# ============================================================
# 2. PER-PLUGIN STRUCTURE CHECKS
# ============================================================
for plugin_dir in "${PLUGIN_DIRS[@]}"; do
  plugin_name=$(basename "$plugin_dir")

  section "Plugin: $plugin_name"

  # --- Required files ---
  for required in ".claude-plugin/plugin.json" "README.md"; do
    if [ -f "$plugin_dir/$required" ]; then
      pass "$required exists"
    else
      fail "$required missing"
    fi
  done

  # --- plugin.json schema ---
  plugin_json="$plugin_dir/.claude-plugin/plugin.json"
  if [ -f "$plugin_json" ]; then
    python3 -c "
import json, sys
with open('$plugin_json') as f:
    data = json.load(f)
required = ['name', 'version', 'description', 'author']
missing = [k for k in required if k not in data]
if missing:
    print('MISSING:' + ','.join(missing))
else:
    print('OK')
if data.get('name') != '$plugin_name':
    print(f'NAME_MISMATCH:{data.get(\"name\")}')
" 2>/dev/null | while IFS=: read -r status detail; do
      if [ "$status" = "OK" ]; then
        pass "plugin.json has all required fields"
      elif [ "$status" = "MISSING" ]; then
        fail "plugin.json missing fields: $detail"
      elif [ "$status" = "NAME_MISMATCH" ]; then
        fail "plugin.json name '$detail' doesn't match directory '$plugin_name'"
      fi
    done
  fi

  # ============================================================
  # 3. SKILL VALIDATION
  # ============================================================
  skills_dir="$plugin_dir/skills"
  if [ -d "$skills_dir" ]; then
    skill_count=0
    for skill_dir in "$skills_dir"/*/; do
      [ ! -d "$skill_dir" ] && continue
      skill_name=$(basename "$skill_dir")
      skill_file="$skill_dir/SKILL.md"
      ((skill_count++))

      if [ ! -f "$skill_file" ]; then
        fail "skills/$skill_name/ missing SKILL.md"
        continue
      fi

      # Extract frontmatter
      frontmatter=$(sed -n '/^---$/,/^---$/p' "$skill_file" | sed '1d;$d')

      # Check required frontmatter fields
      fm_name=$(echo "$frontmatter" | grep -m1 '^name:' | sed 's/^name: *//' || true)
      fm_desc=$(echo "$frontmatter" | grep -m1 '^description:' || true)

      # Check name exists in frontmatter (allow display names that don't match directory)
      has_name=$(python3 -c "
import re
with open('$skill_file') as f:
    content = f.read()
m = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
if m and re.search(r'^name:', m.group(1), re.MULTILINE):
    print('yes')
else:
    print('no')
" 2>/dev/null)
      if [ "$has_name" = "yes" ]; then
        pass "skills/$skill_name has name in frontmatter"
      else
        fail "skills/$skill_name/SKILL.md missing 'name' in frontmatter"
      fi

      # Check description exists (handles multiline > syntax)
      has_desc=$(python3 -c "
import re
with open('$skill_file') as f:
    content = f.read()
m = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
if m and re.search(r'^description:', m.group(1), re.MULTILINE):
    print('yes')
else:
    print('no')
" 2>/dev/null)
      if [ "$has_desc" = "yes" ]; then
        pass "skills/$skill_name has description"
      else
        fail "skills/$skill_name/SKILL.md missing 'description'"
      fi

      # Check line count
      line_count=$(wc -l < "$skill_file" | tr -d ' ')
      if [ "$line_count" -lt 30 ]; then
        warn "skills/$skill_name/SKILL.md is only $line_count lines (may be a stub)"
      else
        pass "skills/$skill_name line count ok ($line_count)"
      fi

      # Check reference file cross-references
      grep -oE 'references/[a-z0-9_-]+\.md' "$skill_file" 2>/dev/null | sort -u | while read -r ref; do
        ref_path="$skill_dir/$ref"
        if [ ! -f "$ref_path" ]; then
          fail "skills/$skill_name references '$ref' but file doesn't exist"
        else
          pass "skills/$skill_name -> $ref exists"
        fi
      done

    done
    pass "Found $skill_count skill(s)"
  fi

  # ============================================================
  # 4. COMMAND VALIDATION
  # ============================================================
  commands_dir="$plugin_dir/commands"
  if [ -d "$commands_dir" ]; then
    cmd_count=0
    for cmd_file in "$commands_dir"/*.md; do
      [ ! -f "$cmd_file" ] && continue
      ((cmd_count++))
      cmd_name=$(basename "$cmd_file" .md)
      pass "commands/$cmd_name.md exists"
    done
    pass "Found $cmd_count command(s)"
  fi

  # ============================================================
  # 5. AGENT VALIDATION
  # ============================================================
  agents_dir="$plugin_dir/agents"
  if [ -d "$agents_dir" ]; then
    for agent_file in "$agents_dir"/*.md; do
      [ ! -f "$agent_file" ] && continue
      agent_name=$(basename "$agent_file" .md)

      # Check frontmatter basics
      frontmatter=$(sed -n '/^---$/,/^---$/p' "$agent_file" | sed '1d;$d')
      fm_name=$(echo "$frontmatter" | grep -m1 '^name:' | sed 's/^name: *//' || true)
      fm_desc=$(echo "$frontmatter" | grep -m1 '^description:' || true)
      fm_tools=$(echo "$frontmatter" | grep -m1 '^tools:' || true)

      # Check name exists (handles multiline frontmatter)
      has_name=$(python3 -c "
import re
with open('$agent_file') as f:
    content = f.read()
m = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
if m and re.search(r'^name:', m.group(1), re.MULTILINE):
    print('yes')
else:
    print('no')
" 2>/dev/null)
      if [ "$has_name" = "yes" ]; then
        pass "agents/$agent_name has name"
      else
        fail "agents/$agent_name.md missing 'name' in frontmatter"
      fi

      # Check description exists (handles multiline | syntax)
      has_desc=$(python3 -c "
import re
with open('$agent_file') as f:
    content = f.read()
m = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
if m and re.search(r'^description:', m.group(1), re.MULTILINE):
    print('yes')
else:
    print('no')
" 2>/dev/null)
      if [ "$has_desc" = "yes" ]; then
        pass "agents/$agent_name has description"
      else
        fail "agents/$agent_name.md missing 'description'"
      fi

      if [ -z "$fm_tools" ]; then
        warn "agents/$agent_name.md missing 'tools' field"
      fi

      # Check agents use 'tools:' not 'allowed-tools:'
      if echo "$frontmatter" | grep -q '^allowed-tools:'; then
        fail "agents/$agent_name.md uses 'allowed-tools:' (agents must use 'tools:')"
      fi

      line_count=$(wc -l < "$agent_file" | tr -d ' ')
      if [ "$line_count" -lt 30 ]; then
        warn "agents/$agent_name is only $line_count lines (may be a stub)"
      else
        pass "agents/$agent_name line count ok ($line_count)"
      fi
    done
  fi

done

# ============================================================
# SUMMARY
# ============================================================
PASSES=$(cat "$COUNTER_DIR/passes")
WARNINGS=$(cat "$COUNTER_DIR/warnings")
ERRORS=$(cat "$COUNTER_DIR/errors")

echo ""
echo -e "${BOLD}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}Passed:${NC}   $PASSES"
echo -e "${YELLOW}Warnings:${NC} $WARNINGS"
echo -e "${RED}Errors:${NC}   $ERRORS"
echo -e "${BOLD}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

if [ "$ERRORS" -gt 0 ]; then
  echo -e "${RED}${BOLD}Validation failed with $ERRORS error(s).${NC}"
  exit 1
else
  if [ "$WARNINGS" -gt 0 ]; then
    echo -e "${YELLOW}${BOLD}Validation passed with $WARNINGS warning(s).${NC}"
  else
    echo -e "${GREEN}${BOLD}All checks passed.${NC}"
  fi
  exit 0
fi
