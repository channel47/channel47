# Animation Reference

## The Philosophy

Animation in editorial design should feel **inevitable** — like the only natural way for elements to appear. If someone notices your animation, it's probably too much.

**The "invisible animation" principle**: Good motion is felt, not seen. It reduces friction and guides attention rather than demanding it. Animation succeeds when it makes the interface feel more natural, not when it impresses.

---

## Core Easing Functions

### The Essential Three

```css
:root {
  /* Smooth deceleration - for entrances */
  --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
  
  /* Smooth acceleration and deceleration - for transitions */
  --ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);
  
  /* Smooth acceleration - for exits */
  --ease-in: cubic-bezier(0.7, 0, 0.84, 0);
}
```

### When to Use Each

- **ease-out**: Page load reveals, modals appearing, elements entering
- **ease-in-out**: State changes, position transitions, hover effects
- **ease-in**: Elements leaving, collapse animations (rare)

### Never Use

```css
/* These feel mechanical and cheap */
animation-timing-function: linear;
animation-timing-function: ease;  /* The CSS default is mediocre */
```

---

## Duration Scale

```css
:root {
  --duration-instant: 100ms;  /* Micro-interactions */
  --duration-fast: 150ms;     /* Hovers, small state changes */
  --duration-default: 250ms;  /* Most transitions */
  --duration-slow: 400ms;     /* Page reveals, large movements */
  --duration-slower: 600ms;   /* Dramatic entrances (use rarely) */
}
```

### Duration Rules

1. **Smaller movements = faster durations**
2. **Larger distances = slower durations**
3. **Users should never wait for animations**

---

## Page Load Reveals

The most impactful animation pattern. One well-orchestrated entrance creates more perception of quality than a hundred hover effects.

### The Staggered Reveal

```css
.reveal {
  opacity: 0;
  transform: translateY(24px);
}

.reveal.loaded {
  animation: reveal var(--duration-slow) var(--ease-out) forwards;
}

@keyframes reveal {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Stagger children */
.reveal:nth-child(1) { animation-delay: 0ms; }
.reveal:nth-child(2) { animation-delay: 60ms; }
.reveal:nth-child(3) { animation-delay: 120ms; }
.reveal:nth-child(4) { animation-delay: 180ms; }
.reveal:nth-child(5) { animation-delay: 240ms; }
```

### Implementation in Astro

```astro
---
// RevealOnLoad.astro
interface Props {
  delay?: number;
  class?: string;
}

const { delay = 0, class: className } = Astro.props;
---

<div 
  class:list={['reveal', className]}
  style={`animation-delay: ${delay}ms;`}
>
  <slot />
</div>

<script>
  // Trigger reveals after DOM is ready
  document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.reveal').forEach(el => {
      el.classList.add('loaded');
    });
  });
</script>

<style>
  .reveal {
    opacity: 0;
    transform: translateY(24px);
  }
  
  .reveal.loaded {
    animation: reveal 400ms cubic-bezier(0.16, 1, 0.3, 1) forwards;
  }
  
  @keyframes reveal {
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }
</style>
```

### Usage

```astro
<section>
  <RevealOnLoad delay={0}>
    <h1>Hero Headline</h1>
  </RevealOnLoad>
  
  <RevealOnLoad delay={60}>
    <p>Supporting text that enters after.</p>
  </RevealOnLoad>
  
  <RevealOnLoad delay={120}>
    <Button>Call to Action</Button>
  </RevealOnLoad>
</section>
```

---

## Scroll-Triggered Animation

Use sparingly. Most content should just... be there.

### When to Use

- Feature sections that tell a story
- Large images that benefit from context
- Interactive demonstrations

### When NOT to Use

- Every section on the page
- Text that needs to be read
- Navigation elements
- Forms

### Simple Scroll Reveal

```astro
---
// ScrollReveal.astro
interface Props {
  class?: string;
}

const { class: className } = Astro.props;
---

<div class:list={['scroll-reveal', className]}>
  <slot />
</div>

<script>
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.1, rootMargin: '0px 0px -50px 0px' }
  );

  document.querySelectorAll('.scroll-reveal').forEach(el => {
    observer.observe(el);
  });
</script>

<style>
  .scroll-reveal {
    opacity: 0;
    transform: translateY(20px);
    transition: 
      opacity 400ms cubic-bezier(0.16, 1, 0.3, 1),
      transform 400ms cubic-bezier(0.16, 1, 0.3, 1);
  }
  
  .scroll-reveal.visible {
    opacity: 1;
    transform: translateY(0);
  }
</style>
```

---

## Hover States

### Buttons

```css
.button {
  transition: 
    background-color var(--duration-fast) var(--ease-in-out),
    transform var(--duration-fast) var(--ease-out);
}

.button:hover {
  transform: translateY(-1px);
}

.button:active {
  transform: translateY(0);
}
```

### Links

```css
/* Underline animation */
.link {
  text-decoration: none;
  background-image: linear-gradient(currentColor, currentColor);
  background-size: 0% 1px;
  background-position: 0 100%;
  background-repeat: no-repeat;
  transition: background-size var(--duration-fast) var(--ease-out);
}

.link:hover {
  background-size: 100% 1px;
}
```

### Cards

```css
.card {
  transition: 
    box-shadow var(--duration-default) var(--ease-out),
    transform var(--duration-default) var(--ease-out);
}

.card:hover {
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);
  transform: translateY(-2px);
}
```

---

## Focus States

Accessibility requires visible focus states. Make them beautiful.

```css
:focus-visible {
  outline: none;
  box-shadow: 0 0 0 2px var(--surface-primary), 0 0 0 4px var(--accent);
}

/* Remove focus ring for mouse users */
:focus:not(:focus-visible) {
  outline: none;
  box-shadow: none;
}
```

---

## Animation Anti-Patterns

### 1. Parallax Everywhere

```css
/* DON'T */
.section {
  background-attachment: fixed;
  transform: translateY(calc(var(--scroll) * 0.5));
}
```

Parallax is almost never necessary. It's distracting and performs poorly.

### 2. Bouncy Easing

```css
/* DON'T */
transition-timing-function: cubic-bezier(0.68, -0.55, 0.265, 1.55);
```

Bounce effects feel playful but rarely fit editorial design.

### 3. Long Durations

```css
/* DON'T */
transition-duration: 800ms;
animation-duration: 1200ms;
```

If users notice the animation taking time, it's too slow.

### 4. Animation on Every Element

```astro
<!-- DON'T -->
<ScrollReveal><h2>Title</h2></ScrollReveal>
<ScrollReveal><p>Paragraph</p></ScrollReveal>
<ScrollReveal><p>Another paragraph</p></ScrollReveal>
<ScrollReveal><img /></ScrollReveal>
<ScrollReveal><p>More text</p></ScrollReveal>
```

This creates a distracting cascade. Animate sections, not elements.

### 5. Decorative Animation

```css
/* DON'T */
.logo {
  animation: float 3s ease-in-out infinite;
}

@keyframes float {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}
```

Looping animations are rarely appropriate for editorial sites.

---

## Performance Considerations

### Animate Only These Properties

```css
/* FAST - composited by GPU */
transform: translateX() translateY() scale() rotate();
opacity: 0-1;

/* SLOW - triggers layout/paint */
width, height, margin, padding, top, left, etc.
```

### Use will-change Sparingly

```css
/* Only add when needed */
.element-that-will-animate {
  will-change: transform, opacity;
}

/* Remove after animation completes if possible */
```

### Reduce Motion for Accessibility

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

---

## Quick Reference

### Page Load Sequence

1. **Navigation**: Instant (no animation)
2. **Hero headline**: First reveal (0ms delay)
3. **Hero subtext**: Second reveal (60ms delay)
4. **Hero CTA**: Third reveal (120ms delay)
5. **Hero image**: Fourth reveal (180ms delay) OR fade in parallel

### Standard Transitions

| Element | Property | Duration | Easing |
|---------|----------|----------|--------|
| Button hover | background | 150ms | ease-in-out |
| Card hover | shadow, transform | 250ms | ease-out |
| Link underline | background-size | 150ms | ease-out |
| Modal appear | opacity, transform | 400ms | ease-out |
| Tooltip | opacity | 150ms | ease-out |

### Stagger Timing

| Delay Gap | Feel |
|-----------|------|
| 40-60ms | Tight, coordinated |
| 80-100ms | Standard, readable |
| 150ms+ | Dramatic, cinematic |
