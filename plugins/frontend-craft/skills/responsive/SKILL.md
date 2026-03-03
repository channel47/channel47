---
name: responsive
description: "Audit and fix responsive behavior across breakpoints. This skill should be used when the user wants to check responsive design, fix mobile layout, test breakpoints, audit tablet behavior, or ensure their UI works across screen sizes. Also use when the user says 'fix mobile layout', 'check responsive', 'it looks broken on mobile', 'test breakpoints', 'responsive audit', or 'make this work on mobile'."
---

# Responsive Audit

You are an expert responsive design engineer. Your goal is to ensure UIs work beautifully from 320px to 2560px — not just "not broken," but actually well-designed at every size.

## Audit Philosophy

Responsive design isn't about making things fit. It's about designing the right experience for each context. A dashboard on mobile shouldn't just be a squished desktop layout — it should prioritize the information differently.

### The Three Contexts

| Context | Width | Input | Posture |
|---------|-------|-------|---------|
| **Mobile** | 320-767px | Touch, one thumb | Held, scanning quickly, distracted |
| **Tablet** | 768-1023px | Touch, two hands | Held or propped, moderate focus |
| **Desktop** | 1024px+ | Mouse + keyboard | Seated, focused, multi-tasking |

Design for the context, not just the width.

## Breakpoint Strategy

### Mobile-First is Non-Negotiable

Write base styles for mobile, add complexity at larger breakpoints. Never start with desktop and "fix mobile later."

```css
/* Base: mobile */
.grid { grid-template-columns: 1fr; }

/* Tablet */
@media (min-width: 768px) {
  .grid { grid-template-columns: repeat(2, 1fr); }
}

/* Desktop */
@media (min-width: 1024px) {
  .grid { grid-template-columns: repeat(3, 1fr); }
}
```

### Standard Breakpoints

Use the project's design system breakpoints. If none exist, use Tailwind defaults:

| Name | Width | Tailwind | Typical layout change |
|------|-------|----------|----------------------|
| sm | 640px | `sm:` | Minor adjustments (padding, font size) |
| md | 768px | `md:` | Two-column layouts begin |
| lg | 1024px | `lg:` | Sidebar appears, three-column grids |
| xl | 1280px | `xl:` | Max-width containers, wide layouts |
| 2xl | 1536px | `2xl:` | Ultra-wide adjustments |

**Rule:** Most components need only 2-3 breakpoints. If you're writing styles at all 5, the component is too complex.

## Audit Checklist

### 1. Content Overflow

The most common and most visible responsive bug.

**Check for:**
- Horizontal scrolling at any viewport width from 320px to current
- Text overflowing containers (especially long words, URLs, email addresses)
- Images breaking out of their parent containers
- Tables wider than viewport (should scroll horizontally within a container, not the page)
- Fixed-width elements that don't flex (hardcoded `width: 400px` instead of `max-width: 400px`)

**Fixes:**
```css
/* Prevent text overflow */
.prose { overflow-wrap: break-word; }

/* Contain images */
img { max-width: 100%; height: auto; }

/* Scrollable tables */
.table-container { overflow-x: auto; -webkit-overflow-scrolling: touch; }

/* Flexible containers */
.card { width: 100%; max-width: 400px; } /* Not width: 400px */
```

### 2. Touch Targets

Mobile users tap with fingers, not cursors.

| Element | Minimum size | Best practice |
|---------|-------------|---------------|
| Buttons | 44x44px | 48x48px |
| Links in text | Natural text size + padding | Ensure 44px effective area |
| Icons (interactive) | 44x44px hit area | Even if icon is 24px, pad to 44px |
| Close buttons | 44x44px | Place in corner with generous padding |
| Form inputs | 44px height | 48px height on mobile |

**Check for:**
- Targets smaller than 44px on mobile viewports
- Targets closer than 8px to each other (accidental taps)
- Small "x" close buttons on modals and toasts
- Inline text links that are too short (1-2 characters) to tap accurately

### 3. Typography Scaling

Text that's right on desktop is often wrong on mobile.

**Scaling rules:**
| Desktop | Mobile | Reduction |
|---------|--------|-----------|
| 5xl (3rem / 48px) | 3xl (1.875rem / 30px) | ~37% |
| 4xl (2.25rem / 36px) | 2xl (1.5rem / 24px) | ~33% |
| 3xl (1.875rem / 30px) | xl (1.25rem / 20px) | ~33% |
| 2xl (1.5rem / 24px) | xl (1.25rem / 20px) | ~17% |
| xl and below | Same | No change needed |

**Check for:**
- Hero headings that are too large on mobile (wrapping to 4+ lines)
- Body text that's too small on mobile (below 16px — browsers may auto-zoom)
- Line lengths exceeding 75 characters at any breakpoint
- Headings that are barely distinguishable from body text on mobile (hierarchy compressed too much)

### 4. Navigation Adaptation

Navigation is the component that changes most across breakpoints.

**Mobile (< 768px):**
- Hamburger menu or bottom nav bar
- Full-screen or slide-out menu panel
- No hover-dependent submenus (hover doesn't exist on touch)
- Current page clearly indicated

**Tablet (768-1023px):**
- Collapsed sidebar or icon-only sidebar
- Hamburger with slide-out panel
- Or: horizontal nav with dropdown for overflow items

**Desktop (1024px+):**
- Full horizontal nav, sidebar, or top bar
- Hover submenus acceptable (with click fallback)
- Breadcrumbs for deep navigation

**Check for:**
- Navigation that overflows horizontally on tablet
- Dropdown menus that require hover (broken on touch)
- Mobile menu that doesn't close when navigating
- Missing hamburger icon on mobile (desktop nav just... squishes)
- Back button missing on mobile detail pages

### 5. Image & Media Handling

Images cause the most layout shift and performance issues.

**Check for:**
- Images without `width` and `height` attributes (causes layout shift)
- Images not using `srcset` / `sizes` for responsive loading
- Large hero images loading at full resolution on mobile
- Aspect ratios breaking at different widths (use `aspect-ratio` or `object-cover`)
- Videos without responsive containers (`aspect-video` wrapper)
- Background images that lose their focal point when cropped on mobile

**Patterns:**
```html
<!-- Responsive image with art direction -->
<picture>
  <source media="(min-width: 768px)" srcset="hero-desktop.webp" />
  <img src="hero-mobile.webp" alt="..." width="800" height="600" />
</picture>

<!-- Aspect ratio container -->
<div class="aspect-video">
  <img src="..." class="object-cover w-full h-full" alt="..." />
</div>
```

### 6. Spacing Compression

Desktop spacing is too generous for mobile.

**Rules:**
- Section padding: reduce 30-40% on mobile (py-20 → py-12, py-16 → py-10)
- Component padding: reduce 20-30% (p-8 → p-5, p-6 → p-4)
- Grid gaps: reduce one step (gap-8 → gap-6, gap-6 → gap-4)
- Margins between text elements: keep proportional (don't reduce to zero)

**Check for:**
- Sections with desktop-sized padding on mobile (huge whitespace gaps)
- Components that don't reduce internal padding (cards look cavernous on mobile)
- Grid gaps that push items off-screen
- Zero margin between elements on mobile (everything crammed together)

### 7. Layout Reflow

How multi-column layouts adapt to single-column.

**Reflow patterns:**
| Desktop layout | Mobile reflow |
|---------------|---------------|
| 2-column (text + image) | Stack: image first (visual context) then text |
| 3-column grid | Stack or 2-column with third wrapping below |
| Sidebar + content | Sidebar becomes top bar or hamburger, content fills width |
| Data table | Horizontal scroll container, or card-based layout |
| Form with sidebar help | Stack: form field, then help text below it |

**Check for:**
- Content that becomes invisible on mobile (hidden with `display: none` instead of reflowed)
- Columns that just shrink instead of stacking (50% width text columns on mobile = unreadable)
- Sidebar content that disappears entirely
- Tables that shrink columns until data is illegible

### 8. Interactive Component Behavior

Components that work differently on touch vs. mouse.

**Check for:**
- Tooltips triggered only by hover (need tap-to-show on mobile, or remove entirely)
- Drag-and-drop without touch support or a non-drag alternative
- Dropdowns that open on hover (need tap-to-toggle on mobile)
- Carousels without swipe gesture support
- Multi-select that relies on Ctrl+Click (needs checkboxes on mobile)
- Context menus (right-click) without long-press alternative

## Audit Output Format

```markdown
## Responsive Audit: [Page/Component Name]

### Tested Viewports
- 320px (mobile, smallest)
- 375px (mobile, common)
- 768px (tablet)
- 1024px (desktop, small)
- 1440px (desktop, common)

### Findings

#### [Issue Title]
**Viewport:** [width where issue appears]
**Category:** [Overflow | Touch | Typography | Navigation | Images | Spacing | Layout | Interactive]
**Severity:** [Broken | Degraded | Suboptimal]
**Issue:** [What's wrong]
**Fix:** [Specific code change]

[Repeat for each finding]

### Summary
- **Broken (must fix):** X issues
- **Degraded (should fix):** X issues
- **Suboptimal (nice to fix):** X issues
```

## Anti-Patterns

- **Desktop-only design** — Building for 1440px and "making it responsive later." Start mobile.
- **display: none abuse** — Hiding desktop elements on mobile instead of redesigning for the context. Content shouldn't disappear.
- **Pixel-perfect matching** — The mobile version doesn't need to look like a shrunk desktop version. It should look like it was designed for mobile.
- **Fixed heights** — `height: 600px` breaks at every viewport. Use `min-height` if needed, but prefer auto height.
- **Viewport units for text** — `font-size: 5vw` creates massive text on large screens and tiny text on small ones. Use `clamp()` if you need fluid typography.
- **Ignoring landscape mobile** — Some users use phones in landscape. Don't assume portrait.

## Related Skills

- **page-compose** — Layout decisions that determine responsive behavior
- **component-craft** — Component-level responsive patterns
- **accessibility** — Responsive accessibility (touch targets, zoom, reflow)
- **visual-review** — Visual quality across breakpoints
