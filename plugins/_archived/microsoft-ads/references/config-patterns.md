# Configuration Patterns

## Credential Storage Options

### Option 1: settings.local.json (Recommended)

Project-scoped, gitignored by default. Works with Claude Code's env injection.

`.claude/settings.local.json`:
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

### Option 2: Shell Environment

Set in `~/.zshrc` or `~/.bashrc`. Available to all projects.

```bash
export BING_ADS_DEVELOPER_TOKEN="your-token"
export BING_ADS_CLIENT_ID="your-azure-app-id"
export BING_ADS_REFRESH_TOKEN="your-refresh-token"
export BING_ADS_CUSTOMER_ID="12345678"
export BING_ADS_ACCOUNT_ID="87654321"
```

### Option 3: .env File

Use with a `.env` loader. Must be gitignored.

## MCP Server Configuration

The plugin's `.mcp.json` references env vars using `${VAR_NAME}` syntax. The MCP server resolves these at startup. Do not hardcode values in `.mcp.json`.

## Multi-Account Setup

- Set `BING_ADS_CUSTOMER_ID` to the manager-level customer ID.
- Set `BING_ADS_ACCOUNT_ID` to the specific ad account to analyze.
- To switch accounts, update `BING_ADS_ACCOUNT_ID`.

## Security Notes

- Never commit credentials to version control.
- Never paste tokens into chat — use file-based config.
- Microsoft may rotate refresh tokens on each use. If auth fails, re-run the OAuth flow.
- This plugin is read-only — no account modifications are possible.
