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
