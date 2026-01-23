---
name: pmax
description: |
  Create Performance Max campaigns with proper asset group structure, audience signals, and asset requirements. Outputs campaign configuration ready for Google Ads.
---

# Performance Max Campaign Builder

Create PMax campaigns with optimized structure, audience signals, and compliant assets.

## Reference Files

This skill uses these reference documents:
- [Campaign Structure](./campaign-structure.md) - Asset groups, URL expansion, budget allocation
- [Audience Signals](./audience-signals.md) - Custom segments, first-party data, Google audiences
- [Asset Requirements](./asset-requirements.md) - Google's official specs for all asset types

---

## Required Inputs

Before starting, you MUST collect:

1. **Business URL** - The landing page or website
2. **Product/Service** - What's being advertised
3. **Target Geography** - Countries/regions
4. **Monthly Budget** - Campaign spend target
5. **Goal** - Sales, leads, website traffic, or store visits

If not provided, ask:

> "I need these inputs to build your PMax campaign:
> 1. Landing page URL
> 2. What product/service are you advertising?
> 3. Target countries/regions
> 4. Monthly budget
> 5. Primary goal (sales/leads/traffic/store visits)
>
> Which can you provide?"

---

## Phase 1: URL Analysis

Use WebFetch on the landing page to extract:
- Business name and category
- Products/services offered
- Unique selling points
- Target audience signals
- Existing brand assets (logos, colors, tone)

Summarize findings in 3-4 sentences.

---

## Phase 2: Campaign Structure Design

Reference: [Campaign Structure](./campaign-structure.md)

### Determine Asset Group Strategy

**Single Asset Group** - Use when:
- One product/service
- Unified audience
- Budget under $3,000/month

**Multiple Asset Groups** - Use when:
- Multiple product lines
- Distinct audience segments
- Budget over $3,000/month

### URL Expansion Settings

Ask user:

> "URL Expansion Options:
> 1. **ON** (Recommended) - Google shows ads for relevant pages across your site
> 2. **OFF** - Ads only drive to your specified landing page
> 3. **Exclude specific URLs** - Expansion on, but block certain pages
>
> Which approach?"

If user selects option 3, collect URLs to exclude.

---

## Phase 3: Audience Signals

Reference: [Audience Signals](./audience-signals.md)

### Custom Segments

Create 2-3 custom segments based on:

1. **Search-based segment**: Keywords people search before buying
2. **URL-based segment**: Competitor/industry websites they visit
3. **App-based segment**: Apps your audience uses (if applicable)

### First-Party Data

Ask user:

> "Do you have any of these to upload?
> 1. Customer email lists
> 2. Website remarketing audiences
> 3. YouTube viewers
> 4. App users
>
> (These significantly improve PMax performance)"

### Google Audiences

Select relevant:
- In-market audiences (active researchers)
- Affinity audiences (lifestyle/interests)
- Life events (if applicable)
- Detailed demographics

---

## Phase 4: Asset Collection

Reference: [Asset Requirements](./asset-requirements.md)

### Required Text Assets

Collect from user or generate suggestions:

**Headlines (minimum 5, max 15)**
- 3-5 headlines, max 30 characters each
- At least 1 with brand name
- Mix benefit-focused and feature-focused

**Long Headlines (minimum 1, max 5)**
- Max 90 characters each
- More descriptive, benefit-rich

**Descriptions (minimum 2, max 5)**
- Max 90 characters each
- Include CTA and key benefits

**Business Name**
- Max 25 characters

**Call to Action**
- Select from Google's options or use "Automated"

### Required Image Assets

**Landscape Images (minimum 1, required)**
- 1200 x 628 px (1.91:1 ratio)
- Max 5 MB, JPG/PNG

**Square Images (minimum 1, required)**
- 1200 x 1200 px (1:1 ratio)
- Max 5 MB, JPG/PNG

**Portrait Images (optional but recommended)**
- 960 x 1200 px (4:5 ratio)
- Max 5 MB, JPG/PNG

**Logo (required)**
- Square: 1200 x 1200 px
- Landscape: 1200 x 300 px (optional)
- Max 5 MB, PNG with transparency preferred

### Video Assets (Optional but Strongly Recommended)

- Minimum 10 seconds duration
- YouTube hosted
- Landscape, square, or portrait
- Google will auto-generate if not provided (lower quality)

### Asset Generation Option

After collecting asset information, assess what's provided vs needed:

```
ASSET STATUS
------------
| Type | Required | Status |
|------|----------|--------|
| Landscape | 1200x628 | [provided/needed] |
| Square | 1200x1200 | [provided/needed] |
| Portrait | 960x1200 | [provided/needed] |
| Logo | 1200x1200 | [provided/needed] |
```

If any required images are needed, offer generation:

> "Based on your asset requirements:
> - [n] required images are missing
> - [n] optional images would improve performance
>
> Would you like me to generate these?
> 1. Yes, run /ads:assets to generate missing images
> 2. No, I'll provide them manually
> 3. Skip optional, continue with required only"

If user selects option 1:
- Launch `/ads:assets` skill with product URL from Phase 1
- Return to Phase 5 when assets are generated

---

## Phase 5: Campaign Settings

### Budget & Bidding

Based on user's monthly budget, recommend:

| Monthly Budget | Daily Budget | Bidding Strategy |
|---------------|--------------|------------------|
| < $1,500 | Budget / 30.4 | Maximize Conversions |
| $1,500 - $5,000 | Budget / 30.4 | Maximize Conversions (consider tCPA after 30 conversions) |
| > $5,000 | Budget / 30.4 | Target CPA or Target ROAS (if sufficient data) |

### Network Settings

PMax automatically runs across all Google networks:
- Search
- Display
- YouTube
- Discover
- Gmail
- Maps

User cannot exclude networks in PMax.

### Location & Language

Configure based on user's target geography input.

---

## Phase 6: Review & Output

Generate campaign configuration document:

```markdown
# PMax Campaign: [Campaign Name]

## Campaign Settings
- **Goal:** [goal]
- **Daily Budget:** $[amount]
- **Bidding:** [strategy]
- **Location:** [targets]
- **Language:** [language]
- **URL Expansion:** [ON/OFF/Exclusions]

## Asset Group: [Name]

### Final URL
[landing page URL]

### Audience Signals

**Custom Segments:**
1. [Segment name]: [keywords or URLs]
2. [Segment name]: [keywords or URLs]

**First-Party Data:** [Yes/No - type]

**Google Audiences:**
- In-market: [list]
- Affinity: [list]

### Text Assets

**Headlines:**
1. [headline]
2. [headline]
...

**Long Headlines:**
1. [long headline]
...

**Descriptions:**
1. [description]
2. [description]
...

### Image Assets

| Asset Type | Dimensions | File |
|------------|------------|------|
| Landscape | 1200x628 | [filename or "needed"] |
| Square | 1200x1200 | [filename or "needed"] |
| Portrait | 960x1200 | [filename or "needed"] |
| Logo (square) | 1200x1200 | [filename or "needed"] |

### Video Assets
[YouTube URLs or "Will use auto-generated"]

---

## Next Steps
1. [ ] Upload images to Google Ads
2. [ ] Connect first-party data (if available)
3. [ ] Create custom segments in Audience Manager
4. [ ] Launch campaign
5. [ ] Allow 2 weeks learning period before optimizations
```

---

## Quality Checklist

Before delivering:
- [ ] All required asset minimums met
- [ ] Headlines under 30 characters
- [ ] Long headlines under 90 characters
- [ ] Descriptions under 90 characters
- [ ] Image dimensions correct
- [ ] Audience signals configured
- [ ] Budget and bidding appropriate for spend level
- [ ] URL expansion setting confirmed

---

## What You Don't Do

- Start without landing page URL
- Recommend PMax for brand-new accounts with no conversion data
- Promise specific performance results
- Skip audience signal configuration
- Use placeholder text in final output
