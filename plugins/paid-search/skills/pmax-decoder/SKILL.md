---
name: pmax-decoder
description: >-
  This skill should be used when the user asks about "Performance Max",
  "PMax", "PMax search terms", "PMax insights", "what is PMax doing",
  "PMax transparency", "PMax placements", "PMax asset performance",
  "decode my PMax", "PMax brand traffic", "PMax cannibalization", or
  mentions Performance Max analysis, PMax audit, PMax search queries,
  asset group performance, or PMax negative keywords.
allowed-tools: mcp__google-ads__query, mcp__google-ads__mutate, mcp__google-ads__list_accounts
---

# PMax Decoder

Generate operational transparency for Performance Max campaigns and convert that analysis into concrete actions.

## Data Access

This skill uses the plugin's Google Ads MCP tools for live API access:

- `mcp__google-ads__query`: Execute GAQL SELECT queries for PMax insights.
- `mcp__google-ads__mutate`: Preview and apply negative keyword actions.
- `mcp__google-ads__list_accounts`: Confirm account access and campaign scope.

Mutation safety flow:

1. Build operations and run `mcp__google-ads__mutate` with `dry_run: true`.
2. Show proposed changes and rationale.
3. Get explicit approval.
4. Re-run with `dry_run: false` only after approval.

## Workflow

### Module 1: Search term extraction

The `campaign_search_term_insight` resource requires single-campaign filtering.

1. Run Module 1A query to list all PMax campaigns.
2. For each campaign ID, run Module 1B query to fetch insight categories.
3. Combine categories across campaigns and rank by `metrics.clicks`.
4. Drill into top categories (default cap: 50) using Module 1C query.

Warn users that large PMax accounts can require many API calls.

### Module 2: Channel distribution (requires API v23+)

`segments.ad_network_type` on `asset_group` returns meaningful channel data (SEARCH, YOUTUBE, DISPLAY, SHOPPING) only in API v23+.

For dates before June 1, 2025, this dimension can return `MIXED` and is not reliable for channel decomposition. If data is pre-v23 behavior, skip this module and note the limitation.

Use `asset_group` with `segments.ad_network_type` to estimate spend and conversion mix by channel. Flag concentration risks when one channel exceeds 70% of spend.

### Module 3: Asset group and asset label review

- Summarize asset-group level performance (impressions, clicks, cost, conversions).
- Pull `asset_group_asset.performance_label` per asset.
- Labels are relative rankings (`BEST`, `GOOD`, `LOW`, `PENDING`), not direct cost metrics.
- Recommend replacement priorities for `LOW` assets. Do not generate creative copy unless requested.

### Module 4: Brand traffic detection

- Require user-provided brand terms.
- Classify Module 1C search terms against that list.
- `campaign_search_term_insight` does not include cost metrics; use click share as the proxy.
- Flag cannibalization risk when brand click share exceeds 30% of PMax clicks.
- Generate campaign-level negative keyword operation previews with `dry_run: true`.

### Module 5: Placement review

Use `performance_max_placement_view` for inventory visibility.

Placement view returns impressions only (no clicks, cost, or conversions). Treat findings as quality-risk diagnostics and do not estimate placement-level cost or CPA.

## Output format

```markdown
## PMax Decoder - [Date]
### Campaign: [Name] ([ID])

### Quick Stats (from Module 1A campaign data)
- Spend, conversions, CPA (cost/conversions), ROAS (conversions_value/cost)

### Channel Distribution
| Channel | Spend | % Spend | Conversions | CPA |
|---|---:|---:|---:|---:|

### Brand Traffic Analysis
- [brand click share, click volume, top branded terms]
- [negative keyword package preview]

### Search Term Insight Categories
| Category | Clicks | Conversions | Notes |
|---|---:|---:|---|

### Asset Performance
| Asset Group | Ad Strength | LOW Assets | Action |
|---|---|---:|---|

### Placement Summary
- [top placement types and quality risks]

### Recommended Actions
1. [prioritized action]
```

## Guardrails

- `campaign_search_term_insight` requires single-campaign filtering.
- Channel-level `segments.ad_network_type` data is reliable only for dates after June 1, 2025.
- Placement view provides impressions only; do not claim placement-level cost.
- Never execute live negatives without explicit user confirmation.
- **Empty results**: when a module query returns zero rows, report it explicitly rather than silently omitting sections.

## References

- `references/gaql-queries.md`
