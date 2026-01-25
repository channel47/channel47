# Easing Curves Reference

Complete library of easing curves for premium animations.

---

## CSS Custom Property Setup

```css
:root {
  /* === STANDARD EASINGS === */
  --ease-linear: linear;
  
  /* Ease In (Accelerate) - Use for EXITS */
  --ease-in-sine: cubic-bezier(0.12, 0, 0.39, 0);
  --ease-in-quad: cubic-bezier(0.11, 0, 0.5, 0);
  --ease-in-cubic: cubic-bezier(0.32, 0, 0.67, 0);
  --ease-in-quart: cubic-bezier(0.5, 0, 0.75, 0);
  --ease-in-quint: cubic-bezier(0.64, 0, 0.78, 0);
  --ease-in-expo: cubic-bezier(0.7, 0, 0.84, 0);
  --ease-in-circ: cubic-bezier(0.55, 0, 1, 0.45);
  
  /* Ease Out (Decelerate) - Use for ENTRIES */
  --ease-out-sine: cubic-bezier(0.61, 1, 0.88, 1);
  --ease-out-quad: cubic-bezier(0.5, 1, 0.89, 1);
  --ease-out-cubic: cubic-bezier(0.33, 1, 0.68, 1);
  --ease-out-quart: cubic-bezier(0.25, 1, 0.5, 1);
  --ease-out-quint: cubic-bezier(0.22, 1, 0.36, 1);
  --ease-out-expo: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-out-circ: cubic-bezier(0, 0.55, 0.45, 1);
  
  /* Ease In-Out (Smooth) - Use for STATE CHANGES */
  --ease-in-out-sine: cubic-bezier(0.37, 0, 0.63, 1);
  --ease-in-out-quad: cubic-bezier(0.45, 0, 0.55, 1);
  --ease-in-out-cubic: cubic-bezier(0.65, 0, 0.35, 1);
  --ease-in-out-quart: cubic-bezier(0.76, 0, 0.24, 1);
  --ease-in-out-quint: cubic-bezier(0.83, 0, 0.17, 1);
  --ease-in-out-expo: cubic-bezier(0.87, 0, 0.13, 1);
  --ease-in-out-circ: cubic-bezier(0.85, 0, 0.15, 1);
  
  /* === SPECIAL EASINGS === */
  
  /* Back (Overshoot) - Use for EMPHASIS */
  --ease-in-back: cubic-bezier(0.36, 0, 0.66, -0.56);
  --ease-out-back: cubic-bezier(0.34, 1.56, 0.64, 1);
  --ease-in-out-back: cubic-bezier(0.68, -0.6, 0.32, 1.6);
  
  /* === PREMIUM PRESETS === */
  
  /* The "Linear App" feel - snappy, premium */
  --ease-premium: cubic-bezier(0.16, 1, 0.3, 1);
  
  /* iOS-like smooth */
  --ease-ios: cubic-bezier(0.25, 0.1, 0.25, 1);
  
  /* Material Design standard */
  --ease-material: cubic-bezier(0.4, 0, 0.2, 1);
  --ease-material-decel: cubic-bezier(0, 0, 0.2, 1);
  --ease-material-accel: cubic-bezier(0.4, 0, 1, 1);
  
  /* Vercel-style smooth */
  --ease-vercel: cubic-bezier(0.65, 0, 0.35, 1);
  
  /* === DURATION TOKENS === */
  --duration-instant: 50ms;
  --duration-fast: 150ms;
  --duration-normal: 250ms;
  --duration-slow: 400ms;
  --duration-slower: 600ms;
}
```

---

## When to Use Each Curve

### Entries (Elements Appearing)
Use **ease-out** curves. Element arrives quickly, settles gently.

| Curve | Feel | Best For |
|-------|------|----------|
| ease-out-quad | Gentle, natural | Default for most UI |
| ease-out-cubic | Smooth, polished | Cards, panels |
| ease-out-quart | Snappy, premium | Modals, dropdowns |
| ease-out-expo | Very snappy | Tooltips, fast reveals |
| ease-out-back | Bouncy overshoot | Success states, CTAs |

### Exits (Elements Leaving)
Use **ease-in** curves. Element accelerates as it leaves.

| Curve | Feel | Best For |
|-------|------|----------|
| ease-in-quad | Gentle departure | Default for most exits |
| ease-in-cubic | Decisive | Modals closing |
| ease-in-expo | Dramatic exit | Page transitions |

### State Changes (On-Screen Transforms)
Use **ease-in-out** curves. Smooth throughout.

| Curve | Feel | Best For |
|-------|------|----------|
| ease-in-out-quad | Natural | Toggle states |
| ease-in-out-cubic | Balanced | Position shifts |
| ease-in-out-quart | Premium, smooth | Page transitions |
| ease-in-out-expo | Dramatic | Full-screen transitions |

---

## Spring Configurations

### Framer Motion Springs

```javascript
const springs = {
  // Snappy - buttons, toggles, quick feedback
  snappy: { type: "spring", stiffness: 400, damping: 30 },
  
  // Responsive - cards, panels
  responsive: { type: "spring", stiffness: 300, damping: 25 },
  
  // Smooth - modals, overlays  
  smooth: { type: "spring", stiffness: 200, damping: 25 },
  
  // Gentle - page transitions
  gentle: { type: "spring", stiffness: 120, damping: 20 },
  
  // Bouncy - success, celebration
  bouncy: { type: "spring", stiffness: 500, damping: 15 },
  
  // Wobbly - playful, attention-grabbing
  wobbly: { type: "spring", stiffness: 350, damping: 10 },
};
```

### Understanding Spring Parameters

**Stiffness** (100-1000): How quickly the spring moves toward target
- Low (100-200): Slow, gentle, floaty
- Medium (200-400): Balanced, natural
- High (400-700): Snappy, responsive
- Very high (700+): Almost instant

**Damping** (5-40): How quickly oscillation settles
- Low (5-15): Bouncy, playful
- Medium (15-25): Natural, slight overshoot
- High (25-40): Smooth, no bounce

**Mass** (0.5-3): Weight of the object
- Low (0.5-1): Light, quick to respond
- Medium (1-2): Natural weight
- High (2-3): Heavy, sluggish

### React Spring Configurations

```javascript
const configs = {
  default: { tension: 170, friction: 26 },
  gentle: { tension: 120, friction: 14 },
  wobbly: { tension: 180, friction: 12 },
  stiff: { tension: 210, friction: 20 },
  slow: { tension: 280, friction: 60 },
  molasses: { tension: 280, friction: 120 },
};
```

---

## CSS Spring Approximations

Using the `linear()` timing function (modern browsers):

```css
/* Bouncy spring approximation */
--spring-bounce: linear(
  0, 0.004, 0.016, 0.035, 0.063, 0.098, 0.141, 0.191, 0.25,
  0.316, 0.391, 0.472, 0.562, 0.66, 0.765, 0.878, 1,
  1.089, 1.158, 1.207, 1.238, 1.252, 1.25, 1.234, 1.206,
  1.168, 1.123, 1.073, 1.021, 0.969, 0.92, 0.876, 0.838,
  0.808, 0.787, 0.775, 0.773, 0.78, 0.795, 0.818, 0.848,
  0.884, 0.925, 0.969, 1.015, 1.061, 1.105, 1.146, 1.182,
  1.21, 1.23, 1.24, 1.24, 1.231, 1.214, 1.191, 1.162,
  1.129, 1.093, 1.057, 1.021, 0.987, 0.956, 0.929, 0.907,
  0.891, 0.881, 0.877, 0.879, 0.886, 0.898, 0.914, 0.933,
  0.955, 0.979, 1.002, 1.026, 1.048, 1.068, 1.084, 1.096,
  1.104, 1.107, 1.106, 1.101, 1.093, 1.082, 1.069, 1.054,
  1.038, 1.022, 1.006, 0.991, 0.978, 0.967, 0.958, 0.952,
  0.949, 0.949, 0.951, 0.956, 0.963, 0.972, 0.982, 0.993, 1
);

/* Smooth spring (no bounce) */
--spring-smooth: linear(
  0, 0.009, 0.035, 0.078, 0.136, 0.208, 0.291, 0.385, 0.486,
  0.592, 0.701, 0.809, 0.913, 1.011, 1.099, 1.176, 1.24,
  1.289, 1.322, 1.341, 1.345, 1.337, 1.318, 1.29, 1.255,
  1.214, 1.171, 1.127, 1.083, 1.042, 1.004, 0.971, 0.943,
  0.921, 0.905, 0.895, 0.89, 0.891, 0.897, 0.906, 0.919,
  0.935, 0.953, 0.972, 0.991, 1.009, 1.026, 1.041, 1.053,
  1.062, 1.068, 1.07, 1.069, 1.065, 1.058, 1.049, 1.039,
  1.027, 1.015, 1.003, 0.991, 0.98, 0.971, 0.964, 0.959,
  0.956, 0.955, 0.957, 0.96, 0.965, 0.972, 0.979, 0.988,
  0.996, 1.004, 1.012, 1.019, 1.024, 1.028, 1.031, 1.032,
  1.032, 1.03, 1.027, 1.023, 1.018, 1.012, 1.006, 1
);
```

---

## Common Mistakes

### ❌ Wrong: Linear motion for UI
```css
.button { transition: transform 0.3s linear; }
```

### ✅ Right: Appropriate easing
```css
.button { transition: transform 0.2s var(--ease-out-quart); }
```

### ❌ Wrong: Same easing for enter and exit
```css
.modal {
  transition: opacity 0.3s ease-in-out;
}
```

### ✅ Right: Different easings for different directions
```javascript
// Framer Motion
<motion.div
  initial={{ opacity: 0, y: 20 }}
  animate={{ opacity: 1, y: 0 }}
  exit={{ opacity: 0, y: -10 }}
  transition={{
    enter: { ease: [0.16, 1, 0.3, 1] },  // ease-out-expo
    exit: { ease: [0.7, 0, 0.84, 0] }    // ease-in-expo
  }}
/>
```

### ❌ Wrong: Too much bounce everywhere
```css
.everything { transition: all 0.5s cubic-bezier(0.68, -0.6, 0.32, 1.6); }
```

### ✅ Right: Reserve bounce for emphasis
```css
.regular-element { transition: transform 0.25s var(--ease-out-quart); }
.success-state { transition: transform 0.3s var(--ease-out-back); }
```
