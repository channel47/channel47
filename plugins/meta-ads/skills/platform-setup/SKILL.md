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

## Guardrails

- Never ask users to paste secrets into chat logs.
- Recommend `.claude/settings.local.json` (gitignored) for credentials.

## References

- `references/` — to be populated when MCP server is built
