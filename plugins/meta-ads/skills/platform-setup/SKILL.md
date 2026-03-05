---
name: platform-setup
description: >-
  This skill should be used when the user asks to "connect to Meta Ads",
  "set up Facebook Ads", "configure Instagram Ads", "verify Meta connection",
  "set up my Meta ad account", "check my Meta Ads access", "test Meta API",
  "first time Meta setup", "get started with Meta Ads plugin",
  "Meta Ads onboarding", "Meta Ads credentials",
  or mentions Meta Ads setup, connection verification,
  or credential configuration.
allowed-tools: mcp__meta-ads__get_ad_accounts, mcp__meta-ads__verify_account_setup, mcp__meta-ads__health_check
---

# Platform Setup

Configure Meta Ads credentials and verify account access via the brijr/meta-mcp server.

## Prerequisites

The user needs:
1. A Meta Business Manager account with ad account access.
2. A long-lived Meta access token with `ads_read` permission.

No app ID or app secret required — brijr/meta-mcp uses a single access token.

## Workflow

### Step 1: Check environment variable

Verify that `META_ACCESS_TOKEN` is set. Do NOT ask the user to paste it into chat.

If not set, guide them:
1. Go to https://developers.facebook.com/tools/explorer/
2. Select their app (or create one).
3. Under Permissions, add `ads_read`, `ads_management` (read scope only), `read_insights`.
4. Generate a long-lived token (User or System User token recommended for durability).
5. Add to shell profile (`~/.zshrc` or `~/.bashrc`):
   ```bash
   export META_ACCESS_TOKEN="your-token-here"
   ```
6. Restart Claude Code (or `source ~/.zshrc`).

### Step 2: Verify API access

Run `mcp__meta-ads__health_check` to confirm the MCP server is responding.

Then run `mcp__meta-ads__get_ad_accounts` and report:
- Whether account listing succeeds.
- Which ad account IDs and names are visible.
- Account status (ACTIVE, DISABLED, etc.).
- Currency and timezone for each account.

If access fails, diagnose:
- Token expired? Guide to token refresh.
- Missing permissions? List required permissions.
- Account not visible? Check Business Manager roles.

### Step 3: Verify account setup details

For each discovered account, run `mcp__meta-ads__verify_account_setup` to check:
- Pixel / Conversions API (CAPI) configuration.
- Payment method status.
- Account spending limit.
- Business verification status.

Report any missing or misconfigured items.

### Step 4: Generate account profile

After verifying platform access:

1. Read `references/profile-template.md` as the base template.
2. Populate the **Accounts** table with discovered account IDs, names, pixel IDs, and statuses from Steps 2-3.
3. Ask the user for their KPI targets:
   - Target CPA and hard ceiling
   - Target ROAS and minimum acceptable
   - CPM ceiling (by objective if known)
   - Frequency cap (7d and 30d)
   - Monthly budget
4. Ask about:
   - Primary conversion event(s) (Purchase, Lead, AddToCart, etc.)
   - Attribution window (default: 7-day click / 1-day view)
   - Active creative or audience tests
   - Campaigns to exclude from analysis (e.g., awareness-only)
   - Preferences for reporting currency, alert sensitivity
5. Write the populated profile to `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md`.
6. Confirm the profile was saved and explain that all analysis skills (morning-brief, waste-detector, creative-fatigue, etc.) will read it automatically on each session start.

If the profile already exists, ask whether to overwrite or merge new account data into the existing profile.

## Output

```
## Platform Setup - Complete

### Accounts Discovered
| Account Name | Account ID | Status | Currency | Timezone | Pixel |
|---|---|---|---|---|---|

### Setup Checklist
- [x] META_ACCESS_TOKEN configured
- [x] MCP server responding (health_check)
- [x] Ad accounts accessible
- [x] Pixel/CAPI verified
- [x] Account profile generated

### Next Steps
- Run `/morning-brief` for your first daily health check.
- Run `/waste-detector` for a full spend audit.
- Run `/creative-fatigue` to assess creative lifecycle health.
```

## Guardrails

- Never ask users to paste secrets into chat logs.
- Recommend shell profile (`~/.zshrc`) for the token — it stays out of git.
- Do not store tokens in `.claude/settings.local.json` or any file that could be committed.

## References

- `references/profile-template.md` — Account profile template
