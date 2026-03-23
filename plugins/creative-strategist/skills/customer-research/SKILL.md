---
name: customer-research
description: This skill should be used when the user asks to "research a product", "find customer voice data", "pull reviews", "what are customers saying about", "research customer pain points", "find real customer language", "VOC research", "voice of customer", "market research for", "find complaints about", "what do people hate about", "pull Reddit data", "pull Amazon reviews", or mentions gathering real customer data from public sources like Reddit, Amazon, Trustpilot, forums, or review sites. This is the foundational research skill — always start here before building personas or angles.
---

# Customer Research — Voice of Customer Data Extraction

Fetch real customer language, pain points, desires, objections, and demographic signals from publicly available sources. The output is structured raw research that feeds into persona building and angle generation.

## Product Context

Before starting, check for a product config file at `.claude/creative-strategist.local.md` in the project root. If it exists, read it — it contains product details, competitors, target audience, and positioning that should guide your research. If it doesn't exist, gather the basics from the user:

- **Product/category** (e.g., "ultrasonic dog training device", "toilet cleaning tablets")
- **Known competitors** (brand names for review searches)
- **Target audience hypothesis** (if any — research may challenge it)
- **Specific questions** (e.g., "what makes people finally buy?", "what do they try first?")

## Platform Access Realities

Some platforms block automated access. Read `references/source-strategies.md` for the full breakdown, but the short version:

- **Reddit, Amazon, Quora, Walmart** — block direct scraping. Use browser automation tools (Playwright, Browserbase) or Google search with `site:` operators to access content.
- **Trustpilot, ConsumerAffairs, SiteJabber, niche forums** — generally accessible via direct fetch.
- **Review aggregation articles** (Wirecutter, BuzzFeed, Tom's Guide) — fetchable and often quote Reddit/Amazon verbatim.

Use whatever tools get results. The goal is real customer quotes, not adherence to a specific tool chain.

## Research Process

### 1. Discover sources

Identify where customers talk about this product or category. Google search with `site:` operators is the fastest way to find relevant threads, reviews, and discussions across platforms.

### 2. Extract customer voice

Hit at least 3-4 distinct source types. Prioritize:
- **Review sites** (Trustpilot, ConsumerAffairs) — direct, structured customer feedback
- **Reddit** — unfiltered discussion, emotional language, comparison threads
- **Amazon** — high-volume review data, star distribution patterns
- **Niche forums** — detailed stories from engaged communities
- **Complaint sites** (BBB, SiteJabber) — objections, fears, deal-breakers

For blocked sites, use browser automation or search engine snippets. Don't waste time retrying failed approaches — move to the next source.

### 3. Tag every quote

Every customer quote must include a source quality tag:

```
- [Direct] "[exact quote]" — Source: [URL]
- [Search] "[exact quote]" — Source: [platform via search snippet]
- [Article] "[exact quote]" — Source: [article URL that quoted the customer]
```

### 4. Structure the data

Organize by source, then categorize within each source:
- **Pain Points** — what hurts, what frustrates, what they complain about
- **Desired Outcomes** — what they want (stated and deeper)
- **Objections / Hesitations** — what stops them from buying
- **Emotional Language** — exact phrases and sentiment
- **Trigger Events** — what made them start searching
- **Competitor Mentions** — how they perceive alternatives
- **Demographic Signals** — age, gender, life situation clues

### 5. Synthesize across sources

Create a top-level synthesis:
1. **Top Pain Points** (ranked by frequency, with example quotes)
2. **Customer Language Patterns** (recurring phrases to mirror in creative)
3. **Objection Map** (what stops them, what they've tried before)
4. **Desire Map** (stated desire vs. deeper emotional desire)
5. **Trigger Events** (moments that push passive to active)
6. **Demographic Clusters** (if patterns emerge)
7. **Competitor Landscape** (how customers perceive alternatives)

### 6. Save output

Save as `[product-slug]-research.md` in the workspace. This file is the input for persona-builder and angle-generator.

## Quality Standards

- Data from at least 3 distinct source types
- At least 30 distinct customer quotes with source tags
- Real customer language — never paraphrase into marketing-speak
- Both positive AND negative sentiment
- Note which sources were directly accessed vs. via search vs. inaccessible
- Do not fabricate quotes, pad with blog content, or include manufacturer marketing language

## Reference Files

- **`references/source-strategies.md`** — Platform access realities, what works, what's blocked, workaround approaches
- **`references/extraction-patterns.md`** — Templates for structuring extracted data
