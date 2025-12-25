# ASCII Art Digital Assets Implementation Plan

## Overview

Transform Channel47's digital assets with ASCII art to create a distinctive CLI-native aesthetic that reinforces the site's identity as a Claude Code plugin marketplace. The goal is to add character while preserving the clean, minimal design system with generous white space.

---

## Part 1: Logo & Wordmark Transformation

### Current State
- **Header wordmark**: Text-based "Channel47" with weight mixing (bold "Channel" + light "47")
- **Favicon**: SVG coral-colored abstract shape (`public/favicon.svg`)
- **Location**: `src/components/Header.astro`

### Proposed Changes

#### 1.1 ASCII Wordmark Component
Create a new `AsciiLogo.astro` component featuring a compact, elegant ASCII representation:

```
╔═══════════════════╗
║  Channel47        ║
╚═══════════════════╝
```

Or a more stylized minimal approach:
```
┌─ channel ─┐
│    47     │
└───────────┘
```

**Design Philosophy**: Keep it small, monospace, and understated. The ASCII should feel like a subtle nod to the CLI world rather than an overwhelming graphic.

#### 1.2 Implementation Details
- **File to create**: `src/components/AsciiLogo.astro`
- **File to modify**: `src/components/Header.astro` - integrate the new component
- **CSS additions**: `src/styles/components/ascii-logo.css`
  - Use `font-family: 'JetBrains Mono', monospace`
  - Small font size (~12-14px) to maintain header elegance
  - Subtle color: primary text color, no accent colors
  - Responsive: collapse to simpler version on mobile

#### 1.3 Alternative Concept: Animated ASCII Cursor
Add a blinking cursor effect after the wordmark to evoke terminal feel:
```
Channel47█
```
- CSS animation for cursor blink
- Enhances CLI aesthetic without adding visual complexity

---

## Part 2: Plugin Card ASCII Art Embellishments

### Current State
- Plugin cards displayed in asymmetric grid (`src/pages/plugins/index.astro`)
- Cards have: category badge, name, description, meta info
- Featured cards show installation command
- Styling in `src/styles/components/plugin-spread.css`

### Proposed Changes

#### 2.1 Category-Specific ASCII Icons
Add small, tasteful ASCII icons that represent each plugin category. These appear subtly in the top-right corner of cards:

| Category | ASCII Art |
|----------|-----------|
| creative | `◈` or `✦` |
| development | `</>` or `{ }` |
| writing | `¶` or `≡` |
| marketing | `◉` or `▣` |
| data | `⊞` or `⋮⋮⋮` |

**Implementation**:
- Position: absolute, top-right of card
- Opacity: 0.15 (very subtle watermark effect)
- Size: Large (3-4rem) but extremely faint
- On hover: opacity increases to 0.25

#### 2.2 ASCII Border Accents for Featured Cards
Featured cards get a subtle ASCII-style corner treatment:

```
┌──────────────────────────────────────┐
│  [Featured Plugin Content Here]      │
└──────────────────────────────────────┘
```

**Implementation approach**:
- Use CSS `::before` and `::after` pseudo-elements
- Only on `.plugin-spread--featured` class
- Keep border very light: `color: var(--color-gray-200)`
- White space preserved inside the border frame

#### 2.3 ASCII Art for ascii-art Plugin Card (Meta/Self-Referential)
The ascii-art plugin itself should showcase its own capability with a small embedded ASCII art preview:

```
 ╭──────────╮
 │  ASCII   │
 │   ART    │
 ╰──────────╯
```

This creates a delightful self-referential moment where the plugin demonstrates itself.

---

## Part 3: Files to Create/Modify

### New Files

1. **`src/components/AsciiLogo.astro`**
   - Compact ASCII wordmark component
   - Props: `size: 'small' | 'large'`
   - Responsive behavior built-in

2. **`src/styles/components/ascii-logo.css`**
   - Monospace font styling
   - Cursor animation keyframes
   - Responsive adjustments

3. **`src/components/AsciiIcon.astro`**
   - Reusable component for category icons
   - Props: `category: string`
   - Maps category to appropriate ASCII symbol

### Modified Files

1. **`src/components/Header.astro`**
   - Import and use `AsciiLogo` component
   - Replace or augment existing wordmark

2. **`src/pages/plugins/index.astro`**
   - Import `AsciiIcon` component
   - Add icon to each plugin card
   - Add special treatment for ascii-art plugin

3. **`src/styles/components/plugin-spread.css`**
   - Add styles for ASCII icons (watermark positioning)
   - Add featured card border treatment
   - Maintain existing white space principles

4. **`public/favicon.svg`** (optional)
   - Could be updated to a simple ASCII-inspired geometric shape
   - Current coral circle could become `[ ]` or similar

---

## Part 4: Design Principles to Maintain

### White Space Preservation
- All ASCII elements should be subtle additions, not space-fillers
- Maintain existing padding/margin values
- Icons and borders should use opacity < 0.3 for watermark effect
- Never sacrifice readability for decoration

### Clean UI Guidelines
- Monochrome ASCII (use text colors, not accent colors)
- Small footprint - ASCII elements should be recognizable but not dominant
- Consistent sizing across all ASCII elements
- No animation except subtle cursor blink (optional)

### Responsive Behavior
- Hide complex ASCII on mobile if needed
- Simplify to single-character symbols on small screens
- Maintain touch target sizes for interactive elements

---

## Part 5: Implementation Order

1. **Phase 1: Logo Component**
   - Create `AsciiLogo.astro`
   - Create accompanying CSS
   - Integrate into Header

2. **Phase 2: Category Icons**
   - Create `AsciiIcon.astro`
   - Add icon mapping for each category
   - Integrate into plugin cards
   - Style with subtle watermark effect

3. **Phase 3: Featured Card Treatment**
   - Add ASCII border styling for featured cards
   - Add special ascii-art plugin showcase

4. **Phase 4: Polish**
   - Test responsive behavior
   - Verify dark mode compatibility
   - Fine-tune opacity/sizing values

---

## Part 6: Visual Mockups

### Header (Before)
```
Channel47                        Blog  Tools  About
```

### Header (After)
```
┌ Channel47 ┐                    Blog  Tools  About
```
or
```
Channel47█                       Blog  Tools  About
```

### Plugin Card (Before)
```
┌─────────────────────────────────────────────────┐
│ CREATIVE                                        │
│ ascii-art                                       │
│ Generate ASCII art logos, banners, diagrams... │
│ by Jackson · v1.1.0                            │
└─────────────────────────────────────────────────┘
```

### Plugin Card (After)
```
┌─────────────────────────────────────────────────┐
│ CREATIVE                                    ◈   │ <- faint watermark
│ ascii-art                                       │
│                                                 │
│ Generate ASCII art logos, banners, diagrams... │
│                                                 │
│ by Jackson · v1.1.0                            │
│                                                 │
│   ╭──────────╮                                 │ <- only for ascii-art
│   │  ASCII   │                                 │
│   ╰──────────╯                                 │
└─────────────────────────────────────────────────┘
```

### Featured Card (After)
```
╭─────────────────────────────────────────────────╮
│ ┌───────────────────────────────────────────┐   │
│ │  FEATURED PLUGIN                          │   │
│ │  plugin-name                              │   │
│ │  Description...                           │   │
│ │  claude plugins install plugin-name       │   │
│ └───────────────────────────────────────────┘   │
╰─────────────────────────────────────────────────╯
```

---

## Summary

This plan adds ASCII art character to Channel47 through:
1. A subtle ASCII-enhanced logo in the header
2. Faint category icons as watermarks on plugin cards
3. Special treatment for featured plugins and the ascii-art plugin itself

All additions maintain the existing white space and clean aesthetic by using:
- Very low opacity for decorative elements
- Monochrome color palette
- Small, tasteful ASCII rather than elaborate graphics
- Proper responsive behavior

The result will be a unique CLI-native aesthetic that differentiates Channel47 while respecting the minimalist design philosophy.
