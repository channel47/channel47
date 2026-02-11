#!/usr/bin/env python3
"""
PreToolUse hook: Require explicit confirmation context for mutations.
Queries flow freely; mutations need user awareness.
"""
import json
import sys

def main():
    input_data = json.load(sys.stdin)
    tool_name = input_data.get("tool_name", "")

    # Only gate mutations
    if "mutate" not in tool_name.lower():
        # Allow all non-mutation tools
        print(json.dumps({"decision": "allow"}))
        return

    tool_input = input_data.get("tool_input", {})
    dry_run = tool_input.get("dry_run", True)

    if dry_run:
        # Dry run mutations are safe - allow
        print(json.dumps({"decision": "allow"}))
    else:
        # Live mutations need acknowledgment in decision
        # Hook passes but adds context reminder
        print(json.dumps({
            "decision": "allow",
            "message": "LIVE MUTATION: dry_run=false. Changes will be permanent."
        }))

if __name__ == "__main__":
    main()
