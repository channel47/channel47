# Color System

Opinionated color palette generation and usage.

---

## Core Principle

**Dominant color + sharp accent beats evenly-distributed palettes.**

Commit to a palette. Don't hedge with "safe" neutrals everywhere.

---

## CSS Variable Structure

Every project should define these semantic colors:

```css
:root {
  /* Backgrounds */
  --color-bg: #ffffff;
  --color-surface: #f5f5f5;
  --color-surface-elevated: #ffffff;

  /* Text */
  --color-text-primary: #171717;
  --color-text-secondary: #525252;
  --color-text-tertiary: #a3a3a3;

  /* Accent */
  --color-accent: #f97316;
  --color-accent-hover: #ea580c;
  --color-accent-subtle: #fff7ed;

  /* Semantic */
  --color-success: #22c55e;
  --color-warning: #eab308;
  --color-error: #ef4444;

  /* Borders */
  --color-border: #e5e5e5;
  --color-border-strong: #d4d4d4;
}
```

---

## Generating from Hero Color

Start with ONE hero color, derive the rest.

```typescript
function generatePalette(heroHex: string) {
  const hsl = hexToHsl(heroHex);

  return {
    // Hero and variants
    accent: heroHex,
    accentHover: `hsl(${hsl.h}, ${hsl.s}%, ${hsl.l - 10}%)`,
    accentSubtle: `hsl(${hsl.h}, ${hsl.s * 0.3}%, 97%)`,

    // Neutrals derived from hero hue
    bg: `hsl(${hsl.h}, 5%, 100%)`,
    surface: `hsl(${hsl.h}, 5%, 97%)`,
    textPrimary: `hsl(${hsl.h}, 10%, 10%)`,
    textSecondary: `hsl(${hsl.h}, 5%, 40%)`,
    border: `hsl(${hsl.h}, 5%, 90%)`
  };
}
```

---

## Dark Mode

Dark mode is NOT "invert colors." It's a separate, intentional palette.

### Principles

1. **Background**: Not pure black (#000). Use #0a0a0a to #171717.
2. **Text**: Not pure white (#fff). Use #fafafa to #e5e5e5.
3. **Accent**: May need adjustment for contrast on dark backgrounds.
4. **Elevation**: Lighter surfaces feel "raised" in dark mode (opposite of light).

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
  }
}
```

---

## Contrast Requirements

WCAG 2.1 minimum ratios:

| Use Case | Minimum Ratio |
|----------|---------------|
| Body text | 4.5:1 |
| Large text (>18px bold, >24px) | 3:1 |
| UI components, graphics | 3:1 |
| Decorative | No requirement |

### Testing

```typescript
function getContrastRatio(fg: string, bg: string): number {
  const fgLum = getLuminance(fg);
  const bgLum = getLuminance(bg);
  const lighter = Math.max(fgLum, bgLum);
  const darker = Math.min(fgLum, bgLum);
  return (lighter + 0.05) / (darker + 0.05);
}

function getLuminance(hex: string): number {
  const rgb = hexToRgb(hex);
  const [r, g, b] = [rgb.r, rgb.g, rgb.b].map(c => {
    c = c / 255;
    return c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4);
  });
  return 0.2126 * r + 0.7152 * g + 0.0722 * b;
}
```

---

## Color Relationships

### Monochrome

Single hue, vary lightness. Always works.

```css
--color-100: hsl(220, 50%, 95%);
--color-200: hsl(220, 50%, 85%);
--color-300: hsl(220, 50%, 70%);
--color-500: hsl(220, 50%, 50%);
--color-700: hsl(220, 50%, 30%);
--color-900: hsl(220, 50%, 15%);
```

### Complementary

Two hues 180° apart. High contrast, use sparingly.

```css
--primary: hsl(220, 50%, 50%);   /* Blue */
--complement: hsl(40, 50%, 50%); /* Orange */
```

### Analogous

Adjacent hues (±30°). Harmonious.

```css
--cool: hsl(190, 50%, 50%);  /* Cyan */
--base: hsl(220, 50%, 50%);  /* Blue */
--warm: hsl(250, 50%, 50%);  /* Purple */
```

---

## What to Avoid

- **Purple gradient on white** — The #1 "AI slop" indicator
- **Rainbow palettes** — Too many hues = visual chaos
- **Low contrast "aesthetic" choices** — Accessibility isn't optional
- **Pure black (#000) on pure white (#fff)** — Too harsh, use near-black/white
