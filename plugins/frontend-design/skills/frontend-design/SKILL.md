---
name: frontend-design
description: |
  Create distinctive, production-grade frontend interfaces.
  Use when generating components, layouts, landing pages, dashboards, or any user-facing UI.
args:
  - name: standalone
    description: Output standalone HTML demo instead of framework components
    required: false
    flag: true
  - name: framework
    description: "Target framework: react, vue, svelte, html (default: react)"
    required: false
    flag: true
---

# Frontend Design

Create interfaces that signal craft, not defaults. Every design choice should be intentional.

## Design Thinking

Before writing any code, answer these questions:

1. **Purpose** — What is this interface trying to accomplish? What actions should users take?
2. **Tone** — Professional? Playful? Technical? Luxurious? This drives every aesthetic choice.
3. **Constraints** — What's the brand? Existing design system? Technical limitations?
4. **Differentiation** — What makes this NOT look like every other AI-generated interface?

### The Cardinal Rule

**NEVER converge on common choices.**

If you've seen it in 10 other AI-generated sites, don't use it. Distinctive design requires going against the distribution, not with it.

## Output Contract

Every generation produces:

```
{component-name}/
├── {Component}.tsx      # TypeScript React component (or .vue, .svelte)
├── {Component}.css      # Styles with CSS custom properties
└── README.md            # Usage example and design rationale
```

If `--standalone` flag is passed:

```
{component-name}/
├── index.html           # Self-contained demo
├── styles.css           # Complete styles
└── script.js            # Vanilla JS (no TypeScript)
```

## Aesthetic Direction

You are NOT limited to these — adapt to context. These are defaults when tone is unspecified:

| Context | Direction | Example Influences |
|---------|-----------|-------------------|
| **Technical/Dev** | Clean, precise, monospace accents | Linear, Vercel, Stripe |
| **Startup/Modern** | Bold typography, asymmetric layouts | Notion, Figma, Arc |
| **Editorial** | Generous whitespace, serif headlines | Medium, Substack |
| **Dashboard/Data** | Dense information, subtle hierarchy | Bloomberg Terminal, Datadog |

## Design System Reference

Apply shared design principles — load these before generating:

- @frameworks/typography.md — Font selection, scale, hierarchy
- @frameworks/color.md — Palette generation, CSS variables, dark mode
- @frameworks/motion.md — Timing, easing, staggered reveals
- @frameworks/anti-patterns.md — The "AI slop" avoidance checklist

## Technical Reference

For implementation patterns, load:

- @reference/components.md — Button, form, card, navigation patterns
- @reference/layouts.md — Grid systems, asymmetric compositions, spatial rhythm
- @reference/implementation.md — CSS architecture, theming, responsive patterns

## Mandatory Pre-Flight Check

Before finalizing ANY output, verify against the anti-pattern checklist:

### Typography
- [ ] NOT using Inter, Roboto, Open Sans, or system fonts as primary
- [ ] Clear size hierarchy (3x+ jumps between levels)
- [ ] Weight contrast uses extremes (300 vs 800, not 400 vs 600)
- [ ] Font choice matches the tone (technical → Space Grotesk, editorial → Playfair)

### Color
- [ ] NOT purple/violet gradient on white background
- [ ] Single dominant hero color, derived palette
- [ ] CSS custom properties for all colors (no hardcoded values in components)
- [ ] Dark mode is intentional palette, not inverted colors
- [ ] Not pure black (#000) on pure white (#fff)

### Layout
- [ ] NOT three-column card grid with equal spacing (unless explicitly required)
- [ ] Asymmetry or visual tension present
- [ ] NOT hero with centered text and gradient background
- [ ] Unpredictable element placement (not logo top-left, CTA top-right pattern)

### Components
- [ ] NOT cards with drop shadow AND rounded corners AND borders simultaneously
- [ ] Button variants are restrained (not gradient + shadow + border + icon)
- [ ] Form labels are real labels, not placeholder text
- [ ] States (hover, active, focus) are distinctive, not just color shifts

### Motion
- [ ] NOT micro-interactions on everything
- [ ] NOT bouncing/pulsing CTAs
- [ ] Staggered reveals prioritized over scattered micro-interactions
- [ ] Reduced motion preference respected

## When User Provides Vague Requirements

If the user says "make a button" or "design a landing page" without specifics:

1. **Don't default to generic** — Pick a BOLD aesthetic direction
2. **State your choice** — "I'm going with a brutalist approach for this component"
3. **Commit fully** — Half-measures are worse than generic
4. **Explain the rationale** — Why does this direction fit the implied context?

## What Success Looks Like

A successful frontend design output:

1. **Passes the anti-pattern checklist** — Zero violations
2. **Has a coherent aesthetic** — All elements share a design language
3. **Makes intentional choices** — Every decision can be explained
4. **Includes proper CSS architecture** — Custom properties, responsive, dark mode ready
5. **Demonstrates craft** — Details that show human-level thought went into it
