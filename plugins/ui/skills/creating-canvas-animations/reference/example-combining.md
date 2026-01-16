# Example: Combining Techniques

Learn to combine primitives for more complex effects.

---

## Combination Patterns

The individual animation patterns can be combined for richer effects:

- **Particles over grid**: Background mosaic + foreground floating particles
- **Lines with noise**: Diagonal lines where positions are offset by noise
- **Wireframe with glow**: Draw wireframe twice — once blurred for glow, once sharp

## Key Principle

The primitives and composition principles let you create any combination.

Rather than seeking more complex templates, focus on:

1. **Layering** — Multiple effects drawn in sequence, back to front
2. **Shared timing** — Use the same `time` variable for coordinated motion
3. **Color harmony** — Effects share a palette from CSS custom properties
4. **Performance** — Each additional layer has a cost; test on target devices

## Example: Glow Effect

```typescript
function drawWithGlow(
  ctx: CanvasRenderingContext2D,
  drawFn: () => void,
  glowColor: string,
  glowRadius: number
) {
  // Draw glow layer (blurred)
  ctx.save();
  ctx.shadowColor = glowColor;
  ctx.shadowBlur = glowRadius;
  drawFn();
  ctx.restore();

  // Draw sharp layer on top
  drawFn();
}
```

## Example: Layered Composition

```typescript
function drawCompositeAnimation(
  ctx: CanvasRenderingContext2D,
  width: number,
  height: number,
  time: number
) {
  // Layer 1: Background grid
  drawMosaic(ctx, mosaicCells, time, 'fade');

  // Layer 2: Middle diagonal lines
  ctx.globalCompositeOperation = 'overlay';
  drawDiagonalLines(ctx, width, height, lineOptions, time);

  // Layer 3: Foreground particles
  ctx.globalCompositeOperation = 'source-over';
  drawParticles(ctx, particles, time);
}
```

See @reference/composition.md for more on layering and blend modes.
