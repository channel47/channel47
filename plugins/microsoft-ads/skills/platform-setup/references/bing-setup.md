# Microsoft Advertising Setup

Configure Microsoft Advertising credentials for the plugin's bundled MCP server.

## Required environment variables

Add these to `.claude/settings.local.json` in your project root (gitignored by default):

```json
{
  "env": {
    "BING_ADS_DEVELOPER_TOKEN": "your_developer_token",
    "BING_ADS_CLIENT_ID": "your_azure_app_client_id",
    "BING_ADS_REFRESH_TOKEN": "your_refresh_token",
    "BING_ADS_CUSTOMER_ID": "your_manager_customer_id",
    "BING_ADS_ACCOUNT_ID": "your_default_account_id"
  }
}
```

## Credential sources

| Variable | Required | Where to get it |
|----------|----------|----------------|
| BING_ADS_DEVELOPER_TOKEN | Yes | Microsoft Advertising Developer Portal > Account Settings > Developer Token |
| BING_ADS_CLIENT_ID | Yes | Azure Portal > App Registrations > your app > Application (client) ID |
| BING_ADS_REFRESH_TOKEN | Yes | OAuth2 flow with scope `https://ads.microsoft.com/msads.manage offline_access` |
| BING_ADS_CUSTOMER_ID | Yes | Microsoft Advertising UI > top-right account dropdown > Customer ID |
| BING_ADS_ACCOUNT_ID | Yes | Microsoft Advertising UI > Accounts Summary > Account Number column |

## Azure app registration

1. Go to Azure Portal > App Registrations.
2. Click "New registration".
3. Name: anything (e.g., "Bing Ads MCP").
4. Supported account types: "Accounts in any organizational directory and personal Microsoft accounts".
5. Redirect URI: http://localhost (for OAuth flow).
6. Copy Application (client) ID > BING_ADS_CLIENT_ID.

## OAuth flow

1. Construct the authorization URL:
   ```
   https://login.microsoftonline.com/common/oauth2/v2.0/authorize?
     client_id={BING_ADS_CLIENT_ID}
     &response_type=code
     &redirect_uri=http://localhost
     &scope=https://ads.microsoft.com/msads.manage offline_access
   ```
2. Open in a browser, sign in with your Microsoft Advertising account.
3. After consent, you'll be redirected to `http://localhost?code={authorization_code}`.
4. Exchange the code for tokens:
   ```bash
   curl -X POST https://login.microsoftonline.com/common/oauth2/v2.0/token \
     -d "client_id={BING_ADS_CLIENT_ID}" \
     -d "grant_type=authorization_code" \
     -d "code={authorization_code}" \
     -d "redirect_uri=http://localhost" \
     -d "scope=https://ads.microsoft.com/msads.manage offline_access"
   ```
5. Copy `refresh_token` from the response > BING_ADS_REFRESH_TOKEN.

## Token rotation

Microsoft rotates refresh tokens on every token refresh. The Bing MCP server handles this within a session, but BING_ADS_REFRESH_TOKEN must be valid at startup. Re-run OAuth flow if sessions expire.

## Finding your Customer ID and Account ID

1. Sign in to Microsoft Advertising at https://ads.microsoft.com.
2. **Customer ID**: Click the gear icon (top right) > Account & Billing > the Customer ID is shown at the top.
3. **Account ID**: Go to Accounts Summary > the Account Number column shows your account IDs.

Note: Customer ID is the parent entity. Account ID is the specific ad account. If you manage multiple accounts under one customer, set BING_ADS_ACCOUNT_ID to your primary account.

## Verification

Run `mcp__bing-ads__list_accounts`. Should return account IDs, names, and statuses.
