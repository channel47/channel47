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

## Phase 0: Asset Inventory Check

**MANDATORY** before generating new assets.

### Query Existing Assets

Check what assets already exist in the Google Ads account:

```sql
SELECT
  asset.id,
  asset.name,
  asset.type,
  asset.image_asset.full_size.width_pixels,
  asset.image_asset.full_size.height_pixels,
  asset.image_asset.file_size
FROM asset
WHERE asset.type = 'IMAGE'
```

### Present Inventory

```
EXISTING IMAGE ASSETS
---------------------
| Name | Dimensions | Type | Status |
|------|------------|------|--------|
| [name] | 1200x628 | Landscape | Available |
| [name] | 1200x1200 | Square | Available |
| [name] | 960x1200 | Portrait | Available |

GAPS IDENTIFIED
---------------
| Required | Status |
|----------|--------|
| Landscape (1200x628) | [Available/Missing] |
| Square (1200x1200) | [Available/Missing] |
| Portrait (960x1200) | [Available/Missing] |
```

### User Decision

Ask user how to proceed:

> "You have [n] existing image assets. How would you like to proceed?
>
> 1. **Reuse existing** - Skip generation, use what you have
> 2. **Generate new** - Create fresh assets (existing remain available)
> 3. **Only generate missing** - Fill gaps, keep existing sizes
>
> Which approach?"

If user selects option 1, skip to Phase 7 (Output Package) with existing assets.
If user selects option 2 or 3, continue to Phase 1.

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

### Asset Quantity Selection

Ask user how many variations to generate:

> "How many images per size would you like?
>
> 1. **1-2 images** - Minimum viable (for testing)
> 2. **3-5 images** - Standard launch (recommended)
> 3. **5-10 images** - Full optimization (larger budgets)
>
> Which quantity level?"

**Budget-based recommendations:**
- Under $1,500/month: 1-2 per size
- $1,500-$5,000/month: 3-5 per size
- Over $5,000/month: 5-10 per size

### Creative Type Selection

Based on product category, suggest appropriate types:

**Beauty/Personal Care:**
- Product shots (hero, detail)
- Before/after transformations
- Lifestyle (product in use)

**Electronics/Tech:**
- Product shots (hero, angles)
- Feature highlights
- Lifestyle (in context)

**Food/Beverage:**
- Product shots (packaging)
- Lifestyle (consumption moment)
- Seasonal/occasion

**Fashion/Apparel:**
- Product shots (flat lay, on model reference)
- Lifestyle (styled context)
- Detail shots (texture, material)

**Home/Furniture:**
- Product shots (hero)
- Room context (in situ)
- Detail shots (materials, features)

Ask user:

> "For [product category], I recommend these creative types:
> - [type 1]
> - [type 2]
> - [type 3]
>
> Which types would you like to generate? (Select multiple or all)"

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

| Asset | Google Spec | Nano Banana Ratio | Notes |
|-------|-------------|-------------------|-------|
| Landscape | 1200x628 | `16:9` | ~10% height crop needed |
| Square | 1200x1200 | `1:1` | Exact match |
| Portrait | 960x1200 | `3:4` | ~6% crop needed |
| Logo | 1200x1200 | `1:1` | Use existing file if 4:1 needed |

**Note:** Nano Banana valid ratios: `1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `2:3`, `3:2`

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
[ ] Landscape (16:9) - [prompt preview]
[ ] Square (1:1) - [prompt preview]
[ ] Portrait (3:4) - [prompt preview]

Reference: [primary reference file]
Quantity per size: [user selection from Phase 1]
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
