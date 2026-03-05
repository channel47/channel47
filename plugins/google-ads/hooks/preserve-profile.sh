#!/bin/bash
set -euo pipefail
# PreCompact hook: preserve account profile through context compaction
# Two actions: (1) output profile as systemMessage, (2) save insights to disk

input=$(cat)

PROFILE_PATH="${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md"
if [ ! -f "$PROFILE_PATH" ]; then exit 0; fi

# Save in-flight insights to disk before compaction
echo "$input" | python3 "${CLAUDE_PLUGIN_ROOT}/hooks/update-profile.py" 2>/dev/null || true

# Output profile as systemMessage so it's fresh in context before summarizer runs
profile_content=$(cat "$PROFILE_PATH")
jq -n --arg msg "$profile_content" '{
  "systemMessage": $msg
}'
