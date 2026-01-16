# Example: Wireframe UI Mockup

**Inspiration:** "Interface Kit" card — black with white UI rectangles

---

## Analysis

- Rectangles representing UI panels
- Outline only (stroke, not fill)
- Arranged to suggest an interface layout
- Optional: sequential reveal animation

## Implementation

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
