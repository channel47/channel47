# Google Reporting Patterns

Use `scripts/google/report.py` for standard and custom GAQL reporting.

## Quick Helpers

- `quick_campaign_summary()`
- `quick_adgroup_summary()`
- `quick_keyword_performance()`
- `quick_search_terms()`
- `quick_shopping_summary()`
- `quick_wasted_spend()`

All helpers accept `date_range` (default `LAST_30_DAYS`) and return pandas DataFrames.

## Date Filtering

`_build_date_clause()` accepts:

- predefined ranges: `LAST_7_DAYS`, `LAST_30_DAYS`, `THIS_MONTH`, etc.
- explicit range tuple: `("2026-01-01", "2026-01-31")`
- raw expressions: `">= '2026-01-01'"`

Examples:

```python
quick_campaign_summary(client, customer_id, "LAST_30_DAYS")
quick_campaign_summary(client, customer_id, ("2026-01-01", "2026-01-31"))
```

## Custom GAQL

Use `pull_report()` for custom queries.

```python
query = """
SELECT
  campaign.name,
  metrics.impressions,
  metrics.clicks,
  metrics.cost_micros,
  metrics.conversions
FROM campaign
WHERE segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC
"""

df = pull_report(client, customer_id, query)
```

## Flattening and Micros Conversion

`pull_report()` automatically:

- flattens nested protobuf fields into dot notation columns
- converts `_micros` fields to numeric
- adds derived non-micros fields (for example `metrics.cost_micros` -> `metrics.cost`)

## Typical Segmentation Fields

- Device: `segments.device`
- Day of week: `segments.day_of_week`
- Geography: `segments.geo_target_region`
- Search term: `search_term_view.search_term`

## Wasted Spend Workflow

`quick_wasted_spend()` combines:
- keywords with spend and zero conversions
- search terms with spend and zero conversions

Use this output to:
- pause non-performing keywords
- add negatives where intent mismatch is clear
- prioritize budget reallocation

## Recommended Sequence

1. Pull quick summary.
2. Drill into keywords and search terms.
3. Validate findings against campaign goals.
4. Propose mutations with dry-run previews.
