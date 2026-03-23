---
name: angle-generator
description: This skill should be used when the user asks to "find angles", "generate angles", "ad angles", "selling angles", "creative angles", "unique angles", "hook ideas", "what angles should I test", "brainstorm ad concepts", "creative strategy", "angle brainstorm", or mentions generating, finding, or developing advertising angles from research or persona data. Trigger after customer-research or persona-builder has been run, or when the user provides their own research to derive angles from.
---

# Angle Generator — Research-Backed Ad Angles

This skill transforms customer research and personas into concrete, testable advertising angles. Each angle is a specific strategic framing that can spawn multiple ads — it's the "what to say" before you decide "how to say it."

## What Makes a Good Angle

An angle is NOT a headline or a hook. An angle is a strategic position — a specific way of framing the product's value that resonates with a specific customer pain point or desire. One angle can generate dozens of different ads.

**Example for a pet training device:**
- Angle: "The Neighbor Complaint" — position the product as the solution to social embarrassment from a misbehaving pet
- Angle: "The Failed Everything" — speak to people who've tried trainers, treats, YouTube videos and are exhausted
- Angle: "The New Puppy Panic" — target first-time dog owners who are overwhelmed

Each of these is a strategic direction, not a piece of copy.

## Angle Generation Process

### Step 1: Gather Inputs

Read the research file (`*-research.md`) and personas file (`*-personas.md`) from the workspace. If these don't exist, inform the user and suggest running those skills first.

### Step 2: Mine Angle Categories

Work through each of these proven DTC angle categories and identify which ones have support in the research data:

**Pain-Agitation Angles**
- What's the most visceral pain point? Frame the product as the direct antidote.
- What embarrassing or socially awkward situation does the problem cause?
- What's the hidden cost of NOT solving this? (time, money, relationships, health)

**Failed-Solution Angles**
- What have customers already tried that didn't work?
- Why did those solutions fail? (too expensive, too complicated, didn't last, side effects)
- Position the product as "what to try after everything else has failed"

**Trigger-Event Angles**
- What specific moment pushes someone from "I should fix this" to "I need to fix this NOW"?
- Frame the ad around that moment of urgency

**Identity Angles**
- How does the problem make the customer see themselves? (bad parent, lazy, unhealthy)
- How does the solution let them become who they want to be?

**Social Proof Angles**
- What surprising group of people is already using this?
- What credible authority endorses it?
- What's the most compelling "before and after" transformation?

**Discovery / Secret Angles**
- Is there a non-obvious mechanism or ingredient that makes this work?
- Frame it as "the thing [industry] doesn't want you to know"
- Works especially well when the product has a genuinely novel approach

**Comparison Angles**
- How does this product compare to the most popular alternative?
- What does this do that competitors literally can't?
- Price comparison angle: what's the cost vs. the cost of NOT solving the problem?

**Specificity Angles**
- Pull the most specific, surprising data point from the research
- "73% of dog owners say barking is their #1 complaint" type framings
- Specific numbers and timeframes build instant credibility

### Step 3: Score and Rank Angles

For each candidate angle, evaluate:

1. **Research Support** (1-5): How much customer data backs this angle?
2. **Emotional Intensity** (1-5): How strongly does this angle hit?
3. **Uniqueness** (1-5): Are competitors already using this angle, or is it fresh?
4. **Breadth** (1-5): Does it resonate with multiple personas or just one?
5. **Testability** (1-5): How easy is it to turn this into an actual ad?

Calculate an overall score and rank angles from strongest to weakest.

### Step 4: Develop Top Angles

For the top 5-8 angles, create a full angle brief:

```markdown
## Angle: [Angle Name]
**Category**: [Pain/Failed-Solution/Trigger/Identity/Social-Proof/Discovery/Comparison/Specificity]
**Score**: [X/25]
**Target Persona**: [Which persona(s) this resonates with most]

### The Strategic Frame
[2-3 sentences explaining the angle's core positioning. What story are we telling? What belief are we trying to create?]

### Supporting Evidence
- "[Customer quote from research]"
- "[Another quote]"
- [Data point if available]

### Example Hook Directions
These are NOT final hooks — they're directional ideas showing how this angle could open an ad:
1. [Hook direction 1]
2. [Hook direction 2]
3. [Hook direction 3]

### Platform Fit
- **Meta (FB/IG)**: [how well this works for image/video ads, any format notes]
- **YouTube**: [pre-roll potential, length considerations]
- **TikTok**: [UGC potential, trend relevance]
- **Google Search**: [keyword/intent alignment]

### Risk / Watch-Out
[Any reason this angle might not work, or a pitfall to avoid in execution]
```

### Step 5: Create the Angle Priority Matrix

Summarize all angles in a prioritization table:

| Rank | Angle Name | Category | Score | Best Persona | Best Platform | Test Priority |
|------|-----------|----------|-------|-------------|---------------|---------------|
| 1 | | | | | | High |
| 2 | | | | | | High |
| 3 | | | | | | Medium |

### Step 6: Save Output

Save to the workspace as `[product-slug]-angles.md`.

## Quality Standards

- Every angle must trace back to real research data — not marketer assumptions
- Angles should be distinct from each other — if two angles are basically the same idea with different words, merge them
- Include at least one angle from each of the "unexpected" categories (Identity, Discovery, Specificity)
- The "Example Hook Directions" should demonstrate range, not repetition
- Platform fit should be realistic — not every angle works everywhere

## Additional Resources

### Reference Files
- **`references/angle-frameworks.md`** — Deep dive into each angle category with DTC examples across verticals
