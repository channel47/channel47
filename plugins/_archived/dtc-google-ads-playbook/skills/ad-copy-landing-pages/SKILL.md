---
name: Ad Copy & Landing Pages
description: >
  This skill should be used when the user asks to "write Google Ads headlines",
  "create Performance Max ad copy", "write Demand Gen ad descriptions", "design landing page
  structure for Google Ads", "set up tracking parameters", "create negative keyword lists",
  "write ad copy for a DTC offer", "plan landing page URLs with UTM parameters",
  "structure af_source tracking", or discusses ad creative strategy, offer positioning,
  headline frameworks, or landing page architecture for DTC Google Ads campaigns. Also
  triggered by questions about asset groups, headline rotation, description writing, or
  negative keyword strategy.
version: 1.0.0
---

# Ad Copy & Landing Page Playbook for DTC Google Ads

Frameworks for writing high-converting ad copy and structuring landing pages with proper tracking, derived from campaigns generating 16,000+ conversions at $330-$360 CPA.

## Headline Framework

Performance Max requires up to 15 headlines (30 chars) and 5 long headlines (90 chars). Fill every slot using this formula system.

### Short Headlines (30 char max)

Use these formulas, adapting product/offer for the brand:

| Formula | Example |
|---------|---------|
| `{Product} ${Price} {Audience} Only` | Tirzepatide $149 Women Only |
| `{Audience} Get ${Price} {Product}` | Seniors Get $149 Tirzepatide |
| `{Audience} Qualify in 5 Min` | Women Qualify in 5 Min |
| `Free Overnight Shipping` | Free Overnight Shipping |
| `${Price/Day} {Product}` | $4.9/Day Tirzepatide |
| `{Audience} Save {X}% This Week` | Seniors Save 30% This Week |
| `{Offer Name}: ${Price}` | Her Reset: $149 Deal |
| `Drop {X}lbs by {Month}` | Drop 40lbs by April |
| `{X}% Off {Product}: {Offer} Deal` | 30% Off GLP-1: Her Reset Deal |
| `Fast Online {Product} Access` | Fast Online GLP-1 Access |

**Key principles:**
- Lead with the audience when possible (creates instant relevance)
- Always include price point (specificity converts)
- Include urgency or time element in at least 2 headlines
- Use the offer/coupon name as a branded hook

### Long Headlines (90 char max)

Long headlines appear in display placements and should tell a mini-story:

| Formula | Example |
|---------|---------|
| `{Offer}: The {Audience}-Only {Product} Special. Get Started Today for Only ${Price}.` | Her Reset 2026: The Women-Only Tirzepatide Special. Get Started Today for Only $149. |
| `{Audience} — Apply Now to Claim {X}% Off {Product}. Limited Spots Available` | Seniors — Apply Now to Claim 30% Off Tirzepatide. Limited Spots Available |
| `Stop {Pain Point} and {Benefit} This {Month}. ${Price} {Product} for {Audience} at {Brand}.` | Stop Food Noise and Reclaim Your Body This February. $149 Tirzepatide for Women at Medvi. |
| `Drop {X}lbs by {Month} with personalized care and {Product} medication` | Drop 40lbs by April with personalized care and GLP-1 medication |
| `{Benefit}: {Product} for Less Than ${Price/Week}. This {Event} Deal Ends Soon.` | GLP-1 for Less Than $37/Week. This February Deal Ends Soon. See If You Qualify. |

### Descriptions (90 char max)

Write 5 descriptions covering these angles:

1. **Social proof + urgency:** "Join thousands of {audience} using {brand} for a {year} reset. ${price} offers end soon."
2. **Call to action + offer:** "Ready for a change? Use code {offer} for ${price} {product}. Quick online process."
3. **Benefit + price:** "Make {year} your year. Get doctor-prescribed {product} for ${price}. Fast online approval."
4. **Value prop + savings:** "Science-backed {benefit} tailored for {audience}. Save over {X}% and pay only ${price} today."
5. **Immediacy + access:** "Immediate online application — {audience} get discounted {product} for just ${price} today."

## Offer Naming Strategy

Create named offers/coupons that serve as campaign-level brands:

| Audience | Offer Name Example | Purpose |
|----------|-------------------|---------|
| Women | "Her Reset 2026" | Empowerment + seasonal hook |
| Seniors | "Senior Discount Program" | Trust + exclusivity |
| Moms | "Mom Reset" | Identity-based hook |
| General | "February Special" | Seasonal urgency |
| Men | "Reclaim26" | Aspiration + year |

Named offers create continuity across headlines, descriptions, and landing pages.

## Landing Page URL Architecture

Every campaign maps to a specific landing page URL with tracking parameters:

### URL Structure Pattern

```
https://{domain}/{page}?page={funnel}&af_source={offer_name}&uid={user_id}&oid={offer_id}&affid={affiliate_id}&sub4={wbraid}&sub5={gbraid}&sub3={gclid}&sub1={campaign_name}
```

**Parameter breakdown:**
| Parameter | Purpose | Example |
|-----------|---------|---------|
| `page` | Funnel step identifier | `dc1` (direct conversion 1) |
| `af_source` | Offer/campaign source tracking | `HerReset2026`, `February`, `Seniors2026` |
| `uid` | Landing page variant ID | `50`, `51`, `76` (different page designs) |
| `oid` | Offer ID | `5` |
| `affid` | Affiliate/team ID | `38` |
| `sub1` | Campaign name passthrough | `gpm-$149-women-4` |
| `sub3` | Google click ID | `{gclid}` |
| `sub4/sub5` | Google wbraid/gbraid | For iOS attribution |

### Domain Strategy

Use multiple domains/subdomains for different funnels:
- **`medvi.org/special.php`** — primary conversion page (highest volume)
- **`glp.medvi.org/special.php`** — secondary/variant page (phone-excl campaigns)
- **`medvi.org/?page=dc1`** — legacy/alternate funnel
- **`directmeds.com/dm-offers-stc/`** — partner brand offers

Map phone-exclusion campaigns to a different subdomain to track device-level landing page performance separately.

### Landing Page Variant Testing

Use the `uid` parameter to rotate landing page variants:
- `uid=50` — Variant A (e.g., long-form with testimonials)
- `uid=51` — Variant B (e.g., short-form with urgency)
- `uid=76` — Variant C (e.g., quiz-based funnel)
- `uid=44` — Variant D (e.g., direct offer page)

Each campaign should point to a specific `uid`. Compare conversion rates across UIDs to find winners per audience segment.

## Negative Keyword Strategy

Protect campaign efficiency with layered negative keywords:

### Campaign-Level Negatives

Block these categories at the campaign level:

1. **Brand misspellings that indicate different intent** — e.g., `[medvidi]` (different company)
2. **Competitor brand names (broad match)** — e.g., `Mounjaro`, `Zepbound`, `semaglutide` (prevent spend on competitor searches)
3. **Product terms that cannibalize other campaigns** — e.g., `[glp 1 weight loss]` blocked in one campaign to funnel it to another
4. **Navigational/existing customer queries** — e.g., `medvi login`, `medvi reviews` (existing customers, not new acquisition)
5. **Low-intent informational terms** — e.g., `weight loss drugs`, `oral semaglutide` (research intent, not purchase)

### Negative Keyword Lists

Create shared lists for terms to block across all campaigns:
- **"Competitor Brands"** — all major competitor names (broad match)
- **"Product Removal"** — specific product terms to exclude from certain campaigns (exact match)
- **"Brand Navigation"** — existing customer navigation queries (broad match)

### Search Term Review Cadence

Review search terms weekly. For each new term with 10+ clicks and zero conversions, add as a negative. For terms converting above target CPA, monitor for 2 more weeks before deciding.

## Asset Group Strategy for PMax

Each Performance Max campaign should have 2-4 asset groups with:
- **Different creative themes** (e.g., before/after, testimonial, product-focused)
- **Same audience signal** (the campaign defines the audience)
- **Same landing page** (URL with same af_source)
- **Varied headlines/descriptions** to test messaging angles

Mark asset groups as "Limited by policy" and appeal if necessary — this is common in health/wellness verticals and does not prevent delivery.

## Additional Resources

### Reference Files

For detailed copy examples and templates, consult:
- **`references/headline-swipe-file.md`** — 100+ proven headline templates across DTC verticals
- **`references/negative-keyword-templates.md`** — Pre-built negative keyword lists by industry vertical
