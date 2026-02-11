# Motion. ch47.

Animation patterns, entrance vocabulary, scroll effects, micro-interactions, and choreography. The core motion principles live in SKILL.md (Motion section). This file is the full reference.

---

## Core Principles

**Purposeful.** Every animation communicates something. An entrance says "this just arrived." A hover says "this is interactive." A scroll effect says "you're making progress." If the animation doesn't communicate, cut it.

**Quick.** Things arrive. They don't drift. Default duration is 200ms. Go shorter before going longer. A 100ms hover feels responsive. A 400ms entrance feels cinematic. A 700ms anything is rare and reserved for hero moments.

**Decisive.** No bounce. No elastic. No spring physics. No overshoot. Elements move from A to B with intent. The easing communicates confidence, not playfulness.

**Sparse.** Motion budget: 8-15 animated elements per page total. 2-4 visible simultaneously in any viewport. If everything moves, nothing moves. Count your animations. If you can't justify each one, cut.

**Composed.** Animations have roles. One lead (the thing you notice), supporting cast (things that follow), and atmosphere (things you feel but don't see). Clear hierarchy. No two animations competing for attention.

### Timing Reference

```
Instant    100ms    Hover states, micro-interactions, focus rings.
Quick      200ms    Reveals, state changes, content transitions. The default.
Measured   400ms    Section entrances, key reveals. Earns attention.
Cinematic  700ms    Hero sequence, page load. Once per page max.
```

### Easing Curves

```css
--ease-out:    cubic-bezier(0.16, 1, 0.3, 1);    /* Fast start, smooth land. Default. */
--ease-sharp:  cubic-bezier(0.33, 1, 0.68, 1);    /* Snappier. Interactive elements. */
--ease-linear: linear;                              /* Atmospheric only. Never for UI. */
```

---

## Entrance Vocabulary

The current site uses fade-up for everything. That's the safe default. These entrances expand the vocabulary so different content types enter differently, creating variety and information hierarchy through motion.

### Fade Up (Default)

Content blocks, body text, secondary elements. The workhorse. Use when nothing else fits.

```css
[data-entrance="fade-up"] {
  opacity: 0;
  transform: translateY(12px);
  transition: opacity 400ms var(--ease-out),
              transform 400ms var(--ease-out);
}

[data-entrance="fade-up"].is-visible {
  opacity: 1;
  transform: translateY(0);
}
```

### Clip Reveal

Headlines, heroes, rupture sections. `clip-path: inset()` expanding from center or edge. CSS-only. Creates a "broadcast coming online" effect. More dramatic than fade-up.

```css
[data-entrance="clip-reveal"] {
  clip-path: inset(0 50% 0 50%);
  transition: clip-path 600ms var(--ease-out);
}

[data-entrance="clip-reveal"].is-visible {
  clip-path: inset(0 0 0 0);
}

/* Variant: reveal from left edge */
[data-entrance="clip-reveal-left"] {
  clip-path: inset(0 100% 0 0);
  transition: clip-path 600ms var(--ease-out);
}

[data-entrance="clip-reveal-left"].is-visible {
  clip-path: inset(0 0 0 0);
}
```

### Line Wipe

Signal-colored line sweeps across, revealing content behind it. The "broadcast" metaphor made physical. For section dividers, accent moments, horizontal rules.

```css
[data-entrance="line-wipe"] {
  position: relative;
  opacity: 0;
}

[data-entrance="line-wipe"]::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  width: 0;
  height: 100%;
  background: var(--color-accent);
  z-index: 1;
  transition: width 400ms var(--ease-out);
}

[data-entrance="line-wipe"].is-visible {
  opacity: 1;
}

[data-entrance="line-wipe"].is-visible::before {
  width: 100%;
  animation: line-wipe-reveal 600ms var(--ease-out) forwards;
}

@keyframes line-wipe-reveal {
  0%   { width: 0; left: 0; }
  50%  { width: 100%; left: 0; }
  100% { width: 0; left: 100%; }
}
```

### Counter Tick

Numbers count up from 0 via `requestAnimationFrame`. For stats strips, proof bars, dashboard metrics. The mechanical feel of numbers incrementing reinforces "this is real data."

```js
function counterTick(element, target, duration = 800) {
  const start = performance.now();
  const isFloat = String(target).includes('.');
  const prefix = element.dataset.prefix || '';
  const suffix = element.dataset.suffix || '';

  function step(now) {
    const elapsed = now - start;
    const progress = Math.min(elapsed / duration, 1);
    // Ease out
    const eased = 1 - Math.pow(1 - progress, 3);
    const current = isFloat
      ? (eased * target).toFixed(1)
      : Math.floor(eased * target);
    element.textContent = prefix + current + suffix;
    if (progress < 1) requestAnimationFrame(step);
  }

  requestAnimationFrame(step);
}
```

Usage with IntersectionObserver:

```js
document.querySelectorAll('[data-counter]').forEach(el => {
  const target = parseFloat(el.dataset.counter);
  const observer = new IntersectionObserver(([entry]) => {
    if (entry.isIntersecting) {
      counterTick(el, target);
      observer.unobserve(el);
    }
  }, { threshold: 0.5 });
  observer.observe(el);
});
```

### Grid Materialize

Grid lines draw first, then panels fill with content. "Being constructed." For feature grids, card layouts, directory sections. Creates a sense of infrastructure.

```css
[data-entrance="grid-materialize"] {
  opacity: 0;
}

[data-entrance="grid-materialize"].is-visible {
  animation: grid-materialize 600ms var(--ease-out) forwards;
}

@keyframes grid-materialize {
  0%   { opacity: 0; outline: 1px solid transparent; }
  30%  { opacity: 0.3; outline: 1px solid var(--color-border); }
  60%  { opacity: 0.6; outline: 1px solid var(--color-border); }
  100% { opacity: 1; outline: none; }
}

/* Apply stagger to children */
[data-entrance="grid-materialize"].is-visible > * {
  animation: fadeUp 400ms var(--ease-out) forwards;
  opacity: 0;
}

[data-entrance="grid-materialize"].is-visible > *:nth-child(1) { animation-delay: 200ms; }
[data-entrance="grid-materialize"].is-visible > *:nth-child(2) { animation-delay: 300ms; }
[data-entrance="grid-materialize"].is-visible > *:nth-child(3) { animation-delay: 400ms; }
```

### Blur Sharpen

Content enters blurred and sharpens into focus. "Tuning a signal." Already defined conceptually in the design system but not used on the site. For atmospheric moments, background elements, secondary content.

```css
[data-entrance="blur-sharpen"] {
  opacity: 0;
  filter: blur(8px);
  transition: opacity 600ms var(--ease-out),
              filter 600ms var(--ease-out);
}

[data-entrance="blur-sharpen"].is-visible {
  opacity: 1;
  filter: blur(0);
}
```

### Mask Slide

Text revealed line by line behind a sliding mask. For rupture headlines, key statements, manifesto moments. Creates drama through progressive revelation.

```css
[data-entrance="mask-slide"] {
  clip-path: polygon(0 0, 0 0, 0 100%, 0 100%);
  transition: clip-path 700ms var(--ease-out);
}

[data-entrance="mask-slide"].is-visible {
  clip-path: polygon(0 0, 100% 0, 100% 100%, 0 100%);
}
```

---

## Scroll-Driven Effects

Use CSS `animation-timeline` where browser support allows. Fallback to IntersectionObserver for broader support. These are ambient, not dramatic. The viewer should feel them without noticing them.

### Scroll Progress Indicator

Thin Signal line at top of viewport showing page scroll progress.

```css
.scroll-progress {
  position: fixed;
  top: 0;
  left: 0;
  height: 2px;
  background: var(--color-accent);
  z-index: 9999;
  transform-origin: left;
  animation: scroll-progress linear;
  animation-timeline: scroll();
}

@keyframes scroll-progress {
  from { transform: scaleX(0); }
  to   { transform: scaleX(1); }
}
```

### Section Opacity Recession

Sections fade slightly as they scroll out of view. Creates depth. The section in the viewport is at full opacity; above and below recede.

```css
[data-section] {
  animation: section-recede linear;
  animation-timeline: view();
  animation-range: exit 0% exit 50%;
}

@keyframes section-recede {
  from { opacity: 1; }
  to   { opacity: 0.6; }
}
```

**JS fallback** for browsers without `animation-timeline`:

```js
const sections = document.querySelectorAll('[data-scroll-recede]');

function handleScroll() {
  const vh = window.innerHeight;
  sections.forEach(section => {
    const rect = section.getBoundingClientRect();
    if (rect.bottom < 0 || rect.top > vh) return;
    // Fade as section exits top
    if (rect.top < 0) {
      const progress = Math.abs(rect.top) / rect.height;
      section.style.opacity = Math.max(0.6, 1 - progress * 0.4);
    } else {
      section.style.opacity = 1;
    }
  });
}

window.addEventListener('scroll', handleScroll, { passive: true });
```

### Accent Bar Growth

Accent bars subtly grow from 40px to 60px as the viewer scrolls deeper into the section they mark. Reinforces engagement.

```css
.accent-bar[data-scroll-grow] {
  animation: bar-grow linear;
  animation-timeline: view();
  animation-range: entry 0% entry 100%;
}

@keyframes bar-grow {
  from { width: 40px; }
  to   { width: 60px; }
}
```

### Subtle Parallax

Atmospheric elements (background textures, decorative bars) move at a slightly different rate than content. Keep the offset small (10-20px max). Anything more reads as a "parallax website" and that's not the intent.

```css
[data-parallax="slow"] {
  animation: parallax-shift linear;
  animation-timeline: view();
}

@keyframes parallax-shift {
  from { transform: translateY(10px); }
  to   { transform: translateY(-10px); }
}
```

---

## Micro-Interactions

The polish layer. These are small, fast, and interactive. Every one reinforces "this was built by someone who cares about details."

The best hover states share a philosophy: **compound, not singular**. A single property change (just color, just border) reads as functional. Two or three properties changing in a staggered cascade reads as crafted. The key is staggering — the border arrives at 100ms, the background shift at 150ms, the shadow at 200ms. The viewer perceives choreography, not chaos.

### Card Compound Hover

The signature card interaction. Three stages, staggered timing. Border → lift → internal accent shift. Each property has its own duration so the hover unfolds rather than snaps.

```css
.card {
  border: 1px solid var(--color-border);
  background: var(--color-bg-elevated);
  transition:
    border-color 100ms var(--ease-sharp),
    transform 200ms var(--ease-out),
    box-shadow 200ms var(--ease-out),
    background-color 200ms var(--ease-out);
}

.card:hover {
  border-color: var(--color-accent);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15),
              0 0 0 1px rgba(245, 158, 11, 0.08);
  background: color-mix(in oklch, var(--color-accent) 3%, var(--color-bg-elevated));
}

.card .accent-bar {
  width: 32px;
  transition: width 200ms var(--ease-out) 100ms;
}

.card:hover .accent-bar {
  width: 48px;
}
```

The `translateY(-2px)` is subtle enough to feel like the card is responding, not jumping. The tinted background (`color-mix` at 3%) warms the card just enough to register subconsciously. The accent bar widens 100ms after the border changes — two beats, not one.

**Active state matters.** On click, reverse the lift. This completes the interaction loop.

```css
.card:active {
  transform: translateY(0);
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
  transition-duration: 50ms;
}
```

### Stats Value Hover Glow

Stats values gain a subtle Signal text-shadow on hover. The glow suggests "this is live data" without being decorative.

```css
.stats__value {
  transition:
    text-shadow 150ms var(--ease-sharp),
    color 150ms var(--ease-sharp);
}

.stats__value:hover {
  text-shadow: 0 0 20px rgba(245, 158, 11, 0.25),
               0 0 4px rgba(245, 158, 11, 0.1);
  color: var(--color-fg-emphasis);
}
```

Keep the glow diffuse (20px spread, low alpha). A tight glow looks like a neon sign. A wide, faint glow looks like data pulsing.

### Underline Draw

Links where the underline grows from left to right on hover. More intentional than a snap-on underline. Use for navigation links, CTA text links, and footer links.

```css
.link-draw {
  position: relative;
  text-decoration: none;
}

.link-draw::after {
  content: '';
  position: absolute;
  left: 0;
  bottom: -2px;
  width: 0;
  height: 2px;
  background: var(--color-accent);
  transition: width 200ms var(--ease-out);
}

.link-draw:hover::after {
  width: 100%;
}
```

**Variant: draw from center.** For centered layouts (CTA voids, footer links):

```css
.link-draw--center::after {
  left: 50%;
  transform: translateX(-50%);
}
```

### Text Brighten on Hover

For list items, metadata rows, and any element where the text should "activate" on hover. The color shifts from secondary to primary — subtle but clear.

```css
.text-brighten {
  color: var(--color-fg-secondary);
  transition: color 150ms var(--ease-out);
}

.text-brighten:hover {
  color: var(--color-fg);
}
```

Pair with an index counter or arrow for compound effect. The brightness change alone is too subtle to carry a hover state — it needs a partner.

### CTA Magnetic Pull

Subtle 2-3px track toward cursor within ~50px proximity. The button follows the cursor slightly. Use sparingly — once per page, on the primary CTA only.

```js
function magneticPull(button, strength = 3, radius = 50) {
  button.addEventListener('mousemove', (e) => {
    const rect = button.getBoundingClientRect();
    const cx = rect.left + rect.width / 2;
    const cy = rect.top + rect.height / 2;
    const dx = e.clientX - cx;
    const dy = e.clientY - cy;
    const dist = Math.sqrt(dx * dx + dy * dy);

    if (dist < radius) {
      const pull = (1 - dist / radius) * strength;
      button.style.transform = `translate(${dx * pull / radius}px, ${dy * pull / radius}px)`;
    }
  });

  button.addEventListener('mouseleave', () => {
    button.style.transform = 'translate(0, 0)';
    button.style.transition = 'transform 200ms var(--ease-out)';
    setTimeout(() => { button.style.transition = ''; }, 200);
  });
}
```

### Link Arrow Slide

Arrow (→) shifts right 4px on hover. Simple, functional, universal for navigation links.

```css
.link-arrow {
  display: inline-block;
  transition: transform 150ms var(--ease-sharp);
}

a:hover .link-arrow {
  transform: translateX(4px);
}
```

### Option Hover (Form Choices)

For selectable options (buttons that act as radio choices). The hover should feel like the option is "rising to meet you." Border → background tint → subtle inner glow.

```css
.option {
  border: 1px solid var(--color-border);
  background: var(--color-bg-elevated);
  transition:
    border-color 100ms var(--ease-sharp),
    background-color 150ms var(--ease-out),
    box-shadow 200ms var(--ease-out);
}

.option:hover {
  border-color: var(--color-accent);
  background: color-mix(in oklch, var(--color-accent) 6%, var(--color-bg-elevated));
  box-shadow: inset 0 0 0 1px rgba(245, 158, 11, 0.06);
}

.option:active {
  transform: scale(0.98);
  transition-duration: 50ms;
}
```

The `inset` shadow at extremely low alpha (0.06) creates a barely-perceptible inner warmth. The viewer won't see it consciously, but the option feels more "ready" than one without it.

### Border Trace

Signal border traces card perimeter clockwise on hover. 300ms. Use on featured cards or highlighted elements only (1-2 per page).

```css
.card-trace {
  position: relative;
  overflow: hidden;
}

.card-trace::after {
  content: '';
  position: absolute;
  inset: 0;
  border: 2px solid transparent;
  border-radius: 2px;
  transition: border-color 300ms var(--ease-out);
}

.card-trace:hover::after {
  border-color: var(--color-accent);
  animation: border-trace 300ms var(--ease-out);
}

@keyframes border-trace {
  0%   { clip-path: polygon(0 0, 0 0, 0 0, 0 0); }
  25%  { clip-path: polygon(0 0, 100% 0, 100% 0, 0 0); }
  50%  { clip-path: polygon(0 0, 100% 0, 100% 100%, 0 0); }
  75%  { clip-path: polygon(0 0, 100% 0, 100% 100%, 0 100%); }
  100% { clip-path: polygon(0 0, 100% 0, 100% 100%, 0 100%); }
}
```

### Index Counter Accent Cascade

On hover over a numbered list item, the index pulses Signal, then the text brightens. Two beats. The stagger creates a left-to-right "activation" sweep.

```css
.features__item {
  transition: background-color 150ms var(--ease-out);
}

.features__item:hover {
  background-color: rgba(245, 158, 11, 0.03);
}

.features__item:hover .features__idx {
  color: var(--color-accent);
  transition: color 100ms var(--ease-sharp);
}

.features__item:hover span:last-child {
  color: var(--color-fg-emphasis);
  transition: color 100ms var(--ease-sharp) 80ms;
}
```

The background tint at 0.03 alpha is nearly invisible but unifies the row. The 80ms delay on the text (not 100ms — slightly faster than the index) creates a smooth sweep rather than a rigid two-step.

### Button Hover Philosophy

Buttons follow a hierarchy of hover intensity matching their visual weight:

**Primary (Signal fill):** Inverts to foreground color. The strongest transition. Background morphs, text darkens.

```css
.btn-primary {
  background: var(--color-accent);
  color: var(--color-fg-inverse);
  transition:
    background-color 150ms var(--ease-sharp),
    box-shadow 200ms var(--ease-out);
}

.btn-primary:hover {
  background: var(--color-fg);
  color: var(--color-bg);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
}
```

**Secondary (border):** Fills with accent. Border dissolves into solid.

```css
.btn-secondary {
  border: 1px solid var(--color-accent);
  color: var(--color-accent);
  background: transparent;
  transition:
    background-color 150ms var(--ease-out),
    color 100ms var(--ease-sharp),
    box-shadow 200ms var(--ease-out);
}

.btn-secondary:hover {
  background: var(--color-accent);
  color: var(--color-fg-inverse);
  box-shadow: 0 4px 12px rgba(245, 158, 11, 0.15);
}
```

**Ghost (subtle border):** Warms. Border turns Signal, background tints barely.

```css
.btn-ghost {
  border: 1px solid var(--color-border);
  background: transparent;
  transition:
    border-color 100ms var(--ease-sharp),
    color 150ms var(--ease-out),
    background-color 200ms var(--ease-out);
}

.btn-ghost:hover {
  border-color: var(--color-accent);
  color: var(--color-accent);
  background: color-mix(in oklch, var(--color-accent) 5%, transparent);
}
```

### Hover on Dark vs. Light Surfaces

On dark surfaces, hover effects use **additive** light: glows, brightening, warm tints. On light surfaces (rupture, light mode), hover effects use **subtractive** shadow: subtle drop shadows, border darkening, slight dimming of surrounding elements.

```css
/* Dark surface hover */
.dark-surface .card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15),
              0 0 0 1px rgba(245, 158, 11, 0.08);
}

/* Light surface hover */
.light-surface .card:hover {
  box-shadow: 0 2px 8px rgba(28, 25, 23, 0.08),
              0 0 0 1px rgba(245, 158, 11, 0.12);
}
```

---

## Atmospheric Effects

Always-running, ambient effects. The viewer should not perceive these as animation. They're texture. If someone notices the effect, it's too strong.

### Breathing Glow

Hero accent bar has subtle brightness oscillation. 4-6s cycle. The oscillation range is tiny (opacity 0.85 to 1.0). "The signal is live."

```css
.hero__bar--breathing {
  animation: breathing-glow 5s ease-in-out infinite;
}

@keyframes breathing-glow {
  0%, 100% { opacity: 0.85; }
  50%      { opacity: 1; }
}
```

### Noise Drift

If a noise texture overlay is present, translate it 1-2px over 8-10s, then back. Creates subtle organic movement in the background. The texture should be near-imperceptible to begin with.

```css
.noise-overlay {
  animation: noise-drift 10s ease-in-out infinite alternate;
}

@keyframes noise-drift {
  from { transform: translate(0, 0); }
  to   { transform: translate(1px, -1px); }
}
```

### Status Dot Pulse

The one exception to "no pulsing." A small dot (6-8px) that pulses to communicate genuine live status. Only use when something is actually live or connected.

```css
.status-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--color-accent);
  animation: status-pulse 2s ease-in-out infinite;
}

@keyframes status-pulse {
  0%, 100% { opacity: 0.6; transform: scale(1); }
  50%      { opacity: 1; transform: scale(1.15); }
}
```

---

## Choreography Sequences

Concrete animation scripts for specific page sections. These define the order, timing, and relationships between multiple animations firing together.

### Enhanced Hero Sequence

Replace uniform fade-up with a choreographed entrance.

```
0ms      Accent bar draws in (drawH, 600ms)
200ms    Broadcast label fades in (fadeIn, 200ms)
300ms    Headline clip-reveals from center (clip-reveal, 600ms)
700ms    Subheadline fades up (fade-up, 400ms)
900ms    CTA fades up (fade-up, 400ms)
1100ms   Glitch trigger on headline (160ms)
```

The headline uses clip-reveal instead of fade-up. This single change makes the hero feel intentional rather than generic. Everything else stays the same.

### Stats Bar Sequence

```
0ms      Top and bottom borders draw in from left (drawH, 400ms)
200ms    Values counter-tick to target numbers (800ms)
400ms    Labels stagger in (fade-in, 200ms each, 100ms stagger)
600ms    Pipes fade in last (fade-in, 200ms)
```

The counter-tick on values creates the feeling of data coming online. Borders drawing first establishes the container. Labels and pipes fill in after the numbers land.

### Plugin Card Sequence

For the plugins page or any card grid.

```
0ms      Grid border lines draw (grid-materialize, 600ms)
200ms    Card 1 content fades up
300ms    Card 2 content fades up
400ms    Card 3 content fades up
500ms    Code blocks within cards clip-reveal from left
```

Stagger between cards: 100ms. Enough to read as sequential, not enough to feel slow.

### Rupture Entrance

The rupture is the most dramatic moment on the page. Its entrance should reflect that.

```
0ms      Surface color transition (background clips from center, 400ms)
200ms    Vertical accent bar draws down (drawV, 600ms)
400ms    Headline mask-slides from left (mask-slide, 700ms)
700ms    Body text fades up (fade-up, 400ms)
```

The surface clips in first. The viewer sees the light background expanding before any content appears. Then the accent bar draws. Then the headline reveals. The body text arrives last and quietest. Each element has a clear entry order.

---

## Implementation Guidance

### CSS-Only vs. JavaScript Decision Tree

**Use CSS when:**
- The animation is triggered by a state change (hover, focus, class toggle)
- The animation is scroll-driven and `animation-timeline` is supported
- The animation is atmospheric (infinite, ambient)
- The animation is a simple transition between two states

**Use JavaScript when:**
- The animation involves counting or dynamic values (counter-tick)
- The animation needs cursor position (magnetic pull)
- The animation requires choreography with precise timing between elements
- The animation needs IntersectionObserver for scroll triggering
- The animation has complex state or conditional logic (glitch)

### Performance Rules

**Only animate these properties:** `transform`, `opacity`, `clip-path`, `filter`. These are compositor-friendly and won't trigger layout or paint. Everything else (width, height, top, left, margin, padding, border-width) triggers layout recalculation and causes jank.

**`will-change` sparingly.** Apply only to elements that will animate soon. Remove after animation completes if possible. Never apply to more than 5 elements per page. Each `will-change` creates a new compositor layer with memory cost.

**Cap simultaneous animations.** Maximum 3 animations running simultaneously in any viewport. The choreography sequences are designed to stagger, not overlap. If you see 3+ things moving at once, the stagger timing is wrong.

**`prefers-reduced-motion`.** Always respect it. All entrance animations should have a reduced-motion fallback that shows content immediately without motion. Atmospheric effects should stop entirely.

```css
@media (prefers-reduced-motion: reduce) {
  [data-entrance] {
    opacity: 1 !important;
    transform: none !important;
    clip-path: none !important;
    filter: none !important;
    animation: none !important;
    transition: none !important;
  }

  .breathing-glow,
  .noise-overlay,
  .status-dot {
    animation: none !important;
  }
}
```

### Astro-Specific Patterns

**Scoped styles.** Entrance animations defined in component `<style>` blocks are scoped. The `data-entrance` attribute pattern works because both the attribute and the CSS selector live in the same component.

**Inline scripts.** IntersectionObserver setup goes in an inline `<script>` at the page level (not component level) so it can observe all sections.

**Extending the existing `data-section` pattern.** The site already uses `data-section` + `is-visible` for scroll reveals. New entrances should extend this system, not replace it. Add `data-entrance` to specify the entrance type while keeping `data-section` for the observer.

```html
<!-- Existing pattern (backwards compatible) -->
<section data-section="features">...</section>

<!-- Enhanced with entrance type -->
<section data-section="features" data-entrance="grid-materialize">...</section>
```

The IntersectionObserver adds `is-visible` to trigger the entrance. The `data-entrance` value determines which CSS animation plays.

**Stagger with `data-delay`.** The site already uses `data-delay="1..12"` for stagger. Continue using this for child-element staggering within a section.

```css
[data-delay="1"] { animation-delay: 100ms; }
[data-delay="2"] { animation-delay: 200ms; }
[data-delay="3"] { animation-delay: 300ms; }
/* ... up to 12 */
```
