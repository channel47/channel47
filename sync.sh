#!/bin/bash
# Channel47 Plugin Suite Sync
# Regenerates marketplace.json from plugin.json files (source of truth).
# Also verifies skill counts in plugin descriptions match reality.
#
# Usage: bash sync.sh [--dry-run]
#   --dry-run  Show what would change without writing files

set -uo pipefail

REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
PLUGINS_DIR="$REPO_ROOT/plugins"
MARKETPLACE="$REPO_ROOT/.claude-plugin/marketplace.json"
DRY_RUN=false

if [ "${1:-}" = "--dry-run" ]; then
  DRY_RUN=true
fi

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}Channel47 Plugin Sync${NC}"

# Build marketplace.json from plugin.json files
python3 -c "
import json, os, glob, re, sys

repo_root = '$REPO_ROOT'
plugins_dir = '$PLUGINS_DIR'
marketplace_path = '$MARKETPLACE'
dry_run = $( [ "$DRY_RUN" = "true" ] && echo "True" || echo "False" )

# Read existing marketplace for metadata preservation
with open(marketplace_path) as f:
    existing = json.load(f)

# Collect all plugin data from plugin.json files (source of truth)
plugins = []
for plugin_json_path in sorted(glob.glob(os.path.join(plugins_dir, '*/.claude-plugin/plugin.json'))):
    plugin_dir = os.path.dirname(os.path.dirname(plugin_json_path))
    plugin_name = os.path.basename(plugin_dir)

    with open(plugin_json_path) as f:
        pj = json.load(f)

    # Count actual skills
    skills_dir = os.path.join(plugin_dir, 'skills')
    skill_count = 0
    if os.path.isdir(skills_dir):
        for d in os.listdir(skills_dir):
            if os.path.isfile(os.path.join(skills_dir, d, 'SKILL.md')):
                skill_count += 1

    # Check if deprecated
    deprecated = os.path.isfile(os.path.join(plugin_dir, 'DEPRECATED.md'))

    # Find existing entry for preserved fields (category, tags, replacedBy)
    existing_entry = next((p for p in existing.get('plugins', []) if p['name'] == plugin_name), {})

    # Verify skill count in description matches reality
    desc = pj.get('description', '')
    desc_match = re.search(r'(\d+)\s+skills?', desc)
    claimed_skills = int(desc_match.group(1)) if desc_match else 0

    if claimed_skills > 0 and claimed_skills != skill_count:
        print(f'SKILL_COUNT_MISMATCH:{plugin_name}:{claimed_skills}:{skill_count}', file=sys.stderr)
        # Auto-fix the description
        desc = re.sub(r'\d+\s+skills?', f'{skill_count} skills', desc)

    entry = {
        'name': plugin_name,
        'source': f'./plugins/{plugin_name}',
        'description': desc,
        'version': pj.get('version', '0.0.0'),
        'category': existing_entry.get('category', 'marketing'),
        'tags': existing_entry.get('tags', pj.get('keywords', []))
    }

    if deprecated:
        entry['deprecated'] = True
        if 'replacedBy' in existing_entry:
            entry['replacedBy'] = existing_entry['replacedBy']

    plugins.append(entry)

# Build final marketplace
marketplace = {
    'name': existing.get('name', 'channel47'),
    'owner': existing.get('owner', {}),
    'metadata': existing.get('metadata', {}),
    'plugins': plugins
}

# Compare with existing
existing_json = json.dumps(existing, indent=2, ensure_ascii=False)
new_json = json.dumps(marketplace, indent=2, ensure_ascii=False)

if existing_json == new_json:
    print('NO_CHANGES', file=sys.stderr)
else:
    # Show diff summary
    old_versions = {p['name']: p.get('version') for p in existing.get('plugins', [])}
    new_versions = {p['name']: p.get('version') for p in plugins}

    for name in sorted(set(list(old_versions.keys()) + list(new_versions.keys()))):
        old_v = old_versions.get(name)
        new_v = new_versions.get(name)
        if old_v is None:
            print(f'ADDED:{name}:{new_v}', file=sys.stderr)
        elif new_v is None:
            print(f'REMOVED:{name}', file=sys.stderr)
        elif old_v != new_v:
            print(f'VERSION_CHANGED:{name}:{old_v}:{new_v}', file=sys.stderr)

    old_descs = {p['name']: p.get('description', '') for p in existing.get('plugins', [])}
    new_descs = {p['name']: p.get('description', '') for p in plugins}
    for name in new_descs:
        if name in old_descs and old_descs[name] != new_descs[name]:
            print(f'DESC_CHANGED:{name}', file=sys.stderr)

    if not dry_run:
        with open(marketplace_path, 'w') as f:
            f.write(new_json + '\n')
        print('WRITTEN', file=sys.stderr)
    else:
        print('DRY_RUN', file=sys.stderr)
" 2>&1 | while IFS=: read -r status a b c; do
  case "$status" in
    NO_CHANGES)
      echo -e "  ${GREEN}ok${NC} marketplace.json is in sync" ;;
    WRITTEN)
      echo -e "  ${GREEN}ok${NC} marketplace.json updated" ;;
    DRY_RUN)
      echo -e "  ${YELLOW}!!${NC} marketplace.json would be updated (dry-run)" ;;
    ADDED)
      echo -e "  ${CYAN}+${NC} New plugin: $a (v$b)" ;;
    REMOVED)
      echo -e "  ${RED}-${NC} Removed plugin: $a" ;;
    VERSION_CHANGED)
      echo -e "  ${YELLOW}~${NC} $a: version $b -> $c" ;;
    DESC_CHANGED)
      echo -e "  ${YELLOW}~${NC} $a: description updated" ;;
    SKILL_COUNT_MISMATCH)
      echo -e "  ${YELLOW}!!${NC} $a: description claims $b skills but found $c (auto-fixed)" ;;
    *)
      [ -n "$status" ] && echo "  $status $a $b $c" ;;
  esac
done

echo ""
if [ "$DRY_RUN" = "true" ]; then
  echo -e "${YELLOW}Dry run complete. Run without --dry-run to apply changes.${NC}"
else
  echo -e "${GREEN}Sync complete.${NC}"
fi
