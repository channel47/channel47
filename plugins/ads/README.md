# Google Ads Plugin

Google Ads campaign creation and optimization with PMax, Search, Audit, and Assets skills plus keyword and competitor research agents.

## Features

### Skills

- **`/ads:start`** - Entry point that detects your state and routes to the right workflow
- **`/ads:setup`** - Interactive wizard to configure MCP server credentials
- **`/ads:pmax`** - Create Performance Max campaigns with asset groups and audience signals
- **`/ads:search`** - Analyze landing page and build complete Search campaigns with intent-based structure
- **`/ads:copy`** - Polish ad copy with landing page message match and direct response frameworks
- **`/ads:audit`** - Audit account health with benchmark comparisons and recommendations
- **`/ads:assets`** - Generate ad-ready images using AI with reference-based workflows
- **`/ads:creative-variations`** - Generate 3-5 strategic variants from a winning ad creative with psychological analysis

### Agents

- **keyword-researcher** - Research keywords for Search campaigns from a URL or product description
- **competitor-researcher** - Research competitors, market positioning, and customer language
- **campaign-strategist** - Analyze accounts and recommend campaign structure

### MCP Servers

- **Google Ads MCP** - Campaign management and GAQL queries
- **DataForSEO MCP** - Keyword volume, CPC, trends, competitor data
- **Reddit MCP** - Search Reddit for customer language and competitor sentiment
- **Nano Banana MCP** - AI image generation with Gemini
- **Playwright MCP** - Browser automation for reference capture

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
    "DATAFORSEO_PASSWORD": "your-api-password",
    "GEMINI_API_KEY": "your-gemini-key"
  }
}
```

## Quick Start

### Don't Know Where to Start?

```
/ads:start
```
Detects your current state (existing account, new account, creative testing) and routes you to the right workflow.

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
Analyzes your landing page and builds Search campaigns with intent-based ad groups, 15-headline RSAs, and CSV output for bulk upload.

### Asset Generation

```
/ads:assets
```
Generate ad images from product pages using AI. Screenshots references, generates brand-consistent imagery across all required sizes.

### Creative Testing

```
/ads:creative-variations
```
Generate 3-5 strategic variants from a winning ad creative. Analyzes why the image works using direct response psychology, then creates test variations that change only 1-2 elements for clean A/B testing.

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

**Nano Banana (Gemini):**
- `mcp__nano-banana__generate_image` - Generate images with prompts
- `mcp__nano-banana__upload_file` - Upload reference images
- `mcp__nano-banana__list_files` - List uploaded files

**Playwright:**
- `mcp__playwright__browser_navigate` - Navigate to URLs
- `mcp__playwright__browser_snapshot` - Capture page accessibility tree
- `mcp__playwright__browser_take_screenshot` - Screenshot page or elements

## Skill Reference Files

Skills include reference documentation:

**PMax Skill:**
- `campaign-structure.md` - Asset groups, URL expansion
- `audience-signals.md` - Custom segments, first-party data
- `asset-requirements.md` - Google's specs for all asset types

**Search Skill:**
- `references/campaign-structure.md` - Ad group organization
- `references/keyword-match-types.md` - Exact/phrase/broad strategies
- `references/audience-signals.md` - Observation vs targeting
- `references/ad-copy-formulas.md` - Headline/description patterns, psychological triggers
- `references/negative-keywords.md` - Comprehensive lists by industry
- `references/worked-example.md` - Full Notion campaign build

**Copy Skill:**
- `frameworks.md` - Direct response frameworks (AIDA, PAS, FAB, 4Ps, Offer-First)
- `headline-formulas.md` - Fill-in-the-blank patterns, psychological triggers, DKI
- `character-limits.md` - Platform specifications by campaign type
- `quality-patterns.md` - Good vs bad copy patterns, headline categories

**Audit Skill:**
- `performance-benchmarks.md` - Industry averages by vertical

**Assets Skill:**
- `prompt-templates.md` - Generation prompts by asset type
- `pmax-specs.md` - Dimension requirements for PMax
- `iteration-patterns.md` - Refinement workflow patterns

**Creative Variations Skill:**
- `psychological-triggers.md` - Complete trigger library with implementation examples
- `variation-dimensions.md` - Exhaustive list of testable elements by impact tier
- `prompt-patterns.md` - Proven Gemini prompts for each variation type

## Version History

- **2.5.0** - Added /ads:start orchestrator; consolidated search skills with landing-page-first methodology
- **2.2.0** - Added Creative Variations skill for systematic ad creative A/B testing
- **2.1.0** - Added Assets skill for AI image generation with Nano Banana and Playwright MCP
- **2.0.0** - Added PMax, Search, Audit skills and campaign-strategist agent
- **1.2.0** - Added Reddit MCP integration
- **1.1.0** - Added competitor-researcher agent
- **1.0.0** - Initial release with setup, keyword-researcher, mutation hooks

## License

MIT
