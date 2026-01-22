---
description: Interactive wizard to configure Google Ads, DataForSEO, and Reddit MCP servers
---

# Ads Plugin Setup Wizard

Guide users through configuring MCP servers with a menu-driven interface.

## Phase 1: Status Dashboard

First, check which servers are configured by testing for their environment variables:

**Google Ads:**
- `GOOGLE_ADS_DEVELOPER_TOKEN`
- `GOOGLE_ADS_CLIENT_ID`
- `GOOGLE_ADS_CLIENT_SECRET`
- `GOOGLE_ADS_REFRESH_TOKEN`

Status: CONFIGURED if all 4 are set, NOT CONFIGURED otherwise.

**DataForSEO:**
- `DATAFORSEO_LOGIN`
- `DATAFORSEO_PASSWORD`

Status: CONFIGURED if both are set, NOT CONFIGURED otherwise.

**Reddit:**
- `REDDIT_CLIENT_ID`
- `REDDIT_CLIENT_SECRET`
- `REDDIT_USERNAME`
- `REDDIT_PASSWORD`

Status: CONFIGURED if all 4 are set, ANONYMOUS if none are set (still works), PARTIAL if some are set.

Display the dashboard:

```
=================================================================
              Ads Plugin Setup Wizard
=================================================================

SERVER STATUS
-------------
[1] Google Ads MCP    [STATUS]
    Features: Campaign management, GAQL queries
    Agent: google-ads-analyst
    Complexity: HIGH (15-20 min first time)
    Priority: HIGH - Core functionality

[2] DataForSEO MCP    [STATUS]
    Features: Keyword volume, CPC, trends
    Agents: keyword-researcher, competitor-researcher
    Complexity: LOW (2 min)
    Priority: MEDIUM - Research agents

[3] Reddit MCP        [STATUS]
    Features: Search Reddit, browse posts/comments
    Agent: competitor-researcher (enhanced)
    Complexity: NONE (anonymous) or LOW (5 min)
    Priority: LOW - Nice-to-have

=================================================================
```

Replace [STATUS] with actual status for each server.

## Phase 2: Menu Selection

Present the action menu using AskUserQuestion:

```
What would you like to do?

[A] Set up Google Ads MCP
[B] Set up DataForSEO MCP
[C] Set up Reddit MCP
[D] Set up all servers
[E] Skip to verification
[F] Show troubleshooting help
```

Accept the user's choice. If they select multiple (e.g., "A, B"), process them in order.

---

## MODULE: Google Ads MCP Setup

This module walks through Google Ads API configuration.

### Step 1: Google Cloud Project

```
GOOGLE ADS SETUP - Step 1 of 6: Create Google Cloud Project
-----------------------------------------------------------

1. Open: https://console.cloud.google.com/

2. Create a new project or select an existing one:
   - Click the project dropdown (top left)
   - Click "New Project"
   - Name: "Google Ads MCP" (or any name)
   - Click "Create"

3. Note your Project ID for later reference.
```

Ask user to confirm they've created/selected a project.

### Step 2: Enable Google Ads API

```
GOOGLE ADS SETUP - Step 2 of 6: Enable Google Ads API
-----------------------------------------------------

1. Go to: https://console.cloud.google.com/apis/library

2. Search for "Google Ads API"

3. Click on "Google Ads API" in the results

4. Click "Enable"
```

Ask user to confirm the API is enabled.

### Step 3: OAuth Consent Screen

```
GOOGLE ADS SETUP - Step 3 of 6: OAuth Consent Screen
----------------------------------------------------

1. Go to: https://console.cloud.google.com/apis/credentials/consent

2. Select User Type:
   - Choose "External" (unless you have Google Workspace)
   - Click "Create"

3. Fill in required fields:
   - App name: "Google Ads MCP"
   - User support email: Your email
   - Developer contact: Your email

4. Click "Save and Continue"

5. Add Scopes:
   - Click "Add or Remove Scopes"
   - Search for: https://www.googleapis.com/auth/adwords
   - Check the box next to it
   - Click "Update"
   - Click "Save and Continue"

6. Add Test Users:
   - Click "Add Users"
   - Enter your Google account email
   - Click "Add"
   - Click "Save and Continue"

7. Review and click "Back to Dashboard"
```

Ask user to confirm consent screen is configured.

### Step 4: OAuth Credentials

```
GOOGLE ADS SETUP - Step 4 of 6: Create OAuth Credentials
--------------------------------------------------------

1. Go to: https://console.cloud.google.com/apis/credentials

2. Click "Create Credentials" > "OAuth client ID"

3. Application type: "Desktop app"

4. Name: "Google Ads MCP Client"

5. Click "Create"

6. Copy from the popup:
   - Client ID (ends with .apps.googleusercontent.com)
   - Client Secret (starts with GOCSPX-)
```

Ask user to provide:
- Client ID
- Client Secret

Store these values for configuration generation.

### Step 5: Developer Token

```
GOOGLE ADS SETUP - Step 5 of 6: Get Developer Token
---------------------------------------------------

1. Sign in to Google Ads: https://ads.google.com/

2. Click Tools icon (wrench) > "API Center" under Setup

3. If you don't have a token:
   - Apply for API access (Basic access is usually auto-approved)

4. Copy your Developer Token

Note: If you manage multiple accounts via MCC, you'll also need
your Manager Account ID (10 digits, no dashes).
```

Ask user to provide:
- Developer Token
- MCC Account ID (optional)

### Step 6: Refresh Token

```
GOOGLE ADS SETUP - Step 6 of 6: Generate Refresh Token
------------------------------------------------------

Run this command in your terminal:

  npx @channel47/google-ads-auth

The script will:
1. Open a browser for Google sign-in
2. Ask you to authorize the app
3. Display your refresh token

Copy the refresh token when it appears.


MANUAL ALTERNATIVE
------------------
If the helper script doesn't work, create get-token.js:

const http = require('http');
const https = require('https');
const url = require('url');

const CLIENT_ID = 'YOUR_CLIENT_ID';
const CLIENT_SECRET = 'YOUR_CLIENT_SECRET';
const REDIRECT_URI = 'http://localhost:8080/oauth2callback';
const SCOPE = 'https://www.googleapis.com/auth/adwords';

const authUrl = `https://accounts.google.com/o/oauth2/v2/auth?` +
  `client_id=${CLIENT_ID}&redirect_uri=${REDIRECT_URI}&` +
  `response_type=code&scope=${SCOPE}&access_type=offline&prompt=consent`;

console.log('Open this URL in your browser:\n');
console.log(authUrl);

const server = http.createServer((req, res) => {
  const query = url.parse(req.url, true).query;
  if (query.code) {
    const postData = `code=${query.code}&client_id=${CLIENT_ID}&` +
      `client_secret=${CLIENT_SECRET}&redirect_uri=${REDIRECT_URI}&` +
      `grant_type=authorization_code`;

    const options = {
      hostname: 'oauth2.googleapis.com',
      path: '/token',
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
    };

    const tokenReq = https.request(options, (tokenRes) => {
      let data = '';
      tokenRes.on('data', chunk => data += chunk);
      tokenRes.on('end', () => {
        const tokens = JSON.parse(data);
        console.log('\n--- Your Refresh Token ---');
        console.log(tokens.refresh_token);
        res.end('Success! Check terminal.');
        server.close();
        process.exit(0);
      });
    });
    tokenReq.write(postData);
    tokenReq.end();
  }
});
server.listen(8080);

Replace YOUR_CLIENT_ID and YOUR_CLIENT_SECRET, then run: node get-token.js
```

Ask user to provide:
- Refresh Token

**Google Ads module complete.** Return to menu or continue to next selected server.

---

## MODULE: DataForSEO MCP Setup

This module configures DataForSEO API access.

```
DATAFORSEO SETUP
----------------

DataForSEO provides keyword search volume, CPC, and competition data.

1. Sign up at: https://dataforseo.com/
   - Free trial includes API credits
   - No credit card required

2. Go to dashboard: https://app.dataforseo.com/

3. Find your API credentials:
   - Login: Your email address
   - Password: Your API password (NOT your account password)

   The API password is shown in your dashboard settings.
```

Ask user to provide:
- DataForSEO Login (email)
- DataForSEO Password (API password)

**DataForSEO module complete.** Return to menu or continue to next selected server.

---

## MODULE: Reddit MCP Setup

This module configures Reddit MCP access.

### Authentication Choice

```
REDDIT MCP SETUP
----------------

Reddit MCP can run in two modes:

ANONYMOUS MODE (Recommended for most users)
- No credentials needed
- Works immediately
- Read-only access to public content
- Sufficient for competitor research

AUTHENTICATED MODE
- Higher rate limits
- Access to more content
- Required for some advanced features
```

Ask user: "Which mode would you like to use?"
- Anonymous (no setup needed)
- Authenticated (continue to credential setup)

### Anonymous Mode

If user chooses anonymous:

```
Reddit MCP: Anonymous Mode Selected
-----------------------------------

No configuration needed! Reddit MCP will work automatically
in anonymous mode with read-only access to public content.
```

**Reddit module complete (anonymous).**

### Authenticated Mode

If user chooses authenticated:

```
REDDIT AUTHENTICATED SETUP
--------------------------

1. Go to: https://www.reddit.com/prefs/apps

2. Click "create another app..." at the bottom

3. Fill in:
   - Name: "Ads Plugin Research"
   - Type: Select "script"
   - Description: (optional)
   - About URL: (leave blank)
   - Redirect URI: http://localhost:8080

4. Click "create app"

5. Copy your credentials:
   - Client ID: The string under your app name
   - Client Secret: The "secret" value
```

Ask user to provide:
- Reddit Client ID
- Reddit Client Secret
- Reddit Username
- Reddit Password

**Reddit module complete (authenticated).**

---

## Phase 3: Configuration Generation

Generate the JSON configuration based on which servers were set up:

```
CONFIGURATION
-------------

Add these credentials to ~/.claude/settings.json:

{
  "env": {
    [ONLY INCLUDE VARIABLES FOR CONFIGURED SERVERS]
  }
}
```

**Google Ads variables (if configured):**
```
"GOOGLE_ADS_DEVELOPER_TOKEN": "...",
"GOOGLE_ADS_CLIENT_ID": "...",
"GOOGLE_ADS_CLIENT_SECRET": "...",
"GOOGLE_ADS_REFRESH_TOKEN": "...",
"GOOGLE_ADS_LOGIN_CUSTOMER_ID": "..."  // Only if MCC provided
```

**DataForSEO variables (if configured):**
```
"DATAFORSEO_LOGIN": "...",
"DATAFORSEO_PASSWORD": "..."
```

**Reddit variables (if authenticated mode):**
```
"REDDIT_CLIENT_ID": "...",
"REDDIT_CLIENT_SECRET": "...",
"REDDIT_USERNAME": "...",
"REDDIT_PASSWORD": "..."
```

Note: Reddit in anonymous mode needs no environment variables.

## Phase 4: Restart Instructions

```
RESTART REQUIRED
----------------

For changes to take effect:

1. Exit Claude Code (Ctrl+C or Cmd+Q)
2. Start Claude Code again: claude
3. Resume your session if needed: /resume

The MCP servers will start automatically!
```

## Phase 5: Verification

After restart, verify configured servers:

**Google Ads Verification:**
```
Testing Google Ads connection...
Running: mcp__google-ads__list_accounts
```

On success: Show account list
On failure: Show error and troubleshooting tips

**DataForSEO Verification:**
```
Testing DataForSEO connection...
Running: mcp__dataforseo__keywords_google_ads_search_volume
with test keyword "test"
```

On success: "DataForSEO: Connected"
On failure: Show error and troubleshooting tips

**Reddit Verification:**
```
Testing Reddit connection...
Running: mcp__reddit-mcp-buddy__search_reddit
with test query "marketing"
```

On success: "Reddit MCP: Connected ([mode])"
On failure: Show error and troubleshooting tips

## Phase 6: Completion Summary

```
=================================================================
                    Setup Complete!
=================================================================

Configured Servers:
------------------
[X] Google Ads MCP     - Campaign management ready
[X] DataForSEO MCP     - Keyword research ready
[X] Reddit MCP         - Reddit search ready (anonymous)

Available Agents:
-----------------
- google-ads-analyst    Analyze campaigns, run GAQL queries
- keyword-researcher    Research keywords for Search campaigns
- competitor-researcher Research competitors and markets

Quick Commands:
---------------
- "List my Google Ads accounts"
- "Show campaign performance for the last 30 days"
- "Research keywords for [product URL or description]"
- "Search Reddit for discussions about [topic]"

=================================================================
```

Only show checkmarks for actually configured servers.

---

## Troubleshooting Reference

**Google Ads Common Issues:**
- "invalid_grant" - Refresh token expired, regenerate with Step 6
- "DEVELOPER_TOKEN_NOT_APPROVED" - Apply for API access at ads.google.com
- "CUSTOMER_NOT_FOUND" - Check customer ID format (10 digits, no dashes)
- "PERMISSION_DENIED" - Check OAuth consent screen scopes

**DataForSEO Common Issues:**
- "401 Unauthorized" - Check login/password credentials
- "402 Payment Required" - Account out of credits
- "Invalid credentials" - Using account password instead of API password

**Reddit Common Issues:**
- "401 Unauthorized" - Check client ID and secret
- "Invalid credentials" - Verify username and password
- Rate limiting - Switch to authenticated mode for higher limits

**Security Reminders:**
- Never share credentials in chat or commit to git
- Store credentials only in ~/.claude/settings.json
- Refresh tokens can be revoked at https://myaccount.google.com/permissions
- Rotate credentials periodically
