#!/bin/bash
set -euo pipefail

# SessionStart hook: inject account profile into context
# Reads profile/account-profile.md and returns as additionalContext
# so every skill and ad-hoc conversation has account context automatically.

input=$(cat)

# Skip on compact — profile already in context
source=$(echo "$input" | jq -r '.source // ""')
if [ "$source" = "compact" ]; then
  exit 0
fi

PROFILE_PATH="${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md"

# If profile doesn't exist, exit silently — no error, no context injected
if [ ! -f "$PROFILE_PATH" ]; then
  exit 0
fi

# Read profile and escape for JSON
profile_content=$(cat "$PROFILE_PATH")

# Output as additionalContext via hookSpecificOutput
jq -n --arg content "$profile_content" '{
  "hookSpecificOutput": {
    "hookEventName": "SessionStart",
    "additionalContext": $content
  }
}'
