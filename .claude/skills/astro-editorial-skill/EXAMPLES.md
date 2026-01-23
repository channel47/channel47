# Examples Reference

## Site Breakdowns

Each breakdown identifies what makes the site work and what can be learned from it.

---

## Personal/Developer Sites to Study

These sites exemplify the craft of individual makers. They're not polished by agencies — they're considered by people who care.

### interfacecraft.dev

**The signature move**: Editorial sophistication meets playful illustration.

**What they did right:**
- **Typography**: Serif headline ("Interface Craft") creates instant editorial sophistication
- **Centered layout**: Narrow, centered content column for intimate reading
- **Illustrations**: Hand-crafted card illustrations with distinct textures (not stock or AI)
- **Hierarchy**: Clear visual levels — large headline, muted subtext, section cards
- **Voice**: The copy is confident and specific ("uncommon care"), not generic

**Key technique**: The serif headline + card illustrations combination feels distinctly crafted and human.

### nan.fyi

**The signature move**: Hand-drawn illustrations as identity.

**What they did right:**
- **Illustrations**: Hand-drawn, sketch-like images for each post create personality
- **Typography**: Serif headlines with comfortable body text
- **Two-column layout**: Sidebar with bio, main content with post list — clean separation
- **Content-first**: The interactive blog posts ARE the design — no decoration competes
- **Neutral palette**: Light background, dark text, minimal color — lets illustrations shine

**Key technique**: The hand-drawn illustrations give each post a distinctive identity. They signal "made by a human who cares" without trying too hard.

### nexxel.dev

**The signature move**: Monospace font as identity.

**What they did right:**
- **Typography as identity**: Monospace throughout signals "developer" without explanation
- **Dark-first**: Deep blacks with considered gray hierarchy (white headings, gray-400 dates, gray-500 descriptions)
- **Keyboard shortcuts**: `[h] home [b] blog [p] projects` — terminal-like navigation reinforces the developer aesthetic
- **Sections**: Clear `* work`, `* blog`, `* projects` markers with asterisk prefix
- **Lowercase**: All lowercase text creates a casual, personal tone

**Key technique**: The monospace choice isn't decoration — it's identity. Everything follows from that single decision.

```css
body {
  font-family: 'JetBrains Mono', monospace;
  background: #0a0a0a;
  color: #fafafa;
}
```

### makingsoftware.com

**The signature move**: Technical blueprint aesthetic for technical content.

**What they did right:**
- **Typography**: Pixel/retro-style headline font creates immediate distinction
- **Illustrations**: Blueprint-style technical diagrams (isometric, schematic) match the "how things work" content
- **Two-column layout**: Text and figures flow together like a technical manual
- **Personality**: Figure labels ("FIG_001"), copyright dates ("© 1986"), retro references
- **Blue-on-white**: Consistent blueprint blue for all illustrations creates cohesion

**Key technique**: The aesthetic perfectly matches the content. A book about how software works looks like a technical manual — form follows function.

---

## Linear (linear.app)

### What They Did Right

**Palette**: Pure dark mode execution
- Near-black backgrounds (#0a0a0b)
- Pure white text for headlines
- Muted grays for secondary content
- Accent blue used only for CTAs and interactive states

**Typography**: Restrained excellence
- Single sans-serif family throughout
- Massive headline scale (60-80px)
- Tight letter-spacing on display text
- Consistent hierarchy across all pages

**Animation**: Purposeful motion
- Orchestrated page load reveals
- Subtle gradient animations in backgrounds
- Smooth transitions between states
- No decorative animation

**Layout**: Editorial density
- Generous whitespace
- Full-bleed imagery
- Asymmetric grid breaks
- Content sections that breathe

### Key Takeaway

Linear proves you can build an entire marketing site with essentially three colors (black, white, blue) if you get typography and spacing right.

---

## Gumroad (gumroad.com)

### What They Did Right

**Palette**: Playful but not childish
- Pink as a confident accent
- Black text on light backgrounds
- Illustrated elements add personality without clutter

**Typography**: Bold and direct
- Heavy weights for headlines
- Comfortable body text sizing
- Short, punchy copy

**Illustration**: Hand-drawn personality
- Sketched elements feel human
- Coins, arrows, and decorative bits
- Never generic stock illustration

**Layout**: Flowing narrative
- Scrolling tells a story
- Varied section treatments
- Testimonials feel natural, not templated

### Key Takeaway

Gumroad shows that "editorial" doesn't mean "serious." Personality can come through illustration and copy while maintaining design rigor.

---

## Nothing (us.nothing.tech)

### What They Did Right

**Palette**: Extreme minimalism
- Black and white only
- Product images provide all color
- No accent color at all

**Typography**: Product is the content
- Minimal text
- Headlines serve to introduce product
- Copy stays out of the way

**Photography**: Architectural precision
- Products shot like sculptures
- Consistent lighting treatment
- Images do the heavy lifting

**Layout**: Full-bleed confidence
- Product images fill the viewport
- Near-zero ornamentation
- White space is the design

### Key Takeaway

Nothing proves that sometimes the best design is no design. When your product is beautiful, get out of its way.

---

## Stripe Sessions (stripesessions.com)

### What They Did Right

**Palette**: Warm and elevated
- Cream/warm white backgrounds
- Deep charcoals for text
- Subtle warm tones throughout
- Limited accent usage

**Typography**: Conference appropriate
- Large, confident headlines
- Clear event information hierarchy
- Date/location always prominent

**Photography**: Professional and human
- Real speaker photos
- Consistent cropping and treatment
- Warm color grading

**Layout**: Event-focused
- Key information above fold
- Clear CTA for registration
- Agenda easy to scan

### Key Takeaway

Stripe Sessions shows how to do warm and premium without becoming generic or "corporate." The restrained palette elevates rather than decorates.

---

## Hyperframe (hyperframe.ai)

### What They Did Right

**Palette**: Soft editorial
- Light backgrounds
- Muted colors throughout
- Video content provides visual interest

**Typography**: Clear hierarchy
- Strong headlines
- Readable body copy
- Professional but not cold

**Content Strategy**: Video-first
- Product demos are central
- Visual proof over claims
- Features shown, not told

**Layout**: Functional clarity
- Problem → Solution flow
- Easy to understand value prop
- Social proof positioned well

### Key Takeaway

Hyperframe demonstrates editorial restraint in the B2B SaaS space. The site trusts its product videos to do the selling.

---

## Channel47 (channel47.dev) — Current State Analysis

### What Works

**Copy**: Strong conceptual hook
- "Same tools. Different outcomes."
- Creates tension and curiosity
- Sets up a clear value proposition

**Typography**: Editorial direction
- Large, confident headline
- Minimal supporting text
- Typography-first approach

### What Could Improve

**Visual Identity**: Needs distinctive character
- No clear color system yet
- Missing the "one distinctive move"
- Background treatment could be bolder

**Hierarchy**: Could be sharper
- Email capture could be more prominent
- Supporting text could have clearer levels
- CTA needs more visual weight

**Animation**: Could add polish
- Page load reveal would add quality
- Subtle motion could reinforce "different"
- Currently feels static

### Recommendations

1. **Choose a distinctive color moment** — even one accent used surgically
2. **Add typographic contrast** — the headline is good but could be bigger
3. **Consider a texture or pattern** — subtle grain or geometric could add depth
4. **Orchestrate the entrance** — staggered reveals would elevate perception

---

## Patterns Across All Examples

### What the best sites share:

1. **Typography leads** — Every great editorial site starts with type
2. **Color restraint** — Maximum 3 colors, usually 2
3. **Whitespace confidence** — They're not afraid of emptiness
4. **Content-first** — Design serves the message
5. **One signature move** — Something memorable and intentional
6. **Narrow content columns** — 540-700px for reading, not edge-to-edge
7. **Fast, subtle animation** — 150-250ms, ease-out, orchestrated reveals

### What none of them have:

1. Purple gradients on white
2. Three-column icon feature grids
3. Generic stock photography
4. Gradient buttons
5. "Learn more →" on everything
6. Decorative animation
7. Timid type scales (18px, 20px, 24px increments)
8. Multiple competing accent colors
9. Hero → Features → Testimonials → CTA template order
10. "At [Company], we believe..." copy
11. Uniform padding throughout

---

## How to Use These References

When building a new page:

1. **Identify the closest analog** — Which reference site shares your mood?
2. **Study their restraint** — What did they NOT include?
3. **Note their signature** — What's the one memorable thing?
4. **Adapt, don't copy** — Use principles, not pixels

When reviewing your work:

1. **Compare to references** — Does your page have the same confidence?
2. **Check for slop** — Are you using any anti-patterns?
3. **Test the squint** — Does the hierarchy read at 25% zoom?
4. **Verify restraint** — Can you remove anything?
