# Bing Setup

Configure Microsoft Advertising credentials for the Bing Ads MCP server.

## Required environment variables

Add these to `.claude/settings.local.json` in your project root (gitignored by default):

```json
{
  "env": {
    "BING_ADS_DEVELOPER_TOKEN": "your_developer_token",
    "BING_ADS_CLIENT_ID": "your_azure_app_client_id",
    "BING_ADS_CLIENT_SECRET": "your_azure_app_client_secret",
    "BING_ADS_REFRESH_TOKEN": "your_refresh_token",
    "BING_ADS_CUSTOMER_ID": "your_manager_customer_id",
    "BING_ADS_ACCOUNT_ID": "your_default_account_id"
  }
}
```

Omit `BING_ADS_CLIENT_SECRET` for public client apps. Alternatively, set these in your shell profile (`~/.zshrc`, `~/.bashrc`). Restart Claude Code after changing either.

## Credential sources

| Variable | Required | Where to get it |
|----------|----------|----------------|
| `BING_ADS_DEVELOPER_TOKEN` | Yes | Microsoft Advertising Developer Portal → Account Settings → Developer Token |
| `BING_ADS_CLIENT_ID` | Yes | Azure Portal → App Registrations → your app → Application (client) ID |
| `BING_ADS_CLIENT_SECRET` | Confidential clients only | Azure Portal → App Registrations → Certificates & secrets → New client secret |
| `BING_ADS_REFRESH_TOKEN` | Yes | OAuth2 flow with scope `https://ads.microsoft.com/msads.manage offline_access` |
| `BING_ADS_CUSTOMER_ID` | Yes | Microsoft Advertising UI → top-right account dropdown → Customer ID |
| `BING_ADS_ACCOUNT_ID` | Yes | Microsoft Advertising UI → Accounts Summary → Account Number column |

**Public client apps** (registered without a client secret) can omit `BING_ADS_CLIENT_SECRET`. The MCP server detects the absence of the env var and uses the public client OAuth flow automatically.

## Azure app registration

1. Go to [Azure Portal → App Registrations](https://portal.azure.com/#blade/Microsoft_AAD_RegisteredApps/ApplicationsListBlade).
2. Click "New registration".
3. Name: anything (e.g., "Bing Ads MCP").
4. Supported account types: "Accounts in any organizational directory and personal Microsoft accounts".
5. Redirect URI: `http://localhost` (for the OAuth flow).
6. After creation, copy the Application (client) ID → `BING_ADS_CLIENT_ID`.
7. Go to Certificates & secrets → New client secret → copy the value → `BING_ADS_CLIENT_SECRET`.

## Token rotation

Microsoft rotates refresh tokens on every token refresh. The Bing MCP server handles this automatically within a session, but the initial `BING_ADS_REFRESH_TOKEN` env var must be valid at startup. If sessions expire between uses, re-run the OAuth flow to get a fresh refresh token.

## Verification

After setting env vars, verify access by running `mcp__bing-ads__list_accounts`. This should return:

- Account IDs, names, and statuses
- Active vs paused accounts

If verification fails, check:

1. Required env vars are set: `DEVELOPER_TOKEN`, `CLIENT_ID`, `REFRESH_TOKEN` (and `CLIENT_SECRET` for confidential client apps)
2. The refresh token hasn't expired (re-run OAuth flow if needed)
3. The Azure app has the correct redirect URI and API permissions
