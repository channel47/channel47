---
name: platform-setup
description: >-
  This skill should be used when the user asks to "connect to Meta Ads",
  "set up Facebook Ads", "configure Instagram Ads", "verify Meta connection",
  "set up my Meta ad account", or "check my Meta Ads access".
allowed-tools: mcp__meta-ads__list_accounts
---

# Platform Setup

Configure Meta Ads credentials and verify account access.

## Status

Skeleton — requires `@channel47/meta-ads-mcp` to be built and published before this skill is functional.

## Workflow

### Step 1: Identify setup requirements

Guide the user through:
- Meta Business Manager account access
- App creation in Meta for Developers
- Access token generation (long-lived token)
- Pixel and Conversions API (CAPI) verification

### Step 2: Configure environment variables

Set in `.claude/settings.local.json` or shell profile:
- `META_ADS_ACCESS_TOKEN`
- `META_ADS_APP_ID`
- `META_ADS_APP_SECRET`
- `META_ADS_ACCOUNT_ID`

### Step 3: Verify access

Run `mcp__meta-ads__list_accounts` and report:
- Whether account listing succeeds
- Which ad account IDs and names are visible
- Any missing credentials or auth failures

### Step 4: Generate account profile

After verifying platform access:

1. Read `references/profile-template.md` as the base template.
2. Populate the **Accounts** table with discovered account IDs, names, pixel IDs, and statuses from Step 3.
3. Ask the user for their KPI targets (CPA, ROAS, CPM ceiling, frequency cap, monthly budget) and fill the **Targets** table.
4. Ask about active creative/audience tests, conversion events, attribution window, and preferences.
5. Write the populated profile to `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md`.
6. Confirm the profile was saved and explain that analysis skills (morning-brief, waste-detector, etc.) will read it automatically on each run.

If the profile already exists, ask whether to overwrite or merge new account data into the existing profile.

## Guardrails

- Never ask users to paste secrets into chat logs.
- Recommend `.claude/settings.local.json` (gitignored) for credentials.

## References

- `references/` — to be populated when MCP server is built
