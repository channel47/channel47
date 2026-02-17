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

No separate query. Reuse Module 1C search term data and classify against
user-provided brand terms in Python.

**Note:** `campaign_search_term_insight` does NOT include `metrics.cost_micros`.
Use `metrics.clicks` as the proxy for brand traffic share.

```python
import re

brand_terms = ["acme", "acme inc"]  # User provides these
pattern = "|".join(re.escape(t) for t in brand_terms)
brand_traffic = terms_df[terms_df["segments.search_term"].str.lower().str.contains(pattern, na=False)]
brand_clicks = brand_traffic["metrics.clicks"].sum()
total_clicks = terms_df["metrics.clicks"].sum()
brand_pct = brand_clicks / total_clicks if total_clicks > 0 else 0
```

Flag cannibalization when brand click share exceeds 30% of PMax clicks.
Report as click-based share (not spend-based) and note the limitation.

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

## Execution pattern

See SKILL.md Foundation Dependency for `sys.path` setup. Then:

```python
from scripts.google.auth import get_auth
from scripts.google.report import pull_report

client, config = get_auth()
customer_id = config["default_customer_id"]

# Module 1A: get all PMax campaigns
campaigns_df = pull_report(client, customer_id, QUERY_1A)

# Module 1B/1C: loop per campaign (see SKILL.md Module 1 for full pattern)
```

## Execution notes

- `pull_report()` auto-converts `_micros` fields and adds derived columns (e.g.
  `metrics.cost`). Use those directly — do not divide by 1,000,000 again.
- Loop through campaigns from Module 1A before running Module 1B/1C per campaign.

## Known limitations

- Insight extraction can be API-call heavy for large PMax campaigns.
- Asset labels are relative (`BEST`, `GOOD`, `LOW`, `PENDING`), not cost metrics.
- Brand cannibalization analysis requires user-supplied brand terms.
- Channel-level `segments.ad_network_type` data only available for dates after June 1, 2025.
- Placement view supports `metrics.impressions` only — no clicks, cost, or conversions.
