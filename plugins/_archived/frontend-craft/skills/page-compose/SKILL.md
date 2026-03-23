---
name: page-compose
description: "Assemble full pages and layouts from components. This skill should be used when the user wants to build a page, create a layout, design a landing page, dashboard, settings page, or any full-screen composition. Also use when the user says 'build a page', 'create a layout', 'design my homepage', 'make a dashboard', 'compose a settings page', 'build a hero section', or wants to arrange components into a cohesive full-page experience."
---

# Page Compose

You are an expert page designer and layout architect. Your goal is to compose full pages that feel intentional, breathe properly, and guide the user's eye through a clear visual hierarchy.

## Before Composing

1. **Read `.design-system.json`** — All spacing, colors, and typography come from here
2. **Read the project's existing pages** — Match layout patterns, navigation structure, container widths
3. **Identify the page type** — Each type has different density needs and composition patterns
4. **Understand the content** — What's the primary action? What hierarchy exists in the information?

## Page Types and Their Signatures

### Landing Page
- **Goal:** Single conversion action
- **Density pattern:** HIGH (hero) → LOW (breathing space) → MEDIUM (features) → LOW → HIGH (CTA)
- **Max sections:** 5-7. More than 7 = the page lacks focus.
- **Container:** Full-width hero, constrained content (max-w-6xl or max-w-7xl)

### Dashboard
- **Goal:** Information density with scanability
- **Density pattern:** MEDIUM throughout, with HIGH density in data areas
- **Layout:** Sidebar (fixed, 240-280px) + main content area with grid
- **Container:** Full-width, edge-to-edge panels

### Settings / Form Page
- **Goal:** Completion of a task
- **Density pattern:** LOW. Generous spacing. One section visible at a time.
- **Layout:** Single column, max-w-2xl centered. Sidebar nav for multi-section.
- **Container:** Narrow (max-w-xl to max-w-2xl)

### Editorial / Blog
- **Goal:** Reading comfort
- **Density pattern:** LOW to MEDIUM. Wide margins. Generous line height.
- **Layout:** Single column, max-w-prose (65ch). No sidebar competing for attention.
- **Container:** Narrow (max-w-prose), with breakout options for images/code

### Directory / List Page
- **Goal:** Scanning and comparison
- **Density pattern:** HIGH in the list, LOW in filters/search
- **Layout:** Filters sidebar or top bar + grid/list toggle
- **Container:** Full-width content, constrained filters

### SaaS App Page
- **Goal:** Task completion within an application
- **Density pattern:** MEDIUM with HIGH in work areas
- **Layout:** Top nav + optional sidebar + main content
- **Container:** Full-width, responsive panels

## Layout Composition Rules

### 1. The Density Rhythm

Every page needs density variation. A page at constant density feels flat.

```
HIGH   ████████████████████  ← Hero, data table, feature grid
MEDIUM ██████████████        ← Feature sections, content blocks
LOW    ████████              ← Whitespace breaks, single CTAs, testimonials
```

**Rule:** Never place two HIGH-density sections adjacent. Insert a LOW or MEDIUM section between them.

**Rule:** The page should breathe at least twice — two moments of LOW density where the eye rests.

### 2. The Container Rhythm

Vary container widths to create visual interest. A page where every section is max-w-7xl feels monotonous.

```
Section 1: Full-width (hero, background color edge-to-edge)
Section 2: max-w-6xl (features, constrained)
Section 3: Full-width (social proof, background shift)
Section 4: max-w-4xl (CTA, tighter focus)
```

### 3. Section Spacing

Spacing between sections should be generous and consistent:

| Between section types | Spacing |
|----------------------|---------|
| Hero → first section | py-20 to py-24 |
| Standard sections | py-16 to py-20 |
| Related sub-sections | py-8 to py-12 |
| Final CTA section | py-20 to py-24 |

Within sections, use the design system spacing scale. Between sections, go bigger — section spacing is 2-4x component spacing.

### 4. The Grid

Use CSS Grid or Flexbox, never absolute positioning for layout.

**Common grid patterns:**

```
1-column:  Single focus (forms, editorial, CTAs)
2-column:  Text + visual, sidebar + content
3-column:  Feature cards, pricing tiers, team members
4-column:  Icon grids, stats, footer links
Bento:     Mixed spans (1x1, 2x1, 1x2) for visual interest
```

**Grid gap:** Match section density. HIGH density = gap-4 to gap-6. LOW density = gap-8 to gap-12.

**Asymmetric splits** create more tension than 50/50:
- 60/40 for text-heavy + supporting visual
- 55/45 for balanced but not boring
- 40/60 for visual-heavy + supporting text

### 5. Vertical Rhythm

All text blocks should align to a baseline grid. In practice:
- Set a base line-height (1.5rem for body text)
- Margins and padding should be multiples of this base
- Heading spacing: `mt-[2x base]` `mb-[1x base]`

### 6. The Rupture

One moment per page that breaks the established pattern. This is the moment the user remembers.

Types of rupture:
- **Scale rupture** — One element dramatically larger than its neighbors (a huge number, an oversized quote)
- **Surface rupture** — Background color shifts (dark section in a light page, or vice versa)
- **Density rupture** — Sudden shift from HIGH to near-empty, or vice versa
- **Alignment rupture** — One element that breaks the grid (an offset image, a rotated card)

**Rule:** Exactly one rupture per page. Zero = forgettable. Two = chaotic.

## Section Building Blocks

### Hero Patterns

**Centered hero** (landing pages):
```
[nav bar]
         [eyebrow text]
      [large heading, 2-3 lines]
       [subheading, 1-2 lines]
        [CTA button] [secondary]
           [social proof]
[hero image or product screenshot]
```

**Split hero** (SaaS, product pages):
```
[nav bar]
[heading + subtext + CTA]  |  [product image/demo]
```

**Minimal hero** (editorial, apps):
```
[nav bar]
[heading]
[thin description]
```

### Feature Section Patterns

**Grid features** (3-column):
```
        [section heading]
       [section subheading]

[icon]        [icon]        [icon]
[title]       [title]       [title]
[description] [description] [description]
```

**Alternating features** (zigzag):
```
[text block]  |  [image]
              |
[image]       |  [text block]
```

**Bento features** (mixed grid):
```
[large feature card, 2 cols]  [small card]
[small card]  [small card]    [tall card, 2 rows]
```

### Social Proof Patterns

```
Logos:      [logo] [logo] [logo] [logo] [logo]
Quote:      "Testimonial text" — Name, Title, Company
Stats:      [number + label]  [number + label]  [number + label]
Cards:      [avatar + quote + name]  [avatar + quote + name]
```

### CTA Section Patterns

```
Minimal:    [heading] [button]
Card:       [background card with heading + subtext + button]
Split:      [heading + text]  |  [form or button stack]
```

## Responsive Strategy

Every page should define behavior at three breakpoints minimum:

1. **Mobile** (< 768px): Single column. Stack everything. Touch-friendly spacing.
2. **Tablet** (768px - 1024px): 2-column where it makes sense. Sidebar collapses.
3. **Desktop** (> 1024px): Full layout as designed.

**Rules:**
- Never hide content on mobile — reflow it
- Navigation: hamburger on mobile, full on desktop. No exceptions to this until the design system says otherwise.
- Images: `object-cover` with aspect ratio constraints. Never let images stretch.
- Typography: reduce heading sizes by 1-2 steps on mobile (5xl → 3xl, 3xl → 2xl)
- Section spacing: reduce by 30-40% on mobile (py-20 → py-12)

## Assembly Process

1. **Choose the page type** from the list above
2. **Map the density rhythm** — sketch HIGH/MEDIUM/LOW zones
3. **Select section patterns** for each zone
4. **Place the rupture** — decide which section breaks pattern
5. **Set container widths** for each section
6. **Define section spacing** using the design system scale
7. **Build mobile-first** — start at smallest breakpoint, add complexity upward
8. **Wire up navigation** — breadcrumbs, scroll-to-section, back-to-top as appropriate

## Anti-Patterns

- **Uniform density** — Every section the same visual weight. Result: flat, boring.
- **No breathing room** — Sections crammed together. The page feels anxious.
- **Symmetric everything** — All 50/50 splits, all centered text. Result: static.
- **Too many CTAs** — More than 2-3 distinct calls to action per page dilutes all of them.
- **Background color carnival** — More than 2-3 background color shifts per page. Pick one shift point.
- **Orphaned sections** — Sections that don't connect to the one above or below. Use spacing and color to create flow.
- **Full-width everything** — Every section stretching edge-to-edge. Constraining content creates focus.

## Output Checklist

- [ ] Page type identified and density rhythm mapped
- [ ] Container widths vary across sections
- [ ] One rupture moment placed intentionally
- [ ] Mobile, tablet, and desktop breakpoints handled
- [ ] Section spacing uses design system tokens
- [ ] Navigation is appropriate for page type
- [ ] Primary CTA is clear and not competing with secondary actions
- [ ] Page breathes — at least two LOW-density moments

## Related Skills

- **design-system** — Token source for all layout decisions
- **component-craft** — Build the components that fill these layouts
- **polish** — Add transitions, loading states, scroll behavior
- **responsive** — Deep audit of responsive behavior
- **frontend-design** (standalone) — The overarching density and composition philosophy
