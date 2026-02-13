# Search Campaign Structure

Best practices for organizing Google Ads Search campaigns, ad groups, and keywords.

---

## Campaign Hierarchy

```
Account
└── Campaign
    ├── Settings (budget, bidding, location)
    ├── Ad Groups
    │   ├── Keywords
    │   ├── Ads (RSAs)
    │   └── Ad Group Negatives
    ├── Campaign Negatives
    └── Audiences (observation/targeting)
```

---

## Campaign Organization

### Campaign Segmentation Strategies

**By Intent:**
- Brand Campaign - Brand name searches
- Non-Brand Campaign - Product/service terms
- Competitor Campaign - Competitor names

**By Product/Service:**
- Product A Campaign
- Product B Campaign
- Service Campaign

**By Funnel Stage:**
- Awareness Campaign (informational keywords)
- Consideration Campaign (comparison keywords)
- Decision Campaign (purchase intent keywords)

**By Geography:**
- US Campaign
- UK Campaign
- Canada Campaign

### When to Separate Campaigns

Create separate campaigns when:
- Different daily budgets needed
- Different bidding strategies required
- Different geographic targets
- Different conversion goals
- Need separate performance tracking

### When to Keep in One Campaign

Keep together when:
- Shared budget
- Same bidding strategy
- Same geographic target
- Limited total keywords (under 500)

---

## Ad Group Organization

### The Single Theme Rule

Each ad group should contain keywords that:
- Share the same search intent
- Could trigger the same ad
- Lead to the same landing page

### Ad Group Size Guidelines

| Scenario | Keywords per Ad Group |
|----------|----------------------|
| Ideal | 5-15 |
| Acceptable | 15-30 |
| Too Large | 30+ (split into multiple) |
| Too Small | Under 5 (consider consolidating) |

### Ad Group Naming Conventions

Use consistent, descriptive names:

**Format:** `[Category] - [Modifier/Theme]`

**Examples:**
- `Running Shoes - Best`
- `Running Shoes - Reviews`
- `Running Shoes - For Women`
- `CRM Software - Small Business`
- `CRM Software - Comparison`

### Clustering Keywords into Ad Groups

**Step 1: Identify Core Themes**
- What are the main topics/products?
- What modifiers appear frequently?

**Step 2: Group by Intent**
- Informational (how to, what is)
- Commercial (best, reviews, comparison)
- Transactional (buy, price, discount)

**Step 3: Check Ad Relevance**
- Can all keywords in this group share one ad?
- Does the landing page match all keywords?

---

## Budget Allocation

### Single Campaign Budget

For accounts with one campaign:
- Set daily budget = Monthly budget / 30.4
- Google may spend up to 2x daily budget on high-traffic days
- Monthly spend won't exceed daily budget x 30.4

### Multi-Campaign Budget Strategy

**Priority-Based Allocation:**

| Campaign Type | Budget Share | Rationale |
|--------------|--------------|-----------|
| Brand | 10-15% | Protects brand, high conversion rate |
| High-Intent Non-Brand | 50-60% | Primary revenue driver |
| Mid-Funnel | 20-30% | Builds pipeline |
| Competitor | 5-10% | Conquest (lower conversion) |

**Performance-Based Reallocation:**
- Review weekly
- Shift budget toward campaigns meeting CPA/ROAS goals
- Reduce budget on underperformers
- Maintain brand campaign regardless

### Shared Budgets

**When to Use:**
- Multiple campaigns, flexible daily allocation
- Want Google to optimize spend across campaigns
- Trust algorithm to allocate

**When to Avoid:**
- Need guaranteed spend per campaign
- Brand protection requires fixed budget
- Testing new campaigns

---

## Keyword Organization

### Match Type Distribution

**Conservative Approach:**
- 70% Exact match
- 30% Phrase match
- 0% Broad match

**Balanced Approach:**
- 30% Exact match
- 50% Phrase match
- 20% Broad match

**Aggressive Approach (with Smart Bidding):**
- 10% Exact match
- 30% Phrase match
- 60% Broad match

### Keyword Prioritization

**Tier 1 - Launch First:**
- High purchase intent
- Proven converters
- Brand terms

**Tier 2 - Add After Validation:**
- Medium intent
- Higher volume, lower conversion
- Adjacent topics

**Tier 3 - Test Carefully:**
- Broad discovery terms
- High volume, uncertain intent
- Competitor terms

---

## Landing Page Alignment

### Best Practices

- Match ad group theme to landing page content
- Use dedicated landing pages for distinct product lines
- Ensure landing page contains ad group keywords
- Mobile-optimized pages essential

### URL Structure

**Campaign Level:**
- Set default Final URL
- Used when ad group doesn't specify

**Ad Group Level:**
- Override with specific landing pages
- Use for product-specific ad groups

**Ad Level:**
- Can vary URLs within same ad group
- Use for testing landing pages

---

## Quality Score Considerations

### Components

| Factor | Weight | How to Improve |
|--------|--------|----------------|
| Expected CTR | ~40% | Write compelling ads, use relevant keywords |
| Ad Relevance | ~20% | Include keywords in ad copy |
| Landing Page | ~40% | Relevant content, fast load, mobile-friendly |

### Structure Impacts Quality Score

Good structure improves Quality Score:
- Tight keyword themes = higher ad relevance
- Specific ads per group = higher CTR
- Matched landing pages = better experience

---

## Scaling Structure

### Starting Small (Under $3k/month)

```
Account
└── Main Campaign
    ├── Ad Group: [High Intent]
    ├── Ad Group: [Problem/Solution]
    └── Ad Group: [Product Category]
```

### Growing (Under $10k/month)

```
Account
├── Brand Campaign
│   └── Ad Group: Brand Terms
├── Non-Brand Campaign
│   ├── Ad Group: [Theme 1]
│   ├── Ad Group: [Theme 2]
│   └── Ad Group: [Theme 3]
└── Competitor Campaign (optional)
    └── Ad Group: Competitor Terms
```

### Mature ($10k+/month)

```
Account
├── Brand Campaign
├── Non-Brand - High Intent
│   ├── Ad Group: [Theme A]
│   └── Ad Group: [Theme B]
├── Non-Brand - Mid Funnel
│   ├── Ad Group: [Theme C]
│   └── Ad Group: [Theme D]
├── Competitor Campaign
└── RLSA Campaign (remarketing)
```

---

## Common Mistakes

1. **One ad group with all keywords** - Impossible to write relevant ads
2. **Too many ad groups** - Dilutes data, harder to optimize
3. **Keywords don't match ads** - Low Quality Score
4. **Ignoring negative keywords** - Wasted spend on irrelevant searches
5. **Same landing page for everything** - Poor user experience
6. **No brand campaign** - Competitors steal brand traffic
7. **Mixing intents in one ad group** - Ad can't be relevant to all
