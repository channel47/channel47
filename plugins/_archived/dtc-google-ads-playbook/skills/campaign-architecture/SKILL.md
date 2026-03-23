---
name: Campaign Architecture
description: >
  This skill should be used when the user asks to "plan a Google Ads campaign structure",
  "set up Performance Max campaigns", "create a PMax account architecture", "segment audiences
  in Google Ads", "structure a DTC Google Ads account", "plan campaign naming conventions",
  "design device segmentation strategy", "scale campaigns with duplication", or discusses
  building a new Google Ads account from scratch for a DTC brand. Also triggered by questions
  about campaign types, audience splits, budget allocation across campaigns, or Performance Max
  vs Demand Gen strategy.
version: 1.0.0
---

# DTC Google Ads Campaign Architecture

A proven framework for structuring high-performance Google Ads accounts for DTC brands, derived from accounts spending $100K-$200K+/day profitably.

## Core Philosophy

Build a PMax-first account with aggressive audience segmentation, systematic naming conventions, and device-level isolation. Treat each campaign as an independent test cell with its own audience, offer, landing page, and budget — then scale winners through duplication.

## Campaign Type Mix

Allocate spend across campaign types using this ratio as a starting point:

| Campaign Type | % of Budget | Role |
|---------------|-------------|------|
| Performance Max | 85-95% | Primary acquisition engine |
| Demand Gen (YouTube) | 5-10% | Supplementary awareness + retargeting |
| Search | 0-5% | Brand defense only (optional) |

Performance Max handles the heavy lifting. Demand Gen extends reach via YouTube at low CPMs. Search is only for brand terms if needed.

## Audience Segmentation Framework

Segment campaigns by audience persona. Each segment gets its own campaign(s) with tailored creative, landing pages, and offers.

**Primary segments to test for any DTC brand:**
- **Women** — largest addressable market for most health/wellness/beauty DTC
- **Seniors (55+)** — high intent, high AOV, responsive to urgency
- **Moms** — responsive to "reset" and transformation messaging
- **Men** — often lower volume but can be efficient
- **Geographic** — state-level campaigns for localized offers or compliance

**Naming convention pattern:**
```
{platform}-{price/offer}-{audience}-{sequence}-{modifier}
```

**Examples:**
```
gpm-$149-women-4           → PMax, $149 offer, women audience, 4th iteration
gpm-$149-senior-1-phone-excl → PMax, $149, seniors, 1st, phone traffic excluded
gpm-$149-feb-13            → PMax, $149, February launch, 13th iteration
directmeds-seniors-3       → PMax, DirectMeds brand, seniors, 3rd iteration
gdg-youtube-seniors-8      → Demand Gen, YouTube, seniors, 8th iteration
```

Encode the offer price, audience, launch date/event, iteration number, and any device modifiers directly in the campaign name. This makes performance analysis instant at a glance.

## Device Segmentation Strategy

Device performance varies dramatically. Isolate devices at the campaign level:

**Three campaign tiers by device:**
1. **All-device campaigns** — default starting point, let PMax optimize
2. **Phone-exclusion campaigns (`-phone-excl`)** — exclude mobile phones to isolate desktop + tablet traffic, which often converts at lower CPA
3. **Tablet-only campaigns (`-tab` or `-tablet`)** — isolate tablet traffic for specific testing

**Typical device performance benchmarks:**
- Mobile: ~83% of spend, highest volume, slightly higher CPA
- Desktop: ~15% of spend, lowest CPA, highest CVR
- Tablet: ~2% of spend, variable performance
- TV screens: negligible spend, no conversions

Create phone-exclusion variants of top-performing campaigns to capture desktop traffic at lower CPAs.

## Campaign Duplication & Scaling

Scale winners through duplication, not just budget increases. The framework:

1. **Identify winners** — campaigns with CPA within 10% of target and stable for 7+ days
2. **Duplicate with variation** — create a new campaign with the same audience but a different:
   - Landing page variant (different `uid` parameter)
   - Slightly adjusted tCPA ($5-$15 higher or lower)
   - Modified budget (start at 30-50% of original)
   - Different creative rotation
3. **Iterate naming** — increment the sequence number (women-2 → women-3 → women-4)
4. **Run in parallel** — let both original and duplicate compete

**Scaling signals (when to duplicate):**
- Campaign hitting daily budget consistently
- CPA stable at or below target for 5+ days
- Conversion volume > 5/day
- "Limited by budget" status in Google Ads

**Pause signals:**
- CPA > 120% of target for 5+ consecutive days
- ROAS < 0.70 with no improvement trend
- Zero conversions in 3+ days with meaningful spend

## Budget Allocation Framework

Distribute budget based on proven performance tiers:

| Tier | Budget Share | Criteria |
|------|-------------|----------|
| Hero campaigns (top 3-5) | 60-70% | CPA < target, ROAS > 0.90 |
| Growth campaigns (5-10) | 20-30% | CPA within 10% of target |
| Test campaigns (5-15) | 5-10% | New launches, audience tests |

Use non-round budget numbers (e.g., $8,888.88 instead of $9,000) as a convention to quickly identify campaigns managed by the team vs. auto-suggestions.

## Additional Resources

### Reference Files

For detailed implementation guides, consult:
- **`references/segmentation-deep-dive.md`** — Complete audience segmentation patterns with examples for 10+ DTC verticals
- **`references/naming-convention-guide.md`** — Full naming convention system with parser logic and examples
