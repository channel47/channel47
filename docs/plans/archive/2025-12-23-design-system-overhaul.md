# Design System Overhaul - Plugin Index Redesign

**Date:** 2025-12-23
**Status:** Ready for implementation
**Scope:** Complete design system rebuild starting with plugin index as proof-of-concept

---

## Overview

Complete overhaul of the Channel 47 design system to align with the style guide at `style/README.md`. The redesign adopts a "refined but strange" editorial aesthetic inspired by 032c, SSENSE, Are.na, and Bloomberg Businessweek.

**Core principle:** Typography-led, restrained color, generous whitespace, intentional asymmetry.

**Proof-of-concept page:** Plugin index (`/plugins/index.astro`) - redesigned as editorial magazine spreads rather than card grid.

---

## Technical Foundation

### CSS Architecture

**Remove Tailwind completely.** Build new design system with:
- CSS custom properties as single source of truth
- BEM-ish naming conventions for components
- Component-scoped styles
- No utility class framework

**File structure:**
```
src/styles/
  ├── global.css              # Design tokens + base styles
  ├── components/
  │   ├── header.css          # Navigation component
  │   ├── plugin-spread.css   # Plugin listing styles
  │   └── ...
  └── utilities.css           # Minimal utilities if needed
```

### Design Tokens

All tokens defined in `global.css` as CSS custom properties.

**Color System:**
```css
:root {
  /* Neutrals - Light Mode */
  --color-black: #0a0a0a;
  --color-white: #fafafa;
  --color-gray-100: #f0f0f0;
  --color-gray-200: #e0e0e0;
  --color-gray-300: #c0c0c0;
  --color-gray-400: #909090;
  --color-gray-500: #606060;
  --color-gray-600: #404040;
  --color-gray-700: #303030;
  --color-gray-800: #1a1a1a;

  /* Accent */
  --color-accent: #0047ff;
  --color-accent-muted: #0047ff20;

  /* Semantic tokens */
  --color-bg: var(--color-white);
  --color-text: var(--color-black);
  --color-text-muted: var(--color-gray-500);
  --color-border: var(--color-gray-200);
}
```

**Typography Scale:**
```css
:root {
  --text-xs: 0.75rem;      /* 12px - captions, metadata */
  --text-sm: 0.875rem;     /* 14px - secondary text */
  --text-base: 1rem;       /* 16px - body copy */
  --text-lg: 1.25rem;      /* 20px - lead paragraphs */
  --text-xl: 1.5rem;       /* 24px - section headers */
  --text-2xl: 2rem;        /* 32px - page titles */
  --text-3xl: 3rem;        /* 48px - display headlines */
  --text-4xl: 4.5rem;      /* 72px - hero statements */
  --text-5xl: 6rem;        /* 96px - editorial moments */
}
```

**Spacing Scale:**
```css
:root {
  --space-1: 0.25rem;   /* 4px */
  --space-2: 0.5rem;    /* 8px */
  --space-3: 0.75rem;   /* 12px */
  --space-4: 1rem;      /* 16px */
  --space-5: 1.5rem;    /* 24px */
  --space-6: 2rem;      /* 32px */
  --space-7: 3rem;      /* 48px */
  --space-8: 4rem;      /* 64px */
  --space-9: 6rem;      /* 96px */
  --space-10: 8rem;     /* 128px */
}
```

**Line Heights:**
```css
:root {
  --leading-tight: 1.1;     /* Display text */
  --leading-normal: 1.4;    /* UI text */
  --leading-relaxed: 1.6;   /* Body text */
}
```

### Typography

**Primary font:** Inter (Google Fonts)
- Load full weight range: 100-900
- Used for all display, body, and UI text
- Aggressive weight mixing creates visual interest

**Monospace font:** JetBrains Mono (Google Fonts)
- Code blocks and technical content only

**Font loading:**
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
```

---

## Navigation Design

### Auto-Hide Scroll Behavior

Header is fixed but hides on scroll down, reveals on scroll up. Always visible at top of page.

**Implementation:**
- JavaScript scroll listener detects direction
- Adds/removes classes to trigger CSS transitions
- Transition: `transform 200ms ease-out`

**States:**
- At top: `transform: translateY(0)` - visible
- Scrolling down: `transform: translateY(-100%)` - hidden
- Scrolling up: `transform: translateY(0)` - visible

### Visual Design

Minimal, text-based. No borders, no backdrop blur.

**Layout:**
```
[Channel 47]                    [Blog] [Tools] [About]
```

- Left: Wordmark ("Channel 47")
- Right: Navigation links
- Single line, minimal padding
- Black text on white (light mode), white on black (dark mode)

**Wordmark:**
- "Channel 47" in Inter
- Weight mixing: "Channel" at 400, "47" at 700
- Font size: --text-base or --text-lg

**Nav links:**
- Font size: --text-sm
- Color: --color-text-muted
- Hover: --color-accent (blue)
- No underline until hover

**Responsive:**
- Mobile: Same behavior, stack to hamburger if needed
- Or keep horizontal if it fits (preferred - simpler)

---

## Plugin Index Redesign

### Page Header

**Hero composition:**

Type-led, no images. Generous whitespace.

- **Title:** "Plugins" or declarative alternative ("Tools that work")
  - Desktop: --text-4xl (72px)
  - Mobile: --text-3xl (48px)
  - Weight mixing: First word 700-800, second word 400-500

- **Subtitle:** 1-2 sentences, --text-lg (20px)
  - Max-width: 65ch
  - Color: --color-text-muted

**Spacing:**
- Top padding: --space-9 (96px) desktop, --space-8 (64px) mobile
- Bottom padding: --space-7 (48px)

**Category filter:**

Simple text-based filter below hero.

Format: `All / Development / Content / Data / Workflow`

- Font size: --text-sm
- Uppercase, tracked out (letter-spacing: 0.05em)
- Default: --color-gray-400
- Active: --color-text (black/white)
- Hover: --color-accent (blue)
- Click filters spreads with fade transition

Spacing: --space-8 (64px) gap to first plugin spread

### Plugin Spreads - Asymmetric Grid

**Grid foundation:**

12-column CSS Grid on desktop. Plugins span varied widths to create asymmetry.

**Span patterns:**
- Featured: 12 columns (full width)
- Large: 8 columns
- Medium: 6 columns
- Small: 4 columns

**Rhythm example:**
1. Featured plugin (12 cols) - large vertical space
2. Two medium plugins (6 cols each) - side by side
3. Large plugin (8 cols)
4. Small plugin (4 cols) - inset right
5. Repeat with variation

**Separation:**
- No borders, no cards, no boxes
- Whitespace only
- Vertical gaps: --space-6 (32px) to --space-9 (96px) depending on size

### Plugin Spread Anatomy

Each spread contains:

**1. Category label**
- Size: --text-xs (12px)
- Uppercase, tracked out (letter-spacing: 0.1em)
- Color: --color-text-muted
- Position: Top of composition

**2. Plugin name**
- Size varies by spread:
  - Featured: --text-4xl or --text-3xl
  - Large: --text-2xl or --text-xl
  - Medium/Small: --text-xl or --text-lg
- Weight mixing: e.g., "Google" (700) + "Ads" (400)
- Color: --color-text
- Hover: --color-accent

**3. Description**
- 2-3 sentences max
- Size: --text-base or --text-lg (depending on spread)
- Max-width: 65ch
- Color: --color-text-muted

**4. Metadata**
- Author, version
- Size: --text-xs
- Color: --color-gray-400
- Layout: Horizontal, separated by middot or slash

**5. Code hint (optional)**
- Install command or snippet
- Some spreads only - for variety
- Monospace font, subtle background
- Size: --text-sm

### Interaction States

**Hover:**
- Plugin name color: --color-text → --color-accent
- Transition: `color 200ms ease-out`
- No background change, no shadows, no lift
- Entire spread clickable (links to detail page)

**Scroll-triggered fade-in:**
- Opacity: 0.7 → 1
- Transform: translateY(20px) → 0
- Duration: 400ms ease-out
- Staggered timing (50ms delay between spreads)
- Optional - can disable if too decorative

### Responsive Behavior

**Desktop (1024px+):**
- Full asymmetric grid (12 columns)
- Varied spans as described

**Tablet (768px - 1023px):**
- Simplified to 6-col and 12-col spreads mostly
- Less asymmetry, still varied

**Mobile (<768px):**
- Single column (all spreads 12/12)
- Stack vertically
- Scale differences maintained (featured = larger type)
- Vertical rhythm via varied spacing

**Margins:**
- Desktop: --space-7 (48px) minimum
- Mobile: --space-6 (32px) minimum
- Content never touches edges

---

## Typography - Implementing "Wrongness"

### Weight Mixing Techniques

**In plugin names:**
- Mix weights within name: "Google" (700) + "Ads" (400)
- Or reverse: "Creative" (400) + "Writing" (700)
- Rule: Use when it creates rhythm, not randomly

**In headlines:**
- Page titles: "Tools" (800) + "that work" (300)
- Or partial mixing: "Plugins" with first letters 700, last letters 400

**Implementation:**
```html
<h1 class="plugin-name">
  <span style="font-weight: 700">Google</span>
  <span style="font-weight: 400">Ads</span>
</h1>
```

### Kerning and Tracking

- Body copy: Normal (0)
- Headlines: Tight (-0.02em to -0.04em)
- Category labels: Wide (0.05em to 0.1em, uppercase)

### Scale Jumps

Within single spread:
- Category: --text-xs (12px)
- Name: --text-3xl (48px) - 4x jump
- Description: --text-base (16px)

Unexpected relationships create visual interest.

---

## Dark Mode Implementation

### Theme Switching

**System preference default:**
- Detect via `prefers-color-scheme` media query
- Manual override via toggle (stores in `localStorage`)

**Implementation:**
```html
<html data-theme="light"> <!-- or "dark" or "auto" -->
```

JavaScript on page load:
1. Check `localStorage` for preference
2. If none, check system preference
3. Apply immediately (no flash)

### Color Tokens

**Light mode:**
```css
:root {
  --color-bg: #fafafa;
  --color-text: #0a0a0a;
  --color-accent: #0047ff;
}
```

**Dark mode:**
```css
[data-theme="dark"],
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --color-bg: #0a0a0a;
    --color-text: #fafafa;
    --color-accent: #0047ff; /* same */

    /* Adjusted grays */
    --color-gray-100: #1a1a1a;
    --color-gray-200: #303030;
    --color-gray-300: #404040;
    --color-gray-400: #606060;
    --color-gray-500: #909090;
    --color-gray-600: #c0c0c0;
    --color-gray-700: #e0e0e0;
    --color-gray-800: #f0f0f0;

    --color-border: #303030;
  }
}
```

### Dark Mode Design

Not an inversion - intentionally designed:
- Background: True black (#0a0a0a)
- Text: Off-white (#fafafa)
- Grays rebalanced for dark backgrounds
- Blue accent may need contrast adjustment
- Code blocks: Subtle lift (#1a1a1a background)

### Toggle UI

Simple text toggle in footer:
```
Light / Dark / Auto
```

- Current selection: Blue accent color or bold weight
- Click cycles through options
- No icons - text only

---

## Implementation Phases

### Phase 1: Foundation
1. Remove Tailwind from `tailwind.config.mjs` and build
2. Define all design tokens in new `global.css`
3. Implement dark mode color switching
4. Update `BaseLayout.astro` with new font loading
5. Test token system works across both themes

### Phase 2: Navigation
1. Build new minimal header in `Header.astro`
2. Implement auto-hide scroll JavaScript
3. Add theme toggle to footer
4. Test on mobile

### Phase 3: Plugin Index
1. Redesign `/plugins/index.astro` layout
2. Build asymmetric grid system
3. Create plugin spread component styles
4. Implement category filter
5. Add hover states and transitions
6. Test responsive behavior

### Phase 4: Polish
1. Add scroll-triggered animations (optional)
2. Fine-tune spacing and typography
3. Cross-browser testing
4. Performance check

### Phase 5: Rollout
1. Validate proof-of-concept with stakeholders
2. Document patterns for other pages
3. Begin migrating other pages to new system

---

## Open Questions

- [ ] Final decision on page title: "Plugins" vs "Tools that work" vs alternative?
- [ ] Should scroll-triggered animations be included or skipped?
- [ ] Hamburger menu design for mobile nav?
- [ ] Code block syntax highlighting theme for dark mode?
- [ ] Should featured plugins be manually curated or algorithm-based?

---

## Success Criteria

The redesign succeeds if:

1. **Visual identity is distinct** - Site doesn't look like typical developer tools sites
2. **Typography leads** - Design interest comes from type, not decoration
3. **Content is discoverable** - Asymmetric layout doesn't sacrifice usability
4. **Dark mode works** - Not an afterthought, intentionally designed
5. **Performance maintained** - No degradation from current site
6. **Mobile experience strong** - Not just compressed desktop

---

## References

- Style guide: `/style/README.md`
- Current implementation: `/src/pages/plugins/index.astro`
- Design inspiration: 032c, SSENSE editorial, Are.na, Bloomberg Businessweek

---

*Ready for implementation review and approval.*
