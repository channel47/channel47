#!/bin/bash
# Channel47 Plugin Suite Validator
# Validates structural consistency, cross-file references, and spec compliance
# across all paid media plugins.
#
# Usage: bash validate.sh [plugin-name]
#   No args = validate all plugins
#   plugin-name = validate one plugin (e.g., "google-ads")

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

# Use temp files for counters so they work inside subshells (piped while-read loops)
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

# Determine which plugins to validate
if [ -n "$TARGET_PLUGIN" ]; then
  if [ ! -d "$PLUGINS_DIR/$TARGET_PLUGIN" ]; then
    echo -e "${RED}Plugin '$TARGET_PLUGIN' not found in $PLUGINS_DIR${NC}"
    exit 1
  fi
  PLUGIN_DIRS=("$PLUGINS_DIR/$TARGET_PLUGIN")
else
  PLUGIN_DIRS=()
  for d in "$PLUGINS_DIR"/*/; do
    [ -d "$d" ] && PLUGIN_DIRS+=("${d%/}")
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
  # Check each plugin directory has a registry entry
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

  # Check registry entries point to existing directories
  python3 -c "
import json, os, sys
with open('$MARKETPLACE') as f:
    data = json.load(f)
for p in data.get('plugins', []):
    source = p.get('source', '')
    full_path = os.path.join('$REPO_ROOT', source)
    if not os.path.isdir(full_path):
        print(f'ORPHAN:{p[\"name\"]}:{source}')
" 2>/dev/null | while IFS=: read -r _ name source; do
    fail "Registry entry '$name' points to missing directory: $source"
  done

  # Check version sync between marketplace and plugin.json
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

  # Skip deprecated plugins
  if [ -f "$plugin_dir/DEPRECATED.md" ]; then
    section "Plugin: $plugin_name (DEPRECATED — skipping)"
    pass "Deprecated plugin skipped"
    continue
  fi

  section "Plugin: $plugin_name"

  # --- Required files ---
  for required in ".claude-plugin/plugin.json" ".mcp.json" "README.md" "LICENSE" "hooks/hooks.json"; do
    if [ -f "$plugin_dir/$required" ]; then
      pass "$required exists"
    else
      if [ "$required" = ".mcp.json" ] && ! grep -rql 'mcp__' "$plugin_dir/skills/" 2>/dev/null; then
        pass "$required not required (no MCP tool references in skills)"
      else
        fail "$required missing"
      fi
    fi
  done

  # --- plugin.json schema ---
  plugin_json="$plugin_dir/.claude-plugin/plugin.json"
  if [ -f "$plugin_json" ]; then
    python3 -c "
import json, sys
with open('$plugin_json') as f:
    data = json.load(f)
required = ['name', 'version', 'description', 'author', 'license']
missing = [k for k in required if k not in data]
if missing:
    print('MISSING:' + ','.join(missing))
else:
    print('OK')
# Check name matches directory
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

  # --- MCP config validation ---
  mcp_json="$plugin_dir/.mcp.json"
  if [ -f "$mcp_json" ]; then
    python3 -c "
import json, sys
with open('$mcp_json') as f:
    data = json.load(f)
for server_name, config in data.items():
    if 'command' not in config:
        print(f'NO_COMMAND:{server_name}')
        continue
    # Check for hardcoded secrets
    env = config.get('env', {})
    for k, v in env.items():
        if not v.startswith('\${') and v not in ('true', 'false'):
            print(f'HARDCODED_SECRET:{server_name}:{k}')
    print(f'OK:{server_name}')
" 2>/dev/null | while IFS=: read -r status detail extra; do
      if [ "$status" = "OK" ]; then
        pass "MCP server '$detail' configured correctly"
      elif [ "$status" = "NO_COMMAND" ]; then
        fail "MCP server '$detail' missing 'command' field"
      elif [ "$status" = "HARDCODED_SECRET" ]; then
        fail "MCP server '$detail' has hardcoded value for '$extra' (use \${ENV_VAR} syntax)"
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
      fm_tools=$(echo "$frontmatter" | grep -m1 '^allowed-tools:' || true)

      if [ -z "$fm_name" ]; then
        fail "skills/$skill_name/SKILL.md missing 'name' in frontmatter"
      elif [ "$fm_name" != "$skill_name" ]; then
        fail "skills/$skill_name/SKILL.md name='$fm_name' doesn't match directory"
      else
        pass "skills/$skill_name name matches directory"
      fi

      if [ -z "$fm_desc" ]; then
        fail "skills/$skill_name/SKILL.md missing 'description'"
      else
        # Count description words using python for reliable YAML parsing
        word_count=$(python3 -c "
import re
with open('$skill_file') as f:
    content = f.read()
# Extract frontmatter
m = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
if not m:
    print(0)
else:
    fm = m.group(1)
    # Extract description field (handles multiline >- syntax)
    dm = re.search(r'^description:\s*>-?\s*\n((?:\s+.*\n)*)', fm, re.MULTILINE)
    if dm:
        desc = dm.group(1).strip()
    else:
        dm = re.search(r'^description:\s*(.+)', fm, re.MULTILINE)
        desc = dm.group(1).strip() if dm else ''
    print(len(desc.split()))
" 2>/dev/null)
        if [ "$word_count" -gt 85 ]; then
          warn "skills/$skill_name description is ~$word_count words (target: 60-80, max: 85)"
        elif [ "$word_count" -lt 30 ]; then
          warn "skills/$skill_name description is only ~$word_count words (target: 60-80)"
        else
          pass "skills/$skill_name description length ok (~$word_count words)"
        fi
      fi

      if [ -z "$fm_tools" ]; then
        warn "skills/$skill_name/SKILL.md missing 'allowed-tools' (skill has no tool access)"
      fi

      # Check line count
      line_count=$(wc -l < "$skill_file" | tr -d ' ')
      if [ "$line_count" -gt 500 ]; then
        warn "skills/$skill_name/SKILL.md is $line_count lines (recommended: <500)"
      elif [ "$line_count" -lt 30 ]; then
        warn "skills/$skill_name/SKILL.md is only $line_count lines (may be a stub)"
      else
        pass "skills/$skill_name line count ok ($line_count)"
      fi

      # Check for mutation tool references (read-only constraint)
      if [ "$plugin_name" != "frontend-craft" ]; then
        if grep -qi 'mutate\|create_campaign\|update_campaign\|delete\|set_budget\|add_keyword\|remove_keyword' "$skill_file" 2>/dev/null; then
          # Only flag if it's in allowed-tools, not in prose
          if echo "$fm_tools" | grep -qi 'mutate\|create\|update\|delete\|set_budget' 2>/dev/null; then
            fail "skills/$skill_name references mutation tools in allowed-tools (read-only constraint)"
          fi
        fi
      fi

      # Check reference file cross-references
      grep -oE 'references/[a-z0-9_-]+\.md' "$skill_file" 2>/dev/null | sort -u | while read -r ref; do
        ref_path="$plugin_dir/$ref"
        if [ ! -f "$ref_path" ]; then
          fail "skills/$skill_name references '$ref' but file doesn't exist"
        else
          pass "skills/$skill_name -> $ref exists"
        fi
      done

      # Check agent cross-references
      grep -oE 'agents/[a-z0-9_-]+\.md' "$skill_file" 2>/dev/null | sort -u | while read -r ref; do
        ref_path="$plugin_dir/$ref"
        if [ ! -f "$ref_path" ]; then
          fail "skills/$skill_name references '$ref' but file doesn't exist"
        fi
      done

    done

    # Check skill count matches plugin.json description
    if [ -f "$plugin_json" ]; then
      claimed_count=$(python3 -c "
import json, re
with open('$plugin_json') as f:
    desc = json.load(f).get('description', '')
m = re.search(r'(\d+)\s+skills?', desc)
print(m.group(1) if m else '0')
" 2>/dev/null)
      if [ "$claimed_count" != "0" ] && [ "$claimed_count" != "$skill_count" ]; then
        fail "plugin.json claims $claimed_count skills but found $skill_count"
      elif [ "$claimed_count" != "0" ]; then
        pass "Skill count matches: $skill_count claimed, $skill_count found"
      fi
    fi
  fi

  # ============================================================
  # 4. AGENT VALIDATION
  # ============================================================
  agents_dir="$plugin_dir/agents"
  if [ -d "$agents_dir" ]; then
    for agent_file in "$agents_dir"/*.md; do
      [ ! -f "$agent_file" ] && continue
      agent_name=$(basename "$agent_file" .md)

      # Check frontmatter
      frontmatter=$(sed -n '/^---$/,/^---$/p' "$agent_file" | sed '1d;$d')
      fm_name=$(echo "$frontmatter" | grep -m1 '^name:' | sed 's/^name: *//' || true)
      fm_desc=$(echo "$frontmatter" | grep -m1 '^description:' || true)
      fm_tools=$(echo "$frontmatter" | grep -m1 '^tools:' || true)

      if [ -z "$fm_name" ]; then
        fail "agents/$agent_name.md missing 'name' in frontmatter"
      elif [ "$fm_name" != "$agent_name" ]; then
        fail "agents/$agent_name.md name='$fm_name' doesn't match filename"
      else
        pass "agents/$agent_name name matches filename"
      fi

      if [ -z "$fm_desc" ]; then
        fail "agents/$agent_name.md missing 'description'"
      else
        pass "agents/$agent_name has description"
      fi

      if [ -z "$fm_tools" ]; then
        warn "agents/$agent_name.md missing 'tools' field"
      fi

      # Check agents use 'tools:' not 'allowed-tools:'
      if echo "$frontmatter" | grep -q '^allowed-tools:'; then
        fail "agents/$agent_name.md uses 'allowed-tools:' (agents must use 'tools:')"
      fi

      # Check for required sections
      for required_section in "Output Schema" "Fallback Behavior"; do
        if grep -q "## $required_section\|## .*$required_section" "$agent_file" 2>/dev/null; then
          pass "agents/$agent_name has '$required_section' section"
        else
          warn "agents/$agent_name missing '$required_section' section"
        fi
      done

      # Check line count (agents should be substantial, not stubs)
      line_count=$(wc -l < "$agent_file" | tr -d ' ')
      if [ "$line_count" -lt 50 ]; then
        warn "agents/$agent_name is only $line_count lines (may be a stub)"
      else
        pass "agents/$agent_name line count ok ($line_count)"
      fi

      # Check reference file cross-references
      grep -oE 'references/[a-z0-9_-]+\.md' "$agent_file" 2>/dev/null | sort -u | while read -r ref; do
        ref_path="$plugin_dir/$ref"
        if [ ! -f "$ref_path" ]; then
          fail "agents/$agent_name references '$ref' but file doesn't exist"
        fi
      done
    done
  fi

  # ============================================================
  # 5. HOOKS VALIDATION
  # ============================================================
  hooks_json="$plugin_dir/hooks/hooks.json"
  if [ -f "$hooks_json" ]; then
    python3 -c "
import json, os, sys

with open('$hooks_json') as f:
    data = json.load(f)

hooks = data.get('hooks', {})
valid_events = {
    'SessionStart', 'UserPromptSubmit', 'PreToolUse', 'PostToolUse',
    'PostToolUseFailure', 'PermissionRequest', 'Notification',
    'SubagentStart', 'SubagentStop', 'Stop', 'TeammateIdle',
    'TaskCompleted', 'InstructionsLoaded', 'ConfigChange',
    'WorktreeCreate', 'WorktreeRemove', 'PreCompact', 'SessionEnd'
}

for event in hooks:
    if event not in valid_events:
        print(f'INVALID_EVENT:{event}')
    else:
        print(f'VALID_EVENT:{event}')
    for hook_group in hooks[event]:
        for hook in hook_group.get('hooks', []):
            cmd = hook.get('command', '')
            if '\${CLAUDE_PLUGIN_ROOT}' in cmd:
                # Extract script path
                script = cmd.replace('bash \${CLAUDE_PLUGIN_ROOT}/', '').replace('python3 \${CLAUDE_PLUGIN_ROOT}/', '')
                script_path = os.path.join('$plugin_dir', script)
                if os.path.exists(script_path):
                    print(f'SCRIPT_OK:{script}')
                else:
                    print(f'SCRIPT_MISSING:{script}')
" 2>/dev/null | while IFS=: read -r status detail; do
      case "$status" in
        VALID_EVENT) pass "Hook event '$detail' is valid" ;;
        INVALID_EVENT) fail "Hook event '$detail' is not a valid Claude Code hook event" ;;
        SCRIPT_OK) pass "Hook script '$detail' exists" ;;
        SCRIPT_MISSING) fail "Hook script '$detail' referenced but not found" ;;
      esac
    done
  fi

  # ============================================================
  # 6. REFERENCE FILES HEALTH
  # ============================================================
  refs_dir="$plugin_dir/references"
  if [ -d "$refs_dir" ]; then
    for ref_file in "$refs_dir"/*.md; do
      [ ! -f "$ref_file" ] && continue
      ref_name=$(basename "$ref_file")
      line_count=$(wc -l < "$ref_file" | tr -d ' ')

      if [ "$line_count" -lt 10 ]; then
        warn "references/$ref_name is only $line_count lines (may be a stub)"
      else
        pass "references/$ref_name has content ($line_count lines)"
      fi

      # Check if any skill or agent actually references this file
      referenced=false
      for check_file in "$plugin_dir"/skills/*/SKILL.md "$plugin_dir"/agents/*.md; do
        [ ! -f "$check_file" ] && continue
        if grep -q "$ref_name" "$check_file" 2>/dev/null; then
          referenced=true
          break
        fi
      done
      if [ "$referenced" = "false" ]; then
        warn "references/$ref_name is not referenced by any skill or agent"
      fi
    done
  fi

done

# ============================================================
# 7. CROSS-PLUGIN CONSISTENCY
# ============================================================
section "Cross-Plugin Consistency"

# Check that shared skills (morning-brief, platform-setup, etc.) exist in all active plugins
ACTIVE_PLUGINS=()
for plugin_dir in "${PLUGIN_DIRS[@]}"; do
  pname=$(basename "$plugin_dir")
  [ "$pname" = "paid-search" ] && continue  # Skip deprecated
  [ "$pname" = "frontend-craft" ] && continue  # Skip non-paid-media
  ACTIVE_PLUGINS+=("$pname")
done

SHARED_SKILLS=("morning-brief" "platform-setup" "profile-review" "waste-detector" "account-scorecard")
for skill in "${SHARED_SKILLS[@]}"; do
  missing_from=()
  for pname in "${ACTIVE_PLUGINS[@]}"; do
    if [ ! -f "$PLUGINS_DIR/$pname/skills/$skill/SKILL.md" ]; then
      missing_from+=("$pname")
    fi
  done
  if [ ${#missing_from[@]} -eq 0 ]; then
    pass "Shared skill '$skill' exists in all active plugins"
  else
    warn "Shared skill '$skill' missing from: ${missing_from[*]}"
  fi
done

# Check hook structure consistency across paid media plugins
HOOK_EVENTS_EXPECTED=("SessionStart" "Stop" "PreCompact")
for pname in "${ACTIVE_PLUGINS[@]}"; do
  hooks_file="$PLUGINS_DIR/$pname/hooks/hooks.json"
  if [ -f "$hooks_file" ]; then
    for event in "${HOOK_EVENTS_EXPECTED[@]}"; do
      if python3 -c "
import json, sys
with open('$hooks_file') as f:
    data = json.load(f)
sys.exit(0 if '$event' in data.get('hooks', {}) else 1)
" 2>/dev/null; then
        pass "$pname has '$event' hook"
      else
        warn "$pname missing '$event' hook (expected for paid media plugins)"
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
