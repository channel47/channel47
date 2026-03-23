---
name: customer-research
description: This skill should be used when the user asks to "research a product", "find customer voice data", "pull reviews", "what are customers saying about", "research customer pain points", "find real customer language", "VOC research", "voice of customer", "customer research for", "pull Reddit data", "pull Amazon reviews", "market research for", "find complaints about", "what do people hate about", "DTC research", or mentions gathering real customer data from public sources like Reddit, Amazon, Trustpilot, forums, or review sites. Use this skill even when the user just names a product category and wants to understand the customer landscape. This is the foundational research skill — always start here before building personas, angles, scripts, or copy.
---

# Customer Research — Voice of Customer Data Extraction

This skill fetches real customer language, pain points, desires, objections, and demographic signals from publicly available sources. The output is structured raw research that feeds directly into persona building, angle generation, and ad creative.

## Why This Matters

DTC advertising lives or dies on **resonance**. The difference between a 1.5x and 4x ROAS ad is almost always rooted in how precisely the copy mirrors the customer's internal monologue. This skill exists to replace guesswork with real data — actual words customers use, actual frustrations they describe, actual outcomes they want.

## CRITICAL: What Works and What Doesn't

Before fetching anything, read `references/source-strategies.md`. It contains verified, tested URL patterns. The short version:

**Reddit and Amazon are BLOCKED by WebFetch.** Do not waste time trying to fetch from reddit.com, old.reddit.com, or amazon.com directly — they will fail. Instead, use WebSearch with carefully crafted queries that include emotional customer language to surface quotes in search result snippets.

**Trustpilot WORKS with WebFetch.** Always fetch Trustpilot directly — it's the single most reliable source of real, verbatim customer quotes.

**Niche forums are hit-or-miss.** Some work (older forum software like vBulletin, phpBB), some don't (modern JS frameworks). Try each one and move on quickly if it fails.

**Review aggregation articles are fetchable and quote-rich.** Articles from Wirecutter, BuzzFeed, Dogster, Tom's Guide, etc. often include verbatim customer quotes from Reddit and Amazon. These are your backdoor to blocked platforms.

## Research Process

### Step 1: Define the Research Target

Gather from the user:
- **Product/category** (e.g., "ultrasonic dog training device", "toilet cleaning tablets")
- **Known competitors** (brand names to search for Trustpilot reviews)
- **Target audience hypothesis** (if any — the research may challenge it)
- **Specific questions** (e.g., "what makes people finally buy?", "what do they try first?")

If the user gives just a product name, infer reasonable search terms and competitor names. Confirm with the user before fetching.

### Step 2: Fetch Data — Follow This Exact Sequence

The order matters. Start with what's most reliable and work outward.

#### Round 1: Trustpilot (Direct Fetch — Do This First)

Identify 2-4 competitor or brand domains, then fetch each one:
```
WebFetch: https://www.trustpilot.com/review/[brand-domain.com]
```

This returns star ratings, review counts, and exact customer quotes. Extract everything — this is your foundation.

If you don't know the brand domains, use WebSearch first: `trustpilot [product category]` or `trustpilot [brand name]`.

#### Round 2: WebSearch for Reddit Customer Language

Reddit is the richest source of unfiltered customer voice, but you can only access it through search snippets. Run 3-4 searches, each targeting a different emotional angle:

**Pain-focused:** `reddit [product category] "doesn't work" OR "waste of money" OR "I've tried everything"`
**Praise-focused:** `reddit [product] "game changer" OR "finally found" OR "changed my life"`
**Comparison-focused:** `reddit best [product category] OR "[product] vs" recommendation`
**Objection-focused:** `reddit [product category] "is it worth" OR "should I buy" OR "skeptical"`

Also search for articles that aggregate Reddit content:
`"reddit recommends" [product category]` or `"redditors say" [product]`
These articles are fetchable via WebFetch and often quote Reddit posts verbatim.

#### Round 3: WebSearch for Amazon Review Language

Same strategy as Reddit — surface review language through search snippets:

`amazon reviews [product] "I bought" OR "doesn't work" OR "game changer" OR "waste of money"`
`amazon [product category] review "finally found" OR "I've tried everything"`
`best [product category] amazon review 2025 OR 2026`

Also search for articles that reference Amazon reviews:
`[product] review site:wirecutter.com OR site:nytimes.com OR site:tomsguide.com`
Fetch these articles — they often include verbatim Amazon review quotes.

#### Round 4: Niche Forums (Direct Fetch — Test Each One)

Use WebSearch to find forums: `[product category] forum discussion`

Then try fetching the top 3-4 forum URLs directly with WebFetch. If a forum returns actual content (posts, quotes, user discussions), extract everything. If it returns JavaScript/empty content, skip it immediately — don't retry.

Good forum categories by vertical:
- Pet products → breed-specific forums, DogForum.com
- Cleaning → CleaningTalk.com (hit-or-miss)
- Hearing aids → HearingTracker.com
- Health → patient forums, condition-specific communities
- Home → HomesteadingToday.com, HomeImprovement forums

#### Round 5: Complaint Sites (Direct Fetch)

Try fetching these directly — they often work:
- `https://www.consumeraffairs.com/[search for product/brand]`
- BBB complaint pages
- `https://www.sitejabber.com/reviews/[domain]`

These skew negative, which is valuable for finding objections and fears.

#### Round 6: Supplementary WebSearch

Fill gaps with targeted searches:
- `[product] complaints OR problems OR issues`
- `[competitor] vs [competitor] comparison`
- `why I stopped using [product]` — defection stories
- `[product category] "I wish" OR "if only"` — unmet needs

### Step 3: Extract and Structure the Data

Every single customer quote must include a source quality tag. This is non-negotiable because downstream skills (persona-builder, angle-generator) weight direct quotes more heavily than search snippets.

Use this exact format for every quote — the tag is part of the quote line itself:

```
- [Direct] "[exact quote]" — Source: [URL]
- [Search] "[exact quote]" — Source: [platform name via WebSearch]
- [Article] "[exact quote]" — Source: [article URL that quoted the customer]
```

The three tags:
- **[Direct]** = you fetched the page and read the quote yourself (Trustpilot, forums, etc.)
- **[Search]** = quote appeared in a WebSearch result snippet (Reddit, Amazon, etc.)
- **[Article]** = a fetchable article (Wirecutter, BuzzFeed, etc.) quoted a customer from another platform

Organize extracted data by source, then by category within each source:

```
## Source: [URL]
### Platform: [Trustpilot/Reddit/Amazon/Forum/etc.] | Access: [Direct fetch / WebSearch / Via article]

### Pain Points
- [Direct] "[exact quote]" — context: [brief note]
- [Search] "[exact quote]" — context: [brief note]

### Desired Outcomes
- [Direct] "[exact quote]" — context: [brief note]

### Objections / Hesitations
- [Article] "[exact quote]" — context: [brief note]

### Emotional Language
- [Direct] "[exact phrase]" — sentiment: [frustration/hope/anger/relief/etc.]

### Trigger Events
- [Search] "[description of what made them buy/search]"

### Competitor Mentions
- [Direct] [Brand]: [positive/negative] — "[brief quote]"

### Demographic Signals
- Age indicators, gender indicators, life situation clues
```

Every quote line starts with its tag. No exceptions. If you're unsure which tag to use, default to [Search].

### Step 4: Synthesize Across Sources

After collecting from multiple sources, create a synthesis document:

1. **Top Pain Points** (ranked by frequency across sources, with example quotes)
2. **Customer Language Patterns** (recurring phrases, metaphors, emotional vocabulary — the exact words to mirror in ads)
3. **Objection Map** (what stops people from buying, what they've tried before, what they're skeptical about)
4. **Desire Map** (stated desire vs. deeper emotional desire — they say "I want my dog to stop barking" but mean "I want to stop feeling like a bad pet owner")
5. **Trigger Events** (life moments that push someone from "I should..." to "I need to buy now")
6. **Demographic Clusters** (if patterns emerge — e.g., "mostly women 35-55 buying for aging parents")
7. **Competitor Landscape** (how customers perceive alternatives, what they've already tried)

### Step 5: Save Research Output

Save the structured research to the workspace as `[product-slug]-research.md`. This file becomes the input for the persona-builder, angle-generator, script-writer, and copy-writer skills.

## Quality Standards

- **Source variety**: Data from at least 3 distinct source types (e.g., Trustpilot + Reddit snippets + forum). If you only hit 1-2 types, note the gap.
- **Real customer language**: At least 30 distinct customer quotes. Paraphrasing defeats the purpose — the whole point is their exact words.
- **Balance**: Include both positive AND negative sentiment. The best ad angles often come from 5-star reviews ("this changed my life") paired with 1-star objections ("I was skeptical but...").
- **Attribution**: Every data point has a source URL so it can be verified.
- **Transparency**: Note which sources were directly fetched vs. accessed via search snippets vs. inaccessible.

## What NOT To Do

- Do not fabricate or embellish customer quotes — ever
- Do not pad with blog content, expert opinions, or marketing copy and call it "customer voice data." Blogs are not customers. Only extract quotes that are clearly from real people who used or considered the product.
- Do not rely on a single source type — cross-platform coverage matters
- Do not spend more than 60 seconds retrying a blocked source — move on
- Do not skip the synthesis step — raw data without structure is unusable
- Do not include manufacturer marketing language as "customer language"

## Additional Resources

### Reference Files (READ BEFORE FETCHING)
- **`references/source-strategies.md`** — Tested URL patterns, what works vs. what's blocked, platform-specific strategies. READ THIS FIRST.
- **`references/extraction-patterns.md`** — Templates and patterns for structuring extracted data

### Scripts
- **`scripts/research_template.py`** — Generates a blank research template markdown file
