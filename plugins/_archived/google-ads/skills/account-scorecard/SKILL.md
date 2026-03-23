---
name: account-scorecard
description: >-
  This skill should be used when the user asks for an "account scorecard",
  "account health check", "Google Ads audit", "account grade",
  "how healthy is my account", "account assessment", "monthly checkup",
  "grade my account", "rate my Google Ads", "QS check",
  "account review", "quarterly review", "optimization readiness",
  "how good is my account", "account quality", "give my account a grade",
  or mentions account health scoring, performance grading,
  optimization readiness, or account quality assessment.
allowed-tools: mcp__google-ads__query, mcp__google-ads__list_accounts
---

# Account Scorecard -- Google Ads

Five-dimension health grade for Google Ads accounts. Produces a letter grade per dimension (A-F), an overall weighted grade, and a prioritized improvement plan with dollar estimates and UI paths.

This is the lightweight monthly check. For quarterly 60-point deep audits, recommend [claude-ads by AgriciDaniel](https://github.com/AgriciDaniel/claude-ads) (652 stars, 74 Google-specific checks) as a companion tool. Our scorecard identifies the top priorities; claude-ads covers the long tail.

## Account Context

Read `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md` at the start of every run.
If it exists:
- Use known account IDs -- skip `list_accounts` discovery.
- Apply KPI targets (CPA, ROAS, monthly budget, impression share) as dimension benchmarks.
- Note active tests when interpreting quality or efficiency scores.
- Check watch list for recurring issues that affect hygiene scoring.
If it doesn't exist, fall back to `list_accounts` and suggest running `platform-setup`.

## Data Access

- `mcp__google-ads__query`: Execute GAQL SELECT queries and return structured rows.
- `mcp__google-ads__list_accounts`: Validate account access before scoring when customer scope is unclear.

Use GAQL templates from `references/gaql-queries.md` directly with `mcp__google-ads__query`.

### Connection verification

1. If the profile has account IDs, use them directly.
2. Otherwise, run `mcp__google-ads__list_accounts` to discover accounts.
3. If it fails, report the connection failure and suggest running `platform-setup`.

## Workflow

### Phase 1: Collect data

Execute the following queries from `references/gaql-queries.md`. All are reused from existing skills -- no new queries needed:

| Query ID | Source Skill | What It Provides | Scorecard Dimension |
|----------|-------------|------------------|-------------------|
| MB-1 | morning-brief | Campaign daily performance (30d) | Structure, Efficiency |
| MB-2 | morning-brief | Budget pacing and impression share | Coverage |
| WD-2 | waste-detector | Quality score distribution | Quality |
| WD-5B | waste-detector | Shared negative list coverage | Hygiene |
| WD-6 | waste-detector | Ad group ad count | Quality, Hygiene |
| ACA-1 | ad-copy-analyzer | RSA performance and ad strength | Quality |
| ACA-2 | ad-copy-analyzer | Asset-level performance labels | Quality |
| MB-3 | morning-brief | Disapproved ads | Hygiene |
| WD-7 | waste-detector | Zero-impression enabled campaigns | Hygiene |

Run queries in parallel where possible. MB-1 and MB-2 cannot share a query due to impression share non-aggregability.

### Phase 2: Score each dimension

#### Dimension 1: Structure (20% weight)

Evaluate campaign organization and information architecture.

Inputs: MB-1 (campaign list), WD-6 (ad group ad count).

Scoring criteria:

| Factor | A (90-100) | B (80-89) | C (70-79) | D (60-69) | F (<60) |
|--------|-----------|-----------|-----------|-----------|---------|
| Ad groups per campaign | 3-20 avg | 2-3 or 21-30 | 1 or 31-50 | 51-100 | >100 or all =1 |
| Keywords per ad group | 5-20 avg | 3-4 or 21-30 | 1-2 or 31-50 | 51-100 | >100 |
| Naming conventions | Consistent pattern detected | Mostly consistent | Mixed patterns | Mostly inconsistent | No discernible pattern |
| Campaign type diversity | Appropriate mix for vertical | Reasonable mix | Slight imbalance | Major gaps | Single type only |

Naming convention check: analyze `campaign.name` and `ad_group.name` patterns for separators, hierarchy tokens (brand/non-brand, geo, match type), and consistency. Do not penalize if the account has <5 campaigns.

Compute `structure_score` as the average of factor scores (0-100 scale).

#### Dimension 2: Quality (25% weight)

Evaluate ad quality signals and landing page health.

Inputs: WD-2 (quality scores), ACA-1 (ad strength), ACA-2 (asset performance labels), WD-6 (ad count per ad group).

Scoring criteria:

| Factor | A (90-100) | B (80-89) | C (70-79) | D (60-69) | F (<60) |
|--------|-----------|-----------|-----------|-----------|---------|
| Quality score distribution | >70% QS 7+ | 50-70% QS 7+ | 30-50% QS 7+ | 10-30% QS 7+ | <10% QS 7+ |
| Ad strength distribution | >60% EXCELLENT/GOOD | 40-60% | 20-40% | 10-20% | <10% |
| Asset performance | >50% BEST/GOOD labels | 30-50% | 15-30% | 5-15% | <5% or all PENDING |
| RSA diversity | 3+ unique themes per ad group | 2-3 themes | 1-2 themes | Repetitive | Single message |
| Ads per ad group | 2-3 enabled RSAs | 1 or 4 | 0 RSAs (legacy only) | Mostly legacy | All legacy |

Quality score sub-components (creative_quality_score, post_click_quality_score, search_predicted_ctr) inform the narrative but do not create separate scoring factors.

Compute `quality_score` as the weighted average of factor scores.

#### Dimension 3: Efficiency (25% weight)

Evaluate spend efficiency against targets and waste signals.

Inputs: MB-1 (cost, conversions, CPA data), MB-2 (impression share), WD-2 (quality score with cost data).

Scoring criteria:

| Factor | A (90-100) | B (80-89) | C (70-79) | D (60-69) | F (<60) |
|--------|-----------|-----------|-----------|-----------|---------|
| CPA vs target | <90% of target | 90-100% | 100-120% | 120-150% | >150% |
| ROAS vs target | >110% of target | 100-110% | 80-100% | 60-80% | <60% |
| Waste ratio | <5% non-converting spend | 5-10% | 10-20% | 20-35% | >35% |
| IS utilization | >80% search IS | 60-80% | 40-60% | 20-40% | <20% |

If the profile has no CPA/ROAS targets, use industry benchmarks from the account's vertical (if known) or skip target-relative scoring and note the gap. The waste ratio uses non-converting keyword spend (from MB-1 daily data, filtered to zero-conversion keywords) as a percentage of total spend.

Compute `efficiency_score` as the weighted average of factor scores.

#### Dimension 4: Coverage (15% weight)

Evaluate market presence and opportunity capture.

Inputs: MB-2 (impression share fields).

Scoring criteria:

| Factor | A (90-100) | B (80-89) | C (70-79) | D (60-69) | F (<60) |
|--------|-----------|-----------|-----------|-----------|---------|
| Search impression share | >80% | 60-80% | 40-60% | 20-40% | <20% |
| Search rank lost IS | <5% | 5-15% | 15-30% | 30-50% | >50% |
| Search budget lost IS | <5% | 5-15% | 15-30% | 30-50% | >50% |
| Campaign type coverage | Search + PMax + Display | Search + one other | Search only | Single non-Search | None active |

Weight impression share metrics by campaign spend when computing the aggregate. A $10K/mo campaign losing 40% IS matters more than a $200/mo campaign losing 40% IS.

Compute `coverage_score` as the weighted average of factor scores.

#### Dimension 5: Hygiene (15% weight)

Evaluate operational cleanliness and maintenance state.

Inputs: WD-5B (shared negative lists), MB-3 (disapproved ads), WD-6 (ad count), WD-7 (zero-impression campaigns), MB-1 (stale campaign detection).

Scoring criteria:

| Factor | A (90-100) | B (80-89) | C (70-79) | D (60-69) | F (<60) |
|--------|-----------|-----------|-----------|-----------|---------|
| Negative keyword lists | Shared lists on all campaigns | Shared lists on >70% | Shared lists on 40-70% | Shared lists on <40% | No shared lists |
| Disapproved ads | 0 | 1-2 | 3-5 | 6-10 | >10 |
| Zero-impression entities | 0 enabled with 0 impr (7d) | 1-2 | 3-5 | 6-10 | >10 |
| Stale campaigns | All campaigns active in 7d | >90% active | 70-90% active | 50-70% active | <50% active |

A "stale campaign" is an enabled campaign with zero impressions in the last 7 days (from WD-7 data).

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
   - Quality factors: use QS-to-CPC pressure relationship (each QS point below 7 adds ~16% CPC premium; calculate monthly cost of QS-related CPC inflation from WD-2 spend data).
   - Coverage factors: `budget_lost_IS * current_spend * 0.5` = estimated lost conversion value.
   - Structure/Hygiene factors: flag as operational risk without direct dollar estimate unless specific waste is quantifiable.
3. Assign severity:
   - **HIGH** (>$500/mo estimated impact)
   - **MEDIUM** ($100-500/mo)
   - **LOW** ($25-100/mo)
   - **INFO** (<$25/mo)
4. Map to the Google Ads UI path for remediation.
5. Rank all priorities by estimated dollar impact descending. Cap at 5 priorities.

## Output format

```markdown
## Account Scorecard -- [Date]

### Account
- Google Ads: [Account Name] ([Customer ID])
- Campaigns: [N] active, [N] paused, [N] removed
- 30-day spend: $X,XXX | Conversions: X,XXX | CPA: $XX.XX

### Overall Grade: [A-F] ([score]/100)

| Dimension | Weight | Score | Grade | Key Factor |
|-----------|-------:|------:|:-----:|------------|
| Structure | 20% | XX | X | [lowest-scoring factor] |
| Quality | 25% | XX | X | [lowest-scoring factor] |
| Efficiency | 25% | XX | X | [lowest-scoring factor] |
| Coverage | 15% | XX | X | [lowest-scoring factor] |
| Hygiene | 15% | XX | X | [lowest-scoring factor] |

### Top Improvement Priorities

| # | Severity | Dimension | Issue | Est. Monthly Impact | Action |
|---|----------|-----------|-------|--------------------:|--------|
| 1 | HIGH | [dim] | [issue] | $X,XXX | [action] |
| 2 | MEDIUM | [dim] | [issue] | $XXX | [action] |
| 3 | ... | ... | ... | ... | ... |

### Detailed Findings

#### Structure ([Grade])
- [finding with context]
- **UI path:** Google Ads > [path to fix]

#### Quality ([Grade])
- [finding with context]
- **UI path:** Google Ads > [path to fix]

#### Efficiency ([Grade])
- [finding with context]
- **UI path:** Google Ads > [path to fix]

#### Coverage ([Grade])
- [finding with context]
- **UI path:** Google Ads > [path to fix]

#### Hygiene ([Grade])
- [finding with context]
- **UI path:** Google Ads > [path to fix]

### Quarterly Deep Audit
For a comprehensive 60-point audit covering bid strategies, audience layers,
conversion tracking, attribution, and more, consider running
[claude-ads](https://github.com/AgriciDaniel/claude-ads) as a companion tool.

### Notes
- Data freshness: [query timestamp caveats]
- Scoring assumptions: [any factors that could not be scored and why]
```

## Guardrails

- **Read-only**: This skill produces analysis and grades only. No account modifications are made. All recommended actions include Google Ads UI paths.
- **Missing data**: If a query returns zero rows for a dimension, assign the dimension score as "N/A" rather than penalizing. Note the gap in the output and explain which data is missing.
- **Small accounts**: For accounts with fewer than 3 campaigns or $500/mo total spend, note that the scorecard is less reliable due to small sample size. Skip factors that require statistical significance (e.g., naming convention patterns).
- **Target-relative scoring**: If the profile has no KPI targets, score Efficiency factors against same-vertical benchmarks if the vertical is known. If unknown, skip target-relative factors and note that setting targets via `platform-setup` would improve future scorecards.
- **Conversion lag**: Do not penalize Efficiency based on yesterday's conversion data alone. Use the full 30-day window from MB-1.
- **QS availability**: Quality score is only reported for keywords with sufficient impression volume. Do not penalize keywords with no QS data (they are simply excluded from the QS distribution).
- **Severity calibration**: Dollar impact estimates are approximations. Label all dollar figures as "estimated" in the output. Distinguish direct spend waste from modeled opportunity cost.
- **claude-ads reference**: Position claude-ads as a complementary quarterly tool, not a competitor. Never disparage external tools.

## Profile Maintenance

After completing analysis, if `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md` exists:
1. Update Watch List with any HIGH or MEDIUM severity findings that require follow-up.
2. Update Active Tests if user mentioned starting or completing a test during the session.
3. Append to Decision Log if the user acknowledges specific action items.
4. Update "Last updated" date.
Present proposed profile changes to the user before writing.

## References

- `references/gaql-queries.md` -- query IDs: MB-1, MB-2, MB-3, WD-2, WD-5B, WD-6, WD-7, ACA-1, ACA-2
