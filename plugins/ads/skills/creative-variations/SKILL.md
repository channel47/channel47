---
name: creative-variations
description: This skill should be used when the user asks to "create ad variations", "iterate on a winning creative", "test creative variants", "A/B test images", "spin off ad creatives", "analyze why an ad works", "create split test images", or wants to generate 3-5 slight variations of an existing ad image. Uploads the reference image to Gemini and generates variants USING that image as a control—not from scratch. Produces psychologically-grounded creative variants that visually match the original.
---

# Creative Variations

Generate 3-5 strategic ad creative variants from a winning reference image. **Uploads the control image to Gemini and uses it as a visual reference** for each variant—ensuring outputs match the original's composition, style, and elements while changing only 1-2 specific things. Enables rigorous split testing without reinventing the wheel.

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

Use the `mcp__plugin_ads_nano-banana__*` tools to generate variants.

**CRITICAL: Two Generation Modes**

This skill supports two distinct modes. **Reference-Based Variations** is the default and primary mode.

#### Mode A: Reference-Based Variations (Default)

Use the uploaded reference image as a visual control. Gemini will generate variations that preserve the reference's composition, style, and elements while making specific changes.

**This is the primary feature.** Always use this mode unless the user explicitly asks for principle-based generation.

#### Mode B: Principle-Based Generation (Alternative)

Generate images from scratch based on analyzed principles from the winning creative. Use this ONLY when:
- The user explicitly says they want "new creatives inspired by" the reference
- The user asks to "apply the winning principles" to a fresh design
- The reference image cannot be uploaded or used effectively

**Always confirm with the user before switching to Mode B:**

```markdown
I've analyzed the reference image. I can generate variations two ways:

1. **Reference-based** (recommended): Generate variants directly from your image,
   changing 1-2 specific elements while keeping everything else visually identical.

2. **Principle-based**: Generate entirely new images that apply the psychological
   principles I identified, but won't visually match your reference.

Which approach would you prefer?
```

---

### Phase 3a: Reference-Based Variant Generation (Primary)

**This is the default workflow. Use this unless the user explicitly requests principle-based generation.**

#### Step 1: Upload the Reference Image

**MANDATORY FIRST STEP.** Before generating ANY variants, upload the reference image to Gemini:

```
mcp__plugin_ads_nano-banana__upload_file
  file_path: "/path/to/control-image.png"
  display_name: "control-creative"
```

Save the returned `file_uri` (format: `files/...`) — you'll need it for every variant.

#### Step 2: Generate Each Variant Using the Reference

Use `generate_image` with the `reference_file_uri` parameter pointing to your uploaded control:

```
mcp__plugin_ads_nano-banana__generate_image
  prompt: "[Variation prompt - see examples below]"
  reference_file_uri: "files/abc123..."  # From upload step
  reference_file_mime_type: "image/png"  # REQUIRED: Must match actual file type
  aspect_ratio: "[same as reference]"
  output_path: "variant-1-[description].png"
```

**CRITICAL Parameters:**
- `reference_file_uri` — Without it, Gemini generates from scratch rather than modifying your control image.
- `reference_file_mime_type` — **Must match the actual file format** (e.g., `"image/png"`, `"image/jpeg"`). Omitting this or using the wrong type causes API errors.

#### Step 3: Repeat for Each Variant

Generate 3-5 variants, each with a different prompt but ALL using the same `reference_file_uri`.

#### Prompt Structure for Reference-Based Variations

When using a reference image, prompts should be modification instructions:

```
Modify this ad creative with the following change:
[SPECIFIC CHANGE - be precise]

Keep everything else exactly the same:
- Same composition and layout
- Same colors except where specified
- Same text styling and positioning
- Same overall aesthetic

The output should look like a minor edit to the original, not a new design.
```

#### Example Prompts (Reference-Based)

**Headline Variation:**
```
Modify this ad creative. Change ONLY the headline text to read:
"[NEW HEADLINE]"

Keep identical:
- Headline position, size, font, and color
- All other text
- Background, product, layout, brand elements
- Overall composition

This should look like the same ad with different headline text.
```

**CTA Color Variation:**
```
Modify this ad creative. Change ONLY the CTA button color to [COLOR].

Keep identical:
- Button shape, size, position, and text
- All other colors
- Layout and composition
- All other elements

The only visible difference should be the button color.
```

**Background Color Variation:**
```
Modify this ad creative. Change ONLY the background color to [COLOR/HEX].

Keep identical:
- All text, logos, and graphics
- Product placement
- Overall composition
- All foreground elements

The only change should be the background color.
```

**Human Element Variation:**
```
Modify this ad creative. Replace the person with a [DEMOGRAPHIC] individual
showing a [EXPRESSION] expression.

Keep identical:
- Person's position in the frame
- Pose and body language
- Background, text, and all design elements
- Overall composition and lighting style
```

---

### Phase 3b: Principle-Based Generation (Alternative)

**Only use this mode if the user explicitly requests it.**

When generating from principles rather than a reference image, you generate entirely new creatives that embody the analyzed psychological triggers and design patterns—but won't visually match the original.

#### When to Offer This Mode

- User says "create new ads inspired by this"
- User wants to test completely different visual approaches
- User wants to apply learnings to a different product/brand
- Technical issues prevent using the reference image

#### Generation Workflow (No Reference)

Generate without the `reference_file_uri` parameter:

```
mcp__plugin_ads_nano-banana__generate_image
  prompt: "[Detailed creative prompt based on analysis]"
  aspect_ratio: "[target aspect ratio]"
  output_path: "inspired-variant-1-[description].png"
```

#### Prompt Structure for Principle-Based Generation

When generating from scratch, prompts must be comprehensive:

```
Create an ad creative for [PRODUCT/SERVICE] that applies these principles:

PSYCHOLOGICAL TRIGGERS:
- [Trigger 1]: [How to implement]
- [Trigger 2]: [How to implement]

VISUAL STYLE:
- Overall aesthetic: [description from analysis]
- Color palette: [colors]
- Typography style: [description]
- Composition: [layout pattern]

REQUIRED ELEMENTS:
- Headline: "[TEXT]"
- CTA: "[TEXT]" in [POSITION]
- [Other required elements]

MOOD/FEELING:
[Description of the emotional response to evoke]

This should feel like a professional ad creative, not AI-generated.
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

**Upload Reference (REQUIRED for reference-based variations):**
```
mcp__plugin_ads_nano-banana__upload_file
  file_path: "/absolute/path/to/image.png"
  display_name: "control-creative"  # Optional descriptive name
```
Returns: `file_uri` (e.g., `files/abc123...`) — save this for generation calls.

**Generate with Reference (Primary workflow):**
```
mcp__plugin_ads_nano-banana__generate_image
  prompt: "Modification instructions..."
  reference_file_uri: "files/abc123..."    # CRITICAL: Links to uploaded control
  reference_file_mime_type: "image/png"    # REQUIRED: Match actual file format
  aspect_ratio: "1:1"                      # Match reference aspect ratio
  output_path: "variant-1-description.png"
```

> ⚠️ **MIME Type Required:** Always provide `reference_file_mime_type` matching your uploaded file (`"image/png"`, `"image/jpeg"`, etc.). The API returns a 400 error if this is missing or mismatched.

**Generate without Reference (Principle-based only):**
```
mcp__plugin_ads_nano-banana__generate_image
  prompt: "Full creative description..."
  aspect_ratio: "1:1"
  output_path: "inspired-variant-1.png"
```

**List Uploaded Files:**
```
mcp__plugin_ads_nano-banana__list_files
```
Use to verify uploads or find existing file URIs.

### Playwright (Optional - for URL screenshots)

- `mcp__plugin_ads_playwright__browser_navigate` - Navigate to URLs
- `mcp__plugin_ads_playwright__browser_take_screenshot` - Capture reference images

---

## Quality Checklist

Before delivering variants:

**Reference-Based Mode (Default):**
- [ ] Reference image uploaded to Gemini via `upload_file`
- [ ] `reference_file_uri` used in ALL `generate_image` calls
- [ ] `reference_file_mime_type` matches actual file format (png/jpeg)
- [ ] Each variant changes only 1-2 elements
- [ ] Variants visually match the control (same composition, style, layout)
- [ ] Hypothesis documented for each variant
- [ ] Psychological basis explained
- [ ] Files named descriptively
- [ ] Summary document complete

**Principle-Based Mode (Alternative):**
- [ ] User explicitly confirmed they want principle-based generation
- [ ] Analysis completed and principles documented
- [ ] Prompts include comprehensive style/element descriptions
- [ ] Generated images embody the identified psychological triggers
- [ ] Clear documentation that these are "inspired by" not "variations of"

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
