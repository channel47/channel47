# GSAP Patterns Reference

Advanced GSAP recipes for premium animations.

---

## Setup

```html
<!-- CDN (Free, all plugins now included) -->
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14/dist/gsap.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14/dist/ScrollTrigger.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14/dist/SplitText.min.js"></script>

<!-- npm -->
npm install gsap
```

```javascript
// ES Module imports
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { SplitText } from "gsap/SplitText";

gsap.registerPlugin(ScrollTrigger, SplitText);
```

---

## Core Patterns

### Staggered Page Load Reveal

```javascript
// Hero section reveal
gsap.from(".hero-content > *", {
  y: 40,
  opacity: 0,
  duration: 0.8,
  stagger: 0.1,
  ease: "power3.out",
  delay: 0.2
});

// Navigation items
gsap.from(".nav-item", {
  y: -20,
  opacity: 0,
  duration: 0.5,
  stagger: 0.05,
  ease: "power2.out"
});
```

### Text Split & Animate

```javascript
// Split text into characters
const split = new SplitText(".headline", { 
  type: "chars,words",
  charsClass: "char",
  wordsClass: "word"
});

// Animate characters with stagger
gsap.from(split.chars, {
  y: 50,
  opacity: 0,
  duration: 0.6,
  stagger: 0.02,
  ease: "power3.out"
});

// Cleanup on unmount
// split.revert();
```

### Scroll-Triggered Reveals

```javascript
// Batch reveal for multiple sections
gsap.utils.toArray(".reveal-section").forEach((section) => {
  gsap.from(section, {
    scrollTrigger: {
      trigger: section,
      start: "top 85%",
      toggleActions: "play none none reverse"
    },
    y: 60,
    opacity: 0,
    duration: 0.8,
    ease: "power2.out"
  });
});

// Staggered cards on scroll
ScrollTrigger.batch(".card", {
  onEnter: (elements) => {
    gsap.from(elements, {
      y: 40,
      opacity: 0,
      duration: 0.6,
      stagger: 0.1,
      ease: "power2.out"
    });
  },
  start: "top 90%"
});
```

### Pinned Scroll Sections

```javascript
// Pin section while scrolling through content
gsap.to(".horizontal-content", {
  x: () => -(document.querySelector(".horizontal-content").scrollWidth - window.innerWidth),
  ease: "none",
  scrollTrigger: {
    trigger: ".horizontal-wrapper",
    pin: true,
    scrub: 1,
    end: () => "+=" + document.querySelector(".horizontal-content").scrollWidth
  }
});
```

---

## Premium Effects

### Magnetic Cursor Effect

```javascript
const magneticElements = document.querySelectorAll("[data-magnetic]");

magneticElements.forEach((el) => {
  el.addEventListener("mousemove", (e) => {
    const rect = el.getBoundingClientRect();
    const x = e.clientX - rect.left - rect.width / 2;
    const y = e.clientY - rect.top - rect.height / 2;
    
    gsap.to(el, {
      x: x * 0.3,
      y: y * 0.3,
      duration: 0.4,
      ease: "power2.out"
    });
  });
  
  el.addEventListener("mouseleave", () => {
    gsap.to(el, {
      x: 0,
      y: 0,
      duration: 0.7,
      ease: "elastic.out(1, 0.3)"
    });
  });
});
```

### Smooth Parallax

```javascript
gsap.utils.toArray("[data-parallax]").forEach((el) => {
  const speed = el.dataset.parallax || 0.5;
  
  gsap.to(el, {
    y: () => (1 - speed) * ScrollTrigger.maxScroll(window) * 0.1,
    ease: "none",
    scrollTrigger: {
      trigger: el.parentElement,
      start: "top bottom",
      end: "bottom top",
      scrub: true
    }
  });
});
```

### Counter Animation

```javascript
function animateCounter(element, target, duration = 2) {
  const obj = { value: 0 };
  
  gsap.to(obj, {
    value: target,
    duration,
    ease: "power1.out",
    onUpdate: () => {
      element.textContent = Math.round(obj.value).toLocaleString();
    },
    scrollTrigger: {
      trigger: element,
      start: "top 80%"
    }
  });
}

animateCounter(document.querySelector(".stat-number"), 10000);
```

### Draw SVG Path

```javascript
const path = document.querySelector(".svg-path");
const length = path.getTotalLength();

// Set up initial state
gsap.set(path, {
  strokeDasharray: length,
  strokeDashoffset: length
});

// Animate draw
gsap.to(path, {
  strokeDashoffset: 0,
  duration: 1.5,
  ease: "power2.inOut",
  scrollTrigger: {
    trigger: path,
    start: "top 70%"
  }
});
```

---

## Timeline Patterns

### Orchestrated Entrance

```javascript
const tl = gsap.timeline({
  defaults: { ease: "power3.out", duration: 0.8 }
});

tl.from(".logo", { y: -30, opacity: 0 })
  .from(".nav-items > *", { y: -20, opacity: 0, stagger: 0.05 }, "-=0.5")
  .from(".hero-title", { y: 50, opacity: 0 }, "-=0.4")
  .from(".hero-subtitle", { y: 30, opacity: 0 }, "-=0.5")
  .from(".hero-cta", { y: 20, opacity: 0, scale: 0.9 }, "-=0.4");
```

### Hover Timeline

```javascript
const cards = document.querySelectorAll(".interactive-card");

cards.forEach((card) => {
  const image = card.querySelector("img");
  const content = card.querySelector(".content");
  
  const tl = gsap.timeline({ paused: true });
  
  tl.to(image, { scale: 1.1, duration: 0.4, ease: "power2.out" })
    .to(content, { y: -10, duration: 0.3, ease: "power2.out" }, 0);
  
  card.addEventListener("mouseenter", () => tl.play());
  card.addEventListener("mouseleave", () => tl.reverse());
});
```

---

## ScrollTrigger Patterns

### Progress-Based Animation

```javascript
gsap.to(".progress-bar", {
  scaleX: 1,
  ease: "none",
  scrollTrigger: {
    trigger: "body",
    start: "top top",
    end: "bottom bottom",
    scrub: 0.3
  }
});
```

### Section Indicators

```javascript
const sections = gsap.utils.toArray(".section");
const indicators = gsap.utils.toArray(".indicator");

sections.forEach((section, i) => {
  ScrollTrigger.create({
    trigger: section,
    start: "top center",
    end: "bottom center",
    onEnter: () => setActiveIndicator(i),
    onEnterBack: () => setActiveIndicator(i)
  });
});

function setActiveIndicator(index) {
  indicators.forEach((ind, i) => {
    gsap.to(ind, {
      scale: i === index ? 1.2 : 1,
      opacity: i === index ? 1 : 0.5,
      duration: 0.3
    });
  });
}
```

### Snap Scrolling

```javascript
const sections = gsap.utils.toArray(".snap-section");

ScrollTrigger.create({
  snap: {
    snapTo: 1 / (sections.length - 1),
    duration: { min: 0.2, max: 0.6 },
    ease: "power1.inOut"
  }
});
```

---

## Performance Tips

### Use GSAP's set() for Initial States

```javascript
// ❌ CSS initial state then animate
// Can cause flash of unstyled content

// ✅ GSAP set() for initial state
gsap.set(".element", { opacity: 0, y: 30 });
gsap.to(".element", { opacity: 1, y: 0, duration: 0.6 });
```

### Batch ScrollTriggers

```javascript
// ❌ Individual ScrollTriggers per element
document.querySelectorAll(".item").forEach(item => {
  ScrollTrigger.create({ trigger: item, /* ... */ });
});

// ✅ Use ScrollTrigger.batch()
ScrollTrigger.batch(".item", {
  onEnter: batch => gsap.to(batch, { opacity: 1, y: 0, stagger: 0.1 }),
  start: "top 90%"
});
```

### Kill Animations on Cleanup

```javascript
// React useEffect cleanup
useEffect(() => {
  const ctx = gsap.context(() => {
    gsap.from(".element", { /* ... */ });
  }, containerRef);
  
  return () => ctx.revert();
}, []);
```

### Use will-change Sparingly

```javascript
// Add before animation
gsap.set(".heavy-element", { willChange: "transform" });

// Animation
gsap.to(".heavy-element", {
  x: 100,
  onComplete: () => {
    // Remove after animation
    gsap.set(".heavy-element", { willChange: "auto" });
  }
});
```

---

## Responsive Animations

### MatchMedia for Breakpoints

```javascript
const mm = gsap.matchMedia();

mm.add("(min-width: 768px)", () => {
  // Desktop animations
  gsap.to(".sidebar", {
    x: 0,
    scrollTrigger: { /* ... */ }
  });
});

mm.add("(max-width: 767px)", () => {
  // Mobile animations (or none)
  gsap.set(".sidebar", { x: 0 });
});
```

### Reduced Motion

```javascript
const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

if (prefersReducedMotion) {
  // Skip animations, set final state
  gsap.set(".animated-element", { opacity: 1, y: 0 });
} else {
  // Full animations
  gsap.from(".animated-element", { opacity: 0, y: 30 });
}
```

---

## Common Mistakes

### ❌ Animating Layout Properties

```javascript
// Causes layout thrashing
gsap.to(".box", { width: 200, height: 200 });
```

### ✅ Use Transforms

```javascript
// GPU-accelerated
gsap.to(".box", { scale: 2 });
```

### ❌ Overusing Scrub

```javascript
// Every animation scrubbed feels sluggish
scrollTrigger: { scrub: true }
```

### ✅ Strategic Scrub

```javascript
// Trigger animations, don't scrub everything
scrollTrigger: { 
  start: "top 80%",
  toggleActions: "play none none reverse"
}

// Only scrub for progress-type effects
scrollTrigger: { scrub: 0.5 } // For progress bars, parallax
```

### ❌ Too Many Overlapping Animations

```javascript
// Fighting for the same properties
gsap.to(".el", { x: 100 });
gsap.to(".el", { x: -100 }); // Conflict!
```

### ✅ Use Timelines or Overwrite

```javascript
gsap.to(".el", { x: 100, overwrite: true });
// Or use a timeline for sequencing
```
