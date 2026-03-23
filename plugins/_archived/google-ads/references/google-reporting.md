# Google Reporting (Morning Brief)

Use `mcp__google-ads__query` for all report pulls.

## Core query sequence

1. Campaign daily performance (30 days) — MB-1
2. Budget pacing and lost impression share (yesterday) — MB-2
3. Disapproved ads — MB-3
4. High-spend, zero-conversion keywords — MB-4
5. Recent change history — MB-5

All GAQL templates are in `gaql-queries.md`.

## Date filtering patterns

Use GAQL date clauses directly:

- `segments.date DURING LAST_7_DAYS`
- `segments.date DURING LAST_30_DAYS`
- `segments.date DURING YESTERDAY`
- `segments.date BETWEEN '2026-01-01' AND '2026-01-31'`

## Processing guidance

- Treat query results as a list of row objects.
- Use row-level iteration for baselines and anomaly math.
- Keep metric math consistent by using one field family (`metrics.cost` or `metrics.cost_micros`) per calculation.

## Common segmentation fields

- Device: `segments.device`
- Day of week: `segments.day_of_week`
- Geography: `segments.geo_target_region`
- Search term: `search_term_view.search_term`

## Recommended execution order

1. Pull campaign summary first.
2. Pull pacing and quality-risk diagnostics.
3. Pull keyword and change-event detail.
4. Produce narrative with `Urgent`, `Watch`, and `Healthy` sections.
