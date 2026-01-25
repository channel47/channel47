---
name: editorial-spacing-hierarchy
description: "Detect and fix spacing and visual hierarchy issues in editorial web design. Analyzes typography, whitespace, proximity relationships, and vertical rhythm. Outputs better-designed pages with principled corrections. Triggers on: fix spacing, improve hierarchy, audit typography, make this look better, why does this feel off."
---

# Editorial Spacing & Visual Hierarchy

You're not decorating pages. You're controlling how eyes move through content.

Spacing isn't about "looking clean." It's about relationships. Every pixel of whitespace is a signal: *these things belong together* or *these things are separate*. Get it wrong and readers feel friction they can't name. Get it right and content feels inevitable.

This skill turns you into the designer who sees what others feel.

---

## The Only Three Things That Matter

Before you touch anything, understand what spacing actually does:

**1. Grouping** — Proximity tells readers what belongs together. A heading 48px above a paragraph but only 16px below it? That heading *owns* that paragraph. Equal spacing above and below? The heading floats, orphaned, belonging to nothing.

**2. Hierarchy** — Size ratios and spacing ratios work together. A 48px heading needs breathing room a 16px caption doesn't. Cramped large type feels wrong. Generous small type feels wasteful.

**3. Rhythm** — Consistent intervals create unconscious harmony. When margins are 24, 48, 72, 96 — all multiples of 24 — the page feels composed. When they're 23, 51, 68, 94 — arbitrary — something feels amateur.

Everything else is implementation details.

---

## The Feel Vocabulary

Experts don't say "the spacing is incorrect." They describe what's wrong in visceral terms. Learn this language — it's how you communicate issues and recognize them.

| Term | What It Means | What's Wrong |
|------|---------------|--------------|
| **Cramped** | Elements too close, fighting for space | Insufficient padding/margins, line-height too tight |
| **Airy** | Excessive whitespace, elements disconnected | Margins too large, content feels scattered |
| **Floaty** | Element doesn't belong to anything | Equal spacing above and below, no proximity anchor |
| **Heavy** | Element dominates inappropriately | Too large, too bold, or too much spacing around it |
| **Light** | Element disappears, lacks presence | Too small, too subtle, insufficient spacing to breathe |
| **Dense** | Wall of content, overwhelming | Insufficient paragraph/section spacing, line-height too tight |
| **Loose** | Content feels scattered, uncommitted | Too much space between related elements |
| **Tight** | Controlled, intentional compression | Deliberate reduction of space (can be good or bad) |
| **Breathing room** | Adequate space for element to exist | Proper margins allowing visual rest |
| **Orphaned** | Element cut off from its group | Single word on line, heading between sections |
| **Competing** | Multiple elements fighting for attention | Insufficient hierarchy contrast |
| **Anchored** | Element clearly connected to its context | Proper proximity relationships |
| **Rhythm** | Consistent vertical intervals | Spacing multiples of baseline |
| **Janky** | Something feels off, unprofessional | Usually arbitrary spacing values |

When you analyze a page, describe problems in these terms. "The heading feels floaty" is more useful than "the margin-top and margin-bottom are equal." The former describes the *effect*, which points to the *cause*.

---

## The Detection Framework

When you analyze a page, run through these checks in order. Each reveals a category of problems.

### 1. Spacing System Audit

**What to look for:** Are spacing values constrained to a system, or arbitrary?

Pull the actual CSS values. Good editorial sites use an 8pt grid:
- Margins/padding: 8, 16, 24, 32, 40, 48, 56, 64...
- Line-heights in 4pt increments: 20, 24, 28, 32...

**Red flags:**
- Values like 13px, 17px, 22px, 37px (not divisible by 4 or 8)
- Different spacing values that serve the same purpose (one card has 24px padding, another has 20px)
- No apparent relationship between spacing values

**The fix:** Establish an 8pt base. Snap all values to the nearest multiple. Use 4pt only for fine-tuning line-height or icon alignment.

```css
/* Before: Arbitrary chaos */
.article { padding: 22px 35px; }
.card { margin-bottom: 18px; }
.section { gap: 43px; }

/* After: 8pt system */
.article { padding: 24px 32px; }
.card { margin-bottom: 16px; }
.section { gap: 48px; }
```

### 2. Type Scale Analysis

**What to look for:** Is there a mathematical relationship between font sizes?

Good editorial typography uses a modular scale. Common ratios:
- **1.200 (Minor Third):** Subtle, elegant — 16, 19, 23, 28, 33
- **1.250 (Major Third):** Balanced contrast — 16, 20, 25, 31, 39
- **1.333 (Perfect Fourth):** Strong hierarchy — 16, 21, 28, 37, 50

**Red flags:**
- Sizes that don't follow a ratio: 14, 16, 18, 22, 28, 36 (what's the relationship?)
- Too many sizes (6+ distinct sizes = visual noise)
- Insufficient contrast between levels (H2 at 20px, body at 18px — barely different)
- H1 to body ratio less than 2:1 (weak hierarchy)

**The fix:** Pick a ratio. Derive all sizes from it. Limit yourself to 4-5 sizes total.

```css
/* Before: Random sizes */
h1 { font-size: 36px; }
h2 { font-size: 28px; }
h3 { font-size: 22px; }
p { font-size: 17px; }
caption { font-size: 13px; }

/* After: 1.25 ratio from 16px base */
h1 { font-size: 39px; }  /* 16 × 1.25³ */
h2 { font-size: 31px; }  /* 16 × 1.25² */
h3 { font-size: 25px; }  /* 16 × 1.25¹ */
p { font-size: 16px; }   /* base */
caption { font-size: 13px; } /* 16 ÷ 1.25 */
```

### 3. Proximity Relationships

**What to look for:** Do spatial relationships communicate content relationships?

This is where most pages fail. The Gestalt principle of proximity: things close together appear related.

**Red flags:**

**Floating headings** — Equal space above and below. The heading belongs to *nothing*.
```
[Previous paragraph]
        ↕ 32px
     [Heading]
        ↕ 32px  ← WRONG: Heading orphaned
[Next paragraph]
```

**Fix:** Space above should be 2-3× space below.
```
[Previous paragraph]
        ↕ 48px
     [Heading]
        ↕ 16px  ← RIGHT: Heading owns what follows
[Next paragraph]
```

**Detached labels** — Form labels equidistant between fields.
```
[Input field 1]
      ↕ 16px
    [Label]      ← Which field does this label belong to?
      ↕ 16px
[Input field 2]
```

**Fix:** Label should be 2-3× closer to its field than to adjacent elements.

**Cramped captions** — Image captions touching or too close to the image.
```
[Image]
[Caption text right against it]  ← Feels suffocating
```

**Fix:** Give captions breathing room (8-12px), but keep them clearly closer to their image than to following content.

### 4. Line Metrics

**What to look for:** Are the fundamentals of readable typography in place?

**Line length (measure):**
- Optimal: 45-75 characters per line
- Ideal for long-form: 66 characters
- Red flag: Full-width text on large screens (100+ characters)
- Red flag: Narrow columns under 40 characters

**Line height:**
- Body text: 1.4-1.6 (140-160%)
- Headings: 1.1-1.3 (tighter for large text)
- Red flag: Line height under 1.3 for body (cramped)
- Red flag: Line height over 1.8 for body (disconnected lines)

**Paragraph spacing:**
- Should exceed line-height
- Typical: 1.5× to 2× the line-height value
- Red flag: Paragraph spacing equal to line-height (paragraphs don't separate)
- Red flag: Massive paragraph gaps (3×+ line-height) that fragment content

```css
/* Before: Problematic */
p {
  font-size: 16px;
  line-height: 1.2;        /* Too tight */
  max-width: none;         /* Lines too long */
  margin-bottom: 1em;      /* Matches line-height — weak separation */
}

/* After: Readable */
p {
  font-size: 18px;
  line-height: 1.6;        /* Comfortable */
  max-width: 65ch;         /* Optimal measure */
  margin-bottom: 1.5em;    /* Clear paragraph breaks */
}
```

### 5. Vertical Rhythm

**What to look for:** Do vertical spacing values share a common denominator?

Vertical rhythm means all spacing derives from a single base unit — typically the body line-height.

If body text is 18px with 1.5 line-height = 27px baseline unit.

Good rhythm: margins of 27, 54, 81, 108...
Bad rhythm: margins of 24, 40, 65, 100...

**How to check:**
1. Identify the body line-height (e.g., 24px)
2. Check if major spacing values are multiples: 24, 48, 72, 96
3. Look for off-rhythm values that break the pattern

**Red flags:**
- Spacing values that aren't multiples of line-height
- Images/components that break text alignment across columns
- Inconsistent section spacing (one section has 64px margin, next has 80px)

**The fix:** Derive spacing scale from line-height.

```css
:root {
  --baseline: 24px;
  --space-1: calc(var(--baseline) * 1);   /* 24px */
  --space-2: calc(var(--baseline) * 2);   /* 48px */
  --space-3: calc(var(--baseline) * 3);   /* 72px */
  --space-4: calc(var(--baseline) * 4);   /* 96px */
}
```

### 6. Internal vs. External Spacing

**What to look for:** Is padding inside elements smaller than margins between them?

The rule: **Internal ≤ External**

A card with 32px padding surrounded by 24px margins? The internal space is greater than external. The card feels like it's bulging outward, disconnected from the layout.

**Red flags:**
- Component padding > component margins
- Button padding that exceeds space between buttons
- Cards with more internal whitespace than the gaps between them

**The fix:** Tighten internal spacing or increase external spacing until internal ≤ external.

```css
/* Before: Internal > External */
.card {
  padding: 32px;
  margin-bottom: 24px;  /* Card feels bloated */
}

/* After: Internal ≤ External */
.card {
  padding: 24px;
  margin-bottom: 32px;  /* Card feels contained */
}
```

### 7. Optical Alignment

**What to look for:** Are asymmetric elements visually balanced, or just mathematically centered?

Software aligns bounding boxes. Eyes perceive visual weight.

**Common failures:**

**Play buttons:** Triangle centered by bounds looks left-heavy. Shift right 5-10%.

**Circular icons next to text:** Circle at same height as square icons looks smaller. Increase circle by ~10%.

**Text in buttons:** Mathematically centered text often looks low. Nudge up 1-2px.

**Hanging punctuation:** Quotation marks and bullets at left edge create visual indent. Let them hang outside the text block for optical alignment.

**Drop caps:** Aligned to text box top leaves gap. Align to cap-height of adjacent text.

**How to check:** Squint. If something looks off-center, it is. Mathematical centering is a starting point, not the answer.

---

---

## Detection Protocol: Extracting Values from a Live Page

Theory is useless if you can't see the actual numbers. Here's how to systematically audit a page.

### Step 1: Capture the Type Scale

Extract all font sizes on the page and identify the ratio.

```javascript
// Run in browser console to extract all font sizes
const elements = document.querySelectorAll('h1, h2, h3, h4, h5, h6, p, span, a, li, figcaption, blockquote');
const sizes = new Set();

elements.forEach(el => {
  const size = parseFloat(window.getComputedStyle(el).fontSize);
  sizes.add(size);
});

const sortedSizes = [...sizes].sort((a, b) => b - a);
console.log('Font sizes found:', sortedSizes);

// Calculate ratios between adjacent sizes
for (let i = 0; i < sortedSizes.length - 1; i++) {
  const ratio = sortedSizes[i] / sortedSizes[i + 1];
  console.log(`${sortedSizes[i]}px / ${sortedSizes[i + 1]}px = ${ratio.toFixed(3)}`);
}
```

**What you're looking for:**
- Consistent ratios (1.2, 1.25, 1.333) = intentional scale
- Random ratios (1.17, 1.31, 1.09) = arbitrary sizing
- Too many sizes (8+) = needs consolidation

### Step 2: Map the Spacing System

Extract margins and paddings to find the grid.

```javascript
// Extract spacing values from key elements
const containers = document.querySelectorAll('article, section, .card, .container, main, aside');
const spacings = [];

containers.forEach(el => {
  const style = window.getComputedStyle(el);
  spacings.push({
    element: el.tagName + (el.className ? '.' + el.className.split(' ')[0] : ''),
    marginTop: parseFloat(style.marginTop),
    marginBottom: parseFloat(style.marginBottom),
    paddingTop: parseFloat(style.paddingTop),
    paddingBottom: parseFloat(style.paddingBottom),
    paddingLeft: parseFloat(style.paddingLeft),
    paddingRight: parseFloat(style.paddingRight)
  });
});

console.table(spacings);

// Find the likely grid unit (GCD of all values)
const allValues = spacings.flatMap(s => [s.marginTop, s.marginBottom, s.paddingTop, s.paddingBottom])
  .filter(v => v > 0);
console.log('All spacing values:', [...new Set(allValues)].sort((a, b) => a - b));
```

**What you're looking for:**
- Values divisible by 8 (8, 16, 24, 32...) = 8pt grid
- Values divisible by 4 but not 8 = 4pt grid
- No common divisor = arbitrary spacing

### Step 3: Audit Proximity Relationships

Check heading-to-content ratios.

```javascript
// Check space above vs below headings
document.querySelectorAll('h1, h2, h3, h4').forEach(heading => {
  const style = window.getComputedStyle(heading);
  const above = parseFloat(style.marginTop);
  const below = parseFloat(style.marginBottom);
  const ratio = above / below;
  
  console.log(`${heading.tagName}: ${above}px above, ${below}px below (ratio: ${ratio.toFixed(2)})`);
  
  if (ratio < 1.5) {
    console.warn(`⚠️ ${heading.tagName} may be floating — space above should be 2-3× space below`);
  }
});
```

**What you're looking for:**
- Ratio ≥ 2:1 (above:below) = heading attached to its content
- Ratio ≈ 1:1 = floating heading (problem)
- Ratio < 1:1 = heading detached from what follows (bigger problem)

### Step 4: Measure Line Metrics

Check readability fundamentals.

```javascript
// Audit body text readability
const bodyText = document.querySelector('article p, .content p, main p');
if (bodyText) {
  const style = window.getComputedStyle(bodyText);
  const fontSize = parseFloat(style.fontSize);
  const lineHeight = parseFloat(style.lineHeight);
  const width = bodyText.offsetWidth;
  
  // Estimate characters per line (rough: width / (fontSize * 0.5))
  const charsPerLine = Math.round(width / (fontSize * 0.5));
  const lineHeightRatio = lineHeight / fontSize;
  
  console.log('Body text metrics:');
  console.log(`  Font size: ${fontSize}px`);
  console.log(`  Line height: ${lineHeight}px (${lineHeightRatio.toFixed(2)} ratio)`);
  console.log(`  Estimated chars/line: ${charsPerLine}`);
  console.log(`  Container width: ${width}px`);
  
  // Warnings
  if (charsPerLine > 90) console.warn('⚠️ Lines too long — aim for 45-75 characters');
  if (charsPerLine < 40) console.warn('⚠️ Lines too short — aim for 45-75 characters');
  if (lineHeightRatio < 1.4) console.warn('⚠️ Line height too tight — aim for 1.4-1.6');
  if (lineHeightRatio > 1.8) console.warn('⚠️ Line height too loose — aim for 1.4-1.6');
}
```

### Step 5: Check Internal vs External

Verify padding doesn't exceed margins.

```javascript
// Check cards, boxes, components
document.querySelectorAll('.card, [class*="card"], article > div, .box').forEach(el => {
  const style = window.getComputedStyle(el);
  const padding = Math.max(
    parseFloat(style.paddingTop),
    parseFloat(style.paddingBottom)
  );
  const margin = Math.max(
    parseFloat(style.marginTop),
    parseFloat(style.marginBottom)
  );
  
  if (padding > margin && margin > 0) {
    console.warn(`⚠️ Internal > External on ${el.className}: padding ${padding}px > margin ${margin}px`);
  }
});
```

### Step 6: Visual Rhythm Check

Overlay a baseline grid to see alignment.

```javascript
// Add visual baseline grid overlay
function showBaselineGrid(baseline = 24) {
  const overlay = document.createElement('div');
  overlay.id = 'baseline-grid';
  overlay.style.cssText = `
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    pointer-events: none;
    z-index: 99999;
    background: repeating-linear-gradient(
      to bottom,
      transparent 0,
      transparent ${baseline - 1}px,
      rgba(255, 0, 0, 0.15) ${baseline - 1}px,
      rgba(255, 0, 0, 0.15) ${baseline}px
    );
  `;
  document.body.appendChild(overlay);
  console.log(`Baseline grid overlay added (${baseline}px). Run document.getElementById('baseline-grid').remove() to hide.`);
}

showBaselineGrid(24); // Adjust baseline as needed
```

**What you're looking for:**
- Text baselines landing on grid lines = good rhythm
- Elements consistently spanning whole grid units = intentional
- Random alignment = no vertical rhythm system

---

## Responsive Spacing Strategy

Spacing isn't fixed — it must breathe across viewport sizes. Here's how to think about it.

### The Principle: Proportional, Not Fixed

Don't just shrink everything on mobile. Relationships matter more than absolute values.

| Viewport | Approach |
|----------|----------|
| **Mobile (<640px)** | Tighter spacing, smaller type, maintained ratios |
| **Tablet (640-1024px)** | Moderate spacing, baseline type size |
| **Desktop (>1024px)** | Generous spacing, potentially larger type |

### Spacing Scale Across Breakpoints

If desktop uses an 8pt grid with 24px baseline:

```css
:root {
  /* Mobile-first: tighter base */
  --baseline: 20px;
  --space-xs: 4px;
  --space-sm: 8px;
  --space-md: 16px;
  --space-lg: 24px;
  --space-xl: 40px;
  --space-2xl: 64px;
}

@media (min-width: 768px) {
  :root {
    /* Tablet: standard base */
    --baseline: 24px;
    --space-xs: 4px;
    --space-sm: 8px;
    --space-md: 16px;
    --space-lg: 32px;
    --space-xl: 48px;
    --space-2xl: 80px;
  }
}

@media (min-width: 1280px) {
  :root {
    /* Desktop: generous base */
    --baseline: 28px;
    --space-xs: 8px;
    --space-sm: 12px;
    --space-md: 24px;
    --space-lg: 40px;
    --space-xl: 64px;
    --space-2xl: 96px;
  }
}
```

### Type Scale Across Breakpoints

Use a tighter ratio on mobile to prevent massive headings.

```css
:root {
  /* Mobile: Minor Third (1.2) — tighter scale */
  --text-sm: 0.833rem;   /* 13px */
  --text-base: 1rem;      /* 16px */
  --text-lg: 1.2rem;      /* 19px */
  --text-xl: 1.44rem;     /* 23px */
  --text-2xl: 1.728rem;   /* 28px */
  --text-3xl: 2.074rem;   /* 33px */
}

@media (min-width: 768px) {
  :root {
    /* Tablet+: Major Third (1.25) — more contrast */
    --text-sm: 0.8rem;    /* 13px */
    --text-base: 1rem;     /* 16px */
    --text-lg: 1.25rem;    /* 20px */
    --text-xl: 1.563rem;   /* 25px */
    --text-2xl: 1.953rem;  /* 31px */
    --text-3xl: 2.441rem;  /* 39px */
  }
}

@media (min-width: 1280px) {
  :root {
    /* Desktop: Perfect Fourth (1.333) — strong hierarchy */
    --text-sm: 0.75rem;   /* 12px */
    --text-base: 1rem;     /* 16px */
    --text-lg: 1.333rem;   /* 21px */
    --text-xl: 1.777rem;   /* 28px */
    --text-2xl: 2.369rem;  /* 38px */
    --text-3xl: 3.157rem;  /* 51px */
  }
}
```

### Line Length Across Breakpoints

```css
.article-body {
  /* Mobile: full width with padding */
  max-width: 100%;
  padding-inline: var(--space-md);
}

@media (min-width: 640px) {
  .article-body {
    /* Tablet+: constrained measure */
    max-width: 65ch;
    padding-inline: var(--space-lg);
    margin-inline: auto;
  }
}
```

### What Stays Constant

Some things shouldn't change much:
- **Line-height ratios** (1.5 is 1.5 at any size)
- **Proximity ratios** (heading space above:below stays 2-3:1)
- **Internal ≤ External rule** (applies at all breakpoints)
- **Type scale ratio consistency** within a breakpoint

---

## Editorial Typography Deep Dive

Editorial design has specific typographic elements that need special handling.

### Drop Caps

The oversized first letter of an article.

**Common mistakes:**
- Drop cap aligned to text bounding box (leaves gap at top)
- Drop cap too far from following text
- Line height of first paragraph breaks around drop cap awkwardly

**Correct implementation:**

```css
.article-body > p:first-of-type::first-letter {
  float: left;
  font-size: 4.5em;
  line-height: 0.8;
  padding-right: 0.1em;
  margin-top: 0.05em; /* Optical alignment to cap-height */
  font-weight: 700;
  color: var(--color-accent);
}
```

**Key points:**
- `line-height: 0.8` or lower to pull it up
- Small `margin-top` for optical alignment with adjacent text cap-height
- `padding-right` for breathing room from text
- 3-4 lines of text should wrap beside it

### Pull Quotes

Extracted quotes that break the text flow for emphasis.

**Spacing rules:**
- More space around pull quotes than standard paragraphs (2-3× baseline)
- Quote should feel like a deliberate pause, not an interruption
- Asymmetric spacing can create visual interest (more above than below, or vice versa)

```css
.pull-quote {
  margin-block: calc(var(--baseline) * 3);
  padding-block: calc(var(--baseline) * 1);
  border-left: 3px solid var(--color-accent);
  padding-left: var(--space-lg);
  font-size: var(--text-xl);
  line-height: 1.4;
  font-style: italic;
}

/* Or centered style */
.pull-quote--centered {
  margin-block: calc(var(--baseline) * 3);
  padding-block: calc(var(--baseline) * 1.5);
  text-align: center;
  font-size: var(--text-2xl);
  line-height: 1.3;
  max-width: 80%;
  margin-inline: auto;
}
```

### Block Quotes

Quoted passages within the text (not pulled out for emphasis).

**Different from pull quotes:**
- Less dramatic spacing
- Smaller size increase (or same size, just indented)
- Clear attribution styling

```css
blockquote {
  margin-block: calc(var(--baseline) * 1.5);
  margin-left: var(--space-lg);
  padding-left: var(--space-md);
  border-left: 2px solid var(--color-border);
  font-size: inherit; /* Or slightly smaller: 0.95em */
  color: var(--color-text-muted);
}

blockquote cite,
blockquote footer {
  display: block;
  margin-top: var(--space-sm);
  font-size: var(--text-sm);
  font-style: normal;
  color: var(--color-text-tertiary);
}

blockquote cite::before {
  content: "— ";
}
```

### Figure Captions

Text describing images, charts, or diagrams.

**Spacing rules:**
- Caption closer to its image than to surrounding content
- But not touching — 8-16px gap
- Clearly subordinate (smaller, lighter)

```css
figure {
  margin-block: calc(var(--baseline) * 2);
}

figure img {
  display: block;
  width: 100%;
}

figcaption {
  margin-top: var(--space-sm); /* 8-12px — close but not touching */
  font-size: var(--text-sm);
  line-height: 1.4;
  color: var(--color-text-secondary);
}

/* If caption is long, constrain width */
figcaption {
  max-width: 90%;
}
```

### Bylines and Metadata

Author, date, reading time, categories.

**Hierarchy:**
- Clearly subordinate to headline and deck
- Grouped together (proximity)
- Often different type treatment (sans-serif if body is serif, or vice versa)

```css
.article-meta {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-sm) var(--space-md);
  margin-top: var(--space-lg);
  margin-bottom: calc(var(--baseline) * 2);
  font-size: var(--text-sm);
  color: var(--color-text-tertiary);
  font-family: var(--font-sans); /* Contrast with serif body */
}

.article-meta a {
  color: var(--color-text-secondary);
  text-decoration: underline;
  text-decoration-color: var(--color-border);
  text-underline-offset: 2px;
}
```

### Section Breaks

Visual separators between major sections.

**Options:**
- Extra whitespace (3-4× baseline)
- Horizontal rule (subtle, not heavy)
- Ornament or symbol (※, ◆, ●●●)

```css
.section-break {
  margin-block: calc(var(--baseline) * 4);
  text-align: center;
  color: var(--color-text-tertiary);
}

/* Whitespace only */
.section-break--space {
  margin-block: calc(var(--baseline) * 5);
}

/* Subtle rule */
.section-break--rule {
  border: none;
  border-top: 1px solid var(--color-border);
  max-width: 100px;
  margin-inline: auto;
}

/* Ornament */
.section-break--ornament::before {
  content: "* * *";
  letter-spacing: 0.5em;
}
```

### Lists in Editorial Content

Lists need special care in long-form reading.

**Spacing rules:**
- Space before and after list = standard paragraph spacing (or slightly more)
- Space between list items = less than paragraph spacing, but more than line-height
- Nested lists: tighter spacing, clear indentation

```css
article ul,
article ol {
  margin-block: calc(var(--baseline) * 1.25);
  padding-left: var(--space-lg);
}

article li {
  margin-bottom: calc(var(--baseline) * 0.5);
  padding-left: var(--space-xs);
}

article li:last-child {
  margin-bottom: 0;
}

/* Nested lists */
article li ul,
article li ol {
  margin-top: calc(var(--baseline) * 0.5);
  margin-bottom: 0;
}
```

---

## The Hierarchy Checklist

For editorial content, hierarchy should be instantly scannable. Run this test:

1. **Can you identify the H1 in under 1 second?** If it doesn't dominate, increase size or weight.

2. **Is there clear differentiation between H1 → H2 → H3?** Each level should be obviously distinct — not just slightly smaller.

3. **Does body text recede?** It should feel comfortable, not competing with headings.

4. **Are metadata and captions clearly subordinate?** Smaller, lighter, or muted color.

5. **Do CTAs stand out without screaming?** Contrast through color or weight, not size inflation.

**Size relationships that work:**
- H1: 2.5-3× body size
- H2: 1.75-2× body size
- H3: 1.25-1.5× body size
- Caption/meta: 0.8-0.9× body size

---

## Editorial-Specific Patterns

Editorial design has conventions that readers expect. Violate them carefully.

### Article Headers
- Headline dominates
- Deck/subhead clearly secondary (60-70% of headline size)
- Byline and date are metadata — small, muted
- Generous space before body begins (2-3× standard paragraph spacing)

### Body Content
- Single column for reading (multi-column only for specific layouts)
- 65-75ch line length
- Clear paragraph separation
- Pull quotes break rhythm intentionally — more space around them
- Images have breathing room (at least 1 baseline unit above and below)

### Sidebars and Asides
- Clearly separated from main content
- Either boxed (background/border) or spatially distinct
- Type slightly smaller than body (0.85-0.9×)

### Navigation and UI
- Should not compete with content
- Lighter weight or smaller size than body
- Consistent spacing patterns (all nav items same padding)

---

## The Fix Protocol

When you identify issues, fix them in this order:

1. **Establish spacing system** — Define 8pt grid, derive all values from it
2. **Set type scale** — Pick ratio, limit sizes, ensure sufficient contrast
3. **Fix proximity** — Headings own their content, groups are clear
4. **Tune line metrics** — Length, height, paragraph spacing
5. **Align to rhythm** — Spacing multiples of baseline
6. **Check internal/external** — Padding never exceeds margins
7. **Optical adjustments** — Last pass for visual balance

---

## What Good Looks Like vs. What Bad Looks Like

### Spacing

**Bad:**
```
Margins: 15px, 22px, 30px, 45px, 67px
Padding: 12px, 18px, 25px, 40px
No discernible system. Every value is a new decision.
```

**Good:**
```
Margins: 16px, 24px, 32px, 48px, 64px
Padding: 8px, 16px, 24px, 32px
8pt grid. Values feel related. Decisions are constrained.
```

### Hierarchy

**Bad:**
```
H1: 28px
H2: 24px
H3: 20px
Body: 16px
Caption: 14px

Sizes too similar. Hierarchy unclear. Everything competes.
```

**Good:**
```
H1: 48px (3× body)
H2: 32px (2× body)
H3: 24px (1.5× body)
Body: 16px
Caption: 13px

Clear jumps. Instant recognition. Nothing competes.
```

### Proximity

**Bad:**
```
[Paragraph ends]
      40px gap
   [H2 Heading]
      40px gap        ← Heading floats between sections
[Paragraph begins]
```

**Good:**
```
[Paragraph ends]
      64px gap        ← Clear section break
   [H2 Heading]
      24px gap        ← Heading attached to its content
[Paragraph begins]
```

---

## Quick Reference: The Numbers

| Element | Value | Notes |
|---------|-------|-------|
| Body font size | 16-20px | 18px is safe for editorial |
| Body line-height | 1.5-1.6 | 1.55 is versatile |
| Line length | 65ch | Use `max-width: 65ch` |
| Paragraph spacing | 1.5em | Or 1× baseline unit |
| H1 size | 2.5-3× body | 48px if body is 18px |
| Heading space above | 2-3× space below | Attach to what follows |
| Section spacing | 3-4× baseline | 72-96px if baseline is 24px |
| Card padding | ≤ card margins | Internal ≤ External |
| ALL CAPS tracking | +0.05-0.1em | Always add letter-spacing |

---

## When to Break the Rules

Rules exist to solve common problems. Break them when:

- **Intentional tension:** A cramped heading can feel urgent. Use deliberately.
- **Brand voice:** Some brands are dense, some are airy. Consistency > formula.
- **Specific content:** A data table needs tighter spacing than a meditation app.
- **Visual weight:** A heavy image might need asymmetric spacing to balance.

But when you break rules, break them *consistently* and *intentionally*. Arbitrary variation is not design.

---

## Verification Checklist

After making changes, run these checks to confirm improvement.

### Visual Verification

**The Squint Test**
Squint at the page until text blurs. You should still see:
- Clear hierarchy (what's biggest, what's smallest)
- Distinct groupings (what belongs together)
- Balanced whitespace (no cramped areas, no voids)

If hierarchy disappears when squinted, contrast is insufficient.

**The Scroll Test**
Scroll through the page at moderate speed. Notice:
- Does rhythm feel consistent?
- Do headings clearly announce new sections?
- Are there jarring jumps in spacing?

Inconsistent rhythm creates subconscious friction.

**The Zoom Test**
View at 50%, 100%, and 150%. Check:
- Does hierarchy hold at all sizes?
- Do spacing relationships stay proportional?
- Is anything breaking (overlapping, colliding)?

**The Grayscale Test**
View in grayscale (browser DevTools can simulate). Verify:
- Hierarchy still clear without color?
- Sufficient contrast between text levels?
- Groupings still visible?

If your design depends on color for hierarchy, it's fragile.

### Metric Verification

Run the detection scripts again after changes. Confirm:

| Check | Before | After | Target |
|-------|--------|-------|--------|
| Font sizes follow ratio | No (1.14, 1.23, 1.31) | Yes (1.25, 1.25, 1.25) | Consistent ratio |
| Spacing on grid | 23, 37, 51px | 24, 40, 48px | Multiples of 8 |
| Line length | 102 chars | 68 chars | 45-75 chars |
| Line height | 1.3 | 1.55 | 1.4-1.6 |
| Heading space ratio | 1.0:1 | 2.5:1 | ≥2:1 above:below |
| Internal vs external | 32px pad, 24px margin | 24px pad, 32px margin | Internal ≤ External |

### Reading Verification

Actually read a section of the content. Notice:
- Eye fatigue? (Line length or height issues)
- Losing your place? (Insufficient paragraph spacing)
- Headings feel connected to content? (Proximity working)
- Can you skim effectively? (Hierarchy working)

### Comparison Verification

Place before and after screenshots side by side.

Ask:
- Which feels more professional?
- Which is easier to scan?
- Which would you trust more?

If the answer isn't clearly "after," keep iterating.

### Code Verification

Review the CSS changes:

```css
/* Check 1: Are all spacing values on the grid? */
/* Bad: 23px, 37px, 51px */
/* Good: 24px, 40px, 48px */

/* Check 2: Are values using CSS custom properties? */
/* Bad: margin: 48px */
/* Good: margin: var(--space-xl) */

/* Check 3: Is the type scale derived from a ratio? */
/* Bad: font-size: 28px (arbitrary) */
/* Good: font-size: var(--text-2xl) (from scale) */

/* Check 4: Are breakpoints handled? */
/* Bad: Fixed values at all sizes */
/* Good: Responsive custom properties or clamp() */
```

### The Final Question

Look at the page and ask: **"Does this feel designed, or does it feel assembled?"**

Designed pages have intention. Every spacing value exists for a reason. Elements relate to each other through consistent systems.

Assembled pages have arbitrary decisions. Spacing varies without logic. Elements sit where they were placed without consideration of neighbors.

Your goal is designed.

---

## Remember

Spacing is information architecture made visible.

Every gap says "these are separate." Every tightening says "these belong together." Your job is to make those relationships so clear that readers never have to think about them.

When spacing is right, content feels effortless. When it's wrong, everything feels slightly broken — even if no one can say why.

You can now say why. Fix it.
