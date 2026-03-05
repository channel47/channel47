#!/bin/bash
# Check MCP server package versions against npm latest
set -uo pipefail

REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"

echo "Checking MCP package versions..."
echo ""

for mcp in "$REPO_ROOT"/plugins/*/.mcp.json; do
  [ ! -f "$mcp" ] && continue
  plugin=$(basename "$(dirname "$mcp")")

  # Skip deprecated plugins
  [ -f "$(dirname "$mcp")/DEPRECATED.md" ] && continue

  python3 -c "
import json, subprocess, re
with open('$mcp') as f:
    data = json.load(f)
for name, config in data.items():
    args = config.get('args', [])
    pkg = None
    for arg in args:
        if '@' in arg and not arg.startswith('-'):
            pkg = arg
            break
    if not pkg:
        continue
    # Parse package name and version (handle scoped packages)
    if pkg.startswith('@'):
        m = re.match(r'^(@[^@]+)@(.+)$', pkg)
    else:
        m = re.match(r'^(.+?)@(.+)$', pkg)
    if m:
        pkg_name, pinned = m.group(1), m.group(2)
        try:
            result = subprocess.run(['npm', 'view', pkg_name, 'version'],
                capture_output=True, text=True, timeout=10)
            latest = result.stdout.strip()
            if latest:
                print(f'  $plugin: {pkg_name}  pinned: {pinned}  latest: {latest}')
            else:
                print(f'  $plugin: {pkg_name}  pinned: {pinned}  latest: (not found on npm)')
        except Exception:
            print(f'  $plugin: {pkg_name}  pinned: {pinned}  latest: (check failed)')
"
done
