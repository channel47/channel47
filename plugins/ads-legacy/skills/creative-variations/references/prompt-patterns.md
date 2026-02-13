# Prompt Patterns for Gemini Image Generation

Proven prompt structures for generating ad creative variants with Nano Banana (Gemini). These patterns maximize consistency with the reference while achieving specific variations.

---

## Critical: Using the Reference Image

**ALWAYS upload and reference the control image.** Without the `reference_file_uri` parameter, Gemini generates from scratch rather than modifying your control.

### Required Workflow

```
# Step 1: Upload the control image
mcp__plugin_ads_nano-banana__upload_file
  file_path: "/path/to/control.png"

# Step 2: Use the returned file_uri in EVERY generation call
mcp__plugin_ads_nano-banana__generate_image
  prompt: "[modification prompt]"
  reference_file_uri: "files/abc123..."  # <-- CRITICAL
  output_path: "variant-1.png"
```

**The `reference_file_uri` parameter is what makes these VARIATIONS rather than completely new images.**

---

## Core Prompt Structure (Reference-Based)

When using a reference image, prompts should be **modification instructions**, not full creative descriptions:

```
Modify this ad creative with the following change:
[PRECISE CHANGE DESCRIPTION - be specific]

Keep everything else exactly the same:
- [Element to preserve]
- [Element to preserve]
- [Element to preserve]

The output should look like a minor edit to the original, not a new design.
```

### Key Principles

1. **Be specific about the change** - "Change the CTA button to green" not "make it more vibrant"
2. **Explicitly list what to preserve** - Don't assume Gemini will keep anything unchanged
3. **Reinforce it's a modification** - "minor edit to the original, not a new design"

---

## Text/Headline Variations

### Headline Replacement

```
Reference image attached. This is a winning ad creative.

Create a variation where the main headline text reads:
"[NEW HEADLINE TEXT]"

The headline should:
- Appear in the same position as the original
- Use the same approximate font size and weight
- Maintain the same text color and any effects (shadow, outline)

Preserve these elements exactly:
- Background image/color
- Product placement and size
- Supporting text elements
- Logo and brand elements
- Overall composition and layout
```

### Subheadline Addition

```
Reference image attached. This is a winning ad creative.

Create a variation that adds a subheadline below the main headline:
"[SUBHEADLINE TEXT]"

The subheadline should:
- Be smaller than the main headline (approximately 60% size)
- Use the same font family
- Appear directly below the main headline with appropriate spacing

Preserve these elements exactly:
- Main headline text and styling
- All other visual elements
- Overall balance and composition
```

### Text Style Variation

```
Reference image attached. This is a winning ad creative.

Create a variation where the headline uses [STYLE CHANGE]:
- [e.g., ALL CAPS instead of Title Case]
- [e.g., Bold weight instead of regular]
- [e.g., Serif font instead of sans-serif]

Preserve these elements exactly:
- Headline content/wording (keep same text)
- Text position and size
- All non-text elements
```

---

## Color Variations

### Background Color

```
Reference image attached. This is a winning ad creative.

Create a variation where the background color is changed to:
[COLOR NAME or HEX CODE]

The new background should:
- Maintain the same level of visual interest (solid, gradient, or texture as original)
- Ensure all text and elements remain clearly readable
- Keep the overall mood consistent with the brand

Preserve these elements exactly:
- All text content, position, and styling
- Product/subject placement
- Non-background colors (text, CTA, accents)
- Logo and brand elements
```

### CTA Button Color

```
Reference image attached. This is a winning ad creative.

Create a variation where the CTA button color is changed to:
[COLOR NAME]

Requirements:
- Button should maintain its shape, size, and position
- Text on the button should remain readable (adjust text color if needed for contrast)
- The new color should create strong visual contrast with the background

Preserve these elements exactly:
- Button text content
- Button position and size
- All other elements
```

### Accent Color Shift

```
Reference image attached. This is a winning ad creative.

Create a variation where the accent color is changed from [CURRENT] to [NEW]:
- Apply to: [decorative elements, borders, highlights, etc.]
- Do NOT change: [background, text, product colors]

Preserve these elements exactly:
- Primary color scheme (except specified accent)
- All text content
- Product appearance
- Overall composition
```

---

## Human Element Variations

### Expression Change

```
Reference image attached. This is a winning ad creative featuring a person.

Create a variation where the person's expression changes to:
[EXPRESSION: e.g., excited/surprised, calm/confident, thoughtful/curious]

The person should:
- Maintain the same general appearance (age, gender, styling)
- Be in the same position and pose
- Interact with the environment/product in the same way

Preserve these elements exactly:
- Background and setting
- Product placement
- All text and design elements
- Clothing and personal styling
```

### Demographic Variation

```
Reference image attached. This is a winning ad creative.

Create a variation featuring a [DEMOGRAPHIC DESCRIPTION] person:
- Age range: [e.g., 35-45]
- Gender: [e.g., female]
- Appearance: [e.g., professional, athletic, casual]

The person should:
- Be in the same position as the current subject
- Have a similar expression and body language
- Interact with the product/scene in the same way

Preserve these elements exactly:
- Background, setting, and lighting
- All text and design elements
- Product placement
- Overall composition
```

### Gaze Direction

```
Reference image attached. This is a winning ad creative.

Create a variation where the person's gaze is directed:
[DIRECTION: at the camera, at the product, toward the CTA, off to the side]

The change in gaze should:
- Feel natural and intentional
- Maintain the same expression/mood
- Create [desired effect: connection with viewer, focus on product, etc.]

Preserve these elements exactly:
- All other aspects of the person's appearance
- Background and setting
- Text and design elements
```

---

## Composition Variations

### Text Position

```
Reference image attached. This is a winning ad creative.

Create a variation where the text elements are positioned at the [TOP/CENTER/BOTTOM] of the image instead of their current position.

The text should:
- Maintain its current hierarchy and styling
- Remain readable against whatever is behind it (add subtle background overlay if needed)
- Feel balanced within the new composition

Preserve these elements exactly:
- Text content and styling
- Product/subject positioning
- Background image/elements
```

### Layout Flip

```
Reference image attached. This is a winning ad creative.

Create a variation with a mirrored layout where:
- Elements on the left move to the right
- Elements on the right move to the left
- Text remains readable (not mirrored)

The flipped layout should:
- Maintain the same overall balance
- Keep all relationships between elements intact

Preserve these elements exactly:
- Text content (just repositioned)
- Color scheme
- Element sizes and styling
```

### Aspect Ratio Adaptation

```
Reference image attached. This is a winning ad creative.

Create a variation adapted to [NEW ASPECT RATIO: e.g., 9:16 vertical, 1:1 square, 16:9 horizontal].

The adaptation should:
- Prioritize the most important elements (headline, product, CTA)
- Recompose thoughtfully for the new format
- Maintain visual hierarchy and balance

Preserve these elements exactly:
- All text content
- Product representation
- Brand elements and colors
- Overall aesthetic and quality
```

---

## Social Proof Variations

### Adding Social Proof

```
Reference image attached. This is a winning ad creative.

Create a variation that adds a [SOCIAL PROOF TYPE] element:
- [Star rating badge: 4.8/5 stars]
- [User count: "Join 50,000+ users"]
- [Testimonial snippet: "Best purchase I've made" - Sarah K.]
- [Trust badges: SSL/Money-back guarantee icons]

The social proof should:
- Be placed in a prominent but non-intrusive location
- Match the visual style of the existing design
- Be clearly readable

Preserve these elements exactly:
- Primary headline and messaging
- Product placement
- Overall layout (adjust minimally to accommodate)
```

### Social Proof Style Change

```
Reference image attached. This is a winning ad creative with social proof.

Create a variation where the social proof element is changed from [CURRENT TYPE] to [NEW TYPE]:
- From: [e.g., star rating]
- To: [e.g., customer testimonial with photo]

The new social proof should:
- Occupy approximately the same space
- Match the visual style of the design
- Be equally or more prominent

Preserve these elements exactly:
- All other elements
- Overall composition and balance
```

---

## Urgency/Scarcity Variations

### Adding Urgency Element

```
Reference image attached. This is a winning ad creative.

Create a variation that adds an urgency indicator:
- [Badge: "Limited Time Offer"]
- [Banner: "Ends Friday"]
- [Counter: "Only 12 left"]

The urgency element should:
- Be visually prominent without overwhelming the main message
- Use colors that create appropriate urgency (typically warm colors)
- Be positioned in [corner/top/bottom as appropriate]

Preserve these elements exactly:
- Primary headline and messaging
- Product representation
- Core layout and composition
```

### Urgency Style Variation

```
Reference image attached. This is a winning ad creative with an urgency element.

Create a variation where the urgency indicator style changes:
- From: [e.g., corner badge]
- To: [e.g., banner across top]

The new urgency treatment should:
- Convey the same message
- Be more/less prominent as specified
- Fit naturally with the design

Preserve these elements exactly:
- Urgency message content
- All other elements
```

---

## Product/Subject Variations

### Product Angle Change

```
Reference image attached. This is a winning ad creative featuring a product.

Create a variation showing the product from a [NEW ANGLE]:
- [e.g., 3/4 view instead of straight-on]
- [e.g., close-up of key feature]
- [e.g., in-use context]

The product should:
- Be recognizably the same product
- Maintain the same size/prominence in the composition
- Be well-lit and clearly visible

Preserve these elements exactly:
- Background style and color
- Text content and positioning
- Overall composition structure
```

### Context Addition

```
Reference image attached. This is a winning ad creative with a product on a plain background.

Create a variation placing the product in a lifestyle context:
- Setting: [e.g., home office, kitchen counter, gym]
- Mood: [e.g., bright and energetic, calm and professional]

The context should:
- Feel authentic and aspirational
- Not compete with the product for attention
- Enhance the value proposition

Preserve these elements exactly:
- Product appearance and quality
- Text content and styling
- Brand elements
```

---

## Quality Control Prompts

### Consistency Check Addition

Add to any prompt when consistency is critical:

```
Additional requirements:
- The generated image should be indistinguishable in quality from the reference
- Match the reference's: lighting style, color grading, level of detail
- Avoid: artificial look, obvious AI artifacts, inconsistent shadows
```

### Brand Compliance Addition

Add when brand guidelines are strict:

```
Brand requirements:
- Colors must match exactly: [list hex codes]
- Font style must remain: [font description]
- Logo must be: [size/position requirements]
- No elements that conflict with brand guidelines
```

---

## Troubleshooting Prompts

### When Output Is Completely Different (Not a Variation)

**First check: Did you include `reference_file_uri` in the generate_image call?**

If you forgot to include the `reference_file_uri` parameter, Gemini generates from scratch based on the prompt alone—it has no knowledge of your control image. This is the most common cause of "variations" that look nothing like the original.

**Fix:** Ensure every `generate_image` call includes:
```
reference_file_uri: "files/[your-uploaded-file-id]"
```

### When Output Is Too Different

If variants drift too far from the reference (even with `reference_file_uri`):

```
Critical: This variant must look like a minor edit to the reference image, not a completely new design.

Only change: [specific element]

Everything else must be nearly identical to the reference:
- Same background
- Same layout
- Same colors
- Same styling
- Same composition

The viewer should think: "These are the same ad with one small difference."
```

### When Text Is Unreadable

If text comes out poorly:

```
Text quality requirements:
- All text must be perfectly sharp and readable
- Text should have consistent spacing and alignment
- If text is over an image, ensure sufficient contrast (add subtle shadow or background if needed)
- Text should look professionally designed, not AI-generated
```

### When Style Is Inconsistent

If the aesthetic doesn't match:

```
Style matching requirements:
- Match the exact aesthetic of the reference: [describe: e.g., "minimal, modern, high-end"]
- Use the same level of visual complexity
- Match the photography/illustration style
- Ensure color relationships are preserved (warm/cool balance, saturation levels)
```
