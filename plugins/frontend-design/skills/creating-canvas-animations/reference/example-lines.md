# Example: Diagonal Line Pattern

**Inspiration:** "Working Knowledge" card — orange diagonal stripes

---

## Analysis

- Parallel lines at ~45 degree angle
- Single color (orange) with subtle opacity
- Optional: slow drift animation
- Dense enough to create texture, sparse enough to read text over

## Implementation

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
