# Google Ads Plugin

Google Ads campaign creation and optimization with PMax, Search, and Audit skills plus keyword and competitor research agents.

## Features

### Skills

- **`/ads:setup`** - Interactive wizard to configure MCP server credentials
- **`/ads:pmax`** - Create Performance Max campaigns with asset groups and audience signals
- **`/ads:search`** - Create Search campaigns with keyword structure and ad copy
- **`/ads:audit`** - Audit account health with benchmark comparisons and recommendations

### Agents

- **keyword-researcher** - Research keywords for Search campaigns from a URL or product description
- **competitor-researcher** - Research competitors, market positioning, and customer language
- **campaign-strategist** - Analyze accounts and recommend campaign structure

### MCP Servers

- **Google Ads MCP** - Campaign management and GAQL queries
- **DataForSEO MCP** - Keyword volume, CPC, trends, competitor data
- **Reddit MCP** - Search Reddit for customer language and competitor sentiment

### Hooks

- **Mutation Validation** - Requires explicit `dry_run` parameter on write operations

## Setup

Run `/ads:setup` for guided configuration, or manually add to `~/.claude/settings.json`:

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

## Quick Start

### Research First

```
Research keywords for https://example.com/product
```
Runs keyword-researcher agent.

```
Research competitors for https://example.com/product
```
Runs competitor-researcher agent.

### Campaign Creation

```
/ads:pmax
```
Walks through PMax campaign creation with asset requirements.

```
/ads:search
```
Builds Search campaign structure with keyword grouping and ad copy.

### Account Analysis

```
/ads:audit
```
Runs comprehensive account audit with recommendations.

### Strategic Planning

```
Analyze my Google Ads account and recommend campaign structure
```
Uses campaign-strategist agent to bridge research and creation.

## MCP Tools

**Google Ads:**
- `mcp__google-ads__list_accounts` - List accessible accounts
- `mcp__google-ads__query` - Execute GAQL queries
- `mcp__google-ads__mutate` - Execute mutations (requires `dry_run`)

**DataForSEO:**
- `mcp__dataforseo__keywords_google_ads_search_volume` - Keyword metrics
- `mcp__dataforseo__keywords_google_ads_keywords_for_keyword` - Keyword expansion
- `mcp__dataforseo__keywords_google_ads_keywords_for_site` - Competitor keywords
- `mcp__dataforseo__keywords_google_trends_explore` - Trend data
- `mcp__dataforseo__dataforseo_labs_google_competitors_domain` - Find competitors

**Reddit:**
- `mcp__reddit-mcp-buddy__search_reddit` - Search posts
- `mcp__reddit-mcp-buddy__get_post_details` - Get post and comments

## Skill Reference Files

Skills include reference documentation:

**PMax Skill:**
- `campaign-structure.md` - Asset groups, URL expansion
- `audience-signals.md` - Custom segments, first-party data
- `asset-requirements.md` - Google's specs for all asset types

**Search Skill:**
- `campaign-structure.md` - Ad group organization
- `keyword-match-types.md` - Exact/phrase/broad strategies
- `audience-signals.md` - Observation vs targeting

**Audit Skill:**
- `performance-benchmarks.md` - Industry averages by vertical

## Version History

- **2.0.0** - Added PMax, Search, Audit skills and campaign-strategist agent
- **1.2.0** - Added Reddit MCP integration
- **1.1.0** - Added competitor-researcher agent
- **1.0.0** - Initial release with setup, keyword-researcher, mutation hooks

## License

MIT
