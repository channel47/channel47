---
featured: false
draft: false
---

## What it does

Generate production-ready frontend components with distinctive design. No generic gradients or AI tells—just polished, modern interfaces that match your design system or create new visual directions.

## Key Features

- **Design-first approach**: Generates complete visual designs before writing code
- **Component libraries**: Supports React, Vue, Svelte, vanilla HTML/CSS
- **Responsive by default**: Mobile-first layouts with proper breakpoints
- **Accessibility built-in**: ARIA labels, keyboard navigation, semantic HTML
- **Design system integration**: Matches existing color schemes, typography, spacing
- **No AI aesthetics**: Avoids generic patterns (purple gradients, geometric shapes, overly rounded corners)

## Real-world use cases

I use this when building:

- Landing pages that need visual polish (hero sections, feature grids, pricing tables)
- Dashboard components with data visualization (charts, metrics cards, tables)
- Form interfaces with proper validation UX (multi-step forms, file uploads, error states)
- Navigation patterns (sidebars, mobile menus, breadcrumbs)
- Marketing components (testimonials, feature comparisons, CTAs)

The plugin generates complete, copyable code—not just snippets.

## What makes it different

Most AI code generators produce functional but generic designs. This plugin:

- Creates visual mockups before coding (ensures design quality)
- Avoids common AI tells (no gratuitous gradients or geometric backgrounds)
- Generates production-ready code (proper component structure, TypeScript types)
- Matches your design system (reads existing CSS variables and tokens)
- Includes thoughtful details (hover states, loading states, empty states)

## Setup

1. Install: `/plugin install frontend-design@claude-plugins-official`
2. Generate component: `/frontend-design "hero section with video background"`
3. Optional: Configure design system in `.claude/frontend-design.local.md`

## Example workflows

**Create new component:**

```
/frontend-design "pricing table with 3 tiers and feature comparison"
```

Generates design mockup, then complete component code with responsive styles.

**Match existing design system:**

```
/frontend-design "dashboard sidebar navigation" --design-system docs/design-tokens.css
```

Reads your design tokens and generates components matching existing styles.

**Iterate on design:**

```
/frontend-design "previous hero section but darker theme with subtle texture"
```

References previous generation and applies modifications.

## Available skills

- `/frontend-design` - Create distinctive, production-grade frontend interfaces

The skill accepts natural language descriptions and optional flags:

- `--design-system <path>` - Path to design tokens/variables
- `--framework <react|vue|svelte|html>` - Component framework (defaults to React)
- `--preview` - Generate design mockup only (no code)

Output includes complete component code, styles, and usage examples.
