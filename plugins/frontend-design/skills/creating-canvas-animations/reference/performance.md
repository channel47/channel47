# Performance Patterns

Production-grade performance optimizations for canvas animations.

---

## Standard Initialization Pattern

Most canvas animations should include these foundational elements. Adapt as needed for your specific use case:

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

**Key elements:**
- DPI scaling for retina displays
- Visibility API to pause when tab is hidden
- ResizeObserver for responsive sizing
- Cleanup function for proper teardown

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
