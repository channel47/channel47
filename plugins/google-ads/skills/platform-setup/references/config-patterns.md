# Config Patterns

Use environment variables for all ad-platform credentials. The recommended approach is `.claude/settings.local.json`, which is project-scoped and gitignored by default.

## Recommended: `.claude/settings.local.json`

```json
{
  "env": {
    "GOOGLE_ADS_DEVELOPER_TOKEN": "your_developer_token",
    "GOOGLE_ADS_CLIENT_ID": "your_oauth_client_id",
    "GOOGLE_ADS_CLIENT_SECRET": "your_oauth_client_secret",
    "GOOGLE_ADS_REFRESH_TOKEN": "your_refresh_token",
    "GOOGLE_ADS_LOGIN_CUSTOMER_ID": "your_mcc_customer_id_without_hyphens"
  }
}
```

Restart Claude Code after creating or editing this file.

## Alternative: shell profile

If you prefer a single global config across all projects, set env vars in `~/.zshrc` or `~/.bashrc`:

```bash
export GOOGLE_ADS_DEVELOPER_TOKEN="your_developer_token"
```

## Where env vars are resolved

The plugin's `.mcp.json` uses `${VAR}` syntax. Claude Code resolves these from the session environment, which includes both shell env vars and the `env` field from settings files.

## Google Ads mapping

| Credential | Environment variable |
|---|---|
| Developer token | `GOOGLE_ADS_DEVELOPER_TOKEN` |
| OAuth client ID | `GOOGLE_ADS_CLIENT_ID` |
| OAuth client secret | `GOOGLE_ADS_CLIENT_SECRET` |
| OAuth refresh token | `GOOGLE_ADS_REFRESH_TOKEN` |
| Manager account ID | `GOOGLE_ADS_LOGIN_CUSTOMER_ID` |

## Rules

- Never commit credentials. Use `.claude/settings.local.json` (gitignored) or shell env vars.
- Use one canonical variable name per credential.
- Validate by running a read-only account-listing operation before any report or mutation task.
