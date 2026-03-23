---
name: persona-builder
description: This skill should be used when the user asks to "build personas", "create customer avatars", "who is the target customer", "customer persona", "buyer persona", "demographic profile", "psychographic profile", "who buys this product", "target audience profile", or mentions building, creating, or refining customer personas from research data. Trigger after customer-research has been run, or when the user provides their own research data.
---

# Persona Builder — Data-Driven Customer Avatars

Transform raw customer research into vivid, actionable buyer personas. Unlike generic demographic profiles, these personas are built from real customer language and behavior patterns.

## Inputs

Check for an existing research file (`*-research.md`) in the workspace. If none exists, tell the user to run customer-research first or provide their own data.

Also check `.claude/creative-strategist.local.md` for product details and positioning.

## Persona Construction

### 1. Identify natural clusters

Look for naturally occurring segments in the research. Segments emerge from:
- **Trigger events** — different life situations leading to the same search
- **Pain intensity** — casual annoyance vs. desperate urgency
- **Prior solutions** — naive first-timers vs. jaded veterans who've "tried everything"
- **Purchase motivation** — buying for self vs. someone else
- **Sophistication** — how much they already know about the category

Aim for 2-4 distinct personas. More than 4 usually means overlap.

### 2. Build each persona

For each persona:

```markdown
# Persona: [Vivid Name]
## e.g., "The Desperate Dog Mom" or "The Skeptical Spouse"

### The Snapshot
- **Age Range**: [from research signals, not assumptions]
- **Gender Skew**: [if data supports it — "mixed" if unclear]
- **Life Situation**: [relevant context]
- **Income Signal**: [price-sensitive? premium-seeking?]

### The Internal Monologue
3-5 sentences in first person capturing their thought process at the moment they start searching. Use language directly from research data.

### The Trigger Event
- Primary trigger: [most common from research]
- Secondary triggers: [other situations]

### Pain Points (ranked)
1. [Most intense — use their words]
2. [Second]
3. [Third]

### Desired Outcome
- **Stated desire**: What they'd say if asked
- **Deeper desire**: What they really mean

### Objections & Skepticism
1. [With source quote if available]
2. [...]

### What They've Already Tried
- [Solution] — why it failed
- [Solution] — why it failed

### Language Fingerprint
Key phrases this persona actually uses (from research):
- "[exact phrase]"
- "[exact phrase]"

### Ad Responsiveness Signals
- **Hook style**: [fear? curiosity? social proof? authority?]
- **Proof needed**: [testimonials? demos? scientific backing? guarantee?]
- **CTA style**: [urgency? risk-reversal? curiosity?]
```

### 3. Create comparison matrix

| Dimension | Persona 1 | Persona 2 | Persona 3 |
|-----------|-----------|-----------|-----------|
| Core Pain | | | |
| Trigger | | | |
| Skepticism Level | | | |
| Price Sensitivity | | | |
| Hook Style | | | |

### 4. Save output

Save as `[product-slug]-personas.md` in the workspace.

## Quality Standards

- Every persona element traces back to actual research data — no fabrication
- Internal monologue uses real customer language, not marketing-speak
- Personas feel like real people, not demographic spreadsheets
- Each persona is distinct enough to warrant different creative
- Language fingerprint data is directly usable for copywriting

## Common Mistakes

- Creating personas based on who the marketer *wants* to sell to rather than who actually buys
- Making all personas the same person with slightly different demographics
- Using marketer language instead of customer language
- Skipping "what they've already tried" — this is gold for ad angles
- Creating too many personas — 4 max

## Reference Files

- **`references/persona-framework.md`** — Complete persona examples from different verticals for calibration
