---
name: morning-brief
description: >-
  This skill should be used when the user asks for a "Meta morning brief",
  "Facebook ads daily check", "how are my Meta campaigns doing",
  "Instagram ads performance", "Meta account health", "social ads daily
  summary", "daily Meta check-in", "give me the Facebook rundown",
  "anything weird in my Meta account", "how did my Facebook ads do yesterday",
  "what needs attention on Meta", "what's going on with my Instagram ads",
  "Meta daily report", "Facebook campaign status",
  or mentions Meta Ads monitoring, Facebook campaign health,
  social ads anomaly detection, or Meta spend anomalies.
allowed-tools: mcp__meta-ads__get_ad_accounts, mcp__meta-ads__list_campaigns, mcp__meta-ads__get_campaign_performance, mcp__meta-ads__get_insights, mcp__meta-ads__compare_performance, mcp__meta-ads__list_ad_sets
---

# Meta Ads Morning Brief

Produce a daily, prioritized account-health narrative for Meta Ads (Facebook + Instagram) with actionable items, dollar-quantified anomalies, and UI paths for every fix.

## Account Context

Read `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md` at the start of every run.
If it exists:
- Use known account IDs — skip `get_ad_accounts` discovery.
- Apply KPI targets as anomaly detection thresholds (e.g., flag CPA > target CPA, CPM > ceiling).
- Use frequency cap from profile to calibrate fatigue alerts.
- Note active creative/audience tests when interpreting performance shifts.
- Check watch list for follow-up items from prior sessions.
If it doesn't exist, fall back to `mcp__meta-ads__get_ad_accounts` and suggest running `platform-setup`.

## Key Metrics

| Metric | What It Measures | Anomaly Threshold |
|--------|-----------------|-------------------|
| CPM | Cost per thousand impressions | >20% above 7d avg OR > profile ceiling |
| Frequency | Times shown per person (7d) | >3.0 in any ad set |
| CTR | Click-through rate | >20% decline from 7d avg |
| CPA | Cost per conversion | >profile target CPA |
| ROAS | Return on ad spend | <profile target ROAS |
| Hook Rate | % of video viewers past 3s | <20% (video ads) |
| ThruPlay Rate | % to completion or 15s | <10% (video ads) |
| Quality Ranking | Meta's quality indicator | Below Average or worse |

## Workflow

### Phase 1: Collect data

1. **Campaign performance (today vs 7d vs 30d):**
   Use `mcp__meta-ads__list_campaigns` to get all active campaigns.
   Use `mcp__meta-ads__get_campaign_performance` for each campaign with yesterday, 7d, and 30d windows.
   Metrics: spend, impressions, CPM, clicks, CTR, conversions, CPA, ROAS, frequency.

2. **Ad set delivery status:**
   Use `mcp__meta-ads__list_ad_sets` for each campaign.
   Flag: Learning Limited, Delivery Issue, or any non-Active delivery status.

3. **Period comparison:**
   Use `mcp__meta-ads__compare_performance` for week-over-week and month-over-month trends.

4. **Account-level insights:**
   Use `mcp__meta-ads__get_insights` for account-level aggregated performance.

### Phase 2: Detect anomalies

For each metric, compare yesterday vs 7d baseline:

```
deviation_pct = (yesterday - avg_7d) / avg_7d
dollar_impact = (yesterday_metric - avg_7d_metric) * yesterday_volume
```

Flag when `|deviation_pct| > 0.20` AND `|dollar_impact| > $10`.

**Meta-specific flags:**
- **Learning Limited:** Any ad set stuck in Learning Limited delivery status.
- **Frequency spike:** Any ad set with 7d frequency > 3.0.
- **CPM spike without audience change:** Suggests creative fatigue or auction competition.
- **Delivery issues:** Ad sets with delivery problems (budget constraints, audience too small, billing issues).

Assign severity:
- **HIGH** (>$500/mo projected impact): Broken campaigns, Learning Limited on high-spend ad sets, CPM spikes on primary campaigns.
- **MEDIUM** ($100-500/mo): Frequency violations, declining CTR, budget pacing issues.
- **LOW** ($25-100/mo): Minor metric shifts, low-spend anomalies.
- **INFO** (<$25/mo): Informational observations.

### Phase 3: Budget pacing

For campaigns with **daily budgets:**
```
daily_pacing = yesterday_spend / daily_budget
```
- Flag overpacing: >1.10 (spending faster than expected).
- Flag underpacing: <0.85 (delivery issues or audience saturation).

For campaigns with **lifetime budgets:**
```
days_remaining = end_date - today
remaining_budget = lifetime_budget - total_spend
ideal_daily = remaining_budget / days_remaining
actual_daily = avg_spend_last_3d
pacing_ratio = actual_daily / ideal_daily
```
- Flag overpacing: >1.20 (will exhaust budget early).
- Flag underpacing: <0.80 (will underspend).

### Phase 4: Draft prioritized narrative

Structure output by priority, not by campaign.

## Output Format

```markdown
## Morning Brief - [Date]

### Account Summary
| Metric | Yesterday | 7d Avg | 30d Avg | Trend |
|--------|----------:|-------:|--------:|-------|
| Spend | | | | |
| CPM | | | | |
| CTR | | | | |
| CPA | | | | |
| ROAS | | | | |
| Conversions | | | | |

### Urgent [HIGH]
> Items requiring action today. Each with dollar impact and fix path.

**[Finding title]** — [SEVERITY]
- Impact: $X/mo estimated waste
- Signal: [what triggered the flag]
- Fix: Meta Ads Manager > [exact UI path]
- [Copy-paste artifact if applicable]

### Watch [MEDIUM]
> Monitor — act if trend continues 48 hours.

### Healthy
> Campaigns performing at or above targets.

| Campaign | Objective | Spend | CPA | ROAS | Status |
|----------|-----------|------:|----:|-----:|--------|

### Budget Pacing
| Campaign | Type | Budget | Spend | Pacing | Status |
|----------|------|-------:|------:|-------:|--------|

### Notes
- Attribution: 7-day click / 1-day view (flag if account uses different).
- iOS ATT: Note potential underreporting from opt-outs.
- Learning phase: Campaigns in learning phase are excluded from anomaly flags.
```

## Guardrails

- **Learning phase:** Do NOT flag campaigns in learning phase (<50 conversions/week) as underperforming. Note them separately.
- **Attribution window:** Always note Meta's default 7-day click / 1-day view window. Flag if account uses a different window.
- **iOS privacy:** Note potential underreporting from ATT opt-outs when conversion numbers seem low.
- **Seasonality:** Check if today is a known high/low spending day (weekend, holiday, etc.) before flagging pacing anomalies.
- **Read-only:** This skill produces analysis only. All recommended actions include UI paths — no mutations.

## Profile Maintenance

After completing analysis, if `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md` exists:
1. Update Watch List with any new anomalies flagged in this run.
2. Update Active Tests if user mentioned starting or completing a test.
3. Append to Decision Log if actions were taken.
4. Update "Last updated" date.
Present proposed profile changes to the user before writing.

## References

- `references/thresholds.md` — Anomaly detection thresholds
- `references/benchmarks.md` — 2026 Meta benchmarks by objective and vertical
- `references/ui-paths.md` — Meta Ads Manager UI paths for every action
