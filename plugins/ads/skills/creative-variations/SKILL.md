---
name: creative-variations
description: This skill should be used when the user asks to "create ad variations", "iterate on a winning creative", "test creative variants", "A/B test images", "spin off ad creatives", "analyze why an ad works", "create split test images", or wants to generate 3-5 slight variations of an existing ad image. Produces psychologically-grounded creative variants from a reference image.
---

# Creative Variations

Generate 3-5 strategic ad creative variants from a winning reference image. Each variant tweaks 1-2 elements based on direct response psychology, enabling rigorous split testing without reinventing the wheel.

## When to Use

- A winning ad creative exists and needs testing variants
- Scaling a campaign with fresh creatives that maintain proven elements
- Systematic A/B testing of specific visual elements
- Understanding WHY a creative performs before iterating

## Required Inputs

Before starting, collect:

1. **Reference Image** - The winning creative (file path, URL, or screenshot)
2. **Performance Context** (optional) - CTR, conversion rate, or qualitative "it just works"
3. **What to Test** (optional) - Specific elements to vary, or let analysis guide it
4. **Brand Constraints** (optional) - Colors, fonts, imagery restrictions

If the user provides only an image without context, proceed with analysis-first mode.

---

## Workflow

### Phase 1: Creative Analysis (Optional but Recommended)

When the user wants to understand WHY the image wins, or when test direction is unclear, analyze the reference using direct response principles.

#### Visual Hierarchy Analysis

Examine the image for:
- **Focal point**: Where does the eye land first?
- **Reading path**: F-pattern, Z-pattern, or single focal?
- **Contrast zones**: What pops against the background?
- **Negative space**: Breathing room or cluttered?

#### Psychological Triggers Present

Identify which triggers the creative employs (see `references/psychological-triggers.md`):
- **Pattern interrupt**: Does it stop the scroll?
- **Curiosity gap**: Does it create tension needing resolution?
- **Social proof signals**: People, numbers, logos?
- **Scarcity/urgency cues**: Limited time, limited quantity?
- **Transformation promise**: Before/after, outcome visualization?
- **Identity resonance**: "This is for people like me"?

#### Direct Response Elements

Check for classic DR elements:
- **Headline visibility**: Can you read it in 0.5 seconds?
- **Benefit clarity**: Is the "what's in it for me" obvious?
- **CTA presence**: Is there visual direction toward action?
- **Proof elements**: Screenshots, results, testimonials?

#### Output Analysis Summary

```markdown
## Creative Analysis: [Image Name]

### Why It Works
[2-3 sentences on primary success drivers]

### Psychological Triggers Identified
- [Trigger 1]: [How it's implemented]
- [Trigger 2]: [How it's implemented]

### Elements to Preserve (Control Constants)
- [Element that's working - don't change]
- [Element that's working - don't change]

### High-Potential Test Variables
1. [Element to test] - Hypothesis: [expected impact]
2. [Element to test] - Hypothesis: [expected impact]
3. [Element to test] - Hypothesis: [expected impact]
```

---

### Phase 2: Variant Strategy

Based on analysis (or user direction), select 3-5 test dimensions from `references/variation-dimensions.md`.

#### The 1-2 Element Rule

Each variant changes ONLY 1-2 elements from the control. This enables:
- Clear attribution of performance differences
- Statistical validity in split tests
- Iterative learning about what matters

#### Prioritize High-Impact Variables

Test in order of likely impact:
1. **Headline/text** - Highest impact, easiest to test
2. **Color psychology** - Background, accent, CTA colors
3. **Human elements** - Faces, expressions, demographics
4. **Composition** - Layout, focal point position
5. **Social proof placement** - Where and how proof appears

---

### Phase 3: Generate Variants with Nano Banana

Use the `mcp__nano-banana__*` tools to generate variants.

#### Prompt Structure for Variations

When prompting Gemini for variants, use this structure:

```
Reference image attached.

Create a variation of this ad creative with the following change:
[SPECIFIC CHANGE - be precise]

Preserve these elements exactly:
- [List preserved elements from analysis]

Style requirements:
- Maintain the same overall aesthetic and brand feel
- Keep the same aspect ratio ([ratio])
- Match the visual quality and polish of the reference
```

#### Variant Generation Workflow

1. **Upload reference image** using `mcp__nano-banana__upload_file`
2. **Generate each variant** using `mcp__nano-banana__generate_image` with the reference
3. **Name files descriptively**: `variant-1-headline-urgency.png`, `variant-2-cta-green.png`

#### Example Prompts by Test Type

**Headline Variation:**
```
Reference image attached.
Create a variation where the headline reads "[NEW HEADLINE]" instead of the current text.
Preserve: background color, product placement, overall layout, brand elements.
```

**Color Variation:**
```
Reference image attached.
Create a variation where the CTA button is [COLOR] instead of [CURRENT COLOR].
Preserve: all text, layout, imagery, other colors.
```

**Human Element Variation:**
```
Reference image attached.
Create a variation featuring a [DEMOGRAPHIC] person with [EXPRESSION] instead of the current subject.
Preserve: background, text placement, overall composition, brand elements.
```

---

### Phase 4: Deliverables

#### Variant Summary Document

Create a markdown file documenting all variants:

```markdown
# Creative Test: [Campaign/Product Name]

**Date:** YYYY-MM-DD
**Control:** [filename]
**Test Objective:** [What we're trying to learn]

---

## Control Analysis

[Summary from Phase 1]

---

## Variants

### Variant 1: [Test Name]
**File:** variant-1-[description].png
**Change:** [What's different]
**Hypothesis:** [Expected impact and why]
**Psychological Basis:** [Which trigger/principle applies]

### Variant 2: [Test Name]
**File:** variant-2-[description].png
**Change:** [What's different]
**Hypothesis:** [Expected impact and why]
**Psychological Basis:** [Which trigger/principle applies]

[...repeat for all variants]

---

## Testing Recommendations

**Platform:** [Where to run the test]
**Budget Split:** [Recommended allocation]
**Success Metric:** [Primary KPI]
**Minimum Runtime:** [Statistical significance requirement]

---

## Next Steps Based on Results

- If Variant X wins: [Implication and next test]
- If Control wins: [Implication and next test]
```

#### Image Files

Save all generated images with descriptive names:
- `control-[description].png`
- `variant-1-[test-element].png`
- `variant-2-[test-element].png`
- etc.

---

## MCP Tools Reference

### Nano Banana (Gemini Image)

- `mcp__nano-banana__upload_file` - Upload reference images
- `mcp__nano-banana__generate_image` - Generate new images with prompts
- `mcp__nano-banana__list_files` - List uploaded files

### Playwright (Optional - for URL screenshots)

- `mcp__playwright__browser_navigate` - Navigate to URLs
- `mcp__playwright__browser_take_screenshot` - Capture reference images

---

## Quality Checklist

Before delivering variants:

- [ ] Each variant changes only 1-2 elements
- [ ] Control elements are preserved in all variants
- [ ] Hypothesis documented for each variant
- [ ] Psychological basis explained
- [ ] Files named descriptively
- [ ] Summary document complete
- [ ] Testing recommendations included

---

## Additional Resources

### Reference Files

For detailed guidance, consult:
- **`references/psychological-triggers.md`** - Complete trigger library with implementation examples
- **`references/variation-dimensions.md`** - Exhaustive list of testable elements
- **`references/prompt-patterns.md`** - Proven Gemini prompts for each variation type

### Examples

Working examples in `examples/`:
- **`ecommerce-product-test.md`** - Product ad variation example
- **`saas-hero-test.md`** - SaaS landing page hero test
