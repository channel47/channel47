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

## Reference Architecture

### Always Consult
- @frameworks/anti-patterns.md — The "AI slop" avoidance checklist

### Load By Task
| Building... | Consult... |
|-------------|------------|
| Buttons | @reference/buttons.md |
| Forms, inputs | @reference/forms.md |
| Cards | @reference/cards.md |
| Navigation | @reference/navigation.md |
| Modals, dialogs | @reference/modals.md |
| Page structure, grids, heroes | @reference/layouts.md |
| CSS custom properties, naming | @reference/css-architecture.md |
| Dark mode, theme switching | @reference/theming.md |
| Breakpoints, fluid typography | @reference/responsive.md |
| Focus states, semantic HTML | @reference/accessibility.md |

### Design System Deep Dives
| For... | Consult... |
|--------|------------|
| Font selection, scale, hierarchy | @frameworks/typography.md |
| Palette generation, dark mode | @frameworks/color.md |
| Timing, easing, staggered reveals | @frameworks/motion.md |

## Mandatory Pre-Flight Check

Before finalizing ANY output, verify each choice is INTENTIONAL:

### Typography
- [ ] Typography choice is INTENTIONAL (if using Inter/Roboto/system fonts, there's a specific reason)
- [ ] Clear size hierarchy (3x+ jumps between levels)
- [ ] Weight contrast uses extremes (300 vs 800, not 400 vs 600)
- [ ] Font choice matches the tone (or intentionally contrasts it)

### Color
- [ ] Color palette is INTENTIONAL (if using purple/violet gradients, it serves the brand)
- [ ] Hero color choice is deliberate, with derived palette
- [ ] CSS custom properties for all colors (no hardcoded values in components)
- [ ] Dark mode is intentional palette, not inverted colors
- [ ] Contrast choices are INTENTIONAL (if using pure black/white, it's a stylistic decision)

### Layout
- [ ] Layout choice is INTENTIONAL (if using three-column equal grid, it fits the content)
- [ ] Symmetry/asymmetry choice is deliberate for the context
- [ ] Hero treatment is INTENTIONAL (if centered text + gradient, it serves the message)
- [ ] Component placement serves UX (conventional placement is fine when it aids usability)

### Components
- [ ] Card styling is INTENTIONAL (multiple effects are fine if cohesive with design language)
- [ ] Button styling is restrained OR maximalist by design choice
- [ ] Form labels are real labels, not placeholder text
- [ ] States (hover, active, focus) are distinctive and purposeful

### Motion
- [ ] Motion density is INTENTIONAL (micro-interactions everywhere is fine if that's the brand)
- [ ] CTA animation serves attention hierarchy (pulsing is fine if it's the ONE focus)
- [ ] Staggered reveals vs micro-interactions — choice fits the content
- [ ] Reduced motion preference respected

## When to Override These Guidelines

These guidelines assume greenfield design. Override when:

- **Matching existing design system** — Follow their patterns, even if they use Inter or purple gradients
- **Brand guidelines exist** — Corporate style guides take precedence
- **User explicitly requests** — "Make it look like Stripe" or "Use our brand colors" trumps defaults
- **Technical constraints require it** — System fonts for performance, specific layouts for content

When overriding:
1. **State the override explicitly** — "Using Inter to match existing design system"
2. **Document in README.md** — Explain why default guidance was overridden
3. **Maintain quality in other areas** — One override doesn't mean abandon all principles

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
