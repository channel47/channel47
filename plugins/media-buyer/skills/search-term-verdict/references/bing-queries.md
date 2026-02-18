# Search Term Verdict — Bing Ads Queries

## Report A: Search query performance (30 days)

```json
{
  "report_type": "search_query",
  "date_range": "Last30Days",
  "aggregation": "Summary",
  "columns": ["CampaignName", "AdGroupName", "SearchQuery", "Keyword", "MatchType", "Impressions", "Clicks", "Spend", "Conversions"],
  "limit": 5000
}
```

Use `mcp__bing-ads__report`. This is the primary data source for verdict classification.

Map to verdict heuristics:
- `Spend > 0 AND Conversions == 0` + semantically irrelevant → NEGATE candidate
- `Conversions >= 2 AND CPA <= target` → PROMOTE candidate
- High spend, low conversions, ambiguous intent → INVESTIGATE
- Aligned and converting → KEEP

## Query B: Keyword structure (match type context)

```json
{
  "entity": "keywords",
  "campaign_id": "{campaign_id}",
  "ad_group_id": "{ad_group_id}"
}
```

Use `mcp__bing-ads__query` per ad group. Returns keyword text, match type, status, and bid amount. Use to assess match-type drift: when a search query triggers a broad or phrase match keyword but the query is far from the keyword's intent.

## Execution notes

- Bing `Spend` is already in dollars.
- `MatchType` in the search query report shows which match type triggered the query (Broad, Phrase, Exact).
- Bing search query reports have the same privacy thresholds as Google — low-volume terms may be hidden.
- For large accounts, request the user to scope to specific campaigns first.
- The `Keyword` column shows which keyword triggered the query — use this for match-type drift analysis.

## Data mapping to Google equivalents

| Google field | Bing field | Notes |
|-------------|-----------|-------|
| `search_term_view.search_term` | `SearchQuery` | Identical concept |
| `metrics.cost_micros` (auto-converted) | `Spend` | Already dollars |
| `metrics.conversions` | `Conversions` | Same |
| `ad_group_criterion.keyword.match_type` | `MatchType` | Same concept, different enum values (e.g., "Broad" vs "BROAD") |
| `search_term_view.status` | N/A | Bing does not flag excluded terms in the search query report |
