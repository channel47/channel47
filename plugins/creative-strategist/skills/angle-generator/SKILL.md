---
name: angle-generator
description: This skill should be used when the user asks to "find angles", "generate angles", "ad angles", "selling angles", "creative angles", "hook ideas", "what angles should I test", "brainstorm ad concepts", "creative strategy", "angle brainstorm", or mentions generating advertising angles from research or persona data. Trigger after customer-research or persona-builder has been run, or when the user provides their own research.
---

# Angle Generator — Research-Backed Creative Angles

Transform customer research and personas into concrete, testable advertising angles. Each angle is a strategic framing — the "what to say" before "how to say it." One angle can generate dozens of different ads.

## Inputs

Read the research file (`*-research.md`) and personas file (`*-personas.md`) from the workspace. If these don't exist, inform the user and suggest running those skills first.

Also check `.claude/creative-strategist.local.md` for product positioning.

## Angle Categories

Work through each category and identify which have support in the research data:

**Pain-Agitation** — frame the product as the direct antidote to the most visceral pain point. Look for cascading consequences and social embarrassment.

**Failed-Solution** — speak to people who've tried everything. Position the product as what to try after nothing else worked. Name the specific failed solutions.

**Trigger-Event** — frame around the specific moment someone goes from passive to active. Start the ad at that moment of urgency.

**Identity** — target how the problem makes them see themselves. "Stop being the person who..." or "Become the kind of person who..."

**Social Proof** — leverage surprising users, authority endorsements, or compelling transformations.

**Discovery / Secret** — position as a hidden solution. Works when the product has a genuinely novel mechanism.

**Comparison** — direct or indirect comparison to alternatives. Works with clear, demonstrable advantages.

**Specificity** — lead with a concrete, surprising data point. Specific numbers build instant credibility.

## Process

### 1. Mine angles from research

For each category, check if the research data supports it. Skip categories without evidence.

### 2. Score and rank

For each candidate angle, evaluate:
1. **Research Support** (1-5): How much customer data backs this?
2. **Emotional Intensity** (1-5): How strongly does it hit?
3. **Uniqueness** (1-5): Are competitors already using this?
4. **Breadth** (1-5): Resonates with multiple personas or just one?
5. **Testability** (1-5): How easy to turn into an actual ad?

### 3. Develop top angles

For the top 5-8 angles:

```markdown
## Angle: [Name]
**Category**: [Pain/Failed-Solution/Trigger/Identity/Social-Proof/Discovery/Comparison/Specificity]
**Score**: [X/25]
**Target Persona**: [Which persona(s)]

### The Strategic Frame
[2-3 sentences — what story are we telling? What belief are we creating?]

### Supporting Evidence
- "[Customer quote from research]"
- "[Another quote]"

### Example Hook Directions
1. [Hook direction 1]
2. [Hook direction 2]
3. [Hook direction 3]

### Platform Fit
- **Meta**: [image/video ad notes]
- **YouTube**: [pre-roll potential]
- **TikTok**: [UGC potential]
- **Google Search**: [keyword/intent alignment]

### Risk / Watch-Out
[Any reason this might not work or pitfall to avoid]
```

### 4. Priority matrix

| Rank | Angle | Category | Score | Best Persona | Best Platform | Priority |
|------|-------|----------|-------|-------------|---------------|----------|
| 1 | | | | | | High |
| 2 | | | | | | High |
| 3 | | | | | | Medium |

### 5. Save output

Save as `[product-slug]-angles.md` in the workspace.

## Quality Standards

- Every angle traces back to real research data
- Angles are distinct — merge overlapping ones
- Include at least one angle from an "unexpected" category (Identity, Discovery, Specificity)
- Hook directions demonstrate range, not repetition
- Platform fit is realistic — not every angle works everywhere

## Reference Files

- **`references/angle-frameworks.md`** — Deep dive into each angle category with examples across verticals
