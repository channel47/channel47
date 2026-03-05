---
name: audience-analyzer
description: >-
  This skill should be used when the user asks to "analyze my audiences",
  "audience performance review", "which audiences are working", "audience
  overlap check", "audience saturation", "lookalike performance", "targeting
  analysis", "audience health", "audience refresh", "audience efficiency",
  "are my audiences exhausted", "which targeting is best",
  "should I refresh my lookalikes",
  or mentions audience performance, targeting effectiveness, audience
  exhaustion, overlap detection, or audience strategy review for Meta Ads.
allowed-tools: mcp__meta-ads__list_audiences, mcp__meta-ads__get_audience_insights, mcp__meta-ads__estimate_audience_size, mcp__meta-ads__list_ad_sets, mcp__meta-ads__get_insights
---

# Audience Analyzer

Analyze audience performance by type, detect saturation, surface overlap signals, rank by efficiency, and provide refresh recommendations. Replaces the skeleton `audience-builder` with a read-only, analysis-first approach.

## Account Context

Read `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md` at the start of every run.
If it exists:
- Use known account IDs.
- Apply KPI targets for efficiency ranking (CPA/ROAS targets).
- Reference audience notes from Preferences section.
- Note active audience tests.
- Check watch list for audience-related items from prior sessions.
If it doesn't exist, fall back to discovery and suggest running `platform-setup`.

## Audience Types Analyzed

| Type | Source | Key Metrics |
|------|--------|-------------|
| Custom Audience — Customer List | CRM upload | Match rate, freshness, CPA |
| Custom Audience — Website | Pixel/CAPI events | Size, CPA, saturation signals |
| Custom Audience — Engagement | On-platform actions | Size, CPA, frequency |
| Lookalike (1-3%) | Seeded from custom audience | Seed quality, CPA, ROAS |
| Lookalike (3-10%) | Seeded from custom audience | CPA vs narrower lookalikes |
| Interest/Behavior | Meta targeting categories | CPA, CPM, frequency |
| Broad (Advantage+) | Algorithmic | CPA, audience quality signals |

## Saturation Signals

An audience is approaching saturation when:
- **Frequency rising:** 7d frequency > 2.5 AND increasing week-over-week.
- **CPM rising without auction changes:** CPM up >15% while audience size stable.
- **CTR declining:** 7d CTR < 80% of 30d average.
- **Diminishing returns:** CPA rising while spend is flat or declining.
- **Audience size shrinking:** Custom audience size declining (members leaving, exclusions growing).

## Workflow

### Phase 1: Pull audience data

1. Use `mcp__meta-ads__list_audiences` to get all audiences (custom, lookalike, saved).
2. Use `mcp__meta-ads__get_audience_insights` for audience details — size, source, creation date, last updated.
3. Use `mcp__meta-ads__estimate_audience_size` for current reach estimates.
4. Use `mcp__meta-ads__list_ad_sets` to map audiences to active ad sets.
5. Use `mcp__meta-ads__get_insights` for performance metrics per ad set (proxy for audience performance).

### Phase 2: Performance analysis

For each audience (via its ad set proxy):
1. Pull 7d, 14d, and 30d performance: spend, impressions, frequency, CTR, CPA, ROAS, CPM.
2. Compute efficiency score: `efficiency = target_CPA / actual_CPA` (>1.0 = beating target).
3. Compute saturation score based on signals above.
4. Compute freshness score for custom/lookalike audiences: days since last update.

### Phase 3: Overlap detection

- Compare targeting criteria across all active ad sets.
- Flag when ad sets in different campaigns target the same or highly similar audiences.
- Flag when lookalike audiences overlap (e.g., 1% and 3% lookalikes from same seed without exclusions).
- Estimate overlap cost: overlapping spend * estimated CPM premium (15-30%).

### Phase 4: Build recommendations

For each audience with issues:
1. **Saturated audiences:** Recommend expansion (broader lookalike, new interest stacks) or rest (pause for 2-4 weeks).
2. **Stale custom audiences:** Recommend refresh with current data.
3. **Overlapping audiences:** Recommend consolidation or mutual exclusions.
4. **High-performing audiences:** Recommend scaling (increase budget, test new creative within).
5. **Missing audiences:** Identify audience types not being used (e.g., no retargeting layers, no customer exclusions).

## Output Format

```markdown
## Audience Analysis - [Date]

### Account: [Name] (act_XXXXXXXXX)

### Audience Performance Summary
| Audience | Type | Size | Ad Sets | 30d Spend | CPA | ROAS | Frequency | Efficiency | Status |
|----------|------|-----:|--------:|----------:|----:|-----:|----------:|-----------:|:-------|
| | | | | $ | $ | | | | |

*Efficiency = target CPA / actual CPA. >1.0 = beating target. <1.0 = above target.*

### Efficiency Ranking
| Rank | Audience | Type | CPA | vs Target | 30d Spend | Recommendation |
|:-----|----------|------|----:|----------:|----------:|:---------------|
| 1 | | | $ | % below | $ | Scale |
| 2 | | | $ | % below | $ | Maintain |
| ... | | | $ | % above | $ | Investigate |

### Saturation Alerts
| Audience | Signal | Severity | 7d Trend | Recommendation |
|----------|--------|:---------|:---------|:---------------|
| | Frequency > 2.5, rising | HIGH | | Expand or rest |
| | CPM rising + CTR declining | MEDIUM | | Refresh creative or expand |

For each saturated audience:
- **Impact:** $X/mo excess cost at current saturation level.
- **Fix:** [specific action with UI path]

### Overlap Signals
| Audience A | Audience B | Estimated Overlap | CPM Impact | Fix |
|-----------|-----------|:-----------------:|----------:|:----|
| | | ~X% | $X/mo | Add mutual exclusion |

For each overlap:
- **Fix:** Meta Ads Manager > Audiences > [Audience] > Create Exclusion
- Or: Meta Ads Manager > Campaign > Ad Set > Audience > Exclude > Custom Audiences

### Audience Freshness
| Audience | Type | Created | Last Updated | Days Stale | Action |
|----------|------|---------|-------------|----------:|:-------|
| | Lookalike | | | | Refresh seed |
| | Customer List | | | | Re-upload |

### Missing Audience Types
| Gap | Why It Matters | Action | Priority |
|-----|---------------|:-------|:---------|
| No customer list exclusion | Paying to reach existing customers | Upload CRM list | HIGH |
| No website retargeting | Missing warmest audience | Create pixel audience | HIGH |
| No video viewer retargeting | Wasting engagement signals | Create engagement audience | MEDIUM |
| Single retargeting window | No funnel differentiation | Layer 7d / 14d / 30d windows | MEDIUM |

### Audience Refresh Recommendations
| Audience | Current State | Action | UI Path | Priority |
|----------|:-------------|:-------|:--------|:---------|
| | Stale seed (>90d) | Refresh with current data | Meta Ads Manager > Audiences > [Audience] > Edit | HIGH |
| | Saturated | Expand to 3% lookalike | Meta Ads Manager > Audiences > Create > Lookalike | MEDIUM |
| | Small size | Combine sources | Meta Ads Manager > Audiences > [Audience] > Edit Source | LOW |
```

## Guardrails

- **Read-only:** This skill produces analysis only. All audience actions include UI paths.
- **Audience overlap tool:** Meta's built-in Audience Overlap tool is the source of truth for overlap analysis. This skill estimates overlap from targeting criteria, which is directional but not exact. Recommend the user verify with Meta's tool.
- **iOS ATT impact:** Custom audience match rates have declined post-iOS 14.5. Note this when evaluating audience sizes and performance.
- **Lookalike quality:** Lookalike quality degrades above 3% — flag if wider lookalikes are in use without performance justification.
- **Consent/compliance:** Customer list uploads require consent. Remind user to verify compliance before recommending uploads.
- **Minimum data:** Require 7+ days of data per audience before drawing conclusions.

## Profile Maintenance

After completing analysis, if `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md` exists:
1. Update Watch List with saturated or stale audiences.
2. Note overlap findings for follow-up.
3. If user commits to audience refreshes, add to Active Tests.
4. Update "Last updated" date.
Present proposed profile changes to the user before writing.

## References

- `references/thresholds.md` — Saturation and freshness thresholds
- `references/benchmarks.md` — 2026 Meta audience benchmarks
- `references/ui-paths.md` — Meta Ads Manager UI paths for audience management
