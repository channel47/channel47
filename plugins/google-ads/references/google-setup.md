# Google Ads API Setup

## Prerequisites

1. Google Ads account (or manager account / MCC)
2. Google Cloud project with Google Ads API enabled
3. OAuth 2.0 credentials (Desktop app type)
4. Google Ads API developer token (Basic Access minimum)

## Required Environment Variables

| Variable | Source | Notes |
|----------|--------|-------|
| `GOOGLE_ADS_DEVELOPER_TOKEN` | Google Ads UI > Tools > API Center | Basic Access = 15K ops/day |
| `GOOGLE_ADS_CLIENT_ID` | Google Cloud Console > Credentials | OAuth 2.0 Client ID |
| `GOOGLE_ADS_CLIENT_SECRET` | Google Cloud Console > Credentials | OAuth 2.0 Client Secret |
| `GOOGLE_ADS_REFRESH_TOKEN` | OAuth flow output | Long-lived, doesn't expire unless revoked |
| `GOOGLE_ADS_LOGIN_CUSTOMER_ID` | Google Ads UI | Manager (MCC) ID, no hyphens (e.g., `1234567890`) |

## Step-by-Step

### 1. Enable the Google Ads API

Google Cloud Console > APIs & Services > Enable APIs > Search "Google Ads API" > Enable.

### 2. Create OAuth Credentials

Google Cloud Console > APIs & Services > Credentials > Create Credentials > OAuth Client ID.
- Application type: Desktop app
- Copy the Client ID and Client Secret.

### 3. Get Developer Token

Google Ads UI > Tools & Settings > Setup > API Center.
- Apply for Basic Access if you don't have one.
- Basic Access provides 15,000 operations/day (shared with PaidBrief if applicable).

### 4. Generate Refresh Token

Use the Google OAuth 2.0 playground or a tool like `google-ads-auth-helper`:
- Authorize with scope: `https://www.googleapis.com/auth/adwords`
- Exchange the authorization code for a refresh token at the token endpoint.

See Google's official guide: "Google Ads API > Getting Started > OAuth2" for the full flow.

### 5. Configure Credentials

Recommended: `.claude/settings.local.json` (gitignored, project-scoped):
```json
{
  "env": {
    "GOOGLE_ADS_DEVELOPER_TOKEN": "your-token",
    "GOOGLE_ADS_CLIENT_ID": "your-client-id.apps.googleusercontent.com",
    "GOOGLE_ADS_CLIENT_SECRET": "your-secret",
    "GOOGLE_ADS_REFRESH_TOKEN": "your-refresh-token",
    "GOOGLE_ADS_LOGIN_CUSTOMER_ID": "1234567890"
  }
}
```

Alternative: Shell environment variables in `~/.zshrc`.

### 6. Verify

Run `/setup` to verify access. The skill calls `mcp__google-ads__list_accounts` and reports accessible accounts.

## Common Issues

| Error | Cause | Fix |
|-------|-------|-----|
| `AUTHENTICATION_ERROR` | Invalid or expired refresh token | Re-run OAuth flow |
| `AUTHORIZATION_ERROR` | Developer token not approved | Check API Center for approval status |
| `CUSTOMER_NOT_FOUND` | Wrong login customer ID | Use the MCC ID, not a child account ID |
| No accounts returned | Token linked to wrong Google account | Re-auth with the account that has Google Ads access |

## Read-Only Constraint

This plugin sets `GOOGLE_ADS_READ_ONLY=true` in `.mcp.json`. The MCP server blocks all mutation operations. No account changes are possible through this plugin.
