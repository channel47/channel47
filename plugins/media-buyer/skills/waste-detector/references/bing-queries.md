# Waste Detector — Bing Ads Queries

## Waste Type 1 & 2: Non-converting and low-QS keywords

```json
{
  "report_type": "keyword",
  "date_range": "Last30Days",
  "aggregation": "Summary",
  "columns": ["CampaignName", "AdGroupName", "Keyword", "KeywordId", "MatchType", "Impressions", "Clicks", "Spend", "Conversions", "QualityScore"],
  "limit": 5000
}
```

Use `mcp__bing-ads__report`. Filter results:
- **Type 1**: `Spend > 0 AND Conversions == 0` → non-converting keywords
- **Type 2**: `QualityScore <= 4 AND Spend > 0` → low-QS keywords still spending

## Waste Type 4: Budget-limited campaigns

```json
{
  "entity": "campaigns"
}
```

Use `mcp__bing-ads__query`. Check `status` for campaigns that are active but have very low `daily_budget` relative to their spend. Cross-reference with campaign performance report to identify campaigns where spend consistently hits budget.

## Waste Type 5: Broad match keywords

```json
{
  "entity": "keywords",
  "campaign_id": "{campaign_id}",
  "ad_group_id": "{ad_group_id}"
}
```

Use `mcp__bing-ads__query` to enumerate keywords per ad group. Filter for `match_type: "Broad"`. Flag campaigns with broad match keywords but no negative keyword strategy (manual check — Bing API does not expose shared negative lists directly).

## Waste Type 6: Single-ad ad groups

```json
{
  "entity": "ads",
  "campaign_id": "{campaign_id}",
  "ad_group_id": "{ad_group_id}"
}
```

Use `mcp__bing-ads__query` per ad group. Count ads per ad group. Flag ad groups with only 1 active ad.

## Waste Type 7: Zero-impression enabled campaigns

```json
{
  "report_type": "campaign",
  "date_range": "Last30Days",
  "aggregation": "Summary",
  "columns": ["CampaignName", "CampaignId", "Impressions", "Clicks", "Spend"],
  "limit": 1000
}
```

Use `mcp__bing-ads__report`. Filter: `Impressions == 0` for campaigns that are active (cross-reference with campaign query status).

## Waste Type 8: Semantic mismatch in search terms

```json
{
  "report_type": "search_query",
  "date_range": "Last30Days",
  "aggregation": "Summary",
  "columns": ["CampaignName", "AdGroupName", "SearchQuery", "Keyword", "Impressions", "Clicks", "Spend", "Conversions"],
  "limit": 5000
}
```

Use `mcp__bing-ads__report`. Filter: `Spend > 0 AND Conversions == 0`, then assess semantic relevance of `SearchQuery` to `Keyword`.

## Waste types not applicable to Bing

- **Type 3 (Display network expansion)**: Bing does not have a "Search with Display expansion" toggle. Skip.

## Execution notes

- Bing `Spend` is already in dollars (no micros conversion).
- `QualityScore` may be `"--"` or empty for keywords with insufficient data. Treat as "no QS" and skip for Type 2.
- Types 5 and 6 require per-ad-group queries, which can be slow on large accounts. Cap at 50 ad groups per campaign, prioritized by spend.
- For Type 8, the search query report has the same privacy thresholds as Google — low-volume terms may be hidden.
