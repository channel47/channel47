---
name: validate
description: Validate plugin suite structure and spec compliance
allowed-tools: Bash
---

# Plugin Suite Validator

Run the validation script to check structural consistency across all plugins.

## Steps

1. Run `bash validate.sh` from the repo root.
2. If a plugin name is provided as an argument (e.g., `/validate dtc-google-ads-playbook`), pass it to the script: `bash validate.sh dtc-google-ads-playbook`.
3. Review the output — fix any errors (red), investigate warnings (yellow).

## What It Checks

- Marketplace registry consistency (entries match directories, versions synced)
- Plugin structure (required files: plugin.json, README.md)
- Skill frontmatter (name, description present)
- Command files exist
- Agent frontmatter (uses `tools:` not `allowed-tools:`, has name and description)
- Reference file cross-references (skills referencing files that exist)
