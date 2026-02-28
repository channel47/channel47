# Waste Detector GAQL Queries

## Waste Type 1: Non-converting keywords

```sql
SELECT
  campaign.id,
  campaign.name,
  ad_group.id,
  ad_group.name,
  ad_group_criterion.criterion_id,
  ad_group_criterion.keyword.text,
  ad_group_criterion.keyword.match_type,
  metrics.impressions,
  metrics.clicks,
  metrics.cost_micros,
  metrics.conversions,
  metrics.average_cpc
FROM keyword_view
WHERE segments.date DURING LAST_30_DAYS
  AND ad_group_criterion.status != 'REMOVED'
  AND metrics.cost_micros > 0
  AND metrics.conversions = 0
ORDER BY metrics.cost_micros DESC
```

## Waste Type 2: Low quality score keywords spending

```sql
SELECT
  campaign.name,
  ad_group.name,
  ad_group_criterion.criterion_id,
  ad_group_criterion.keyword.text,
  ad_group_criterion.keyword.match_type,
  ad_group_criterion.quality_info.quality_score,
  ad_group_criterion.quality_info.creative_quality_score,
  ad_group_criterion.quality_info.post_click_quality_score,
  ad_group_criterion.quality_info.search_predicted_ctr,
  metrics.impressions,
  metrics.clicks,
  metrics.cost_micros,
  metrics.conversions,
  metrics.average_cpc
FROM keyword_view
WHERE ad_group_criterion.status != 'REMOVED'
  AND metrics.cost_micros > 0
  AND segments.date DURING LAST_30_DAYS
ORDER BY ad_group_criterion.quality_info.quality_score ASC
```

Apply thresholds with plain iteration:

```python
filtered = []
for row in rows:
    qs = row.get("ad_group_criterion.quality_info.quality_score")
    spend = float(row.get("metrics.cost", 0) or 0)
    if qs is None:
        continue
    if float(qs) <= 5 and spend >= 10:
        filtered.append(row)
```

## Waste Type 3: Display expansion enabled on Search campaigns

```sql
SELECT
  campaign.id,
  campaign.name,
  campaign.status,
  campaign.advertising_channel_type,
  campaign.network_settings.target_google_search,
  campaign.network_settings.target_search_network,
  campaign.network_settings.target_content_network,
  campaign.network_settings.target_partner_search_network,
  metrics.cost_micros,
  metrics.conversions
FROM campaign
WHERE campaign.status != 'REMOVED'
  AND campaign.advertising_channel_type = 'SEARCH'
  AND campaign.network_settings.target_content_network = TRUE
  AND segments.date DURING LAST_30_DAYS
```

## Waste Type 4: Budget-limited campaigns

```sql
SELECT
  campaign.id,
  campaign.name,
  campaign.status,
  campaign.advertising_channel_type,
  campaign_budget.amount_micros,
  metrics.cost_micros,
  metrics.impressions,
  metrics.conversions,
  metrics.search_impression_share,
  metrics.search_budget_lost_impression_share
FROM campaign
WHERE campaign.status != 'REMOVED'
  AND segments.date DURING YESTERDAY
```

Impression share fields are non-aggregable; use YESTERDAY and filter rows where `metrics.search_budget_lost_impression_share > 0.10`.

## Waste Type 5A: Broad match keywords

```sql
SELECT
  campaign.id,
  campaign.name,
  ad_group.name,
  ad_group_criterion.keyword.text,
  ad_group_criterion.keyword.match_type,
  metrics.cost_micros,
  metrics.conversions
FROM keyword_view
WHERE ad_group_criterion.keyword.match_type = 'BROAD'
  AND ad_group_criterion.status != 'REMOVED'
  AND segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC
```

## Waste Type 5B: Shared negative list coverage

```sql
SELECT
  campaign.id,
  campaign.name,
  shared_set.id,
  shared_set.name,
  shared_set.type,
  shared_set.status
FROM campaign_shared_set
WHERE shared_set.type = 'NEGATIVE_KEYWORDS'
  AND shared_set.status = 'ENABLED'
```

Join pattern with plain iteration:

```python
protected = {str(r.get("campaign.id")) for r in negative_list_rows}
unprotected_broad = [
    r for r in broad_rows
    if str(r.get("campaign.id")) not in protected
]
```

## Waste Type 6: Single-ad ad groups

```sql
SELECT
  campaign.id,
  campaign.name,
  ad_group.id,
  ad_group.name,
  ad_group_ad.ad.id,
  ad_group_ad.ad.type,
  ad_group_ad.status
FROM ad_group_ad
WHERE ad_group_ad.status = 'ENABLED'
  AND campaign.status != 'REMOVED'
```

Count enabled ads per ad group using dictionary aggregation:

```python
counts = {}
for row in ad_rows:
    key = (str(row.get("campaign.id")), str(row.get("ad_group.id")))
    ad_id = row.get("ad_group_ad.ad.id")
    if ad_id is None:
        continue
    counts.setdefault(key, set()).add(str(ad_id))

single_ad_groups = [key for key, ad_ids in counts.items() if len(ad_ids) == 1]
```

## Waste Type 7: Zero-impression enabled campaigns

```sql
SELECT
  campaign.id,
  campaign.name,
  campaign.status,
  campaign.advertising_channel_type,
  campaign_budget.amount_micros,
  metrics.impressions
FROM campaign
WHERE campaign.status = 'ENABLED'
  AND segments.date DURING LAST_7_DAYS
```

## Waste Type 8: Semantic mismatch search terms

```sql
SELECT
  search_term_view.search_term,
  campaign.name,
  ad_group.name,
  metrics.clicks,
  metrics.cost_micros,
  metrics.conversions
FROM search_term_view
WHERE segments.date DURING LAST_30_DAYS
  AND metrics.cost_micros > 0
  AND metrics.conversions = 0
ORDER BY metrics.cost_micros DESC
```

## Execution notes

- Run each query via `mcp__google-ads__query`.
- Keep one consistent customer ID and date window across all waste types unless the user requests otherwise.
- Query responses include `_micros` and converted currency fields; choose one for calculations and stay consistent.

## Limitations

- Quality score may be null for low-volume keywords.
- Impression share metrics are non-aggregable.
- Some resource views do not provide full cost and conversion metrics.
