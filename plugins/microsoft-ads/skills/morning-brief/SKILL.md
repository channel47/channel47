---
name: morning-brief
description: >-
  This skill should be used when the user asks for a "morning brief",
  "daily check", "what happened overnight", "Microsoft Ads health check",
  "Bing Ads health check", "what should I worry about",
  "how are my Bing campaigns doing", "daily summary",
  "how did Bing do yesterday", "what needs attention",
  "what's going on in my Bing account",
  or mentions daily monitoring, anomaly detection,
  Microsoft Advertising account health, or Bing spend anomalies.
allowed-tools: mcp__bing-ads__report, mcp__bing-ads__query, mcp__bing-ads__list_accounts
---

# Microsoft Ads Morning Brief

Produce a daily, prioritized account-health narrative for Microsoft Advertising campaigns with actionable items, budget pacing vs monthly target projection, bot traffic monitoring, and import drift detection.

## Account Context

Read `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md` at the start of every run.
If it exists:
- Use known account IDs -- skip `list_accounts` discovery.
- Apply KPI targets as anomaly detection thresholds (e.g., flag CPA > target CPA).
- Note active tests when interpreting performance shifts.
- Check watch list for follow-up items from prior sessions.
- Read Import Config for auto-import drift detection.
If it doesn't exist, fall back to `list_accounts` and suggest running `platform-setup`.

## Data Access

- `mcp__bing-ads__report`: Generate performance reports (campaign, keyword, search query). Returns parsed CSV data as JSON.
- `mcp__bing-ads__query`: Query campaign structure (campaigns, ad groups, keywords, ads). Read-only.
- `mcp__bing-ads__list_accounts`: Validate account access and discover account IDs.

Use the report tool with `report_type` and `date_range` parameters. See `references/bing-queries.md` for report configurations.

### Connection verification

1. If the profile has account IDs, use them directly.
2. Otherwise, run `mcp__bing-ads__list_accounts` to discover accounts.
3. If it fails, report the connection failure and suggest running `platform-setup`.
4. If auth fails with token error, note that Microsoft rotates refresh tokens and suggest re-running the OAuth flow.

## Workflow

### Phase 1: Collect data

Execute four data pulls from `references/bing-queries.md`:

1. **MB-1**: Campaign performance report (30d, Daily aggregation).
2. **MB-2**: Keyword performance report (Yesterday, Daily aggregation).
3. **MB-3**: Campaign structure query for budget, status, and network settings.
4. **MB-4**: Search query report (Yesterday) for bot traffic signal detection.

Run reports 1, 2, and 4 in parallel. Query 3 depends on account access confirmation.

### Phase 2: Detect and rank anomalies

Use `references/anomaly-formulas.md` for exact formulas. The formulas are platform-agnostic -- they operate on metric values, not platform-specific fields.

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

### Phase 3: Bot traffic monitoring

Analyze yesterday's data for suspicious click patterns that indicate bot or invalid traffic:

1. **High click, zero conversion campaigns**: Flag campaigns with clicks > 50 and conversions = 0 yesterday.
2. **Geographic anomalies**: If geo data is available, flag unexpected spikes from geos not in targeting.
3. **Device anomalies**: Flag campaigns where a single device type accounts for >80% of clicks with zero conversions.
4. **CTR outliers**: Flag keywords or campaigns with CTR > 15% combined with zero conversions (likely click fraud).

Present bot traffic signals as a separate section. These are signals, not confirmations -- recommend checking Microsoft Advertising's Invalid Clicks report in the UI.

### Phase 4: Import drift detection

If the account profile has Import Config data:

1. Check if auto-import is enabled and the last known import date.
2. Compare current campaign settings (from MB-3) against expected settings:
   - MSAN distribution unexpectedly enabled (common auto-import side effect).
   - Search partners unexpectedly enabled.
   - Budget changes that don't match manual adjustments in the Decision Log.
3. Flag any drift as a Watch item with the specific setting that changed.

If no Import Config exists, skip this phase.

### Phase 5: Budget pacing assessment

Bing campaign budgets are retrieved via `mcp__bing-ads__query` (campaigns entity returns `daily_budget`).

For each campaign:

1. `daily_budget` = campaign daily budget from structure query.
2. `monthly_budget` = `daily_budget * 30.4`.
3. `day_of_month` = calendar day number.
4. `expected_mtd_spend` = `daily_budget * day_of_month`.
5. `actual_mtd_spend` = sum of daily cost for current month from MB-1.
6. `pacing_ratio` = `actual_mtd_spend / expected_mtd_spend`.
7. Flag overpacing when `pacing_ratio > 1.10` and underpacing when `pacing_ratio < 0.85`.

#### Monthly target projection

If the account profile includes a **Monthly Budget** target:

1. `total_mtd_spend` = sum of all campaign MTD spend.
2. `projected_eom_spend` = `total_mtd_spend / day_of_month * days_in_month`.
3. `budget_utilization` = `projected_eom_spend / monthly_budget_target`.
4. Flag when projected spend exceeds target by >10% or falls below target by >15%.

Present both campaign-level pacing and account-level monthly projection.

### Phase 6: Draft prioritized narrative

Structure output with three priority tiers:

- `Urgent`: needs action today.
- `Watch`: monitor or schedule action.
- `Healthy`: stable areas.

Every item must include the likely cause and one concrete next action with a Microsoft Advertising UI path.

## Output format

```markdown
## Morning Brief - [Date]

### Account
- Microsoft Ads: [Account Name] ([Account ID]) - [N] campaigns active

**Overall:** [one-sentence account summary]

### Budget Pacing
| Campaign | Daily Budget | MTD Spend | Expected MTD | Pacing | Status |
|---|---:|---:|---:|---:|---|

**Monthly Projection:** $X,XXX projected vs $X,XXX target ([over/under] by X%)

### Bot Traffic Signals
| Campaign | Signal | Clicks | Conv | CTR | Recommended Check |
|---|---|---:|---:|---:|---|

(If no signals detected: "No suspicious click patterns detected yesterday.")

### Import Drift
- [drift findings or "No import drift detected."]

### Urgent
1. [Issue + dollar impact + recommended action + UI path]

### Watch
1. [Issue + dollar impact + recommended action + UI path]

### Healthy
- [stability observation]

### Notes
- Data freshness: Bing reports reflect data through yesterday's close.
- **Limitations**: No change event history available via API. No ad disapproval data in reports -- check Microsoft Advertising UI > Ad Extensions & Ads > Ads for editorial status. No impression share in standard reports -- use budget pacing as a proxy for coverage.
```

## Guardrails

- **Conversion lag**: When yesterday conversions are >30% below 7d baseline, add a note that conversions typically backfill for 24-72 hours. Do not flag as "Urgent" unless the drop also appears in 2-day-old data.
- **Bing data differences**: Spend is already in dollars (no micros conversion). CTR is returned as a percentage string -- parse to float for math.
- **No change events**: Bing API does not expose account change logs. Note this limitation rather than omitting historical context.
- **No disapproval data**: Ad editorial status is not available via the reporting API. Note this in the output.
- **No impression share**: Standard Bing reports do not include impression share. Use budget pacing and spend-to-budget ratio as proxy signals for coverage gaps.
- Distinguish between "no issues found" and "insufficient data".
- Keep recommendations operational and specific with UI paths from `references/ui-paths.md`.
- Cap each priority section: max 5 Urgent, 5 Watch, 5 Healthy items.
- **Read-only**: This skill produces analysis and recommendations only. No account modifications are made.

## Profile Maintenance

After completing analysis, if `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md` exists:
1. Update Watch List with any new anomalies flagged in this run.
2. Update Active Tests if user mentioned starting or completing a test.
3. Append to Decision Log if actions were taken (pauses, negatives added, etc.).
4. Update "Last updated" date.
Present proposed profile changes to the user before writing.

## References

- `references/bing-queries.md`
- `references/anomaly-formulas.md`
- `references/ui-paths.md`
