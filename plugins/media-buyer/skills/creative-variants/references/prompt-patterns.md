# Prompt Patterns — Ad Variant Generation

## Core Principles

1. **Anchor first, change second.** Every prompt starts with what must be preserved, then specifies what changes. The model handles "keep X, change Y" better than "change Y" alone.

2. **Be concrete, not abstract.** "Make it warmer" is vague. "Shift the background from #FFFFFF to a warm cream (#FFF8F0) with a soft radial gradient" is actionable.

3. **Include the context.** Tell the model this is an ad. "This is a paid social media advertisement for [platform]" changes how the model treats text, composition, and quality.

4. **Constrain aggressively.** AI image models add things. For ads, you want removal of ambiguity. Explicit constraints prevent the model from "helping" in ways that break the ad.

5. **One concept per variant.** Don't ask for a background change AND a copy rewrite AND a layout shift in one prompt. Test one variable at a time.

---

## Prompt Template

```
[CONTEXT]
This is a static image advertisement for [platform]. The original ad is a proven performer 
and I need a variation that [divergence-level description].

[REFERENCE DESCRIPTION]
The original ad features: [brief description of key elements — layout, product, colors, 
copy, CTA, mood]

[PRESERVE — do not change these elements]
- [element 1]: [specific description]
- [element 2]: [specific description]
- [element 3]: [specific description]

[CHANGE — modify these elements as described]
- [element A]: change from [current state] to [target state]
- [element B]: change from [current state] to [target state]

[CONSTRAINTS]
- Maintain professional advertising quality suitable for paid media
- All text must be sharp, legible, and correctly spelled
- CTA must be clearly visible and appear clickable
- No watermarks, stock photo indicators, or template marks
- No AI artifacts: no distorted text, uncanny faces, extra digits, melted objects
- Output must be a standalone ad — no device mockups, no borders, no frames
- Aspect ratio: [WxH]
- Text must not exceed ~20% of image area

[AVOID]
- [specific thing to avoid]
- Generic stock photo aesthetic
- Cluttered composition
- Low contrast between text and background
```

---

## Divergence-Specific Patterns

### Subtle Prompts

Subtle prompts should feel like instructions to a photo editor, not a designer. You're adjusting knobs, not redesigning.

**Color temperature shift:**
```
Edit this ad image. Change only the background color temperature — shift it 
from cool white to warm cream. Everything else must remain exactly as-is: 
product placement, text, logo, CTA button, shadows, composition. 
This is a Facebook feed ad at 1080x1080.
```

**Texture overlay:**
```
Add a subtle paper grain texture to the background of this ad. Opacity should 
be low enough that it reads as "premium print" not "damaged image." 
Preserve all elements: product, text, CTA, logo, layout. No other changes.
```

**Shadow/lighting adjustment:**
```
Deepen the drop shadow under the product by approximately 20%. Shift the 
shadow direction from directly below to slightly lower-right. All other 
elements stay exactly as they are.
```

**Gradient modification:**
```
The background gradient currently runs left-to-right. Change it to a 
radial gradient centered behind the product. Same colors, same opacity range. 
Everything else unchanged.
```

### Moderate Prompts

Moderate prompts give the model more creative room but still clearly anchor to the original.

**Background scene swap:**
```
This is a product ad for [product]. Keep the product shot in its current 
position and size. Keep the headline "[exact headline]" and the CTA button 
"[CTA text]" with its current style. Replace the white studio background with 
a lifestyle scene: a clean wooden table in a bright kitchen with natural 
window light. The mood should shift from clinical to warm and inviting. 
Logo stays in the [position]. Aspect ratio: 1080x1080.
```

**Layout mirror:**
```
Rearrange this ad layout: move the product from center-right to center-left. 
Move the headline and body copy to the right side. Keep the CTA button at 
bottom-center. Maintain the same color palette, typography, and mood. 
The ad should feel like a "mirror" of the original.
```

**Copy angle reframe:**
```
Keep the visual composition of this ad identical — same product shot, same 
background, same layout, same CTA button style. Replace the headline from 
"[original headline]" to "[new headline]". Adjust the subhead to match the 
new angle. All text must be sharp and legible. This is a [platform] ad.
```

**Mood shift:**
```
Transform the mood of this ad from bright and energetic to warm and premium. 
Adjust the color palette: shift blues to deep navy, whites to cream, 
green accents to gold. Darken the overall exposure slightly. Keep the product, 
layout structure, and text content the same. The CTA button should shift 
to a gold tone to match.
```

### Dramatic Prompts

Dramatic prompts describe a new ad concept. The reference image is context, not a template.

**Style transformation:**
```
Create a new ad for [product] with a [40% off] offer. Instead of the 
photographic style of the reference, use a bold flat illustration style 
with thick outlines and a limited color palette (3-4 colors max). 
Large, confident sans-serif headline at the top. Product illustration 
centered. CTA button at the bottom in a contrasting color. 
Logo in the top-left corner. Mood: playful, modern, approachable. 
Size: 1080x1080 for Facebook feed.
```

**Environment change:**
```
Create a completely new ad showing [product] being used in a real-world 
setting — someone holding it in a sunlit café. Lifestyle photography style, 
shallow depth of field. Headline text overlaid in the top third: 
"[new headline]". Small logo in the bottom-right. CTA overlaid as a 
semi-transparent pill button at the bottom. Warm, aspirational mood. 
The ad should feel editorial, not commercial.
```

**Minimal text-heavy:**
```
Design a bold, text-forward ad for [product]. Black background. 
White sans-serif headline in large type taking up 60% of the image: 
"[headline]". Small product image in the bottom-right corner, no larger 
than 20% of the image. Logo centered at the top, small. No CTA button — 
the headline IS the CTA. Stark, confident, Apple-inspired minimalism.
```

---

## Common Pitfalls & Fixes

| Problem | Cause | Fix |
|---------|-------|-----|
| Model changes elements you said to preserve | Preserve instructions too vague | Be hyper-specific: name exact elements, positions, colors |
| Text is garbled or misspelled | AI image models struggle with text | Specify exact text in quotes; if still garbled, plan to overlay text in post-processing |
| CTA button disappeared | Not emphasized enough in prompt | Add: "The CTA button is a critical element — it must be prominent and clearly visible" |
| Variant looks nothing like the original | Used `generate` mode when `edit` was needed | For subtle/moderate, always use edit mode with the reference image |
| Output has that "AI look" | Over-prompted with conflicting styles | Simplify. Remove decorative prompt language. Focus on the change, not the aesthetic |
| Brand colors shifted | Model interpreted "warm" as changing brand colors | Explicitly list brand color hex codes in the preserve section |
| Layout is chaotic | Too many changes in one prompt | Split into multiple variants, each testing one structural change |

---

## Post-Processing Notes

Some things are better handled in post-production than in the prompt:

- **Exact text placement** — If the model can't nail text rendering, generate the visual variant without text, then overlay copy in a design tool
- **Logo placement** — If the logo gets distorted, remove it from the prompt and composite it in post
- **Brand-specific fonts** — AI models can't use proprietary fonts; consider generating the visual and adding typography separately

The CLI generates the visual base. A 2-minute touch-up in Figma or Canva can turn a 90% variant into a 100% production-ready ad.
