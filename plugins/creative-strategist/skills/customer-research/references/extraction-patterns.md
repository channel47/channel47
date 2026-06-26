# Extraction Patterns — Structuring and Selecting Customer Voice Data

## Quote Selection Criteria

Not every customer statement is worth capturing. High-signal quotes share these traits:

### Worth capturing
- **Specific and detailed** — names a product, describes a situation, includes context
- **Emotionally charged** — uses vivid language, tells a story, reveals stakes
- **Reveals a decision** — why they bought, didn't buy, switched, or returned
- **Contains comparison** — positions one solution against another with reasoning
- **Contradicts assumptions** — says something unexpected about the audience or product
- **Uses memorable phrasing** — language a copywriter would want to mirror in ad creative

### Skip these
- **Generic praise/complaints** — "Great product!" "Terrible company." (no specifics)
- **Pure logistics** — "Arrived in 2 days" (unless delivery speed is a key differentiator)
- **Solicited/incentivized reviews** — "I received this product for free in exchange for review"
- **Repetitive** — if 10 people say "fast shipping," capture the best-phrased one, not all 10
- **Manufacturer language** — "Revolutionary formula" is marketing, not customer voice

### Edge cases
- **Short but revealing** — "I've literally tried EVERYTHING" is only 5 words but 🔥3 intensity and reveals a Failed-Solution angle. Capture it.
- **Long rambling reviews** — Extract the core 1-2 sentences. Don't quote the full paragraph.
- **Sarcasm/humor** — Capture if the underlying sentiment is clear. Tag the real emotion.

## Quote Tagging System

Every quote gets three tags:

```
- [SourceTag|🔥Intensity] "[exact quote]" — Source: [URL] | Journey: [Stage]
```

### Source tags
- **[Direct]** — Fetched the page directly and read the quote in full context
- **[Search]** — Quote appeared in a Google search result snippet
- **[Article]** — A fetchable article quoted a customer from another platform
- **[Browser]** — Accessed via browser automation (Playwright, etc.)

### Emotional intensity
- **🔥1** — Factual, calm. Useful as supporting evidence. "It works but takes a while."
- **🔥2** — Clear emotion. Good for body copy. "I was really frustrated with the old one."
- **🔥3** — Visceral, story-driven. Hook material. "I was literally in tears — nothing worked until this."

Calibration: Most quotes will be 🔥1-2. If more than 30% of quotes are tagged 🔥3, recalibrate — true 🔥3 quotes are rare and powerful.

### Journey stage
- **[Pre-aware]** — Describing the problem without knowing solutions exist
- **[Problem-aware]** — Actively searching for solutions
- **[Solution-aware]** — Evaluating specific options
- **[Decision]** — Ready to buy, final hesitations
- **[Post-purchase]** — Has bought, sharing experience

## Per-Source Structure

```markdown
## Source: [URL or platform name]
### Platform: [Trustpilot/Reddit/Amazon/Forum/etc.] | Access: [Direct/Search/Browser/Article] | Signal Priority: [P1/P2/P3]

### Pain Points
- [Direct|🔥3] "[exact quote]" — Journey: Post-purchase | context: [brief note]
- [Direct|🔥2] "[exact quote]" — Journey: Problem-aware | context: [brief note]

### Desired Outcomes
- [Direct|🔥2] "[exact quote]" — Journey: Solution-aware | context: [brief note]

### Objections / Hesitations
- [Search|🔥2] "[exact quote]" — Journey: Decision | context: [brief note]

### Trigger Events
- [Direct|🔥3] "[description of what made them buy/search]" — Journey: [stage]

### Competitor Positioning
- [Direct|🔥2] [Brand A] vs [Brand B]: "[quote showing how they compare]"
  - Trade-off: [what they gain vs. lose by choosing one over the other]

### Demographic Signals
- Age indicators, gender indicators, life situation clues — with source quotes
```

## Synthesis Structure

```markdown
---
product: "[product-slug]"
stage: research
generated: "[YYYY-MM-DD]"
quotes: [total count]
sources: [platform count]
p1_coverage: "[N]/3 thorough"
fire3_count: [count]
journey_stages: [list of stages with quotes]
---

# [Product] — Customer Research Synthesis

## Research Coverage
- **Sources accessed**: [count] across [count] platform types
- **Total quotes captured**: [count]
- **Signal distribution**: [X] P1 | [Y] P2 | [Z] P3
- **Intensity distribution**: [X] 🔥3 | [Y] 🔥2 | [Z] 🔥1

## Journey Stage Distribution
| Stage | % of Quotes | Notes |
|-------|-------------|-------|
| Pre-aware | X% | [gap note if underrepresented] |
| Problem-aware | X% | |
| Solution-aware | X% | |
| Decision | X% | [gap note if underrepresented] |
| Post-purchase | X% | |

## Top Pain Points (ranked by frequency x intensity)
1. **[Pain point]** — frequency: [X mentions] | avg intensity: 🔥[X] | journey stages: [stages]
   - "[highest-intensity quote]" — [source]
   - "[second quote]" — [source]
   - **Why this matters for creative**: [1 sentence on how this translates to ad angles]

2. [continue ranking...]

## Language Clusters

### Frustration Language
Phrases expressing anger, exhaustion, giving up:
- "[phrase]" (X occurrences)
- "[phrase]" (X occurrences)

### Hope Language
Phrases expressing desire, aspiration, possibility:
- "[phrase]" (X occurrences)

### Skepticism Language
Phrases expressing doubt, distrust, "too good to be true":
- "[phrase]" (X occurrences)

### Urgency Language
Phrases expressing time pressure, desperation, breaking points:
- "[phrase]" (X occurrences)

### Relief Language
Phrases from satisfied customers expressing "finally found it":
- "[phrase]" (X occurrences)

## Objection Map
| Objection | Frequency | Avg Intensity | Journey Stage | Best Quote |
|-----------|-----------|---------------|---------------|------------|
| [objection] | [count] | 🔥[X] | [stage] | "[quote]" |

## Desire Map
| Stated Desire | Deeper Desire | Evidence |
|---------------|---------------|----------|
| "I want [surface thing]" | [underlying emotional need] | "[quote that reveals the gap]" |

## Trigger Events (ranked)
1. **[Event]** — frequency: [X] | journey shift: [from stage] → [to stage]
   - "[example quote]"

## Competitive Positioning Map
| Competitor | Perceived Strengths | Perceived Weaknesses | What Customers Wish It Had | Trade-off vs. Our Product |
|------------|-------------------|---------------------|---------------------------|--------------------------|
| [brand] | [from quotes] | [from quotes] | [from quotes] | [synthesis] |

## Demographic Clusters
- **[Cluster name]**: [description] — supporting signals: [quote snippets]

## Surprising Findings
1. **[Finding]** — [why it's surprising and what it implies for creative strategy]
2. **[Finding]** — [why it's surprising]
3. **[Finding]** — [why it's surprising]

## Data Gaps
- [Category/stage with insufficient data] — [why, and what it means for downstream skills]

## Source Coverage Log
| Platform | Access Method | Status | Quotes Extracted |
|----------|--------------|--------|-----------------|
| [platform] | [Direct/Browser/Search] | [Success/Partial/Failed] | [count] |
```
