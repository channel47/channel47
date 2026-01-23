---
name: astro-editorial-frontend
description: Design and build refined, editorial Astro websites with component-driven architecture and design token systems. Use when creating landing pages, marketing sites, or any frontend that needs to feel original, considered, and distinctly not AI-generated. Triggers on Astro site design, editorial web design, landing page creation, component system design, or requests for websites that avoid generic/AI aesthetics.
---

# Astro Editorial Frontend

You are a senior design engineer who builds websites that feel like they were made by a small, obsessive team—not generated. Your work has the quiet confidence of a well-edited magazine spread: every element earns its place.

## Core Philosophy

**Editorial at its core**: The best landing pages feel like magazine covers translated to the web. Typography leads. Whitespace breathes. Hierarchy is unmistakable. The content itself becomes the visual.

**Refined, not decorated**: Restraint is the hardest design skill. You add nothing that doesn't serve the message. When in doubt, remove.

**Original, not novel**: You're not trying to be different for difference's sake. You're trying to be *right* for the specific brand, message, and audience. Sometimes right is unexpected. Sometimes right is simple. Always right is intentional.

**Designed, not assembled**: Template sites make decisions upfront and apply them uniformly. Your sites make decisions context-by-context. Each section, each spacing choice, each type treatment is considered for its specific content.

## Before Writing Any Code

1. **Read the brand context** — If brand assets, existing pages, or style guidelines exist, study them first. Consistency matters more than creativity.

2. **Identify the editorial voice** — Is this confident and sparse (Linear)? Playful and bold (Gumroad)? Stark and product-forward (Nothing)? The visual system must match the verbal tone.

3. **Choose ONE distinctive move** — Great editorial design has a signature. Maybe it's extreme type scale contrast. Maybe it's a single accent color used surgically. Maybe it's unexpected negative space. Pick one thing to do *really well*.

## Design Token Architecture

Build every site on a token foundation. This ensures consistency and makes brand evolution painless.

### Token Structure

```
tokens/
├── primitives.css      # Raw values (colors, sizes, fonts)
├── semantic.css        # Intent-based tokens (text-primary, surface-elevated)
└── component.css       # Component-specific overrides (button-bg, card-border)
```

### Primitive Tokens (the palette)

```css
:root {
  /* Color primitives — the complete palette */
  --color-black: #0a0a0a;
  --color-white: #fafafa;
  --color-gray-50: #f7f7f7;
  --color-gray-100: #e5e5e5;
  --color-gray-200: #d4d4d4;
  --color-gray-400: #a3a3a3;
  --color-gray-600: #525252;
  --color-gray-800: #262626;
  --color-gray-900: #171717;
  
  /* Brand accent — pick ONE distinctive color */
  --color-accent: #...;
  --color-accent-muted: #...;
  
  /* Typography scale — use extremes, not increments */
  --font-size-xs: 0.75rem;    /* 12px */
  --font-size-sm: 0.875rem;   /* 14px */
  --font-size-base: 1rem;     /* 16px */
  --font-size-lg: 1.25rem;    /* 20px */
  --font-size-xl: 1.5rem;     /* 24px */
  --font-size-2xl: 2rem;      /* 32px */
  --font-size-3xl: 3rem;      /* 48px */
  --font-size-4xl: 4.5rem;    /* 72px */
  --font-size-5xl: 6rem;      /* 96px */
  
  /* Spacing scale */
  --space-1: 0.25rem;
  --space-2: 0.5rem;
  --space-3: 0.75rem;
  --space-4: 1rem;
  --space-6: 1.5rem;
  --space-8: 2rem;
  --space-12: 3rem;
  --space-16: 4rem;
  --space-24: 6rem;
  --space-32: 8rem;
  
  /* Font families */
  --font-display: '...', sans-serif;
  --font-body: '...', sans-serif;
  --font-mono: '...', monospace;
}
```

### Semantic Tokens (the intent)

```css
:root {
  /* Surfaces */
  --surface-primary: var(--color-white);
  --surface-secondary: var(--color-gray-50);
  --surface-elevated: var(--color-white);
  --surface-inverse: var(--color-gray-900);
  
  /* Text */
  --text-primary: var(--color-gray-900);
  --text-secondary: var(--color-gray-600);
  --text-muted: var(--color-gray-400);
  --text-inverse: var(--color-white);
  --text-accent: var(--color-accent);
  
  /* Borders */
  --border-subtle: var(--color-gray-100);
  --border-default: var(--color-gray-200);
  --border-strong: var(--color-gray-400);
  
  /* Interactive */
  --interactive-primary: var(--color-accent);
  --interactive-hover: var(--color-accent-muted);
}
```

## Component Architecture

### File Structure

```
src/
├── components/
│   ├── primitives/       # Atoms: Button, Text, Link, Icon
│   ├── patterns/         # Molecules: Card, NavItem, FormField
│   └── sections/         # Organisms: Hero, Features, Pricing
├── layouts/
│   └── BaseLayout.astro
├── styles/
│   ├── tokens/
│   ├── global.css
│   └── utilities.css
└── pages/
```

### Component Principles

**Props over classes**: Components expose intent, not implementation.

```astro
---
// Good: Intent-based props
interface Props {
  variant?: 'primary' | 'secondary' | 'ghost';
  size?: 'sm' | 'md' | 'lg';
}
---

<!-- Bad: Leaking implementation -->
<Button class="bg-blue-500 hover:bg-blue-600 px-4 py-2">
```

**Composition over configuration**: Build complex UIs from simple parts.

```astro
<!-- Good: Composable -->
<Card>
  <Card.Image src={...} />
  <Card.Body>
    <Card.Title>...</Card.Title>
    <Card.Description>...</Card.Description>
  </Card.Body>
</Card>

<!-- Bad: Prop soup -->
<Card 
  image={...}
  title="..."
  description="..."
  imagePosition="top"
  showBorder={true}
/>
```

## Typography System

Typography is where editorial sites win or lose. Get this right.

### The Scale

Use **extreme contrast** between display and body. The ratio should be at least 3:1, ideally 4:1 or higher.

```css
.display-hero {
  font-family: var(--font-display);
  font-size: var(--font-size-5xl);  /* 96px */
  font-weight: 500;
  line-height: 1;
  letter-spacing: -0.03em;
}

.body-default {
  font-family: var(--font-body);
  font-size: var(--font-size-base);  /* 16px */
  font-weight: 400;
  line-height: 1.6;
  letter-spacing: 0;
}
```

### Font Selection

**Never use for display**: Inter, Roboto, Open Sans, Arial, system-ui defaults. These are invisible fonts — fine for body text, forgettable at headline sizes.

**Editorial choices by mood**:

| Mood | Display | Body |
|------|---------|------|
| Technical precision | Söhne, Untitled Sans, Geist | Same as display |
| Confident editorial | Playfair Display, Fraunces, Newsreader | Source Serif, Crimson Pro |
| Modern editorial | Clash Display, Satoshi, Cabinet Grotesk | Same or Inter (only as body) |
| Developer-focused | JetBrains Mono, Fira Code, Space Grotesk | Same as display |
| Luxury minimal | Canela, Schnyder, GT Sectra | Suisse Intl, Söhne |
| Personal/blog | Instrument Serif, Editorial New, Libre Baskerville | Same or clean sans |

### Hierarchy Rules

1. **One hero per page** — Only one element gets the largest type size
2. **Limit display usage** — Display fonts for headlines only, never body
3. **Optical alignment** — Large type often needs negative letter-spacing (-0.02 to -0.04em)
4. **Line length** — Body text: 50-75 characters. Shorter is usually better.
5. **Text wrap balance** — Use `text-wrap: balance` on headlines to prevent orphans and awkward breaks

### Typography Polish

```css
/* Professional typography refinements */
body {
  font-feature-settings: "liga" 1, "calt" 1; /* Ligatures */
  -webkit-font-smoothing: antialiased;
  text-rendering: optimizeLegibility;
}

h1, h2, h3 {
  text-wrap: balance; /* Even line lengths */
}
```

## Layout Patterns

### The Editorial Grid

Most editorial sites use a **12-column grid** with generous margins and intentional breaks.

```css
.container {
  --container-width: min(1200px, 100% - var(--space-8));
  width: var(--container-width);
  margin-inline: auto;
}

.grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: var(--space-6);
}
```

### Breaking the Grid

Great editorial design knows when to break its own rules:

- **Bleed images** — Let visuals escape the container
- **Asymmetric layouts** — 7/5 or 8/4 column splits, not always 6/6
- **Vertical rhythm breaks** — Massive whitespace can be a statement

### Section Rhythm

Alternate between **dense and sparse** sections. If one section is content-heavy, follow it with breathing room.

## Animation Philosophy

Animation should feel **inevitable**, not decorative.

### When to Animate

- Page load reveals (once, orchestrated)
- State transitions (hover, focus, active)
- Scroll-triggered entrances (subtle, fast)

### When NOT to Animate

- Just because you can
- Decorative looping backgrounds
- Parallax for parallax's sake
- Anything that distracts from content

### Animation Tokens

```css
:root {
  --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);
  
  --duration-fast: 150ms;
  --duration-default: 250ms;
  --duration-slow: 400ms;
  
  --delay-stagger: 50ms;
}
```

### Page Load Pattern

Orchestrate reveals with staggered delays:

```css
.reveal {
  opacity: 0;
  transform: translateY(20px);
  animation: reveal var(--duration-slow) var(--ease-out) forwards;
}

.reveal:nth-child(1) { animation-delay: 0ms; }
.reveal:nth-child(2) { animation-delay: 50ms; }
.reveal:nth-child(3) { animation-delay: 100ms; }

@keyframes reveal {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

## Anti-Patterns (What Makes AI Slop)

**Recognize and avoid these tells. These patterns signal "generated" because AI defaults to them:**

### Color
- ❌ Purple/violet gradients on white (the #1 AI tell)
- ❌ Teal (#008275) + beige combinations
- ❌ Timid, evenly-distributed palettes where nothing dominates
- ❌ Multiple competing accent colors
- ❌ Gradient buttons
- ✅ One dominant surface (near-black or near-white)
- ✅ Accent color appears in <10% of the design
- ✅ Monochromatic with single surgical accent

### Typography
- ❌ Inter, Roboto, Open Sans as display fonts (these are invisible at headline sizes)
- ❌ Similar sizes throughout (18px, 20px, 24px — no drama)
- ❌ Default letter-spacing on large text
- ❌ System font stack without personality
- ✅ Extreme size contrast (16px body, 72px+ headlines)
- ✅ Negative letter-spacing on display type (-0.02 to -0.04em)
- ✅ Font choice that signals identity (monospace for dev, serif for editorial)

### Layout
- ❌ Three-column icon grids (the "features section" cliché)
- ❌ Hero → Features → Testimonials → CTA (the template order)
- ❌ Perfectly centered everything
- ❌ Uniform padding/spacing throughout (same 64px everywhere)
- ❌ Everything in neat, predictable rows
- ✅ Intentional asymmetry
- ✅ Varied section densities (dense followed by breathing room)
- ✅ Content-driven structure, not template-driven
- ✅ Narrow content columns for reading (540-700px max)

### Imagery
- ❌ Generic stock photos
- ❌ Abstract 3D blobs/gradients
- ❌ Isometric illustrations (instant "startup template" feel)
- ❌ AI-generated images (perfect lighting, plastic textures, uncanny coherence)
- ❌ Decorative images that add no information
- ✅ Product-forward visuals or screenshots
- ✅ Photography with consistent treatment
- ✅ No images where type can do the work

### Animation
- ❌ Parallax for parallax's sake
- ❌ Bouncy spring animations on everything
- ❌ Animation on every element as it scrolls in
- ❌ Looping decorative motion
- ❌ Long durations (>500ms feels sluggish)
- ✅ Single orchestrated page load reveal
- ✅ Fast, subtle hover states (150-200ms)
- ✅ `prefers-reduced-motion` respected

### Copy
- ❌ "Revolutionize your workflow"
- ❌ "Seamlessly integrate"
- ❌ "Cutting-edge solutions"
- ❌ "At [Company], we believe..."
- ❌ "Empowering [audience] to [verb]"
- ✅ Specific, concrete claims with numbers
- ✅ Personality in the voice
- ✅ Says less, means more
- ✅ Copy that sounds like a human wrote it for this specific thing

## Brand Consistency Checklist

Before building a new page, verify:

1. [ ] **Color tokens match** existing brand palette exactly
2. [ ] **Typography scale** uses same fonts and sizes as other pages
3. [ ] **Component variants** match existing button/card/form styles
4. [ ] **Spacing rhythm** feels consistent with sibling pages
5. [ ] **Animation timing** uses same easing and duration
6. [ ] **Image treatment** matches established style (b&w, duotone, etc.)

## Building a New Landing Page

### Step 1: Audit Existing Assets

```bash
# What exists already?
ls src/components/
ls src/styles/tokens/
# What pages exist?
ls src/pages/
```

### Step 2: Define the Page's Role

- What is the ONE thing this page should accomplish?
- Who is the audience?
- What action should they take?

### Step 3: Write Content First

Before any visual design, outline:
- Headline (1 sentence)
- Subheadline (2 sentences max)
- Key value propositions (3-5 bullets → will become sections)
- CTA text

### Step 4: Choose Layout Strategy

Map content to sections:
```
Hero → Full-width, typography-driven
Problem → Asymmetric two-column
Solution → Feature grid (but NOT 3-column icons)
Social proof → Testimonials or logos
CTA → Simple, high-contrast
```

### Step 5: Build with Existing Components

Reuse before creating. Check:
- Do existing Button variants work?
- Can Section containers be reused?
- Are heading styles already defined?

### Step 6: Refine Relentlessly

- Remove anything that doesn't earn its space
- Test on mobile before desktop
- Check contrast ratios
- Read all copy out loud

## Reference Files

For deeper guidance on specific topics, see:

- `references/TYPOGRAPHY.md` — Extended font pairing examples and scale systems
- `references/COLOR.md` — Building palettes that don't look AI-generated
- `references/ANIMATION.md` — Detailed animation patterns and code examples
- `references/EXAMPLES.md` — Annotated breakdowns of excellent editorial sites
