---
title: Performance Max Diagnostic
description: Deep-dive analysis of your PMax campaigns. Uncover asset performance issues, audience signal gaps, and budget allocation problems that the Google Ads UI hides.
version: "1.0.0"
category: google-ads
tags:
  - performance max
  - pmax
  - asset groups
  - audience signals
  - diagnostics
tier: premium
price: 29
featured: true
publishedAt: 2025-01-04
---

## The PMax Black Box Problem

Performance Max campaigns are notoriously opaque. Google shows you aggregated metrics, but hides the details that actually matter:

- Which asset combinations are driving results?
- Are your audience signals being used or ignored?
- Where is your budget actually being spent (Search vs. Display vs. YouTube)?
- Which products in your feed are underperforming?

This skill cracks open the black box.

## What You Get

### Asset Performance Analysis

The skill evaluates every asset in your asset groups:

- **Headlines** — Which ones appear most often? Which drive clicks?
- **Descriptions** — Identifying weak performers to replace
- **Images** — Size and format issues, performance rankings
- **Videos** — Are they even being shown? View-through rates

### Audience Signal Audit

Performance Max can ignore your carefully crafted audience signals. This skill detects:

- Whether your custom segments are actually being used
- If Google is expanding too aggressively beyond your signals
- Gaps in your first-party data integration
- Opportunities to strengthen signal quality

### Budget Allocation Insights

Using available placement data and creative heuristics:

- Estimated spend distribution across channels
- Identification of wasteful placements
- Recommendations for budget reallocation

### Product Feed Diagnostics (Shopping)

For ecommerce campaigns:

- Products consuming budget without converting
- High-potential products with low impression share
- Title and description optimization opportunities
- Image quality issues affecting performance

## Sample Diagnostic Report

```
## PMax Diagnostic: Campaign "Summer Collection 2025"

### Overall Health Score: 62/100

#### Critical Issues (Fix Now)
1. Asset Group "Women's Shoes" has 3 headlines rated "Low"
   - Replace: "Great Shoes for Every Occasion"
   - Replace: "Shop Our Collection Today"
   - Replace: "Free Shipping Available"
   → Suggested replacements provided below

2. Video assets not serving (0 impressions in 30 days)
   - Reason: Likely format/length issues
   - Action: Add 15-second vertical video

3. Audience signal utilization: 23% (Poor)
   - Your customer match list is being largely ignored
   - Recommendation: Strengthen with purchase data signals

#### Optimization Opportunities
- Product ID 4829 has 3.2x higher ROAS than campaign average
  but only 4% of budget. Consider dedicated asset group.

- Search impression share: 34% (opportunity: $2,400/mo)
  Increase budget or improve asset relevance for these queries:
  [query analysis follows]
```

## What Makes This Different

Unlike surface-level audits, this skill:

1. **Cross-references multiple data sources** — Combines asset reports, placement data, and product feed metrics
2. **Applies real-world heuristics** — Built from patterns observed across 200+ PMax accounts
3. **Provides specific actions** — Not just "improve your headlines" but actual replacement suggestions
4. **Estimates impact** — Quantifies the opportunity cost of each issue

## How to Use

After purchase, you'll receive the skill file to install in your Claude Code environment.

Run the diagnostic:

```
/pmax-diagnostic --campaign="Campaign Name" --lookback=30
```

The skill will guide you through providing the necessary data (API access or exports) and generate a comprehensive diagnostic report.

## Requirements

- Google Ads account with Performance Max campaigns
- At least 14 days of campaign data (30+ recommended)
- Google Merchant Center access (for Shopping diagnostics)
- Google Ads API access or export capabilities

## Included

- PMax Diagnostic skill file
- Setup guide for API integration
- Interpretation guide for diagnostic reports
- 30-day money-back guarantee
