# Iteration Patterns

Refinement workflows for improving generated ad assets.

---

## Core Iteration Loop

The standard workflow for refining generated images:

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  1. GENERATE with product reference                         │
│              ↓                                              │
│  2. REVIEW output vs reference                              │
│              ↓                                              │
│  3. DECISION                                                │
│     ├── APPROVED → Next size/type                          │
│     └── NEEDS FIX → Continue to step 4                     │
│              ↓                                              │
│  4. UPLOAD generated as new reference                       │
│              ↓                                              │
│  5. PROMPT for specific correction                          │
│              ↓                                              │
│  6. REGENERATE                                              │
│              ↓                                              │
│  └──────── Return to step 2                                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Quality Gates

Apply these sequential checks at step 2 (REVIEW):

### Gate 1: Product Recognition
> "Can I identify this as the same product from the reference?"

**Check for:**
- Overall shape matches
- Key distinguishing features present
- Scale/proportions correct
- Brand elements recognizable

**If fails:** Reference not used effectively → restart with clearer reference or more specific prompt

### Gate 2: Color & Detail Accuracy
> "Do the colors, textures, and details match the reference?"

**Check for:**
- Color accuracy (brand colors correct)
- Material representation (matte/gloss/texture)
- Label/packaging details (if applicable)
- Lighting consistency with reference

**If fails:** Upload generated → prompt for specific color/detail corrections

### Gate 3: Composition & Framing
> "Does the image work as an ad in this format?"

**Check for:**
- Subject properly positioned for ratio
- Breathing room for text overlay zones
- No awkward cropping of important elements
- Balance appropriate for placement type

**If fails:** Describe composition adjustment → regenerate

### Gate 4: Cross-Size Consistency
> "Does this match the approved images in other sizes?"

**Check for:**
- Same product angle/representation
- Consistent lighting and style
- Brand feel maintained
- Could be recognized as same campaign

**If fails:** Reference approved version → match style

---

## Refinement Prompt Patterns

### Pattern 1: Keep/Change Framework

Most effective for targeted fixes:

```
"Keep: [specific elements to preserve]
Change: [specific elements to modify]
Reference shows: [description of what's in uploaded image]
Goal: [desired outcome]"
```

**Example:**
```
"Keep: the product angle, background color, and overall composition
Change: the bottle color from green to blue as shown in original reference
Reference shows: current generation with green bottle
Goal: exact color match to original product photo"
```

### Pattern 2: Element Isolation

For fixing one specific thing:

```
"The reference image is my current generation. Everything is correct except [ELEMENT].
Please regenerate with [ELEMENT] changed to [CORRECTION].
Keep all other aspects identical: [list key elements to preserve]."
```

**Example:**
```
"The reference image is my current generation. Everything is correct except the spray trigger.
Please regenerate with the trigger changed to yellow instead of orange.
Keep all other aspects identical: product angle, blue bottle, white background, lighting."
```

### Pattern 3: Style Transfer

For adjusting overall aesthetic:

```
"Using the product from the reference image, regenerate in [NEW STYLE].
Maintain product accuracy: [key product details].
Change atmosphere to: [style description]."
```

**Example:**
```
"Using the product from the reference image, regenerate in lifestyle context.
Maintain product accuracy: blue bottle, yellow trigger, clear window.
Change atmosphere to: kitchen counter, natural morning light, home cleaning context."
```

### Pattern 4: Composition Adjustment

For framing/layout fixes:

```
"Same product and style as reference.
Adjust composition: [framing change].
Ensure: [important elements] remain visible and prominent."
```

**Example:**
```
"Same product and style as reference.
Adjust composition: move product to left third, add more negative space on right.
Ensure: full product visible, label facing camera."
```

---

## Iteration Limits

### Maximum Attempts Per Asset

| Iteration | Action |
|-----------|--------|
| 1 | Initial generation |
| 2 | First refinement |
| 3 | Second refinement |
| 4+ | Escalate decision |

### Escalation Options (After 3 Iterations)

Present to user:

```
This asset has been refined 3 times. Options:

1. ACCEPT CURRENT - Use best version so far
2. NEW REFERENCE - Try different source image
3. DIFFERENT TYPE - Switch asset type (e.g., lifestyle → product)
4. MANUAL EDIT - Provide for manual touch-up in image editor
5. SKIP - Continue without this asset (if not required)

Which approach?
```

---

## Common Fixes by Issue Type

### Color Issues

**Problem:** Product color doesn't match
**Solution:**
```
"Reference shows [correct color description].
The [element] should be [exact color] not [current color].
Keep composition and lighting identical."
```

### Shape/Proportion Issues

**Problem:** Product looks distorted
**Solution:**
```
"The product shape in reference is [description].
Current generation has [distortion issue].
Regenerate with accurate proportions matching reference exactly."
```

### Background Issues

**Problem:** Background doesn't work for ads
**Solution:**
```
"Keep the product exactly as generated.
Replace background with [clean/lifestyle description].
Ensure product edges integrate naturally."
```

### Unwanted Elements

**Problem:** Generated text, artifacts, extra objects
**Solution:**
```
"Keep the product and composition.
Remove the [unwanted element] completely.
Replace area with [clean continuation of background/surface]."
```

### Lighting Issues

**Problem:** Shadows wrong, too dark/bright
**Solution:**
```
"Keep product and composition.
Adjust lighting to [desired lighting description].
Match the lighting style from the original reference photo."
```

---

## Multi-Size Consistency Workflow

When generating a set of assets:

### Step 1: Establish Hero
- Generate square (1:1) first
- Iterate until approved
- This becomes the "reference style"

### Step 2: Match Landscape
- Upload approved square as reference
- Prompt: "Same product, same style, same lighting. Adapt to landscape 2:1 composition."
- Compare: product angle, colors, overall feel

### Step 3: Match Portrait
- Reference both approved square and landscape
- Prompt: "Match the established style. Adapt to portrait 3:4 composition."
- Ensure vertical framing works for mobile

### Cross-Reference Prompt
```
"I have approved [landscape/square/portrait] versions with this style:
[describe the established look]

Generate [new size] that matches this campaign aesthetic.
Product must be recognizable as the same item.
Lighting, color treatment, and brand feel must be consistent."
```

---

## Documentation During Iteration

Track refinements for reproducibility:

```
ITERATION LOG: [Asset Name]
===========================

V1 - Initial Generation
-----------------------
Prompt: [full prompt]
Reference: [file used]
Result: [brief description]
Decision: REFINE - [reason]

V2 - First Refinement
---------------------
Prompt: [refined prompt]
Reference: [V1 output + original]
Changes requested: [specific changes]
Result: [brief description]
Decision: APPROVED

Final: [filename]
```

This log helps:
- Reproduce successful generations
- Learn what prompts work
- Speed up future similar assets
