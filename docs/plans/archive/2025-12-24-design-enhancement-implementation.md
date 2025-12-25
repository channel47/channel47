# Design Enhancement Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Implement modern/geometric visual identity with bold typography, expanded color system, and refined component interactions

**Architecture:** CSS-only enhancements leveraging existing Astro component structure. Add DM Sans via Google Fonts, expand design token system in global.css, apply visual refinements to component stylesheets. No JavaScript required.

**Tech Stack:** Astro, CSS custom properties, Google Fonts (DM Sans)

---

## Task 1: Add DM Sans Typography

**Files:**
- Modify: `src/layouts/BaseLayout.astro:23`
- Modify: `src/styles/global.css:62`

**Step 1: Add DM Sans to Google Fonts link**

Update the Google Fonts link in BaseLayout.astro to include DM Sans variable font:

```html
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,100..1000&family=Inter:wght@100;200;300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
```

**Step 2: Test font loads in browser**

Run: `npm run dev` and open `http://localhost:4321`
Check: DevTools Network tab shows DM Sans fonts loading
Expected: Multiple DM Sans font files loaded (woff2 format)

**Step 3: Commit typography foundation**

```bash
git add src/layouts/BaseLayout.astro
git commit -m "feat: add DM Sans variable font"
```

---

## Task 2: Expand Design Token System

**Files:**
- Modify: `src/styles/global.css:2-52`

**Step 1: Add new color tokens to :root**

Insert after line 17 (after `--color-accent-muted`):

```css
  /* Secondary Accents */
  --color-accent-coral: #ff6b35;
  --color-accent-coral-light: rgba(255, 107, 53, 0.12);
  --color-accent-purple: #7c3aed;
  --color-accent-purple-light: rgba(124, 58, 237, 0.12);
  --color-accent-green: #10b981;
  --color-accent-green-light: rgba(16, 185, 129, 0.12);

  /* Rename existing accent for consistency */
  --color-accent: var(--color-accent-blue);
  --color-accent-blue: #0047ff;
  --color-accent-blue-hover: #0039cc;
  --color-accent-blue-light: rgba(0, 71, 255, 0.12);
```

**Step 2: Add typography scale tokens**

Replace existing type scale (lines 25-34) with expanded scale:

```css
  /* Typography Scale */
  --text-xs: 0.75rem;      /* 12px */
  --text-sm: 0.875rem;     /* 14px */
  --text-base: 1rem;       /* 16px */
  --text-lg: 1.25rem;      /* 20px */
  --text-xl: 1.5rem;       /* 24px */
  --text-2xl: 2rem;        /* 32px */
  --text-3xl: 3rem;        /* 48px */
  --text-4xl: 4rem;        /* 64px */
  --text-5xl: 7rem;        /* 112px */

  /* Font Weights */
  --weight-normal: 400;
  --weight-medium: 500;
  --weight-semibold: 600;
  --weight-bold: 700;
  --weight-extrabold: 800;
  --weight-black: 900;
```

**Step 3: Add spacing tokens**

Insert after typography tokens:

```css
  /* Spacing Scale - Desktop */
  --section-gap: 8rem;     /* 128px */
  --content-gap: 6rem;     /* 96px */
  --element-gap: 3rem;     /* 48px */
```

**Step 4: Add code block color tokens**

Insert after `--color-gray-800`:

```css
  /* Code Blocks */
  --color-code-bg: #1a1a1a;
  --color-code-border: rgba(255, 255, 255, 0.1);
```

**Step 5: Update dark mode code block border**

In `[data-theme="dark"]` section (around line 88), add:

```css
  --color-code-border: rgba(255, 255, 255, 0.15);
```

**Step 6: Update system preference dark mode code block border**

In `@media (prefers-color-scheme: dark)` section (around line 107), add:

```css
    --color-code-border: rgba(255, 255, 255, 0.15);
```

**Step 7: Test design tokens in DevTools**

Run: `npm run dev`
Check: DevTools > Elements > Computed styles on :root
Expected: All new CSS variables present with correct values

**Step 8: Commit design tokens**

```bash
git add src/styles/global.css
git commit -m "feat: expand design token system with colors, typography, spacing"
```

---

## Task 3: Apply DM Sans to Headings

**Files:**
- Modify: `src/styles/global.css:62-65`

**Step 1: Update base font-family to include DM Sans**

Replace line 62:

```css
html {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
```

**Step 2: Add heading font rules**

Insert after body styles (after line 75):

```css
h1, h2, h3, h4, h5, h6 {
  font-family: 'DM Sans', 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  font-weight: var(--weight-black);
  letter-spacing: -0.02em;
  line-height: var(--leading-tight);
}

h1 {
  font-size: var(--text-4xl);
  font-weight: var(--weight-black);
}

h2 {
  font-size: var(--text-3xl);
  font-weight: var(--weight-extrabold);
}

h3 {
  font-size: var(--text-2xl);
  font-weight: var(--weight-bold);
}

@media (min-width: 768px) {
  h1 {
    font-size: var(--text-5xl);
  }
}
```

**Step 3: Visual test typography**

Run: `npm run dev`
Visit: `http://localhost:4321/`
Check: Hero heading uses DM Sans at larger size
Expected: "Claude Code tools I actually use" is now 64px (mobile) with DM Sans

**Step 4: Commit typography application**

```bash
git add src/styles/global.css
git commit -m "feat: apply DM Sans to all headings with responsive sizing"
```

---

## Task 4: Update Home Page Typography

**Files:**
- Modify: `src/styles/components/home.css`

**Step 1: Remove manual heading size from hero title**

The global h1 styles now handle sizing, but we can add specific overrides for home hero.

Update `.home-hero__title` (around line 13):

```css
.home-hero__title {
  font-size: var(--text-5xl);
  font-weight: var(--weight-black);
  line-height: var(--leading-tight);
  letter-spacing: -0.03em;
  margin-bottom: var(--space-6);
}
```

**Step 2: Add responsive typography for mobile**

Update mobile media query (around line 79):

```css
@media (max-width: 768px) {
  .home-section {
    padding: var(--space-8) var(--space-6);
  }

  .home-hero__title {
    font-size: var(--text-4xl);
  }

  .home-hero__description {
    font-size: var(--text-base);
  }
}
```

**Step 3: Visual test home page**

Run: `npm run dev`
Visit: `http://localhost:4321/`
Check: Hero title is dramatically larger, uses DM Sans
Resize: Mobile view shows smaller but still bold heading
Expected: Desktop ~112px, mobile ~64px heading size

**Step 4: Commit home page typography**

```bash
git add src/styles/components/home.css
git commit -m "feat: enhance home page typography with larger hero heading"
```

---

## Task 5: Enhance Button Styles

**Files:**
- Modify: `src/styles/components/home.css:38-67`

**Step 1: Update button base styles**

Replace `.button` class (around line 38):

```css
.button {
  display: inline-flex;
  align-items: center;
  padding: var(--space-4) var(--space-6);
  font-size: var(--text-base);
  font-weight: var(--weight-semibold);
  border-radius: 8px;
  transition: all 200ms cubic-bezier(0.4, 0, 0.2, 1);
  cursor: pointer;
  border: none;
}
```

**Step 2: Enhance primary button with hover effects**

Replace `.button--primary` and add hover state:

```css
.button--primary {
  background-color: var(--color-accent-blue);
  color: var(--color-white);
}

.button--primary:hover {
  background-color: var(--color-accent-blue-hover);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 71, 255, 0.2);
}

.button--primary:focus-visible {
  outline: 2px solid var(--color-accent-blue);
  outline-offset: 2px;
}
```

**Step 3: Enhance secondary button with hover effects**

Replace `.button--secondary` and add hover state:

```css
.button--secondary {
  background-color: transparent;
  color: var(--color-text);
  border: 1px solid var(--color-border);
}

.button--secondary:hover {
  border-color: var(--color-text);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
}

.button--secondary:focus-visible {
  outline: 2px solid var(--color-text);
  outline-offset: 2px;
}
```

**Step 4: Test button interactions**

Run: `npm run dev`
Visit: `http://localhost:4321/`
Check: Hover over "Browse Tools" and "Read the Blog" buttons
Expected: Smooth lift animation with shadow on hover
Test: Tab to buttons with keyboard
Expected: Visible focus outline appears

**Step 5: Commit button enhancements**

```bash
git add src/styles/components/home.css
git commit -m "feat: add hover transforms and focus states to buttons"
```

---

## Task 6: Add Category Color System to Plugin Badges

**Files:**
- Modify: `src/styles/components/plugin-spread.css`

**Step 1: Read current plugin-spread styles**

```bash
cat src/styles/components/plugin-spread.css
```

Expected: See current badge styling

**Step 2: Add category-specific color classes**

Add after existing badge styles:

```css
.plugin-card__category[data-category="writing"] {
  background: var(--color-accent-coral-light);
  color: var(--color-accent-coral);
}

.plugin-card__category[data-category="marketing"] {
  background: var(--color-accent-green-light);
  color: var(--color-accent-green);
}

.plugin-card__category[data-category="development"] {
  background: var(--color-accent-purple-light);
  color: var(--color-accent-purple);
}

.plugin-card__category:not([data-category]) {
  background: var(--color-accent-blue-light);
  color: var(--color-accent-blue);
}
```

**Step 3: Update badge base styles**

Update base `.plugin-card__category` to improve typography:

```css
.plugin-card__category {
  display: inline-block;
  padding: 0.25rem 0.75rem;
  border-radius: 4px;
  font-size: var(--text-xs);
  font-weight: var(--weight-semibold);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  line-height: 1;
}
```

**Step 4: Test category colors**

Run: `npm run dev`
Visit: `http://localhost:4321/plugins`
Check: "MARKETING" badge should be green, "WRITING" badge should be coral
Expected: Category badges use distinct colors

**Step 5: Commit category color system**

```bash
git add src/styles/components/plugin-spread.css
git commit -m "feat: add color-coded category badges"
```

---

## Task 7: Enhance Plugin Card Hover States

**Files:**
- Modify: `src/styles/components/plugin-spread.css`

**Step 1: Add plugin card base transition**

Update `.plugin-card` or equivalent wrapper class:

```css
.plugin-card {
  background: var(--color-bg);
  border: 1px solid var(--color-border);
  border-radius: 12px;
  padding: var(--space-6);
  transition: all 200ms cubic-bezier(0.4, 0, 0.2, 1);
  text-decoration: none;
  display: block;
}
```

**Step 2: Add hover state with transform and shadow**

```css
.plugin-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
  border-color: var(--color-gray-300);
}
```

**Step 3: Add dark mode hover shadow**

In dark mode section or add new rule:

```css
[data-theme="dark"] .plugin-card:hover {
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
}
```

**Step 4: Test plugin card hover**

Run: `npm run dev`
Visit: `http://localhost:4321/plugins`
Check: Hover over plugin cards
Expected: Card lifts up with subtle shadow

**Step 5: Commit card hover enhancements**

```bash
git add src/styles/components/plugin-spread.css
git commit -m "feat: add hover lift effect to plugin cards"
```

---

## Task 8: Improve Code Block Styling

**Files:**
- Modify: `src/styles/components/plugin-page.css`
- Modify: `src/styles/components/blog-post.css`

**Step 1: Add code block base styles to plugin pages**

In `plugin-page.css`, add or update code/pre styles:

```css
code {
  font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace;
  font-size: var(--text-sm);
}

pre {
  background: var(--color-code-bg);
  border: 1px solid var(--color-code-border);
  border-radius: 8px;
  padding: var(--space-5);
  overflow-x: auto;
  line-height: 1.6;
}

pre code {
  background: none;
  padding: 0;
  border-radius: 0;
  font-size: var(--text-sm);
}
```

**Step 2: Add inline code styles**

```css
p code,
li code {
  background: var(--color-gray-100);
  padding: 0.125rem 0.375rem;
  border-radius: 4px;
  font-size: 0.875em;
}
```

**Step 3: Apply same code styles to blog posts**

Copy the code block styles to `blog-post.css` in the prose styles section.

**Step 4: Test code block appearance**

Run: `npm run dev`
Visit: `http://localhost:4321/plugins/google-ads`
Check: Code blocks have rounded corners, lighter background, subtle border
Expected: Less harsh appearance, better integration with page

**Step 5: Commit code block improvements**

```bash
git add src/styles/components/plugin-page.css src/styles/components/blog-post.css
git commit -m "feat: improve code block styling with borders and rounded corners"
```

---

## Task 9: Enhance Section Spacing

**Files:**
- Modify: `src/styles/components/home.css:2-6`
- Modify: `src/styles/components/blog-index.css`

**Step 1: Increase home section padding**

Update `.home-section`:

```css
.home-section {
  max-width: 1280px;
  margin: 0 auto;
  padding: var(--section-gap) var(--space-7);
}
```

**Step 2: Update mobile section padding**

In mobile media query:

```css
@media (max-width: 768px) {
  .home-section {
    padding: var(--content-gap) var(--space-6);
  }

  /* Add mobile spacing tokens */
  :root {
    --section-gap: 6rem;
    --content-gap: 4rem;
    --element-gap: 2rem;
  }
}
```

**Step 3: Apply to blog index if exists**

Similar spacing updates to blog-index.css for consistency.

**Step 4: Visual test spacing**

Run: `npm run dev`
Visit all pages: `/`, `/plugins`, `/blog`, `/about`
Check: More generous white space between sections
Expected: Sections feel less cramped, better breathing room

**Step 5: Commit spacing improvements**

```bash
git add src/styles/components/home.css src/styles/components/blog-index.css
git commit -m "feat: increase section spacing for better visual rhythm"
```

---

## Task 10: Add Link Underlines and Hover States

**Files:**
- Modify: `src/styles/components/blog-post.css`
- Modify: `src/styles/components/plugin-page.css`

**Step 1: Style inline content links in blog posts**

In blog-post.css prose section:

```css
.blog-post__content a {
  color: var(--color-accent-blue);
  text-decoration: underline;
  text-decoration-thickness: 1px;
  text-underline-offset: 2px;
  transition: color 200ms ease-out;
}

.blog-post__content a:hover {
  color: var(--color-accent-blue-hover);
}
```

**Step 2: Apply same link styles to plugin pages**

Copy similar rules to plugin-page.css for article links.

**Step 3: Style "Back to..." navigation links**

```css
.back-link {
  color: var(--color-text-muted);
  transition: color 200ms ease-out;
}

.back-link:hover {
  color: var(--color-accent-blue);
}
```

**Step 4: Test link interactions**

Run: `npm run dev`
Visit: `http://localhost:4321/blog/hello-world`
Check: Links have underlines, color changes on hover
Expected: Clear visual affordance for clickable links

**Step 5: Commit link enhancements**

```bash
git add src/styles/components/blog-post.css src/styles/components/plugin-page.css
git commit -m "feat: add underlines and hover states to content links"
```

---

## Task 11: QA - Visual Testing

**Files:**
- None (testing only)

**Step 1: Test all pages in light mode**

```bash
npm run dev
```

Visit and verify:
- `/` - Hero typography, button hovers, spacing
- `/plugins` - Category colors, card hovers
- `/plugins/google-ads` - Typography, code blocks, links
- `/blog` - Typography, spacing
- `/blog/hello-world` - Typography, code blocks, links, spacing
- `/about` - Typography, spacing

Expected: All visual enhancements applied consistently

**Step 2: Toggle to dark mode and retest**

Click theme switcher to dark mode
Revisit all pages
Check: Code block borders visible, shadows appropriate, colors have good contrast
Expected: Dark mode works well with all enhancements

**Step 3: Test mobile viewport**

Resize browser to 375px width
Revisit all pages
Check: Typography scales down, spacing adjusts, touch targets are adequate
Expected: Mobile experience is refined

**Step 4: Test keyboard navigation**

Tab through all pages
Check: Focus states visible on buttons and links
Expected: Clear focus indicators throughout

**Step 5: Document any issues found**

Create notes:
```bash
echo "## QA Notes" > qa-notes.md
echo "- [ ] Issue 1" >> qa-notes.md
echo "- [ ] Issue 2" >> qa-notes.md
```

---

## Task 12: Final Commit and Build Test

**Files:**
- None (verification only)

**Step 1: Run build to check for errors**

```bash
npm run build
```

Expected: Build succeeds with no TypeScript or Astro errors

**Step 2: Test production preview**

```bash
npm run preview
```

Visit: http://localhost:4321
Check: All enhancements work in production build
Expected: Same appearance as dev mode

**Step 3: Review all commits**

```bash
git log --oneline -15
```

Expected: ~12 commits with clear, descriptive messages following pattern:
- "feat: add DM Sans variable font"
- "feat: expand design token system..."
- etc.

**Step 4: Create summary commit if needed**

If there were bug fixes during QA:

```bash
git add .
git commit -m "fix: resolve QA issues from visual testing"
```

**Step 5: Document completion**

```bash
echo "Design enhancement implementation complete" >> qa-notes.md
echo "All 12 tasks finished successfully" >> qa-notes.md
git add qa-notes.md
git commit -m "docs: add QA notes and completion summary"
```

---

## Success Criteria

After completing all tasks, verify:

- [ ] DM Sans loads and applies to all headings
- [ ] H1 headings are dramatically larger (7rem desktop, 4rem mobile)
- [ ] Category badges use color-coded backgrounds
- [ ] Buttons have smooth hover animations with lift and shadow
- [ ] Plugin cards have hover states with transform and shadow
- [ ] Code blocks use lighter background with borders
- [ ] Inline links have underlines and color changes
- [ ] Section spacing is more generous (128px desktop, 96px mobile)
- [ ] Focus states are visible for keyboard navigation
- [ ] Dark mode works correctly with all enhancements
- [ ] Mobile viewport has appropriate scaling
- [ ] Build succeeds without errors

---

## Notes

- Each task builds on previous tasks - complete in order
- Test frequently in browser to catch issues early
- Commit after each task for clean git history
- If a step fails, debug before proceeding
- Reference design spec document for detailed token values
