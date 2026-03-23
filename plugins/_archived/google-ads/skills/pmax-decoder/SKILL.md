---
name: pmax-decoder
description: >-
  This skill should be used when the user asks about "Performance Max",
  "PMax", "PMax search terms", "what is PMax doing",
  "PMax placements", "PMax asset performance", "decode my PMax",
  "is PMax stealing brand traffic", "PMax channel breakdown",
  "where is PMax spending", "what channels is PMax using",
  "asset group performance", "PMax negative keywords",
  or mentions Performance Max analysis, PMax audit,
  PMax brand exclusions, or PMax cannibalization.
allowed-tools: mcp__google-ads__query, mcp__google-ads__list_accounts
---

# PMax Decoder — Google Ads

Generate operational transparency for Performance Max campaigns and produce concrete action plans for optimization.

**Read-only by design.** This skill does not modify your account. All recommendations -- including brand negative keywords -- are delivered as action plans with Google Ads UI paths and copy-paste artifacts.

## Account Context

Read `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md` at the start of every run.
If it exists:
- Use known account IDs -- skip `list_accounts` discovery.
- Apply KPI targets as anomaly detection thresholds (e.g., flag CPA > target CPA).
- Note active tests when interpreting performance shifts.
- Check watch list for follow-up items from prior sessions.
If it doesn't exist, fall back to `list_accounts` and suggest running `platform-setup`.

## Data Access

This skill uses the plugin's Google Ads MCP tools for live API access:

- `mcp__google-ads__query`: Execute GAQL SELECT queries for PMax insights.
- `mcp__google-ads__list_accounts`: Confirm account access and campaign scope.

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

#### Brand negative action plan

When brand cannibalization is detected, produce an action plan instead of API mutations:

**Dollar table:**
| Campaign | Brand Click Share | Brand Clicks | Total Clicks | Top Brand Terms | Action |
|---|---:|---:|---:|---|---|

**Copy-paste negative keyword list:**
```
-- Brand negatives for PMax Campaign '[name]' --
"brand term one"
"brand term two"
[exact brand query]
```

**UI paths for adding campaign-level brand negatives:**

Option A -- Brand exclusions (recommended for PMax):
`Google Ads > Campaign '[Campaign Name]' > Settings > Additional settings > Brand exclusions > Edit > add brand names > Save`

Option B -- Campaign-level negative keywords:
`Google Ads > Campaign '[Campaign Name]' > Keywords > Negative keywords > + > paste keywords > Save`

Option C -- Account-level brand exclusions:
`Google Ads > Tools & Settings > Account Settings > Brand exclusions > Edit > add brand names > Save`

Note: PMax brand exclusions use Google's brand list matching, which is broader than exact keyword negatives. Test with campaign-level first.

### Module 5: Placement review

Use `performance_max_placement_view` for inventory visibility.

Placement view returns impressions only (no clicks, cost, or conversions). Treat findings as quality-risk diagnostics and do not estimate placement-level cost or CPA.

Flag concerning placement types:
- Mobile app placements with high impression share (potential accidental app traffic).
- Low-quality or irrelevant display placements.
- YouTube placements on off-brand content.

For placement exclusions, provide the UI path:
`Google Ads > Campaign '[Campaign Name]' > Content > Placements > Exclusions > + > enter placement URLs > Save`

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
- Brand click share: X% ([N] brand clicks / [N] total clicks)
- Top branded terms: [list]
- Cannibalization risk: [HIGH/LOW]

**Brand Negative Action Plan:**
[copy-paste list + UI paths]

### Search Term Insight Categories
| Category | Clicks | Conversions | Notes |
|---|---:|---:|---|

### Asset Performance
| Asset Group | Ad Strength | LOW Assets | Action |
|---|---|---:|---|

### Placement Summary
- Top placement types by impression volume
- Quality risk flags

### Recommended Actions
1. [prioritized action with UI path]
2. [prioritized action with UI path]
```

## Guardrails

- `campaign_search_term_insight` requires single-campaign filtering.
- Channel-level `segments.ad_network_type` data is reliable only for dates after June 1, 2025.
- Placement view provides impressions only; do not claim placement-level cost.
- **Read-only**: This skill produces action plans only. No account modifications are made. Brand negatives and placement exclusions are delivered as copy-paste lists with UI paths.
- **Empty results**: when a module query returns zero rows, report it explicitly rather than silently omitting sections.

## Profile Maintenance

After completing analysis, if `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md` exists:
1. Update Watch List with any new anomalies flagged in this run (e.g., brand cannibalization > 30%).
2. Update Active Tests if user mentioned starting or completing a test.
3. Append to Decision Log if actions were taken.
4. Update "Last updated" date.
Present proposed profile changes to the user before writing.

## References

- `references/gaql-queries.md`
