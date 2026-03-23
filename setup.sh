#!/bin/bash
set -euo pipefail

# channel47 Plugin Installer
# Usage: ./setup.sh [plugin-name|all]

CLAUDE_DIR="$HOME/.claude"
PLUGIN_DIR="$CLAUDE_DIR/plugins"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}" 2>/dev/null || echo ".")" && pwd)"

# Available plugins
PLUGINS=("dtc-google-ads-playbook" "dtc-research-engine")

print_header() {
  echo ""
  echo "  channel47 Plugin Installer"
  echo "  =========================="
  echo ""
}

check_claude() {
  if [ ! -d "$CLAUDE_DIR" ]; then
    echo "Error: Claude Code not found (~/.claude/ directory missing)."
    echo "Install Claude Code first: https://claude.ai/download"
    exit 1
  fi
  mkdir -p "$PLUGIN_DIR"
}

install_plugin() {
  local plugin="$1"
  local source_dir="$SCRIPT_DIR/plugins/$plugin"
  local dest_dir="$PLUGIN_DIR/channel47-$plugin"

  if [ ! -d "$source_dir" ]; then
    echo "  Error: Plugin source not found at $source_dir"
    echo "  Run this script from the plugins repo root."
    return 1
  fi

  # Remove existing install
  if [ -d "$dest_dir" ]; then
    rm -rf "$dest_dir"
  fi

  # Copy plugin
  cp -r "$source_dir" "$dest_dir"
  echo "  Installed: $plugin -> $dest_dir"
}

show_menu() {
  echo "  Which plugin(s) would you like to install?"
  echo ""
  echo "  1) dtc-google-ads-playbook  — Google Ads playbook for DTC brands (3 skills, 3 commands, 1 agent)"
  echo "  2) dtc-research-engine      — Customer research to ad creative pipeline (5 skills, 6 commands, 1 agent)"
  echo "  3) all                      — Install both"
  echo "  q) quit"
  echo ""
  read -rp "  Choose [1-3, q]: " choice

  case "$choice" in
    1) install_plugin "dtc-google-ads-playbook" ;;
    2) install_plugin "dtc-research-engine" ;;
    3)
      for plugin in "${PLUGINS[@]}"; do
        install_plugin "$plugin"
      done
      ;;
    q|Q) echo "  Cancelled."; exit 0 ;;
    *) echo "  Invalid choice."; exit 1 ;;
  esac
}

print_success() {
  echo ""
  echo "  Done! Try it now:"
  echo ""
  echo "    claude"
  echo "    > /campaign-audit [paste your Google Ads data]"
  echo "    > /research [product name]"
  echo "    > /full-pipeline [product name]"
  echo ""
}

# Main
print_header
check_claude

if [ $# -eq 0 ]; then
  show_menu
elif [ "$1" = "all" ]; then
  for plugin in "${PLUGINS[@]}"; do
    install_plugin "$plugin"
  done
else
  if [[ " ${PLUGINS[*]} " =~ " $1 " ]]; then
    install_plugin "$1"
  else
    echo "  Unknown plugin: $1"
    echo "  Available: ${PLUGINS[*]}"
    exit 1
  fi
fi

print_success
