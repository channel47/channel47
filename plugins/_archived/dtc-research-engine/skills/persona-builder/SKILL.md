---
name: persona-builder
description: This skill should be used when the user asks to "build personas", "create customer avatars", "who is the target customer", "customer persona", "buyer persona", "avatar creation", "demographic profile", "psychographic profile", "who buys this product", "target audience profile", or mentions building, creating, or refining customer personas from research data. Trigger after customer-research has been run, or when the user provides their own research/data to base personas on.
---

# Persona Builder — Data-Driven Customer Avatars

This skill transforms raw customer research into vivid, actionable buyer personas that drive ad creative decisions. Unlike generic demographic profiles, these personas are built from real customer language and behavior patterns.

## Why Data-Driven Personas Beat Guesswork

Most DTC personas are fiction — "Sarah, 34, loves yoga, shops at Whole Foods." These are useless because they're based on marketer assumptions rather than customer reality. A data-driven persona captures the actual internal monologue of someone at the moment they decide to search for a solution. That's what makes ad creative resonate.

## Persona Construction Process

### Step 1: Locate the Research File

Check the workspace for an existing research file (`*-research.md`). If none exists, tell the user to run the customer-research skill first, or provide their own research data.

Read the research file thoroughly before proceeding.

### Step 2: Identify Natural Clusters

Look for naturally occurring customer segments in the research data. Segments emerge from patterns in:

- **Trigger events** — Different life situations that lead to the same product search
- **Pain intensity** — Casual annoyance vs. desperate urgency
- **Prior solutions attempted** — Naive first-timers vs. jaded veterans who've "tried everything"
- **Purchase motivation** — Buying for self vs. buying for someone else (spouse, parent, pet, child)
- **Sophistication level** — How much they already know about the product category

Aim for 2-4 distinct personas. More than 4 usually means some are overlapping.

### Step 3: Build Each Persona

For each persona, create a complete profile using this structure:

```markdown
# Persona: [Vivid Name — not generic]
## e.g., "The Desperate Dog Mom" or "The Skeptical Spouse"

### The Snapshot
- **Age Range**: [derived from research signals, not assumed]
- **Gender Skew**: [if data supports it — say "mixed" if unclear]
- **Life Situation**: [the relevant context — e.g., "works from home, dog barks at everything"]
- **Income Signal**: [are they price-sensitive? Premium-seeking? Budget mentions?]
- **Tech Comfort**: [do they shop online easily? Need hand-holding?]

### The Internal Monologue
Write 3-5 sentences in first person as this persona, capturing their actual thought process at the moment they start searching for a solution. Use language patterns directly from the research data.

> "I've tried everything — the spray bottle, the training treats, even that expensive trainer. Nothing works. My neighbor just complained again and I'm honestly afraid they're going to report us. I need something that actually works, not another gimmick."

### The Trigger Event
What specific moment pushed them from passive frustration to active searching?
- Primary trigger: [the most common one from research]
- Secondary triggers: [other situations that push this persona]

### Pain Points (ranked)
1. [Most intense pain — use their words]
2. [Second pain point]
3. [Third pain point]

### Desired Outcome
What do they actually want? Not the product feature — the life outcome.
- **Stated desire**: What they'd say if asked ("I want my dog to stop barking")
- **Deeper desire**: What they really mean ("I want peace and to not feel like a bad dog owner")

### Objections & Skepticism
What's stopping them from buying immediately?
1. [Objection 1 — with source quote if available]
2. [Objection 2]
3. [Objection 3]

### What They've Already Tried
- [Solution 1] — why it failed
- [Solution 2] — why it failed
- [Solution 3] — why it failed

### Language Fingerprint
Key phrases this persona actually uses (from research data):
- "[exact phrase 1]"
- "[exact phrase 2]"
- "[exact phrase 3]"
- "[exact phrase 4]"

### Where They Hang Out Online
Based on where the research data came from:
- [Platform/community 1]
- [Platform/community 2]

### Ad Responsiveness Signals
- **Hook style that works**: [fear-based? curiosity? social proof? authority?]
- **Proof they need**: [testimonials? demonstrations? scientific backing? money-back guarantee?]
- **CTA style**: [urgency? risk-reversal? curiosity-driven?]
```

### Step 4: Create the Persona Comparison Matrix

After building individual personas, create a comparison table:

| Dimension | Persona 1 | Persona 2 | Persona 3 |
|-----------|-----------|-----------|-----------|
| Core Pain | | | |
| Trigger | | | |
| Skepticism Level | | | |
| Price Sensitivity | | | |
| Platform Affinity | | | |
| Hook Style | | | |

### Step 5: Save Output

Save to the workspace as `[product-slug]-personas.md`.

## Quality Standards

- Every persona element must trace back to actual research data — no fabrication
- The "Internal Monologue" section must use real customer language patterns, not marketing-speak
- Personas should feel like real people, not demographic spreadsheets
- Each persona should be distinct enough to warrant different ad creative
- Include enough language fingerprint data to directly inform copywriting

## Common Mistakes to Avoid

- Creating personas based on who the marketer *wants* to sell to rather than who actually buys
- Making all personas basically the same person with slightly different demographics
- Using marketer language instead of customer language in the monologue
- Skipping the "what they've already tried" section — this is gold for ad angles
- Creating too many personas (4 max) — focus on the most distinct and addressable segments

## Additional Resources

### Reference Files
- **`references/persona-examples.md`** — Complete persona examples from different DTC verticals for calibration
