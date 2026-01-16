# Example: Grid/Mosaic Tiles

**Inspiration:** "Practical Demonstration" card — tan/beige mosaic

---

## Analysis

- Rectangular cells in a grid
- Slight color variation within same hue family
- Some cells taller than others (varied heights)
- Subtle pulse or fade animation

## Implementation

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
