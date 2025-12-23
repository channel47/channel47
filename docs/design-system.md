# Design System Documentation

## Using Design Tokens

All design tokens are defined in `src/styles/global.css` as CSS custom properties.

### Colors

```css
var(--color-bg)          /* Background */
var(--color-text)        /* Primary text */
var(--color-text-muted)  /* Secondary text */
var(--color-accent)      /* Blue accent */
var(--color-border)      /* Borders */
```

### Typography

```css
var(--text-xs)    /* 12px */
var(--text-sm)    /* 14px */
var(--text-base)  /* 16px */
var(--text-lg)    /* 20px */
var(--text-xl)    /* 24px */
var(--text-2xl)   /* 32px */
var(--text-3xl)   /* 48px */
var(--text-4xl)   /* 72px */
```

### Spacing

```css
var(--space-1)   /* 4px */
var(--space-4)   /* 16px */
var(--space-6)   /* 32px */
var(--space-8)   /* 64px */
var(--space-9)   /* 96px */
```

## Component Styles

Create component-scoped styles in `src/styles/components/`.

Import in Astro components:
```astro
import '../styles/components/my-component.css';
```

## Weight Mixing

Use weight mixing for typographic interest:
```html
<h1>
  <span style="font-weight: 700">Bold</span>
  <span style="font-weight: 400">Light</span>
</h1>
```

## Dark Mode

Theme is controlled by `data-theme` attribute on `<html>`:
- `data-theme="light"` - Light mode
- `data-theme="dark"` - Dark mode
- No attribute - Auto (follows system preference)
