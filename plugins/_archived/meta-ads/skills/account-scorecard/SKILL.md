---
name: account-scorecard
description: >-
  This skill should be used when the user asks for an "account scorecard",
  "account health score", "Meta account grade", "Facebook ads grade",
  "how healthy is my account", "account audit score", "rate my Meta account",
  "account assessment", "quarterly review", "grade my Meta account",
  "monthly checkup", "how good is my Meta account",
  or mentions account scoring, health dimensions, account grading,
  optimization readiness, or performance grading for Meta Ads.
allowed-tools: mcp__meta-ads__list_campaigns, mcp__meta-ads__list_ad_sets, mcp__meta-ads__list_ads, mcp__meta-ads__get_insights, mcp__meta-ads__verify_account_setup, mcp__meta-ads__check_campaign_readiness, mcp__meta-ads__get_quick_fixes
---

# Account Scorecard

Score a Meta Ads account across 5 dimensions with weighted grades, specific findings, and an improvement roadmap. Designed for monthly or quarterly reviews. For deeper, check-by-check audits, reference claude-ads (46 Meta-specific checks).

## Account Context

Read `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md` at the start of every run.
If it exists:
- Use known account IDs.
- Apply KPI targets for Efficiency scoring.
- Check watch list for recurring issues.
- Reference prior scorecard results if mentioned in Decision Log.
If it doesn't exist, fall back to discovery and suggest running `platform-setup`.

## Scoring Dimensions

| Dimension | Weight | What It Measures |
|-----------|-------:|------------------|
| Structure | 15% | Campaign organization, naming conventions, objective alignment |
| Creative Health | 30% | Lifecycle mix, format diversity, fatigue levels, refresh rate |
| Audience Quality | 25% | Targeting strategy, overlap, exclusions, seed freshness |
| Efficiency | 20% | CPA vs target, ROAS vs target, waste ratio, budget pacing |
| Tracking | 10% | Pixel health, CAPI coverage, attribution setup, conversion events |

## Grading Scale

| Grade | Score Range | Meaning |
|:------|:-----------|:--------|
| A | 90-100 | Excellent — maintain current practices |
| B | 75-89 | Good — minor optimizations available |
| C | 60-74 | Fair — significant improvement opportunities |
| D | 40-59 | Poor — structural issues limiting performance |
| F | 0-39 | Critical — fundamental setup problems |

## Dimension Details

### 1. Structure (15%)

**Checks:**
- Campaign count and organization (campaigns grouped by objective?).
- Naming convention consistency (do campaign/ad set/ad names follow a pattern?).
- Objective alignment (is each campaign using the right optimization objective?).
- Campaign Budget Optimization (CBO) vs Ad Set Budget usage and appropriateness.
- Number of ad sets per campaign (too few = undertesting, too many = fragmentation).

**Tools:** `mcp__meta-ads__list_campaigns`, `mcp__meta-ads__list_ad_sets`, `mcp__meta-ads__check_campaign_readiness`

**Scoring:**
- 90-100: Consistent naming, 3-5 ad sets/campaign, correct objectives, CBO where appropriate.
- 75-89: Minor naming inconsistencies, mostly correct structure.
- 60-74: Some campaigns with wrong objectives, inconsistent organization.
- 40-59: Many structural issues, fragmented ad sets, misaligned objectives.
- 0-39: No naming convention, single ad set campaigns, mismatched objectives.

### 2. Creative Health (30%)

**Checks:**
- Lifecycle stage distribution (from creative-fatigue analysis: Testing/Rising/Peak/Fatiguing/Dead ratio).
- Format diversity (image, video, carousel — are multiple formats tested?).
- Average ad frequency across account.
- Creative refresh rate (how often are new ads introduced?).
- Ads per ad set (minimum 3-5 recommended for algorithmic optimization).

**Tools:** `mcp__meta-ads__list_ads`, `mcp__meta-ads__get_insights`

**Scoring:**
- 90-100: Healthy pipeline (Testing+Rising > Fatiguing+Dead), 3+ formats, frequency <2.5, regular refresh.
- 75-89: Mostly healthy, 2+ formats, some fatiguing ads being managed.
- 60-74: Fatiguing ads > Rising ads, limited formats, frequency approaching 3.0.
- 40-59: Many dead/fatiguing ads, single format, frequency >3.0, no refresh cadence.
- 0-39: All ads fatigued/dead, no new creative pipeline.

### 3. Audience Quality (25%)

**Checks:**
- Audience overlap between ad sets (self-competition).
- Customer list exclusions on prospecting campaigns.
- Lookalike audience seed freshness (<90 days = good).
- Lookalike audience size (1-3% = good, >5% = too broad).
- Retargeting window strategy (layered windows vs. single bucket).
- Audience size vs. budget (too much budget for small audiences = frequency issues).

**Tools:** `mcp__meta-ads__list_ad_sets`, `mcp__meta-ads__get_insights`

**Scoring:**
- 90-100: No significant overlap, fresh seeds, proper exclusions, layered retargeting.
- 75-89: Minor overlap, most exclusions in place, seeds <90 days old.
- 60-74: Some overlap, missing exclusions on 1-2 campaigns, seeds aging.
- 40-59: Significant overlap, no customer exclusions, stale seeds.
- 0-39: Severe self-competition, no exclusion strategy, no custom audiences.

### 4. Efficiency (20%)

**Checks:**
- CPA vs. profile target (account-wide and by campaign).
- ROAS vs. profile target (if applicable).
- Waste ratio (wasted spend from waste-detector findings / total spend).
- Budget pacing accuracy (within 10% of target = good).
- Cost trend direction (improving, stable, or deteriorating over 30d).

**Tools:** `mcp__meta-ads__get_insights`, `mcp__meta-ads__get_quick_fixes`

**Scoring:**
- 90-100: CPA < target, ROAS > target, <5% waste ratio, good pacing.
- 75-89: CPA within 10% of target, <10% waste ratio.
- 60-74: CPA 10-25% above target, 10-20% waste ratio.
- 40-59: CPA 25-50% above target, >20% waste ratio.
- 0-39: CPA >2x target, massive waste, severe pacing issues.

### 5. Tracking (10%)

**Checks:**
- Pixel installed and firing correctly.
- Conversions API (CAPI) configured (critical post-iOS 14.5).
- Correct conversion events configured per campaign objective.
- Attribution window settings (7-day click / 1-day view = Meta best practice).
- Domain verification status.

**Tools:** `mcp__meta-ads__verify_account_setup`

**Scoring:**
- 90-100: Pixel + CAPI both active, correct events, proper attribution, domain verified.
- 75-89: Pixel active, CAPI configured but coverage gaps, mostly correct events.
- 60-74: Pixel active, no CAPI, some event mismatches.
- 40-59: Pixel active but misconfigured, no CAPI, wrong events on some campaigns.
- 0-39: No pixel or CAPI, missing conversion events, unverified domain.

## Workflow

### Phase 1: Collect data

For each dimension, execute the relevant tool calls to gather data:
1. **Structure:** List all campaigns and ad sets, check readiness.
2. **Creative Health:** List all ads, pull frequency and performance data.
3. **Audience Quality:** List ad sets with targeting details, check audiences.
4. **Efficiency:** Pull account-level and campaign-level insights for 30d.
5. **Tracking:** Verify account setup.

### Phase 2: Score each dimension

Apply scoring criteria to compute a 0-100 score per dimension.
For each dimension, list specific findings that contributed to the score (both positive and negative).

### Phase 3: Compute weighted total

```
total_score = (structure * 0.15) + (creative * 0.30) + (audience * 0.25) + (efficiency * 0.20) + (tracking * 0.10)
```

### Phase 4: Build improvement roadmap

For each dimension scoring below 75:
1. Identify the highest-impact improvement.
2. Dollar-quantify the opportunity where possible.
3. Provide UI path and specific action.
4. Assign severity tag (HIGH/MEDIUM/LOW).

## Output Format

```markdown
## Account Scorecard - [Date]

### Account: [Name] (act_XXXXXXXXX)

### Overall Grade: [A-F] ([score]/100)

| Dimension | Weight | Score | Grade | Key Finding |
|-----------|-------:|------:|:------|:------------|
| Structure | 15% | /100 | | |
| Creative Health | 30% | /100 | | |
| Audience Quality | 25% | /100 | | |
| Efficiency | 20% | /100 | | |
| Tracking | 10% | /100 | | |
| **Weighted Total** | **100%** | **/100** | **[Grade]** | |

### Dimension Details

#### Structure ([score]/100) — [Grade]
**Positives:**
- [specific positive finding]

**Issues:**
- [specific issue + dollar impact if quantifiable]

#### Creative Health ([score]/100) — [Grade]
...

#### Audience Quality ([score]/100) — [Grade]
...

#### Efficiency ([score]/100) — [Grade]
...

#### Tracking ([score]/100) — [Grade]
...

### Improvement Roadmap
| Priority | Dimension | Action | Impact | Severity | UI Path |
|:---------|-----------|--------|-------:|:---------|---------|
| 1 | | | $/mo | HIGH | |
| 2 | | | $/mo | MEDIUM | |
| 3 | | | $/mo | MEDIUM | |

### Companion Audit
For a deeper, check-by-check audit (46 Meta-specific checks), consider running
[claude-ads](https://github.com/AgriciDaniel/claude-ads) as a quarterly complement to this scorecard.

### Next Steps
- Run `/creative-fatigue` for detailed creative lifecycle analysis.
- Run `/waste-detector` for spend leak identification.
- Run `/audience-analyzer` for audience strategy review.
- Re-run this scorecard in 30 days to track improvement.
```

## Guardrails

- **Read-only:** This skill produces analysis and scores only. Improvement actions include UI paths.
- **Score calibration:** Scores are directional, not absolute. The same account may score differently on different days due to data recency. Note the analysis date prominently.
- **Subjectivity in Structure:** Naming conventions and organization are somewhat subjective. Focus on consistency and alignment with objectives rather than prescribing a specific naming format.
- **claude-ads companion:** Reference claude-ads for quarterly deep audits but do NOT position it as a replacement for this scorecard. This scorecard is for monthly/weekly tracking; claude-ads is for comprehensive quarterly reviews.

## Profile Maintenance

After completing analysis, if `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md` exists:
1. Record scorecard results in Decision Log (date, overall grade, dimension scores).
2. Add improvement roadmap items to Watch List.
3. Update "Last updated" date.
Present proposed profile changes to the user before writing.

## References

- `references/thresholds.md` — Scoring thresholds
- `references/benchmarks.md` — 2026 Meta benchmarks
- `references/ui-paths.md` — Meta Ads Manager UI paths for improvement actions
