# GAQL Query Reference

Consolidated GAQL queries used across all google-ads plugin skills. Run via `mcp__google-ads__query`.

## Morning Brief Queries

### MB-1: Campaign daily performance (30 days)

```sql
SELECT
  campaign.id,
  campaign.name,
  campaign.status,
  campaign.advertising_channel_type,
  segments.date,
  metrics.impressions,
  metrics.clicks,
  metrics.ctr,
  metrics.cost_micros,
  metrics.conversions,
  metrics.conversions_value,
  metrics.cost_per_conversion
FROM campaign
WHERE campaign.status != 'REMOVED'
  AND segments.date DURING LAST_30_DAYS
ORDER BY segments.date DESC
```

### MB-2: Budget pacing and impression share (yesterday)

```sql
SELECT
  campaign.id,
  campaign.name,
  campaign.status,
  campaign_budget.amount_micros,
  metrics.cost_micros,
  metrics.search_impression_share,
  metrics.search_budget_lost_impression_share,
  metrics.search_rank_lost_impression_share
FROM campaign
WHERE campaign.status != 'REMOVED'
  AND segments.date DURING YESTERDAY
```

Impression share fields are non-aggregable; keep separate from MB-1.

### MB-3: Disapproved ads

```sql
SELECT
  campaign.id,
  campaign.name,
  ad_group.id,
  ad_group.name,
  ad_group_ad.ad.id,
  ad_group_ad.ad.type,
  ad_group_ad.policy_summary.approval_status,
  ad_group_ad.policy_summary.policy_topic_entries
FROM ad_group_ad
WHERE ad_group_ad.policy_summary.approval_status IN ('DISAPPROVED', 'AREA_OF_INTEREST_ONLY')
  AND ad_group_ad.status != 'REMOVED'
```

### MB-4: High-spend zero-conversion keywords (yesterday)

```sql
SELECT
  campaign.name,
  ad_group.name,
  ad_group_criterion.keyword.text,
  ad_group_criterion.keyword.match_type,
  metrics.clicks,
  metrics.cost_micros,
  metrics.conversions
FROM keyword_view
WHERE segments.date DURING YESTERDAY
  AND ad_group_criterion.status != 'REMOVED'
  AND metrics.cost_micros > 0
  AND metrics.conversions = 0
ORDER BY metrics.cost_micros DESC
```

### MB-5: Recent account changes (last 24 hours)

```sql
SELECT
  change_event.change_date_time,
  change_event.change_resource_name,
  change_event.user_email,
  change_event.change_resource_type,
  change_event.resource_change_operation,
  change_event.changed_fields
FROM change_event
WHERE change_event.change_date_time >= 'YESTERDAY_DATE'
  AND change_event.change_date_time <= 'TODAY_DATE'
ORDER BY change_event.change_date_time DESC
LIMIT 10000
```

Replace `YESTERDAY_DATE` and `TODAY_DATE` with datetime strings in `YYYY-MM-DD HH:MM:SS` format.

## Waste Detector Queries

### WD-1: Non-converting keywords (30d)

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

### WD-2: Low quality score keywords

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

Filter: quality_score <= 5 AND spend >= $10.

### WD-3: Display expansion on Search campaigns

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

### WD-4: Budget-limited campaigns

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

Filter: search_budget_lost_impression_share > 0.10.

### WD-5A: Broad match keywords

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

### WD-5B: Shared negative list coverage

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

Join: campaigns with broad keywords (WD-5A) that lack shared negative lists.

### WD-6: Single-ad ad groups

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

Count enabled ads per ad group; flag groups with exactly 1.

### WD-7: Zero-impression enabled campaigns

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

### WD-8: Non-converting search terms

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

## Search Term Verdict Queries

### STV-A: Full search-term report

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

### STV-B: Keyword mapping (Search only)

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

Adding `segments.keyword.info.text` limits to Search keyword traffic (excludes Shopping, DSA, PMax).

## PMax Decoder Queries

### PM-1A: PMax campaign list

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

### PM-1B: Search term insight categories

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

Requires single-campaign filtering.

### PM-1C: Search terms within category

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

### PM-2: Channel distribution (API v23+)

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

### PM-3A: Asset group performance

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

### PM-3B: Asset performance labels

```sql
SELECT
  asset_group_asset.asset,
  asset_group_asset.performance_label,
  asset_group_asset.status
FROM asset_group_asset
WHERE asset_group.id = 'ASSET_GROUP_ID'
  AND asset_group_asset.status != 'REMOVED'
```

### PM-5: Placement visibility

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

Placement view supports impressions only (no clicks, cost, or conversions).

## Ad Copy Analyzer Queries

### ACA-1: RSA performance by ad

```sql
SELECT
  campaign.id,
  campaign.name,
  ad_group.id,
  ad_group.name,
  ad_group_ad.ad.id,
  ad_group_ad.ad.type,
  ad_group_ad.ad.responsive_search_ad.headlines,
  ad_group_ad.ad.responsive_search_ad.descriptions,
  ad_group_ad.ad.final_urls,
  ad_group_ad.ad_strength,
  metrics.impressions,
  metrics.clicks,
  metrics.ctr,
  metrics.cost_micros,
  metrics.conversions,
  metrics.conversions_value,
  metrics.cost_per_conversion
FROM ad_group_ad
WHERE ad_group_ad.ad.type = 'RESPONSIVE_SEARCH_AD'
  AND ad_group_ad.status = 'ENABLED'
  AND campaign.status != 'REMOVED'
  AND segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC
```

### ACA-2: Asset-level performance

```sql
SELECT
  ad_group_ad_asset_view.asset,
  ad_group_ad_asset_view.field_type,
  ad_group_ad_asset_view.performance_label,
  ad_group_ad_asset_view.pinned_field,
  ad_group_ad.ad.id,
  campaign.name,
  ad_group.name,
  metrics.impressions,
  metrics.clicks,
  metrics.cost_micros,
  metrics.conversions
FROM ad_group_ad_asset_view
WHERE ad_group_ad.status = 'ENABLED'
  AND campaign.status != 'REMOVED'
  AND segments.date DURING LAST_30_DAYS
ORDER BY metrics.impressions DESC
```

## Account Scorecard Queries

### AS-1: Campaign structure overview

Reuses MB-1 (campaign daily performance).

### AS-2: Quality score distribution

Reuses WD-2 (quality score query).

### AS-3: Ad coverage

Reuses WD-6 (single-ad ad groups).

### AS-4: Impression share

Reuses MB-2 (pacing and impression share).

### AS-5: Negative keyword coverage

Reuses WD-5B (shared negative list coverage).

## Competitor Intel Queries

### CI-1: Auction insights

```sql
SELECT
  campaign.id,
  campaign.name,
  metrics.auction_insight_search_impression_share,
  metrics.auction_insight_search_overlap_rate,
  metrics.auction_insight_search_position_above_rate,
  metrics.auction_insight_search_top_impression_percentage,
  metrics.auction_insight_search_absolute_top_impression_percentage,
  metrics.auction_insight_search_outranking_share
FROM campaign
WHERE campaign.status != 'REMOVED'
  AND segments.date DURING LAST_30_DAYS
```

Note: Auction insights may require the `auction_insight` resource for per-domain data. Use the campaign-level report above for overall competitive position.

## Execution Notes

- Run all queries via `mcp__google-ads__query` with GAQL string and customer ID.
- Query responses include both `_micros` and auto-converted currency fields. Use converted fields directly.
- Change events (MB-5) require dynamic date substitution.
- `campaign_search_term_insight` requires single-campaign filtering.
- Impression share fields are non-aggregable; use YESTERDAY date range.
- Channel-level `segments.ad_network_type` data reliable only after June 1, 2025.
