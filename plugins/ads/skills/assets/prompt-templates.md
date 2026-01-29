# Asset Generation Prompt Templates

Curated prompts for each asset type, optimized for Nano Banana (Gemini) image generation.

---

## Template Structure

Each template follows this pattern:

```
[Style/Quality] + [Subject] + [Context] + [Technical] + [Exclusions]
```

- **Style/Quality**: Professional, studio, natural, etc.
- **Subject**: What to show and how
- **Context**: Background, setting, lighting
- **Technical**: Composition, framing notes
- **Exclusions**: What NOT to include

---

## Product Shot Templates

### `product_studio` - Hero Product Photography

**Use for:** Main product images, e-commerce style, clean backgrounds

```
Professional e-commerce product photography, studio lighting with soft shadows,
[PRODUCT DESCRIPTION] centered in frame occupying 70-80% of composition,
clean white or light gray gradient background, sharp focus on product details,
commercial quality, high-end advertising aesthetic.
No text, no watermarks, no human hands, no props unless essential to product.
```

**Variables to fill:**
- `[PRODUCT DESCRIPTION]`: Specific product details from reference (e.g., "blue squeeze bottle with yellow trigger spray, clear window showing liquid inside")

### `product_detail` - Close-Up Details

**Use for:** Texture, materials, craftsmanship highlights

```
Macro product photography, extreme detail focus, professional studio lighting,
close-up of [SPECIFIC DETAIL] showing [MATERIAL/TEXTURE],
shallow depth of field with crisp focus on subject,
neutral background that complements product colors.
No text overlays, no distracting elements.
```

**Variables:**
- `[SPECIFIC DETAIL]`: What feature to highlight
- `[MATERIAL/TEXTURE]`: Surface quality (matte, glossy, fabric weave, etc.)

### `product_packaging` - Package/Box Shots

**Use for:** Retail packaging, unboxing experience

```
Professional packaging photography, [PACKAGE TYPE] displayed at slight angle,
studio lighting emphasizing package design and branding,
clean surface reflection, premium commercial quality,
package as hero with [BACKGROUND COLOR] backdrop.
No hands, no additional props.
```

**Variables:**
- `[PACKAGE TYPE]`: Box, pouch, bottle, tube, etc.
- `[BACKGROUND COLOR]`: Match or complement brand colors

---

## Lifestyle Templates

### `lifestyle_context` - Product in Use

**Use for:** Showing product in natural environment, target audience connection

```
Authentic lifestyle photography, [PRODUCT] being used by [DEMOGRAPHIC]
in [SETTING], natural daylight with [TIME OF DAY] warmth,
candid moment not staged, [BRAND COLORS] subtly visible in scene,
aspirational but believable, emotional connection to viewer.
No posed studio looks, no obvious advertising aesthetic.
```

**Variables:**
- `[PRODUCT]`: Brief product description
- `[DEMOGRAPHIC]`: Target user (e.g., "young professional", "active mom", "home cook")
- `[SETTING]`: Environment (kitchen, office, gym, outdoors, etc.)
- `[TIME OF DAY]`: Morning, afternoon, golden hour
- `[BRAND COLORS]`: Colors to incorporate subtly

### `lifestyle_aspirational` - Outcome/Result Focus

**Use for:** Showing the benefit/result of using product

```
Aspirational lifestyle image, [DESIRED OUTCOME] achieved through product use,
[PERSON/SCENE] radiating [EMOTION], high-end editorial photography style,
natural lighting in [PREMIUM SETTING], subtle product placement or implied use,
Instagram-worthy composition, genuine not commercial.
No direct product display, focus on transformation/result.
```

**Variables:**
- `[DESIRED OUTCOME]`: What the product helps achieve
- `[PERSON/SCENE]`: Who or what to show
- `[EMOTION]`: Confidence, joy, relaxation, energy, etc.
- `[PREMIUM SETTING]`: Upscale environment matching brand positioning

---

## Before/After Templates

### `before_after` - Transformation Split

**Use for:** Results-focused products (cleaning, beauty, fitness, etc.)

```
Split composition transformation image, left side showing [PROBLEM STATE],
right side showing [SOLVED STATE with product result], clear visual contrast
between before and after, same lighting and angle on both sides for fair comparison,
professional photography quality, believable transformation.
No text labels, no arrows, no obvious manipulation.
```

**Variables:**
- `[PROBLEM STATE]`: The challenge/issue (dirty surface, tired skin, messy space)
- `[SOLVED STATE]`: After using product (clean, refreshed, organized)

### `before_after_subtle` - Implied Transformation

**Use for:** When direct comparison isn't appropriate

```
Single image implying positive transformation, [SUBJECT] in clearly improved state,
visual cues suggesting recent change or upgrade, [PRODUCT] visible but not dominant,
aspirational outcome photography, natural lighting,
story of improvement without explicit before.
No split screen, no comparison markers.
```

---

## Social Proof Templates

### `social_proof` - Happy Customer Moment

**Use for:** User-generated content style, testimonial support

```
Authentic customer photography, genuine happy expression from [DEMOGRAPHIC]
with [PRODUCT], casual setting like [LOCATION], smartphone-quality aesthetic
but well-lit, real moment of satisfaction or discovery,
relatable not model-perfect, warm and approachable.
No studio lighting, no commercial poses.
```

**Variables:**
- `[DEMOGRAPHIC]`: Target customer type
- `[PRODUCT]`: Product in use or recently used
- `[LOCATION]`: Home, office, outdoor casual setting

### `social_proof_outcome` - Result Celebration

**Use for:** Showing achieved results, success moments

```
Celebration of achievement moment, [PERSON TYPE] experiencing [POSITIVE OUTCOME],
genuine emotion of satisfaction/joy/relief, implies product-assisted success,
candid photography style, natural environment,
emotional resonance over product visibility.
No forced poses, no direct camera awareness.
```

---

## Promotional Templates

### `promotional_seasonal` - Holiday/Event Themed

**Use for:** Seasonal campaigns, holiday promotions

```
[SEASON/HOLIDAY] themed product presentation, [PRODUCT] as hero
with subtle [HOLIDAY ELEMENTS] in background or styling,
festive but not overwhelming, premium advertising quality,
[SEASONAL COLORS] incorporated tastefully, gift-worthy presentation.
No text, no price tags, no sale graphics.
```

**Variables:**
- `[SEASON/HOLIDAY]`: Christmas, summer, Valentine's, etc.
- `[PRODUCT]`: Product description
- `[HOLIDAY ELEMENTS]`: Subtle thematic props (greenery, lights, hearts, etc.)
- `[SEASONAL COLORS]`: Red/green, pastels, autumn tones, etc.

### `promotional_premium` - Luxury/Value Enhancement

**Use for:** Upgrading perceived value, premium positioning

```
Luxury product photography, [PRODUCT] presented with premium styling,
high-end materials in scene (marble, velvet, gold accents),
dramatic lighting with [MOOD] atmosphere, aspirational wealth aesthetic,
boutique or designer brand quality, exclusive and desirable.
No cluttered compositions, no budget aesthetic.
```

**Variables:**
- `[PRODUCT]`: Product description
- `[MOOD]`: Sophisticated, warm, dramatic, serene

---

## Aspect Ratio Adjustments

Modify templates based on target aspect ratio:

### Landscape (2:1)
- Add: "horizontal composition with product left of center, space for text overlay on right"
- Good for: Hero banners, YouTube thumbnails

### Square (1:1)
- Add: "centered composition, balanced framing, product occupies majority of frame"
- Good for: Instagram, Discovery ads

### Portrait (4:3 / 9:16)
- Add: "vertical composition, product in upper third, context in lower portion"
- Good for: Stories, mobile-first placements

---

## Refinement Prompt Patterns

When iterating on a generated image:

### Color Correction
```
"Keep the composition and product placement exactly as shown in reference.
Change the [COLOR ELEMENT] from [CURRENT] to [DESIRED].
Match the color accuracy of the original product image."
```

### Style Adjustment
```
"Keep the product and layout from reference image.
Change the style from [CURRENT STYLE] to [DESIRED STYLE].
Maintain product recognition and brand colors."
```

### Background Swap
```
"Keep the product exactly as shown, same angle and lighting on product.
Replace the background with [NEW BACKGROUND DESCRIPTION].
Ensure product edges integrate naturally with new background."
```

### Detail Enhancement
```
"Keep the overall image, improve detail on [SPECIFIC ELEMENT].
Make [FEATURE] more visible/prominent/accurate.
Reference shows the correct [FEATURE] to match."
```

---

## Anti-Patterns to Avoid

**Don't include in prompts:**
- "With text saying..." (Google adds text dynamically)
- "Sale" or "% off" or price indicators
- Specific celebrity or brand references
- "Photorealistic human face" (often uncanny)
- Competitor product references
- Misleading before/after claims

**Watch for:**
- Generated text/numbers (regenerate if present)
- Extra limbs or distorted body parts
- Inconsistent lighting between elements
- Brand logo alterations
- Product proportion errors
