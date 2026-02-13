# PMax Campaign Structure

Performance Max campaigns use asset groups instead of ad groups. This document covers structural best practices.

---

## Campaign Hierarchy

```
Campaign
└── Asset Group(s)
    ├── Final URL
    ├── Audience Signals
    ├── Text Assets (headlines, descriptions)
    ├── Image Assets
    ├── Video Assets
    └── Extensions
```

---

## Asset Groups

### What Is an Asset Group?

An asset group is a collection of creatives centered around a single theme or product. Google's AI combines assets to create ads across all channels.

### When to Use Single vs Multiple Asset Groups

**Single Asset Group:**
- One product or service
- One target audience
- Unified messaging
- Budget under $3,000/month
- Simpler reporting and optimization

**Multiple Asset Groups:**
- Distinct product categories
- Different audience segments
- Varied messaging needs
- Budget supports split testing
- Need granular performance data

### Asset Group Naming Convention

Use descriptive names for easier reporting:
- `[Product] - [Audience]` (e.g., "Running Shoes - Fitness Enthusiasts")
- `[Category] - [Intent]` (e.g., "Software - Trial Seekers")

---

## URL Expansion

### How It Works

When enabled, Google can show ads for pages beyond your specified Final URL if they're relevant to the user's search.

### Settings

| Setting | Behavior | Best For |
|---------|----------|----------|
| **ON** | Google uses any relevant page on your domain | E-commerce, content-rich sites |
| **OFF** | Only your specified Final URL | Single product, specific landing pages |
| **Exclusions** | Expansion on, but specific URLs blocked | Most sites (exclude irrelevant pages) |

### URL Exclusion Best Practices

Exclude:
- Careers/jobs pages
- About us/company pages
- Blog posts unrelated to products
- Support/help center
- Privacy policy, terms of service
- Pages with broken tracking
- Low-converting pages

### How to Exclude URLs

In Google Ads:
1. Campaign Settings > Additional Settings
2. URL Expansion > Exclude URLs
3. Add URL patterns (supports wildcards)

---

## Budget Allocation

### Single Campaign

For most advertisers, one PMax campaign is sufficient:
- Easier to manage
- Algorithm has more data
- Clearer performance picture

### Multiple Campaigns

Consider separate campaigns when:
- Distinct business lines with separate budgets
- Different conversion goals (leads vs sales)
- Geographic separation needed
- Vastly different ROAS targets

### Budget Recommendations by Spend

| Monthly Spend | Recommended Structure |
|--------------|----------------------|
| < $3,000 | 1 campaign, 1-2 asset groups |
| $3,000 - $10,000 | 1 campaign, 2-4 asset groups |
| $10,000 - $50,000 | 1-2 campaigns, 3-5 asset groups each |
| > $50,000 | Multiple campaigns by business line |

---

## Campaign Settings

### Bidding Strategies

| Strategy | When to Use | Requirements |
|----------|-------------|--------------|
| Maximize Conversions | New campaigns, limited data | Conversion tracking |
| Maximize Conversion Value | E-commerce with varied product values | Value tracking |
| Target CPA | Established campaigns with stable CPA | 30+ conversions/month |
| Target ROAS | E-commerce with consistent ROAS | 30+ conversions/month |

### Location Targeting

- Target by country, region, state, city, or radius
- Use "Presence" (recommended) vs "Presence or Interest"
- Exclude locations where you can't serve customers

### Language Targeting

- Match user's browser/Google language settings
- Can target multiple languages in one campaign
- Don't restrict unnecessarily

---

## Learning Period

### What to Expect

- **Duration:** 1-2 weeks minimum
- **Behavior:** Performance may fluctuate
- **Spend:** May not hit full daily budget initially

### Best Practices During Learning

- Don't make changes for first 2 weeks
- Avoid pausing/resuming the campaign
- Don't adjust bids or budgets
- Let the algorithm gather data

### After Learning Period

Review performance weekly:
- Check asset group performance
- Review audience insights
- Analyze top-performing asset combinations
- Adjust audience signals if needed

---

## Reporting & Optimization

### Key Metrics to Monitor

| Metric | What It Tells You |
|--------|-------------------|
| Conversions | Primary success metric |
| Cost/Conversion | Efficiency |
| Conversion Value | Revenue (if tracked) |
| Asset Performance | Which creatives work |
| Audience Insights | Who's converting |

### Asset Group Insights

In Google Ads, view:
- Asset performance ratings (Best, Good, Low)
- Top asset combinations
- Audience segment performance

### When to Add/Remove Asset Groups

**Add new asset group when:**
- Launching new product line
- Testing new audience
- Performance plateau (test new messaging)

**Remove/pause asset group when:**
- Consistently underperforms for 30+ days
- Product discontinued
- Budget constraints require focus

---

## Common Mistakes

1. **Too many asset groups** - Splits budget and data
2. **Vague asset group themes** - Mixed messaging confuses algorithm
3. **Ignoring URL expansion** - Missing relevant traffic or showing irrelevant pages
4. **Changing settings during learning** - Resets the algorithm
5. **No audience signals** - Algorithm starts cold
6. **Single headline/description** - Limits ad combinations
