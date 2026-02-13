# Audience Signals for Search Campaigns

Using audiences in Google Ads Search campaigns for observation, targeting, and bid adjustments.

---

## Observation vs Targeting

### Observation Mode

**How it works:**
- Ads show to ALL searchers matching your keywords
- Audience data collected alongside keyword data
- No reach restriction

**When to use:**
- Starting out with Search campaigns
- Gathering audience insights
- Want to apply bid adjustments later

### Targeting Mode

**How it works:**
- Ads ONLY show to searchers who are also in your audience
- Significantly restricts reach
- Combines keyword + audience requirement

**When to use:**
- RLSA (Remarketing Lists for Search Ads)
- Customer match targeting
- Very specific audience strategies

---

## Adding Audiences to Search

### Step-by-Step

1. Campaign or Ad Group > Audiences
2. Click "Edit Audiences"
3. Select "Observation" or "Targeting"
4. Browse or search for audiences
5. Apply

### Campaign vs Ad Group Level

**Campaign level:**
- Applies to all ad groups
- Good for broad audiences
- Easier management

**Ad group level:**
- Specific to that ad group
- Good for theme-matched audiences
- More granular control

---

## Audience Types for Search

### Website Visitors (Remarketing)

People who visited your website.

**Segments to create:**
- All website visitors (30/60/90/180 days)
- Product page viewers
- Cart abandoners
- Past purchasers
- High-value page visitors

**Use case:** Bid higher for people already familiar with your brand.

### Customer Match

Upload your customer lists.

**Segments:**
- All customers
- High-LTV customers
- Recent purchasers
- Lapsed customers
- Newsletter subscribers

**Use case:** Bid higher for existing customers or exclude them.

### Similar Audiences

Based on your remarketing lists and customer match.

**Google creates:**
- Similar to all converters
- Similar to high-value customers
- Similar to remarketing lists

**Use case:** Find new customers like your best existing ones.

### In-Market Audiences

People actively researching or planning to buy.

**Examples:**
- In-market for Business Services
- In-market for Consumer Electronics
- In-market for Travel

**Use case:** Identify high-intent searchers and bid accordingly.

### Affinity Audiences

People with demonstrated interests.

**Examples:**
- Business Professionals
- Technology Enthusiasts
- Health & Fitness Buffs

**Use case:** Layer on top of keywords for better targeting signals.

### Detailed Demographics

Target by life circumstances.

**Options:**
- Parental status
- Marital status
- Education
- Homeownership
- Employment status

**Use case:** Refine targeting for specific customer profiles.

---

## RLSA (Remarketing Lists for Search Ads)

### What Is RLSA?

Combining remarketing audiences with Search campaigns.

### Two Strategies

**Strategy 1: Observation + Bid Adjustments**
- Show ads to everyone
- Bid higher for remarketing audiences
- Most common approach

**Strategy 2: Targeting Only (RLSA-Only Campaign)**
- Ads only show to past visitors
- Can use broader keywords
- Higher conversion rate, lower volume

### RLSA Best Practices

1. Create separate RLSA campaign for different bidding strategy
2. Use broader keywords than regular Search (past visitors convert better)
3. Segment by recency (0-7 days, 8-30 days, 31-90 days)
4. Exclude converters or target specifically

---

## Bid Adjustments

### How Bid Adjustments Work

Increase or decrease bids for specific audiences.

**Formula:** Base bid × (1 + adjustment) = Audience bid

**Example:**
- Base bid: $2.00
- Audience adjustment: +50%
- Audience bid: $2.00 × 1.5 = $3.00

### Recommended Starting Adjustments

| Audience | Starting Adjustment |
|----------|-------------------|
| All website visitors | +25% to +50% |
| Cart abandoners | +50% to +100% |
| Past purchasers | +20% to +50% (or exclude) |
| High-LTV customers | +75% to +150% |
| Similar audiences | +10% to +25% |
| In-market audiences | +10% to +30% |

### Adjustment Strategy

1. Start with observation only (no adjustments)
2. Gather 2-4 weeks of data
3. Review conversion rates by audience
4. Apply adjustments based on performance
5. Monitor and refine monthly

---

## Audience Exclusions

### Why Exclude Audiences?

- Prevent wasted spend
- Separate campaign strategies
- Avoid annoying recent converters

### Common Exclusions

**Exclude from non-brand campaigns:**
- Past 7-day converters (already purchased)
- Irrelevant remarketing lists

**Exclude from acquisition campaigns:**
- All customers (for new customer focus)

**Exclude from RLSA campaigns:**
- All website visitors (for non-RLSA control)

---

## Combined Audiences

### Creating Combined Audiences

In Audience Manager, combine audiences with AND/OR logic.

**Examples:**
- Website visitors AND in-market for [category]
- Cart abandoners AND NOT past purchasers
- High-value customers OR similar audiences

### Use Cases

- More precise targeting
- Better bid adjustment logic
- Cleaner reporting

---

## Audience Insights

### Where to Find Data

1. Campaign > Audiences
2. View metrics by audience
3. Compare conversion rates, CPA, ROAS

### What to Look For

| Metric | What It Tells You |
|--------|-------------------|
| Conversion rate | Audience quality |
| Cost per conversion | Efficiency |
| Conversion value | Revenue potential |
| Impression share | Room to grow |

### Optimization Actions

**High conversion rate, low volume:**
- Increase bid adjustment
- Expand similar audiences

**Low conversion rate, high volume:**
- Decrease bid adjustment
- Consider exclusion

**High conversion rate, high CPA:**
- Audience is valuable but expensive
- May need landing page improvements

---

## Search vs PMax Audience Differences

| Aspect | Search | PMax |
|--------|--------|------|
| Role | Optional layer on keywords | Required signals |
| Default | Observation | Signals (suggestions) |
| Restrictions | Can target/exclude | Can't restrict |
| Bid control | Manual adjustments | Algorithmic |

---

## Implementation Checklist

For new Search campaigns:

1. [ ] Add all website visitors as observation
2. [ ] Add relevant in-market audiences
3. [ ] Add customer match (if available)
4. [ ] Run 2-4 weeks without adjustments
5. [ ] Review performance by audience
6. [ ] Apply bid adjustments based on data
7. [ ] Create RLSA campaign (optional)
8. [ ] Set up audience exclusions as needed

---

## Common Mistakes

1. **Using targeting mode too early** - Restricts reach before you have data
2. **No audiences added** - Missing valuable insights
3. **Aggressive bid adjustments without data** - Based on assumptions
4. **Not segmenting remarketing by recency** - Recent visitors convert better
5. **Forgetting exclusions** - Wasting budget on converters
6. **Ignoring audience insights** - Missing optimization opportunities
