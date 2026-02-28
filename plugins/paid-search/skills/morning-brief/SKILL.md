---
name: morning-brief
description: >-
  This skill should be used when the user asks for a "morning brief",
  "daily check", "what happened overnight", "paid search health check",
  "what should I worry about", "how are my search campaigns doing",
  "daily summary", "search performance check", or mentions daily
  monitoring, anomaly detection, or paid search account health.
allowed-tools: mcp__google-ads__query, mcp__google-ads__list_accounts, mcp__bing-ads__report, mcp__bing-ads__query, mcp__bing-ads__list_accounts
---

# Paid Search Morning Brief

Produce a daily, prioritized account-health narrative across Google Ads and Bing Ads paid search campaigns with actionable items.

## Account Context

Read `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md` at the start of every run.
If it exists:
- Use known account IDs — skip `list_accounts` discovery.
- Apply KPI targets as anomaly detection thresholds (e.g., flag CPA > target CPA).
- Note active tests when interpreting performance shifts.
- Check watch list for follow-up items from prior sessions.
If it doesn't exist, fall back to `list_accounts` and suggest running `platform-setup`.

## Data Access

### Google Ads

- `mcp__google-ads__query`: Execute GAQL SELECT queries and return structured rows.
- `mcp__google-ads__list_accounts`: Validate account access before reporting when customer scope is unclear.

Use GAQL templates from `references/gaql-queries.md` directly with `mcp__google-ads__query`.

### Bing Ads

- `mcp__bing-ads__report`: Generate performance reports (campaign, keyword, search query). Returns parsed CSV data as JSON.
- `mcp__bing-ads__query`: Query campaign structure (campaigns, ad groups, keywords, ads). Read-only.
- `mcp__bing-ads__list_accounts`: Validate account access and discover account IDs.

Use the report tool with `report_type` and `date_range` parameters. See `references/bing-queries.md` for report configurations.

### Platform detection

1. Try `mcp__google-ads__list_accounts` first. If it succeeds, include Google data.
2. Try `mcp__bing-ads__list_accounts`. If it succeeds, include Bing data.
3. If only one platform responds, run the brief for that platform alone. Do not error on a missing platform.
4. If neither responds, report the connection failure and suggest running `platform-setup`.

## Workflow

### Phase 1: Collect data

#### Google Ads (five queries from `references/gaql-queries.md`)

1. Campaign daily performance (30d).
2. Budget pacing and impression share (yesterday snapshot).
3. Disapproved ads.
4. High-spend, zero-conversion keywords (yesterday).
5. Recent account changes (last 24h).

#### Bing Ads (three reports from `references/bing-queries.md`)

1. Campaign performance report (Last30Days, Daily aggregation).
2. Keyword performance report (Yesterday, Daily aggregation).
3. Campaign structure query (campaigns entity) for budget and status context.

Run Google and Bing data collection in parallel where possible.

### Phase 2: Detect and rank anomalies

Use `references/anomaly-formulas.md` for exact formulas. The formulas apply identically to both platforms — they operate on metric values, not platform-specific fields.

For each campaign (Google and Bing), for each metric (cost, conversions, CPA, CTR):

1. Compute `baseline_7d` = mean of last 7 days (excluding yesterday).
2. Compute `baseline_30d` = mean of last 30 days (excluding yesterday).
3. Compute `deviation_pct` = `(yesterday - baseline_7d) / baseline_7d`.
4. Compute `dollar_impact` = `yesterday_value - baseline_7d` (for cost/CPA metrics).
   CTR is not dollar-denominated; use deviation_pct only.
5. Surface when BOTH: `|deviation_pct| > 0.20` AND `|dollar_impact| > $10`.
   For CTR: surface when `|deviation_pct| > 0.25` (no dollar gate).
6. Rank all flagged items by `|dollar_impact|` descending, across both platforms.

Cap output at **10 anomaly items** to keep the brief actionable.

### Phase 3: Budget pacing assessment

#### Google Ads

Google Ads daily budgets are daily targets, not monthly caps.

For each campaign:

1. `daily_budget` = campaign daily budget converted to dollars.
2. `monthly_budget` = `daily_budget * 30.4`.
3. `day_of_month` = calendar day number.
4. `expected_mtd_spend` = `daily_budget * day_of_month`.
5. `actual_mtd_spend` = sum of daily cost for current month from Query 1.
6. `pacing_ratio` = `actual_mtd_spend / expected_mtd_spend`.
7. Flag overpacing when `pacing_ratio > 1.10` and underpacing when `pacing_ratio < 0.85`.

#### Bing Ads

Bing campaign budgets are retrieved via `mcp__bing-ads__query` (campaigns entity returns `daily_budget`). Apply the same pacing formula using daily spend from the campaign performance report.

### Phase 4: Draft prioritized narrative

Structure output as a unified cross-platform brief:

- `Urgent`: needs action today (any platform).
- `Watch`: monitor or schedule action.
- `Healthy`: stable areas.

Every item must include the **platform label** (Google / Bing), the likely cause, and one concrete next action.

## Output format

```markdown
## Morning Brief - [Date]

### Platforms
- Google Ads: [Account Name] ([Customer ID]) - [N] campaigns active
- Bing Ads: [Account Name] ([Account ID]) - [N] campaigns active

**Overall:** [one-sentence cross-platform summary]

### Urgent
1. **[Google/Bing]** [Issue + impact + recommended action]

### Watch
1. **[Google/Bing]** [Issue + impact + recommended action]

### Healthy
- **[Google/Bing]** [stability observation]

### Notes
- Data freshness and known caveats per platform
```

## Guardrails

- **Conversion lag**: When yesterday conversions are >30% below 7d baseline, add a note that conversions typically backfill for 24-72 hours. Do not flag as "Urgent" unless the drop also appears in 2-day-old data. Applies to both platforms.
- Mention change-event delay (~3 min lag for Google) and timestamp cut-off.
- Distinguish between "no issues found" and "insufficient data".
- Keep recommendations operational and specific.
- Cap each priority section: max 5 Urgent, 5 Watch, 5 Healthy items.
- **Bing token rotation**: If `mcp__bing-ads__list_accounts` fails with auth error, note that Microsoft rotates refresh tokens and suggest re-running the OAuth flow.
- **Single-platform graceful**: If one platform is not configured, produce the brief for the available platform without error messaging. Only mention the missing platform in a Notes footer.

## Profile Maintenance

After completing analysis, if `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md` exists:
1. Update Watch List with any new anomalies flagged in this run.
2. Update Active Tests if user mentioned starting or completing a test.
3. Append to Decision Log if actions were taken (pauses, negatives added, etc.).
4. Update "Last updated" date.
Present proposed profile changes to the user before writing.

## References

- `references/gaql-queries.md`
- `references/bing-queries.md`
- `references/anomaly-formulas.md`
- `references/google-reporting.md`
