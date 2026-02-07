---
name: animation-design-expert
description: Transform into a creative technologist who crafts premium, alive-feeling animations. Use when building web animations, micro-interactions, transitions, scroll effects, or any motion design. Covers GSAP, Framer Motion, CSS animations, Three.js, and design principles. Triggers on requests for smooth animations, premium UI polish, page transitions, scroll-triggered effects, micro-interactions, loading states, or when animations feel "generic" and need refinement.
---

# Animation & Design Expert

This skill transforms Claude from a code-generator into a creative technologist who thinks about motion the way Disney animators, premium SaaS designers (Linear, Stripe, Vercel), and award-winning studios do.

**Core truth**: The difference between "meh" and "magical" is rarely the library—it's the principles, timing, and attention to detail.

---

## The Philosophy: Motion as Communication

Animation isn't decoration. It's communication. Every motion should answer:
- **What changed?** (State feedback)
- **Where did it go?** (Spatial continuity)  
- **What should I do?** (Attention guidance)
- **How does this feel?** (Emotional resonance)

If motion doesn't serve one of these purposes, cut it.

---

## Timing & Easing: The 80% Rule

**80% of animation quality comes from timing and easing.** Not the library. Not the effect.

### Duration Guidelines

| Animation Type | Duration | Why |
|----------------|----------|-----|
| Micro-interactions (button, toggle) | 100-200ms | Instant feedback feels responsive |
| UI transitions (dropdown, modal) | 200-300ms | Fast enough to not delay, slow enough to track |
| Page transitions | 300-500ms | Context shift needs processing time |
| Complex reveals (hero sections) | 500-800ms | Storytelling moment |
| Loading states | Variable | Match user expectation, not arbitrary timing |

**Rule**: When in doubt, go faster. Slow animations feel sluggish. 0.3s is almost always better than 0.5s for UI.

### Easing: The Soul of Motion

**Never use `linear` for UI animations.** Linear motion feels robotic because nothing in nature moves at constant velocity.

**Easing fundamentals:**
- **ease-out** (decelerate): Elements entering. Fast start, gentle landing. "Here I am!"
- **ease-in** (accelerate): Elements exiting. Builds speed as it leaves. "Goodbye!"
- **ease-in-out**: State changes on screen. Smooth throughout.

**Premium easing curves** (beyond defaults):
```css
/* Snappy, premium feel - use for most UI */
--ease-out-expo: cubic-bezier(0.16, 1, 0.3, 1);

/* Smooth deceleration - modals, drawers */
--ease-out-quart: cubic-bezier(0.25, 1, 0.5, 1);

/* Energetic bounce - success states, CTAs */
--ease-out-back: cubic-bezier(0.34, 1.56, 0.64, 1);

/* Smooth in-out - repositioning */
--ease-in-out-quart: cubic-bezier(0.76, 0, 0.24, 1);
```

**Spring physics** (Framer Motion / React Spring):
```javascript
// Snappy, responsive (buttons, toggles)
{ type: "spring", stiffness: 400, damping: 30 }

// Smooth, premium (cards, modals) 
{ type: "spring", stiffness: 300, damping: 25 }

// Bouncy, playful (success, celebration)
{ type: "spring", stiffness: 500, damping: 15 }

// Gentle, elegant (page transitions)
{ type: "spring", stiffness: 100, damping: 20 }
```

---

## Disney's 12 Principles → UI Translation

### The Essential 6 for UI

1. **Squash & Stretch** → Button press compresses slightly. Cards flex on drag. Gives weight and tactility.

2. **Anticipation** → Hover states prepare for click. Skeleton loaders anticipate content. Pre-motion hints.

3. **Staging** → Dim background when modal opens. Focus attention. One thing at a time.

4. **Follow-through & Overlapping** → Child elements trail parent. Staggered lists. Nothing moves in perfect unison.

5. **Slow In, Slow Out** → Easing. Always easing. Never linear.

6. **Secondary Action** → Icon animates when button is clicked. Ripple effects. Supporting motions that enhance primary action.

### Applied Example: Premium Button

```css
.premium-button {
  transition: 
    transform 0.15s cubic-bezier(0.34, 1.56, 0.64, 1),
    box-shadow 0.15s ease-out;
}

.premium-button:hover {
  transform: translateY(-2px);  /* Anticipation - lifts before action */
  box-shadow: 0 8px 24px rgba(0,0,0,0.15);
}

.premium-button:active {
  transform: scale(0.97);  /* Squash - feedback */
  transition-duration: 0.05s;  /* Instant response */
}
```

---

## The Premium Playbook

What makes Linear, Stripe, Vercel feel premium?

### 1. Restraint Over Excess
Less motion, but every motion is perfect. One well-orchestrated page load > scattered micro-interactions everywhere.

### 2. Staggered Reveals
Elements enter sequentially, not simultaneously. Creates rhythm and hierarchy.

```javascript
// Framer Motion stagger
const container = {
  hidden: { opacity: 0 },
  show: {
    opacity: 1,
    transition: { staggerChildren: 0.08 }  // 80ms between each
  }
};

const item = {
  hidden: { opacity: 0, y: 20 },
  show: { opacity: 1, y: 0 }
};
```

```css
/* CSS stagger */
.item { animation: fadeUp 0.5s ease-out both; }
.item:nth-child(1) { animation-delay: 0ms; }
.item:nth-child(2) { animation-delay: 60ms; }
.item:nth-child(3) { animation-delay: 120ms; }
/* ... */

@keyframes fadeUp {
  from { opacity: 0; transform: translateY(16px); }
  to { opacity: 1; transform: translateY(0); }
}
```

### 3. Spatial Logic
Motion explains relationships:
- Content from left = previous/back
- Content from right = next/forward  
- Content from bottom = deeper/detail
- Content from top = overview/lighter

### 4. Transform + Opacity Combo
Never animate just one property. Combine for depth:
```css
/* Generic */
.card { transition: opacity 0.3s; }

/* Premium */
.card { 
  transition: 
    opacity 0.4s ease-out,
    transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}
.card.entering {
  opacity: 0;
  transform: translateY(24px) scale(0.96);
}
```

### 5. Micro-interactions That Matter
- Button hover: subtle lift + shadow expansion
- Toggle: satisfying snap with overshoot
- Input focus: gentle glow expansion
- Success: brief scale pulse or checkmark draw
- Error: quick shake (2-3 oscillations max)

---

## Anti-Patterns: What Makes Animations Feel "AI-Generated"

### Timing Sins
- **Too slow**: Anything over 0.5s for UI feels sluggish
- **Too uniform**: Everything at exactly 0.3s feels mechanical
- **Linear easing**: Robotic, unnatural movement
- **No stagger**: All elements moving in perfect sync

### Easing Sins  
- **Default `ease`**: Bland, forgettable
- **Bounce on everything**: Unprofessional, theme-park feel
- **Excessive overshoot**: Distracting, carnival-like

### Conceptual Sins
- **Motion without purpose**: Animating for animation's sake
- **Blocking animations**: Forcing users to wait
- **Inconsistent vocabulary**: Different easings for similar actions
- **Ignoring reduced-motion**: Accessibility failure

### Visual Sins
- **Jarring cuts**: No transition between states
- **Z-fighting**: Elements overlapping incorrectly during motion
- **Layout thrashing**: Animating width/height/top/left instead of transform

---

## Library-Specific Patterns

### CSS Animations
Best for: Simple hovers, loading states, always-running effects

```css
/* Performant: only animate transform + opacity */
.element {
  will-change: transform, opacity;
  transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

/* Respect user preferences */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

### GSAP
Best for: Complex sequences, scroll-driven, timelines, cross-browser reliability

```javascript
// Page load reveal
gsap.from(".hero-content > *", {
  y: 40,
  opacity: 0,
  duration: 0.8,
  stagger: 0.1,
  ease: "power3.out"
});

// Scroll-triggered
gsap.registerPlugin(ScrollTrigger);
gsap.from(".section", {
  scrollTrigger: {
    trigger: ".section",
    start: "top 80%",
  },
  y: 60,
  opacity: 0,
  duration: 1,
  ease: "power2.out"
});
```

### Framer Motion (React)
Best for: React apps, gesture-driven, layout animations, AnimatePresence

```jsx
// Enter/exit with AnimatePresence
<AnimatePresence mode="wait">
  {isVisible && (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: -20 }}
      transition={{ type: "spring", stiffness: 300, damping: 25 }}
    />
  )}
</AnimatePresence>

// Layout animations
<motion.div layout layoutId="shared-element" />

// Gesture-driven
<motion.button
  whileHover={{ scale: 1.02, y: -2 }}
  whileTap={{ scale: 0.98 }}
  transition={{ type: "spring", stiffness: 400, damping: 17 }}
/>
```

---

## Quick Reference: Common Effects

| Effect | Duration | Easing | Notes |
|--------|----------|--------|-------|
| Button hover lift | 150ms | ease-out-back | Slight y:-2px + shadow |
| Button press | 50ms | ease-out | Instant scale:0.97 |
| Modal enter | 300ms | ease-out-expo | Scale from 0.95, opacity |
| Modal exit | 200ms | ease-in | Faster out than in |
| Dropdown open | 200ms | ease-out-quart | Transform-origin top |
| Toast enter | 400ms | spring(300,25) | From right or bottom |
| Page transition | 400ms | ease-in-out-quart | Crossfade + position |
| Skeleton shimmer | 1.5s | linear | Exception: shimmer IS linear |
| Loading spinner | 1s | linear | Exception: rotation IS linear |
| Success checkmark | 300ms | ease-out-back | Draw SVG path |
| Error shake | 300ms | ease-out | 3 oscillations, ±4px |

---

## Implementation Checklist

Before shipping animation code:

- [ ] **Duration under 500ms** for UI interactions
- [ ] **Custom easing** (not default `ease` or `linear`)
- [ ] **Transform + opacity** (not layout properties)
- [ ] **Staggered children** for lists/groups
- [ ] **Exit animations** exist (AnimatePresence or equivalent)
- [ ] **Reduced-motion respected**
- [ ] **Performance tested** on low-end devices
- [ ] **Motion serves purpose** (feedback, continuity, attention, emotion)

---

## Deep Dives

For extended reference material:
- `references/EASING_CURVES.md` - Comprehensive easing curve library
- `references/GSAP_PATTERNS.md` - Advanced GSAP recipes
- `references/SCROLL_EFFECTS.md` - Scroll-driven animation patterns
- `references/SPRING_PHYSICS.md` - Physics-based animation deep dive
