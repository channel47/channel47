---
name: motion-design
description: "channel47 motion and interaction design system. Intentional, restrained micro-interactions that feel built, not decorated. Use when adding animation, hover effects, scroll reveals, transitions, or any interactive behavior to ch47 interfaces. Complements the frontend-design skill. Triggers on: animation, hover effect, scroll animation, transition, micro-interaction, motion, interactive, loading state, page transition, reveal, entrance animation, ch47 motion."
---

# Motion Design. ch47.

Motion is opinion. Every animation says something about the brand. Bounce says playful. Drift says editorial. ch47 says decisive.

Things arrive. They don't wander in. They don't bounce. They don't float. They appear with intent, like someone placed them there quickly and confidently.

## Principles

**Purposeful.** Every animation answers "why does this move?" If the answer is "because it looks cool," cut it.

**Quick.** Default shorter than you think. 200ms solves most problems. 400ms is a big moment. Anything over 700ms better be earning its time.

**Decisive.** Fast start, smooth land. The easing curve is the personality. No elastic, no spring, no bounce. Things decelerate into place.

**Sparse.** 2-4 animated elements per page. Everything else just exists. The stillness makes the motion matter.

**Composed.** Animations don't exist in isolation. They exist in relation to each other. The *sequence* of animations, the pauses between them, and the hierarchy of who moves first, is the choreography. A page where everything animates at once is a page with no choreography. That's a demo reel, not a design.

## Timing

```
Instant    100ms    Hover states, focus rings, color shifts.
Quick      200ms    Reveals, toggles, state changes. The default.
Measured   400ms    Section entrances, hero reveals, content swaps.
Cinematic  700ms    Full-page loads, one-time hero moments. Rare.
```

Use Instant for anything the user triggered directly (hover, click). Use Quick for things appearing in response. Use Measured for things the user is watching arrive.

## Easing

```
Default    cubic-bezier(0.16, 1, 0.3, 1)    Fast start, smooth land.
Sharp      cubic-bezier(0.33, 1, 0.68, 1)    Snappier. Buttons, toggles.
Linear     linear                              Progress bars only.
```

The default curve starts fast (0.16) and decelerates slowly (0.3, 1). Things feel like they were placed deliberately, not dropped.

**Banned:** `ease-in-out` (too symmetrical, feels floaty), `ease` (generic), spring/bounce physics, `cubic-bezier` with values > 1 (overshoot).

## Patterns

### Fade Up (Default Entrance)

The workhorse. Element fades in while translating up 10-14px. Used for content blocks, cards, text sections.

```css
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(12px); }
  to   { opacity: 1; transform: translateY(0); }
}

.reveal {
  opacity: 0;
  animation: fadeUp 400ms cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
```

The 12px translate is deliberate. Enough to notice, not enough to distract. Never exceed 20px.

### Stagger (Sequential Entrance)

Children of a container enter one by one. 60ms between each. Creates a sense of items being laid out, not dumped.

```css
.stagger > * {
  opacity: 0;
  animation: fadeUp 400ms cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
.stagger > *:nth-child(1) { animation-delay: 0ms; }
.stagger > *:nth-child(2) { animation-delay: 60ms; }
.stagger > *:nth-child(3) { animation-delay: 120ms; }
.stagger > *:nth-child(4) { animation-delay: 180ms; }
.stagger > *:nth-child(5) { animation-delay: 240ms; }
```

Cap at 5 children. Beyond that, the last items wait too long. If more than 5, group them.

### Fade In (Subtle Entrance)

Opacity only. No translate. For elements that should appear without drawing attention. Metadata, secondary info, decorative elements.

```css
@keyframes fadeIn {
  from { opacity: 0; }
  to   { opacity: 1; }
}
```

### Draw In (Line/Bar Entrance)

For accent bars, dividers, and borders. The element grows from zero width or height rather than fading. Communicates precision and intent.

```css
/* Horizontal bar drawing in from left */
.draw-h {
  width: 0;
  animation: drawH 400ms cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
@keyframes drawH {
  to { width: var(--target-width, 40px); }
}

/* Vertical bar growing down */
.draw-v {
  height: 0;
  animation: drawV 600ms cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
@keyframes drawV {
  to { height: var(--target-height, 200px); }
}
```

Use for accent bars in hero sections and section dividers. The draw creates a sense of the page being constructed, which aligns with the builder identity.

### The Glitch (Signature Hover)

Micro-stutter on hover. 1-2 frames via `steps(2)`. Not an animation, an interruption. The brand's signature interactive moment.

**CSS version (for static sites):**
```css
.glitch-hover:hover {
  animation: glitch 150ms steps(2) 1;
}
@keyframes glitch {
  0%   { transform: translate(0); }
  25%  { transform: translate(-2px, 1px); }
  50%  { transform: translate(1px, -1px); }
  75%  { transform: translate(-1px, 0); }
  100% { transform: translate(0); }
}
```

**React version (for artifact sandboxes and SPAs):**

CSS keyframe animations sometimes fail in sandboxed environments. The React version uses `requestAnimationFrame` for reliable execution:

```jsx
function GlitchText({ children, as: Tag = "span", style = {} }) {
  const [active, setActive] = useState(false);
  const [frame, setFrame] = useState({ x: 0, y: 0 });
  const raf = useRef(null);
  const t0 = useRef(0);

  const offsets = [
    { x: -3, y: 1 }, { x: 2, y: -1 },
    { x: -1, y: 2 }, { x: 1, y: -1 }, { x: 0, y: 0 },
  ];

  const run = useCallback((ts) => {
    if (!t0.current) t0.current = ts;
    const elapsed = ts - t0.current;
    if (elapsed > 160) {
      setActive(false);
      setFrame({ x: 0, y: 0 });
      t0.current = 0;
      return;
    }
    setFrame(offsets[Math.floor(elapsed / 35) % offsets.length]);
    raf.current = requestAnimationFrame(run);
  }, []);

  const trigger = () => {
    if (active) return;
    setActive(true);
    t0.current = 0;
    raf.current = requestAnimationFrame(run);
  };

  useEffect(() => () => { if (raf.current) cancelAnimationFrame(raf.current); }, []);

  return (
    <Tag onMouseEnter={trigger} style={{
      ...style,
      transform: `translate(${frame.x}px, ${frame.y}px)`,
      display: "inline-block", cursor: "default", position: "relative",
    }}>
      {children}
      {/* Chromatic aberration layers */}
      {active && (
        <>
          <span style={{
            position: "absolute", inset: 0,
            clipPath: "inset(8% 0 62% 0)",
            transform: `translate(${frame.x + 4}px, 0)`,
            color: "#F59E0B", opacity: 0.6, pointerEvents: "none",
            ...style,
          }}>{children}</span>
          <span style={{
            position: "absolute", inset: 0,
            clipPath: "inset(58% 0 8% 0)",
            transform: `translate(${-frame.x - 3}px, 0)`,
            color: "#F59E0B", opacity: 0.35, pointerEvents: "none",
            ...style,
          }}>{children}</span>
        </>
      )}
    </Tag>
  );
}
```

The chromatic aberration layers (clipped spans with Signal color, offset in opposite directions) create a color-split effect that reinforces the broadcast/signal identity. The clip paths isolate a top slice and bottom slice so the ghost layers don't fully overlap the original text.

**Use on:** Hero headlines, feature titles, 404 page elements. One, maybe two elements per page.

**Never on:** Body text, navigation, buttons, form elements. The glitch is for display moments only.

### Scroll Reveal (Intersection Observer)

Elements animate when they enter the viewport. Use IntersectionObserver, not scroll listeners. Threshold 0.15 (triggers when 15% visible).

```jsx
function Reveal({ children, delay = 0 }) {
  const ref = useRef(null);
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    const el = ref.current;
    if (!el) return;
    const obs = new IntersectionObserver(
      ([e]) => { if (e.isIntersecting) { setVisible(true); obs.disconnect(); } },
      { threshold: 0.15 }
    );
    obs.observe(el);
    return () => obs.disconnect();
  }, []);

  return (
    <div ref={ref} style={{
      opacity: visible ? 1 : 0,
      transform: visible ? "translateY(0)" : "translateY(12px)",
      transition: `opacity 400ms cubic-bezier(0.16,1,0.3,1) ${delay}ms, transform 400ms cubic-bezier(0.16,1,0.3,1) ${delay}ms`,
    }}>{children}</div>
  );
}
```

Each section gets one reveal. Don't wrap every element individually. Wrap the section, let children appear together or use stagger within.

### Sequential Reveal (Line-by-Line)

For terminal mocks, code blocks, or data that should appear as if being typed or computed. Uses IntersectionObserver to trigger, then reveals items on a timer.

```jsx
function SequentialReveal({ items, renderItem, interval = 250 }) {
  const ref = useRef(null);
  const [count, setCount] = useState(0);
  const started = useRef(false);

  useEffect(() => {
    const el = ref.current;
    if (!el) return;
    const obs = new IntersectionObserver(
      ([e]) => {
        if (e.isIntersecting && !started.current) {
          started.current = true;
          obs.disconnect();
          let i = 0;
          const go = () => {
            i++;
            setCount(i);
            if (i < items.length) setTimeout(go, interval + Math.random() * 100);
          };
          setTimeout(go, 400);
        }
      },
      { threshold: 0.3 }
    );
    obs.observe(el);
    return () => obs.disconnect();
  }, [items.length, interval]);

  return <div ref={ref}>{items.slice(0, count).map(renderItem)}</div>;
}
```

The random jitter on the interval (Math.random() * 100) prevents mechanical regularity. Real terminals aren't metronomic.

## Choreography

Individual patterns are instruments. Choreography is the composition. This section defines how animations *relate to each other*.

### The Sequence

When a scroll reveal triggers a section, the elements inside don't all appear at once. They follow a sequence:

**Default section choreography:**
1. **Lead element** enters (fade up, 400ms). Usually the headline or the accent bar.
2. **Pause** (80-120ms). The viewer registers the lead before anything else appears.
3. **Support elements** enter (fade up or fade in, 400ms, staggered at 60ms each). Body text, cards, metadata.

The pause between lead and support is the critical detail. Without it, everything feels simultaneous. With it, there's a sense of things being placed in order.

**Implementation:**
```jsx
// Lead element: delay 0
<Reveal delay={0}><Headline /></Reveal>

// Pause is implicit: 80ms gap before first support
<Reveal delay={480}><BodyText /></Reveal>  {/* 400ms lead + 80ms pause */}
<Reveal delay={540}><Card1 /></Reveal>     {/* +60ms stagger */}
<Reveal delay={600}><Card2 /></Reveal>     {/* +60ms stagger */}
```

### The Motion Budget

Per viewport (what the user sees without scrolling at any given scroll position), assign roles:

**Lead** (1 per viewport). Gets the longest or most complex animation. This is the element the eye goes to first. Examples: hero headline, rupture section entrance, terminal mock, glitch element.

**Support** (1-3 per viewport). Shorter, simpler animations. Fade ups, staggers, color transitions. These appear after the lead, reinforcing the hierarchy.

**Static** (everything else). No animation. Just exists. The stillness is what makes the lead and support visible.

If you can't identify which element is the lead in a viewport, the choreography is flat. Promote one element or demote the others.

**Full page motion budget:**
- Hero viewport: 1 lead (headline), 2-3 support (label, body, CTA). Cinematic timing (700ms lead).
- Middle viewports: 1 lead per section, 1-2 support. Measured timing (400ms).
- Rupture viewport: 1 lead (the rupture itself). Support is the content within the rupture. This is the page's biggest motion moment.
- Closing viewport: 1 lead (CTA or closing headline). Minimal support. Quieter than the hero.

Total animated elements across the entire page: 8-15. Fewer is usually better. Count them. If you're over 15, you're animating for the sake of it.

### The Pause as Design Element

The pauses between animations are as important as the animations themselves. A pause says "notice what just appeared before the next thing arrives."

**Micro-pause** (60-80ms). Between staggered siblings. The viewer barely perceives it consciously, but it creates a feeling of sequence rather than simultaneity.

**Breath** (100-150ms). Between the lead element and support elements within a section. The viewer registers the lead before context arrives.

**Beat** (200-400ms). Between sections, when using sequential scroll reveals. The viewer finishes absorbing one section before the next begins. This happens naturally via scroll distance, but for auto-playing sequences (terminal mocks, slideshows), build the beat in explicitly.

### Exit Choreography

Everything in the pattern library is about entrance. But what happens when a section scrolls *away*?

**Default: nothing.** Sections stay visible and static once they've entered. This is correct 80% of the time.

**Subtle recession** (use sparingly). As the next section enters the viewport, the previous section reduces opacity to 0.85-0.9. This creates a sense of depth, as if the page has layers and the current viewport is the "active" one.

```jsx
function RecedingSection({ children }) {
  const ref = useRef(null);
  const [receded, setReceded] = useState(false);

  useEffect(() => {
    const el = ref.current;
    if (!el) return;
    const obs = new IntersectionObserver(
      ([e]) => setReceded(!e.isIntersecting && e.boundingClientRect.top < 0),
      { threshold: 0 }
    );
    obs.observe(el);
    return () => obs.disconnect();
  }, []);

  return (
    <div ref={ref} style={{
      opacity: receded ? 0.88 : 1,
      transition: "opacity 400ms cubic-bezier(0.16,1,0.3,1)",
    }}>{children}</div>
  );
}
```

Use only on the hero section and one or two key sections. If every section recedes, the page feels like it's dimming, not layering.

**Hard exit** (rare). For the rupture section, when it scrolls away and the dark surface returns, the transition should feel decisive. No lingering. The light section is there, then it's gone. Don't add any fade-out. Let the scroll handle it.

### The First Impression Sequence

The page load is a one-time choreographic moment. The viewer arrives and the page assembles itself. This is the hero sequence.

**Default hero choreography:**
1. **Frame appears** (0ms). Background color renders. The dark surface is immediately present. No white flash.
2. **Nav fades in** (100ms delay, 300ms duration, fade only). Peripheral awareness.
3. **Accent element draws in** (200ms delay, 600ms duration). A vertical bar growing, or a horizontal accent bar extending. The first visual motion.
4. **Broadcast label fades in** (300ms delay, 200ms duration). Context arrives.
5. **Headline fades up** (400ms delay, 700ms duration). The lead. Cinematic timing because this is the first thing the viewer reads.
6. **Body text fades up** (700ms delay, 400ms duration). Supporting context.
7. **CTA fades in** (900ms delay, 300ms duration). The ask, appearing last.

Total sequence: ~1200ms from load to fully rendered. Under 1.5 seconds. The viewer should never feel like they're waiting.

**The auto-glitch.** On page load, the hero headline glitches once automatically, 300ms after it finishes fading in. Unprompted. A one-time introduction of the brand's signature motion. After that, the glitch only fires on hover. This distinction (between something that happens to you and something you choose to trigger) is what separates a brand moment from a feature.

```jsx
// In hero component:
const [autoGlitched, setAutoGlitched] = useState(false);
useEffect(() => {
  const t = setTimeout(() => setAutoGlitched(true), 1100); // 400ms delay + 700ms fade
  return () => clearTimeout(t);
}, []);
// Pass autoGlitched to GlitchText to trigger once on mount
```

## Hover States

Hover is feedback, not decoration. It says "this is interactive" and nothing else.

### Interactive Elements (Links, Buttons, Cards)

```css
/* Color shift: Instant (100ms) */
a:hover { color: #F59E0B; transition: color 100ms; }

/* Border shift: Instant */
.card:hover { border-color: #F59E0B; transition: border-color 100ms; }

/* Background shift: Quick (200ms) for larger surfaces */
.card:hover { background-color: #292524; transition: background-color 200ms; }

/* Arrow/icon shift: color change, no translate */
.arrow:hover { color: #F59E0B; transition: color 100ms; }
```

**Compound hover effects.** When a card has both a border shift and an internal element that reacts (an accent bar that widens, an arrow that changes color), the border changes at Instant (100ms) and the internal element changes at Quick (200ms). The slight delay between them creates a cascade that feels responsive, not mechanical.

```jsx
// Card with compound hover
const [hov, setHov] = useState(false);
<div
  onMouseEnter={() => setHov(true)}
  onMouseLeave={() => setHov(false)}
  style={{
    borderColor: hov ? "#F59E0B" : "#44403C",    // Instant
    transition: "border-color 100ms",
  }}
>
  <div style={{
    width: hov ? 40 : 24, height: 2,
    backgroundColor: hov ? "#F59E0B" : "#44403C", // Quick
    transition: "width 200ms cubic-bezier(0.16,1,0.3,1), background-color 200ms",
  }} />
</div>
```

**Banned hover effects:** Scale transforms on cards. Box shadow additions. Background color shifts to accent (too loud). Underline animations that slide in. Any transform on text besides the glitch.

### Non-Interactive Elements

Non-interactive elements do not have hover states. If it doesn't do anything when clicked, it shouldn't react when hovered.

## Loading States

### Skeleton (Default)

Placeholder shapes that match the content layout. Background color Smoke (#292524). No shimmer animation. Static placeholder until content arrives.

```jsx
<div style={{
  height: 16, width: "60%",
  backgroundColor: "#292524", borderRadius: 2,
}} />
```

**Why no shimmer:** Shimmer implies smooth, gradual loading. ch47 interfaces appear decisively. Content replaces skeleton via fadeIn (200ms).

### Status Indicator

A small circle (6-8px) in the nav or header. Solid Signal (#F59E0B) color when connected/active. Solid Ash (#44403C) when inactive. No pulsing, no glowing. State is binary, the indicator is binary.

```jsx
<div style={{
  width: 8, height: 8, borderRadius: "50%",
  backgroundColor: isActive ? "#F59E0B" : "#44403C",
  transition: "background-color 200ms",
}} />
```

## Page Transitions

Keep them simple. Fade the entire page out (200ms), swap content, fade in (300ms). No slide, no morph, no shared element transitions.

```css
.page-exit  { animation: fadeIn 200ms reverse forwards; }
.page-enter { animation: fadeIn 300ms forwards; }
```

## Anti-Patterns

Kill on sight:

- **Pulsing/glowing elements.** Implies urgency that doesn't exist. The "live" dot doesn't pulse.
- **Scanline overlays.** Sci-fi cliche. Reads as decoration, not design.
- **Particle effects.** Never.
- **Parallax scrolling.** Implies editorial warmth, not technical precision.
- **Scroll-jacking.** Never take control of the scroll.
- **Hover zoo.** If everything reacts, nothing is special. 2-4 hover effects per view.
- **Text typing animation.** Chatbot aesthetic. Not ch47.
- **Scale on hover for cards.** The universal "I used a CSS tutorial" tell.
- **Bounce/spring easing.** Playful, not decisive.
- **Infinite animations.** Nothing loops except functional spinners. And even those should be rare.
- **Slide-in from sides.** Implies something was hiding offscreen. Content appears, it doesn't enter stage left.
- **Simultaneous entrance.** If 5+ elements animate at the exact same time with the same duration, it reads as a single flash, not a composed entrance. Stagger or pick a lead.
- **Identical timing everywhere.** If every animation on the page is 400ms with the same easing, the motion has no hierarchy. Vary timing to match importance. Lead elements get more time. Support gets less.

## Decision Framework

When adding motion to a ch47 interface:

1. Does this element need to move? (Most don't.)
2. What is the motion communicating? (Entrance, feedback, state change.)
3. Is it under 400ms? (If not, justify the duration.)
4. Does it use the default easing? (If not, justify the curve.)
5. After adding it, do you have more than 4 animated elements in this viewport? (If yes, cut one.)
6. Can you identify the lead? (If every element has equal animation, promote one or demote the rest.)
7. Are there pauses between animation groups? (If everything triggers simultaneously, add micro-pauses.)
8. Does the hero sequence complete under 1.5 seconds? (If not, tighten delays.)

The best ch47 interfaces feel almost static until you interact with them. Then the few things that move feel precise and intentional. That restraint is the design.
