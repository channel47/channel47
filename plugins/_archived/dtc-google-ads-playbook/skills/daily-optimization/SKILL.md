---
name: Daily Optimization
description: >
  This skill should be used when the user asks to "optimize Google Ads campaigns",
  "adjust budgets and bids", "manage tCPA targets", "review daily campaign performance",
  "create an optimization cadence", "decide when to pause or scale campaigns",
  "troubleshoot high CPA", "fix underperforming campaigns", or discusses daily/weekly
  Google Ads management routines. Also triggered by questions about bid strategy changes,
  budget reallocation, performance thresholds, or when to pause vs scale a campaign.
version: 1.0.0
---

# Daily Google Ads Optimization Playbook

A systematic approach to daily campaign management derived from accounts making 100+ budget/bid adjustments per day across $100K+/day in spend.

## Optimization Cadence

High-performing accounts require multiple daily touchpoints. Follow this cadence:

### Morning Review (9-10 AM)
1. Check overnight spend vs. budget pacing
2. Identify any campaigns that exhausted budget early (opportunity to increase)
3. Review CPA trends from previous 24 hours
4. Flag any campaigns with CPA > 120% of target
5. Check for policy disapprovals or status changes

### Midday Adjustment (12-2 PM)
1. Adjust budgets based on morning performance
2. Increase budgets on campaigns pacing under daily target with good CPA
3. Decrease budgets on campaigns overspending with high CPA
4. Make tCPA adjustments (small increments only)

### Evening Review (6-8 PM)
1. Final budget adjustments for overnight
2. Review day-over-day conversion trends
3. Identify campaigns ready for duplication
4. Plan next-day tests or launches

## tCPA Management Rules

Target CPA is the primary lever. Adjust with discipline:

**Adjustment increments:** Move tCPA in $3-$8 increments. Never make large jumps (>$20) unless resetting a campaign.

**When to INCREASE tCPA (+$3 to $8):**
- Campaign is limited by bidding strategy with good conversion volume
- CPA is already at or below target but volume is low
- Campaign has been in "learning" for 3+ days
- Goal is to increase delivery/volume

**When to DECREASE tCPA (-$3 to $8):**
- CPA trending 10%+ above target for 2+ consecutive days
- Campaign spending fast but conversion rate is declining
- Testing if the campaign can sustain volume at lower CPA

**tCPA anchor ranges by campaign maturity:**
| Stage | tCPA Range | Notes |
|-------|-----------|-------|
| New launch (day 1-7) | +15-25% above target | Give room to learn |
| Ramping (day 7-14) | +5-15% above target | Gradually tighten |
| Mature (day 14+) | At or -5% below target | Optimize for efficiency |
| Scaling | +5-10% above target | Trade efficiency for volume |

## Budget Management Rules

Budget changes should be frequent and data-driven:

**Daily budget adjustment framework:**
- Campaign CPA < 90% of target → Increase budget 20-50%
- Campaign CPA at 90-110% of target → Hold or increase 10-20%
- Campaign CPA at 110-130% of target → Hold and monitor
- Campaign CPA > 130% of target → Decrease budget 20-40%
- Campaign CPA > 150% of target for 3+ days → Pause and reassess

**Budget signals from Google Ads status:**
- "Limited by budget" + good CPA → Increase budget immediately
- "Limited by bidding strategy type" → Review tCPA, may need increase
- "Bidding strategy learning" → Wait 3-5 days before major changes
- "Bidding strategy constrained" → tCPA may be too aggressive

## Pause vs. Scale Decision Framework

Use this decision tree for any campaign:

```
Is CPA < 120% of target?
├── YES → Is volume > 5 conv/day?
│   ├── YES → SCALE: Increase budget + consider duplication
│   └── NO → GROW: Increase budget 20%, raise tCPA $5-$8
└── NO → Has CPA been high for 3+ days?
    ├── YES → Is there a clear cause (creative, landing page, competition)?
    │   ├── YES → FIX: Address root cause, hold budget
    │   └── NO → PAUSE: Stop campaign, reallocate budget to winners
    └── NO → WAIT: Monitor 2 more days, decrease tCPA $3-$5
```

## Key Performance Thresholds

Reference these benchmarks when evaluating campaigns:

| Metric | Good | Acceptable | Action Needed |
|--------|------|------------|---------------|
| CPA | < target | target to 1.2x | > 1.2x target |
| ROAS | > 0.95 | 0.80-0.95 | < 0.80 |
| Conv Rate | > 3% | 1.5-3% | < 1.5% |
| CTR (PMax) | > 2.5% | 1.5-2.5% | < 1.5% |
| CTR (DGen) | > 0.5% | 0.3-0.5% | < 0.3% |

## Demand Gen / YouTube Optimization

Demand Gen campaigns require a different approach:

- **Higher tCPA tolerance** — set tCPA 50-100% above PMax targets initially
- **Volume is king** — optimize for impressions and view rates first
- **Slower learning** — allow 7-14 days before major adjustments
- **Creative-dependent** — video creative quality matters more than bid management
- **Supplementary role** — do not expect Demand Gen to match PMax efficiency

## Common Optimization Mistakes to Avoid

1. **Making too-large tCPA jumps** — $3-$8 increments, not $20+
2. **Pausing too early** — give new campaigns 5-7 days minimum
3. **Ignoring device splits** — check if phone vs desktop CPA differs by 20%+
4. **Chasing daily fluctuations** — look at 3-day and 7-day trends
5. **Not duplicating winners** — scaling via duplication beats budget increases
6. **Neglecting negative keywords** — review search terms weekly

## Additional Resources

### Reference Files

For detailed optimization procedures, consult:
- **`references/budget-playbook.md`** — Complete budget management scenarios with worked examples
- **`references/troubleshooting-guide.md`** — Diagnosis and fix patterns for common performance issues
