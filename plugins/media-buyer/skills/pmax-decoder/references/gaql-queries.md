# PMax Decoder GAQL Queries

## Module 1A: PMax campaign list

```sql
SELECT
  campaign.id,
  campaign.name,
  campaign.status,
  metrics.cost_micros,
  metrics.conversions,
  metrics.conversions_value
FROM campaign
WHERE campaign.advertising_channel_type = 'PERFORMANCE_MAX'
  AND campaign.status = 'ENABLED'
  AND segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC
```

## Module 1B: Search term insight categories by campaign

```sql
SELECT
  campaign_search_term_insight.campaign_id,
  campaign_search_term_insight.category_label,
  campaign_search_term_insight.id,
  metrics.clicks,
  metrics.impressions,
  metrics.conversions,
  metrics.conversions_value
FROM campaign_search_term_insight
WHERE segments.date DURING LAST_30_DAYS
  AND campaign_search_term_insight.campaign_id = 'CAMPAIGN_ID'
```

`campaign_search_term_insight` requires filtering by one campaign ID.

## Module 1C: Search terms within a category

```sql
SELECT
  segments.search_subcategory,
  segments.search_term,
  metrics.impressions,
  metrics.clicks,
  metrics.conversions,
  metrics.conversions_value
FROM campaign_search_term_insight
WHERE segments.date DURING LAST_30_DAYS
  AND campaign_search_term_insight.campaign_id = 'CAMPAIGN_ID'
  AND campaign_search_term_insight.id = 'CATEGORY_ID'
```

## Module 2: Channel distribution (API v23+)

```sql
SELECT
  campaign.name,
  asset_group.id,
  asset_group.name,
  segments.ad_network_type,
  metrics.impressions,
  metrics.clicks,
  metrics.cost_micros,
  metrics.conversions,
  metrics.conversions_value
FROM asset_group
WHERE campaign.advertising_channel_type = 'PERFORMANCE_MAX'
  AND segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC
```

## Module 3A: Asset group performance

```sql
SELECT
  asset_group.id,
  asset_group.name,
  asset_group.primary_status,
  asset_group.ad_strength,
  metrics.impressions,
  metrics.clicks,
  metrics.cost_micros,
  metrics.conversions,
  metrics.conversions_value
FROM asset_group
WHERE campaign.advertising_channel_type = 'PERFORMANCE_MAX'
  AND segments.date DURING LAST_30_DAYS
```

## Module 3B: Asset performance labels

```sql
SELECT
  asset_group_asset.asset,
  asset_group_asset.performance_label,
  asset_group_asset.status
FROM asset_group_asset
WHERE asset_group.id = 'ASSET_GROUP_ID'
  AND asset_group_asset.status != 'REMOVED'
```

## Module 4: Brand traffic detection

No separate query. Reuse Module 1C search term data and classify terms against user-provided brand terms.

`campaign_search_term_insight` does not include `metrics.cost_micros`, so use click share as the traffic proxy.

Plain iteration pattern:

```python
import re

brand_terms = ["acme", "acme inc"]  # user-provided
pattern = re.compile("|".join(re.escape(t.lower()) for t in brand_terms))

brand_clicks = 0
all_clicks = 0
for row in term_rows:
    term = str(row.get("segments.search_term", "")).lower()
    clicks = float(row.get("metrics.clicks", 0) or 0)
    all_clicks += clicks
    if pattern.search(term):
        brand_clicks += clicks

brand_pct = (brand_clicks / all_clicks) if all_clicks > 0 else 0
```

Flag cannibalization when brand click share exceeds 30% of PMax clicks.

## Module 5: Placement visibility

```sql
SELECT
  performance_max_placement_view.display_name,
  performance_max_placement_view.placement,
  performance_max_placement_view.placement_type,
  performance_max_placement_view.target_url,
  metrics.impressions,
  campaign.id
FROM performance_max_placement_view
WHERE campaign.id = 'CAMPAIGN_ID'
  AND segments.date DURING LAST_30_DAYS
```

Placement view supports impressions only.

## Execution pattern (MCP)

1. Run Module 1A query with `mcp__google-ads__query`.
2. For each campaign ID from Module 1A, run Module 1B.
3. Merge all category rows into one list and sort by clicks descending.
4. Take the top 50 categories and run Module 1C for each.
5. Build summaries and recommendations from the returned rows.

## Execution notes

- Query responses include both `_micros` and converted currency fields; use one consistent field family in calculations.
- Run modules in order so campaign/category IDs are available for downstream queries.

## Known limitations

- Insight extraction can be API-call heavy for large PMax accounts.
- Asset labels are relative (`BEST`, `GOOD`, `LOW`, `PENDING`), not direct cost metrics.
- Brand cannibalization analysis requires user-supplied brand terms.
- Channel-level `segments.ad_network_type` data is reliable only for dates after June 1, 2025.
- Placement view supports impressions only (no clicks, cost, or conversions).
