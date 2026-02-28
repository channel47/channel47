# Morning Brief Anomaly Detection Formulas

Apply these formulas consistently. Do not invent alternative thresholds.

## Input data

Use Query 1 daily performance data from `gaql-queries.md`.

- Input format: list of rows from `mcp__google-ads__query`
- Each row should include `campaign.id`, `segments.date`, `metrics.cost`, `metrics.conversions`, and `metrics.ctr`

## Baseline windows

Let `yesterday` be current date minus one day.

- 7-day baseline window: days -8 through -2 (excludes yesterday)
- 30-day baseline window: days -31 through -2 (excludes yesterday)

## Plain iteration pattern

```python
from datetime import date, timedelta

rows = query_rows  # list[dict]
yesterday = date.today() - timedelta(days=1)

# Group rows by campaign ID
by_campaign = {}
for row in rows:
    campaign_id = str(row["campaign.id"])
    by_campaign.setdefault(campaign_id, []).append(row)

summaries = []
for campaign_id, campaign_rows in by_campaign.items():
    # Keep only rows in the last 31 days so we can compute both baselines.
    dated_rows = [
        r for r in campaign_rows
        if "segments.date" in r
    ]

    # Split into windows using date comparisons in your implementation.
    rows_7d = [...]
    rows_30d = [...]
    row_yesterday = ...

    if len(rows_7d) < 7 or row_yesterday is None:
        summaries.append({"campaign.id": campaign_id, "status": "insufficient_baseline"})
        continue

    baseline_7d_cost = sum(r.get("metrics.cost", 0) for r in rows_7d) / len(rows_7d)
    baseline_7d_conv = sum(r.get("metrics.conversions", 0) for r in rows_7d) / len(rows_7d)
    baseline_7d_ctr = sum(r.get("metrics.ctr", 0) for r in rows_7d) / len(rows_7d)
    baseline_7d_cpa = (
        baseline_7d_cost / baseline_7d_conv if baseline_7d_conv > 0 else None
    )

    summaries.append(
        {
            "campaign.id": campaign_id,
            "yesterday": row_yesterday,
            "baseline_7d_cost": baseline_7d_cost,
            "baseline_7d_conv": baseline_7d_conv,
            "baseline_7d_ctr": baseline_7d_ctr,
            "baseline_7d_cpa": baseline_7d_cpa,
        }
    )
```

## Deviation formulas

For each metric:

```python
deviation_pct = (yesterday_value - baseline_7d) / baseline_7d if baseline_7d != 0 else None
```

Dollar impact depends on metric type:

| Metric | Dollar Impact Formula |
|--------|----------------------|
| Cost | `yesterday_cost - baseline_7d_cost` |
| Conversions | `(baseline_7d_conv - yesterday_conv) * baseline_7d_cpa` |
| CPA | `(yesterday_cpa - baseline_7d_cpa) * yesterday_conv` |
| CTR | Not dollar-denominated; use `deviation_pct` only |

## Threshold gate

Flag an anomaly only when both conditions are met:

1. `abs(deviation_pct) > 0.20`
2. `abs(dollar_impact) > 10.00`

For CTR, flag when `abs(deviation_pct) > 0.25` (no dollar gate).

## Ranking

Sort all flagged anomalies by `abs(dollar_impact)` descending and cap at 10 items.

## Direction labels

| deviation_pct | Label |
|---------------|-------|
| > 0.20 for cost/CPA | Cost spike / CPA spike |
| < -0.20 for cost | Spend drop |
| < -0.20 for conversions | Conversion drop |
| > 0.20 for conversions | Conversion surge |
| < -0.25 for CTR | CTR decline |
| > 0.25 for CTR | CTR surge (positive, usually `Watch`) |

## Edge cases

- **New campaigns** (< 7 days of data): skip anomaly detection and note "insufficient baseline".
- **Zero baseline**: if baseline is 0, do not compute deviation percentage; mark as "new activity" with raw value.
- **Calendar effects**: if yesterday is Monday or holiday-adjacent, note potential weekday bias.
