# Config Patterns

Use environment variables for all ad-platform credentials. The recommended approach is `.claude/settings.local.json`, which is project-scoped and gitignored by default.

## Recommended: `.claude/settings.local.json`

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

Restart Claude Code after creating or editing this file.

## Alternative: shell profile

If you prefer a single global config across all projects, set env vars in `~/.zshrc` or `~/.bashrc`:

```bash
export BING_ADS_DEVELOPER_TOKEN="your_developer_token"
export BING_ADS_CLIENT_ID="your_azure_app_client_id"
export BING_ADS_REFRESH_TOKEN="your_refresh_token"
export BING_ADS_CUSTOMER_ID="your_manager_customer_id"
export BING_ADS_ACCOUNT_ID="your_default_account_id"
```

## Where env vars are resolved

The plugin's `.mcp.json` uses `${VAR}` syntax. Claude Code resolves these from the session environment, which includes both shell env vars and the `env` field from settings files.

## Microsoft Advertising credential mapping

| Credential | Environment variable |
|---|---|
| Developer token | `BING_ADS_DEVELOPER_TOKEN` |
| Azure App client ID | `BING_ADS_CLIENT_ID` |
| OAuth refresh token | `BING_ADS_REFRESH_TOKEN` |
| Customer ID (manager) | `BING_ADS_CUSTOMER_ID` |
| Account ID (default) | `BING_ADS_ACCOUNT_ID` |

## Rules

- Never commit credentials. Use `.claude/settings.local.json` (gitignored) or shell env vars.
- Use one canonical variable name per credential.
- Validate by running `mcp__bing-ads__list_accounts` before any report or analysis task.
- Microsoft rotates refresh tokens on every use. If sessions fail to start, re-run the OAuth flow for a fresh BING_ADS_REFRESH_TOKEN.
