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
