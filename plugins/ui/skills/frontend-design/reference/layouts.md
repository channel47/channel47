# Layout Patterns

Breaking the grid, creating tension, and spatial composition.

---

## The Problem with Default Layouts

AI-generated layouts converge on:
- Three-column grids with equal spacing
- Hero sections centered with gradient backgrounds
- Predictable component placement (logo top-left, CTA top-right)
- Symmetry everywhere

These are "safe" but signal "no thought went into this."

---

## Asymmetric Layouts

### The 2:1 Split

Instead of three equal columns, use unequal splits:

```css
.layout-asymmetric {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 3rem;
}

/* Or flip it */
.layout-asymmetric-reverse {
  grid-template-columns: 1fr 2fr;
}
```

### The Golden Ratio Split

```css
.layout-golden {
  display: grid;
  grid-template-columns: 1fr 1.618fr;
  gap: 2rem;
}
```

### Breaking the Container

Let content break out of the container:

```css
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
}

.breakout {
  width: 100vw;
  position: relative;
  left: 50%;
  right: 50%;
  margin-left: -50vw;
  margin-right: -50vw;
}

.breakout-partial {
  margin-left: -4rem;
  margin-right: -4rem;
}
```

---

## Grid Systems

### Flexible Grid

```css
.grid {
  display: grid;
  gap: var(--grid-gap, 1.5rem);
}

/* Column variants */
.grid-2 { grid-template-columns: repeat(2, 1fr); }
.grid-3 { grid-template-columns: repeat(3, 1fr); }
.grid-4 { grid-template-columns: repeat(4, 1fr); }

/* Auto-fit for responsive */
.grid-auto {
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 300px), 1fr));
}

/* Asymmetric grids */
.grid-1-2 { grid-template-columns: 1fr 2fr; }
.grid-2-1 { grid-template-columns: 2fr 1fr; }
.grid-1-3 { grid-template-columns: 1fr 3fr; }
```

### Masonry-Style Layout

For variable-height content:

```css
.masonry {
  columns: 3;
  column-gap: 1.5rem;
}

.masonry-item {
  break-inside: avoid;
  margin-bottom: 1.5rem;
}

/* Responsive */
@media (max-width: 768px) {
  .masonry { columns: 2; }
}

@media (max-width: 480px) {
  .masonry { columns: 1; }
}
```

---

## Spatial Rhythm

### Vertical Spacing Scale

Don't use arbitrary values. Use a scale:

```css
:root {
  --space-xs: 0.25rem;  /* 4px */
  --space-sm: 0.5rem;   /* 8px */
  --space-md: 1rem;     /* 16px */
  --space-lg: 1.5rem;   /* 24px */
  --space-xl: 2rem;     /* 32px */
  --space-2xl: 3rem;    /* 48px */
  --space-3xl: 4rem;    /* 64px */
  --space-4xl: 6rem;    /* 96px */
}
```

### Section Spacing

```css
.section {
  padding: var(--space-4xl) 0;
}

.section + .section {
  padding-top: 0; /* Collapse margins between sections */
}

/* Or use lobotomized owl */
.stack > * + * {
  margin-top: var(--space-lg);
}
```

### Generous Whitespace

Counter-intuitively, MORE whitespace = MORE premium feel:

```css
/* Generic */
.hero-generic {
  padding: 3rem 2rem;
}

/* Premium */
.hero-premium {
  padding: 8rem 4rem;
  min-height: 80vh;
}
```

---

## Hero Sections

### NOT This (Generic AI Pattern)

```css
/* ❌ The AI slop hero */
.hero-bad {
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
  text-align: center;
  padding: 4rem 2rem;
}

.hero-bad h1 {
  font-size: 48px;
  color: white;
  margin-bottom: 1rem;
}

.hero-bad p {
  color: rgba(255, 255, 255, 0.8);
  margin-bottom: 2rem;
}
```

### Alternative: Left-Aligned with Asymmetry

```css
.hero {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4rem;
  padding: 6rem 4rem;
  min-height: 80vh;
  align-items: center;
}

.hero-content {
  max-width: 600px;
}

.hero h1 {
  font-size: clamp(2.5rem, 5vw, 4rem);
  font-weight: 800;
  line-height: 1.1;
  margin-bottom: 1.5rem;
}

.hero p {
  font-size: 1.25rem;
  color: var(--color-text-secondary);
  line-height: 1.6;
  margin-bottom: 2rem;
}

.hero-visual {
  /* Image, illustration, or abstract element */
}
```

### Alternative: Full-Bleed with Overlay

```css
.hero-fullbleed {
  position: relative;
  min-height: 90vh;
  display: flex;
  align-items: flex-end;
  padding: 4rem;
}

.hero-fullbleed-bg {
  position: absolute;
  inset: 0;
  background-image: url('...');
  background-size: cover;
  background-position: center;
}

.hero-fullbleed-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, rgba(0, 0, 0, 0.7), transparent);
}

.hero-fullbleed-content {
  position: relative;
  z-index: 1;
  max-width: 600px;
  color: white;
}
```

### Alternative: Brutalist/Bold

```css
.hero-brutalist {
  padding: 8rem 4rem;
  background: var(--color-bg);
}

.hero-brutalist h1 {
  font-size: clamp(4rem, 10vw, 12rem);
  font-weight: 900;
  line-height: 0.9;
  text-transform: uppercase;
  letter-spacing: -0.03em;
}

.hero-brutalist .accent {
  display: block;
  color: var(--color-accent);
}
```

---

## Dashboard Layouts

### Sidebar + Main Content

```css
.dashboard {
  display: grid;
  grid-template-columns: 250px 1fr;
  min-height: 100vh;
}

.dashboard-sidebar {
  background: var(--color-surface);
  border-right: 1px solid var(--color-border);
  padding: 1.5rem;
  position: sticky;
  top: 0;
  height: 100vh;
  overflow-y: auto;
}

.dashboard-main {
  padding: 2rem;
  background: var(--color-bg);
}

/* Responsive: collapse sidebar */
@media (max-width: 1024px) {
  .dashboard {
    grid-template-columns: 1fr;
  }

  .dashboard-sidebar {
    position: fixed;
    left: 0;
    top: 0;
    width: 250px;
    transform: translateX(-100%);
    transition: transform 300ms var(--ease-out);
    z-index: 100;
  }

  .dashboard-sidebar.open {
    transform: translateX(0);
  }
}
```

### Stats Grid (NOT Equal Columns)

```css
/* ❌ Generic */
.stats-grid-bad {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1rem;
}

/* ✅ Hierarchy through size */
.stats-grid {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr;
  grid-template-rows: auto auto;
  gap: 1rem;
}

.stat-featured {
  grid-row: span 2;
}
```

---

## Content Layouts

### Article/Blog Layout

```css
.article {
  max-width: 65ch; /* Optimal reading width */
  margin: 0 auto;
  padding: 4rem 2rem;
}

.article h1 {
  font-size: 2.5rem;
  font-weight: 700;
  line-height: 1.2;
  margin-bottom: 1rem;
}

.article-meta {
  font-size: 0.875rem;
  color: var(--color-text-tertiary);
  margin-bottom: 3rem;
}

.article-content > * + * {
  margin-top: 1.5rem;
}

.article-content h2 {
  margin-top: 3rem;
}
```

### Feature Section (Alternating)

```css
.feature-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4rem;
  align-items: center;
  padding: 4rem 0;
}

.feature-row:nth-child(even) {
  direction: rtl; /* Flip order */
}

.feature-row:nth-child(even) > * {
  direction: ltr; /* Reset text direction */
}

/* Or use order */
.feature-row:nth-child(even) .feature-content {
  order: 2;
}
```

---

## Responsive Patterns

### Container Queries (Modern)

```css
.card-container {
  container-type: inline-size;
}

.card {
  /* Default: compact */
  display: flex;
  gap: 1rem;
  align-items: center;
}

@container (min-width: 400px) {
  .card {
    /* Expanded: stack */
    flex-direction: column;
    align-items: flex-start;
  }
}
```

### Fluid Typography

```css
h1 {
  font-size: clamp(2rem, 5vw, 4rem);
}

p {
  font-size: clamp(1rem, 2vw, 1.25rem);
}
```

### Responsive Spacing

```css
.section {
  padding: clamp(2rem, 8vw, 6rem) clamp(1rem, 4vw, 4rem);
}
```
