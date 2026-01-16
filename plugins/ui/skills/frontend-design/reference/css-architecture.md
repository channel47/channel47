# CSS Architecture

Custom properties structure, component scoping, and naming conventions.

---

## Custom Properties Structure

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

## Component Scoping

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
