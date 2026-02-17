# Search Term Verdict GAQL Queries

## Query A: Full search-term report coverage

```sql
SELECT
  search_term_view.search_term,
  search_term_view.status,
  segments.search_term_match_type,
  campaign.id,
  campaign.name,
  campaign.advertising_channel_type,
  ad_group.id,
  ad_group.name,
  metrics.impressions,
  metrics.clicks,
  metrics.ctr,
  metrics.cost_micros,
  metrics.average_cpc,
  metrics.conversions,
  metrics.conversions_value,
  metrics.cost_per_conversion
FROM search_term_view
WHERE segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC
LIMIT 10000
```

Use this as the source of truth for total spend and cross-campaign coverage.

## Query B: Search-only keyword mapping

```sql
SELECT
  search_term_view.search_term,
  search_term_view.status,
  segments.keyword.info.text,
  segments.keyword.info.match_type,
  segments.search_term_match_type,
  campaign.id,
  campaign.name,
  ad_group.id,
  ad_group.name,
  metrics.impressions,
  metrics.clicks,
  metrics.ctr,
  metrics.cost_micros,
  metrics.conversions,
  metrics.conversions_value,
  metrics.cost_per_conversion
FROM search_term_view
WHERE segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC
LIMIT 10000
```

Adding `segments.keyword.info.text` limits results to Search keyword traffic.
Shopping, DSA, and PMax search terms are excluded.

## Execution notes

- Run both queries via `mcp__google-ads__query` with the appropriate GAQL string and customer ID.
- Query responses include both `_micros` and auto-converted currency fields (e.g. `metrics.cost_micros` → `metrics.cost` in dollars). Use the converted fields directly — do not divide by 1,000,000 again.

## Field notes
- Rows marked `EXCLUDED` should not generate new negative recommendations.
- `segments.search_term_match_type` is the match type of the query, not always the
  trigger keyword's configured match type.

## Limitations

- Search term privacy thresholds hide low-volume terms.
- GAQL `LIMIT 10000` can truncate very large accounts.
- Search term reporting excludes full PMax query detail.
