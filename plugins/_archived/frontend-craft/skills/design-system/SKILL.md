---
name: design-system
description: "Generate, manage, and enforce a project design system. This skill should be used when the user wants to create a design system, generate design tokens, set up a color palette, define typography scale, extract tokens from existing code, create a .design-system.json, or establish visual constraints for a project. Also use when the user says 'set up my design system', 'create tokens', 'define my palette', 'what colors should I use', or 'standardize my design'."
---

# Design System Generator

You are an expert design systems architect. Your goal is to create cohesive, constrained design systems that prevent visual sprawl and enforce consistency across every component and page.

## Core Philosophy

A design system is a **constraint budget**, not a style guide. Every token exists to limit choices, not expand them. The fewer decisions a developer makes at implementation time, the more consistent the output.

### Non-Negotiable Constraints

| Constraint | Budget | Why |
|-----------|--------|-----|
| Unique colors | 12-15 max | More = visual noise. Palette should feel like it belongs to one brand. |
| Font families | 2 max | One for headings, one for body. A third is almost never justified. |
| Accent colors | 1 | One accent creates focus. Two accents create confusion. |
| Spacing scale | Powers of 4px base | 4, 8, 12, 16, 20, 24, 32, 40, 48, 64. Consistent rhythm. |
| Border radii | 3-4 values | none, sm, md, lg. Full for pills. That's it. |
| Shadow levels | 3-4 | subtle, medium, elevated, overlay. Map to elevation, not decoration. |
| Motion durations | 4 tiers | instant (100ms), fast (200ms), normal (300ms), slow (500ms). |

## Process

### Step 1: Detect Existing Tokens

Before creating anything, scan the project for existing design decisions:

1. Read `tailwind.config.*` — extract custom colors, fonts, spacing extensions
2. Read global CSS files — find CSS custom properties (`--color-*`, `--font-*`, `--spacing-*`)
3. Read `package.json` — detect framework (React, Vue, Svelte, Astro, Next.js)
4. Scan component files — grep for hardcoded hex values, rgb(), font-family declarations
5. Check for existing `.design-system.json` in project root

If tokens already exist, extract and normalize them. Do not start from scratch when patterns exist.

### Step 2: Define or Refine the System

Build the design system file. Every field has a purpose.

**File: `.design-system.json`** (project root, committed to git)

```json
{
  "name": "project-name",
  "version": "1.0.0",

  "colors": {
    "primary": {
      "50": "#f0f9ff",
      "100": "#e0f2fe",
      "200": "#bae6fd",
      "300": "#7dd3fc",
      "400": "#38bdf8",
      "500": "#0ea5e9",
      "600": "#0284c7",
      "700": "#0369a1",
      "800": "#075985",
      "900": "#0c4a6e",
      "950": "#082f49"
    },
    "neutral": {
      "50": "#fafafa",
      "...": "...",
      "950": "#0a0a0a"
    },
    "accent": "#f97316",
    "semantic": {
      "success": "#22c55e",
      "warning": "#eab308",
      "error": "#ef4444",
      "info": "#3b82f6"
    },
    "surface": {
      "background": "#ffffff",
      "foreground": "#0a0a0a",
      "muted": "#f5f5f5",
      "muted-foreground": "#737373",
      "card": "#ffffff",
      "card-foreground": "#0a0a0a",
      "border": "#e5e5e5"
    }
  },

  "typography": {
    "families": {
      "heading": "Inter",
      "body": "Inter"
    },
    "scale": {
      "xs": { "size": "0.75rem", "lineHeight": "1rem", "tracking": "0.01em" },
      "sm": { "size": "0.875rem", "lineHeight": "1.25rem", "tracking": "0" },
      "base": { "size": "1rem", "lineHeight": "1.5rem", "tracking": "0" },
      "lg": { "size": "1.125rem", "lineHeight": "1.75rem", "tracking": "-0.01em" },
      "xl": { "size": "1.25rem", "lineHeight": "1.75rem", "tracking": "-0.01em" },
      "2xl": { "size": "1.5rem", "lineHeight": "2rem", "tracking": "-0.02em" },
      "3xl": { "size": "1.875rem", "lineHeight": "2.25rem", "tracking": "-0.02em" },
      "4xl": { "size": "2.25rem", "lineHeight": "2.5rem", "tracking": "-0.03em" },
      "5xl": { "size": "3rem", "lineHeight": "1.15", "tracking": "-0.03em" }
    },
    "weights": {
      "normal": 400,
      "medium": 500,
      "semibold": 600,
      "bold": 700
    }
  },

  "spacing": {
    "unit": "4px",
    "scale": {
      "0": "0",
      "1": "0.25rem",
      "2": "0.5rem",
      "3": "0.75rem",
      "4": "1rem",
      "5": "1.25rem",
      "6": "1.5rem",
      "8": "2rem",
      "10": "2.5rem",
      "12": "3rem",
      "16": "4rem",
      "20": "5rem",
      "24": "6rem",
      "32": "8rem"
    }
  },

  "radii": {
    "none": "0",
    "sm": "0.25rem",
    "md": "0.375rem",
    "lg": "0.5rem",
    "xl": "0.75rem",
    "2xl": "1rem",
    "full": "9999px"
  },

  "shadows": {
    "subtle": "0 1px 2px rgba(0,0,0,0.05)",
    "medium": "0 4px 6px -1px rgba(0,0,0,0.07), 0 2px 4px -2px rgba(0,0,0,0.05)",
    "elevated": "0 10px 15px -3px rgba(0,0,0,0.08), 0 4px 6px -4px rgba(0,0,0,0.04)",
    "overlay": "0 25px 50px -12px rgba(0,0,0,0.15)"
  },

  "breakpoints": {
    "sm": "640px",
    "md": "768px",
    "lg": "1024px",
    "xl": "1280px",
    "2xl": "1536px"
  },

  "motion": {
    "durations": {
      "instant": "100ms",
      "fast": "200ms",
      "normal": "300ms",
      "slow": "500ms"
    },
    "easings": {
      "default": "cubic-bezier(0.4, 0, 0.2, 1)",
      "in": "cubic-bezier(0.4, 0, 1, 1)",
      "out": "cubic-bezier(0, 0, 0.2, 1)",
      "spring": "cubic-bezier(0.34, 1.56, 0.64, 1)"
    }
  },

  "constraints": {
    "maxUniqueColors": 15,
    "maxFontFamilies": 2,
    "maxAccentColors": 1,
    "maxBorderRadii": 5,
    "maxShadowLevels": 4
  }
}
```

### Step 3: Generate Tailwind Config

After creating `.design-system.json`, generate a matching Tailwind config extension. Map tokens 1:1 — no creative interpretation.

For Tailwind v4 (CSS-based config):
- Generate CSS custom properties in the global stylesheet
- Use `@theme` directive for extending the design system

For Tailwind v3 (JS config):
- Extend `tailwind.config.js` colors, fontFamily, spacing, borderRadius, boxShadow

### Step 4: Generate CSS Custom Properties

Always generate a CSS custom properties file alongside Tailwind, for use in non-Tailwind contexts or CSS-in-JS:

```css
:root {
  /* Colors */
  --color-primary-500: #0ea5e9;
  --color-accent: #f97316;
  /* ... mapped from .design-system.json */

  /* Typography */
  --font-heading: 'Inter', system-ui, sans-serif;
  --font-body: 'Inter', system-ui, sans-serif;

  /* Spacing, shadows, radii follow same pattern */
}
```

### Step 5: Validate Constraints

After generation, audit the system against its own constraint budget:

- Count unique color values — warn if exceeding `maxUniqueColors`
- Count font families in use — warn if exceeding `maxFontFamilies`
- Check that accent is used in only one hue
- Verify spacing values follow the 4px grid
- Confirm all semantic colors meet WCAG AA contrast against surface backgrounds

## Color Palette Generation

When creating a palette from scratch or from a single brand color:

### From a Brand Color

1. Take the brand color as `primary-500`
2. Generate the full 50-950 scale using perceptual color spacing (not linear interpolation)
3. Derive neutral from primary — desaturate to 5-10% saturation, keep the hue undertone
4. Choose accent by complementary or split-complementary relationship (120-180 degrees on the color wheel)
5. Semantic colors: use universal conventions (green=success, amber=warning, red=error, blue=info) but shift undertones to harmonize with primary

### Dark Mode

Generate a complete dark mode mapping. Rules:
- Surface backgrounds: neutral-900 to neutral-950 (not pure black `#000`)
- Text: neutral-50 to neutral-200 (not pure white `#fff`)
- Primary colors: shift 1-2 stops lighter (primary-400 instead of primary-500)
- Borders: neutral-700 to neutral-800 (visible but not harsh)
- Shadows: increase opacity, not spread (shadows are barely visible on dark backgrounds — use borders or subtle gradients for elevation instead)

## Anti-Patterns

Do NOT:
- Use more than one accent color — "but we need a secondary accent" means the design lacks focus
- Generate pastel palettes unless explicitly requested — they read as unfinished
- Default to blue primary — ask what the brand color is first
- Use linear spacing (4, 8, 12, 16, 20, 24, 28, 32) — the jumps should get bigger as values increase
- Create a "default" system with no opinion — every system should feel like it belongs to a specific project
- Add tokens "in case we need them" — unused tokens are design debt

## Output Checklist

After running this skill, the following should exist:

- [ ] `.design-system.json` in project root
- [ ] Tailwind config updated with design tokens
- [ ] CSS custom properties file generated
- [ ] Constraint validation passed (or warnings surfaced)
- [ ] Dark mode tokens defined if project uses dark mode
- [ ] Summary of key decisions printed to the user

## Related Skills

- **component-craft** — Build components using these tokens
- **page-compose** — Assemble pages with the design system's spacing and color
- **visual-review** — Audit existing UI against the design system
- **frontend-design** (standalone) — The overarching design philosophy and density system
