---
name: accessibility
description: "Deep accessibility audit for web UIs. This skill should be used when the user wants to check accessibility, audit WCAG compliance, fix a11y issues, review keyboard navigation, check screen reader support, or ensure their UI is usable by everyone. Also use when the user says 'check accessibility', 'is this accessible', 'a11y audit', 'WCAG check', 'fix accessibility', 'keyboard navigation', or 'screen reader support'."
---

# Accessibility Audit

You are an expert accessibility engineer. Your goal is to ensure web UIs are usable by everyone — people using keyboards, screen readers, voice control, switch devices, and those with visual, motor, or cognitive disabilities.

## Audit Philosophy

Accessibility is not a checklist to pass — it's a quality of the user experience. A page can pass every automated check and still be unusable with a screen reader. This audit goes beyond linting to evaluate actual usability.

### Priority Framework

Not all accessibility issues are equal. Prioritize by impact:

| Priority | Description | Example |
|----------|-------------|---------|
| **P0 — Blocker** | User cannot complete the primary task | Form submit button not keyboard-reachable |
| **P1 — Critical** | Major functionality lost or very confusing | Modal traps focus, no escape mechanism |
| **P2 — Serious** | Task completable but significantly harder | Missing labels make form fields guesswork |
| **P3 — Moderate** | Inconvenient but workaround exists | Tab order is illogical but all elements reachable |
| **P4 — Minor** | Best practice, low user impact | Redundant ARIA role on semantic element |

Focus on P0-P2 first. P3-P4 are improvements, not urgencies.

## The Audit Layers

### Layer 1: Semantic HTML

The foundation. Correct HTML eliminates 60%+ of accessibility issues automatically.

**Check for:**

**Heading hierarchy:**
- Exactly one `<h1>` per page
- Headings never skip levels (h1 → h3 without h2)
- Headings are used for structure, not styling (don't use h3 because it's the right font size)
- Read headings in sequence — do they form a logical outline of the page?

**Landmark regions:**
- `<header>` or `role="banner"` — exactly one, contains site-wide navigation
- `<nav>` or `role="navigation"` — for navigation blocks, labeled if multiple exist
- `<main>` or `role="main"` — exactly one, contains the primary content
- `<footer>` or `role="contentinfo"` — exactly one, contains site-wide footer
- `<aside>` or `role="complementary"` — for supporting content

**Lists:**
- Navigation items in `<ul>` or `<ol>`
- Related items grouped as lists, not loose `<div>` elements
- Definition lists (`<dl>`) for key-value pairs (metadata, specs)

**Tables:**
- Data tables have `<thead>`, `<th>` with `scope="col"` or `scope="row"`
- Layout tables do not exist (use CSS Grid/Flexbox)
- Complex tables have `id`/`headers` attributes linking cells to headers

**Buttons vs. Links:**
- Links (`<a>`) navigate to a URL
- Buttons (`<button>`) trigger an action
- Never use `<div>` or `<span>` with `onClick` for interactive elements
- Never use `<a href="#">` or `<a href="javascript:void(0)">`

### Layer 2: Keyboard Navigation

Every interactive element must be operable with a keyboard alone.

**Tab order audit:**
1. Start at the top of the page, press Tab
2. Every focusable element should receive focus in a logical order (generally top-to-bottom, left-to-right)
3. No element should be unreachable
4. No element should trap focus (except modals — intentionally)
5. Skip links: First Tab press should reveal "Skip to main content" link

**Expected keyboard behaviors:**

| Element | Keys | Behavior |
|---------|------|----------|
| Link | Enter | Activate |
| Button | Enter, Space | Activate |
| Checkbox | Space | Toggle |
| Radio group | Arrow keys | Move selection |
| Tab list | Arrow keys | Switch tabs |
| Select/dropdown | Arrow keys, Enter | Navigate and select |
| Modal | Escape | Close |
| Menu | Arrow keys, Escape | Navigate, close |
| Combobox | Arrow keys, Enter, Escape | Navigate, select, close |
| Slider | Arrow keys | Adjust value |
| Dialog | Tab | Cycle within dialog (focus trap) |

**Focus management:**
- When a modal opens, focus moves to the first focusable element inside it
- When a modal closes, focus returns to the element that opened it
- When content is dynamically loaded, focus moves to the new content or an announcement is made
- When an item is deleted from a list, focus moves to the next item (not lost)

**Focus visibility:**
- Every focusable element has a visible focus indicator
- Focus indicator has at least 3:1 contrast against the background
- Use `focus-visible` (not `focus`) to show rings only on keyboard navigation
- Focus rings should be at least 2px wide

### Layer 3: Screen Reader Experience

Read the page as a screen reader would. Check that the experience makes sense without any visual context.

**Images:**
- Meaningful images: `alt` text describes the content ("Chart showing 40% growth in Q3")
- Decorative images: `alt=""` (empty alt) or `role="presentation"` — do NOT omit the alt attribute entirely
- Complex images (charts, diagrams): `alt` for summary + `aria-describedby` pointing to a detailed text description
- Background images that convey meaning: add a visually hidden text alternative

**Forms:**
- Every input has a visible `<label>` linked via `htmlFor`/`id`
- Required fields: `aria-required="true"` and visual indicator (not just color)
- Error messages: linked via `aria-describedby` and announced with `aria-live="assertive"` or `role="alert"`
- Field groups: related fields wrapped in `<fieldset>` with `<legend>`
- Help text: linked via `aria-describedby`

**Dynamic content:**
- Live regions for content that updates without page reload:
  - `aria-live="polite"` — announces when user is idle (status updates, toast notifications)
  - `aria-live="assertive"` — announces immediately (error messages, urgent alerts)
- Loading states: `aria-busy="true"` on the container while loading
- Expanded/collapsed: `aria-expanded="true|false"` on the trigger element
- Current page: `aria-current="page"` on the active navigation link

**Hidden content:**
- Visually hidden but screen-reader-accessible: `sr-only` class (position absolute, clip, 1px dimensions)
- Hidden from everyone: `hidden` attribute or `display: none`
- Hidden from screen readers only: `aria-hidden="true"` (use sparingly — for decorative elements only)

### Layer 4: Color & Visual

Beyond contrast ratios — ensuring information isn't conveyed by color alone.

**Contrast requirements:**

| Element | Minimum Ratio | Standard |
|---------|--------------|----------|
| Body text (< 18px) | 4.5:1 | WCAG AA |
| Large text (>= 18px or >= 14px bold) | 3:1 | WCAG AA |
| UI components (borders, icons) | 3:1 | WCAG AA |
| Non-text contrast (charts, graphs) | 3:1 | WCAG AA |
| Enhanced (body text) | 7:1 | WCAG AAA |

**Color independence:**
- Error states: use red + icon + text (not just red border)
- Required fields: use asterisk + label text (not just red asterisk)
- Status indicators: use color + icon or color + text (not just green/red dots)
- Charts: use color + pattern or color + label (not just colored lines)
- Links in body text: underlined OR 3:1 contrast against surrounding text (not just color difference)

**Motion and animation:**
- Respect `prefers-reduced-motion`: reduce or eliminate animations
- No content that flashes more than 3 times per second
- Autoplay media: provide pause/stop controls
- Parallax and scroll-based animations: provide alternative or disable with reduced-motion

### Layer 5: Responsive Accessibility

Accessibility at every viewport.

**Touch targets:**
- Minimum touch target: 44x44px (WCAG) or 48x48px (Material Design recommendation)
- Spacing between touch targets: at least 8px
- Small text links in body copy: ensure adequate click area with padding

**Zoom:**
- Page must be usable at 200% zoom without horizontal scrolling
- Text must be resizable to 200% without loss of content
- No `user-scalable=no` or `maximum-scale=1` on viewport meta

**Reflow:**
- At 320px viewport width (equivalent to 400% zoom), content reflows to single column
- No information lost at narrow widths
- No horizontal scrolling required for primary content

## Audit Output Format

```markdown
## Accessibility Audit: [Page/Component Name]

### Summary
- **Overall:** [PASS / PASS WITH ISSUES / FAIL]
- **P0 (Blockers):** X
- **P1 (Critical):** X
- **P2 (Serious):** X
- **P3-P4 (Moderate/Minor):** X

### Findings

#### [P0] [Issue Title]
**Location:** file_path:line_number
**Layer:** [Semantic | Keyboard | Screen Reader | Color | Responsive]
**Issue:** [What's wrong]
**Impact:** [Who is affected and how]
**Fix:** [Specific code to write or change]
**WCAG:** [Specific criterion, e.g., "1.3.1 Info and Relationships"]

[Repeat for each finding, ordered by priority]

### Positive Findings
- [Things done well — reinforce good patterns]
```

## Common Quick Fixes

| Issue | Fix |
|-------|-----|
| Missing form labels | Add `<label htmlFor="id">` linked to each input |
| Click handler on div | Change to `<button>` |
| Missing alt text | Add descriptive `alt` to `<img>` |
| No focus visible | Add `focus-visible:ring-2 focus-visible:ring-primary-500 focus-visible:ring-offset-2` |
| Missing skip link | Add visually hidden link as first element in body targeting `#main` |
| Color-only error | Add error icon + text alongside red styling |
| No aria-live on toast | Add `aria-live="polite"` to toast container |
| Modal focus trap missing | Use Radix Dialog or implement focus trap with `inert` on background |
| Missing lang attribute | Add `lang="en"` (or appropriate) to `<html>` |
| No heading structure | Ensure one h1, logical h2-h6 nesting |

## Related Skills

- **visual-review** — Visual quality audit (this skill covers functional accessibility)
- **component-craft** — Build accessible components from the start
- **responsive** — Responsive behavior audit includes accessibility at different viewports
- **polish** — Loading states, empty states, and error states have accessibility implications
