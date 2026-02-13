# Frontend Design Plugin - Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Create a production-grade frontend-design plugin for the channel47 marketplace with a canvas animations skill as the first capability.

**Architecture:** Plugin with shared `frameworks/` directory at root for design system consistency across all future skills. First skill `creating-canvas-animations` includes technique-first reference docs teaching primitives + composition rather than fixed patterns.

**Tech Stack:** Markdown (SKILL.md, frameworks), JSON (plugin.json, site.json, marketplace.json), no MCP server required.

---

## Task 1: Create Plugin Directory Structure

**Files:**
- Create: `plugins/frontend-design/.claude-plugin/` (directory)
- Create: `plugins/frontend-design/skills/creating-canvas-animations/reference/` (directory)
- Create: `plugins/frontend-design/frameworks/` (directory)

**Step 1: Create all directories**

```bash
mkdir -p plugins/frontend-design/.claude-plugin
mkdir -p plugins/frontend-design/skills/creating-canvas-animations/reference
mkdir -p plugins/frontend-design/frameworks
```

**Step 2: Verify directory structure**

Run: `find plugins/frontend-design -type d | sort`

Expected output:
```
plugins/frontend-design
plugins/frontend-design/.claude-plugin
plugins/frontend-design/frameworks
plugins/frontend-design/skills
plugins/frontend-design/skills/creating-canvas-animations
plugins/frontend-design/skills/creating-canvas-animations/reference
```

**Step 3: Commit**

```bash
git add plugins/frontend-design
git commit -m "chore(frontend-design): create plugin directory structure"
```

---

## Task 2: Create Plugin Metadata (plugin.json)

**Files:**
- Create: `plugins/frontend-design/.claude-plugin/plugin.json`

**Step 1: Write plugin.json**

```json
{
  "name": "frontend-design",
  "version": "1.0.0",
  "description": "Production-grade frontend interfaces with built-in design sensibility. Canvas animations, component patterns, and distinctive aesthetics.",
  "author": {
    "name": "Jackson",
    "url": "https://channel47.dev"
  },
  "homepage": "https://channel47.dev/plugins/frontend-design",
  "repository": "https://github.com/channel47/channel47",
  "license": "MIT",
  "keywords": [
    "frontend",
    "design",
    "canvas",
    "animation",
    "ui",
    "components",
    "aesthetics",
    "typography",
    "motion"
  ]
}
```

**Step 2: Verify JSON is valid**

Run: `cat plugins/frontend-design/.claude-plugin/plugin.json | python3 -m json.tool > /dev/null && echo "Valid JSON"`

Expected: `Valid JSON`

**Step 3: Commit**

```bash
git add plugins/frontend-design/.claude-plugin/plugin.json
git commit -m "feat(frontend-design): add plugin.json metadata"
```

---

## Task 3: Create Site Display Metadata (site.json)

**Files:**
- Create: `plugins/frontend-design/.claude-plugin/site.json`

**Step 1: Write site.json**

```json
{
  "displayName": "Frontend Design",
  "tagline": "Production-grade interfaces with built-in taste. Canvas animations, typography, color systems.",
  "label": "Claude Code Plugin",
  "features": [
    "Canvas animations skill — Particles, grids, lines, matrix rain, wireframes",
    "Technique-first approach — Learn primitives + composition, not fixed patterns",
    "Shared design system — Typography, color, motion frameworks",
    "Anti-AI-slop guardrails — Explicit guidance on what to avoid",
    "TypeScript output — Production-ready ES modules with cleanup functions",
    "Performance by default — 60fps, retina-aware, ResizeObserver"
  ]
}
```

**Step 2: Verify JSON is valid**

Run: `cat plugins/frontend-design/.claude-plugin/site.json | python3 -m json.tool > /dev/null && echo "Valid JSON"`

Expected: `Valid JSON`

**Step 3: Commit**

```bash
git add plugins/frontend-design/.claude-plugin/site.json
git commit -m "feat(frontend-design): add site.json for marketplace display"
```

---

## Task 4: Create Main SKILL.md for Canvas Animations

**Files:**
- Create: `plugins/frontend-design/skills/creating-canvas-animations/SKILL.md`

**Step 1: Write SKILL.md**

````markdown
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
````

**Step 2: Verify file was created**

Run: `head -20 plugins/frontend-design/skills/creating-canvas-animations/SKILL.md`

Expected: Should show YAML frontmatter starting with `---`

**Step 3: Commit**

```bash
git add plugins/frontend-design/skills/creating-canvas-animations/SKILL.md
git commit -m "feat(frontend-design): add creating-canvas-animations skill"
```

---

## Task 5: Create Reference - Primitives

**Files:**
- Create: `plugins/frontend-design/skills/creating-canvas-animations/reference/primitives.md`

**Step 1: Write primitives.md**

````markdown
# Canvas Primitives

The building blocks for constructing any canvas animation.

---

## Lines

### Drawing a Line

```typescript
ctx.beginPath();
ctx.moveTo(x1, y1);
ctx.lineTo(x2, y2);
ctx.strokeStyle = color;
ctx.lineWidth = width;
ctx.stroke();
```

### Animation Techniques

**Traveling** — Animate start/end points over time:
```typescript
const progress = (Date.now() % duration) / duration;
const currentX = startX + (endX - startX) * progress;
ctx.lineTo(currentX, y);
```

**Drawing on** — Line dash offset for reveal effect:
```typescript
ctx.setLineDash([lineLength]);
ctx.lineDashOffset = lineLength * (1 - progress);
```

**Fading** — Animate alpha:
```typescript
ctx.globalAlpha = 1 - progress;
// or use rgba in strokeStyle
ctx.strokeStyle = `rgba(255, 255, 255, ${1 - progress})`;
```

**Pulsing** — Oscillate lineWidth:
```typescript
const pulse = Math.sin(Date.now() * 0.005) * 0.5 + 1;
ctx.lineWidth = baseWidth * pulse;
```

---

## Shapes

### Rectangles

```typescript
// Filled
ctx.fillStyle = color;
ctx.fillRect(x, y, width, height);

// Outline only
ctx.strokeStyle = color;
ctx.strokeRect(x, y, width, height);
```

### Circles

```typescript
ctx.beginPath();
ctx.arc(centerX, centerY, radius, 0, Math.PI * 2);
ctx.fillStyle = color;
ctx.fill();
// or ctx.stroke() for outline
```

### Rounded Rectangles

```typescript
// Modern browsers
ctx.beginPath();
ctx.roundRect(x, y, width, height, radius);
ctx.fill();

// Fallback for older browsers
function roundRect(ctx, x, y, w, h, r) {
  ctx.beginPath();
  ctx.moveTo(x + r, y);
  ctx.arcTo(x + w, y, x + w, y + h, r);
  ctx.arcTo(x + w, y + h, x, y + h, r);
  ctx.arcTo(x, y + h, x, y, r);
  ctx.arcTo(x, y, x + w, y, r);
  ctx.closePath();
}
```

---

## Text/Characters

### Basic Text

```typescript
ctx.font = '16px JetBrains Mono';
ctx.fillStyle = color;
ctx.textAlign = 'center';
ctx.textBaseline = 'middle';
ctx.fillText(text, x, y);
```

### Matrix Rain Technique

```typescript
interface Column {
  x: number;
  y: number;
  speed: number;
  chars: string[];
}

// Initialize columns
const columns: Column[] = [];
for (let x = 0; x < width; x += fontSize) {
  columns.push({
    x,
    y: Math.random() * -height,
    speed: 2 + Math.random() * 3,
    chars: generateRandomChars(20)
  });
}

// Animation frame
function draw() {
  // Fade effect: semi-transparent overlay
  ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
  ctx.fillRect(0, 0, width, height);

  ctx.fillStyle = color;
  ctx.font = `${fontSize}px monospace`;

  columns.forEach(col => {
    const char = col.chars[Math.floor(col.y / fontSize) % col.chars.length];
    ctx.fillText(char, col.x, col.y);

    col.y += col.speed;
    if (col.y > height) {
      col.y = Math.random() * -100;
    }
  });
}
```

---

## Particles

### Data Structure

```typescript
interface Particle {
  x: number;
  y: number;
  vx: number;        // velocity x
  vy: number;        // velocity y
  radius: number;
  color: string;
  life: number;      // 0-1, for fade out
  maxLife: number;
}

function createParticle(x: number, y: number): Particle {
  return {
    x,
    y,
    vx: (Math.random() - 0.5) * 2,
    vy: (Math.random() - 0.5) * 2,
    radius: 2 + Math.random() * 3,
    color: '#ffffff',
    life: 1,
    maxLife: 1
  };
}
```

### Update Loop

```typescript
function updateParticles(particles: Particle[], decay: number) {
  particles.forEach(p => {
    p.x += p.vx;
    p.y += p.vy;
    p.life -= decay;
  });

  // Remove dead particles
  return particles.filter(p => p.life > 0);
}
```

### Drawing

```typescript
function drawParticle(ctx: CanvasRenderingContext2D, p: Particle) {
  ctx.globalAlpha = p.life;
  ctx.beginPath();
  ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
  ctx.fillStyle = p.color;
  ctx.fill();
  ctx.globalAlpha = 1;
}
```

### Connection Lines

```typescript
function drawConnections(
  ctx: CanvasRenderingContext2D,
  particles: Particle[],
  threshold: number
) {
  particles.forEach((a, i) => {
    particles.slice(i + 1).forEach(b => {
      const dx = a.x - b.x;
      const dy = a.y - b.y;
      const dist = Math.sqrt(dx * dx + dy * dy);

      if (dist < threshold) {
        ctx.globalAlpha = (1 - dist / threshold) * Math.min(a.life, b.life);
        ctx.beginPath();
        ctx.moveTo(a.x, a.y);
        ctx.lineTo(b.x, b.y);
        ctx.strokeStyle = a.color;
        ctx.stroke();
      }
    });
  });
  ctx.globalAlpha = 1;
}
```

---

## Grids

### Generation

```typescript
interface Cell {
  x: number;
  y: number;
  width: number;
  height: number;
  color: string;
  delay: number;  // animation delay
}

function createGrid(
  cols: number,
  rows: number,
  cellWidth: number,
  cellHeight: number,
  baseColor: string
): Cell[] {
  const grid: Cell[] = [];

  for (let col = 0; col < cols; col++) {
    for (let row = 0; row < rows; row++) {
      grid.push({
        x: col * cellWidth,
        y: row * cellHeight,
        width: cellWidth,
        height: cellHeight,
        color: varyColor(baseColor, 0.1), // slight variation
        delay: (col + row) * 50  // stagger delay
      });
    }
  }

  return grid;
}
```

### Animation Patterns

**Wave** — Delay by distance from origin:
```typescript
cell.delay = Math.sqrt(cell.x ** 2 + cell.y ** 2) * 0.5;
```

**Cascade** — Row by row:
```typescript
cell.delay = row * 100;
```

**Random** — Independent timing:
```typescript
cell.delay = Math.random() * 1000;
```

**Ripple** — From click point:
```typescript
function setRippleDelay(cells: Cell[], clickX: number, clickY: number) {
  cells.forEach(cell => {
    const dist = Math.sqrt(
      (cell.x - clickX) ** 2 + (cell.y - clickY) ** 2
    );
    cell.delay = dist * 2;
  });
}
```

---

## Noise (Organic Variation)

### Simple Noise (No Library)

```typescript
// Value noise using sine combination
function noise(x: number, y: number, t: number): number {
  return (
    Math.sin(x * 0.01 + t) *
    Math.cos(y * 0.01 + t * 0.5) *
    0.5 + 0.5
  );
}

// Usage: returns 0-1
const value = noise(particle.x, particle.y, Date.now() * 0.001);
```

### Perlin-like Smoothness

```typescript
function smoothNoise(x: number, y: number, t: number): number {
  const frequencies = [1, 0.5, 0.25];
  const amplitudes = [1, 0.5, 0.25];

  let value = 0;
  let totalAmplitude = 0;

  frequencies.forEach((freq, i) => {
    value += Math.sin(x * freq * 0.01 + t) *
             Math.cos(y * freq * 0.01 + t * 0.7) *
             amplitudes[i];
    totalAmplitude += amplitudes[i];
  });

  return (value / totalAmplitude) * 0.5 + 0.5;
}
```

### Applications

- **Vary particle velocity**: `p.vx += (noise(p.x, p.y, t) - 0.5) * 0.1`
- **Distort grid positions**: `cell.x += noise(cell.x, cell.y, t) * 10`
- **Animate opacity**: `ctx.globalAlpha = noise(x, y, t)`
- **Color variation**: `hsl(${baseHue + noise(x, y, t) * 20}, 50%, 50%)`
````

**Step 2: Verify file length**

Run: `wc -l plugins/frontend-design/skills/creating-canvas-animations/reference/primitives.md`

Expected: Should be ~300+ lines

**Step 3: Commit**

```bash
git add plugins/frontend-design/skills/creating-canvas-animations/reference/primitives.md
git commit -m "feat(frontend-design): add primitives reference doc"
```

---

## Task 6: Create Reference - Composition

**Files:**
- Create: `plugins/frontend-design/skills/creating-canvas-animations/reference/composition.md`

**Step 1: Write composition.md**

````markdown
# Composition Principles

How to combine primitives into cohesive, intentional effects.

---

## Layering

Create depth by separating elements into layers with different behaviors.

### Three-Layer Model

| Layer | Speed | Opacity | Purpose |
|-------|-------|---------|---------|
| Background | Slowest | 0.1-0.3 | Atmosphere, texture |
| Midground | Medium | 0.4-0.7 | Primary visual interest |
| Foreground | Fastest | 0.8-1.0 | Draws attention, accents |

### Implementation

```typescript
interface Layer {
  elements: Element[];
  speed: number;
  opacity: number;
}

const layers: Layer[] = [
  { elements: backgroundParticles, speed: 0.5, opacity: 0.2 },
  { elements: mainElements, speed: 1, opacity: 0.6 },
  { elements: foregroundAccents, speed: 2, opacity: 1 }
];

function draw() {
  layers.forEach(layer => {
    ctx.globalAlpha = layer.opacity;
    layer.elements.forEach(el => {
      el.update(layer.speed);
      el.draw(ctx);
    });
  });
  ctx.globalAlpha = 1;
}
```

---

## Color Relationships

### Monochrome

Single hue, vary lightness and opacity. Always safe, always elegant.

```typescript
const baseHue = 220; // blue
const colors = {
  dark: `hsl(${baseHue}, 50%, 20%)`,
  mid: `hsl(${baseHue}, 50%, 50%)`,
  light: `hsl(${baseHue}, 50%, 80%)`,
  accent: `hsl(${baseHue}, 70%, 60%)`
};
```

### Complementary

Two opposing hues (180° apart). High contrast, use sparingly.

```typescript
const primary = 220;   // blue
const complement = 40; // orange (220 + 180 = 400 → 40)
```

### Analogous

Adjacent hues (±30°). Harmonious, natural feel.

```typescript
const base = 220;
const analogous = {
  cool: `hsl(${base - 30}, 50%, 50%)`,  // 190 - cyan
  base: `hsl(${base}, 50%, 50%)`,        // 220 - blue
  warm: `hsl(${base + 30}, 50%, 50%)`   // 250 - purple
};
```

### Color from Dominant

Extract from a hero color:

```typescript
function deriveColors(heroHex: string) {
  const hsl = hexToHsl(heroHex);
  return {
    bg: `hsl(${hsl.h}, ${hsl.s * 0.3}%, ${hsl.l * 0.2}%)`,
    surface: `hsl(${hsl.h}, ${hsl.s * 0.5}%, ${hsl.l * 0.3}%)`,
    primary: heroHex,
    accent: `hsl(${hsl.h}, ${hsl.s}%, ${Math.min(hsl.l + 20, 90)}%)`
  };
}
```

---

## Density and Spacing

### Density Guidelines

| Density | Element Count | Feel | Use Case |
|---------|---------------|------|----------|
| Sparse | 10-20 | Contemplative, minimal | Hero backgrounds, luxury |
| Medium | 50-100 | Balanced, professional | General purpose |
| Dense | 200+ | Energetic, complex | Tech, data visualization |

### Spacing Principles

- **Even spacing**: Grid-like, orderly, corporate
- **Random spacing**: Organic, natural, creative
- **Clustered**: Groups with gaps, creates focal points

```typescript
// Even
const x = col * spacing;

// Random
const x = Math.random() * width;

// Clustered
const clusterX = clusterCenters[i % clusterCenters.length].x;
const x = clusterX + (Math.random() - 0.5) * clusterRadius;
```

---

## Motion Choreography

### Stagger

Elements animate in sequence with fixed delay.

```typescript
elements.forEach((el, i) => {
  el.delay = i * 50; // 50ms between each
});
```

### Wave

Delay based on position (distance from origin).

```typescript
elements.forEach(el => {
  const dist = Math.sqrt(el.x ** 2 + el.y ** 2);
  el.delay = dist * 2; // further = later
});
```

### Cascade

Row-by-row or column-by-column.

```typescript
// Top to bottom
elements.forEach(el => {
  el.delay = el.row * 100;
});

// Left to right
elements.forEach(el => {
  el.delay = el.col * 100;
});

// Diagonal
elements.forEach(el => {
  el.delay = (el.row + el.col) * 50;
});
```

### Simultaneous

All at once. Use sparingly — often feels jarring.

```typescript
elements.forEach(el => {
  el.delay = 0;
});
```

---

## Focal Points

Direct viewer attention intentionally.

### Techniques

**Speed differential**: Faster elements draw the eye.

```typescript
// Hero element moves faster
heroElement.speed = 2;
backgroundElements.forEach(el => el.speed = 0.5);
```

**Brightness/opacity**: Brighter stands out.

```typescript
focalElement.opacity = 1;
otherElements.forEach(el => el.opacity = 0.3);
```

**Size**: Larger elements dominate.

```typescript
focalElement.radius = 10;
otherElements.forEach(el => el.radius = 2 + Math.random() * 3);
```

**Isolation**: Negative space around focal point.

```typescript
// Don't place elements within 100px of focal point
if (distance(el, focalPoint) < 100) {
  el.visible = false;
}
```

### The Rule of Thirds

Place focal points at intersection of thirds grid, not center.

```typescript
const focalPoints = [
  { x: width / 3, y: height / 3 },
  { x: width * 2/3, y: height / 3 },
  { x: width / 3, y: height * 2/3 },
  { x: width * 2/3, y: height * 2/3 }
];
```

---

## Rhythm and Repetition

### Visual Rhythm

Repeating patterns create cohesion.

```typescript
// Consistent spacing
const gap = 40;
for (let x = 0; x < width; x += gap) {
  drawElement(x, y);
}

// Consistent sizing
const sizes = [10, 20, 40]; // fixed set, not random
element.size = sizes[i % sizes.length];
```

### Breaking Rhythm

Occasional breaks create interest.

```typescript
for (let i = 0; i < count; i++) {
  const isAccent = i % 7 === 0; // every 7th is different
  element.size = isAccent ? 30 : 10;
  element.color = isAccent ? accentColor : baseColor;
}
```
````

**Step 2: Verify file exists**

Run: `head -30 plugins/frontend-design/skills/creating-canvas-animations/reference/composition.md`

Expected: Should show "# Composition Principles" header

**Step 3: Commit**

```bash
git add plugins/frontend-design/skills/creating-canvas-animations/reference/composition.md
git commit -m "feat(frontend-design): add composition reference doc"
```

---

## Task 7: Create Reference - Easing

**Files:**
- Create: `plugins/frontend-design/skills/creating-canvas-animations/reference/easing.md`

**Step 1: Write easing.md**

````markdown
# Easing Functions

A library of easing functions for canvas animations. All functions take `t` (progress 0-1) and return eased value (0-1).

---

## Core Set (Always Include)

These cover 90% of use cases.

```typescript
// Linear — constant speed, only for continuous rotation
const linear = (t: number): number => t;

// Quad — smooth, professional
const easeInQuad = (t: number): number => t * t;
const easeOutQuad = (t: number): number => t * (2 - t);
const easeInOutQuad = (t: number): number =>
  t < 0.5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2;

// Cubic — slightly more pronounced
const easeInCubic = (t: number): number => t * t * t;
const easeOutCubic = (t: number): number => 1 - Math.pow(1 - t, 3);
const easeInOutCubic = (t: number): number =>
  t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
```

---

## Expressive Set

For animations that need personality.

```typescript
// Back — overshoots then settles, playful
const easeOutBack = (t: number): number => {
  const c1 = 1.70158;
  const c3 = c1 + 1;
  return 1 + c3 * Math.pow(t - 1, 3) + c1 * Math.pow(t - 1, 2);
};

const easeInBack = (t: number): number => {
  const c1 = 1.70158;
  const c3 = c1 + 1;
  return c3 * t * t * t - c1 * t * t;
};

// Elastic — spring/bounce, energetic
const easeOutElastic = (t: number): number => {
  if (t === 0 || t === 1) return t;
  const c4 = (2 * Math.PI) / 3;
  return Math.pow(2, -10 * t) * Math.sin((t * 10 - 0.75) * c4) + 1;
};

const easeInElastic = (t: number): number => {
  if (t === 0 || t === 1) return t;
  const c4 = (2 * Math.PI) / 3;
  return -Math.pow(2, 10 * t - 10) * Math.sin((t * 10 - 10.75) * c4);
};

// Expo — dramatic deceleration, impactful
const easeOutExpo = (t: number): number =>
  t === 1 ? 1 : 1 - Math.pow(2, -10 * t);

const easeInExpo = (t: number): number =>
  t === 0 ? 0 : Math.pow(2, 10 * t - 10);

// Bounce — bouncing ball effect
const easeOutBounce = (t: number): number => {
  const n1 = 7.5625;
  const d1 = 2.75;
  if (t < 1 / d1) {
    return n1 * t * t;
  } else if (t < 2 / d1) {
    return n1 * (t -= 1.5 / d1) * t + 0.75;
  } else if (t < 2.5 / d1) {
    return n1 * (t -= 2.25 / d1) * t + 0.9375;
  } else {
    return n1 * (t -= 2.625 / d1) * t + 0.984375;
  }
};
```

---

## Usage Principle

Match easing to intent:

| Intent | Easing | Why |
|--------|--------|-----|
| Subtle, professional | Quad, Cubic | Smooth, doesn't draw attention |
| Playful, delightful | Back, Elastic | Overshoots create surprise |
| Dramatic, impactful | Expo | Fast start/end, lingering middle |
| Physical, realistic | Bounce | Mimics real-world physics |

---

## Application Pattern

```typescript
function animate(
  from: number,
  to: number,
  duration: number,
  easing: (t: number) => number,
  onUpdate: (value: number) => void,
  onComplete?: () => void
) {
  const startTime = Date.now();

  function tick() {
    const elapsed = Date.now() - startTime;
    const progress = Math.min(elapsed / duration, 1);
    const easedProgress = easing(progress);
    const value = from + (to - from) * easedProgress;

    onUpdate(value);

    if (progress < 1) {
      requestAnimationFrame(tick);
    } else if (onComplete) {
      onComplete();
    }
  }

  tick();
}

// Usage
animate(0, 100, 500, easeOutQuad, (x) => {
  element.x = x;
});
```

---

## Chaining Easings

For complex animations, chain multiple easings:

```typescript
function chainedEase(t: number): number {
  if (t < 0.5) {
    // First half: ease in
    return easeInQuad(t * 2) * 0.5;
  } else {
    // Second half: bounce out
    return 0.5 + easeOutBounce((t - 0.5) * 2) * 0.5;
  }
}
```
````

**Step 2: Verify file exists**

Run: `grep -c "const ease" plugins/frontend-design/skills/creating-canvas-animations/reference/easing.md`

Expected: Should be 10+ (counting easing function declarations)

**Step 3: Commit**

```bash
git add plugins/frontend-design/skills/creating-canvas-animations/reference/easing.md
git commit -m "feat(frontend-design): add easing functions reference"
```

---

## Task 8: Create Reference - Performance

**Files:**
- Create: `plugins/frontend-design/skills/creating-canvas-animations/reference/performance.md`

**Step 1: Write performance.md**

````markdown
# Performance Patterns

Production-grade performance optimizations for canvas animations.

---

## The Basics

### Always Use requestAnimationFrame

```typescript
// ❌ Never do this
setInterval(draw, 16);

// ✅ Always do this
function animate() {
  draw();
  animationId = requestAnimationFrame(animate);
}
animate();
```

### Cache Canvas Context

```typescript
// ❌ Don't query every frame
function draw() {
  const ctx = canvas.getContext('2d'); // expensive
  // ...
}

// ✅ Cache once
const ctx = canvas.getContext('2d');
function draw() {
  // use cached ctx
}
```

### Batch Draws

```typescript
// ❌ Multiple strokes
lines.forEach(line => {
  ctx.beginPath();
  ctx.moveTo(line.x1, line.y1);
  ctx.lineTo(line.x2, line.y2);
  ctx.stroke(); // called N times
});

// ✅ Single stroke
ctx.beginPath();
lines.forEach(line => {
  ctx.moveTo(line.x1, line.y1);
  ctx.lineTo(line.x2, line.y2);
});
ctx.stroke(); // called once
```

---

## Retina/DPI Handling

Always scale for device pixel ratio.

```typescript
function setupCanvas(
  canvas: HTMLCanvasElement,
  width: number,
  height: number
): CanvasRenderingContext2D {
  const dpr = window.devicePixelRatio || 1;

  // Set actual size in memory
  canvas.width = width * dpr;
  canvas.height = height * dpr;

  // Set display size
  canvas.style.width = `${width}px`;
  canvas.style.height = `${height}px`;

  const ctx = canvas.getContext('2d')!;

  // Scale context to match
  ctx.scale(dpr, dpr);

  return ctx;
}
```

---

## Visibility Optimization

Pause when tab is not visible — saves CPU/battery.

```typescript
let animationId: number;
let isPaused = false;

function pause() {
  isPaused = true;
  cancelAnimationFrame(animationId);
}

function resume() {
  if (isPaused) {
    isPaused = false;
    animate();
  }
}

document.addEventListener('visibilitychange', () => {
  if (document.hidden) {
    pause();
  } else {
    resume();
  }
});
```

---

## Resize Handling

Use ResizeObserver, not window resize event.

```typescript
function setupResize(
  container: HTMLElement,
  canvas: HTMLCanvasElement,
  onResize: (width: number, height: number) => void
) {
  const ro = new ResizeObserver(entries => {
    const { width, height } = entries[0].contentRect;

    // Debounce for performance
    clearTimeout(resizeTimeout);
    resizeTimeout = setTimeout(() => {
      setupCanvas(canvas, width, height);
      onResize(width, height);
    }, 100);
  });

  ro.observe(container);

  return () => ro.disconnect(); // cleanup
}
```

---

## Memory Management

### Object Pooling

Avoid GC spikes by reusing objects.

```typescript
class ParticlePool {
  private pool: Particle[] = [];
  private active: Particle[] = [];

  acquire(): Particle {
    const particle = this.pool.pop() || this.createParticle();
    this.active.push(particle);
    return particle;
  }

  release(particle: Particle) {
    const index = this.active.indexOf(particle);
    if (index > -1) {
      this.active.splice(index, 1);
      this.resetParticle(particle);
      this.pool.push(particle);
    }
  }

  private createParticle(): Particle {
    return { x: 0, y: 0, vx: 0, vy: 0, life: 1, /* ... */ };
  }

  private resetParticle(p: Particle) {
    p.x = 0; p.y = 0; p.vx = 0; p.vy = 0; p.life = 1;
  }
}
```

### Cleanup Function

Always provide a destroy method.

```typescript
export function initAnimation(canvas: HTMLCanvasElement, options: Options) {
  const ctx = setupCanvas(canvas, options.width, options.height);
  const ro = setupResize(/* ... */);
  let animationId: number;

  function animate() {
    draw(ctx);
    animationId = requestAnimationFrame(animate);
  }

  animate();

  // MUST return cleanup function
  return {
    destroy() {
      cancelAnimationFrame(animationId);
      ro.disconnect();
      // Clear any references
      particles.length = 0;
    },
    pause,
    resume
  };
}
```

---

## Graceful Degradation

Reduce complexity if frame rate drops.

```typescript
let lastFrameTime = Date.now();
let frameCount = 0;
let fps = 60;

function measureFps() {
  frameCount++;
  const now = Date.now();

  if (now - lastFrameTime >= 1000) {
    fps = frameCount;
    frameCount = 0;
    lastFrameTime = now;

    // Reduce particle count if dropping frames
    if (fps < 30 && particles.length > 50) {
      particles.length = Math.floor(particles.length * 0.8);
      console.warn(`Reduced particles to ${particles.length} for performance`);
    }
  }
}

function animate() {
  measureFps();
  draw();
  requestAnimationFrame(animate);
}
```

---

## Target Metrics

| Metric | Target | Action if Missed |
|--------|--------|------------------|
| Frame rate | 60fps (16.67ms/frame) | Reduce particle count, simplify effects |
| First paint | <100ms | Pre-calculate initial state |
| Memory | Stable | Use object pooling, clear references |
| CPU (idle tab) | 0% | Pause on visibility change |

---

## Full Boilerplate

Every animation should include this structure:

```typescript
export interface AnimationOptions {
  // ... specific options
}

export interface AnimationController {
  destroy: () => void;
  pause: () => void;
  resume: () => void;
}

export function initAnimation(
  canvas: HTMLCanvasElement,
  options: AnimationOptions
): AnimationController {
  // 1. Setup
  const dpr = window.devicePixelRatio || 1;
  const ctx = canvas.getContext('2d')!;
  let width = canvas.clientWidth;
  let height = canvas.clientHeight;
  let animationId: number;
  let isPaused = false;

  // 2. DPI scaling
  function resize(w: number, h: number) {
    width = w;
    height = h;
    canvas.width = w * dpr;
    canvas.height = h * dpr;
    canvas.style.width = `${w}px`;
    canvas.style.height = `${h}px`;
    ctx.scale(dpr, dpr);
  }
  resize(width, height);

  // 3. ResizeObserver
  const ro = new ResizeObserver(entries => {
    const { width: w, height: h } = entries[0].contentRect;
    resize(w, h);
  });
  ro.observe(canvas.parentElement || canvas);

  // 4. Visibility API
  function onVisibilityChange() {
    if (document.hidden) pause();
    else resume();
  }
  document.addEventListener('visibilitychange', onVisibilityChange);

  // 5. Animation loop
  function animate() {
    if (isPaused) return;
    draw();
    animationId = requestAnimationFrame(animate);
  }

  function draw() {
    ctx.clearRect(0, 0, width, height);
    // ... drawing logic
  }

  // 6. Controls
  function pause() {
    isPaused = true;
    cancelAnimationFrame(animationId);
  }

  function resume() {
    if (!isPaused) return;
    isPaused = false;
    animate();
  }

  // 7. Start
  animate();

  // 8. Return controller
  return {
    destroy() {
      pause();
      ro.disconnect();
      document.removeEventListener('visibilitychange', onVisibilityChange);
    },
    pause,
    resume
  };
}
```
````

**Step 2: Verify file exists**

Run: `tail -20 plugins/frontend-design/skills/creating-canvas-animations/reference/performance.md`

Expected: Should show the closing of the "Full Boilerplate" code block

**Step 3: Commit**

```bash
git add plugins/frontend-design/skills/creating-canvas-animations/reference/performance.md
git commit -m "feat(frontend-design): add performance patterns reference"
```

---

## Task 9: Create Reference - Examples

**Files:**
- Create: `plugins/frontend-design/skills/creating-canvas-animations/reference/examples.md`

**Step 1: Write examples.md**

````markdown
# Worked Examples

Real-world animation patterns inspired by [Interface Craft](https://interfacecraft.dev).

These demonstrate how to apply primitives + composition principles, not templates to copy.

---

## Diagonal Line Pattern

**Inspiration:** "Working Knowledge" card — orange diagonal stripes

### Analysis

- Parallel lines at ~45° angle
- Single color (orange) with subtle opacity
- Optional: slow drift animation
- Dense enough to create texture, sparse enough to read text over

### Implementation

```typescript
interface DiagonalLinesOptions {
  color: string;
  lineWidth: number;
  spacing: number;
  angle: number;       // degrees
  opacity: number;
  drift: boolean;
  driftSpeed: number;  // pixels per second
}

const defaults: DiagonalLinesOptions = {
  color: '#f97316',    // orange-500
  lineWidth: 1.5,
  spacing: 25,
  angle: 45,
  opacity: 0.4,
  drift: true,
  driftSpeed: 20
};

function drawDiagonalLines(
  ctx: CanvasRenderingContext2D,
  width: number,
  height: number,
  options: DiagonalLinesOptions,
  time: number
) {
  const { color, lineWidth, spacing, angle, opacity, drift, driftSpeed } = options;
  const radians = (angle * Math.PI) / 180;

  // Calculate offset for drift
  const offset = drift ? (time * driftSpeed / 1000) % spacing : 0;

  // Calculate how many lines we need
  const diagonal = Math.sqrt(width * width + height * height);
  const lineCount = Math.ceil(diagonal / spacing) + 2;

  ctx.save();
  ctx.strokeStyle = color;
  ctx.lineWidth = lineWidth;
  ctx.globalAlpha = opacity;

  // Rotate canvas
  ctx.translate(width / 2, height / 2);
  ctx.rotate(radians);
  ctx.translate(-width / 2, -height / 2);

  // Draw lines
  ctx.beginPath();
  for (let i = -lineCount; i < lineCount; i++) {
    const x = i * spacing + offset;
    ctx.moveTo(x, -diagonal);
    ctx.lineTo(x, diagonal * 2);
  }
  ctx.stroke();
  ctx.restore();
}
```

---

## Grid/Mosaic Tiles

**Inspiration:** "Practical Demonstration" card — tan/beige mosaic

### Analysis

- Rectangular cells in a grid
- Slight color variation within same hue family
- Some cells taller than others (varied heights)
- Subtle pulse or fade animation

### Implementation

```typescript
interface MosaicOptions {
  baseColor: string;
  colorVariation: number;  // 0-1, how much to vary lightness
  cellWidth: number;
  cellHeight: number;
  heightVariation: number; // 0-1, how much cell heights vary
  gap: number;
  animationStyle: 'pulse' | 'fade' | 'none';
}

interface Cell {
  x: number;
  y: number;
  width: number;
  height: number;
  color: string;
  phase: number;  // for animation offset
}

function createMosaicCells(
  width: number,
  height: number,
  options: MosaicOptions
): Cell[] {
  const cells: Cell[] = [];
  const { cellWidth, cellHeight, gap, heightVariation, baseColor, colorVariation } = options;
  const baseHsl = hexToHsl(baseColor);

  for (let x = 0; x < width; x += cellWidth + gap) {
    for (let y = 0; y < height; y += cellHeight + gap) {
      // Vary height
      const h = cellHeight * (1 - heightVariation + Math.random() * heightVariation);

      // Vary color lightness
      const lightness = baseHsl.l + (Math.random() - 0.5) * colorVariation * 50;
      const color = `hsl(${baseHsl.h}, ${baseHsl.s}%, ${Math.max(0, Math.min(100, lightness))}%)`;

      cells.push({
        x,
        y,
        width: cellWidth,
        height: h,
        color,
        phase: Math.random() * Math.PI * 2
      });
    }
  }

  return cells;
}

function drawMosaic(
  ctx: CanvasRenderingContext2D,
  cells: Cell[],
  time: number,
  animationStyle: 'pulse' | 'fade' | 'none'
) {
  cells.forEach(cell => {
    let alpha = 1;

    if (animationStyle === 'pulse') {
      alpha = 0.6 + Math.sin(time * 0.002 + cell.phase) * 0.4;
    } else if (animationStyle === 'fade') {
      alpha = 0.3 + Math.sin(time * 0.001 + cell.phase) * 0.2;
    }

    ctx.globalAlpha = alpha;
    ctx.fillStyle = cell.color;
    ctx.fillRect(cell.x, cell.y, cell.width, cell.height);
  });

  ctx.globalAlpha = 1;
}
```

---

## Matrix/Code Rain

**Inspiration:** "Building Interface Kit" card — green character rain

### Analysis

- Vertical columns of characters
- Characters fade as they fall (trail effect)
- Monospace font (JetBrains Mono, Fira Code)
- Continuous loop, no visible reset

### Implementation

```typescript
interface MatrixRainOptions {
  color: string;
  charset: string;
  fontSize: number;
  columnDensity: number;  // 0-1, percentage of columns filled
  fallSpeed: number;
  fadeStrength: number;   // 0-1, how much to fade per frame
}

interface Column {
  x: number;
  y: number;
  speed: number;
  chars: string[];
  length: number;
}

const defaultCharset = 'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン0123456789';

function createColumns(
  width: number,
  height: number,
  options: MatrixRainOptions
): Column[] {
  const columns: Column[] = [];
  const { fontSize, columnDensity, fallSpeed, charset } = options;
  const colWidth = fontSize;
  const colCount = Math.floor(width / colWidth);

  for (let i = 0; i < colCount; i++) {
    if (Math.random() > columnDensity) continue;

    const chars: string[] = [];
    const length = 10 + Math.floor(Math.random() * 20);
    for (let j = 0; j < length; j++) {
      chars.push(charset[Math.floor(Math.random() * charset.length)]);
    }

    columns.push({
      x: i * colWidth,
      y: Math.random() * -height,
      speed: fallSpeed * (0.5 + Math.random()),
      chars,
      length
    });
  }

  return columns;
}

function drawMatrixRain(
  ctx: CanvasRenderingContext2D,
  columns: Column[],
  width: number,
  height: number,
  options: MatrixRainOptions
) {
  const { color, fontSize, fadeStrength } = options;

  // Fade effect
  ctx.fillStyle = `rgba(0, 0, 0, ${fadeStrength})`;
  ctx.fillRect(0, 0, width, height);

  ctx.font = `${fontSize}px 'JetBrains Mono', monospace`;

  columns.forEach(col => {
    // Draw characters with gradient fade
    col.chars.forEach((char, i) => {
      const y = col.y - i * fontSize;
      if (y < -fontSize || y > height + fontSize) return;

      // Head is brightest, tail fades
      const brightness = 1 - (i / col.length);
      ctx.fillStyle = i === 0
        ? '#ffffff'  // bright head
        : `rgba(${hexToRgb(color)}, ${brightness})`;

      ctx.fillText(char, col.x, y);
    });

    // Move column
    col.y += col.speed;

    // Reset when off screen
    if (col.y - col.length * fontSize > height) {
      col.y = Math.random() * -200;
      // Randomize chars on reset
      col.chars = col.chars.map(() =>
        options.charset[Math.floor(Math.random() * options.charset.length)]
      );
    }
  });
}
```

---

## Wireframe UI Mockup

**Inspiration:** "Interface Kit" card — black with white UI rectangles

### Analysis

- Rectangles representing UI panels
- Outline only (stroke, not fill)
- Arranged to suggest an interface layout
- Optional: sequential reveal animation

### Implementation

```typescript
interface WireframeOptions {
  strokeColor: string;
  strokeWidth: number;
  panels: PanelConfig[] | 'auto';
  animationStyle: 'draw' | 'fade' | 'sequence' | 'none';
  animationDuration: number;
}

interface PanelConfig {
  x: number;      // percentage 0-100
  y: number;
  width: number;
  height: number;
  delay: number;  // ms
}

// Auto-generate a dashboard-like layout
function generateAutoPanels(): PanelConfig[] {
  return [
    // Sidebar
    { x: 2, y: 2, width: 18, height: 96, delay: 0 },
    // Header
    { x: 22, y: 2, width: 76, height: 10, delay: 100 },
    // Main content cards
    { x: 22, y: 14, width: 35, height: 40, delay: 200 },
    { x: 59, y: 14, width: 39, height: 40, delay: 300 },
    // Bottom panels
    { x: 22, y: 56, width: 50, height: 42, delay: 400 },
    { x: 74, y: 56, width: 24, height: 42, delay: 500 },
  ];
}

function drawWireframe(
  ctx: CanvasRenderingContext2D,
  width: number,
  height: number,
  options: WireframeOptions,
  time: number,
  startTime: number
) {
  const { strokeColor, strokeWidth, animationStyle, animationDuration } = options;
  const panels = options.panels === 'auto' ? generateAutoPanels() : options.panels;
  const elapsed = time - startTime;

  ctx.strokeStyle = strokeColor;
  ctx.lineWidth = strokeWidth;

  panels.forEach(panel => {
    const x = (panel.x / 100) * width;
    const y = (panel.y / 100) * height;
    const w = (panel.width / 100) * width;
    const h = (panel.height / 100) * height;

    let progress = 1;

    if (animationStyle === 'sequence') {
      const panelStart = panel.delay;
      const panelElapsed = elapsed - panelStart;
      progress = Math.max(0, Math.min(1, panelElapsed / (animationDuration / panels.length)));
    } else if (animationStyle === 'fade') {
      progress = Math.max(0, Math.min(1, (elapsed - panel.delay) / animationDuration));
      ctx.globalAlpha = progress;
    } else if (animationStyle === 'draw') {
      progress = Math.max(0, Math.min(1, (elapsed - panel.delay) / animationDuration));
    }

    if (progress <= 0) return;

    if (animationStyle === 'draw') {
      // Draw rectangle progressively
      const perimeter = 2 * (w + h);
      const drawLength = perimeter * progress;

      ctx.beginPath();
      drawPartialRect(ctx, x, y, w, h, drawLength);
      ctx.stroke();
    } else {
      ctx.strokeRect(x, y, w, h);
    }
  });

  ctx.globalAlpha = 1;
}

// Helper to draw partial rectangle (for "draw" animation)
function drawPartialRect(
  ctx: CanvasRenderingContext2D,
  x: number, y: number,
  w: number, h: number,
  length: number
) {
  const sides = [
    { dx: w, dy: 0 },   // top
    { dx: 0, dy: h },   // right
    { dx: -w, dy: 0 },  // bottom
    { dx: 0, dy: -h }   // left
  ];

  ctx.moveTo(x, y);
  let remaining = length;
  let cx = x, cy = y;

  for (const side of sides) {
    const sideLength = Math.abs(side.dx || side.dy);
    if (remaining <= 0) break;

    const draw = Math.min(remaining, sideLength);
    const ratio = draw / sideLength;

    cx += side.dx * ratio;
    cy += side.dy * ratio;
    ctx.lineTo(cx, cy);

    remaining -= sideLength;
  }
}
```

---

## Combining Techniques

These examples can be combined. For instance:

- **Particles over grid**: Background mosaic + foreground floating particles
- **Lines with noise**: Diagonal lines where positions are offset by noise
- **Wireframe with glow**: Draw wireframe twice — once blurred for glow, once sharp

The primitives and composition principles let you create any combination.
````

**Step 2: Verify file exists**

Run: `grep -c "##" plugins/frontend-design/skills/creating-canvas-animations/reference/examples.md`

Expected: Should be 5+ (section headers)

**Step 3: Commit**

```bash
git add plugins/frontend-design/skills/creating-canvas-animations/reference/examples.md
git commit -m "feat(frontend-design): add worked examples reference"
```

---

## Task 10: Create Framework - Typography

**Files:**
- Create: `plugins/frontend-design/frameworks/typography.md`

**Step 1: Write typography.md**

```markdown
# Typography System

Opinionated font selection and usage patterns.

---

## The Rule

**Never use:** Inter, Roboto, Open Sans, Lato, system-ui defaults.

These are safe choices that signal "I didn't think about this." Distinctive typography signals intention.

---

## Recommended by Context

| Context | Display Font | Body Font | Mono Font |
|---------|--------------|-----------|-----------|
| **Technical/Dev** | Space Grotesk | IBM Plex Sans | JetBrains Mono |
| **Editorial** | Playfair Display | Source Serif 4 | — |
| **Startup/Modern** | Clash Display | Satoshi | Fira Code |
| **Luxury** | Cormorant Garamond | Lora | — |
| **Brutalist** | Obviously | Neue Haas Grotesk | IBM Plex Mono |

### Font Sources

- [Google Fonts](https://fonts.google.com) — Free, easy CDN
- [Fontshare](https://fontshare.com) — Free, high quality (Satoshi, Clash Display)
- [Adobe Fonts](https://fonts.adobe.com) — Paid, extensive library

---

## Loading Strategy

### Critical Fonts (Above the fold)

```html
<head>
  <!-- Preload critical fonts -->
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="preload" as="font" type="font/woff2"
        href="/fonts/display.woff2" crossorigin>

  <!-- Load with swap for body, optional for display -->
  <style>
    @font-face {
      font-family: 'Display';
      src: url('/fonts/display.woff2') format('woff2');
      font-display: optional; /* Don't flash if slow */
    }

    @font-face {
      font-family: 'Body';
      src: url('/fonts/body.woff2') format('woff2');
      font-display: swap; /* Show fallback, then swap */
    }
  </style>
</head>
```

### Subsetting

Only include characters you need:

```bash
# Using pyftsubset
pyftsubset font.ttf \
  --unicodes="U+0020-007E,U+00A0-00FF" \
  --layout-features="kern,liga" \
  --output-file="font-subset.woff2" \
  --flavor="woff2"
```

---

## Type Scale

Use a consistent multiplier, not arbitrary sizes.

### Recommended Scales

| Scale | Multiplier | Use Case |
|-------|------------|----------|
| Minor Third | 1.2 | Compact UI, dense information |
| Major Third | 1.25 | General purpose, balanced |
| Perfect Fourth | 1.333 | Editorial, generous spacing |
| Golden Ratio | 1.618 | Display, dramatic hierarchy |

### Example (Major Third, base 16px)

```css
:root {
  --font-size-xs: 0.64rem;   /* 10.24px */
  --font-size-sm: 0.8rem;    /* 12.8px */
  --font-size-base: 1rem;    /* 16px */
  --font-size-lg: 1.25rem;   /* 20px */
  --font-size-xl: 1.563rem;  /* 25px */
  --font-size-2xl: 1.953rem; /* 31.25px */
  --font-size-3xl: 2.441rem; /* 39px */
  --font-size-4xl: 3.052rem; /* 48.8px */
}
```

---

## Hierarchy Rules

### Minimum Contrast

For clear hierarchy, size jumps should be **3x or more**.

```css
/* ❌ Weak hierarchy */
h1 { font-size: 24px; }
h2 { font-size: 20px; }  /* Only 1.2x — hard to distinguish */

/* ✅ Strong hierarchy */
h1 { font-size: 48px; }
h2 { font-size: 24px; }  /* 2x — clear distinction */
p  { font-size: 16px; }  /* 1.5x from h2 — readable flow */
```

### Weight Contrast

Use extremes: 100/200 vs 700/800, not 400 vs 500.

```css
/* ❌ Weak */
h1 { font-weight: 600; }
p  { font-weight: 400; }

/* ✅ Strong */
h1 { font-weight: 800; }
p  { font-weight: 300; }
```

---

## Line Height

| Element | Line Height | Why |
|---------|-------------|-----|
| Display/Headings | 1.1-1.2 | Tight, compact |
| Body text | 1.5-1.7 | Readable, breathable |
| UI labels | 1.2-1.4 | Compact but legible |

```css
h1, h2, h3 { line-height: 1.15; }
p, li { line-height: 1.6; }
button, label { line-height: 1.3; }
```

---

## Letter Spacing

| Context | Letter Spacing |
|---------|----------------|
| Large display (>48px) | -0.02em to -0.04em (tighten) |
| Body text | 0 (default) |
| All caps | +0.05em to +0.1em (loosen) |
| Small text (<12px) | +0.02em (improve legibility) |

```css
.display { letter-spacing: -0.03em; }
.allcaps { letter-spacing: 0.08em; text-transform: uppercase; }
.fine-print { letter-spacing: 0.02em; }
```
```

**Step 2: Verify file exists**

Run: `head -20 plugins/frontend-design/frameworks/typography.md`

Expected: Should show "# Typography System" header

**Step 3: Commit**

```bash
git add plugins/frontend-design/frameworks/typography.md
git commit -m "feat(frontend-design): add typography framework"
```

---

## Task 11: Create Framework - Color

**Files:**
- Create: `plugins/frontend-design/frameworks/color.md`

**Step 1: Write color.md**

```markdown
# Color System

Opinionated color palette generation and usage.

---

## Core Principle

**Dominant color + sharp accent beats evenly-distributed palettes.**

Commit to a palette. Don't hedge with "safe" neutrals everywhere.

---

## CSS Variable Structure

Every project should define these semantic colors:

```css
:root {
  /* Backgrounds */
  --color-bg: #ffffff;
  --color-surface: #f5f5f5;
  --color-surface-elevated: #ffffff;

  /* Text */
  --color-text-primary: #171717;
  --color-text-secondary: #525252;
  --color-text-tertiary: #a3a3a3;

  /* Accent */
  --color-accent: #f97316;
  --color-accent-hover: #ea580c;
  --color-accent-subtle: #fff7ed;

  /* Semantic */
  --color-success: #22c55e;
  --color-warning: #eab308;
  --color-error: #ef4444;

  /* Borders */
  --color-border: #e5e5e5;
  --color-border-strong: #d4d4d4;
}
```

---

## Generating from Hero Color

Start with ONE hero color, derive the rest.

```typescript
function generatePalette(heroHex: string) {
  const hsl = hexToHsl(heroHex);

  return {
    // Hero and variants
    accent: heroHex,
    accentHover: `hsl(${hsl.h}, ${hsl.s}%, ${hsl.l - 10}%)`,
    accentSubtle: `hsl(${hsl.h}, ${hsl.s * 0.3}%, 97%)`,

    // Neutrals derived from hero hue
    bg: `hsl(${hsl.h}, 5%, 100%)`,
    surface: `hsl(${hsl.h}, 5%, 97%)`,
    textPrimary: `hsl(${hsl.h}, 10%, 10%)`,
    textSecondary: `hsl(${hsl.h}, 5%, 40%)`,
    border: `hsl(${hsl.h}, 5%, 90%)`
  };
}
```

---

## Dark Mode

Dark mode is NOT "invert colors." It's a separate, intentional palette.

### Principles

1. **Background**: Not pure black (#000). Use #0a0a0a to #171717.
2. **Text**: Not pure white (#fff). Use #fafafa to #e5e5e5.
3. **Accent**: May need adjustment for contrast on dark backgrounds.
4. **Elevation**: Lighter surfaces feel "raised" in dark mode (opposite of light).

```css
@media (prefers-color-scheme: dark) {
  :root {
    --color-bg: #0a0a0a;
    --color-surface: #171717;
    --color-surface-elevated: #262626;

    --color-text-primary: #fafafa;
    --color-text-secondary: #a3a3a3;
    --color-text-tertiary: #525252;

    --color-border: #262626;
    --color-border-strong: #404040;
  }
}
```

---

## Contrast Requirements

WCAG 2.1 minimum ratios:

| Use Case | Minimum Ratio |
|----------|---------------|
| Body text | 4.5:1 |
| Large text (>18px bold, >24px) | 3:1 |
| UI components, graphics | 3:1 |
| Decorative | No requirement |

### Testing

```typescript
function getContrastRatio(fg: string, bg: string): number {
  const fgLum = getLuminance(fg);
  const bgLum = getLuminance(bg);
  const lighter = Math.max(fgLum, bgLum);
  const darker = Math.min(fgLum, bgLum);
  return (lighter + 0.05) / (darker + 0.05);
}

function getLuminance(hex: string): number {
  const rgb = hexToRgb(hex);
  const [r, g, b] = [rgb.r, rgb.g, rgb.b].map(c => {
    c = c / 255;
    return c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4);
  });
  return 0.2126 * r + 0.7152 * g + 0.0722 * b;
}
```

---

## Color Relationships

### Monochrome

Single hue, vary lightness. Always works.

```css
--color-100: hsl(220, 50%, 95%);
--color-200: hsl(220, 50%, 85%);
--color-300: hsl(220, 50%, 70%);
--color-500: hsl(220, 50%, 50%);
--color-700: hsl(220, 50%, 30%);
--color-900: hsl(220, 50%, 15%);
```

### Complementary

Two hues 180° apart. High contrast, use sparingly.

```css
--primary: hsl(220, 50%, 50%);   /* Blue */
--complement: hsl(40, 50%, 50%); /* Orange */
```

### Analogous

Adjacent hues (±30°). Harmonious.

```css
--cool: hsl(190, 50%, 50%);  /* Cyan */
--base: hsl(220, 50%, 50%);  /* Blue */
--warm: hsl(250, 50%, 50%);  /* Purple */
```

---

## What to Avoid

- **Purple gradient on white** — The #1 "AI slop" indicator
- **Rainbow palettes** — Too many hues = visual chaos
- **Low contrast "aesthetic" choices** — Accessibility isn't optional
- **Pure black (#000) on pure white (#fff)** — Too harsh, use near-black/white
```

**Step 2: Verify file exists**

Run: `grep "color-" plugins/frontend-design/frameworks/color.md | head -10`

Expected: Should show CSS variable declarations

**Step 3: Commit**

```bash
git add plugins/frontend-design/frameworks/color.md
git commit -m "feat(frontend-design): add color framework"
```

---

## Task 12: Create Framework - Motion

**Files:**
- Create: `plugins/frontend-design/frameworks/motion.md`

**Step 1: Write motion.md**

```markdown
# Motion Principles

When and how to use animation effectively.

---

## Hierarchy of Impact

Not all motion is equal. Prioritize high-impact moments.

| Level | Type | Impact | Example |
|-------|------|--------|---------|
| 1 | Page transitions | Highest | Route changes, major state shifts |
| 2 | Component entrances | High | Modal opens, panel slides in |
| 3 | State changes | Medium | Hover, focus, active states |
| 4 | Micro-interactions | Lowest | Button ripples, icon morphs |

**Rule:** One well-orchestrated page load with staggered reveals creates more delight than scattered micro-interactions.

---

## Timing

### Duration by Context

| Context | Duration | Why |
|---------|----------|-----|
| Instant feedback | 100-150ms | Buttons, toggles — must feel immediate |
| State transitions | 200-300ms | Hover effects, color changes |
| Component motion | 300-500ms | Modals, panels, drawers |
| Page transitions | 400-600ms | Route changes, major reveals |
| Atmospheric | 1000ms+ | Background animations, ambient effects |

### The 200ms Rule

If an interaction feels sluggish, it's probably >200ms. Under 100ms feels instant but may be too fast to register visually.

---

## Easing

### Never Use Linear

Linear motion feels robotic and unnatural. Real objects accelerate and decelerate.

```css
/* ❌ Robotic */
transition: transform 300ms linear;

/* ✅ Natural */
transition: transform 300ms ease-out;
```

### Easing by Context

| Action | Easing | Curve | Why |
|--------|--------|-------|-----|
| **Entrances** | ease-out | Fast start, slow end | Element arrives and settles |
| **Exits** | ease-in | Slow start, fast end | Element accelerates away |
| **State changes** | ease-in-out | Slow-fast-slow | Smooth position changes |
| **Emphasis** | ease-out-back | Overshoots then settles | Playful, attention-grabbing |

### CSS Custom Easings

```css
:root {
  --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-in: cubic-bezier(0.7, 0, 0.84, 0);
  --ease-in-out: cubic-bezier(0.87, 0, 0.13, 1);
  --ease-out-back: cubic-bezier(0.34, 1.56, 0.64, 1);
  --ease-elastic: cubic-bezier(0.68, -0.6, 0.32, 1.6);
}
```

---

## Staggered Reveals

The most impactful animation pattern. Elements appear in sequence.

```css
.card {
  opacity: 0;
  transform: translateY(20px);
  animation: fadeUp 400ms var(--ease-out) forwards;
}

.card:nth-child(1) { animation-delay: 0ms; }
.card:nth-child(2) { animation-delay: 50ms; }
.card:nth-child(3) { animation-delay: 100ms; }
.card:nth-child(4) { animation-delay: 150ms; }

@keyframes fadeUp {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

### Stagger Timing

- **Fast stagger (30-50ms)**: Feels like a wave
- **Medium stagger (75-100ms)**: Each item distinct but connected
- **Slow stagger (150ms+)**: Very deliberate, dramatic

---

## Reduced Motion

Always respect user preferences.

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

For JavaScript animations:

```typescript
const prefersReducedMotion = window.matchMedia(
  '(prefers-reduced-motion: reduce)'
).matches;

const duration = prefersReducedMotion ? 0 : 300;
```

---

## Performance

### Animate Only Transform and Opacity

These are GPU-accelerated and don't trigger layout.

```css
/* ❌ Triggers layout */
.bad {
  transition: width 300ms, height 300ms, top 300ms, left 300ms;
}

/* ✅ GPU-accelerated */
.good {
  transition: transform 300ms, opacity 300ms;
}
```

### Will-Change

Hint to browser for optimization (use sparingly).

```css
.will-animate {
  will-change: transform, opacity;
}

.animating {
  transform: translateX(100px);
}

.done {
  will-change: auto; /* Remove after animation */
}
```

---

## What to Avoid

- **Bouncing/pulsing CTAs** — Desperate, annoying
- **Auto-playing carousels** — Users hate them
- **Parallax everything** — Nauseating, often breaks scroll
- **Loading spinners longer than 1s** — Use skeleton screens instead
- **Animations that block interaction** — Never prevent user action
```

**Step 2: Verify file exists**

Run: `grep -c "##" plugins/frontend-design/frameworks/motion.md`

Expected: Should be 7+ (section count)

**Step 3: Commit**

```bash
git add plugins/frontend-design/frameworks/motion.md
git commit -m "feat(frontend-design): add motion principles framework"
```

---

## Task 13: Create Framework - Anti-Patterns

**Files:**
- Create: `plugins/frontend-design/frameworks/anti-patterns.md`

**Step 1: Write anti-patterns.md**

```markdown
# Anti-Patterns

What to avoid — the "AI slop" checklist.

---

## The Problem

AI-generated frontends tend to converge on safe, generic choices. This creates a recognizable "AI aesthetic" that signals "no human thought went into this."

Distinctive design requires intentional choices, not defaults.

---

## The Checklist

Before shipping, verify NONE of these apply:

### Typography
- [ ] Using Inter, Roboto, Open Sans, or system fonts as primary
- [ ] All text at similar sizes (weak hierarchy)
- [ ] Font weights only 400 and 600 (use extremes: 300 vs 800)
- [ ] Generic sans-serif everywhere (no personality)

### Color
- [ ] Purple/violet gradient on white background (THE #1 tell)
- [ ] Blue as primary with no secondary consideration
- [ ] Evenly-distributed rainbow palette (too many hues)
- [ ] Gray-on-gray with no accent color
- [ ] Pure black (#000) on pure white (#fff)

### Layout
- [ ] Three-column card grid with equal spacing
- [ ] Hero section with centered text and gradient background
- [ ] Identical border-radius on every element
- [ ] No asymmetry or visual tension anywhere
- [ ] Predictable component placement (logo top-left, CTA top-right)

### Motion
- [ ] Micro-interactions on everything
- [ ] Bouncing/pulsing call-to-action buttons
- [ ] Auto-playing carousels
- [ ] Fade-in on scroll for every element
- [ ] No motion at all (equally generic)

### Imagery
- [ ] Generic stock photos of people shaking hands
- [ ] Abstract 3D blob shapes
- [ ] Gradient mesh backgrounds
- [ ] Illustrations in "corporate Memphis" style

### Components
- [ ] Cards with drop shadows AND rounded corners AND borders
- [ ] Buttons with too many states (gradient + shadow + border + icon)
- [ ] Forms with placeholder text as labels
- [ ] Modals for everything

---

## Why These Fail

Generic choices signal:
- "I didn't think about this"
- "I went with the first suggestion"
- "I optimized for safety, not impact"

Distinctive choices signal:
- "I made an intentional decision"
- "I understand the context"
- "I care about craft"

---

## The Fix

For each anti-pattern, ask: **"What would a human designer with taste do differently?"**

### Instead of Inter
→ Pick a font that matches the brand personality. Technical product? Try Space Grotesk. Luxury? Try Cormorant. Startup? Try Satoshi.

### Instead of purple gradient
→ Commit to ONE hero color. Derive palette from it. Let it dominate.

### Instead of three-column grid
→ Try asymmetry. Try two columns with different widths. Try a single column with generous margins.

### Instead of micro-interactions everywhere
→ Pick ONE moment to delight. Make it count. Everything else should be invisible.

---

## The Meta-Rule

**If you've seen it in 10 other AI-generated sites, don't use it.**

Distinctive design requires going against the distribution, not with it.
```

**Step 2: Verify file exists**

Run: `grep -c "\[ \]" plugins/frontend-design/frameworks/anti-patterns.md`

Expected: Should be 15+ (checklist items)

**Step 3: Commit**

```bash
git add plugins/frontend-design/frameworks/anti-patterns.md
git commit -m "feat(frontend-design): add anti-patterns framework"
```

---

## Task 14: Create README

**Files:**
- Create: `plugins/frontend-design/README.md`

**Step 1: Write README.md**

```markdown
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
```

**Step 2: Verify file exists**

Run: `head -30 plugins/frontend-design/README.md`

Expected: Should show "# Frontend Design" header and description

**Step 3: Commit**

```bash
git add plugins/frontend-design/README.md
git commit -m "feat(frontend-design): add README"
```

---

## Task 15: Create CHANGELOG

**Files:**
- Create: `plugins/frontend-design/CHANGELOG.md`

**Step 1: Write CHANGELOG.md**

```markdown
# Changelog

All notable changes to the frontend-design plugin.

## [1.0.0] - 2026-01-14

### Added

- Initial release
- `creating-canvas-animations` skill for HTML5 Canvas 2D animations
  - Primitives reference (lines, shapes, text, particles, grids, noise)
  - Composition reference (layering, color, density, choreography)
  - Easing functions library
  - Performance patterns (DPI, visibility, resize, cleanup)
  - Worked examples (Interface Craft style)
- Shared design system frameworks
  - Typography (font selection, pairing, scale)
  - Color (palette generation, CSS variables, dark mode)
  - Motion (timing, easing, staggered reveals)
  - Anti-patterns ("AI slop" avoidance checklist)
- TypeScript ES module output by default
- Standalone HTML demo output option
```

**Step 2: Verify file exists**

Run: `cat plugins/frontend-design/CHANGELOG.md`

Expected: Should show changelog with [1.0.0] entry

**Step 3: Commit**

```bash
git add plugins/frontend-design/CHANGELOG.md
git commit -m "feat(frontend-design): add CHANGELOG"
```

---

## Task 16: Register in Marketplace

**Files:**
- Modify: `.claude-plugin/marketplace.json`

**Step 1: Read current marketplace.json**

Run: `cat .claude-plugin/marketplace.json`

**Step 2: Add frontend-design entry to plugins array**

Add this entry to the `plugins` array:

```json
{
  "name": "frontend-design",
  "source": "./plugins/frontend-design",
  "description": "Production-grade frontend interfaces with built-in design sensibility. Canvas animations, typography, color systems.",
  "version": "1.0.0",
  "category": "frontend",
  "tags": ["frontend", "design", "canvas", "animation", "ui", "typography", "motion"]
}
```

**Step 3: Verify JSON is valid**

Run: `cat .claude-plugin/marketplace.json | python3 -m json.tool > /dev/null && echo "Valid JSON"`

Expected: `Valid JSON`

**Step 4: Commit**

```bash
git add .claude-plugin/marketplace.json
git commit -m "feat(marketplace): register frontend-design plugin"
```

---

## Task 17: Final Verification

**Step 1: Verify directory structure**

Run: `find plugins/frontend-design -type f | sort`

Expected output:
```
plugins/frontend-design/.claude-plugin/plugin.json
plugins/frontend-design/.claude-plugin/site.json
plugins/frontend-design/CHANGELOG.md
plugins/frontend-design/README.md
plugins/frontend-design/frameworks/anti-patterns.md
plugins/frontend-design/frameworks/color.md
plugins/frontend-design/frameworks/motion.md
plugins/frontend-design/frameworks/typography.md
plugins/frontend-design/skills/creating-canvas-animations/SKILL.md
plugins/frontend-design/skills/creating-canvas-animations/reference/composition.md
plugins/frontend-design/skills/creating-canvas-animations/reference/easing.md
plugins/frontend-design/skills/creating-canvas-animations/reference/examples.md
plugins/frontend-design/skills/creating-canvas-animations/reference/performance.md
plugins/frontend-design/skills/creating-canvas-animations/reference/primitives.md
```

**Step 2: Verify version consistency**

Run: `grep -h '"version"' plugins/frontend-design/.claude-plugin/plugin.json .claude-plugin/marketplace.json | grep "1.0.0"`

Expected: Should show version "1.0.0" in both files

**Step 3: Count total lines written**

Run: `find plugins/frontend-design -name "*.md" -o -name "*.json" | xargs wc -l | tail -1`

Expected: Should be ~2000+ lines total

---

## Summary

| Task | Files | Description |
|------|-------|-------------|
| 1 | directories | Create plugin structure |
| 2 | plugin.json | Plugin metadata |
| 3 | site.json | Marketplace display |
| 4 | SKILL.md | Canvas animations skill |
| 5 | primitives.md | Canvas building blocks |
| 6 | composition.md | Combining primitives |
| 7 | easing.md | Easing functions |
| 8 | performance.md | Optimization patterns |
| 9 | examples.md | Worked examples |
| 10 | typography.md | Font framework |
| 11 | color.md | Color framework |
| 12 | motion.md | Motion framework |
| 13 | anti-patterns.md | AI slop checklist |
| 14 | README.md | Plugin documentation |
| 15 | CHANGELOG.md | Version history |
| 16 | marketplace.json | Register plugin |
| 17 | — | Final verification |

**Total: 17 tasks, ~15 files, ~2000 lines**
