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
