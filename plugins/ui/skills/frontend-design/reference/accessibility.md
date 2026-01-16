# Accessibility

Focus states, reduced motion, color contrast, semantic HTML, and ARIA.

---

## Focus States

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

## Reduced Motion

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

## Color Contrast

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

## Semantic HTML

```tsx
// Bad: Div soup
<div onClick={handleClick}>Click me</div>

// Good: Semantic
<button type="button" onClick={handleClick}>Click me</button>

// Bad: Missing landmarks
<div className="header">...</div>
<div className="main">...</div>
<div className="footer">...</div>

// Good: Landmarks
<header>...</header>
<main>...</main>
<footer>...</footer>

// Bad: Missing labels
<input type="text" placeholder="Email" />

// Good: Properly labeled
<label htmlFor="email">Email</label>
<input id="email" type="email" />
```

## Performance Considerations

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
/* Bad: Triggers layout */
.bad {
  transition: width 300ms, height 300ms, top 300ms;
}

/* Good: GPU-accelerated */
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
