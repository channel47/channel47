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

## Required Boilerplate

Every animation MUST include:

```typescript
// DPI scaling
const dpr = window.devicePixelRatio || 1;
canvas.width = width * dpr;
canvas.height = height * dpr;
canvas.style.width = `${width}px`;
canvas.style.height = `${height}px`;
ctx.scale(dpr, dpr);

// Visibility API
document.addEventListener('visibilitychange', () => {
  if (document.hidden) pause();
  else resume();
});

// ResizeObserver
const ro = new ResizeObserver(entries => {
  const { width, height } = entries[0].contentRect;
  resize(width, height);
});
ro.observe(container);

// Cleanup
export function destroy() {
  ro.disconnect();
  cancelAnimationFrame(animationId);
}
```

## Technique Reference

Before generating, load relevant technique docs:

- @reference/primitives.md — Lines, shapes, text, particles, grids, noise
- @reference/composition.md — Layering, color relationships, density, choreography
- @reference/easing.md — Easing function library
- @reference/performance.md — Optimization patterns
- @reference/examples.md — Worked examples (Interface Craft style)

## Design System Reference

Apply shared design principles:

- @frameworks/typography.md — Font selection (avoid Inter, Roboto)
- @frameworks/color.md — Palette generation, CSS variables
- @frameworks/motion.md — Timing, easing principles
- @frameworks/anti-patterns.md — What to avoid ("AI slop" list)

## Aesthetic Direction

Default to **Minimal/Swiss** aesthetic:
- Clean geometry, generous whitespace
- Restrained color palettes (monochrome or single accent)
- Subtle, meditative motion (not frantic)
- Think: Linear, Stripe, Vercel

When user specifies a different direction, adapt while maintaining production quality.

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
