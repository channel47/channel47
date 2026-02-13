# Frontend Design Plugin - Design Document

**Date:** 2026-01-14
**Status:** Ready for implementation
**Author:** jackson + Claude

---

## Overview

A new plugin for the channel47 marketplace that generates production-grade frontend interfaces with built-in design sensibility. Differentiates from the official Claude frontend-design plugin by focusing on code quality and opinionated aesthetics, not just working code.

### Positioning

| Official Claude Plugin | Our `frontend-design` |
|------------------------|----------------------|
| Aesthetic guidance only | Aesthetic + production code quality |
| General "motion" guidance | Deep canvas animation expertise |
| Font recommendations | Font recommendations + loading/performance |
| Avoids defaults | Avoids defaults + explains *why* |
| Single skill | Expandable multi-skill architecture |

### First Skill

`creating-canvas-animations` - HTML5 Canvas 2D animations for backgrounds, hero sections, card visuals, and abstract motion graphics.

---

## Plugin Architecture

```
plugins/frontend-design/
├── .claude-plugin/
│   ├── plugin.json              # Plugin metadata, version, triggers
│   └── site.json                # Marketplace display info
├── skills/
│   └── creating-canvas-animations/
│       ├── SKILL.md             # Core skill instructions + principles
│       └── reference/
│           ├── primitives.md    # Canvas building blocks
│           ├── composition.md   # How to combine primitives
│           ├── easing.md        # Easing function library
│           ├── performance.md   # Production performance patterns
│           └── examples.md      # Worked examples (Interface Craft style)
├── frameworks/                   # Shared across all skills
│   ├── typography.md            # Font selection, pairing, loading
│   ├── color.md                 # Palette generation, CSS variables
│   ├── motion.md                # Animation principles
│   └── anti-patterns.md         # The "AI slop" avoidance list
├── README.md
├── CHANGELOG.md
└── package.json
```

### Key Decisions

- **`frameworks/` at plugin root** - Shared design system across all future skills
- **`reference/` inside skill** - Specific to canvas animations
- **No MCP server** - Pure code generation, no external APIs
- **Technique-first approach** - Teach primitives + composition, not fixed patterns

---

## Skill: creating-canvas-animations

### SKILL.md Frontmatter

```yaml
---
name: creating-canvas-animations
description: Creates elegant HTML5 Canvas 2D animations. Use when generating animated backgrounds, hero sections, card visuals, or abstract motion graphics.
---
```

### Trigger Conditions

Activates when user asks for:
- Animated backgrounds, hero animations
- Canvas-based visuals, particle systems
- Geometric patterns, grid animations, line patterns
- Matrix/code rain effects, wireframe mockups

### Output Contract

Every generation produces:

```
{component-name}/
├── animation.ts       # ES module: initAnimation(canvas, options)
├── types.ts           # AnimationOptions, ColorScheme interfaces
└── README.md          # Usage example, configuration options
```

### Core Principles

1. **60fps or graceful degradation** - Use `requestAnimationFrame`, pause on hidden tabs
2. **Retina-aware** - Always handle `devicePixelRatio` scaling
3. **Responsive** - `ResizeObserver` for container-based sizing, not window
4. **Configurable** - Colors, speed, density exposed as typed options
5. **Self-contained** - Zero dependencies, vanilla TypeScript only
6. **Seamless loops** - Animations reset without visible jumps

### Output Format

- **Default:** TypeScript ES module
- **On request:** Standalone HTML/JS/CSS demo files

---

## Reference: Primitives (`reference/primitives.md`)

The building blocks Claude uses to construct any canvas animation.

### Lines

```typescript
// Drawing
ctx.beginPath();
ctx.moveTo(x1, y1);
ctx.lineTo(x2, y2);
ctx.strokeStyle = color;
ctx.lineWidth = width;
ctx.stroke();
```

**Animation Techniques:**
- **Traveling**: Animate start/end points over time
- **Drawing on**: Use `setLineDash` + `lineDashOffset` for reveal effect
- **Fading**: Animate `globalAlpha` or strokeStyle alpha
- **Pulsing**: Oscillate lineWidth with sine wave

### Shapes

```typescript
// Rectangles
ctx.fillRect(x, y, w, h);        // filled
ctx.strokeRect(x, y, w, h);      // outline only

// Circles
ctx.beginPath();
ctx.arc(x, y, radius, 0, Math.PI * 2);
ctx.fill(); // or ctx.stroke();

// Rounded Rectangles
ctx.roundRect(x, y, w, h, radius); // modern browsers
```

### Text/Characters

```typescript
ctx.font = '16px JetBrains Mono';
ctx.fillStyle = color;
ctx.fillText(char, x, y);
```

**Matrix Rain Technique:**
- Column array, each tracks current y position
- Draw character, increment y
- Reset to top with random delay when off-screen
- Fade: draw semi-transparent rect over canvas each frame

### Particles

```typescript
interface Particle {
  x: number; y: number;
  vx: number; vy: number;
  radius: number;
  color: string;
  life: number; // 0-1, for fade out
}

// Update loop
particles.forEach(p => {
  p.x += p.vx;
  p.y += p.vy;
  p.life -= decay;
});

// Connection lines (draw between particles within threshold)
particles.forEach((a, i) => {
  particles.slice(i + 1).forEach(b => {
    const dist = distance(a, b);
    if (dist < threshold) {
      ctx.globalAlpha = 1 - (dist / threshold);
      drawLine(a.x, a.y, b.x, b.y);
    }
  });
});
```

### Grids

```typescript
// Generation
for (let x = 0; x < cols; x++) {
  for (let y = 0; y < rows; y++) {
    const cell = { x: x * cellWidth, y: y * cellHeight, ... };
    grid.push(cell);
  }
}
```

**Animation Patterns:**
- **Wave**: offset animation delay by distance from origin
- **Cascade**: animate row by row or column by column
- **Random**: each cell has independent random delay
- **Ripple**: distance from click point determines delay

### Noise (Organic Variation)

```typescript
// Simple noise using sine combination (no library needed)
const noise = (x: number, y: number, t: number): number => {
  return Math.sin(x * 0.1 + t) * Math.cos(y * 0.1 + t) * 0.5 + 0.5;
};
```

**Usage:**
- Vary particle velocity
- Distort grid positions
- Animate color/opacity organically
- Create flowing, non-mechanical motion

---

## Reference: Composition (`reference/composition.md`)

How to combine primitives into cohesive effects.

### Layering

- Background layer: slowest, most subtle
- Midground layer: primary visual interest
- Foreground layer: fastest, draws attention

### Color Relationships

- **Monochrome**: Single hue, vary lightness/opacity
- **Complementary**: Two opposing hues, high contrast
- **Analogous**: Adjacent hues, harmonious

### Density and Spacing

- **Sparse**: 10-20 elements, contemplative feel
- **Medium**: 50-100 elements, balanced
- **Dense**: 200+ elements, energetic/chaotic

### Motion Choreography

- **Stagger**: Elements animate in sequence with delay
- **Wave**: Delay based on position (distance from origin)
- **Cascade**: Row-by-row or column-by-column
- **Simultaneous**: All at once (use sparingly)

### Focal Points

- Use motion to draw eye to specific area
- Slower/static elements recede
- Faster/brighter elements advance

---

## Reference: Easing (`reference/easing.md`)

### Core Set (Always Include)

```typescript
// t = progress (0-1), returns eased value (0-1)

const linear = (t: number): number => t;

const easeOutQuad = (t: number): number => t * (2 - t);

const easeInQuad = (t: number): number => t * t;

const easeInOutQuad = (t: number): number =>
  t < 0.5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2;
```

### Expressive Set (When Personality Needed)

```typescript
const easeOutBack = (t: number): number => {
  const c = 1.70158;
  return 1 + (c + 1) * Math.pow(t - 1, 3) + c * Math.pow(t - 1, 2);
};

const easeOutElastic = (t: number): number => {
  if (t === 0 || t === 1) return t;
  return Math.pow(2, -10 * t) * Math.sin((t * 10 - 0.75) * ((2 * Math.PI) / 3)) + 1;
};

const easeOutExpo = (t: number): number =>
  t === 1 ? 1 : 1 - Math.pow(2, -10 * t);
```

### Usage Principle

Match easing to intent:
- **Subtle/professional** → Quad family
- **Playful/delightful** → Back/Elastic family
- **Dramatic/impactful** → Expo family

---

## Reference: Performance (`reference/performance.md`)

### The Basics

- Always use `requestAnimationFrame`, never `setInterval`
- Cache canvas context, don't re-query every frame
- Batch draws when possible (single path for multiple shapes)

### Retina/DPI Handling

```typescript
const dpr = window.devicePixelRatio || 1;
canvas.width = width * dpr;
canvas.height = height * dpr;
canvas.style.width = `${width}px`;
canvas.style.height = `${height}px`;
ctx.scale(dpr, dpr);
```

### Visibility Optimization

```typescript
// Pause when tab not visible
document.addEventListener('visibilitychange', () => {
  if (document.hidden) pause();
  else resume();
});
```

### Resize Handling

```typescript
// Use ResizeObserver, not window resize
const ro = new ResizeObserver(entries => {
  const { width, height } = entries[0].contentRect;
  resize(width, height);
});
ro.observe(container);
```

### Memory Management

- Object pool for particles (avoid GC spikes)
- Clear references on destroy
- Provide cleanup function: `animation.destroy()`

### Target Metrics

- 60fps sustained (16.67ms per frame budget)
- <100ms to first visual
- Graceful degradation: reduce particle count if dropping frames

---

## Reference: Examples (`reference/examples.md`)

Worked examples inspired by [Interface Craft](https://interfacecraft.dev) cards.

### Diagonal Line Pattern

**Target:** "Working Knowledge" card style

```typescript
interface DiagonalLinesOptions {
  color: string;        // e.g., '#f97316' (orange)
  lineWidth: number;    // 1-2px
  spacing: number;      // 20-40px
  angle: number;        // degrees, e.g., 45
  opacity: number;      // 0.3-0.6
  drift?: boolean;      // subtle movement
}
```

**Technique:** Draw parallel lines at angle, optionally animate offset for drift effect.

### Grid/Mosaic Tiles

**Target:** "Practical Demonstration" card style

```typescript
interface MosaicOptions {
  baseColor: string;
  cellSize: number;
  variation: number;    // how much cells vary in shade
  animationStyle: 'fade' | 'scale' | 'none';
}
```

**Technique:** Grid of rectangles with varied heights, subtle color variation within same hue family.

### Horizontal Scan Lines

**Target:** "Collaborating with AI" card style

```typescript
interface ScanLinesOptions {
  color: string;
  lineSpacing: number;
  scanSpeed: number;    // ms per full scan
  glowIntensity: number;
}
```

**Technique:** Evenly spaced horizontal lines with optional scanning highlight animation.

### Matrix/Code Rain

**Target:** "Building Interface Kit" card style

```typescript
interface MatrixRainOptions {
  color: string;        // e.g., '#22c55e' (green)
  charset: string;      // characters to use
  fontSize: number;
  columnDensity: number;
  fallSpeed: number;
}
```

**Technique:** Vertical character columns, characters fade as they fall, monospace font.

### Wireframe UI Mockup

**Target:** "Interface Kit" card style

```typescript
interface WireframeOptions {
  strokeColor: string;
  fillColor?: string;
  panels: PanelConfig[];  // or 'auto' for generated layout
  animationStyle: 'draw' | 'fade' | 'sequence';
}
```

**Technique:** Rectangles representing UI panels, minimal aesthetic, optional sequential reveal.

---

## Shared Frameworks

### Typography (`frameworks/typography.md`)

**Never Use:**
- Inter, Roboto, Open Sans, Lato, default system fonts

**Recommended by Context:**

| Context | Display | Body | Mono |
|---------|---------|------|------|
| Technical/Dev | Space Grotesk | IBM Plex Sans | JetBrains Mono |
| Editorial | Playfair Display | Source Serif | — |
| Startup/Modern | Clash Display | Satoshi | Fira Code |
| Luxury | Cormorant | Lora | — |

**Loading Strategy:**
- Use `font-display: swap` for body, `optional` for display
- Subset fonts when possible
- Preload critical fonts in `<head>`

**Scale:**
- Use multiplier of 1.25-1.5 (not arbitrary sizes)
- Minimum 3x jump for visual hierarchy

### Color (`frameworks/color.md`)

**Principles:**
- Dominant color + sharp accent beats evenly distributed
- Commit to a palette, don't hedge
- Dark mode is not "invert" — it's a separate palette

**CSS Variable Structure:**
```css
:root {
  --color-bg: ...;
  --color-surface: ...;
  --color-text-primary: ...;
  --color-text-secondary: ...;
  --color-accent: ...;
  --color-accent-subtle: ...;
}
```

**Generating Palettes:**
- Start with one hero color
- Derive shades using HSL (adjust L, not H)
- Test contrast ratios (4.5:1 minimum for text)

### Motion (`frameworks/motion.md`)

**Hierarchy of Impact:**
1. Page transitions (highest impact)
2. Component entrances (staggered reveals)
3. State changes (hover, focus, active)
4. Micro-interactions (lowest impact, use sparingly)

**Timing:**
- Fast feedback: 100-200ms (buttons, toggles)
- Transitions: 200-400ms (modals, panels)
- Atmospheric: 1000ms+ (background animations)

**Easing:**
- Never use linear for UI (feels robotic)
- `ease-out` for entrances (decelerating)
- `ease-in` for exits (accelerating away)
- `ease-in-out` for position changes

### Anti-Patterns (`frameworks/anti-patterns.md`)

**The "AI Slop" Checklist:**
- [ ] Purple gradient on white background
- [ ] Inter or Roboto as primary font
- [ ] Evenly-spaced 3-column card grid
- [ ] Generic stock imagery
- [ ] Drop shadows on everything
- [ ] Rounded corners on everything (pick a radius, commit)
- [ ] Blue primary color with no personality

**Why These Fail:**
Generic choices signal "I didn't think about this." Distinctive choices signal intention and care.

---

## Plugin Metadata

### `.claude-plugin/plugin.json`

```json
{
  "name": "frontend-design",
  "version": "1.0.0",
  "description": "Production-grade frontend interfaces with built-in design sensibility",
  "author": "channel47",
  "skills": ["creating-canvas-animations"],
  "triggers": {
    "creating-canvas-animations": [
      "canvas animation",
      "animated background",
      "particle system",
      "matrix rain",
      "geometric pattern",
      "hero animation"
    ]
  }
}
```

### `package.json`

```json
{
  "name": "@channel47/frontend-design",
  "version": "1.0.0",
  "description": "Production-grade frontend interfaces with built-in design sensibility",
  "keywords": ["claude-code", "plugin", "frontend", "design", "canvas"],
  "author": "channel47",
  "license": "MIT"
}
```

### Marketplace Entry (`.claude-plugin/marketplace.json`)

```json
{
  "name": "frontend-design",
  "source": "./plugins/frontend-design",
  "description": "Production-grade frontend interfaces with built-in design sensibility. Canvas animations, component design, and more.",
  "version": "1.0.0",
  "category": "frontend",
  "tags": ["design", "canvas", "animation", "ui", "components"]
}
```

---

## Future Skills (Roadmap)

The plugin architecture supports adding more skills:

- `designing-components/` - React/Vue/Svelte component generation
- `building-layouts/` - Page layouts, grid systems, responsive patterns
- `crafting-forms/` - Form design, validation UX, accessibility
- `creating-svg-animations/` - SVG-based animations and illustrations

Each new skill would:
1. Add a directory under `skills/`
2. Include its own SKILL.md and reference files
3. Share the `frameworks/` design system
4. Update plugin.json triggers

---

## Implementation Notes

### Aesthetic Direction

Default to **Minimal/Swiss** aesthetic:
- Clean geometry, generous whitespace
- Restrained color palettes
- Subtle motion
- Think: Linear, Stripe, Vercel

### Key Differentiators

1. **Production-grade output** - TypeScript, proper exports, cleanup functions
2. **Performance by default** - DPI handling, visibility API, ResizeObserver
3. **Technique-first teaching** - Claude learns to design, not copy patterns
4. **Shared design system** - Consistent typography, color, motion across skills

### Reference Inspiration

- [Interface Craft](https://interfacecraft.dev) - Card animation styles
- [Anthropic Frontend Aesthetics Cookbook](https://github.com/anthropics/claude-cookbooks/blob/main/coding/prompting_for_frontend_aesthetics.ipynb) - Anti-slop patterns
- [Official Claude frontend-design plugin](https://github.com/anthropics/claude-code/tree/main/plugins/frontend-design) - Trigger patterns

---

## Next Steps

1. Create plugin directory structure
2. Write SKILL.md for `creating-canvas-animations`
3. Write reference files (primitives, composition, easing, performance, examples)
4. Write shared framework files
5. Write plugin metadata files
6. Add to marketplace.json
7. Test with sample prompts
