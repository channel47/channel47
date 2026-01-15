# Typography System

Opinionated font selection and usage patterns.

---

## The Rule

**Never use:** Inter, Roboto, Open Sans, Lato, system-ui defaults.

These are safe choices that signal "I didn't think about this." Distinctive typography signals intention.

---

## Recommended by Context

| Context | Display Font | Body Font | Mono Font |
|---------|--------------|-----------|-----------|
| **Technical/Dev** | Space Grotesk | IBM Plex Sans | JetBrains Mono |
| **Editorial** | Playfair Display | Source Serif 4 | — |
| **Startup/Modern** | Clash Display | Satoshi | Fira Code |
| **Luxury** | Cormorant Garamond | Lora | — |
| **Brutalist** | Obviously | Neue Haas Grotesk | IBM Plex Mono |

### Font Sources

- [Google Fonts](https://fonts.google.com) — Free, easy CDN
- [Fontshare](https://fontshare.com) — Free, high quality (Satoshi, Clash Display)
- [Adobe Fonts](https://fonts.adobe.com) — Paid, extensive library

---

## Loading Strategy

### Critical Fonts (Above the fold)

```html
<head>
  <!-- Preload critical fonts -->
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="preload" as="font" type="font/woff2"
        href="/fonts/display.woff2" crossorigin>

  <!-- Load with swap for body, optional for display -->
  <style>
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
  </style>
</head>
```

### Subsetting

Only include characters you need:

```bash
# Using pyftsubset
pyftsubset font.ttf \
  --unicodes="U+0020-007E,U+00A0-00FF" \
  --layout-features="kern,liga" \
  --output-file="font-subset.woff2" \
  --flavor="woff2"
```

---

## Type Scale

Use a consistent multiplier, not arbitrary sizes.

### Recommended Scales

| Scale | Multiplier | Use Case |
|-------|------------|----------|
| Minor Third | 1.2 | Compact UI, dense information |
| Major Third | 1.25 | General purpose, balanced |
| Perfect Fourth | 1.333 | Editorial, generous spacing |
| Golden Ratio | 1.618 | Display, dramatic hierarchy |

### Example (Major Third, base 16px)

```css
:root {
  --font-size-xs: 0.64rem;   /* 10.24px */
  --font-size-sm: 0.8rem;    /* 12.8px */
  --font-size-base: 1rem;    /* 16px */
  --font-size-lg: 1.25rem;   /* 20px */
  --font-size-xl: 1.563rem;  /* 25px */
  --font-size-2xl: 1.953rem; /* 31.25px */
  --font-size-3xl: 2.441rem; /* 39px */
  --font-size-4xl: 3.052rem; /* 48.8px */
}
```

---

## Hierarchy Rules

### Minimum Contrast

For clear hierarchy, size jumps should be **3x or more**.

```css
/* ❌ Weak hierarchy */
h1 { font-size: 24px; }
h2 { font-size: 20px; }  /* Only 1.2x — hard to distinguish */

/* ✅ Strong hierarchy */
h1 { font-size: 48px; }
h2 { font-size: 24px; }  /* 2x — clear distinction */
p  { font-size: 16px; }  /* 1.5x from h2 — readable flow */
```

### Weight Contrast

Use extremes: 100/200 vs 700/800, not 400 vs 500.

```css
/* ❌ Weak */
h1 { font-weight: 600; }
p  { font-weight: 400; }

/* ✅ Strong */
h1 { font-weight: 800; }
p  { font-weight: 300; }
```

---

## Line Height

| Element | Line Height | Why |
|---------|-------------|-----|
| Display/Headings | 1.1-1.2 | Tight, compact |
| Body text | 1.5-1.7 | Readable, breathable |
| UI labels | 1.2-1.4 | Compact but legible |

```css
h1, h2, h3 { line-height: 1.15; }
p, li { line-height: 1.6; }
button, label { line-height: 1.3; }
```

---

## Letter Spacing

| Context | Letter Spacing |
|---------|----------------|
| Large display (>48px) | -0.02em to -0.04em (tighten) |
| Body text | 0 (default) |
| All caps | +0.05em to +0.1em (loosen) |
| Small text (<12px) | +0.02em (improve legibility) |

```css
.display { letter-spacing: -0.03em; }
.allcaps { letter-spacing: 0.08em; text-transform: uppercase; }
.fine-print { letter-spacing: 0.02em; }
```
