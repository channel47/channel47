# Budget Management Playbook

## Daily Budget Adjustment Scenarios

### Scenario 1: Campaign Under Budget with Good CPA
**Situation:** Campaign spent 60% of daily budget, CPA is 15% below target.
**Action:** Increase budget by 30-50%. This campaign has room to scale.
**Example:** Budget $2,588 → $3,888. CPA target $350, actual $300.

### Scenario 2: Campaign Hitting Budget Limit with Good CPA
**Situation:** Campaign exhausts budget by 3 PM, CPA at target.
**Action:** Increase budget by 50-100%. Campaign is leaving conversions on the table.
**Example:** Budget $1,388 → $2,588. CPA target $350, actual $345.
**Signal:** Google Ads shows "Limited by budget" status.

### Scenario 3: Campaign Over-Spending with High CPA
**Situation:** Campaign on pace to overspend by 20%, CPA is 25% above target.
**Action:** Decrease budget by 20-30%. Also decrease tCPA by $5.
**Example:** Budget $3,388 → $2,588. tCPA $322 → $315.

### Scenario 4: New Campaign in Learning Phase
**Situation:** Campaign launched 3 days ago, showing "Bidding strategy learning."
**Action:** Hold. Do not adjust budget or tCPA for at least 5 days.
**Exception:** If CPA is 2x+ target after day 5, decrease tCPA by $5-$10.

### Scenario 5: Campaign with Zero Conversions After 3 Days
**Situation:** Campaign has spent $1,500 over 3 days with zero conversions.
**Action:** Check landing page, creative, and audience signal. If all look correct, decrease budget to minimum ($100/day) and monitor 2 more days. Pause if still zero conversions after day 5.

### Scenario 6: Campaign Achieving ROAS > 1.0
**Situation:** Campaign ROAS is 1.05+ consistently for 5+ days.
**Action:** This is a hero campaign. Scale aggressively: increase budget 50-100% AND create a duplicate campaign.
**Example:** Budget $8,888 → $15,888. Also create gpm-$149-women-5 as a duplicate.

## Budget Reallocation Framework

When total account budget is fixed, reallocate from losers to winners daily:

```
1. Rank all campaigns by CPA (lowest to highest)
2. Top 20% of campaigns → increase budget 20%
3. Middle 60% → hold budget
4. Bottom 20% → decrease budget 20%
5. Any campaign 50%+ above CPA target for 5+ days → pause and reallocate 100%
```

## Budget Scaling Milestones

| Daily Account Spend | # of Active Campaigns | Hero Campaigns | Test Budget |
|---------------------|----------------------|----------------|-------------|
| $1K-$5K/day | 3-5 | 1-2 | 20% of total |
| $5K-$20K/day | 8-15 | 3-5 | 15% of total |
| $20K-$50K/day | 15-25 | 5-8 | 10% of total |
| $50K-$100K/day | 20-35 | 8-12 | 10% of total |
| $100K+/day | 25-50+ | 10-15 | 5-10% of total |

## Non-Round Budget Convention

Use non-round numbers ending in `.88` for team-managed budgets:
- $288.88, $588.88, $888.88, $1,388.88, $2,588.88, $8,888.88, $68,888.88

This convention:
1. Makes team-managed campaigns instantly identifiable
2. Prevents confusion with Google's automated suggestions (which use round numbers)
3. Creates a visual audit trail in the change history
