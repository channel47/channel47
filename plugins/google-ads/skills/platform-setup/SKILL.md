---
name: platform-setup
description: >-
  This skill should be used when the user asks to "connect to Google Ads",
  "verify connection", "configure my Google Ads account",
  "check my Google Ads access", "set up Google Ads",
  "connect my ad account", "test my API connection",
  "Google Ads credentials", "first time setup", "onboarding",
  "get started with Google Ads plugin",
  or mentions Google Ads setup, connection verification,
  or credential configuration.
allowed-tools: mcp__google-ads__list_accounts
---

# Platform Setup — Google Ads

Configure Google Ads credentials for this plugin and verify account access.

## Workflow

### Step 1: Identify setup needs

- Use `references/google-setup.md` for credential configuration.
- Use `references/config-patterns.md` for environment variable guidance.
- If the user already has credentials configured, skip to Step 3.

### Step 2: Google Ads setup

Guide the user through OAuth credentials, developer token setup, and environment variable configuration from `references/google-setup.md`.

Key items:
- Developer token from Google Ads API Center.
- OAuth client ID and secret from Google Cloud Console.
- OAuth refresh token for the API user.
- Manager account (MCC) customer ID without hyphens.

Recommend `.claude/settings.local.json` (gitignored, project-scoped) as the primary credential store.

### Step 3: Verify Google Ads access

After env vars are configured, run `mcp__google-ads__list_accounts` and report:

- Whether account listing succeeds.
- Which customer IDs and account names are visible.
- Any missing env vars or auth failures that block access.

If verification fails, map the error to the specific missing or invalid variable and provide the fix.

### Step 4: Summary

Summarize:

- Google Ads: [N] accounts accessible.
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

- `references/google-setup.md`
- `references/config-patterns.md`
- `references/profile-template.md`
