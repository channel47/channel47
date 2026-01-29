---
name: search
description: |
  Create Google Ads Search campaigns with proper keyword structure, ad groups, match types, and audience targeting. Outputs CSV ready for Google Ads Editor bulk upload.
---

# Search Campaign Builder

Create Search campaigns with optimized structure, keyword organization, and ad copy.

## Reference Files

This skill uses these reference documents:
- [Campaign Structure](./campaign-structure.md) - Campaign hierarchy, ad group organization, budget allocation
- [Keyword Match Types](./keyword-match-types.md) - Exact, phrase, broad strategies and when to use each
- [Audience Signals](./audience-signals.md) - Observation and targeting audiences for Search

---

## Required Inputs

Before starting, you MUST collect:

1. **Product/Service** - What's being advertised
2. **Landing Page URL** - Destination for ad clicks
3. **Target Geography** - Countries/regions
4. **Monthly Budget** - Campaign spend target
5. **Keyword Research** - From keyword-researcher agent or user-provided list

If not provided, ask:

> "I need these inputs to build your Search campaign:
> 1. What product/service are you advertising?
> 2. Landing page URL
> 3. Target countries/regions
> 4. Monthly budget
> 5. Keyword list (or run /ads:keyword-researcher first)
>
> Which can you provide?"

---

## Phase 1: Input Analysis

### If Keywords Provided

Review the keyword list for:
- Total keyword count
- Volume distribution (high/medium/low)
- Intent clusters (brand, non-brand, competitor)
- Match type recommendations

### If No Keywords

Direct user to keyword research:

> "You'll need keywords first. Would you like me to:
> 1. Run the keyword-researcher agent now
> 2. Accept a keyword list you provide
>
> Which approach?"

If option 1, hand off to keyword-researcher agent.

---

## Phase 2: Campaign Structure Design

Reference: [Campaign Structure](./campaign-structure.md)

### Determine Campaign Count

**Single Campaign** - Use when:
- One product/service focus
- Budget under $3,000/month
- Unified geographic targeting

**Multiple Campaigns** - Use when:
- Brand vs non-brand separation needed
- Competitor conquest keywords
- Different landing pages per product
- Multiple geographic targets with different bids

### Standard Campaign Types

| Campaign | Keywords | Purpose |
|----------|----------|---------|
| Core/Non-Brand | Product/service terms | Main conversion driver |
| Brand | Brand name terms | Protect brand searches |
| Competitor | Competitor names | Conquest strategy |

Ask user:

> "Based on your keywords, I recommend this structure:
> 1. [Campaign A] - [X keywords]
> 2. [Campaign B] - [Y keywords]
>
> Does this structure work for your goals?"

---

## Phase 3: Ad Group Organization

Reference: [Campaign Structure](./campaign-structure.md)

### Cluster Keywords by Intent

Group keywords into ad groups based on:
- Search intent (problem, solution, comparison)
- Theme/topic
- Funnel stage

**Target:** 5-20 keywords per ad group

### Ad Group Naming

Use descriptive names:
- `[Intent] - [Theme]` (e.g., "Problem - Stain Removal")
- `[Product] - [Modifier]` (e.g., "Running Shoes - Best")

### Create Ad Group Plan

For each ad group, define:
- Ad group name
- Keywords (with match types)
- Landing page URL (if different from campaign default)
- Responsive Search Ad copy

---

## Phase 4: Match Type Strategy

Reference: [Keyword Match Types](./keyword-match-types.md)

### Default Approach

For most campaigns:

| Match Type | Usage | Purpose |
|------------|-------|---------|
| Exact | Top 20-30% of keywords by priority | Precision bidding |
| Phrase | 50-60% of keywords | Balanced reach |
| Broad | 10-20% of keywords (with smart bidding) | Discovery |

### Assign Match Types

Ask user preference:

> "Match type strategy options:
> 1. **Conservative** - Exact + Phrase only (more control)
> 2. **Balanced** - Mix of Exact, Phrase, Broad (recommended)
> 3. **Aggressive** - Broad-heavy with smart bidding (max reach)
>
> Which approach?"

Apply match types based on selection.

---

## Phase 5: Ad Copy Creation

### Responsive Search Ads (RSA)

Each ad group needs at least 1 RSA with:

**Headlines (minimum 8, max 15):**
- 30 characters max each
- Include keyword in at least 2
- Include brand in at least 1
- Include CTA in at least 1
- Include offer/benefit in several

**Descriptions (minimum 2, max 4):**
- 90 characters max each
- Lead with strongest value proposition
- Include CTA
- Include differentiators

### Ad Copy Generation

Generate ad copy suggestions based on:
- Landing page content (if URL provided)
- Keyword themes in ad group
- Best practices

Present options for user review:

```
Ad Group: [Name]

Headlines:
1. [Headline suggestion]
2. [Headline suggestion]
...

Descriptions:
1. [Description suggestion]
2. [Description suggestion]
```

---

## Phase 6: Audience Configuration

Reference: [Audience Signals](./audience-signals.md)

### Observation vs Targeting

**Observation Mode (Recommended for Search):**
- Ads show to all searchers
- Collect data on audience performance
- Apply bid adjustments later

**Targeting Mode:**
- Ads only show to audience members
- Restricts reach significantly
- Use only for specific strategies

### Recommended Audiences

Add as observation:
- In-market for [relevant category]
- Website visitors (remarketing)
- Customer match (if available)
- Similar audiences

---

## Phase 7: Negative Keywords

### Campaign-Level Negatives

Add negatives to prevent irrelevant traffic:

**Standard Exclusions:**
- DIY terms (if not applicable)
- Free/cheap (if premium product)
- Jobs/careers
- [Industry]-specific irrelevant terms

**Cross-Campaign Negatives:**
- Add brand terms as negatives to non-brand campaigns
- Add competitor terms as negatives to core campaigns

### Ad Group-Level Negatives

Prevent overlap between ad groups:
- Add ad group A keywords as negatives to ad group B
- Ensures each search triggers the most relevant ad group

---

## Phase 8: Campaign Settings

### Budget & Bidding

| Monthly Budget | Bidding Strategy |
|---------------|------------------|
| < $1,500 | Maximize Clicks (initially) or Maximize Conversions |
| $1,500 - $5,000 | Maximize Conversions |
| > $5,000 | Target CPA or Target ROAS (with conversion history) |

### Network Settings

**Recommended:**
- Search Network: ON
- Search Partners: OFF (initially, test later)
- Display Network: OFF (use separate Display campaigns)

### Ad Rotation

- Optimize: Prefer best performing ads (recommended)
- Rotate indefinitely: Only for A/B testing

---

## Phase 9: Output Generation

### File 1: Campaign Structure (`search-campaign-[name].md`)

```markdown
# Search Campaign: [Campaign Name]

## Campaign Settings
- **Goal:** [goal]
- **Daily Budget:** $[amount]
- **Bidding:** [strategy]
- **Location:** [targets]
- **Language:** [language]
- **Networks:** Search only

## Ad Groups

### Ad Group: [Name]
**Keywords:** [count]
**Landing Page:** [URL]

| Keyword | Match Type | Volume | CPC |
|---------|------------|--------|-----|
| [keyword] | [type] | [vol] | [$X] |

**Responsive Search Ad:**

Headlines:
1. [headline]
2. [headline]
...

Descriptions:
1. [description]
2. [description]

---

## Negative Keywords

### Campaign Level
- [negative]
- [negative]

### By Ad Group
[If applicable]

---

## Audiences (Observation)
- [audience 1]
- [audience 2]
```

### File 2: Google Ads Editor CSV (`keywords-[campaign].csv`)

```csv
Campaign,Ad Group,Keyword,Match Type,Final URL,Max CPC
[campaign],[ad group],[keyword],[Exact/Phrase/Broad],[url],[bid]
```

Ready for Google Ads Editor bulk upload.

### File 3: Ad Copy CSV (`ads-[campaign].csv`)

```csv
Campaign,Ad Group,Headline 1,Headline 2,Headline 3,Headline 4,Headline 5,Headline 6,Headline 7,Headline 8,Description 1,Description 2,Final URL,Path 1,Path 2
[campaign],[ad group],[h1],[h2],...,[d1],[d2],[url],[path],[path]
```

### File 4: Negatives CSV (`negatives-[campaign].csv`)

```csv
Campaign,Ad Group,Negative Keyword,Match Type
[campaign],[ad group or empty for campaign-level],[negative],[type]
```

---

## Quality Checklist

Before delivering:
- [ ] Keywords grouped by clear themes
- [ ] Each ad group has 5-20 keywords
- [ ] Match types assigned strategically
- [ ] Each ad group has RSA with 8+ headlines
- [ ] Headlines under 30 characters
- [ ] Descriptions under 90 characters
- [ ] Negative keywords configured
- [ ] Brand/competitor keywords separated
- [ ] CSV format matches Google Ads Editor spec

---

## What You Don't Do

- Start without keywords or landing page
- Create ad groups with 100+ keywords
- Use only one match type across entire campaign
- Skip negative keyword configuration
- Create ads without reviewing landing page
- Mix brand and non-brand in same campaign
- Use Display Network in Search campaigns
