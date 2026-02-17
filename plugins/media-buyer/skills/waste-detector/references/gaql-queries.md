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

Filter in Python — apply both QS and cost thresholds:

```python
df = df.dropna(subset=["ad_group_criterion.quality_info.quality_score"])
df = df[df["ad_group_criterion.quality_info.quality_score"] <= 5]
df = df[df["metrics.cost"] >= 10]  # $10 minimum spend threshold
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

Impression share fields are non-aggregable; use YESTERDAY (single-day) not
LAST_30_DAYS. Filter in Python: `df[df['metrics.search_budget_lost_impression_share'] > 0.10]`.

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

Join in Python to find campaigns with broad match spend and no shared negative list:

```python
protected_campaigns = set(neg_list_df["campaign.id"])
unprotected_broad = broad_df[~broad_df["campaign.id"].isin(protected_campaigns)]
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

Only count ENABLED ads — PAUSED ads do not contribute to testing. GAQL has no
`GROUP BY`; count ads per ad group in Python:

```python
ad_counts = df.groupby(["campaign.id", "ad_group.id"])["ad_group_ad.ad.id"].nunique()
single_ad_groups = ad_counts[ad_counts == 1].reset_index()
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

- See SKILL.md Foundation Dependency for `sys.path` setup before importing.
- Reuse `quick_wasted_spend` and `quick_keyword_performance` where possible.
- Use `pull_report` for custom query groups.
- `pull_report()` auto-converts `_micros` fields and adds derived columns (e.g.
  `metrics.cost`). Use those directly — do not divide by 1,000,000 again.

## Limitations

- Quality score may be null for low-volume keywords.
- Impression share metrics are non-aggregable.
- Placement-level cost is unavailable for some resource views.
