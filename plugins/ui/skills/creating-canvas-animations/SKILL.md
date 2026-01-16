---
name: creating-canvas-animations
description: |
  Creates elegant HTML5 Canvas 2D animations for web interfaces.
  Use when generating animated backgrounds, hero sections, card visuals, particle systems, or abstract motion graphics.
args:
  - name: type
    description: "Animation type hint: lines, grid, particles, matrix, wireframe, wave"
    required: false
    flag: true
  - name: color
    description: Primary color for the animation (hex or named)
    required: false
    flag: true
  - name: standalone
    description: Output standalone HTML demo instead of ES module
    required: false
    flag: true
---

# Creating Canvas Animations

Generate production-grade HTML5 Canvas 2D animations. Output is TypeScript ES modules by default.

## Output Contract

Every generation produces:

```
{component-name}/
├── animation.ts       # ES module: initAnimation(canvas, options)
├── types.ts           # AnimationOptions interface
└── README.md          # Usage example
```

If `--standalone` flag is passed, output instead:

```
{component-name}/
├── index.html         # Self-contained demo
├── animation.js       # Vanilla JS (no TypeScript)
└── styles.css         # Minimal container styles
```

## Core Principles

1. **60fps or graceful degradation** — Use `requestAnimationFrame`, pause on hidden tabs
2. **Retina-aware** — Always handle `devicePixelRatio` scaling
3. **Responsive** — `ResizeObserver` for container-based sizing
4. **Configurable** — Colors, speed, density as typed options
5. **Self-contained** — Zero dependencies, vanilla TS only
6. **Cleanup provided** — Always export a `destroy()` function

## Core Requirements

Every animation MUST handle:

1. **DPI scaling** — Account for `devicePixelRatio`
2. **Visibility** — Pause when tab is hidden (Visibility API)
3. **Responsiveness** — Use `ResizeObserver`, not window resize
4. **Cleanup** — Export a `destroy()` function

See @reference/performance.md for the standard initialization pattern.

## Reference Architecture

### Always Consult
- @frameworks/anti-patterns.md — Verify no "AI slop" violations

### Load By Task
| Building... | Consult... |
|-------------|------------|
| Basic shapes, lines, particles | @reference/primitives.md |
| Layering multiple effects | @reference/composition.md |
| Custom motion curves | @reference/easing.md |
| Production optimization | @reference/performance.md |

### Deep Dives
| For... | Consult... |
|--------|------------|
| Font selection, scale | @frameworks/typography.md |
| Palette generation, CSS vars | @frameworks/color.md |
| Timing, easing principles | @frameworks/motion.md |

### For Inspiration
| Pattern | Reference |
|---------|-----------|
| Diagonal line patterns | @reference/example-lines.md |
| Grid/mosaic tiles | @reference/example-grid.md |
| Matrix/code rain | @reference/example-matrix.md |
| Wireframe UI mockups | @reference/example-wireframe.md |
| Combining techniques | @reference/example-combining.md |

## Aesthetic Direction

Default to **Minimal/Swiss** aesthetic:
- Clean geometry, generous whitespace
- Restrained color palettes (monochrome or single accent)
- Subtle, meditative motion (not frantic)
- Think: Linear, Stripe, Vercel

When user specifies a different direction, adapt while maintaining production quality.

## When to Override These Guidelines

These guidelines assume creative freedom. Override when:

- **Matching existing brand** — If the site uses specific colors/motion patterns, match them
- **Performance constraints** — Simpler animations for low-power devices or older browsers
- **Accessibility requirements** — Some users need reduced motion; provide static fallbacks
- **User explicitly requests** — "Make it flashy" or "Keep it subtle" trumps defaults

When overriding, document the reason in the output README.md.

## Animation Types

You are NOT limited to these — use primitives to create anything. These are common starting points:

| Type | Description | Key Primitives |
|------|-------------|----------------|
| **Lines** | Parallel, radial, or converging line patterns | Lines + easing |
| **Grid** | Mosaic, checkerboard, animated tiles | Grid + color variation |
| **Particles** | Floating dots, connections, constellations | Particles + optional connections |
| **Matrix** | Character rain, code streams | Text + columns + fade |
| **Wireframe** | UI mockup rectangles, interface skeletons | Shapes + sequential reveal |
| **Wave** | Sinusoidal, flowing, organic motion | Lines/shapes + noise |
