# Google Ads Specialist Plugin

A Claude Code plugin for Google Ads campaign management using GAQL (Google Ads Query Language). Version 4.0.0 introduces a subagent-based architecture where queries are handled autonomously by a specialized analyst subagent, while mutations remain gated by hook validation.

## Architecture

**Version 4.0.0** - Subagent-based design with minimal token footprint:

- **NPM Package**: MCP server published as `@channel47/google-ads-mcp`
- **Auto-Installation**: Server installed via npx on first use
- **3 Core MCP Tools**: Minimal data access layer (list_accounts, query, mutate)
- **1 Subagent**: `google-ads-analyst` for query isolation and autonomous GAQL generation
- **1 Skill**: Troubleshooting guide for plugin-specific errors
- **PreToolUse Hook**: Validates dry_run on mutations only (queries flow freely)
- **~450 Tokens**: Down from 7,883 tokens (94% reduction)

### Design Philosophy

The subagent architecture separates concerns:
- **Queries**: Handled autonomously by `google-ads-analyst` subagent (no skill lookup needed)
- **Mutations**: Gated by hook validation requiring explicit dry_run handling
- **Troubleshooting**: Minimal skill for plugin-specific errors only (GAQL syntax in Google docs)

This design eliminates token overhead from skill files while maintaining safety for write operations.

## Features

- **Subagent Query Isolation**: Analyst subagent handles all GAQL queries autonomously
- **Minimal Tool Surface**: Just 3 tools (list_accounts, query, mutate)
- **Autonomous GAQL Generation**: No skill reference required for queries
- **Mutation Oversight**: Hook validates dry_run on write operations
- **Full GAQL Access**: Any SELECT query via `mcp__google-ads__query` tool
- **Safe Mutations**: Write operations via `mcp__google-ads__mutate` tool with dry_run validation
- **OAuth 2.0 Authentication**: Secure refresh token auth

## Requirements

- Node.js 18.0.0 or higher
- Google Ads API access (Developer Token)
- Google Cloud OAuth 2.0 credentials
- Claude Code (for plugin installation)

## Installation

### As a Claude Code Plugin

Install via the Claude Code plugin marketplace:

1. Open Claude Code
2. Navigate to Plugin Marketplace
3. Search for "Google Ads Specialist"
4. Click Install

The plugin will automatically install the required MCP server (`@channel47/google-ads-mcp`) via npx when first activated.

**Manual Installation:**

1. Clone this repository
2. Copy to your Claude Code plugins directory: `~/.claude/plugins/google-ads-specialist`
3. Configure OAuth credentials (see GETTING_STARTED.md)

The MCP server is distributed as an npm package and installed automatically. No manual server setup required.

## Configuration

The MCP server requires these environment variables. Configure them before activating the plugin:

**Required:**

| Variable | Description |
|----------|-------------|
| `GOOGLE_ADS_DEVELOPER_TOKEN` | Your Google Ads API Developer Token |
| `GOOGLE_ADS_CLIENT_ID` | OAuth 2.0 Client ID from Google Cloud |
| `GOOGLE_ADS_CLIENT_SECRET` | OAuth 2.0 Client Secret |
| `GOOGLE_ADS_REFRESH_TOKEN` | OAuth 2.0 Refresh Token |

Optional:

| Variable | Description |
|----------|-------------|
| `GOOGLE_ADS_LOGIN_CUSTOMER_ID` | MCC Account ID (10 digits, no dashes) |
| `GOOGLE_ADS_DEFAULT_CUSTOMER_ID` | Default account ID for queries |

**Quick Setup:** Run `/google-ads-specialist:setup` for an interactive setup wizard.

See `GETTING_STARTED.md` for detailed OAuth setup instructions.

**Note:** The MCP server (`@channel47/google-ads-mcp`) is automatically installed via npx. You do not need to manually install it.

## Core MCP Tools (google-ads)

The plugin provides tools via the `google-ads` MCP server. Tools are accessed as `mcp__google-ads__<tool_name>`.

### 1. mcp__google-ads__list_accounts

List all accessible Google Ads accounts.

**Parameters:**
- `include_manager_accounts` (boolean, optional): Include MCC accounts (default: false)

**Example:**
```json
{
  "include_manager_accounts": false
}
```

### 2. mcp__google-ads__query

Execute any GAQL SELECT query. Queries are handled autonomously - no skill reference required.

**Parameters:**
- `customer_id` (string, optional): Account ID (uses default if not specified)
- `query` (string, required): Full GAQL SELECT query
- `limit` (integer, optional): Max rows to return (default: 100, max: 10000)

**Example:**
```json
{
  "query": "SELECT campaign.name, metrics.cost_micros FROM campaign WHERE segments.date DURING LAST_30_DAYS",
  "limit": 50
}
```

### 3. mcp__google-ads__mutate

Execute write operations via GoogleAdsService.Mutate. **Requires dry_run validation** (enforced by hook).

**Parameters:**
- `customer_id` (string, optional): Account ID
- `operations` (array, required): Array of mutation operation objects
- `partial_failure` (boolean, optional): Enable partial failure mode (default: true)
- `dry_run` (boolean, optional): Validate only, don't execute (default: **true** for safety)

**Example:**
```json
{
  "operations": [
    {
      "campaign_criterion_operation": {
        "create": {
          "campaign": "customers/1234567890/campaigns/987654321",
          "negative": true,
          "keyword": {
            "text": "free",
            "match_type": "PHRASE"
          }
        }
      }
    }
  ],
  "dry_run": true
}
```

## Subagent

### google-ads-analyst

The analyst subagent handles all Google Ads query operations autonomously. It:

- Constructs GAQL queries from natural language requests
- Executes queries via `mcp__google-ads__query` tool
- Formats results appropriately (inline for small results, file output for large datasets)
- Handles query errors and provides troubleshooting guidance

**When spawned:**
- User requests campaign performance data
- User asks for search terms analysis
- User needs budget or spend information
- Any read-only Google Ads data request

The subagent operates independently without requiring skill references, generating GAQL queries based on its training knowledge and the Google Ads API schema.

## Skill

### troubleshooting

The single troubleshooting skill provides guidance for plugin-specific errors:

- MCP server connection issues
- OAuth authentication problems
- Hook validation errors
- Plugin configuration issues

For GAQL syntax help, refer to [Google's GAQL documentation](https://developers.google.com/google-ads/api/docs/query/overview).

## Workflow Example

1. **User:** "Show me campaign performance for the last 30 days"

2. **Claude** spawns `google-ads-analyst` subagent

3. **Subagent** autonomously constructs GAQL:
   ```sql
   SELECT campaign.id, campaign.name, metrics.cost_micros, metrics.conversions
   FROM campaign
   WHERE segments.date DURING LAST_30_DAYS
   ```

4. **Subagent** executes query via `mcp__google-ads__query` tool

5. **Subagent** formats and returns results to main conversation

For mutations:

1. **User:** "Add 'free' as a negative keyword to campaign X"

2. **Claude** constructs mutation operation

3. **Hook** validates that `dry_run` parameter is explicitly set

4. **Claude** executes with `dry_run: true` first, then confirms with user before live execution

## Hook Validation

The PreToolUse hook gates mutation operations:

- **Monitors** `mcp__google-ads__mutate` tool calls
- **Validates** that `dry_run` parameter is explicitly handled
- **Allows** all query operations without validation (queries are read-only)
- **Allows** `mcp__google-ads__list_accounts` (safe enumeration)
- **Fail-open** on errors (prevents workflow breakage)

This ensures mutations receive human oversight while queries flow freely.

## Architecture Details

### Plugin Structure

```
agents/
└── google-ads-analyst.md   # Subagent for query isolation
skills/
└── troubleshooting/
    └── SKILL.md            # Plugin-specific errors only
.claude/hooks/
└── validate-mutations.py   # Gates live mutations only
```

### Hook Configuration

```
.claude/
├── hooks/
│   └── validate-mutations.py   # Mutation validation script
└── settings.json               # Hook registration
```

## Security

- **Dry Run Default**: Mutations default to `dry_run: true` for safety
- **Mutation Blocking**: Query tool blocks CREATE/UPDATE/REMOVE keywords
- **Hook Validation**: Requires explicit dry_run handling for mutations
- **Query Freedom**: Read-only operations flow without friction
- **OAuth 2.0**: Secure refresh token authentication
- **Input Validation**: All parameters validated before execution

## Development

This plugin uses the `@channel47/google-ads-mcp` npm package for the MCP server.

### Plugin Development

To modify the subagent, skill, or documentation:

1. Clone this repository
2. Edit files in `agents/`, `skills/`, or `.claude/hooks/`
3. Update documentation as needed
4. Test locally by copying to `~/.claude/plugins/google-ads-specialist`

### MCP Server Development

The MCP server is developed separately at [github.com/channel47/google-ads-mcp-server](https://github.com/channel47/google-ads-mcp-server).

To test with a local server build:
1. Clone the server repository
2. Update `.mcp.json` to point to local server: `"command": "node", "args": ["/path/to/server/index.js"]`
3. Restore npx command before committing

### Publish to Marketplace

```bash
npm run publish-to-marketplace
```

## Migration from v3.x

Version 4.0.0 is a **breaking change**:

**Removed:**
- 7 atomic skills (campaign-performance, search-terms, wasted-spend, quality-score, budget-pacing, add-negatives, adjust-bids)
- 1 playbook skill (account-health-audit)
- Skill-reference requirement for queries

**Added:**
- `google-ads-analyst` subagent for query isolation
- Autonomous GAQL generation (no skill lookup needed)

**Changed:**
- Hook now gates mutations only (queries flow freely)
- Troubleshooting skill reduced to plugin-specific errors only

**Migration Path:**
1. Update to v4.0.0
2. Queries work immediately - no changes needed
3. Mutations unchanged - still require dry_run handling
4. For GAQL syntax help, use [Google's documentation](https://developers.google.com/google-ads/api/docs/query/overview)

**Benefits:**
- 94% token reduction (7,883 -> ~450 tokens)
- Faster query execution (no skill lookup overhead)
- Simpler mental model (subagent handles queries autonomously)
- Maintained safety (mutations still gated)

## Resources

- [Getting Started Guide](GETTING_STARTED.md)
- [Changelog](CHANGELOG.md)
- [MCP Server (npm)](https://www.npmjs.com/package/@channel47/google-ads-mcp)
- [MCP Server (GitHub)](https://github.com/channel47/google-ads-mcp-server)
- [Google Ads API Docs](https://developers.google.com/google-ads/api/docs/start)
- [GAQL Reference](https://developers.google.com/google-ads/api/docs/query/overview)
- [Claude Code Documentation](https://code.claude.com/docs)

## License

MIT License - See LICENSE file for details.
