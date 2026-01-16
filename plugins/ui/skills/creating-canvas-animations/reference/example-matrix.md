# Example: Matrix/Code Rain

**Inspiration:** "Building Interface Kit" card — green character rain

---

## Analysis

- Vertical columns of characters
- Characters fade as they fall (trail effect)
- Monospace font (JetBrains Mono, Fira Code)
- Continuous loop, no visible reset

## Implementation

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
