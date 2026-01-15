# Anti-Patterns

What to avoid — the "AI slop" checklist.

---

## The Problem

AI-generated frontends tend to converge on safe, generic choices. This creates a recognizable "AI aesthetic" that signals "no human thought went into this."

Distinctive design requires intentional choices, not defaults.

---

## The Checklist

Before shipping, verify NONE of these apply:

### Typography
- [ ] Using Inter, Roboto, Open Sans, or system fonts as primary
- [ ] All text at similar sizes (weak hierarchy)
- [ ] Font weights only 400 and 600 (use extremes: 300 vs 800)
- [ ] Generic sans-serif everywhere (no personality)

### Color
- [ ] Purple/violet gradient on white background (THE #1 tell)
- [ ] Blue as primary with no secondary consideration
- [ ] Evenly-distributed rainbow palette (too many hues)
- [ ] Gray-on-gray with no accent color
- [ ] Pure black (#000) on pure white (#fff)

### Layout
- [ ] Three-column card grid with equal spacing
- [ ] Hero section with centered text and gradient background
- [ ] Identical border-radius on every element
- [ ] No asymmetry or visual tension anywhere
- [ ] Predictable component placement (logo top-left, CTA top-right)

### Motion
- [ ] Micro-interactions on everything
- [ ] Bouncing/pulsing call-to-action buttons
- [ ] Auto-playing carousels
- [ ] Fade-in on scroll for every element
- [ ] No motion at all (equally generic)

### Imagery
- [ ] Generic stock photos of people shaking hands
- [ ] Abstract 3D blob shapes
- [ ] Gradient mesh backgrounds
- [ ] Illustrations in "corporate Memphis" style

### Components
- [ ] Cards with drop shadows AND rounded corners AND borders
- [ ] Buttons with too many states (gradient + shadow + border + icon)
- [ ] Forms with placeholder text as labels
- [ ] Modals for everything

---

## Why These Fail

Generic choices signal:
- "I didn't think about this"
- "I went with the first suggestion"
- "I optimized for safety, not impact"

Distinctive choices signal:
- "I made an intentional decision"
- "I understand the context"
- "I care about craft"

---

## The Fix

For each anti-pattern, ask: **"What would a human designer with taste do differently?"**

### Instead of Inter
→ Pick a font that matches the brand personality. Technical product? Try Space Grotesk. Luxury? Try Cormorant. Startup? Try Satoshi.

### Instead of purple gradient
→ Commit to ONE hero color. Derive palette from it. Let it dominate.

### Instead of three-column grid
→ Try asymmetry. Try two columns with different widths. Try a single column with generous margins.

### Instead of micro-interactions everywhere
→ Pick ONE moment to delight. Make it count. Everything else should be invisible.

---

## The Meta-Rule

**If you've seen it in 10 other AI-generated sites, don't use it.**

Distinctive design requires going against the distribution, not with it.
