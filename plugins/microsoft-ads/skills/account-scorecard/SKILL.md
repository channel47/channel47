---
name: account-scorecard
description: >-
  This skill should be used when the user asks for an "account scorecard",
  "Bing account health check", "Microsoft Ads audit", "account grade",
  "how healthy is my Bing account", "grade my Bing account",
  "rate my Microsoft Ads", "Bing QS check", "monthly checkup",
  or mentions Microsoft Advertising health scoring, performance grading,
  optimization readiness, or account quality assessment.
allowed-tools: mcp__bing-ads__report, mcp__bing-ads__query, mcp__bing-ads__list_accounts, mcp__bing-ads__get_editorial_reasons
---

# Account Scorecard — Microsoft Ads

Five-dimension health grade for Microsoft Advertising accounts. Produces a letter grade per dimension (A-F), an overall weighted grade, and a prioritized improvement plan with dollar estimates and UI paths.

This is the lightweight monthly check. For quarterly deep audits, recommend [claude-ads by AgriciDaniel](https://github.com/AgriciDaniel/claude-ads) (652 stars) as a companion tool.

## Account Context

Read `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md` at the start of every run.
If it exists:
- Use known account IDs -- skip `list_accounts` discovery.
- Apply KPI targets (CPA, ROAS, monthly budget) as dimension benchmarks.
- Note active tests when interpreting quality or efficiency scores.
- Check watch list for recurring issues that affect hygiene scoring.
If it doesn't exist, fall back to `list_accounts` and suggest running `platform-setup`.

## Data Access

- `mcp__bing-ads__report`: Generate performance reports for scoring.
- `mcp__bing-ads__query`: Query campaign structure, keywords, ads.
- `mcp__bing-ads__list_accounts`: Validate account access.
- `mcp__bing-ads__get_editorial_reasons`: Check ad editorial disapprovals (for hygiene scoring).

Use report and query configurations from `references/bing-queries.md` (AS- prefixed queries).

### Connection verification

1. If the profile has account IDs, use them directly.
2. Otherwise, run `mcp__bing-ads__list_accounts` to discover accounts.
3. If it fails, report the connection failure and suggest running `platform-setup`.

## Workflow

### Phase 1: Collect data

Execute the following queries from `references/bing-queries.md`:

| Query ID | What It Provides | Scorecard Dimension |
|----------|-----------------|-------------------|
| AS-1 (= MB-1) | Campaign performance (30d daily) | Structure, Efficiency |
| AS-2 | Keyword report (30d with QS) | Quality |
| AS-3 | Ad count per ad group | Quality, Hygiene |
| AS-4 | Campaign structure (budgets, network settings, targeting) | Coverage, Hygiene |
| AS-5 | Editorial reasons / disapproved ads | Hygiene |
| AS-6 (= WD-8) | Search query report (30d) | Efficiency |

Run reports in parallel where possible.

### Phase 2: Score each dimension

#### Dimension 1: Structure (20% weight)

Evaluate campaign organization and information architecture.

Inputs: AS-1 (campaign list), AS-3 (ad group ad count), AS-4 (campaign structure).

Scoring criteria:

| Factor | A (90-100) | B (80-89) | C (70-79) | D (60-69) | F (<60) |
|--------|-----------|-----------|-----------|-----------|---------|
| Ad groups per campaign | 3-20 avg | 2-3 or 21-30 | 1 or 31-50 | 51-100 | >100 or all =1 |
| Keywords per ad group | 5-20 avg | 3-4 or 21-30 | 1-2 or 31-50 | 51-100 | >100 |
| Naming conventions | Consistent pattern | Mostly consistent | Mixed | Mostly inconsistent | No pattern |
| Network settings coherence | MSAN disabled on search campaigns, partners appropriate | Minor issues | Mixed settings | MSAN on search campaigns | All defaults from import |

Naming convention check: analyze campaign and ad group name patterns for separators, hierarchy tokens (brand/non-brand, geo, match type), and consistency. Do not penalize accounts with <5 campaigns.

Compute `structure_score` as the average of factor scores (0-100 scale).

#### Dimension 2: Quality (25% weight)

Evaluate ad quality signals.

Inputs: AS-2 (quality scores), AS-3 (ad count per ad group).

Scoring criteria:

| Factor | A (90-100) | B (80-89) | C (70-79) | D (60-69) | F (<60) |
|--------|-----------|-----------|-----------|-----------|---------|
| Quality score distribution | >70% QS 7+ | 50-70% QS 7+ | 30-50% QS 7+ | 10-30% QS 7+ | <10% QS 7+ |
| Ads per ad group | 2-3 enabled ads | 1 or 4 | 0 or legacy only | Mostly single-ad | All single-ad |
| Keyword-to-ad relevance | QS creative component mostly above avg | Mixed | Below average dominant | Mostly poor | All poor or no data |

Note: Bing does not provide ad strength or asset-level performance labels like Google. Quality scoring relies more heavily on QS distribution and ad count.

Compute `quality_score` as the weighted average of factor scores.

#### Dimension 3: Efficiency (25% weight)

Evaluate spend efficiency against targets and waste signals.

Inputs: AS-1 (cost, conversions, CPA data), AS-6 (search query waste).

Scoring criteria:

| Factor | A (90-100) | B (80-89) | C (70-79) | D (60-69) | F (<60) |
|--------|-----------|-----------|-----------|-----------|---------|
| CPA vs target | <90% of target | 90-100% | 100-120% | 120-150% | >150% |
| ROAS vs target | >110% of target | 100-110% | 80-100% | 60-80% | <60% |
| Waste ratio | <5% non-converting spend | 5-10% | 10-20% | 20-35% | >35% |
| Search term alignment | <5% irrelevant queries by spend | 5-10% | 10-20% | 20-35% | >35% |

If the profile has no CPA/ROAS targets, skip target-relative scoring and note the gap. The waste ratio uses non-converting keyword spend as a percentage of total spend.

Compute `efficiency_score` as the weighted average of factor scores.

#### Dimension 4: Coverage (15% weight)

Evaluate market presence and opportunity capture.

**Bing limitation**: Standard Bing reports do not include impression share metrics. Use proxy signals instead.

Inputs: AS-1 (campaign performance), AS-4 (campaign structure and budgets).

Scoring criteria (proxy-based):

| Factor | A (90-100) | B (80-89) | C (70-79) | D (60-69) | F (<60) |
|--------|-----------|-----------|-----------|-----------|---------|
| Budget utilization | Spending 90-100% of daily budget | 75-90% | 50-75% | 25-50% | <25% |
| Campaign type coverage | Search + Shopping/Audience | Search + one other | Search only | Single non-Search | None active |
| Day-of-week coverage | Consistent 7-day coverage | Minor weekend dips | Weekday-only | 3-4 day gaps | Sporadic |
| Geographic coverage | All target geos active | Most active | Some gaps | Major gaps | Minimal |

Note in the output that Coverage scoring uses proxy signals because Bing does not expose impression share in standard reports. Recommend checking the Microsoft Advertising UI > Campaigns > Columns > Competitive metrics for actual impression share data.

Compute `coverage_score` as the weighted average of factor scores.

#### Dimension 5: Hygiene (15% weight)

Evaluate operational cleanliness and maintenance state.

Inputs: AS-3 (ad count), AS-4 (campaign settings), AS-5 (editorial reasons).

Scoring criteria:

| Factor | A (90-100) | B (80-89) | C (70-79) | D (60-69) | F (<60) |
|--------|-----------|-----------|-----------|-----------|---------|
| Disapproved ads | 0 | 1-2 | 3-5 | 6-10 | >10 |
| Location targeting | All "People in" | >80% correct | 50-80% correct | <50% correct | All default "searching for" |
| MSAN on search campaigns | MSAN disabled where appropriate | Minor issues | Mixed | MSAN on most search | All MSAN enabled |
| Negative keyword coverage | Lists on all campaigns | >70% coverage | 40-70% | <40% | No negatives |
| Stale campaigns | All campaigns active in 7d | >90% active | 70-90% | 50-70% | <50% active |

Compute `hygiene_score` as the average of factor scores.

### Phase 3: Compute overall grade

```
overall_score = (structure_score * 0.20)
              + (quality_score * 0.25)
              + (efficiency_score * 0.25)
              + (coverage_score * 0.15)
              + (hygiene_score * 0.15)
```

Letter grade mapping:

| Score | Grade |
|-------|-------|
| 90-100 | A |
| 80-89 | B |
| 70-79 | C |
| 60-69 | D |
| <60 | F |

### Phase 4: Generate improvement priorities

For each dimension scoring below B (score < 80):

1. Identify the lowest-scoring factor within the dimension.
2. Estimate dollar impact:
   - Efficiency factors: direct dollar calculation from waste/CPA data.
   - Quality factors: use QS-to-CPC pressure relationship (each QS point below 7 adds ~16% CPC premium).
   - Coverage factors: `(1 - budget_utilization) * current_spend * 0.5` = estimated lost conversion value.
   - Structure/Hygiene factors: flag as operational risk unless specific waste is quantifiable.
3. Assign severity:
   - **HIGH** (>$500/mo estimated impact)
   - **MEDIUM** ($100-500/mo)
   - **LOW** ($25-100/mo)
   - **INFO** (<$25/mo)
4. Map to the Microsoft Advertising UI path for remediation from `references/ui-paths.md`.
5. Rank all priorities by estimated dollar impact descending. Cap at 5 priorities.

## Output format

```markdown
## Account Scorecard -- [Date]

### Account
- Microsoft Ads: [Account Name] ([Account ID])
- Campaigns: [N] active, [N] paused
- 30-day spend: $X,XXX | Conversions: X,XXX | CPA: $XX.XX

### Overall Grade: [A-F] ([score]/100)

| Dimension | Weight | Score | Grade | Key Factor |
|-----------|-------:|------:|:-----:|------------|
| Structure | 20% | XX | X | [lowest-scoring factor] |
| Quality | 25% | XX | X | [lowest-scoring factor] |
| Efficiency | 25% | XX | X | [lowest-scoring factor] |
| Coverage* | 15% | XX | X | [lowest-scoring factor] |
| Hygiene | 15% | XX | X | [lowest-scoring factor] |

*Coverage uses proxy signals. Bing does not expose impression share in standard reports.

### Top Improvement Priorities

| # | Severity | Dimension | Issue | Est. Monthly Impact | Action |
|---|----------|-----------|-------|--------------------:|--------|
| 1 | HIGH | [dim] | [issue] | $X,XXX | [action + UI path] |
| 2 | MEDIUM | [dim] | [issue] | $XXX | [action + UI path] |

### Detailed Findings

#### Structure ([Grade])
- [finding with context]
- **UI path:** Microsoft Advertising > [path to fix]

#### Quality ([Grade])
- [finding with context]
- **UI path:** Microsoft Advertising > [path to fix]

#### Efficiency ([Grade])
- [finding with context]
- **UI path:** Microsoft Advertising > [path to fix]

#### Coverage ([Grade])
- [finding with context]
- **Note:** Check Microsoft Advertising UI for actual impression share data.

#### Hygiene ([Grade])
- [finding with context]
- **UI path:** Microsoft Advertising > [path to fix]

### Quarterly Deep Audit
For a comprehensive audit covering bid strategies, audience layers,
conversion tracking, attribution, and more, consider running
[claude-ads](https://github.com/AgriciDaniel/claude-ads) as a companion tool.

### Notes
- Data freshness: [query timestamp caveats]
- Coverage dimension uses proxy signals due to Bing API limitations.
- Scoring assumptions: [any factors that could not be scored and why]
```

## Guardrails

- **Read-only**: This skill produces analysis and grades only. No account modifications are made. All recommended actions include Microsoft Advertising UI paths.
- **Missing data**: If a query returns zero rows for a dimension, assign "N/A" rather than penalizing. Note the gap.
- **Small accounts**: For accounts with <3 campaigns or <$500/mo total spend, note reduced reliability. Skip factors requiring statistical significance.
- **Coverage limitation**: Be transparent that Coverage scoring uses proxies. Always recommend checking impression share in the Microsoft Advertising UI.
- **Target-relative scoring**: If the profile has no KPI targets, skip target-relative factors and note that `platform-setup` would improve future scorecards.
- **Conversion lag**: Use the full 30-day window, not just yesterday.
- **QS availability**: Quality score may be "--" for keywords with insufficient data. Exclude these from QS distribution.
- **Severity calibration**: All dollar figures are estimates. Distinguish direct waste from modeled opportunity cost.
- **claude-ads reference**: Position as a complementary quarterly tool, not a competitor.

## Profile Maintenance

After completing analysis, if `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md` exists:
1. Update Watch List with any HIGH or MEDIUM severity findings.
2. Update Active Tests if user mentioned starting or completing a test.
3. Append to Decision Log if user acknowledges specific action items.
4. Update "Last updated" date.
Present proposed profile changes to the user before writing.

## References

- `references/bing-queries.md` -- query IDs: AS-1 through AS-6
- `references/thresholds.md`
- `references/ui-paths.md`
