---
name: waste-detector
description: >-
  This skill should be used when the user asks to "find Meta waste",
  "audit my Facebook account", "where am I wasting Meta budget",
  "Meta ads audit", "Facebook spend leaks", "Instagram waste",
  "social ads optimization", "Meta budget efficiency", "find wasted spend",
  "am I wasting money on Facebook", "where's my Meta budget going",
  "which ad sets are bleeding money", "find the waste on Meta",
  "Facebook ROAS check", "why is my Meta CPA so high",
  "what's eating my Facebook budget",
  or mentions Meta Ads waste analysis, Facebook budget efficiency,
  social ad spend optimization, or Meta spend leaks.
allowed-tools: mcp__meta-ads__get_ad_accounts, mcp__meta-ads__list_campaigns, mcp__meta-ads__list_ad_sets, mcp__meta-ads__list_ads, mcp__meta-ads__get_insights, mcp__meta-ads__get_campaign_performance, mcp__meta-ads__list_audiences, mcp__meta-ads__get_audience_insights, mcp__meta-ads__get_creative_performance
---

# Meta Ads Waste Detector

Scan Meta Ads accounts for 8 categories of spend leaks. Every finding is dollar-quantified, severity-tagged, and paired with a UI path and copy-paste action plan. Read-only — no mutations.

## Account Context

Read `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md` at the start of every run.
If it exists:
- Use known account IDs — skip `get_ad_accounts` discovery.
- Apply KPI targets as waste thresholds (e.g., flag CPA > target CPA, CPM > ceiling).
- Use frequency cap from profile to calibrate fatigue and frequency alerts.
- Note active creative/audience tests — exclude from waste flags if intentional.
- Check watch list for follow-up items from prior sessions.
If it doesn't exist, fall back to `mcp__meta-ads__get_ad_accounts` and suggest running `platform-setup`.

## Severity Tags

| Tag | Monthly Impact | Action |
|-----|---------------|--------|
| **HIGH** | >$500/mo | Act today |
| **MEDIUM** | $100-500/mo | Act this week |
| **LOW** | $25-100/mo | Add to optimization queue |
| **INFO** | <$25/mo | Note for context |

## 8 Meta Waste Types

### 1. Audience Overlap (Self-Competition)

**Signal:** Multiple ad sets targeting overlapping audiences, driving up CPM via self-competition in the same auction.

**Detection:**
- Use `mcp__meta-ads__list_ad_sets` to pull all active ad sets.
- Use `mcp__meta-ads__get_audience_insights` to check audience definitions.
- Compare targeting criteria across ad sets within the same campaign and across campaigns.
- Flag when two or more ad sets have >30% estimated overlap.
- Quantify: excess CPM cost from self-competition (overlapping spend * estimated CPM premium of 15-30%).

**Remediation (UI path):**
- Meta Ads Manager > Audiences > Audience Overlap tool (select 2+ audiences to compare).
- Consolidate overlapping ad sets or add exclusions.
- See `references/ui-paths.md` for step-by-step.

### 2. Creative Fatigue

**Signal:** Frequency > 3.0 with declining CTR — audience has seen the ad too many times.

**Detection:**
- Use `mcp__meta-ads__list_ads` to pull all active ads.
- Use `mcp__meta-ads__get_creative_performance` for ad-level frequency and CTR over 7d and 30d.
- Flag when: 7d frequency > 3.0 AND 7d CTR < 80% of 30d CTR (i.e., >20% decline).
- Quantify: wasted spend = (current CPA - target CPA) * conversions in period.

**Remediation (UI path):**
- Meta Ads Manager > Campaign > Ad Set > Ads > Duplicate winning ad > Modify creative > Publish.
- Pause the fatigued ad only after replacement is active and out of Learning.
- See `references/ui-paths.md` for step-by-step.

### 3. Placement Bleed

**Signal:** Audience Network or low-quality placements consuming disproportionate spend with poor CPA/ROAS.

**Detection:**
- Use `mcp__meta-ads__get_insights` with placement breakdown for each campaign.
- Flag when Audience Network spend > 10% of campaign spend AND Audience Network CPA > 2x campaign avg CPA.
- Also flag: Right Column, Instant Articles, or Messenger placements with >15% spend and below-average CPA.
- Quantify: excess spend on underperforming placements = placement spend * (1 - avg_campaign_CPA / placement_CPA).

**Remediation (UI path):**
- Meta Ads Manager > Campaign > Ad Set > Placements > Edit > Switch from Advantage+ to Manual Placements.
- Uncheck Audience Network, Right Column, or other underperformers.
- See `references/ui-paths.md` for step-by-step.

### 4. Non-Converting Ad Sets

**Signal:** Spend above CPA threshold with zero conversions.

**Detection:**
- Use `mcp__meta-ads__list_ad_sets` for all active ad sets.
- Use `mcp__meta-ads__get_insights` for 7d performance per ad set.
- Flag when: 7d spend > 2x target CPA AND 0 conversions.
- Also flag: 14d spend > 5x target CPA AND <2 conversions.
- Quantify: total wasted spend on non-converting ad sets.

**Remediation (UI path):**
- Meta Ads Manager > Campaign > Ad Set > Toggle off (pause).
- Before pausing: check if ad set is in Learning phase (may just need more time/budget).
- If CBO: let the algorithm reallocate. If ABO: pause and redirect budget manually.
- See `references/ui-paths.md` for step-by-step.

### 5. Learning Phase Churn

**Signal:** Ad sets repeatedly entering and exiting Learning phase due to frequent edits.

**Detection:**
- Use `mcp__meta-ads__list_ad_sets` to check delivery status history.
- Flag when an ad set shows "Learning Limited" or has been edited (budget, targeting, creative) more than 2x in the past 7 days.
- Quantify: spend during unstable learning periods at reduced efficiency (typically 20-30% above target CPA).

**Remediation (UI path):**
- Stop editing ad sets during Learning phase (first ~50 conversions).
- If budget must change, adjust by <20% at a time.
- Meta Ads Manager > Campaign > Ad Set > Edit > Review recent edit history.
- See `references/ui-paths.md` for step-by-step.

### 6. Broad Targeting Without Exclusions

**Signal:** Prospecting campaigns missing customer list exclusions — paying to reach existing customers.

**Detection:**
- Use `mcp__meta-ads__list_ad_sets` to check targeting.
- Use `mcp__meta-ads__list_audiences` to check custom audience usage.
- Flag when: prospecting/acquisition campaigns (non-retargeting) have no Custom Audience exclusions.
- Quantify: estimated overlap with customer base * CPA = wasted spend on existing customers.

**Remediation (UI path):**
- Meta Ads Manager > Campaign > Ad Set > Audience > Exclude > Custom Audiences > Select customer list.
- If no customer list exists: Audiences > Create Audience > Custom Audience > Customer List > Upload.
- See `references/ui-paths.md` for step-by-step.

### 7. Frequency Cap Violations

**Signal:** Reach/awareness campaigns without frequency caps, resulting in excessive impressions per person.

**Detection:**
- Use `mcp__meta-ads__list_campaigns` to find Reach/Brand Awareness objective campaigns.
- Use `mcp__meta-ads__list_ad_sets` to check frequency cap settings.
- Flag when: Reach or Brand Awareness campaign has no frequency cap AND average frequency > 2.0 in 7d.
- Quantify: excess impressions beyond 2.0 frequency * CPM / 1000 = wasted spend.

**Remediation (UI path):**
- Meta Ads Manager > Campaign > Ad Set > Optimization & Delivery > Frequency Cap.
- Recommended: 1 impression per 7 days for Reach campaigns, 2 per 7 days for Awareness.
- See `references/ui-paths.md` for step-by-step.

### 8. Stale Lookalike Seeds

**Signal:** Lookalike audiences based on source audiences older than 90 days or with small seed sizes.

**Detection:**
- Use `mcp__meta-ads__list_audiences` to pull all lookalike audiences.
- Use `mcp__meta-ads__get_audience_insights` to check source audience details.
- Flag when: lookalike source audience was last updated >90 days ago.
- Also flag: source audience size <1,000 (poor signal quality).
- Quantify: spend on stale-seeded lookalikes * estimated CPA premium (10-25% above fresh lookalikes).

**Remediation (UI path):**
- Audiences > Custom Audiences > Select source audience > Update Source.
- Or: Create new Custom Audience with fresh data > Create new Lookalike from it.
- Update ad sets to use refreshed lookalike.
- See `references/ui-paths.md` for step-by-step.

## Workflow

### Phase 1: Run waste queries

For each of the 8 waste types, execute the detection queries described above:
1. Pull campaign, ad set, ad, audience, and insight data.
2. Apply detection criteria per waste type.
3. Record all findings with raw data.

Use `references/waste-queries.md` for detailed query templates.

### Phase 2: Quantify impact

For each finding:
1. Calculate dollar impact (monthly projection).
2. Assign severity tag (HIGH/MEDIUM/LOW/INFO).
3. Rank all findings across waste types by dollar impact, descending.

### Phase 3: Build remediation package

For each finding:
1. Write a plain-English description of the issue.
2. Include a dollar table showing current vs. target metrics.
3. Provide the exact Meta Ads Manager UI path to fix it.
4. Include a copy-paste artifact where applicable (e.g., exclusion audience name, frequency cap value).

## Output Format

```markdown
## Waste Report - [Date]

### Account: [Name] (act_XXXXXXXXX)

### Summary
| Waste Type | Findings | Est. Monthly Waste | Top Severity |
|-----------|--------:|-------------------:|:-------------|
| Audience Overlap | | | |
| Creative Fatigue | | | |
| Placement Bleed | | | |
| Non-Converting Ad Sets | | | |
| Learning Phase Churn | | | |
| Broad Without Exclusions | | | |
| Frequency Cap Violations | | | |
| Stale Lookalike Seeds | | | |
| **Total** | | **$X,XXX** | |

### HIGH Severity Findings
> Act today. Each finding >$500/mo estimated waste.

**[#] [Waste Type]: [Specific finding]** — HIGH
| Metric | Current | Target | Gap |
|--------|--------:|-------:|----:|
| | | | |
- **Impact:** $X,XXX/mo estimated waste
- **Evidence:** [specific data points]
- **Fix:** Meta Ads Manager > [exact UI path]
- **Copy-paste:** `[artifact]`

### MEDIUM Severity Findings
> Act this week. $100-500/mo each.

### LOW Severity Findings
> Optimization queue. $25-100/mo each.

### INFO
> Context items. <$25/mo each.

### Action Plan (Priority Order)
| # | Action | Waste Type | Impact | Effort | UI Path |
|---|--------|-----------|-------:|--------|---------|
| 1 | | | | | |
```

## Guardrails

- **Read-only:** This skill produces analysis and action plans only. No mutations. All fixes include UI paths for the user to execute manually.
- **Creative pause warning:** Pausing a Meta creative kills its learnings permanently (unlike pausing a keyword). Always note this tradeoff.
- **Learning phase:** Do NOT flag ad sets in Learning phase as waste. They need time to optimize.
- **Active tests:** Cross-reference with profile's Active Tests section. Intentional tests should not be flagged as waste.
- **Minimum data:** Require at least 7 days of data and $50 spend before flagging an ad set as waste.

## Profile Maintenance

After completing analysis, if `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md` exists:
1. Update Watch List with any new waste findings flagged in this run.
2. Append to Decision Log if user indicates they will act on findings.
3. Update "Last updated" date.
Present proposed profile changes to the user before writing.

## References

- `references/waste-queries.md` — Query templates per waste category
- `references/thresholds.md` — Detection thresholds
- `references/benchmarks.md` — 2026 Meta benchmarks
- `references/ui-paths.md` — Meta Ads Manager UI paths for every remediation action
