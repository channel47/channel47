# Google Ads Plugin

Google Ads and DataForSEO MCP servers with setup wizard, keyword research agent, and mutation validation hooks.

## Features

- **Google Ads MCP**: `@channel47/google-ads-mcp` - Campaign management and GAQL queries
- **DataForSEO MCP**: `@channel47/dataforseo-mcp-server` - Keyword search volume and CPC data
- **Keyword Researcher Agent**: Research keywords for Search campaigns using sales page or product description
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
    "GOOGLE_ADS_REFRESH_TOKEN": "your-refresh-token",
    "DATAFORSEO_LOGIN": "your-email",
    "DATAFORSEO_PASSWORD": "your-api-password"
  }
}
```

## MCP Tools

**Google Ads:**
- `mcp__google-ads__list_accounts` - List accessible accounts
- `mcp__google-ads__query` - Execute GAQL queries
- `mcp__google-ads__mutate` - Execute mutations (requires explicit `dry_run`)

**DataForSEO:**
- `mcp__dataforseo__keywords_google_ads_search_volume` - Get keyword metrics (volume, CPC, competition)

## Agents

- **keyword-researcher** - Research keywords for Google Ads Search campaigns. Provide a sales page URL or product description and it returns clustered keywords ready for campaign upload.

## License

MIT
