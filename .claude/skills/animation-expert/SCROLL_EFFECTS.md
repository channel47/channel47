# Scroll Effects Reference

Patterns for scroll-driven animations that feel premium.

---

## Scroll Effect Philosophy

**Rule**: Scroll effects should enhance content, not compete with it.

| Good Scroll Effects | Bad Scroll Effects |
|---------------------|-------------------|
| Reveal content as it enters | Force users to scroll specific amounts |
| Provide context/progress | Hijack scroll behavior |
| Add subtle parallax depth | Make users dizzy |
| Reward exploration | Block navigation |

---

## CSS-Only Scroll Effects

### Scroll-Driven Animations (Native CSS)

```css
/* Modern browsers - scroll-driven animations */
@keyframes reveal {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}

.reveal-on-scroll {
  animation: reveal linear both;
  animation-timeline: view();
  animation-range: entry 0% entry 40%;
}

/* Progress bar based on scroll */
.progress-bar {
  transform-origin: left;
  animation: grow linear both;
  animation-timeline: scroll();
}

@keyframes grow {
  from { transform: scaleX(0); }
  to { transform: scaleX(1); }
}
```

### Scroll Snap

```css
.scroll-container {
  overflow-y: scroll;
  scroll-snap-type: y mandatory;
  scroll-behavior: smooth;
}

.snap-section {
  scroll-snap-align: start;
  scroll-snap-stop: always; /* Prevents skipping */
  min-height: 100vh;
}
```

### Sticky Elements

```css
.sticky-header {
  position: sticky;
  top: 0;
  z-index: 100;
  transition: background-color 0.3s ease, box-shadow 0.3s ease;
}

/* Add shadow when scrolled - use JS to toggle class */
.sticky-header.scrolled {
  background: rgba(255, 255, 255, 0.95);
  box-shadow: 0 2px 20px rgba(0, 0, 0, 0.1);
  backdrop-filter: blur(10px);
}
```

---

## Intersection Observer Patterns

### Basic Reveal

```javascript
const observerOptions = {
  threshold: 0.1,
  rootMargin: "0px 0px -10% 0px"
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add("visible");
      observer.unobserve(entry.target); // Animate once
    }
  });
}, observerOptions);

document.querySelectorAll(".reveal").forEach(el => observer.observe(el));
```

```css
.reveal {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.6s ease-out, transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
}

.reveal.visible {
  opacity: 1;
  transform: translateY(0);
}

/* Staggered children */
.reveal-stagger .child {
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 0.5s ease-out, transform 0.5s cubic-bezier(0.16, 1, 0.3, 1);
}

.reveal-stagger.visible .child:nth-child(1) { transition-delay: 0ms; }
.reveal-stagger.visible .child:nth-child(2) { transition-delay: 80ms; }
.reveal-stagger.visible .child:nth-child(3) { transition-delay: 160ms; }
/* ... */

.reveal-stagger.visible .child {
  opacity: 1;
  transform: translateY(0);
}
```

### Scroll Progress

```javascript
function updateScrollProgress() {
  const scrollTop = window.scrollY;
  const docHeight = document.documentElement.scrollHeight - window.innerHeight;
  const progress = scrollTop / docHeight;
  
  document.querySelector(".progress-bar").style.transform = `scaleX(${progress})`;
}

window.addEventListener("scroll", updateScrollProgress, { passive: true });
```

---

## Framer Motion Scroll Patterns

### useScroll + useTransform

```jsx
import { motion, useScroll, useTransform } from "framer-motion";

function ParallaxHero() {
  const { scrollYProgress } = useScroll();
  
  const y = useTransform(scrollYProgress, [0, 1], [0, -200]);
  const opacity = useTransform(scrollYProgress, [0, 0.3], [1, 0]);
  const scale = useTransform(scrollYProgress, [0, 0.3], [1, 0.9]);
  
  return (
    <motion.div 
      style={{ y, opacity, scale }}
      className="hero"
    >
      {/* Content */}
    </motion.div>
  );
}
```

### Element-Scoped Scroll

```jsx
function ScrollRevealSection() {
  const ref = useRef(null);
  const { scrollYProgress } = useScroll({
    target: ref,
    offset: ["start end", "end start"]
  });
  
  const opacity = useTransform(scrollYProgress, [0, 0.3, 0.7, 1], [0, 1, 1, 0]);
  const y = useTransform(scrollYProgress, [0, 0.3, 0.7, 1], [50, 0, 0, -50]);
  
  return (
    <motion.section ref={ref} style={{ opacity, y }}>
      {/* Content */}
    </motion.section>
  );
}
```

### whileInView

```jsx
<motion.div
  initial={{ opacity: 0, y: 50 }}
  whileInView={{ opacity: 1, y: 0 }}
  viewport={{ once: true, margin: "-100px" }}
  transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
>
  {/* Content */}
</motion.div>
```

### Staggered Grid Reveal

```jsx
const containerVariants = {
  hidden: { opacity: 0 },
  visible: {
    opacity: 1,
    transition: {
      staggerChildren: 0.08,
      delayChildren: 0.1
    }
  }
};

const itemVariants = {
  hidden: { opacity: 0, y: 30, scale: 0.95 },
  visible: { 
    opacity: 1, 
    y: 0, 
    scale: 1,
    transition: { 
      type: "spring", 
      stiffness: 300, 
      damping: 24 
    }
  }
};

function StaggeredGrid({ items }) {
  return (
    <motion.div
      variants={containerVariants}
      initial="hidden"
      whileInView="visible"
      viewport={{ once: true, amount: 0.1 }}
      className="grid"
    >
      {items.map(item => (
        <motion.div key={item.id} variants={itemVariants}>
          {/* Item content */}
        </motion.div>
      ))}
    </motion.div>
  );
}
```

---

## Premium Scroll Patterns

### Horizontal Scroll Section

```jsx
function HorizontalScroll({ children }) {
  const containerRef = useRef(null);
  const { scrollYProgress } = useScroll({ target: containerRef });
  
  const x = useTransform(scrollYProgress, [0, 1], ["0%", "-75%"]);
  
  return (
    <section ref={containerRef} className="h-[300vh] relative">
      <div className="sticky top-0 h-screen overflow-hidden">
        <motion.div style={{ x }} className="flex">
          {children}
        </motion.div>
      </div>
    </section>
  );
}
```

### Text Reveal Word-by-Word

```jsx
function AnimatedText({ text }) {
  const words = text.split(" ");
  const container = {
    hidden: { opacity: 0 },
    visible: {
      opacity: 1,
      transition: { staggerChildren: 0.05 }
    }
  };
  
  const child = {
    hidden: { opacity: 0, y: 20 },
    visible: { 
      opacity: 1, 
      y: 0,
      transition: { type: "spring", stiffness: 300, damping: 24 }
    }
  };
  
  return (
    <motion.p
      variants={container}
      initial="hidden"
      whileInView="visible"
      viewport={{ once: true }}
    >
      {words.map((word, i) => (
        <motion.span key={i} variants={child} className="inline-block mr-1">
          {word}
        </motion.span>
      ))}
    </motion.p>
  );
}
```

### Scroll-Linked Navbar

```jsx
function ScrollNavbar() {
  const { scrollY } = useScroll();
  const [isScrolled, setIsScrolled] = useState(false);
  
  useMotionValueEvent(scrollY, "change", (latest) => {
    setIsScrolled(latest > 50);
  });
  
  return (
    <motion.nav
      animate={{
        backgroundColor: isScrolled ? "rgba(255,255,255,0.95)" : "transparent",
        backdropFilter: isScrolled ? "blur(10px)" : "blur(0px)",
        boxShadow: isScrolled ? "0 2px 20px rgba(0,0,0,0.1)" : "none"
      }}
      transition={{ duration: 0.3 }}
      className="fixed top-0 w-full"
    >
      {/* Nav content */}
    </motion.nav>
  );
}
```

---

## Anti-Patterns to Avoid

### ❌ Scroll Hijacking
```javascript
// Don't prevent default scroll behavior
window.addEventListener("wheel", (e) => {
  e.preventDefault(); // BAD!
  // Custom scroll logic
});
```

### ❌ Excessive Parallax
```css
/* Too many parallax layers = visual chaos */
.layer-1 { transform: translateY(calc(var(--scroll) * 0.1)); }
.layer-2 { transform: translateY(calc(var(--scroll) * 0.3)); }
.layer-3 { transform: translateY(calc(var(--scroll) * 0.5)); }
/* Keep parallax subtle: 1-2 layers max */
```

### ❌ Mandatory Scroll Amounts
```javascript
// Don't force users to scroll exact amounts
ScrollTrigger.create({
  snap: 1 / sections.length, // Can feel jarring
});
```

### ✅ Better: Optional Snap
```javascript
ScrollTrigger.create({
  snap: {
    snapTo: 1 / sections.length,
    duration: { min: 0.2, max: 0.5 },
    delay: 0.1,
    ease: "power1.inOut"
  }
});
```

---

## Performance

### Passive Event Listeners
```javascript
// Always use passive for scroll events
window.addEventListener("scroll", handler, { passive: true });
```

### Throttle/Debounce
```javascript
// For expensive scroll calculations
let ticking = false;

window.addEventListener("scroll", () => {
  if (!ticking) {
    requestAnimationFrame(() => {
      updateOnScroll();
      ticking = false;
    });
    ticking = true;
  }
}, { passive: true });
```

### will-change for Heavy Animations
```css
.parallax-element {
  will-change: transform;
}

/* Remove after animation completes */
.parallax-element.done {
  will-change: auto;
}
```

### Respect Reduced Motion
```javascript
const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

if (prefersReducedMotion.matches) {
  // Skip scroll animations entirely
  document.querySelectorAll(".reveal").forEach(el => el.classList.add("visible"));
}
```
