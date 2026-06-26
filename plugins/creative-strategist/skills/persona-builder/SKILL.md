---
name: persona-builder
description: This skill should be used when the user asks to "build personas", "create customer avatars", "who is the target customer", "customer persona", "buyer persona", "demographic profile", "psychographic profile", "who buys this product", "target audience profile", or mentions building, creating, or refining customer personas from research data. Trigger after customer-research has been run, or when the user provides their own research data.
---

# Persona Builder — Data-Driven Customer Avatars for Creative Teams

Transform raw customer research into vivid, actionable buyer personas. Each persona is a creative targeting tool — not a demographic spreadsheet. Every persona ends with a mini creative brief that angle-generator can directly consume.

## Orchestration

1. Search the workspace for a research file (`*-research.md`). If multiple exist, ask which product to build personas for. If none exist, tell the user: "No research file found. Run customer-research first to fetch customer voice data." and stop.

2. Read the research file's YAML frontmatter for a quick validation pass — check `stage: research`, `quotes` count (≥50), `p1_coverage`, and `fire3_count`. Then validate the body has the data needed:
   - Quotes with intensity scores (needed for pain point ranking)
   - Journey stage tags (needed for journey entry point clustering)
   - Language clusters (needed for language fingerprint per persona)
   - Competitive positioning data (needed for competitive relationship section)
   - If any are missing, warn the user the research may need to be re-run.

3. Check `.claude/creative-strategist.local.md` for product context.

4. Build personas following the construction process below.

5. Save output as `[product-slug]-personas.md` in the workspace.

6. Present a summary:
   - Persona names and one-line core tensions
   - Anti-persona name and why they'll never convert
   - The highest-weight differentiating dimension across personas
   - Suggest running angle-generator next

## Inputs

### Upstream data to consume

The customer-research output includes data that must be explicitly ingested:
- **Emotional intensity scores (fire 1-3)** — identify which pain points hit hardest per persona
- **Journey stage tags** — determine where each persona enters the funnel
- **Language clusters** (frustration, hope, skepticism, urgency, relief) — assign relevant clusters to each persona
- **Competitive positioning map** — determine each persona's relationship with alternatives
- **Surprising findings** — check if any findings challenge initial persona hypotheses

## Persona Construction

### 1. Cluster by behavior, not demographics

Demographics describe people. Behavior predicts response to ads. Cluster on these behavioral axes:

**Primary clustering axes (use at least 2):**
- **Journey entry point** — Where do they enter the funnel? Pre-aware people who stumbled on the problem need different creative than solution-aware comparison shoppers.
- **Prior solution history** — Naive first-timers vs. jaded veterans who've "tried everything." This single axis often creates the sharpest persona splits.
- **Conviction pattern** — What type of evidence converts them? Some need social proof. Some need data. Some need risk-reversal. Some need authority.

**Secondary axes (use to sharpen if clusters overlap):**
- **Pain intensity** — casual annoyance vs. desperate urgency
- **Purchase motivation** — buying for self vs. someone else vs. professional use
- **Price relationship** — price-sensitive bargain hunters vs. "just tell me the best one" premium buyers

**Method:**
1. Sort all 🔥3 quotes from the research into piles by behavioral similarity
2. Check if the piles align with journey stage clusters from the research
3. Merge piles that would respond to the same ad creative
4. Split piles where the same ad would fail for part of the group
5. Validate: if two personas would respond identically to the same hook, proof, and CTA — they're the same persona

Aim for 2-4 distinct personas. More than 4 usually means overlap. Fewer than 2 means the research wasn't deep enough.

### 2. Build each persona

Read `references/persona-framework.md` for calibration examples. For each persona:

```markdown
# Persona: [Name]

## Naming Principles
The name should encode the core tension or defining behavior — not just demographics.
- Good: "The Burned Buyer" (encodes prior failure), "The Secret Sufferer" (encodes hidden pain), "The Reluctant Upgrader" (encodes resistance)
- Bad: "Young Professional Sarah" (just demographics), "The Buyer" (too generic), "Persona A" (meaningless)
The name should be instantly evocative — a creative team should understand the persona's deal from the name alone.

### The Snapshot
- **Age Range**: [from research signals, not assumptions]
- **Gender Skew**: [if data supports it — "mixed" if unclear]
- **Life Situation**: [relevant context from research]
- **Income Signal**: [price-sensitive? premium-seeking? evidence from quotes]
- **Journey Entry Point**: [Pre-aware / Problem-aware / Solution-aware — where they typically enter]
- **Prior Solution History**: [naive / 1-2 attempts / veteran who's tried everything]

### The Decision Journey Monologue
5-8 sentences in first person that trace the FULL decision arc — not just emotions, but the sequence: trigger -> search -> evaluate -> hesitate -> decide (or abandon). Use language directly from research data. This monologue should reveal:
- What pushed them to start looking (trigger)
- How they search and what they find (discovery)
- What they compare and how (evaluation)
- What almost stops them (objection)
- What would tip them over the edge (conversion signal)

### The Trigger Event
- **Primary trigger**: [most common from research, with intensity score]
- **Secondary triggers**: [other situations]
- **Trigger frequency**: [one-time event or recurring frustration?]

### Pain Points (ranked by intensity, not just frequency)
1. [Most intense — use their words, cite intensity score] — Journey stage: [stage]
2. [Second — their words] — Journey stage: [stage]
3. [Third — their words] — Journey stage: [stage]

### Desired Outcome
- **Stated desire**: What they'd say if asked (surface)
- **Deeper desire**: What they really mean (emotional core)
- **Evidence**: [quote that reveals the gap between stated and deeper]

### Objections & Skepticism
1. [Objection in their words] — Intensity: 🔥[X] | What would overcome it: [evidence type]
2. [Objection] — Intensity: 🔥[X] | What would overcome it: [evidence type]

### What They've Already Tried
- [Solution] — Why it failed: [specific reason from research]
- [Solution] — Why it failed: [specific reason]
(Skip this section for naive first-timer personas)

### Competitive Relationship
- **Current alternative**: [what they're using now or considering]
- **What they like about it**: [from competitive positioning map]
- **What they wish were different**: [gap = opportunity]
- **Switching barrier**: [what would need to be true to switch]

### Language Fingerprint
Key phrases this persona actually uses, organized by emotional register:
- **Frustration**: "[phrase]", "[phrase]"
- **Hope**: "[phrase]", "[phrase]"
- **Skepticism**: "[phrase]", "[phrase]"
(Pull directly from the language clusters in research synthesis)

### Attention & Platform Patterns
- **Where they search**: [Google? Reddit? TikTok? Ask friends?]
- **Content they trust**: [reviews? videos? expert articles? UGC?]
- **When they're receptive**: [late night scrolling? active research mode? impulse?]
- **Platform affinity**: [which ad platforms reach them in the right mindset?]
(Infer from research signals — where the quotes came from reveals where the persona lives)

### Creative Brief for This Persona
This is the direct handoff to angle-generator and creative teams:

| Field | Value |
|-------|-------|
| Lead with | [the single most resonant pain point or desire — the thing that stops them scrolling] |
| Prove with | [testimonial? demo? data? guarantee? — the evidence type that converts this persona] |
| Avoid | [what will make them scroll past or distrust — the anti-pattern] |
| CTA style | [urgency? risk-reversal? curiosity? social proof?] |
| Best platform | [where to reach them + why] |
| Hook archetype | [fear? empathy? curiosity? authority? humor?] |
```

### 3. Build the anti-persona

Identify 1-2 customer types who will NEVER convert, no matter the creative. This prevents wasted ad spend.

```markdown
# Anti-Persona: [Name]

### Who they are
[Brief description]

### Why they'll never convert
- [Reason 1 — structural, not just "not interested"]
- [Reason 2]

### How to recognize them in targeting
- [Signals in their behavior or demographics that flag them]

### Research evidence
- "[Quote that reveals why this person is not a fit]"
```

Common anti-personas: DIY loyalists who will never buy a product, people who need a different product category entirely, tire-kickers who research obsessively but never buy.

### 4. Create weighted comparison matrix

Weight each dimension by its importance for creative differentiation. High-weight dimensions are where personas diverge enough to require different ad creative.

| Dimension | Weight | Persona 1 | Persona 2 | Persona 3 |
|-----------|--------|-----------|-----------|-----------|
| Journey Entry Point | High | | | |
| Core Pain | High | | | |
| Prior Solutions Tried | High | | | |
| Conviction Pattern | High | | | |
| Trigger Type | Med | | | |
| Price Sensitivity | Med | | | |
| Platform Affinity | Med | | | |
| Demographics | Low | | | |

If two personas are identical on all High-weight dimensions, merge them.

### 5. Save output

Save as `[product-slug]-personas.md` in the workspace. Include YAML frontmatter:

```yaml
---
product: "[product-slug]"
stage: personas
generated: "[YYYY-MM-DD]"
persona_count: [N]
persona_names: ["Name 1", "Name 2"]
anti_persona: "[Name]"
research_file: "[product-slug]-research.md"
---
```

## Quality Standards

- Every persona element traces back to actual research data — no fabrication
- Decision journey monologue traces the full arc (trigger -> search -> evaluate -> hesitate -> decide), not just emotions
- Personas are clustered by behavior, not demographics — the comparison matrix proves differentiation on high-weight dimensions
- Language fingerprint is organized by emotional register and directly usable for copywriting
- Creative brief per persona is tight and specific enough that a copywriter could start writing immediately
- Anti-persona is included with structural reasons, not just "not the target"
- At least one persona addresses a cluster revealed by the Surprising Findings from research

## Common Mistakes

- Creating personas based on who the marketer *wants* to sell to rather than who actually buys
- Making all personas the same person with slightly different demographics
- Using marketer language instead of customer language
- Skipping "what they've already tried" — this is gold for Failed-Solution ad angles
- Creating too many personas — 4 max
- Writing monologues that are emotion dumps instead of decision journey traces
- Ignoring the anti-persona — every product has people who will waste ad spend

## Reference Files

- **`references/persona-framework.md`** — Complete persona examples with creative briefs, calibrated across verticals
