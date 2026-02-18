# Morning Brief — Bing Ads Queries

## Report 1: Campaign performance (30 days, daily)

```json
{
  "report_type": "campaign",
  "date_range": "Last30Days",
  "aggregation": "Daily",
  "columns": ["TimePeriod", "AccountName", "CampaignName", "CampaignId", "Impressions", "Clicks", "Ctr", "AverageCpc", "Spend", "Conversions", "Revenue"],
  "limit": 5000
}
```

Use `mcp__bing-ads__report` with these parameters. Returns daily rows per campaign.

Map to anomaly detection:
- `Spend` → cost metric (already in dollars, no micros conversion needed)
- `Conversions` → conversion metric
- `Ctr` → CTR metric (already a percentage)
- CPA = `Spend / Conversions` (compute inline, skip rows where Conversions = 0)

## Report 2: Keyword performance (yesterday)

```json
{
  "report_type": "keyword",
  "date_range": "Yesterday",
  "aggregation": "Daily",
  "columns": ["CampaignName", "AdGroupName", "Keyword", "KeywordId", "Impressions", "Clicks", "Spend", "Conversions", "QualityScore"],
  "limit": 1000
}
```

Use to identify high-spend zero-conversion keywords (same pattern as Google Query 4).

Filter: `Spend > 0 AND Conversions == 0`, sort by `Spend` descending.

## Query 3: Campaign structure

```json
{
  "entity": "campaigns"
}
```

Use `mcp__bing-ads__query` with `entity: "campaigns"`. Returns campaign IDs, names, statuses, budget types, and daily budgets. Use `daily_budget` for pacing calculations.

## Execution notes

- Bing reports return `Spend` in dollars (not micros). Do not divide by 1,000,000.
- Bing `Ctr` is returned as a percentage string (e.g., "2.45%"). Parse to float for anomaly math.
- Report 1 and Report 2 can run in parallel.
- Query 3 depends on `mcp__bing-ads__list_accounts` succeeding first (needs valid account context).

## Data differences from Google

| Field | Google Ads | Bing Ads |
|-------|-----------|----------|
| Cost | `metrics.cost_micros` (auto-converted by MCP) | `Spend` (already dollars) |
| CTR | `metrics.ctr` (decimal, e.g., 0.0245) | `Ctr` (percentage string, e.g., "2.45%") |
| Conversions | `metrics.conversions` (float) | `Conversions` (float) |
| Date segment | `segments.date` (YYYY-MM-DD) | `TimePeriod` (varies by aggregation) |
| Impression share | Available via GAQL | Not available in standard reports — use campaign query for budget context |
| Change events | `change_event` resource | Not available via API — skip for Bing |
| Disapproved ads | `ad_group_ad.policy_summary` GAQL | Not available via reporting API — skip for Bing |

## What Bing cannot provide (vs Google)

- **No change event history** — Bing API does not expose account change logs.
- **No ad disapproval data** via reporting — must check in Microsoft Advertising UI.
- **No impression share** in standard performance reports.

These gaps are expected. The morning brief should note "Bing: change events and disapprovals not available via API" in the Notes section rather than omitting Bing data entirely.
