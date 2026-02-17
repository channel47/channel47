---
name: morning-brief
description: >-
  This skill should be used when the user asks for a "morning brief",
  "daily check", "what happened overnight", "account health check",
  "what should I worry about", "how are my campaigns doing", "daily
  summary", "performance check", or mentions daily monitoring, anomaly
  detection, or account health.
---

# Morning Brief

Produce a daily, prioritized account-health narrative with actionable items.

## Foundation Dependency

Use `skills/ad-platform-connection` for auth and reporting execution. Scripts
live in that skill's directory — add it to `sys.path` before importing:

```python
import sys, os
skill_root = os.path.join(os.environ.get("CLAUDE_PLUGIN_ROOT", "."), "skills", "ad-platform-connection")
sys.path.insert(0, skill_root)

from scripts.google.auth import get_auth
from scripts.google.report import pull_report
```

## Workflow

### Phase 1: Collect data (five queries)

Run all queries in `references/gaql-queries.md`:

1. Campaign daily performance (30d).
2. Budget pacing and impression share (yesterday snapshot).
3. Disapproved ads.
4. High-spend, zero-conversion keywords (yesterday).
5. Recent account changes (last 24h).

### Phase 2: Detect and rank anomalies

Use `references/anomaly-formulas.md` for exact formulas. Summary:

For each campaign, for each metric (cost, conversions, CPA, CTR):

1. Compute `baseline_7d` = mean of last 7 days (excluding yesterday).
2. Compute `baseline_30d` = mean of last 30 days (excluding yesterday).
3. Compute `deviation_pct` = `(yesterday - baseline_7d) / baseline_7d`.
4. Compute `dollar_impact` = `yesterday_value - baseline_7d` (for cost/CPA metrics).
   CTR is not dollar-denominated — use deviation_pct only.
5. Surface when BOTH: `|deviation_pct| > 0.20` AND `|dollar_impact| > $10`.
   For CTR: surface when `|deviation_pct| > 0.25` (no dollar gate).
6. Rank all flagged items by `|dollar_impact|` descending.

Cap output at **10 anomaly items** to keep the brief actionable.

### Phase 3: Budget pacing assessment

Google Ads daily budgets are daily targets, not monthly caps. The API returns
`campaign_budget.amount_micros` as a **daily** budget.

For each campaign:

1. `daily_budget` = `campaign_budget.amount_micros` (already converted by pull_report).
2. `monthly_budget` = `daily_budget * 30.4` (Google's average days/month).
3. `day_of_month` = calendar day number.
4. `expected_mtd_spend` = `daily_budget * day_of_month`.
5. `actual_mtd_spend` = sum of daily cost for current month from Query 1.
6. `pacing_ratio` = `actual_mtd_spend / expected_mtd_spend`.
7. Flag overpacing when `pacing_ratio > 1.10` and underpacing when `pacing_ratio < 0.85`.

### Phase 4: Draft prioritized narrative

Structure output as:

- `Urgent`: needs action today.
- `Watch`: monitor or schedule action.
- `Healthy`: stable areas.

Every item must include the likely cause and one concrete next action.

## Output format

```markdown
## Morning Brief - [Date]
### Account: [Account Name] ([Customer ID])

**Overall:** [one-sentence summary]

### Urgent
1. [Issue + impact + recommended action]

### Watch
1. [Issue + impact + recommended action]

### Healthy
- [stability observation]

### Notes
- Data freshness and known caveats
```

## Guardrails

- **Conversion lag**: When yesterday conversions are >30% below 7d baseline, add a
  note that conversions typically backfill for 24-72 hours. Do not flag as "Urgent"
  unless the drop also appears in 2-day-old data.
- Mention change-event delay (~3 min lag) and timestamp cut-off.
- Distinguish between "no issues found" and "insufficient data".
- Keep recommendations operational and specific.
- Cap each priority section: max 5 Urgent, 5 Watch, 5 Healthy items.

## References

- `references/gaql-queries.md`
- `references/anomaly-formulas.md`
