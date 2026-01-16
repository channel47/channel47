# Easing Functions

A library of easing functions for canvas animations. All functions take `t` (progress 0-1) and return eased value (0-1).

---

## Core Set (Always Include)

These cover 90% of use cases.

```typescript
// Linear — constant speed, only for continuous rotation
const linear = (t: number): number => t;

// Quad — smooth, professional
const easeInQuad = (t: number): number => t * t;
const easeOutQuad = (t: number): number => t * (2 - t);
const easeInOutQuad = (t: number): number =>
  t < 0.5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2;

// Cubic — slightly more pronounced
const easeInCubic = (t: number): number => t * t * t;
const easeOutCubic = (t: number): number => 1 - Math.pow(1 - t, 3);
const easeInOutCubic = (t: number): number =>
  t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
```

---

## Expressive Set

For animations that need personality.

```typescript
// Back — overshoots then settles, playful
const easeOutBack = (t: number): number => {
  const c1 = 1.70158;
  const c3 = c1 + 1;
  return 1 + c3 * Math.pow(t - 1, 3) + c1 * Math.pow(t - 1, 2);
};

const easeInBack = (t: number): number => {
  const c1 = 1.70158;
  const c3 = c1 + 1;
  return c3 * t * t * t - c1 * t * t;
};

// Elastic — spring/bounce, energetic
const easeOutElastic = (t: number): number => {
  if (t === 0 || t === 1) return t;
  const c4 = (2 * Math.PI) / 3;
  return Math.pow(2, -10 * t) * Math.sin((t * 10 - 0.75) * c4) + 1;
};

const easeInElastic = (t: number): number => {
  if (t === 0 || t === 1) return t;
  const c4 = (2 * Math.PI) / 3;
  return -Math.pow(2, 10 * t - 10) * Math.sin((t * 10 - 10.75) * c4);
};

// Expo — dramatic deceleration, impactful
const easeOutExpo = (t: number): number =>
  t === 1 ? 1 : 1 - Math.pow(2, -10 * t);

const easeInExpo = (t: number): number =>
  t === 0 ? 0 : Math.pow(2, 10 * t - 10);

// Bounce — bouncing ball effect
const easeOutBounce = (t: number): number => {
  const n1 = 7.5625;
  const d1 = 2.75;
  if (t < 1 / d1) {
    return n1 * t * t;
  } else if (t < 2 / d1) {
    return n1 * (t -= 1.5 / d1) * t + 0.75;
  } else if (t < 2.5 / d1) {
    return n1 * (t -= 2.25 / d1) * t + 0.9375;
  } else {
    return n1 * (t -= 2.625 / d1) * t + 0.984375;
  }
};
```

---

## Usage Principle

Match easing to intent:

| Intent | Easing | Why |
|--------|--------|-----|
| Subtle, professional | Quad, Cubic | Smooth, doesn't draw attention |
| Playful, delightful | Back, Elastic | Overshoots create surprise |
| Dramatic, impactful | Expo | Fast start/end, lingering middle |
| Physical, realistic | Bounce | Mimics real-world physics |

---

## Application Pattern

```typescript
function animate(
  from: number,
  to: number,
  duration: number,
  easing: (t: number) => number,
  onUpdate: (value: number) => void,
  onComplete?: () => void
) {
  const startTime = Date.now();

  function tick() {
    const elapsed = Date.now() - startTime;
    const progress = Math.min(elapsed / duration, 1);
    const easedProgress = easing(progress);
    const value = from + (to - from) * easedProgress;

    onUpdate(value);

    if (progress < 1) {
      requestAnimationFrame(tick);
    } else if (onComplete) {
      onComplete();
    }
  }

  tick();
}

// Usage
animate(0, 100, 500, easeOutQuad, (x) => {
  element.x = x;
});
```

---

## Chaining Easings

For complex animations, chain multiple easings:

```typescript
function chainedEase(t: number): number {
  if (t < 0.5) {
    // First half: ease in
    return easeInQuad(t * 2) * 0.5;
  } else {
    // Second half: bounce out
    return 0.5 + easeOutBounce((t - 0.5) * 2) * 0.5;
  }
}
```
