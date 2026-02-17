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

## Execution pattern

See SKILL.md Foundation Dependency for `sys.path` setup. Then:

```python
from scripts.google.auth import get_auth
from scripts.google.report import pull_report

client, config = get_auth()
customer_id = config["default_customer_id"]

df_all = pull_report(client, customer_id, QUERY_A)
df_search = pull_report(client, customer_id, QUERY_B)
```

## Field notes

- `pull_report()` automatically converts `_micros` fields and adds a derived column
  (e.g. `metrics.cost_micros` → `metrics.cost` in dollars). Use the derived column
  directly — do not divide by 1,000,000 again.
- Rows marked `EXCLUDED` should not generate new negative recommendations.
- `segments.search_term_match_type` is the match type of the query, not always the
  trigger keyword's configured match type.

## Limitations

- Search term privacy thresholds hide low-volume terms.
- GAQL `LIMIT 10000` can truncate very large accounts.
- Search term reporting excludes full PMax query detail.
