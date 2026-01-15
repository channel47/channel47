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
