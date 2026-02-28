#!/usr/bin/env python3
"""
PreToolUse hook: Flag live mutations before execution.

Checks mcp__meta-ads__mutate calls for dry_run parameter.
Queries and dry-run mutations pass through silently.
"""
import json
import sys


def main():
    input_data = json.load(sys.stdin)
    tool_name = input_data.get("tool_name", "")
    tool_input = input_data.get("tool_input", {})

    if "mutate" in tool_name.lower():
        if not tool_input.get("dry_run", True):
            print(json.dumps({
                "decision": "allow",
                "message": "LIVE MUTATION: dry_run=false. Changes will be permanent."
            }))
            return
        print(json.dumps({"decision": "allow"}))
        return

    print(json.dumps({"decision": "allow"}))


if __name__ == "__main__":
    main()
