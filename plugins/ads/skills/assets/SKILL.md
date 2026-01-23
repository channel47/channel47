---
name: assets
description: |
  Generate ad-ready images using AI with reference-based generation.
  Screenshots product pages for reference, generates brand-consistent
  imagery across all required sizes. Supports PMax and future platforms.
---

# Ad Asset Generator

Generate professional ad images using AI with reference-based workflows.

## Reference Files

This skill uses these reference documents:
- [Prompt Templates](./prompt-templates.md) - Generation prompts by asset type
- [PMax Specs](./pmax-specs.md) - Dimension requirements for Performance Max
- [Iteration Patterns](./iteration-patterns.md) - Refinement workflow patterns

---

## Required Inputs

Before starting, you MUST collect:

1. **Product URL** - The sales page or product landing page
2. **Asset Type** - What kind of image to generate
3. **Platform** - Where assets will be used (PMax, Display, etc.)

If not provided, ask:

> "I need these inputs to generate your ad assets:
> 1. Product URL (I'll screenshot for reference)
> 2. Asset type:
>    - Product shots (hero, detail, packaging)
>    - Lifestyle scenes (product in context)
>    - Before/after transformations
>    - Social proof (customer moments)
>    - Promotional/seasonal
> 3. Platform (PMax, Display, or general)
>
> Which can you provide?"

---

## Phase 1: Input Collection

Confirm all inputs before proceeding:

| Input | Value | Status |
|-------|-------|--------|
| Product URL | [url] | Required |
| Asset Type | [type] | Required |
| Platform | [platform] | Required (default: PMax) |
| Brand Colors | [colors] | Optional |
| Style Notes | [notes] | Optional |

---

## Phase 2: Reference Capture

Use Playwright to capture product images from the sales page.

### Navigate and Analyze

```
1. Navigate to product URL
2. Take page snapshot to understand layout
3. Identify product images (hero, gallery, lifestyle shots)
4. Screenshot each relevant product image
```

**MCP Tools:**
- `mcp__playwright__browser_navigate` - Go to product URL
- `mcp__playwright__browser_snapshot` - Analyze page structure
- `mcp__playwright__browser_take_screenshot` - Capture reference images

### Screenshot Strategy

**For Product Shots:**
- Hero image (main product photo)
- Detail images (close-ups, angles)
- Packaging if visible

**For Lifestyle:**
- In-context usage photos
- Testimonial imagery
- Before/after if present

### Output Format

After capturing, report:

```
REFERENCE IMAGES CAPTURED
-------------------------
1. [filename] - Hero product shot
2. [filename] - Product detail
3. [filename] - Lifestyle context
...

Total: [n] reference images ready for upload
```

---

## Phase 3: Reference Upload

Upload captured screenshots to Nano Banana for use as generation references.

**MCP Tool:**
- `mcp__nano-banana__upload_file` - Upload reference to Gemini Files API

### Upload Each Reference

For each captured screenshot:
```
Uploading: [filename]
Display name: "product-reference-[n]"
```

Track uploaded file URIs for generation phase:

```
UPLOADED REFERENCES
-------------------
1. [file_uri] - Hero shot
2. [file_uri] - Detail
3. [file_uri] - Lifestyle
```

---

## Phase 4: Generation Planning

Map platform specs to Nano Banana aspect ratios.

### PMax Requirements

Reference: [PMax Specs](./pmax-specs.md)

| Asset | Google Spec | Nano Banana Ratio |
|-------|-------------|-------------------|
| Landscape | 1200x628 | `2:1` |
| Square | 1200x1200 | `1:1` |
| Portrait | 960x1200 | `4:3` (portrait) |
| Logo | 1200x1200 | `1:1` |

### Select Prompt Template

Reference: [Prompt Templates](./prompt-templates.md)

Based on asset type, select appropriate template:

| Asset Type | Template Key |
|------------|--------------|
| Product shots | `product_studio` |
| Lifestyle | `lifestyle_context` |
| Before/after | `before_after` |
| Social proof | `social_proof` |
| Promotional | `promotional_seasonal` |

### Generation Queue

Build queue for all required assets:

```
GENERATION QUEUE
----------------
[ ] Landscape (2:1) - [prompt preview]
[ ] Square (1:1) - [prompt preview]
[ ] Portrait (4:3) - [prompt preview]

Reference: [primary reference file]
```

---

## Phase 5: Generation Loop

Generate each asset with review checkpoints.

**MCP Tool:**
- `mcp__nano-banana__generate_image` - Generate with reference and aspect ratio

### Generation Parameters

```python
{
  "prompt": "[constructed from template]",
  "aspect_ratio": "[from spec mapping]",
  "reference_file_uri": "[uploaded reference]",
  "model_tier": "pro",  # Higher quality for ads
  "output_path": "[filename]"
}
```

### Review Checkpoint

After each generation, present for review:

```
GENERATED: [asset type] - [aspect ratio]
------------------------------------------
File: [filename]
Prompt used: [prompt]
Reference: [reference used]

Quality Check:
- [ ] Product recognizable?
- [ ] Colors accurate to reference?
- [ ] No unwanted text/artifacts?
- [ ] Composition appropriate for ads?

[Show generated image]

Options:
1. Approve - Continue to next size
2. Refine - Adjust and regenerate
3. Restart - Use different reference
4. Skip - Move to next asset type
```

---

## Phase 6: Iteration Workflow

Reference: [Iteration Patterns](./iteration-patterns.md)

When refinement is needed:

### Upload Generated as New Reference

```
1. Upload the generated image as new reference
2. Describe what to KEEP from current generation
3. Describe what to CHANGE
4. Regenerate with new prompt
```

### Refinement Prompt Pattern

```
"Keep: [elements to preserve]
Change: [elements to modify]
Reference shows: [description of uploaded generated image]
Goal: [desired outcome]"
```

### Iteration Limits

- Maximum 3 iterations per asset
- If still unsatisfied, offer to:
  - Try different reference image
  - Switch to different asset type
  - Continue with current (can iterate later)

---

## Phase 7: Output Package

Deliver final assets with documentation.

### Asset Summary

```
=================================================================
              Ad Assets Generated
=================================================================

FINAL ASSETS
------------
| File | Type | Dimensions | Status |
|------|------|------------|--------|
| [file] | Landscape | 1200x628 | Approved |
| [file] | Square | 1200x1200 | Approved |
| [file] | Portrait | 960x1200 | Approved |

GENERATION DETAILS
------------------
Reference URL: [original product URL]
Asset Type: [type used]
Model: Gemini Pro (Nano Banana)
Total Iterations: [n]

PROMPTS USED
------------
Landscape: "[final prompt]"
Square: "[final prompt]"
Portrait: "[final prompt]"

=================================================================
```

### Next Steps

```
NEXT STEPS
----------
1. Review assets in file explorer
2. Upload to Google Ads (Assets > Images)
3. For PMax: Return to /ads:pmax Phase 4

Regeneration Commands:
- "Regenerate landscape with [change]"
- "Try different style for square"
- "Generate additional variations"
```

---

## Quality Gates

Apply these checks throughout:

### Gate 1: Product Recognition
> Is the product clearly identifiable?
> Does it match the reference accurately?

### Gate 2: Brand Consistency
> Colors match the original product?
> Style appropriate for the brand?

### Gate 3: Ad Readiness
> Clean background or appropriate context?
> No text overlays (Google adds these)?
> Professional quality suitable for ads?

### Gate 4: Size Consistency
> Consistent look across all sizes?
> Product equally recognizable in each format?

---

## What You Don't Do

- Generate without first capturing reference images
- Skip the review checkpoint
- Output assets that fail quality gates
- Use text overlays (Google adds text dynamically)
- Promise specific ad performance results
- Generate misleading or deceptive imagery
