# Google Ads Plugin

Google Ads MCP server with setup wizard and mutation validation hooks.

## Features

- **MCP Server**: `@channel47/google-ads-mcp` via npx
- **Setup Wizard**: `/ads:setup` for interactive credential configuration
- **Mutation Hooks**: Validates `dry_run` on write operations

## Setup

1. Run `/ads:setup` to configure credentials
2. Or manually add to `~/.claude/settings.json`:

```json
{
  "env": {
    "GOOGLE_ADS_DEVELOPER_TOKEN": "your-token",
    "GOOGLE_ADS_CLIENT_ID": "your-client-id",
    "GOOGLE_ADS_CLIENT_SECRET": "your-secret",
    "GOOGLE_ADS_REFRESH_TOKEN": "your-refresh-token"
  }
}
```

## MCP Tools

- `mcp__google-ads__list_accounts` - List accessible accounts
- `mcp__google-ads__query` - Execute GAQL queries
- `mcp__google-ads__mutate` - Execute mutations (requires explicit `dry_run`)

## License

MIT
