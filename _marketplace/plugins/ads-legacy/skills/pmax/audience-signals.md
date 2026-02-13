# Audience Signals for Performance Max

Audience signals tell Google who your ideal customers are. They're suggestions, not restrictions - Google uses them as starting points for optimization.

---

## How Audience Signals Work

**Signals ≠ Targeting**

Unlike Search or Display campaigns, PMax audience signals are hints:
- Google starts by showing ads to signaled audiences
- Learns which users convert
- Expands to similar users automatically
- May show ads outside your signals if likely to convert

---

## Custom Segments

Custom segments let you define audiences based on their behavior.

### Search-Based Segments

Target users who search for specific keywords on Google.

**How to Create:**
1. Audience Manager > Custom Segments > New
2. Select "People who searched for any of these terms"
3. Add keywords

**Best Practices:**
- Use buyer-intent keywords (not just awareness)
- Include competitor brand searches
- Add product-specific terms
- 10-15 keywords per segment works well

**Example Keywords (E-commerce):**
```
buy [product]
[product] price
best [product] 2024
[product] reviews
[competitor] alternative
where to buy [product]
[product] near me
```

### URL-Based Segments

Target users who browse specific types of websites.

**How to Create:**
1. Audience Manager > Custom Segments > New
2. Select "People who browse types of websites"
3. Add URLs

**Best Practices:**
- Use competitor websites
- Include industry publications
- Add review sites in your category
- 5-10 URLs per segment

**Example URLs:**
- Direct competitors' homepages
- Industry comparison sites
- Relevant subreddits or forums
- Trade publication sites

### App-Based Segments

Target users who use specific apps.

**Best For:**
- Mobile-focused products
- App promotion
- Lifestyle/hobby targeting

**Example Apps:**
- Competitor apps
- Category-adjacent apps
- Lifestyle apps matching your audience

---

## First-Party Data

Your own customer data is the strongest signal.

### Customer Match (Email Lists)

Upload customer email lists:
- Past purchasers
- Newsletter subscribers
- Leads
- High-value customers

**Requirements:**
- Minimum 1,000 matched users
- Hashed or plain text (Google hashes automatically)
- Terms of service compliance

**Segment Ideas:**
- All customers
- High-LTV customers
- Repeat buyers
- Recent purchasers (90 days)
- Lapsed customers

### Website Remarketing

Requires Google Ads tag installed.

**Segments to Create:**
- All website visitors
- Product page viewers
- Cart abandoners
- Past converters
- Blog/content viewers

### YouTube Audiences

If you have a YouTube channel:
- Channel subscribers
- Video viewers
- Liked a video
- Commented on a video

### App Users

For mobile app owners:
- All app users
- In-app purchasers
- Specific action completers

---

## Google Audiences

Pre-built audiences based on Google's data.

### In-Market Audiences

Users actively researching or planning to buy.

**How to Find Relevant Segments:**
1. Audience Manager > Browse
2. Filter by "In-market"
3. Search your category

**Examples:**
- "In-market for Business Software"
- "In-market for Fitness Equipment"
- "In-market for Home Services"

### Affinity Audiences

Users with demonstrated interests and lifestyles.

**How to Use:**
- Match to your customer profile
- Broader than in-market
- Good for awareness + conversion

**Examples:**
- "Health & Fitness Buffs"
- "Business Professionals"
- "Technophiles"

### Life Events

Users experiencing major life changes.

**Available Events:**
- Graduating college
- Getting married
- Moving
- Starting a business
- Having a baby
- Retiring

**Best For:**
- Products tied to life transitions
- One-time purchase items
- Major decisions

### Detailed Demographics

Target by:
- Parental status
- Marital status
- Education level
- Homeownership status
- Employment status

---

## Signal Strategy

### Layering Signals

Combine signal types for better results:

```
Campaign Signal Stack:
├── Custom Segment: Search terms (buyer intent keywords)
├── Custom Segment: Competitor URLs
├── First-Party: Website remarketing
├── First-Party: Customer match (if available)
├── In-Market: [Relevant category]
└── Affinity: [Supporting interest]
```

### Signal Strength Hierarchy

Most valuable to least:
1. **First-party data** - Your actual customers
2. **Custom search segments** - High intent
3. **Website remarketing** - Engaged users
4. **In-market audiences** - Active researchers
5. **Affinity audiences** - Broad interest
6. **Demographics** - Basic filtering

### How Many Signals?

**Recommended:**
- 2-3 custom segments
- 1-2 first-party audiences (if available)
- 2-4 Google audiences

**Avoid:**
- Zero signals (cold start)
- 10+ signals (over-constrained)

---

## Monitoring Audience Performance

### Where to Find Data

In Google Ads:
1. Campaign > Insights
2. Audience Insights tab
3. View top-performing segments

### What to Look For

- Which segments drive conversions
- Cost per conversion by segment
- Conversion rate by audience type
- Audience overlap

### Optimization Actions

**If a segment underperforms:**
- Don't remove immediately
- Check if it's still in learning
- Consider if it drives assisted conversions
- Remove after 30 days of poor performance

**If a segment overperforms:**
- Consider creating similar segments
- Extract keywords/URLs for new segments
- Increase budget if limited

---

## Common Mistakes

1. **No audience signals** - Campaign starts blind
2. **Only demographic signals** - Too broad
3. **Too many signals** - Conflicting data
4. **Ignoring first-party data** - Missing your best signal
5. **Never reviewing performance** - Stale signals
6. **Treating signals as targeting** - Expecting strict audience limits
