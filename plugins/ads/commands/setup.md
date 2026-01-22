---
description: Interactive wizard to configure Google Ads API credentials for the MCP server
---

# Google Ads Specialist Setup Wizard

Guide users through configuring the Google Ads MCP server with OAuth 2.0 credentials.

## Phase 1: Welcome and Prerequisites Check

Display welcome message and verify prerequisites:

```
=================================================================
         Google Ads Specialist Setup Wizard
=================================================================

This wizard will help you configure the Google Ads MCP server
for campaign management and GAQL queries.

Prerequisites:
- A Google Ads account with API access
- A Google Cloud project (we'll help you create one)
- About 10-15 minutes to complete setup

Let's get started!
```

Check if any Google Ads environment variables are already configured by examining the environment. Report which are set and which are missing.

**Required Environment Variables:**
| Variable | Status |
|----------|--------|
| `GOOGLE_ADS_DEVELOPER_TOKEN` | Check if set |
| `GOOGLE_ADS_CLIENT_ID` | Check if set |
| `GOOGLE_ADS_CLIENT_SECRET` | Check if set |
| `GOOGLE_ADS_REFRESH_TOKEN` | Check if set |

**Optional Environment Variables:**
| Variable | Status |
|----------|--------|
| `GOOGLE_ADS_LOGIN_CUSTOMER_ID` | Check if set (required for MCC accounts) |
| `GOOGLE_ADS_DEFAULT_CUSTOMER_ID` | Check if set |

If all required variables are set, offer to skip to verification (Phase 6).

## Phase 2: Google Cloud Project Setup

Guide user through Google Cloud Console setup:

```
STEP 1: Create a Google Cloud Project
--------------------------------------

1. Open: https://console.cloud.google.com/

2. Create a new project or select an existing one:
   - Click the project dropdown (top left)
   - Click "New Project"
   - Name: "Google Ads MCP" (or any name)
   - Click "Create"

3. Note your Project ID for later reference.

Have you created/selected a Google Cloud project?
```

After confirmation, continue:

```
STEP 2: Enable the Google Ads API
---------------------------------

1. Go to: https://console.cloud.google.com/apis/library

2. Search for "Google Ads API"

3. Click on "Google Ads API" in the results

4. Click "Enable"

Have you enabled the Google Ads API?
```

## Phase 3: OAuth Consent Screen

Guide user through OAuth consent screen configuration:

```
STEP 3: Configure OAuth Consent Screen
--------------------------------------

1. Go to: https://console.cloud.google.com/apis/credentials/consent

2. Select User Type:
   - Choose "External" (unless you have Google Workspace)
   - Click "Create"

3. Fill in the required fields:
   - App name: "Google Ads MCP"
   - User support email: Your email address
   - Developer contact: Your email address

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

Have you configured the OAuth consent screen?
```

## Phase 4: Create OAuth Credentials

Guide user through creating OAuth 2.0 credentials:

```
STEP 4: Create OAuth 2.0 Credentials
------------------------------------

1. Go to: https://console.cloud.google.com/apis/credentials

2. Click "Create Credentials" at the top

3. Select "OAuth client ID"

4. Application type: Select "Desktop app"

5. Name: "Google Ads MCP Client"

6. Click "Create"

7. A popup will show your credentials:
   - Copy the "Client ID" (ends with .apps.googleusercontent.com)
   - Copy the "Client Secret" (starts with GOCSPX-)

Save these values - you'll need them in the next steps!

Client ID: ________________________________
Client Secret: ____________________________
```

Ask user to provide their Client ID and Client Secret for validation (format check only).

## Phase 5: Get Developer Token

Guide user to obtain their Google Ads Developer Token:

```
STEP 5: Get Your Developer Token
--------------------------------

1. Sign in to Google Ads: https://ads.google.com/

2. Click the Tools icon (wrench) in the top menu

3. Under "Setup", click "API Center"

4. If you don't have a Developer Token:
   - You'll see an option to apply for API access
   - Basic access is sufficient for most use cases
   - Approval is usually automatic for basic access

5. Copy your Developer Token

Developer Token: ____________________________

Note: If you manage multiple accounts, you'll also need your
Manager Account (MCC) ID - a 10-digit number without dashes.

MCC Account ID (optional): ____________________________
```

## Phase 6: Generate Refresh Token

This is the most complex step. Provide a helper script:

```
STEP 6: Generate OAuth Refresh Token
------------------------------------

This step exchanges your OAuth credentials for a refresh token
that allows the MCP server to authenticate automatically.

Option A: Use our helper script (Recommended)
---------------------------------------------

Run this command in your terminal:

npx @channel47/google-ads-auth

The script will:
1. Open a browser for Google sign-in
2. Ask you to authorize the app
3. Display your refresh token

Copy the refresh token when it appears.


Option B: Manual OAuth Flow
---------------------------

If the helper script doesn't work, you can generate the token manually:

1. Create a file called get-token.js with the following content:

---
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
console.log('\nWaiting for authorization...');

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
        console.log('--------------------------\n');
        res.end('Success! Check your terminal for the refresh token.');
        server.close();
        process.exit(0);
      });
    });
    tokenReq.write(postData);
    tokenReq.end();
  }
});

server.listen(8080);
---

2. Replace YOUR_CLIENT_ID and YOUR_CLIENT_SECRET with your values

3. Run: node get-token.js

4. Open the URL in your browser and sign in

5. Copy the refresh token from the terminal output


Refresh Token: ____________________________
```

## Phase 7: Configure Environment Variables

Provide the complete configuration:

```
STEP 7: Configure Claude Code
-----------------------------

Add your credentials to ~/.claude/settings.json:

{
  "env": {
    "GOOGLE_ADS_DEVELOPER_TOKEN": "YOUR_DEVELOPER_TOKEN",
    "GOOGLE_ADS_CLIENT_ID": "YOUR_CLIENT_ID.apps.googleusercontent.com",
    "GOOGLE_ADS_CLIENT_SECRET": "GOCSPX-YOUR_CLIENT_SECRET",
    "GOOGLE_ADS_REFRESH_TOKEN": "1//YOUR_REFRESH_TOKEN",
    "GOOGLE_ADS_LOGIN_CUSTOMER_ID": "1234567890"
  }
}

Notes:
- GOOGLE_ADS_LOGIN_CUSTOMER_ID is your MCC account ID (10 digits, no dashes)
- Only include LOGIN_CUSTOMER_ID if you have an MCC account
- If you already have an "env" section, merge these values into it

Would you like me to show you the exact JSON to add?
```

Generate the exact JSON configuration using the values collected.

## Phase 8: Restart Instructions

```
STEP 8: Restart Claude Code
---------------------------

For changes to take effect:

1. Exit Claude Code (Ctrl+C or Cmd+Q)

2. Start Claude Code again: claude

3. Resume your session if needed: /resume

The Google Ads MCP server will start automatically!
```

## Phase 9: Verification

After restart, verify the setup:

```
STEP 9: Verify Setup
--------------------

Let's test your configuration by listing your Google Ads accounts.

Running: mcp__google-ads__list_accounts
```

Execute `mcp__google-ads__list_accounts` to verify the connection.

**On Success:**
```
Setup Complete!

Your Google Ads accounts:
- Account Name (ID: 1234567890)
- Account Name (ID: 0987654321)

You're ready to use the Google Ads Specialist plugin!
```

**On Failure:**
```
Connection Failed

Error: [specific error message]

Common issues:
- Invalid credentials: Double-check your Client ID, Secret, and Refresh Token
- Expired refresh token: Generate a new one using Step 6
- Missing permissions: Ensure the Google Ads API is enabled
- Wrong account: Verify LOGIN_CUSTOMER_ID matches your MCC account

Run /ads:setup again to reconfigure.
```

## Phase 10: Quick Reference

```
=================================================================
                    Setup Complete!
=================================================================

Quick Commands:
--------------
- "List my Google Ads accounts"
- "Show campaign performance for the last 30 days"
- "What keywords are converting best?"

MCP Tools:
---------
- mcp__google-ads__list_accounts  List accessible accounts
- mcp__google-ads__query          Execute GAQL queries
- mcp__google-ads__mutate         Execute write operations (dry_run validated)

Happy optimizing!
=================================================================
```

## Error Recovery

If user encounters issues at any step:

1. Identify the specific error
2. Provide targeted solution from common issues:
   - "invalid_grant" → Refresh token expired, regenerate
   - "DEVELOPER_TOKEN_NOT_APPROVED" → Apply for API access
   - "CUSTOMER_NOT_FOUND" → Check customer ID format (10 digits, no dashes)
   - "PERMISSION_DENIED" → Check OAuth consent screen and scopes
3. Offer to retry the failed step

## Credential Security Reminders

Throughout the wizard, remind users:

- Never share credentials in chat or commit them to git
- Store credentials only in ~/.claude/settings.json (gitignored by default)
- Refresh tokens can be revoked at https://myaccount.google.com/permissions
- Rotate credentials periodically for security
