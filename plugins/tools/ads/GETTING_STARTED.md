# Getting Started with Google Ads MCP Server

This guide walks you through setting up the Google Ads MCP Server from scratch.

## Prerequisites

Before you begin, ensure you have:

1. **Node.js 18+** installed ([download](https://nodejs.org/))
2. **A Google Ads account** with API access
3. **A Google Cloud project** with OAuth 2.0 configured
4. **An MCC (Manager) account** if querying multiple accounts

## Quick Start

If you've already configured Google Ads API access:

1. Install the plugin via Claude Code Marketplace
2. The MCP server (`@channel47/google-ads-mcp`) will auto-install via npx
3. Set your environment variables (see Step 4)
4. Start using the plugin

The first time you activate the plugin, npx will download and cache the MCP server. Subsequent uses will be instant.

**If this is your first time:** Run the interactive setup wizard:

```
/ads:setup
```

Or follow the complete manual setup guide below.

## Step 1: Google Cloud Project Setup

### 1.1 Create or Select a Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Note your project ID

### 1.2 Enable Google Ads API

1. Go to **APIs & Services** > **Library**
2. Search for "Google Ads API"
3. Click **Enable**

### 1.3 Configure OAuth Consent Screen

1. Go to **APIs & Services** > **OAuth consent screen**
2. Select **External** user type (or Internal for Workspace)
3. Fill in required fields:
   - App name: "Google Ads MCP Server"
   - User support email: Your email
   - Developer contact: Your email
4. Add scopes:
   - `https://www.googleapis.com/auth/adwords`
5. Add test users (your Google account email)
6. Save and continue

### 1.4 Create OAuth 2.0 Credentials

1. Go to **APIs & Services** > **Credentials**
2. Click **Create Credentials** > **OAuth client ID**
3. Application type: **Desktop app**
4. Name: "Google Ads MCP Client"
5. Click **Create**
6. Download the JSON file (you'll need `client_id` and `client_secret`)

## Step 2: Get Your Google Ads Developer Token

1. Sign in to [Google Ads](https://ads.google.com/)
2. Go to **Tools & Settings** > **API Center**
3. If you don't have a Developer Token:
   - Apply for one (requires MCC account)
   - Basic access is sufficient for read-only operations
4. Copy your Developer Token

## Step 3: Generate OAuth Refresh Token

You need a refresh token to authenticate without user interaction.

### Option A: Use the Python Helper Script

If you have the Python plugin installed:

```bash
cd plugins/google-ads
python scripts/generate_refresh_token.py
```

### Option B: Manual OAuth Flow

1. Create a file `get_token.js`:

```javascript
import { OAuth2Client } from 'google-auth-library';
import http from 'http';
import url from 'url';

const CLIENT_ID = 'YOUR_CLIENT_ID';
const CLIENT_SECRET = 'YOUR_CLIENT_SECRET';
const REDIRECT_URI = 'http://localhost:8080/oauth2callback';
const SCOPES = ['https://www.googleapis.com/auth/adwords'];

const oauth2Client = new OAuth2Client(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI);

// Generate auth URL
const authUrl = oauth2Client.generateAuthUrl({
  access_type: 'offline',
  scope: SCOPES,
  prompt: 'consent',
});

console.log('Open this URL in your browser:\n');
console.log(authUrl);
console.log('\nWaiting for authorization...');

// Start local server to receive callback
const server = http.createServer(async (req, res) => {
  const queryParams = new url.URL(req.url, 'http://localhost:8080').searchParams;
  const code = queryParams.get('code');

  if (code) {
    try {
      const { tokens } = await oauth2Client.getToken(code);
      console.log('\n--- Your Refresh Token ---');
      console.log(tokens.refresh_token);
      console.log('--------------------------\n');

      res.end('Authorization successful! You can close this window.');
      server.close();
      process.exit(0);
    } catch (error) {
      console.error('Error getting tokens:', error);
      res.end('Error: ' + error.message);
    }
  }
});

server.listen(8080);
```

2. Run it:
```bash
node get_token.js
```

3. Open the URL in your browser and authorize
4. Copy the refresh token from the output

## Step 4: Configure Environment Variables

### Option A: Claude Code Settings

Add to `~/.claude/settings.json`:

```json
{
  "env": {
    "GOOGLE_ADS_DEVELOPER_TOKEN": "your_developer_token",
    "GOOGLE_ADS_LOGIN_CUSTOMER_ID": "1234567890",
    "GOOGLE_ADS_CLIENT_ID": "your_client_id.apps.googleusercontent.com",
    "GOOGLE_ADS_CLIENT_SECRET": "GOCSPX-your_client_secret",
    "GOOGLE_ADS_REFRESH_TOKEN": "1//0your_refresh_token"
  }
}
```

### Option B: Project-Level Settings

Add to `.claude/settings.json` in your project:

```json
{
  "env": {
    "GOOGLE_ADS_DEVELOPER_TOKEN": "...",
    "GOOGLE_ADS_LOGIN_CUSTOMER_ID": "...",
    "GOOGLE_ADS_CLIENT_ID": "...",
    "GOOGLE_ADS_CLIENT_SECRET": "...",
    "GOOGLE_ADS_REFRESH_TOKEN": "..."
  }
}
```

### Option C: Shell Environment

```bash
export GOOGLE_ADS_DEVELOPER_TOKEN="your_developer_token"
export GOOGLE_ADS_LOGIN_CUSTOMER_ID="1234567890"
export GOOGLE_ADS_CLIENT_ID="your_client_id.apps.googleusercontent.com"
export GOOGLE_ADS_CLIENT_SECRET="GOCSPX-your_client_secret"
export GOOGLE_ADS_REFRESH_TOKEN="1//0your_refresh_token"
```

## Step 5: Verify Installation

After setting environment variables:

1. Open Claude Code
2. Start a new conversation
3. The plugin should auto-activate when Google Ads topics are mentioned
4. Check Claude Code logs for "google-ads-mcp v1.0.0 started"

The MCP server is automatically managed by Claude Code. No manual server commands needed.

**The first time:** npx will download and install `@channel47/google-ads-mcp` automatically. This takes 3-5 seconds. Subsequent activations are instant (cached).

### Test with Claude Code

Try these commands:
- "List my Google Ads accounts"
- "Show my top campaigns for the last 30 days"
- "Analyze my search terms and find wasted spend"

The `google-ads-analyst` subagent handles query construction autonomously—no skill references needed.

## Troubleshooting

### "Missing required environment variables"

Check that all 5 environment variables are set:
```bash
echo $GOOGLE_ADS_DEVELOPER_TOKEN
echo $GOOGLE_ADS_LOGIN_CUSTOMER_ID
echo $GOOGLE_ADS_CLIENT_ID
echo $GOOGLE_ADS_CLIENT_SECRET
echo $GOOGLE_ADS_REFRESH_TOKEN
```

### "invalid_grant" Error

Your refresh token may have expired or been revoked:
1. Generate a new refresh token (Step 3)
2. Update your settings

### "DEVELOPER_TOKEN_NOT_APPROVED"

Your developer token needs approval:
1. Apply for Basic Access in Google Ads API Center
2. Wait for approval (usually 24-48 hours)

### "CUSTOMER_NOT_FOUND"

Verify the customer ID:
- Must be 10 digits (no dashes)
- Must be accessible from your MCC account
- Use `google_ads_list_accounts` to see available accounts

### "PERMISSION_DENIED"

Check that:
1. Your Google account has access to the Google Ads account
2. The OAuth consent screen is properly configured
3. The `adwords` scope is included

### Query Errors

Common GAQL issues:
- **Incompatible fields**: Some fields can't be selected together
- **Missing WHERE clause**: Date segmentation requires date filter
- **Invalid resource**: Check the resource name spelling

## Rate Limits

| Access Level | Limit |
|--------------|-------|
| Basic | 15,000 operations/day |
| Standard | 40 operations/second |

## Next Steps

1. **Learn GAQL**: Review the [GAQL reference](https://developers.google.com/google-ads/api/docs/query/overview) for query syntax

2. **Understand the Architecture**: Read the [README](./README.md) to learn about:
   - 3-tool architecture via `google-ads` MCP server
   - Subagent-based query handling
   - Hook validation for mutations

3. **Try Analysis Queries**: The `google-ads-analyst` subagent handles queries autonomously:
   - "Analyze campaign performance trends over the last 90 days"
   - "Find my worst performing keywords by cost per conversion"
   - "Show search terms with high spend but no conversions"

4. **Run Mutations Safely**: Mutations default to `dry_run: true`:
   - "Add 'free' as a negative keyword to my brand campaign"
   - Review the dry-run preview before confirming live execution

## Support

- [Google Ads API Documentation](https://developers.google.com/google-ads/api/docs/start)
- [MCP Protocol Specification](https://modelcontextprotocol.io/)
- [Report Issues](https://github.com/ctrlswing/channel47-marketplace/issues)
