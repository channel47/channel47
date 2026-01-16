# Frontend Design

Production-grade frontend interfaces with built-in design sensibility.

## What This Does

Generates distinctive, high-quality frontend code that avoids the generic "AI aesthetic." Every output is:

- **Production-ready** — TypeScript, proper exports, cleanup functions
- **Performance-optimized** — 60fps animations, retina support, visibility API
- **Aesthetically intentional** — Opinionated typography, color, motion

## Skills

### creating-canvas-animations

Generate HTML5 Canvas 2D animations for backgrounds, hero sections, and visual effects.

**Trigger phrases:**
- "Create an animated background"
- "Build a particle system"
- "Make a matrix rain effect"
- "Design a grid animation"

**Output:**
```
{component-name}/
├── animation.ts    # ES module with initAnimation()
├── types.ts        # TypeScript interfaces
└── README.md       # Usage instructions
```

**Flags:**
- `--standalone` — Output HTML/JS/CSS demo instead of ES module
- `--type <type>` — Hint animation type (lines, grid, particles, matrix, wireframe, wave)
- `--color <hex>` — Primary color

## Design System

Shared frameworks apply to all skills:

- **Typography** — Font selection, pairing, scale (never Inter/Roboto)
- **Color** — Palette generation, CSS variables, dark mode
- **Motion** — Timing, easing, staggered reveals
- **Anti-patterns** — The "AI slop" checklist

## Philosophy

1. **Technique over templates** — Learn primitives, compose anything
2. **Intentionality over intensity** — Bold maximalism and refined minimalism both work
3. **Production over prototype** — Code you'd actually ship
4. **Distinctive over safe** — Generic choices signal "I didn't think"

## Examples

```
"Create an animated background with diagonal orange lines, similar to Interface Craft"

"Build a particle system with connection lines for a tech landing page"

"Generate a matrix rain effect with green characters on black"

"Make a wireframe UI animation that reveals panels sequentially"
```

## Installation

```bash
claude plugin install channel47/frontend-design
```

## Version

1.0.0
