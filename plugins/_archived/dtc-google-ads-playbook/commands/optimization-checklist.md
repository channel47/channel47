---
name: optimization-checklist
description: Generate a daily or weekly Google Ads optimization checklist tailored to the current account state, with specific action items and thresholds.
argument-hint: "[daily|weekly] [optional: campaign data or context]"
allowed-tools: ["Read", "Grep"]
---

# Optimization Checklist Command

Generate a structured optimization checklist based on the Daily Optimization skill, tailored to the user's account context.

## Process

1. **Determine checklist type.** Check if the user specified daily or weekly. Default to daily if not specified.

2. **Check for account context.** If the user provides campaign data, file paths, or describes their account, use that to customize the checklist. If no context, generate a generic playbook-aligned checklist.

3. **Generate the checklist.**

### For Daily Checklist:

```
## Daily Optimization Checklist — [Date]

### Morning Review (9-10 AM)
- [ ] Check overnight spend pacing — any campaigns exhaust budget before midnight?
- [ ] Review CPA for all active campaigns vs target (flag any >120% of target)
- [ ] Check for new policy disapprovals or status changes
- [ ] Review "limited by budget" campaigns — scale candidates
- [ ] Check "bidding strategy learning" campaigns — hold or nudge?

### Midday Adjustments (12-2 PM)
- [ ] Increase budget on campaigns with CPA <90% of target and "limited by budget"
- [ ] Decrease budget on campaigns with CPA >130% of target
- [ ] Adjust tCPA where needed ($3-$8 increments only):
  - Increase tCPA for campaigns "limited by bidding strategy" with good volume
  - Decrease tCPA for campaigns trending above target for 2+ days
- [ ] Review any campaigns with zero conversions today (with >$200 spend)

### Evening Review (6-8 PM)
- [ ] Final budget adjustments for overnight
- [ ] Flag campaigns ready for duplication (good CPA + hitting budget 3+ days)
- [ ] Note campaigns trending toward pause threshold (CPA >120% for 3+ days)
- [ ] Check Demand Gen campaigns — any with conversions? Adjust tCPA if needed

### Quick Reference Thresholds
| Metric | Green (Scale) | Yellow (Monitor) | Red (Act) |
|--------|--------------|-----------------|-----------|
| CPA vs Target | <90% | 90-120% | >120% |
| Daily Budget Used | >90% + good CPA | 50-90% | <50% with bad CPA |
| Conversions/Day | >5 | 1-5 | 0 for 2+ days |
| Days in Learning | <5 | 5-7 | >7 |
```

### For Weekly Checklist:

```
## Weekly Optimization Checklist — Week of [Date]

### Performance Review
- [ ] Pull 7-day campaign performance report
- [ ] Rank campaigns by CPA — identify top 5 and bottom 5
- [ ] Calculate account-level ROAS and CPA trend (improving or declining?)
- [ ] Compare this week vs last week: spend, CPA, conversion volume, ROAS

### Search Terms & Negative Keywords
- [ ] Review search terms report (filter: 10+ clicks, 0 conversions)
- [ ] Add new negative keywords for irrelevant or high-cost/no-conversion terms
- [ ] Check if any negative keywords are blocking good traffic (negative keyword report)
- [ ] Update shared negative keyword lists

### Campaign Structure
- [ ] Identify campaigns to duplicate (CPA <target, hitting budget, 7+ day trend)
- [ ] Identify campaigns to pause (CPA >130% target for 5+ days, no improvement)
- [ ] Review device performance — create phone-excl variants if desktop CPA is 20%+ better
- [ ] Check if any new audience segments should be tested

### Creative & Landing Pages
- [ ] Review asset group performance — pause underperforming asset groups
- [ ] Check landing page conversion rates by uid — any winners to scale?
- [ ] Review ad strength scores — improve any "Poor" or "Average" asset groups
- [ ] Check for policy disapprovals and submit appeals if needed

### Budget Reallocation
- [ ] Shift budget from bottom 20% campaigns to top 20%
- [ ] Ensure hero campaigns have sufficient budget headroom
- [ ] Review test campaign spend — capped at 5-10% of total?
- [ ] Set budget targets for next week based on this week's performance

### Demand Gen / YouTube
- [ ] Review Demand Gen CPA trend — is it improving week over week?
- [ ] Check video engagement metrics (view rate, watch time)
- [ ] Adjust Demand Gen tCPA if needed (slower, larger increments OK)
- [ ] Consider new video creative if CTR <0.3%

### Reporting Notes
- [ ] Document key changes made this week
- [ ] Note campaigns launched or paused
- [ ] Record tCPA and budget changes with rationale
- [ ] Flag items for next week's review
```

4. **Customize if context is available.** If the user provided campaign data or account context, replace generic items with specific campaign names and numbers. For example:
   - "Increase gpm-$149-women-4 budget from $8,888 to $12,888 (CPA $330 vs $350 target, limited by budget)"
   - "Consider pausing gpm-$149-feb-12-tab (CPA $506, 44% above $350 target, 5 days running)"

5. **Keep it actionable.** Every checklist item should have a clear done/not-done state. Include specific thresholds and campaign names wherever possible.
