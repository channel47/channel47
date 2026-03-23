# Microsoft Advertising API Setup

## Prerequisites

1. Microsoft Advertising account
2. Azure App Registration (for OAuth)
3. Microsoft Advertising developer token

## Required Environment Variables

| Variable | Source | Notes |
|----------|--------|-------|
| `BING_ADS_DEVELOPER_TOKEN` | Microsoft Advertising Developer Portal | Apply at developers.ads.microsoft.com |
| `BING_ADS_CLIENT_ID` | Azure Portal > App Registrations | Application (client) ID |
| `BING_ADS_REFRESH_TOKEN` | OAuth flow output | Rotates on each refresh in some configs |
| `BING_ADS_CUSTOMER_ID` | Microsoft Advertising UI | Manager-level customer ID |
| `BING_ADS_ACCOUNT_ID` | Microsoft Advertising UI | Specific ad account ID |

## Step-by-Step

### 1. Get Developer Token

Microsoft Advertising > Tools > Developer Portal (developers.ads.microsoft.com).
- Sign in with your Microsoft Advertising credentials.
- Request a developer token. Super Admin access may be required.

### 2. Create Azure App Registration

Azure Portal > Azure Active Directory > App registrations > New registration.
- Name: "Bing Ads MCP" (or similar)
- Supported account types: "Accounts in any organizational directory and personal Microsoft accounts"
- Redirect URI: `http://localhost` (for desktop flow)
- Copy the Application (client) ID.

### 3. Generate Refresh Token

Use the Microsoft identity platform OAuth flow:
1. Authorization endpoint: `https://login.microsoftonline.com/common/oauth2/v2/authorize`
2. Scope: `https://ads.microsoft.com/msads.manage offline_access`
3. Exchange the authorization code at the token endpoint for a refresh token.

Note: Microsoft may rotate refresh tokens on every use. If you see auth failures, re-run the OAuth flow.

### 4. Find Customer ID and Account ID

Microsoft Advertising UI:
- **Customer ID:** Settings > Account > Customer ID (manager-level)
- **Account ID:** The specific ad account number (visible in account selector or Settings)

### 5. Configure Credentials

Recommended: `.claude/settings.local.json` (gitignored, project-scoped):
```json
{
  "env": {
    "BING_ADS_DEVELOPER_TOKEN": "your-token",
    "BING_ADS_CLIENT_ID": "your-azure-app-id",
    "BING_ADS_REFRESH_TOKEN": "your-refresh-token",
    "BING_ADS_CUSTOMER_ID": "12345678",
    "BING_ADS_ACCOUNT_ID": "87654321"
  }
}
```

Alternative: Shell environment variables in `~/.zshrc`.

### 6. Verify

Run `/setup` to verify access. The skill calls `mcp__bing-ads__list_accounts` and reports accessible accounts.

## Common Issues

| Error | Cause | Fix |
|-------|-------|-----|
| `AuthenticationTokenExpired` | Refresh token rotated or expired | Re-run OAuth flow for new token |
| `InvalidClientId` | Wrong Azure App Registration ID | Verify Application (client) ID in Azure Portal |
| `CustomerNotFound` | Wrong customer ID | Customer ID is manager-level, not account-level |
| No accounts returned | Token linked to wrong Microsoft account | Re-auth with the account that has Microsoft Advertising access |

## Bing Data Quirks

- Spend values are in dollars (no micros conversion needed, unlike Google).
- CTR comes as a percentage string (e.g., "2.45") — parse to float before math.
- No change event history via API.
- No impression share in standard reports.
- No ad disapproval data via API.
