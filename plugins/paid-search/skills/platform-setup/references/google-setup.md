# Google Ads Setup

Use this guide to configure Google Ads access for the plugin's bundled MCP server.

## Required environment variables

Add these to `.claude/settings.local.json` in your project root (gitignored by default):

```json
{
  "env": {
    "GOOGLE_ADS_DEVELOPER_TOKEN": "your_developer_token",
    "GOOGLE_ADS_CLIENT_ID": "your_oauth_client_id",
    "GOOGLE_ADS_CLIENT_SECRET": "your_oauth_client_secret",
    "GOOGLE_ADS_REFRESH_TOKEN": "your_refresh_token",
    "GOOGLE_ADS_LOGIN_CUSTOMER_ID": "your_mcc_customer_id_without_hyphens"
  }
}
```

Alternatively, set them in your shell profile (`~/.zshrc`, `~/.bashrc`). Restart Claude Code after changing either.

## Credential sources

- `GOOGLE_ADS_DEVELOPER_TOKEN`: Google Ads API Center token
- `GOOGLE_ADS_CLIENT_ID` and `GOOGLE_ADS_CLIENT_SECRET`: OAuth app credentials from Google Cloud Console
- `GOOGLE_ADS_REFRESH_TOKEN`: OAuth refresh token for the API user
- `GOOGLE_ADS_LOGIN_CUSTOMER_ID`: manager account ID used as login customer ID

## Verification flow

1. Confirm all required env vars are set (in `.claude/settings.local.json` or shell environment).
2. Run `mcp__google-ads__list_accounts`.
3. If successful, capture visible account IDs and names.
4. If failed, report the exact auth error and map it to the missing/invalid variable.

## Common issues

- Customer IDs with hyphens: use digits only.
- Wrong OAuth project: ensure the refresh token was issued for the same client ID.
- Missing API access: confirm developer token status in API Center.
