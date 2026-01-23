# Typography Reference

## The Philosophy

Typography is the skeleton of editorial design. A site can have mediocre color and still work. It cannot have mediocre type.

The best editorial sites feel like they chose their typeface first and built everything else around it.

---

## Font Pairing Strategies

### Strategy 1: Single Family

Use one typeface across all weights and sizes. The simplest and often most effective approach.

**When to use**: Technical products, developer tools, minimalist brands

**Examples**:
- Linear uses a single sans-serif throughout
- Stripe uses their custom font across all contexts

**Implementation**:
```css
:root {
  --font-display: 'Söhne', system-ui, sans-serif;
  --font-body: 'Söhne', system-ui, sans-serif;
  --font-mono: 'Söhne Mono', ui-monospace, monospace;
}
```

### Strategy 2: Serif Display + Sans Body

The classic editorial pairing. Creates immediate sophistication.

**When to use**: Media sites, luxury brands, content-heavy platforms

**Proven pairs**:
- Playfair Display + Source Sans Pro
- Fraunces + Inter (Inter ONLY as body, never display)
- GT Sectra + Suisse Intl
- Canela + Söhne

**Implementation**:
```css
:root {
  --font-display: 'Playfair Display', Georgia, serif;
  --font-body: 'Source Sans 3', system-ui, sans-serif;
}

.headline {
  font-family: var(--font-display);
  font-weight: 700;
  letter-spacing: -0.02em;
}

.body {
  font-family: var(--font-body);
  font-weight: 400;
}
```

### Strategy 3: Sans Display + Serif Body

Inverted classic. Creates tension and sophistication.

**When to use**: Fashion, art direction, brand differentiation

**Proven pairs**:
- Clash Display + Newsreader
- Cabinet Grotesk + Crimson Pro
- Satoshi + Libre Baskerville

### Strategy 4: Mono + Sans

Technical, developer-focused, precise.

**When to use**: Dev tools, technical products, code-adjacent brands

**Proven pairs**:
- JetBrains Mono + Inter
- Fira Code + Fira Sans
- Space Grotesk (works as both)

---

## The Type Scale

### The Problem with Default Scales

Most scales increment too gradually:
```
14px → 16px → 18px → 20px → 24px → 30px → 36px
```

This creates visual monotony. Nothing dominates. Nothing recedes.

### The Editorial Scale

Use **exponential jumps**:
```
12px → 14px → 16px → 20px → 32px → 48px → 72px → 96px
```

The goal: your headline should be **4-6x** your body size.

### Implementing the Scale

```css
:root {
  /* Base scale using clamp for responsiveness */
  --text-xs: clamp(0.7rem, 0.65rem + 0.25vw, 0.75rem);
  --text-sm: clamp(0.8rem, 0.75rem + 0.25vw, 0.875rem);
  --text-base: clamp(0.95rem, 0.9rem + 0.25vw, 1rem);
  --text-lg: clamp(1.1rem, 1rem + 0.5vw, 1.25rem);
  --text-xl: clamp(1.4rem, 1.2rem + 1vw, 2rem);
  --text-2xl: clamp(1.8rem, 1.5rem + 1.5vw, 3rem);
  --text-3xl: clamp(2.5rem, 2rem + 2.5vw, 4.5rem);
  --text-4xl: clamp(3rem, 2.5rem + 3vw, 6rem);
}
```

---

## Line Height Guidelines

Line height varies with size:

| Size | Line Height | Use Case |
|------|-------------|----------|
| 12-14px | 1.5-1.6 | Captions, metadata |
| 16-18px | 1.5-1.6 | Body text |
| 20-24px | 1.4-1.5 | Large body, subtitles |
| 32-48px | 1.2-1.3 | Subheadings |
| 48-72px | 1.05-1.15 | Headlines |
| 72px+ | 0.95-1.05 | Hero display |

**Rule**: As type gets larger, line height gets tighter.

---

## Letter Spacing

### Display Type (32px+)

Large type needs **negative** letter-spacing:
```css
.display {
  letter-spacing: -0.02em;  /* Subtle */
  letter-spacing: -0.03em;  /* Standard for headlines */
  letter-spacing: -0.04em;  /* Tight, dramatic */
}
```

### Body Type (14-20px)

Usually `0` or very subtle tracking:
```css
.body {
  letter-spacing: 0;  /* Most fonts */
  letter-spacing: 0.01em;  /* If font runs tight */
}
```

### Small Caps / Labels (10-12px)

Small text often benefits from **positive** tracking:
```css
.label {
  font-size: 0.75rem;
  letter-spacing: 0.05em;
  text-transform: uppercase;
}
```

---

## Practical Typography Components

### Headline Component

```astro
---
interface Props {
  level?: 1 | 2 | 3 | 4 | 5;
  size?: 'display' | 'headline' | 'title' | 'subtitle';
  class?: string;
}

const { level = 1, size = 'headline', class: className } = Astro.props;
const Tag = `h${level}` as any;

const sizeClasses = {
  display: 'text-4xl md:text-5xl font-medium tracking-tight leading-none',
  headline: 'text-2xl md:text-3xl font-medium tracking-tight leading-tight',
  title: 'text-xl md:text-2xl font-medium tracking-snug leading-snug',
  subtitle: 'text-lg md:text-xl font-normal leading-relaxed',
};
---

<Tag class:list={[sizeClasses[size], className]}>
  <slot />
</Tag>

<style>
  .tracking-tight { letter-spacing: -0.03em; }
  .tracking-snug { letter-spacing: -0.02em; }
</style>
```

### Body Text Component

```astro
---
interface Props {
  size?: 'sm' | 'base' | 'lg';
  muted?: boolean;
  class?: string;
}

const { size = 'base', muted = false, class: className } = Astro.props;

const sizeClasses = {
  sm: 'text-sm leading-relaxed',
  base: 'text-base leading-relaxed',
  lg: 'text-lg leading-relaxed',
};
---

<p class:list={[
  sizeClasses[size],
  muted && 'text-muted',
  className
]}>
  <slot />
</p>

<style>
  p {
    max-width: 65ch;
  }
  .text-muted {
    color: var(--text-secondary);
  }
</style>
```

---

## Responsive Typography

### The clamp() Approach

Instead of breakpoint-based sizes, use fluid scaling:

```css
.hero-headline {
  font-size: clamp(2.5rem, 5vw + 1rem, 6rem);
}
```

This gives you:
- Minimum: 2.5rem (40px) on small screens
- Fluid scaling in the middle
- Maximum: 6rem (96px) on large screens

### When to Use Breakpoints

Use breakpoints for **structural changes**, not size tweaks:

```css
/* Font size: use clamp */
.headline {
  font-size: clamp(2rem, 4vw + 1rem, 4rem);
}

/* Line breaks: use breakpoints */
@media (min-width: 768px) {
  .headline br {
    display: none; /* Remove mobile line breaks */
  }
}
```

---

## Font Loading Strategy

### The Approach

1. **Subset fonts** — Only include characters you need
2. **Preload critical fonts** — The display font used above the fold
3. **Use font-display: swap** — Show fallback immediately

```html
<!-- In BaseLayout.astro <head> -->
<link 
  rel="preload" 
  href="/fonts/display-font.woff2" 
  as="font" 
  type="font/woff2" 
  crossorigin
/>

<style>
  @font-face {
    font-family: 'Display Font';
    src: url('/fonts/display-font.woff2') format('woff2');
    font-weight: 500;
    font-display: swap;
  }
</style>
```

### Fallback Stacks

Always include quality fallbacks:

```css
:root {
  /* Serif fallback */
  --font-serif: 'Your Serif', Georgia, 'Times New Roman', serif;
  
  /* Sans fallback with metrics-matched system fonts */
  --font-sans: 'Your Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  
  /* Mono fallback */
  --font-mono: 'Your Mono', ui-monospace, 'Cascadia Code', 'Fira Code', monospace;
}
```

---

## Common Mistakes

### 1. Using Inter for Display Text

Inter is an excellent UI font at small sizes. It's generic and forgettable at display sizes.

**Fix**: Keep Inter for body/UI only. Use something distinctive for headlines.

### 2. Not Adjusting for Optical Size

Large text and small text have different needs. A font that looks great at 16px may look wrong at 72px.

**Fix**: Some fonts have optical size variants (Display, Text, Caption). Use them.

### 3. Ignoring Vertical Rhythm

Random spacing between text elements creates visual noise.

**Fix**: Use consistent spacing tokens. Usually `1.5em` or `2em` between paragraphs.

### 4. Over-styling Links

Links don't need to be a different color, underlined, AND bold.

**Fix**: Pick one treatment. Usually underline or color, not both.

---

## Quick Reference: Editorial Type Stacks

### Developer/Technical
```css
--font-display: 'Space Grotesk', 'JetBrains Mono', sans-serif;
--font-body: 'Space Grotesk', system-ui, sans-serif;
```

### Editorial/Magazine
```css
--font-display: 'Playfair Display', Georgia, serif;
--font-body: 'Source Serif 4', Georgia, serif;
```

### Startup/Modern
```css
--font-display: 'Cabinet Grotesk', 'Satoshi', sans-serif;
--font-body: 'Cabinet Grotesk', system-ui, sans-serif;
```

### Luxury/Minimal
```css
--font-display: 'Canela', 'Didot', serif;
--font-body: 'Söhne', 'Helvetica Neue', sans-serif;
```

### Bold/Confident
```css
--font-display: 'Clash Display', 'Impact', sans-serif;
--font-body: 'Satoshi', system-ui, sans-serif;
```
