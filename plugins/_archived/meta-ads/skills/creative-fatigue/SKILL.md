---
name: creative-fatigue
description: >-
  This skill should be used when the user asks about "creative fatigue",
  "ad fatigue analysis", "which ads are dying", "creative lifecycle",
  "frequency decay", "ad replacement priorities", "creative health check",
  "how long will my ads last", "days remaining on creatives",
  "are my ads getting stale", "ad burnout", "frequency is too high",
  "declining CTR on my ads", "when do I need new creatives",
  or mentions creative decay, frequency-CTR correlation, ad lifecycle stages,
  creative replacement planning, or Meta ad fatigue detection.
allowed-tools: mcp__meta-ads__list_ads, mcp__meta-ads__get_insights, mcp__meta-ads__get_creative_performance, mcp__meta-ads__analyze_account_creatives, mcp__meta-ads__list_creatives
---

# Creative Fatigue Analysis

Classify every active ad into lifecycle stages (Testing / Rising / Peak / Fatiguing / Dead), estimate days remaining for fatiguing ads, and produce a prioritized replacement plan. This is the key differentiator skill for the meta-ads plugin.

## Account Context

Read `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md` at the start of every run.
If it exists:
- Use known account IDs.
- Apply KPI targets for CPA thresholds (Dead = CPA > 2x target).
- Use frequency cap from profile to calibrate fatigue bands.
- Note active creative tests — label them separately, do not flag test variants as fatiguing.
- Check watch list for creatives flagged in prior sessions.
If it doesn't exist, fall back to discovery and suggest running `platform-setup`.

## Lifecycle Stages

Defined in detail at `references/fatigue-model.md`. Summary:

| Stage | Criteria | Action |
|-------|----------|--------|
| **Testing** | <500 impressions OR <$25 spend | Wait — insufficient data |
| **Rising** | Frequency <2.0, CTR improving or stable, CPA at/below target | Scale — increase budget |
| **Peak** | Best 7d CTR in ad's history, frequency 1.5-2.5 | Maintain — don't touch |
| **Fatiguing** | Frequency >2.5, CTR declined >15% from peak 7d, CPM rising >10% | Plan replacement — 5-10 days remaining |
| **Dead** | Frequency >4.0 OR CTR declined >40% from peak OR CPA >2x target | Replace immediately |

## Days Remaining Formula

For ads in the Fatiguing stage:

```
daily_ctr_decay = (peak_7d_ctr - current_7d_ctr) / days_since_peak
dead_threshold_ctr = peak_7d_ctr * 0.60  (40% decline from peak = Dead)
days_to_dead = (current_7d_ctr - dead_threshold_ctr) / daily_ctr_decay
```

If `daily_ctr_decay <= 0` (CTR not declining), days_remaining = "Stable" (re-evaluate in 7 days).

See `references/fatigue-model.md` for the full formula and vertical-specific benchmarks.

## Frequency-CTR Decay Correlation

Analyze the relationship between frequency and CTR decline across the account:
- Plot (conceptually) frequency vs. CTR for each ad over its lifetime.
- Identify the account's typical "frequency ceiling" — the frequency at which CTR drops >20%.
- Compare against vertical benchmarks from `references/fatigue-model.md`.
- Flag if the account's decay rate is faster than vertical benchmarks (possible creative quality issue).

## CPM Inflation Signal

When CPM is rising alongside frequency, it is likely fatigue (Meta charges more to show stale ads). When CPM rises but frequency is stable, it is auction competition or seasonal demand. Distinguish and note in findings.

## Workflow

### Phase 1: Pull creative performance data

1. Use `mcp__meta-ads__list_ads` to get all active ads across all campaigns.
2. Use `mcp__meta-ads__get_creative_performance` for each ad — pull:
   - Impressions, frequency, CTR, CPA, CPM over multiple time windows (7d, 14d, 30d, lifetime).
   - Peak 7d CTR (best 7-day CTR in the ad's history).
   - Days since ad was created / first impression.
3. Use `mcp__meta-ads__get_insights` for time-series data to compute decay trends.
4. Use `mcp__meta-ads__analyze_account_creatives` for account-level creative health overview.

**Parallelization:** If the account has more than 5 active ad sets, consider spawning the `creative-analyst` subagent (see `agents/creative-analyst.md`) for parallel ad set analysis.

### Phase 2: Classify each ad

For each active ad, apply the lifecycle stage criteria:
1. Check Testing criteria first (low data = can't classify further).
2. For ads with sufficient data, compute:
   - Current 7d frequency.
   - Current 7d CTR vs. peak 7d CTR (% decline).
   - Current 7d CPM vs. 14d/30d CPM (% change).
   - Current CPA vs. target CPA.
3. Assign lifecycle stage.
4. For Fatiguing ads, compute days_remaining using the formula above.

### Phase 3: Build replacement plan

1. Sort Fatiguing ads by days_remaining ascending (most urgent first).
2. Sort Dead ads by 30d spend descending (biggest waste first).
3. For each Fatiguing/Dead ad, provide:
   - Dollar impact (excess CPA * conversions = wasted spend).
   - Which ad set it belongs to (Campaign > Ad Set context).
   - Replacement guidance: duplicate the best-performing ad in the same ad set, modify creative, publish.
   - Severity tag based on dollar impact.

## Output Format

```markdown
## Creative Lifecycle Report - [Date]

### Account: [Name] (act_XXXXXXXXX)

### Pipeline Summary
| Stage | Count | % of Active | Total Spend (30d) |
|-------|------:|------------:|------------------:|
| Testing | | | $ |
| Rising | | | $ |
| Peak | | | $ |
| Fatiguing | | | $ |
| Dead | | | $ |

### Pipeline Health
- **Healthy pipeline:** Testing + Rising > Fatiguing + Dead (new creatives entering faster than old ones dying).
- **Unhealthy pipeline:** Fatiguing + Dead > Testing + Rising (creative drought — need new ads urgently).
- **Current status:** [Healthy / Warning / Critical]

### Frequency-CTR Decay Analysis
| Metric | Account Avg | Vertical Benchmark | Assessment |
|--------|----------:|------------------:|:-----------|
| Frequency at Peak CTR | | | |
| Frequency at 50% CTR | | | |
| Typical Peak-to-Dead (days) | | | |

### Urgent: Fatiguing Ads (replace within estimated days)
| Ad | Campaign > Ad Set | Frequency | CTR Trend | Days Remaining | 30d Spend | Severity |
|---|---|---:|---|---:|---:|:---|

For each fatiguing ad:
- **Impact:** $X/mo wasted at current decay rate.
- **Replace by:** [estimated date]
- **How:** Meta Ads Manager > Campaign "[Name]" > Ad Set "[Name]" > Ads > Duplicate winning ad > modify creative > Publish

### Dead Ads (replace immediately)
| Ad | Campaign > Ad Set | Frequency | CTR vs Peak | 30d Spend | Action | Severity |
|---|---|---:|---|---:|---|:---|

For each dead ad:
- **Impact:** $X/mo wasted since entering Dead stage.
- **Fix:** Meta Ads Manager > Campaign "[Name]" > Ad Set "[Name]" > Ads > Toggle off dead ad. Duplicate and modify creative for replacement.

### Rising + Peak Ads (protect these)
| Ad | Campaign > Ad Set | Frequency | CTR | CPA | Status |
|---|---|---:|---:|---:|---|

### Testing Ads (awaiting data)
| Ad | Campaign > Ad Set | Impressions | Spend | Days Active |
|---|---|---:|---:|---:|

### Replacement Roadmap
| Priority | Ad to Replace | Replacement Action | Deadline | Est. Impact |
|:---------|---|---|---|---:|
| 1 | | Duplicate + new creative | | $ |
| 2 | | Duplicate + new creative | | $ |

**How to replace a Meta ad:**
Meta Ads Manager > Campaign "[Name]" > Ad Set "[Name]" > Ads > Duplicate winning ad > modify creative > Publish. Do NOT pause the old ad until the new one exits Learning phase.
```

## Guardrails

- **Read-only:** This skill produces analysis only. All replacement actions include UI paths.
- **Learning phase:** Do not classify ads in Learning phase. They may appear "Fatiguing" but are still optimizing.
- **Minimum data:** Require 500+ impressions and $25+ spend before lifecycle classification. Below that = Testing.
- **Creative tests:** Cross-reference with profile's Active Tests. Intentional test variants should be labeled as such, not flagged as Fatiguing/Dead.
- **Pause warning:** Always warn that pausing a Meta creative kills its learnings permanently. Recommend duplicating before pausing.
- **Seasonal context:** CTR can decline due to seasonal factors, not just fatigue. Note if analysis period includes known seasonal shifts (holidays, end-of-quarter, etc.).

## Profile Maintenance

After completing analysis, if `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md` exists:
1. Update Watch List with Fatiguing ads and their estimated replacement dates.
2. Note Dead ads that should have been replaced.
3. Update "Last updated" date.
Present proposed profile changes to the user before writing.

## References

- `references/fatigue-model.md` — Complete lifecycle criteria, days-remaining formula, vertical benchmarks
- `references/thresholds.md` — Fatigue detection thresholds
- `references/benchmarks.md` — 2026 Meta benchmarks (CTR, CPM, frequency by vertical)
- `references/ui-paths.md` — Meta Ads Manager UI paths for creative replacement
