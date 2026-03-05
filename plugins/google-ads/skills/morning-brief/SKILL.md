---
name: morning-brief
description: >-
  This skill should be used when the user asks for a "morning brief",
  "daily check", "what happened overnight", "Google Ads health check",
  "what should I worry about", "how are my campaigns doing",
  "daily summary", "give me the rundown", "anything weird in my account",
  "how did my ads do yesterday", "what needs attention",
  "what's going on in my account",
  or mentions daily monitoring, anomaly detection, Google Ads account health,
  spend anomalies, or CPA trending.
allowed-tools: mcp__google-ads__query, mcp__google-ads__list_accounts
---

# Google Ads Morning Brief

Produce a daily, prioritized account-health narrative for Google Ads campaigns with actionable items and budget pacing vs monthly target projection.

## Account Context

Read `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md` at the start of every run.
If it exists:
- Use known account IDs -- skip `list_accounts` discovery.
- Apply KPI targets as anomaly detection thresholds (e.g., flag CPA > target CPA).
- Note active tests when interpreting performance shifts.
- Check watch list for follow-up items from prior sessions.
If it doesn't exist, fall back to `list_accounts` and suggest running `platform-setup`.

## Data Access

### Google Ads

- `mcp__google-ads__query`: Execute GAQL SELECT queries and return structured rows.
- `mcp__google-ads__list_accounts`: Validate account access before reporting when customer scope is unclear.

Use GAQL templates from `references/gaql-queries.md` directly with `mcp__google-ads__query`.

### Connection verification

1. If the profile has account IDs, use them directly.
2. Otherwise, run `mcp__google-ads__list_accounts` to discover accounts.
3. If it fails, report the connection failure and suggest running `platform-setup`.

## Workflow

### Phase 1: Collect data

Execute five queries from `references/gaql-queries.md`:

1. Campaign daily performance (30d).
2. Budget pacing and impression share (yesterday snapshot).
3. Disapproved ads.
4. High-spend, zero-conversion keywords (yesterday).
5. Recent account changes (last 24h).

Run queries 1-4 first. Query 5 can run in parallel since it has no dependency on the others.

### Phase 2: Detect and rank anomalies

Use `references/anomaly-formulas.md` for exact formulas.

For each campaign, for each metric (cost, conversions, CPA, CTR):

1. Compute `baseline_7d` = mean of last 7 days (excluding yesterday).
2. Compute `baseline_30d` = mean of last 30 days (excluding yesterday).
3. Compute `deviation_pct` = `(yesterday - baseline_7d) / baseline_7d`.
4. Compute `dollar_impact` = `yesterday_value - baseline_7d` (for cost/CPA metrics).
   CTR is not dollar-denominated; use deviation_pct only.
5. Surface when BOTH: `|deviation_pct| > 0.20` AND `|dollar_impact| > $10`.
   For CTR: surface when `|deviation_pct| > 0.25` (no dollar gate).
6. Rank all flagged items by `|dollar_impact|` descending.

Cap output at **10 anomaly items** to keep the brief actionable.

### Phase 3: Budget pacing assessment

Google Ads daily budgets are daily targets, not monthly caps.

For each campaign:

1. `daily_budget` = campaign daily budget converted to dollars.
2. `monthly_budget` = `daily_budget * 30.4`.
3. `day_of_month` = calendar day number.
4. `expected_mtd_spend` = `daily_budget * day_of_month`.
5. `actual_mtd_spend` = sum of daily cost for current month from Query 1.
6. `pacing_ratio` = `actual_mtd_spend / expected_mtd_spend`.
7. Flag overpacing when `pacing_ratio > 1.10` and underpacing when `pacing_ratio < 0.85`.

#### Monthly target projection

If the account profile includes a **Monthly Budget** target:

1. `total_mtd_spend` = sum of all campaign MTD spend.
2. `projected_eom_spend` = `total_mtd_spend / day_of_month * days_in_month`.
3. `budget_utilization` = `projected_eom_spend / monthly_budget_target`.
4. Flag when projected spend exceeds target by >10% or falls below target by >15%.

Present both campaign-level pacing and account-level monthly projection.

### Phase 4: Draft prioritized narrative

Structure output with three priority tiers:

- `Urgent`: needs action today.
- `Watch`: monitor or schedule action.
- `Healthy`: stable areas.

Every item must include the likely cause and one concrete next action.

## Output format

```markdown
## Morning Brief - [Date]

### Account
- Google Ads: [Account Name] ([Customer ID]) - [N] campaigns active

**Overall:** [one-sentence account summary]

### Budget Pacing
| Campaign | Daily Budget | MTD Spend | Expected MTD | Pacing | Status |
|---|---:|---:|---:|---:|---|

**Monthly Projection:** $X,XXX projected vs $X,XXX target ([over/under] by X%)

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

- **Conversion lag**: When yesterday conversions are >30% below 7d baseline, add a note that conversions typically backfill for 24-72 hours. Do not flag as "Urgent" unless the drop also appears in 2-day-old data.
- Mention change-event delay (~3 min lag for Google) and timestamp cut-off.
- Distinguish between "no issues found" and "insufficient data".
- Keep recommendations operational and specific.
- Cap each priority section: max 5 Urgent, 5 Watch, 5 Healthy items.
- **Read-only**: This skill produces analysis and recommendations only. No account modifications are made. Recommended actions include Google Ads UI paths where applicable.

## Profile Maintenance

After completing analysis, if `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md` exists:
1. Update Watch List with any new anomalies flagged in this run.
2. Update Active Tests if user mentioned starting or completing a test.
3. Append to Decision Log if actions were taken (pauses, negatives added, etc.).
4. Update "Last updated" date.
Present proposed profile changes to the user before writing.

## References

- `references/gaql-queries.md`
- `references/anomaly-formulas.md`
- `references/google-reporting.md`
