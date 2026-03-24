---
name: customer-research
description: This skill should be used when the user asks to "research a product", "find customer voice data", "pull reviews", "what are customers saying about", "research customer pain points", "find real customer language", "VOC research", "voice of customer", "market research for", "find complaints about", "what do people hate about", "pull Reddit data", "pull Amazon reviews", or mentions gathering real customer data from public sources like Reddit, Amazon, Trustpilot, forums, or review sites. This is the foundational research skill — always start here before building personas or angles.
allowed-tools: ["Read", "Write", "Glob", "WebFetch", "WebSearch", "Agent"]
---

# Customer Research — Voice of Customer Data Extraction

Extract real customer language from publicly available sources. Output structured, scored research that feeds directly into persona-builder and angle-generator.

## Orchestration

1. Check `.claude/creative-strategist.local.md` for product context. If it exists, use the product name, competitors, and target audience to guide research.

2. Determine the research target from the user's request or the config file. If neither provides a clear target, ask:
   - What product or category to research
   - Any known competitors (brand names help find reviews)
   - Any specific questions they want answered

3. **Launch the research-crawler agent** to autonomously fetch data from multiple platforms. Pass the research target and any context from the config file. The agent handles source discovery, fallback chains for blocked platforms, and quote extraction.

4. When the agent returns, verify output quality:
   - **P1 coverage**: All three P1 source types attempted. At least 2 of 3 must show thorough extraction (8+ quotes). If fewer than 2 are thorough, send the agent back with different URLs and fallback tools.
   - At least 50 quotes with triple-tagging (source + intensity + journey stage)
   - At least 3 distinct source types
   - Language clusters populated (frustration, hope, skepticism, urgency, relief)
   - Surprising findings section present with 3+ insights
   - Source coverage log present

5. Save output as `[product-slug]-research.md` in the workspace.

6. Present a summary:
   - Sources accessed and methods used
   - Total quotes with intensity distribution (X fire-3, Y fire-2, Z fire-1)
   - Top 3 pain points (with example quotes)
   - Top 3 surprising findings
   - Any data gaps or underrepresented journey stages
   - Suggest running persona-builder next

## Intent

Creative teams need real customer language — not marketing-speak, not paraphrased summaries, but the exact words people use when they're frustrated, hopeful, skeptical, or relieved. This research becomes the foundation for everything downstream: personas that reflect real behavior, angles that resonate because they use the audience's own language, and hook copy that stops scrolling because it sounds like an internal monologue.

## Platform Access

Read `references/source-strategies.md` for the full platform breakdown. Short version:

- **Direct access works**: Trustpilot, ConsumerAffairs, SiteJabber, BBB, niche forums, review articles
- **Blocked — needs browser automation or search**: Reddit, Amazon, Quora, Walmart
- **Indirect only**: YouTube comments, Facebook groups (use articles that quote them)

Never abandon a source after a single tool failure — exhaust the fallback chain in `references/source-strategies.md` before moving on.

## Research Process

### 1. Discover sources

Search broadly with `site:` operators to find relevant threads, reviews, and discussions. Cast wide initially, then focus on the richest sources.

### 2. Extract with signal priority

| Priority | Source Type | Why | Effort |
|----------|-----------|-----|--------|
| **P1 — Gold** | Direct reviews (Trustpilot, Amazon, ConsumerAffairs) | Unprompted, purchase-verified, emotional | Extract thoroughly |
| **P1 — Gold** | Reddit discussion threads | Unfiltered, comparative, high context | Extract thoroughly |
| **P2 — Silver** | Niche forums, complaint sites (BBB) | Detailed stories, engaged community | Extract selectively |
| **P2 — Silver** | Q&A platforms (Quora, niche Q&A) | Reveals objections and decision criteria | Extract selectively |
| **P3 — Bronze** | Review aggregation articles (Wirecutter, etc.) | Curated quotes, often from P1 sources | Extract only unique quotes |
| **P3 — Bronze** | Search snippets from blocked platforms | Partial, decontextualized | Use to supplement, not replace |

**All three P1 source types are mandatory to attempt with persistent retry.** (1) A review site like Trustpilot/ConsumerAffairs, (2) Reddit, and (3) Amazon. At least 2 of the 3 must reach thorough extraction (8+ quotes each). Target all 3. Also hit at least one P2 or P3 source.

### 3. Tag every quote

Every customer quote gets three tags — source quality, emotional intensity, and journey stage:

```
- [Direct|fire-3] "[exact quote]" — Source: [URL] | Journey: [Stage]
- [Search|fire-1] "[exact quote]" — Source: [platform via search snippet] | Journey: [Stage]
- [Article|fire-2] "[exact quote]" — Source: [article URL] | Journey: [Stage]
- [Browser|fire-3] "[exact quote]" — Source: [URL via browser automation] | Journey: [Stage]
```

**Source tags:** `[Direct]`, `[Search]`, `[Article]`, `[Browser]`

**Emotional intensity (fire 1-3):**
- fire-1 — Factual, calm observation. "It works okay but delivery was slow."
- fire-2 — Clear emotional charge. "I was so frustrated I almost returned it."
- fire-3 — Visceral, story-driven, high stakes. "I literally cried when this finally worked after months of trying everything."

Creative teams mine fire-3 quotes for hooks. fire-1 quotes provide supporting evidence. Tag honestly — inflating intensity degrades downstream output.

### 4. Map quotes to the buying journey

- **[Pre-aware]** — Doesn't know the product category exists. Describes the problem without naming solutions.
- **[Problem-aware]** — Knows they have a problem, actively searching.
- **[Solution-aware]** — Knows solutions exist, evaluating options.
- **[Decision]** — Ready to buy, needs final push.
- **[Post-purchase]** — Has bought, sharing experience.

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

This is where research becomes strategy. The synthesis is analysis, not summary.

#### Top Pain Points (ranked by frequency AND intensity)
Rank by combined frequency + emotional intensity, not just count. A pain point mentioned 3 times at fire-3 outranks one mentioned 8 times at fire-1.

#### Language Clusters
Group recurring phrases into thematic clusters copywriters can directly pull from:
- **Frustration language** — anger, exhaustion, being fed up
- **Hope language** — desire, aspiration, what-if
- **Skepticism language** — doubt, distrust, "is this legit"
- **Urgency language** — time pressure, desperation, breaking points
- **Relief language** — satisfied customers expressing "finally"

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
3-5 non-obvious insights that emerged from the research. Things that contradict assumptions, unexpected patterns, or underrepresented perspectives. This section is mandatory. If nothing is surprising, the research isn't deep enough.

#### Journey Stage Distribution
Estimate what % of extracted quotes fall into each journey stage. Note underrepresented stages — this signals gaps for downstream skills.

### 7. Save output

Save as `[product-slug]-research.md` in the workspace. This file is the input for persona-builder and angle-generator.

## Quality Standards

### Volume with balance
- At least 50 distinct customer quotes with source and intensity tags
- Distribution target across categories (not hard limits, but check):
  - Pain Points: 10-15 quotes
  - Desired Outcomes: 8-12 quotes
  - Objections: 8-12 quotes
  - Trigger Events: 5-8 quotes
  - Competitor Positioning: 5-10 quotes
  - Emotional Language: woven throughout, not a separate dump
- If any category has fewer than 3 quotes, note the gap and explain why

### Signal quality
- **All three P1 source types attempted with persistent retry** — at least 2 of 3 must reach thorough extraction (8+ quotes each), target all 3
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
