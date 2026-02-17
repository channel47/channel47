# Morning Brief GAQL Queries

## Query 1: Campaign performance with daily segmentation (30 days)

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

## Query 2: Budget pacing and impression share (yesterday)

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

Impression share fields are non-aggregable; keep this separate from Query 1.

## Query 3: Disapproved ads

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

## Query 4: High-spend zero-conversion keywords (yesterday)

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

## Query 5: Recent account changes (last 24 hours)

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

Replace `YESTERDAY_DATE` and `TODAY_DATE` with datetime strings in `YYYY-MM-DD HH:MM:SS`
format (e.g., `2026-02-15 00:00:00`). Bare `YYYY-MM-DD` dates may also work but the
full datetime format is the documented standard for `change_event.change_date_time`.
`change_event` does not use `segments.date`; it uses its own `change_date_time` field.

## Execution notes

- Run each query via `mcp__google-ads__query` with the appropriate GAQL string and customer ID.
- Query 5 requires dynamic date substitution — replace `YESTERDAY_DATE` and `TODAY_DATE` with actual datetime strings before passing to the query tool.
- Query responses include both `_micros` and auto-converted currency fields (e.g. `metrics.cost`). Use the converted fields directly — do not divide by 1,000,000 again.
- Run queries 1–4 first; query 5 can run in parallel since it has no dependency on the others.

## Known limitations

- Change events can lag by about 3 minutes.
- Conversion metrics for yesterday can backfill later.
- Impression share cannot be trended daily from one query.
