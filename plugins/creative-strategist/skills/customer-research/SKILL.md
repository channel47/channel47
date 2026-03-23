---
name: customer-research
description: This skill should be used when the user asks to "research a product", "find customer voice data", "pull reviews", "what are customers saying about", "research customer pain points", "find real customer language", "VOC research", "voice of customer", "market research for", "find complaints about", "what do people hate about", "pull Reddit data", "pull Amazon reviews", or mentions gathering real customer data from public sources like Reddit, Amazon, Trustpilot, forums, or review sites. This is the foundational research skill — always start here before building personas or angles.
---

# Customer Research — Voice of Customer Data Extraction

Extract real customer language, pain points, desires, objections, and behavioral signals from publicly available sources. Output is structured, scored research that feeds directly into persona building and angle generation.

## Product Context

Before starting, check for `.claude/creative-strategist.local.md` in the project root. If it exists, read it for product details, competitors, target audience, and positioning. If it doesn't exist, gather from the user:

- **Product/category** (e.g., "ultrasonic dog training device", "toilet cleaning tablets")
- **Known competitors** (brand names for review searches)
- **Target audience hypothesis** (if any — research may challenge it)
- **Specific questions** (e.g., "what makes people finally buy?", "what do they try first?")

## Platform Access

Read `references/source-strategies.md` for full platform breakdown. Short version:

- **Direct access works**: Trustpilot, ConsumerAffairs, SiteJabber, BBB, niche forums, review articles
- **Blocked — needs browser automation or search**: Reddit, Amazon, Quora, Walmart
- **Indirect only**: YouTube comments, Facebook groups (use articles that quote them)

Use whatever tools get results. **Never abandon a source after a single tool failure** — exhaust the fallback chain in `references/source-strategies.md` before moving on.

## Research Process

### 1. Discover sources

Use Google search with `site:` operators to find relevant threads, reviews, and discussions across platforms. Cast wide initially, then focus on the richest sources.

### 2. Extract with signal priority

Not all sources carry equal weight. Prioritize extraction effort by signal quality:

| Priority | Source Type | Why | Effort |
|----------|-----------|-----|--------|
| **P1 — Gold** | Direct reviews (Trustpilot, Amazon, ConsumerAffairs) | Unprompted, purchase-verified, emotional | Extract thoroughly |
| **P1 — Gold** | Reddit discussion threads | Unfiltered, comparative, high context | Extract thoroughly |
| **P2 — Silver** | Niche forums, complaint sites (BBB) | Detailed stories, engaged community | Extract selectively |
| **P2 — Silver** | Q&A platforms (Quora, niche Q&A) | Reveals objections and decision criteria | Extract selectively |
| **P3 — Bronze** | Review aggregation articles (Wirecutter, etc.) | Curated quotes, often from P1 sources | Extract only unique quotes |
| **P3 — Bronze** | Search snippets from blocked platforms | Partial, decontextualized | Use to supplement, not replace |

Hit at least 3 distinct source types, including at least one P1 source.

### 3. Tag every quote with source and intensity

Every customer quote gets two tags — source quality AND emotional intensity:

```
- [Direct|🔥3] "[exact quote]" — Source: [URL]
- [Search|🔥1] "[exact quote]" — Source: [platform via search snippet]
- [Article|🔥2] "[exact quote]" — Source: [article URL]
- [Browser|🔥3] "[exact quote]" — Source: [URL via browser automation]
```

**Source tags:** `[Direct]`, `[Search]`, `[Article]`, `[Browser]`

**Emotional intensity (🔥1-3):**
- 🔥1 — Factual, calm observation. "It works okay but delivery was slow."
- 🔥2 — Clear emotional charge. "I was so frustrated I almost returned it."
- 🔥3 — Visceral, story-driven, high stakes. "I literally cried when this finally worked after months of trying everything."

Creative teams mine 🔥3 quotes for hooks. 🔥1 quotes provide supporting evidence. Tag honestly — inflating intensity degrades downstream output.

### 4. Map quotes to the buying journey

Tag each quote's position in the purchase journey. This is critical for downstream angle generation — different angles target different journey stages.

- **[Pre-aware]** — Doesn't know the product category exists. Describes the problem without naming solutions.
- **[Problem-aware]** — Knows they have a problem, actively searching. "How do I get rid of hard water stains?"
- **[Solution-aware]** — Knows solutions exist, evaluating options. "Is [product] better than [competitor]?"
- **[Decision]** — Ready to buy, needs final push. "Is it worth the price?" "Anyone have a discount code?"
- **[Post-purchase]** — Has bought, sharing experience. Reviews, complaints, recommendations.

Most quotes will be Solution-aware or Post-purchase. Pre-aware and Decision quotes are rarer but extremely valuable — flag them prominently.

### 5. Structure the data by source

Read `references/extraction-patterns.md` for the full template. Organize by source, then categorize within each:

- **Pain Points** — what hurts, what frustrates
- **Desired Outcomes** — what they want (stated and deeper)
- **Objections / Hesitations** — what stops them from buying
- **Emotional Language** — exact phrases with sentiment
- **Trigger Events** — what pushed them from passive to active
- **Competitor Positioning** — how they compare alternatives (not just mentions — capture trade-offs, what's better/worse, what they wish existed)
- **Demographic Signals** — age, gender, life situation clues

### 6. Synthesize across sources

This is where research becomes strategy. The synthesis is NOT a summary — it's analysis. Follow this structure:

#### Top Pain Points (ranked by frequency AND intensity)
Rank by combined frequency + emotional intensity, not just count. A pain point mentioned 3 times at 🔥3 outranks one mentioned 8 times at 🔥1.

#### Language Clusters
Group recurring phrases into thematic clusters that copywriters can directly pull from:
- **Frustration language** — phrases expressing anger, exhaustion, being fed up
- **Hope language** — phrases expressing desire, aspiration, what-if
- **Skepticism language** — phrases expressing doubt, distrust, "is this legit"
- **Urgency language** — phrases expressing time pressure, desperation, breaking points
- **Relief language** — phrases from satisfied customers expressing "finally"

Each cluster: 5-8 exact phrases with usage frequency.

#### Objection Map
| Objection | Frequency | Intensity | Journey Stage | Example Quote |
|-----------|-----------|-----------|---------------|---------------|

#### Desire Map
| Stated Desire | Deeper Desire | Evidence |
|---------------|---------------|----------|
| "I want X" | They really mean Y | "[quote that reveals the deeper desire]" |

#### Trigger Events (ranked by frequency)
What pushed people from passive awareness to active searching. Tag each with journey stage.

#### Competitive Positioning Map
Not just mentions — synthesize how customers position alternatives:
| Competitor | Perceived Strengths | Perceived Weaknesses | What Customers Wish It Had | Trade-off vs. Our Product |
|------------|-------------------|---------------------|---------------------------|--------------------------|

#### Demographic Clusters
With supporting signals from the data.

#### Surprising Findings
3-5 non-obvious insights that emerged from the research. Things that contradict assumptions, unexpected patterns, or underrepresented perspectives. Examples:
- "Expected audience is women 25-40 but research shows 40% of reviewers are men buying for themselves"
- "The #1 objection isn't price — it's 'I've been burned before by similar products'"
- "Post-purchase customers report an unexpected benefit the brand doesn't advertise"

This section is mandatory. If nothing is surprising, the research isn't deep enough.

#### Journey Stage Distribution
Estimate what % of extracted quotes fall into each journey stage. Note which stages are underrepresented — this signals gaps for downstream skills.

### 7. Save output

Save as `[product-slug]-research.md` in the workspace. This file is the input for persona-builder and angle-generator.

## Quality Standards

### Volume with balance
- At least 40 distinct customer quotes with source and intensity tags
- Distribution target across categories (not hard limits, but check):
  - Pain Points: 8-12 quotes
  - Desired Outcomes: 6-10 quotes
  - Objections: 6-10 quotes
  - Trigger Events: 4-6 quotes
  - Competitor Positioning: 4-8 quotes
  - Emotional Language: woven throughout, not a separate dump
- If any category has fewer than 3 quotes, note the gap and explain why (is it a data gap or a genuine absence?)

### Signal quality
- At least one P1 source extracted thoroughly
- Data from at least 3 distinct source types
- Every quote tagged with source type, emotional intensity, and journey stage
- Real customer language — never paraphrase into marketing-speak
- Both positive AND negative sentiment

### Synthesis quality
- Surprising Findings section populated with genuine insights
- Language Clusters with 5+ phrases per cluster
- Competitive Positioning Map with trade-offs, not just mention counts
- Journey Stage Distribution estimated

### What to exclude
- Quotes that say nothing specific ("Great product!" "Would recommend." "5 stars.")
- Manufacturer marketing language or PR quotes
- Blog author opinions (unless quoting a customer)
- Duplicate quotes from the same person across platforms

## Reference Files

- **`references/source-strategies.md`** — Platform access realities, what works, what's blocked, workaround approaches
- **`references/extraction-patterns.md`** — Templates for structuring extracted data, quote selection criteria, and judgment heuristics for what's worth capturing
