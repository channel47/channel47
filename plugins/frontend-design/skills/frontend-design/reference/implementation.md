# Implementation Patterns

CSS architecture, theming, responsive design, and production considerations.

---

## CSS Architecture

### Custom Properties Structure

Every project should define a consistent token structure:

```css
:root {
  /* === Typography === */
  --font-display: 'Space Grotesk', sans-serif;
  --font-body: 'IBM Plex Sans', sans-serif;
  --font-mono: 'JetBrains Mono', monospace;

  --font-size-xs: 0.75rem;
  --font-size-sm: 0.875rem;
  --font-size-base: 1rem;
  --font-size-lg: 1.125rem;
  --font-size-xl: 1.25rem;
  --font-size-2xl: 1.5rem;
  --font-size-3xl: 2rem;
  --font-size-4xl: 3rem;

  --font-weight-light: 300;
  --font-weight-normal: 400;
  --font-weight-medium: 500;
  --font-weight-bold: 700;
  --font-weight-black: 900;

  --line-height-tight: 1.15;
  --line-height-normal: 1.5;
  --line-height-relaxed: 1.75;

  /* === Colors === */
  --color-bg: #fafafa;
  --color-surface: #ffffff;
  --color-surface-elevated: #ffffff;

  --color-text-primary: #171717;
  --color-text-secondary: #525252;
  --color-text-tertiary: #a3a3a3;

  --color-accent: #f97316;
  --color-accent-hover: #ea580c;
  --color-accent-subtle: #fff7ed;

  --color-success: #22c55e;
  --color-warning: #eab308;
  --color-error: #ef4444;

  --color-border: #e5e5e5;
  --color-border-strong: #d4d4d4;

  /* === Spacing === */
  --space-1: 0.25rem;
  --space-2: 0.5rem;
  --space-3: 0.75rem;
  --space-4: 1rem;
  --space-5: 1.25rem;
  --space-6: 1.5rem;
  --space-8: 2rem;
  --space-10: 2.5rem;
  --space-12: 3rem;
  --space-16: 4rem;
  --space-20: 5rem;
  --space-24: 6rem;

  /* === Effects === */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-full: 9999px;

  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
  --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1);

  /* === Motion === */
  --duration-instant: 100ms;
  --duration-fast: 150ms;
  --duration-normal: 200ms;
  --duration-slow: 300ms;
  --duration-slower: 500ms;

  --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-in: cubic-bezier(0.7, 0, 0.84, 0);
  --ease-in-out: cubic-bezier(0.87, 0, 0.13, 1);
  --ease-out-back: cubic-bezier(0.34, 1.56, 0.64, 1);
}
```

### Component Scoping

Use BEM-like naming or data attributes for state:

```css
/* Block */
.button { }

/* Element */
.button__icon { }
.button__label { }

/* Modifier via data attribute (preferred) */
.button[data-variant="primary"] { }
.button[data-variant="secondary"] { }
.button[data-size="sm"] { }
.button[data-size="lg"] { }

/* State */
.button[data-loading="true"] { }
.button:disabled { }
```

---

## Dark Mode

### System Preference Detection

```css
@media (prefers-color-scheme: dark) {
  :root {
    --color-bg: #0a0a0a;
    --color-surface: #171717;
    --color-surface-elevated: #262626;

    --color-text-primary: #fafafa;
    --color-text-secondary: #a3a3a3;
    --color-text-tertiary: #525252;

    --color-border: #262626;
    --color-border-strong: #404040;

    /* Accent may need adjustment for contrast */
    --color-accent-subtle: #431407;
  }
}
```

### Manual Toggle Support

```css
/* Light mode explicit */
[data-theme="light"] {
  --color-bg: #fafafa;
  /* ... light colors */
}

/* Dark mode explicit */
[data-theme="dark"] {
  --color-bg: #0a0a0a;
  /* ... dark colors */
}

/* System default (no data-theme attribute) */
@media (prefers-color-scheme: dark) {
  :root:not([data-theme]) {
    --color-bg: #0a0a0a;
    /* ... dark colors */
  }
}
```

### Toggle Implementation

```typescript
function ThemeToggle() {
  const [theme, setTheme] = useState<'light' | 'dark' | 'system'>('system');

  useEffect(() => {
    const root = document.documentElement;
    if (theme === 'system') {
      root.removeAttribute('data-theme');
    } else {
      root.setAttribute('data-theme', theme);
    }
    localStorage.setItem('theme', theme);
  }, [theme]);

  useEffect(() => {
    const saved = localStorage.getItem('theme') as typeof theme;
    if (saved) setTheme(saved);
  }, []);

  return (
    <select value={theme} onChange={e => setTheme(e.target.value as typeof theme)}>
      <option value="system">System</option>
      <option value="light">Light</option>
      <option value="dark">Dark</option>
    </select>
  );
}
```

### Dark Mode Design Principles

1. **Not inversion** — Dark mode is a separate, intentional palette
2. **Elevation = lightness** — In dark mode, elevated surfaces are LIGHTER
3. **Reduce contrast slightly** — Pure white (#fff) on dark is harsh; use #fafafa or #e5e5e5
4. **Accent colors may need adjustment** — Some colors look different on dark backgrounds
5. **Shadows become less visible** — Consider borders or lighter surfaces instead

---

## Responsive Design

### Breakpoint Strategy

```css
/* Mobile-first approach */
:root {
  --breakpoint-sm: 640px;
  --breakpoint-md: 768px;
  --breakpoint-lg: 1024px;
  --breakpoint-xl: 1280px;
  --breakpoint-2xl: 1536px;
}

/* Base styles = mobile */
.component { }

/* Progressively enhance */
@media (min-width: 768px) {
  .component { }
}

@media (min-width: 1024px) {
  .component { }
}
```

### Fluid Typography

```css
/* Don't use fixed sizes */
h1 {
  font-size: clamp(2rem, 5vw + 1rem, 4rem);
}

/* Scale */
--font-size-display: clamp(2.5rem, 8vw, 6rem);
--font-size-heading: clamp(1.5rem, 4vw, 2.5rem);
--font-size-body: clamp(1rem, 2vw, 1.125rem);
```

### Fluid Spacing

```css
.section {
  padding-block: clamp(var(--space-12), 8vw, var(--space-24));
  padding-inline: clamp(var(--space-4), 4vw, var(--space-12));
}
```

### Container Queries

```css
/* Define container */
.card-wrapper {
  container-type: inline-size;
  container-name: card;
}

/* Query container, not viewport */
@container card (min-width: 400px) {
  .card {
    flex-direction: row;
  }
}
```

---

## Accessibility

### Focus States

```css
/* Remove default, add custom */
:focus {
  outline: none;
}

:focus-visible {
  outline: 2px solid var(--color-accent);
  outline-offset: 2px;
}

/* For components that need custom focus */
.button:focus-visible {
  box-shadow: 0 0 0 3px var(--color-accent-subtle);
}
```

### Reduced Motion

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

### Color Contrast

Always verify contrast ratios:
- Body text: 4.5:1 minimum
- Large text (>18px bold, >24px): 3:1 minimum
- UI components: 3:1 minimum

```typescript
// Utility to check contrast
function getContrastRatio(fg: string, bg: string): number {
  const getLuminance = (hex: string) => {
    const rgb = hexToRgb(hex);
    const [r, g, b] = [rgb.r, rgb.g, rgb.b].map(c => {
      c = c / 255;
      return c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4);
    });
    return 0.2126 * r + 0.7152 * g + 0.0722 * b;
  };

  const l1 = getLuminance(fg);
  const l2 = getLuminance(bg);
  const lighter = Math.max(l1, l2);
  const darker = Math.min(l1, l2);

  return (lighter + 0.05) / (darker + 0.05);
}
```

### Semantic HTML

```tsx
// ❌ Div soup
<div onClick={handleClick}>Click me</div>

// ✅ Semantic
<button type="button" onClick={handleClick}>Click me</button>

// ❌ Missing landmarks
<div className="header">...</div>
<div className="main">...</div>
<div className="footer">...</div>

// ✅ Landmarks
<header>...</header>
<main>...</main>
<footer>...</footer>

// ❌ Missing labels
<input type="text" placeholder="Email" />

// ✅ Properly labeled
<label htmlFor="email">Email</label>
<input id="email" type="email" />
```

---

## Performance

### CSS Loading

```html
<!-- Critical CSS inline in head -->
<style>
  /* Above-the-fold styles only */
</style>

<!-- Non-critical CSS async -->
<link rel="preload" href="/styles.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="/styles.css"></noscript>
```

### Font Loading

```html
<!-- Preconnect to font origin -->
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

<!-- Preload critical fonts -->
<link rel="preload" as="font" type="font/woff2" href="/fonts/display.woff2" crossorigin>
```

```css
@font-face {
  font-family: 'Display';
  src: url('/fonts/display.woff2') format('woff2');
  font-display: optional; /* Don't flash if slow */
}

@font-face {
  font-family: 'Body';
  src: url('/fonts/body.woff2') format('woff2');
  font-display: swap; /* Show fallback, then swap */
}
```

### Animation Performance

```css
/* ❌ Triggers layout */
.bad {
  transition: width 300ms, height 300ms, top 300ms;
}

/* ✅ GPU-accelerated */
.good {
  transition: transform 300ms, opacity 300ms;
}

/* Use will-change sparingly */
.will-animate {
  will-change: transform;
}

.done-animating {
  will-change: auto;
}
```

---

## File Organization

### Component Structure

```
components/
├── Button/
│   ├── Button.tsx        # Component logic
│   ├── Button.css        # Component styles
│   ├── Button.test.tsx   # Tests
│   └── index.ts          # Export
├── Card/
│   ├── Card.tsx
│   ├── Card.css
│   └── index.ts
└── index.ts              # Barrel export
```

### Styles Structure

```
styles/
├── tokens/
│   ├── colors.css        # Color tokens
│   ├── typography.css    # Font tokens
│   ├── spacing.css       # Spacing scale
│   └── effects.css       # Shadows, radius
├── base/
│   ├── reset.css         # CSS reset
│   ├── globals.css       # Global styles
│   └── typography.css    # Base typography
├── utilities/
│   └── utilities.css     # Utility classes
└── main.css              # Import all
```

### Import Order

```css
/* main.css */
@import './tokens/colors.css';
@import './tokens/typography.css';
@import './tokens/spacing.css';
@import './tokens/effects.css';

@import './base/reset.css';
@import './base/globals.css';
@import './base/typography.css';

@import './utilities/utilities.css';
```
