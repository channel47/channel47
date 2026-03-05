#!/bin/bash
set -euo pipefail

# channel47 Plugin Installer
# Usage: ./setup.sh [plugin-name|all]
# Or:    curl -fsSL https://raw.githubusercontent.com/channel47/plugins/main/setup.sh | bash

REPO_URL="https://github.com/channel47/plugins"
CLAUDE_DIR="$HOME/.claude"
PLUGIN_DIR="$CLAUDE_DIR/plugins"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}" 2>/dev/null || echo ".")" && pwd)"

# Available plugins
PLUGINS=("google-ads" "microsoft-ads" "meta-ads")

# Required env vars per plugin
declare -A REQUIRED_VARS
REQUIRED_VARS[google-ads]="GOOGLE_ADS_DEVELOPER_TOKEN GOOGLE_ADS_CLIENT_ID GOOGLE_ADS_CLIENT_SECRET GOOGLE_ADS_REFRESH_TOKEN"
REQUIRED_VARS[microsoft-ads]="BING_ADS_DEVELOPER_TOKEN BING_ADS_CLIENT_ID BING_ADS_CLIENT_SECRET BING_ADS_REFRESH_TOKEN"
REQUIRED_VARS[meta-ads]="META_ACCESS_TOKEN"

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

check_env_vars() {
  local plugin="$1"
  local vars="${REQUIRED_VARS[$plugin]}"
  local missing=()

  for var in $vars; do
    if [ -z "${!var:-}" ]; then
      missing+=("$var")
    fi
  done

  if [ ${#missing[@]} -gt 0 ]; then
    echo "  Warning: Missing environment variables for $plugin:"
    for var in "${missing[@]}"; do
      echo "    - $var"
    done
    echo "  Set these in ~/.zshrc or ~/.bashrc before using the plugin."
    echo ""
  fi
}

install_plugin() {
  local plugin="$1"
  local source_dir="$SCRIPT_DIR/plugins/$plugin"
  local dest_dir="$PLUGIN_DIR/channel47-$plugin"

  # Check if source exists (local install) or needs download
  if [ ! -d "$source_dir" ]; then
    echo "  Error: Plugin source not found at $source_dir"
    echo "  Run this script from the plugins repo root, or use:"
    echo "    /plugin marketplace add channel47/plugins"
    return 1
  fi

  # Remove existing install
  if [ -d "$dest_dir" ]; then
    rm -rf "$dest_dir"
  fi

  # Copy plugin
  cp -r "$source_dir" "$dest_dir"
  echo "  Installed: $plugin → $dest_dir"

  # Make hook scripts executable
  if [ -d "$dest_dir/hooks" ]; then
    chmod +x "$dest_dir/hooks/"*.sh 2>/dev/null || true
  fi

  # Check env vars
  check_env_vars "$plugin"
}

show_menu() {
  echo "  Which plugin(s) would you like to install?"
  echo ""
  echo "  1) google-ads      — Google Ads (9 skills)"
  echo "  2) microsoft-ads   — Microsoft Advertising (8 skills)"
  echo "  3) meta-ads        — Meta Ads / Facebook + Instagram (9 skills, 2 agents)"
  echo "  4) all             — Install all three"
  echo "  q) quit"
  echo ""
  read -rp "  Choose [1-4, q]: " choice

  case "$choice" in
    1) install_plugin "google-ads" ;;
    2) install_plugin "microsoft-ads" ;;
    3) install_plugin "meta-ads" ;;
    4)
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
  echo "    > /google-ads brief"
  echo "    > /microsoft-ads waste"
  echo "    > /meta-ads creative fatigue"
  echo ""
  echo "  First time? Start with:"
  echo "    > /google-ads setup"
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
