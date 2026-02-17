---
name: platform-setup
description: >-
  This skill should be used when the user asks to "connect to Google Ads",
  "set up Bing", "verify connection", "configure my ad accounts", "set up
  Microsoft Advertising", or "check my ad platform access".
allowed-tools: mcp__google-ads__list_accounts
---

# Platform Setup

Configure Google Ads and Bing Ads credentials for this plugin and verify account access.

## Workflow

### Step 1: Identify setup target

- If the user asks about Google Ads setup or verification, use `references/google-setup.md`.
- If the user asks about Bing setup, use `references/bing-setup.md`.
- Use `references/config-patterns.md` for shared environment variable guidance.

### Step 2: Google Ads setup

Guide the user through OAuth credentials, developer token setup, and shell env var configuration from `references/google-setup.md`.

### Step 3: Verify Google Ads access

After env vars are configured, run `mcp__google-ads__list_accounts` and report:

- Whether account listing succeeds
- Which customer IDs are visible
- Any missing env vars or auth failures that block access

### Step 4: Bing setup guidance

Provide Bing setup instructions from `references/bing-setup.md` and explicitly note current status:

- Bing credential instructions are available now
- Bing MCP execution tooling is a placeholder until the Bing MCP server is added

## Cowork compatibility

- **Claude Code / Codex**: Full API access via MCP tools.
- **Claude Cowork**: Full API access via MCP passthrough (MCP servers run on your Desktop, not in the VM).

## Guardrails

- Never ask users to paste secrets into chat logs.
- Prefer environment variables over local JSON credential files.
- For failed verification, report the exact missing variable or auth step.

## References

- `references/google-setup.md`
- `references/bing-setup.md`
- `references/config-patterns.md`
- `references/google-shopping-campaigns.md`
- `references/bing-campaign-management.md`
- `references/bing-shopping-campaigns.md`
- `references/bing-content-api.md`
- `references/bing-bulk-operations.md`
- `references/bing-reporting.md`
