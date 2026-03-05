---
name: platform-setup
description: >-
  This skill should be used when the user asks to "connect to Microsoft Ads",
  "verify Bing connection", "configure my Bing Ads account",
  "check my Microsoft Advertising access", "set up Microsoft Ads",
  "connect my Bing account", "set up Bing Ads",
  "test my Bing API connection", "Microsoft Ads credentials",
  "first time Bing setup", "get started with Microsoft Ads plugin",
  or mentions Microsoft Ads setup, Bing connection verification,
  or credential configuration.
allowed-tools: mcp__bing-ads__list_accounts
---

# Platform Setup — Microsoft Ads

Configure Microsoft Advertising credentials for this plugin and verify account access.

## Workflow

### Step 1: Identify setup needs

- Use `references/bing-setup.md` for credential configuration.
- Use `references/config-patterns.md` for environment variable guidance.
- If the user already has credentials configured, skip to Step 3.

### Step 2: Microsoft Advertising setup

Guide the user through Azure app registration, developer token setup, OAuth credentials, and environment variable configuration from `references/bing-setup.md`.

Key items:
- Developer token from Microsoft Advertising Developer Portal.
- Azure App Registration for OAuth client ID.
- OAuth refresh token via the Microsoft identity platform.
- Customer ID and Account ID from the Microsoft Advertising UI.

Recommend `.claude/settings.local.json` (gitignored, project-scoped) as the primary credential store.

### Step 3: Verify Microsoft Advertising access

After env vars are configured, run `mcp__bing-ads__list_accounts` and report:

- Whether account listing succeeds.
- Which account IDs, names, and statuses are visible.
- Any missing env vars or auth failures that block access.

If verification fails, map the error to the specific missing or invalid variable and provide the fix.

Common failures:
- **Token expired**: Microsoft rotates refresh tokens on every token refresh. Re-run the OAuth flow to get a new BING_ADS_REFRESH_TOKEN.
- **Invalid client ID**: Verify the Azure App Registration application (client) ID.
- **Wrong customer/account ID**: Customer ID is the manager-level ID; Account ID is the specific ad account.

### Step 4: Summary

Summarize:

- Microsoft Advertising: [N] accounts accessible.
- Any credentials with missing or failed configuration.
- Next steps if verification failed.

### Step 5: Generate account profile

After verifying platform access:

1. Read `references/profile-template.md` as the base template.
2. Populate the **Accounts** table with discovered account IDs, names, and statuses from Step 3.
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
- This plugin is read-only. No account modifications are made during setup.

## References

- `references/bing-setup.md`
- `references/config-patterns.md`
- `references/profile-template.md`
