# Configuration Patterns

## Credential Storage Options

### Option 1: settings.local.json (Recommended)

Project-scoped, gitignored by default. Works with Claude Code's env injection.

`.claude/settings.local.json`:
```json
{
  "env": {
    "GOOGLE_ADS_DEVELOPER_TOKEN": "your-token",
    "GOOGLE_ADS_CLIENT_ID": "your-client-id",
    "GOOGLE_ADS_CLIENT_SECRET": "your-secret",
    "GOOGLE_ADS_REFRESH_TOKEN": "your-refresh-token",
    "GOOGLE_ADS_LOGIN_CUSTOMER_ID": "1234567890"
  }
}
```

### Option 2: Shell Environment

Set in `~/.zshrc` or `~/.bashrc`. Available to all projects.

```bash
export GOOGLE_ADS_DEVELOPER_TOKEN="your-token"
export GOOGLE_ADS_CLIENT_ID="your-client-id"
export GOOGLE_ADS_CLIENT_SECRET="your-secret"
export GOOGLE_ADS_REFRESH_TOKEN="your-refresh-token"
export GOOGLE_ADS_LOGIN_CUSTOMER_ID="1234567890"
```

### Option 3: .env File

Use with a `.env` loader. Must be gitignored.

## MCP Server Configuration

The plugin's `.mcp.json` references env vars using `${VAR_NAME}` syntax. The MCP server resolves these at startup. Do not hardcode values in `.mcp.json`.

## Multi-Account Setup

For managing multiple Google Ads accounts under one MCC:
- Set `GOOGLE_ADS_LOGIN_CUSTOMER_ID` to the MCC ID (no hyphens).
- All child accounts under that MCC are accessible.
- Skills will prompt which account to analyze if multiple are found.

## Security Notes

- Never commit credentials to version control.
- Never paste tokens into chat — use file-based config.
- Refresh tokens are long-lived but can be revoked in Google Account > Security > Third-party access.
- The MCP server enforces `READ_ONLY=true` — no account modifications are possible.
