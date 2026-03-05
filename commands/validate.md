---
name: validate
description: Validate plugin suite structure, cross-file references, and spec compliance
allowed-tools: Bash
---

# Plugin Suite Validator

Run the validation script to check structural consistency across all plugins.

## Steps

1. Run `bash validate.sh` from the repo root (`$CLAUDE_PROJECT_ROOT` or the plugins directory).
2. If a plugin name is provided as an argument (e.g., `/validate google-ads`), pass it to the script: `bash validate.sh google-ads`.
3. Review the output — fix any errors (red), investigate warnings (yellow).
4. If errors are found, fix them and re-run validation to confirm.

## What It Checks

- Marketplace registry consistency (entries match directories, versions synced)
- Plugin structure (required files: plugin.json, .mcp.json, hooks.json, etc.)
- Skill frontmatter (name matches directory, description length 60-80 words, allowed-tools present)
- Agent frontmatter (uses `tools:` not `allowed-tools:`, has Output Schema and Fallback sections)
- Hook validity (valid event names, referenced scripts exist)
- Reference file health (not stubs, actually referenced by skills/agents)
- Cross-file references (skills referencing references/ and agents/ that exist)
- Read-only constraint (no mutation tools in allowed-tools)
- MCP config (no hardcoded secrets, required fields present)
- Cross-plugin consistency (shared skills exist everywhere, hook structure uniform)
