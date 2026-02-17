# Morning Brief Anomaly Detection Formulas

Apply these formulas consistently. Do not invent alternative thresholds.

## Input data

Use Query 1 daily performance data from `gaql-queries.md`. Group by campaign and
`segments.date`. Use `metrics.cost` (auto-converted from micros by `pull_report`).

## Baseline computation

```python
import pandas as pd
from datetime import date, timedelta

yesterday = date.today() - timedelta(days=1)

# 7-day baseline: days -8 through -2 (excludes yesterday)
baseline_start_7d = yesterday - timedelta(days=7)
baseline_end_7d = yesterday - timedelta(days=1)

# 30-day baseline: days -31 through -2 (excludes yesterday)
baseline_start_30d = yesterday - timedelta(days=30)
baseline_end_30d = yesterday - timedelta(days=1)
```

For each campaign, compute:

```python
baseline_7d_cost = df_7d["metrics.cost"].mean()
baseline_7d_conv = df_7d["metrics.conversions"].mean()
baseline_7d_cpa  = baseline_7d_cost / baseline_7d_conv if baseline_7d_conv > 0 else None
baseline_7d_ctr  = df_7d["metrics.ctr"].mean()
```

## Deviation formulas

For each metric:

```python
deviation_pct = (yesterday_value - baseline_7d) / baseline_7d if baseline_7d != 0 else None
```

Dollar impact depends on metric type:

| Metric | Dollar Impact Formula |
|--------|----------------------|
| Cost   | `yesterday_cost - baseline_7d_cost` |
| Conversions | `(baseline_7d_conv - yesterday_conv) * baseline_7d_cpa` (reversed so a drop yields positive impact) |
| CPA    | `(yesterday_cpa - baseline_7d_cpa) * yesterday_conv` |
| CTR    | Not dollar-denominated; use deviation_pct only |

## Threshold gate

Flag an anomaly only when **both** conditions are met:

1. `|deviation_pct| > 0.20` (20% change)
2. `|dollar_impact| > 10.00` ($10 minimum)

For CTR, flag when `|deviation_pct| > 0.25` (no dollar gate).

## Ranking

Sort all flagged anomalies by `|dollar_impact|` descending. Cap at 10 items total.

## Direction labels

| deviation_pct | Label |
|---------------|-------|
| > 0.20 for cost/CPA | Cost spike / CPA spike |
| < -0.20 for cost | Spend drop |
| < -0.20 for conversions | Conversion drop |
| > 0.20 for conversions | Conversion surge |
| < -0.25 for CTR | CTR decline |
| > 0.25 for CTR | CTR surge (generally positive — note but do not flag as Urgent) |

## Edge cases

- **New campaigns** (< 7 days of data): skip anomaly detection, note as "insufficient
  baseline" in the brief.
- **Zero-baseline metrics**: if baseline is 0, do not compute deviation_pct. Report
  the raw yesterday value with a "new activity" label.
- **Weekend/weekday patterns**: if yesterday is Monday or a holiday, note that lower
  volume may be calendar-driven, not a true anomaly. Still flag if thresholds are met,
  but add context.
