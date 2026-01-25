# Spring Physics Reference

Deep dive into physics-based animation for natural, premium motion.

---

## Why Springs?

Springs feel natural because they model how real objects behave:
- Objects have **mass** (weight)
- Springs have **stiffness** (tension)
- Movement has **friction** (damping)

This creates motion that:
- Responds to velocity (interruption feels natural)
- Overshoots and settles (bouncy or smooth)
- Never feels abrupt or mechanical

**When to use springs vs. duration-based:**
| Springs | Duration-based |
|---------|----------------|
| Interactive elements | Page transitions |
| Gesture responses | Progress animations |
| State changes | Timed sequences |
| Anything that can be interrupted | One-shot effects |

---

## Spring Parameters Explained

### Stiffness (tension)
How quickly the spring pulls toward the target.

| Value | Feel | Use Case |
|-------|------|----------|
| 100-150 | Gentle, floaty | Page transitions, modals |
| 200-300 | Natural, balanced | Cards, panels |
| 400-500 | Snappy, responsive | Buttons, toggles |
| 600+ | Very quick | Micro-interactions |

### Damping (friction)
How quickly oscillation settles.

| Value | Feel | Use Case |
|-------|------|----------|
| 5-10 | Very bouncy | Playful UI, games |
| 15-20 | Some bounce | Success states, emphasis |
| 25-30 | Smooth, slight overshoot | Most UI |
| 35+ | No bounce | Professional, subtle |

### Mass
Weight of the animated object.

| Value | Feel | Use Case |
|-------|------|----------|
| 0.5 | Light, nimble | Icons, small elements |
| 1.0 | Default, balanced | Most elements |
| 2.0+ | Heavy, sluggish | Dramatic, intentional |

---

## Framer Motion Springs

### Basic Spring

```jsx
<motion.div
  animate={{ x: 100 }}
  transition={{ type: "spring", stiffness: 300, damping: 25 }}
/>
```

### Named Presets

```javascript
// Create reusable spring configs
const springs = {
  // Micro-interactions
  button: { type: "spring", stiffness: 400, damping: 30 },
  
  // Standard UI
  default: { type: "spring", stiffness: 300, damping: 25 },
  
  // Modals, overlays
  modal: { type: "spring", stiffness: 200, damping: 25 },
  
  // Celebration, success
  bounce: { type: "spring", stiffness: 500, damping: 15 },
  
  // Gentle reveals
  gentle: { type: "spring", stiffness: 120, damping: 14 },
  
  // Very snappy
  snappy: { type: "spring", stiffness: 600, damping: 35 },
};

// Usage
<motion.div transition={springs.button} />
```

### Duration-Based Springs (Framer Motion 10+)

When you need a specific duration but want spring feel:

```jsx
<motion.div
  animate={{ x: 100 }}
  transition={{ 
    type: "spring",
    duration: 0.5,  // Approximate duration
    bounce: 0.25    // 0 = no bounce, 1 = very bouncy
  }}
/>
```

### useSpring Hook

For values that need to animate smoothly:

```jsx
import { motion, useSpring, useMotionValue } from "framer-motion";

function MagneticButton() {
  const x = useMotionValue(0);
  const y = useMotionValue(0);
  
  const springX = useSpring(x, { stiffness: 150, damping: 15 });
  const springY = useSpring(y, { stiffness: 150, damping: 15 });
  
  const handleMouseMove = (e) => {
    const rect = e.target.getBoundingClientRect();
    x.set(e.clientX - rect.left - rect.width / 2);
    y.set(e.clientY - rect.top - rect.height / 2);
  };
  
  const handleMouseLeave = () => {
    x.set(0);
    y.set(0);
  };
  
  return (
    <motion.button
      style={{ x: springX, y: springY }}
      onMouseMove={handleMouseMove}
      onMouseLeave={handleMouseLeave}
    >
      Hover me
    </motion.button>
  );
}
```

---

## React Spring

### Basic useSpring

```jsx
import { useSpring, animated } from "@react-spring/web";

function AnimatedBox() {
  const [springs, api] = useSpring(() => ({
    from: { x: 0, opacity: 0 },
    to: { x: 100, opacity: 1 },
    config: { tension: 300, friction: 20 }
  }));
  
  return <animated.div style={springs} />;
}
```

### Config Presets

```javascript
import { config } from "@react-spring/web";

// Built-in configs
config.default    // { tension: 170, friction: 26 }
config.gentle     // { tension: 120, friction: 14 }
config.wobbly     // { tension: 180, friction: 12 }
config.stiff      // { tension: 210, friction: 20 }
config.slow       // { tension: 280, friction: 60 }
config.molasses   // { tension: 280, friction: 120 }
```

### Custom Configs

```javascript
const customConfigs = {
  button: { tension: 400, friction: 30 },
  card: { tension: 280, friction: 25 },
  modal: { tension: 200, friction: 22 },
  bounce: { tension: 500, friction: 15, clamp: false },
  snappy: { tension: 500, friction: 35, clamp: true },
};
```

### useTransition for Lists

```jsx
import { useTransition, animated } from "@react-spring/web";

function AnimatedList({ items }) {
  const transitions = useTransition(items, {
    from: { opacity: 0, transform: "translateY(20px)" },
    enter: { opacity: 1, transform: "translateY(0)" },
    leave: { opacity: 0, transform: "translateY(-20px)" },
    trail: 80, // Stagger delay
    config: { tension: 300, friction: 25 }
  });
  
  return transitions((style, item) => (
    <animated.div style={style}>{item.content}</animated.div>
  ));
}
```

### useTrail for Staggered Springs

```jsx
import { useTrail, animated } from "@react-spring/web";

function StaggeredItems({ items }) {
  const trail = useTrail(items.length, {
    from: { opacity: 0, y: 30 },
    to: { opacity: 1, y: 0 },
    config: { tension: 300, friction: 25 }
  });
  
  return trail.map((style, index) => (
    <animated.div key={items[index].id} style={style}>
      {items[index].content}
    </animated.div>
  ));
}
```

### Gesture Integration

```jsx
import { useSpring, animated } from "@react-spring/web";
import { useDrag } from "@use-gesture/react";

function DraggableCard() {
  const [{ x, y }, api] = useSpring(() => ({ x: 0, y: 0 }));
  
  const bind = useDrag(({ active, movement: [mx, my] }) => {
    api.start({ 
      x: active ? mx : 0, 
      y: active ? my : 0,
      config: active 
        ? { tension: 800, friction: 35 }  // Tight while dragging
        : { tension: 200, friction: 20 }  // Bouncy return
    });
  });
  
  return (
    <animated.div {...bind()} style={{ x, y }}>
      Drag me
    </animated.div>
  );
}
```

---

## Real-World Spring Recipes

### Premium Button Press

```jsx
function PremiumButton({ children }) {
  return (
    <motion.button
      whileHover={{ 
        scale: 1.02,
        y: -2,
        transition: { type: "spring", stiffness: 400, damping: 17 }
      }}
      whileTap={{ 
        scale: 0.98,
        transition: { type: "spring", stiffness: 600, damping: 20 }
      }}
    >
      {children}
    </motion.button>
  );
}
```

### Card Hover with Depth

```jsx
function HoverCard({ children }) {
  return (
    <motion.div
      whileHover={{ 
        scale: 1.02,
        y: -4,
        boxShadow: "0 20px 40px rgba(0,0,0,0.15)",
        transition: { type: "spring", stiffness: 300, damping: 20 }
      }}
      initial={{ 
        boxShadow: "0 4px 12px rgba(0,0,0,0.1)" 
      }}
    >
      {children}
    </motion.div>
  );
}
```

### Toggle Switch

```jsx
function Toggle({ isOn, onToggle }) {
  return (
    <button 
      onClick={onToggle}
      className="w-14 h-8 rounded-full bg-gray-200 data-[on=true]:bg-blue-500"
      data-on={isOn}
    >
      <motion.div
        className="w-6 h-6 rounded-full bg-white shadow"
        animate={{ x: isOn ? 24 : 2 }}
        transition={{ 
          type: "spring", 
          stiffness: 500, 
          damping: 30 
        }}
      />
    </button>
  );
}
```

### Success Checkmark

```jsx
function SuccessCheck() {
  return (
    <motion.svg viewBox="0 0 24 24" className="w-8 h-8">
      <motion.circle
        cx="12"
        cy="12"
        r="10"
        fill="none"
        stroke="currentColor"
        strokeWidth="2"
        initial={{ pathLength: 0 }}
        animate={{ pathLength: 1 }}
        transition={{ 
          type: "spring",
          stiffness: 100,
          damping: 15
        }}
      />
      <motion.path
        d="M8 12l3 3 5-6"
        fill="none"
        stroke="currentColor"
        strokeWidth="2"
        strokeLinecap="round"
        strokeLinejoin="round"
        initial={{ pathLength: 0 }}
        animate={{ pathLength: 1 }}
        transition={{ 
          type: "spring",
          stiffness: 200,
          damping: 20,
          delay: 0.2
        }}
      />
    </motion.svg>
  );
}
```

### Error Shake

```jsx
function ShakeOnError({ hasError, children }) {
  return (
    <motion.div
      animate={hasError ? {
        x: [0, -8, 8, -6, 6, -4, 4, 0],
        transition: { duration: 0.4 }
      } : { x: 0 }}
    >
      {children}
    </motion.div>
  );
}
```

---

## Performance Considerations

### Interrupt Handling
Springs naturally handle interruption—if user triggers new animation mid-motion, the spring incorporates existing velocity:

```jsx
// This "just works" with springs
<motion.div
  animate={{ x: isOpen ? 100 : 0 }}
  transition={{ type: "spring", stiffness: 300, damping: 25 }}
/>
// Rapidly toggling isOpen creates smooth, natural motion
```

### When NOT to Use Springs

- **Progress indicators**: Use linear for actual progress
- **Loading spinners**: Constant rotation should be linear
- **Precise timing**: When sync with audio/video matters
- **Very long animations**: Springs work best < 1s

### Clamp Option

Prevent overshoot when needed:

```jsx
// Framer Motion
transition={{ type: "spring", stiffness: 300, damping: 25, clamp: true }}

// React Spring
config: { tension: 300, friction: 25, clamp: true }
```

---

## Debugging Springs

### Visualize Parameters

```jsx
function SpringDebugger() {
  const [config, setConfig] = useState({ stiffness: 300, damping: 25 });
  const [isActive, setIsActive] = useState(false);
  
  return (
    <div>
      <input 
        type="range" 
        min="100" 
        max="600"
        value={config.stiffness}
        onChange={(e) => setConfig(c => ({ ...c, stiffness: +e.target.value }))}
      />
      <label>Stiffness: {config.stiffness}</label>
      
      <input 
        type="range" 
        min="5" 
        max="50"
        value={config.damping}
        onChange={(e) => setConfig(c => ({ ...c, damping: +e.target.value }))}
      />
      <label>Damping: {config.damping}</label>
      
      <motion.div
        animate={{ x: isActive ? 200 : 0 }}
        transition={{ type: "spring", ...config }}
        onClick={() => setIsActive(!isActive)}
        className="w-16 h-16 bg-blue-500 rounded cursor-pointer"
      />
    </div>
  );
}
```

### Common Issues

**Too bouncy**: Increase damping (25 → 35)
**Too slow**: Increase stiffness (300 → 500)
**Too stiff**: Decrease both slightly
**Feels "floaty"**: Increase stiffness, keep damping moderate
