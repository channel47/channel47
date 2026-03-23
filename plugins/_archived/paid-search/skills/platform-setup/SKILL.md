---
name: platform-setup
description: >-
  This skill should be used when the user asks to "connect to Google Ads",
  "set up Bing", "verify connection", "configure my search ad accounts",
  "set up Microsoft Advertising", "check my paid search access", or
  "connect my paid search platforms".
allowed-tools: mcp__google-ads__list_accounts, mcp__bing-ads__list_accounts
---

# Platform Setup

Configure Google Ads and Bing Ads credentials for this plugin and verify account access.

## Workflow

### Step 1: Identify setup target

- If the user asks about Google Ads setup or verification, use `references/google-setup.md`.
- If the user asks about Bing setup, use `references/bing-setup.md`.
- If the user asks to set up both or "all platforms", run both flows.
- Use `references/config-patterns.md` for shared environment variable guidance.

### Step 2: Google Ads setup

Guide the user through OAuth credentials, developer token setup, and shell env var configuration from `references/google-setup.md`.

### Step 3: Verify Google Ads access

After env vars are configured, run `mcp__google-ads__list_accounts` and report:

- Whether account listing succeeds
- Which customer IDs are visible
- Any missing env vars or auth failures that block access

### Step 4: Bing Ads setup

Guide the user through Azure app registration, developer token, and OAuth credential setup from `references/bing-setup.md`.

### Step 5: Verify Bing Ads access

After env vars are configured, run `mcp__bing-ads__list_accounts` and report:

- Whether account listing succeeds
- Which account IDs, names, and statuses are visible
- Any missing env vars or auth failures that block access

### Step 6: Cross-platform summary

If both platforms are configured, summarize:

- Google Ads: [N] accounts accessible
- Bing Ads: [N] accounts accessible
- Any platforms with missing or failed credentials

### Step 7: Generate account profile

After verifying platform access:

1. Read `references/profile-template.md` as the base template.
2. Populate the **Accounts** table with discovered account IDs, names, and statuses from Steps 3 and 5.
3. Ask the user for their KPI targets (CPA, ROAS, monthly budget) and fill the **Targets** table.
4. Ask about any active tests, conversion actions, attribution model, and preferences.
5. Write the populated profile to `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md`.
6. Confirm the profile was saved and explain that analysis skills (morning-brief, waste-detector, etc.) will read it automatically on each run.

If the profile already exists, ask whether to overwrite or merge new account data into the existing profile.

## Cowork compatibility

- **Claude Code / Codex**: Full API access via MCP tools.
- **Claude Cowork**: MCP servers are expected to work via passthrough. Verify by running `/setup` in your Cowork session.

## Guardrails

- Never ask users to paste secrets into chat logs.
- Recommend `.claude/settings.local.json` (gitignored, project-scoped) for credentials. Shell env vars are an alternative.
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
