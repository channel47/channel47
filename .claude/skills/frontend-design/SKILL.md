---
name: frontend-design
description: Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, artifacts, or applications (examples include websites, landing pages, dashboards, React components, HTML/CSS layouts, or when styling/beautifying any web UI). Generates creative, polished code and UI design that avoids generic AI aesthetics.
---

# Frontend Design

Create frontend interfaces that feel intentionally crafted — not generated.

## Core Philosophy

Every design decision must answer: **"Why this and not something else?"**

Generic AI outputs fail because they optimize for "looks okay" rather than "feels intentional." The goal is not decoration — it's communication through visual design.

## The AI Slop Checklist

Before finalizing any design, verify you haven't fallen into these traps:

### Color

- ❌ Purple-blue-teal gradient (the "AI default palette")
- ❌ Gradients used decoratively rather than to guide attention
- ❌ Low-contrast gray text "for subtlety"
- ✅ Limited palette with intentional accent colors
- ✅ High contrast where readability matters
- ✅ Color that reinforces hierarchy, not fights it

### Layout

- ❌ Cards with rounded corners and drop shadows as the default container
- ❌ Centered everything with max-width containers
- ❌ Three-column feature grids
- ❌ Hero section → features → testimonials → CTA (the template flow)
- ✅ Asymmetry where it creates tension or interest
- ✅ Edge-to-edge elements mixed with contained elements
- ✅ Density variations — some areas breathe, others cluster
- ✅ Grid breaks that draw attention

### Typography

- ❌ System font stack with no personality
- ❌ One font weight throughout
- ❌ Generic sizing scale (text-sm, text-base, text-lg)
- ✅ A display/heading font with character (serif, geometric, monospace — commit to something)
- ✅ Extreme size contrasts for hierarchy (72px headlines next to 14px body text)
- ✅ Weight as a design tool — bold for emphasis, light for elegance
- ✅ Letter-spacing adjustments (tighter for headlines, looser for small caps)

### Spacing

- ❌ Uniform padding everywhere (p-4, p-6, p-8)
- ❌ Spacing that "feels safe"
- ✅ Generous whitespace where content needs room to land
- ✅ Tight spacing to create visual grouping
- ✅ Optical alignment over mathematical alignment
- ✅ Vertical rhythm that creates scannable sections

### Animation & Interaction

- ❌ Hover effects on everything
- ❌ Fade-in-on-scroll for every element
- ❌ Bouncy spring animations as default
- ❌ Transitions that delay the user
- ❌ Pulsing dots/circles to draw attention (cheap, anxious energy)
- ❌ Infinite ambient animations that don't respond to user action
- ✅ Motion that communicates state change
- ✅ Micro-interactions that reward exploration (but don't demand it)
- ✅ Staggered animations that guide the eye through a sequence
- ✅ Physics that match the brand — snappy for tools, gentle for editorial

### Components

- ❌ Every button looks the same
- ❌ Generic "card" component used for everything
- ❌ Icons from three different icon sets
- ✅ Button hierarchy (primary action is unmistakable)
- ✅ Bespoke containers for different content types
- ✅ Consistent icon style (stroke weight, corner radius, optical size)

## Design Process

### 1. Establish Constraints First

Before writing any code, define:

1. **Color palette** — Maximum 5 colors: 1-2 neutrals, 1 primary, 1-2 accents
2. **Type stack** — One display font, one body font (or a single versatile family)
3. **Spacing scale** — Use multipliers of a base unit (e.g., 4px: 4, 8, 12, 16, 24, 32, 48, 64, 96)
4. **Radius scale** — Pick 2-3 values max (e.g., 0, 4px, 8px or 0, 2px, full)
5. **Shadow style** — None, subtle, or dramatic — pick one direction
6. **Motion personality** — Snappy (150ms), smooth (300ms), or cinematic (500ms+)

State these constraints explicitly in a comment block at the top of the code.

### 2. Start with Typography and Spacing

Layout is a consequence of content. Begin with:

1. Set the body text size and line-height for comfortable reading
2. Establish headline sizes relative to body (aim for 3:1 or 4:1 ratio for primary headlines)
3. Define spacing between text blocks
4. Let these decisions inform container widths

### 3. Add Color Sparingly

1. Start in grayscale or near-grayscale
2. Add primary color only to elements that need emphasis
3. Add accent color only when primary isn't enough distinction
4. Ask: "If I remove this color, does the hierarchy break?" If not, remove it.

### 4. Animate with Purpose

Add motion only when it serves one of these functions:

1. **Feedback** — Confirming an action was received
2. **Orientation** — Showing where something came from or went to
3. **Focus** — Drawing attention to what matters now
4. **Personality** — Expressing brand character (use sparingly)

If animation serves none of these, delete it.

## Implementation Patterns

### Tailwind Usage

```jsx
{
  /* ❌ Generic AI output */
}
<div className="bg-gradient-to-r from-purple-500 to-blue-500 rounded-xl shadow-lg p-6">
  <h2 className="text-2xl font-bold text-white mb-4">Features</h2>
</div>;

{
  /* ✅ Intentional design */
}
<div className="border-l-2 border-black pl-6 py-4">
  <h2 className="font-serif text-4xl tracking-tight text-black">Features</h2>
</div>;
```

### Animation Patterns

```jsx
{/* ❌ Motion for motion's sake */}
<div className="hover:scale-105 transition-all duration-300 hover:shadow-xl">

{/* ✅ Purposeful state feedback */}
<button className="transition-colors duration-150 hover:bg-black hover:text-white">

{/* ✅ Meaningful entrance (use sparingly, for key content) */}
<article className="animate-in fade-in slide-in-from-bottom-4 duration-500">
```

### Layout Breaking

```jsx
{
  /* ❌ Everything contained identically */
}
<div className="max-w-4xl mx-auto px-6">
  <Hero />
  <Features />
  <Testimonials />
</div>;

{
  /* ✅ Rhythm through variation */
}
<>
  <header className="max-w-2xl mx-auto px-6 py-24">
    <Headline />
  </header>
  <section className="w-full bg-black text-white py-16">
    <Features />
  </section>
  <aside className="max-w-5xl mx-auto grid grid-cols-3 gap-1 px-6">
    <Testimonials />
  </aside>
</>;
```

### Typography with Character

```jsx
{/* ❌ Safe and forgettable */}
<h1 className="text-3xl font-bold text-gray-900">Welcome</h1>
<p className="text-gray-600 mt-2">Get started today.</p>

{/* ✅ Creates an impression */}
<h1 className="font-serif text-6xl md:text-8xl tracking-tighter text-black">Welcome</h1>
<p className="font-mono text-sm uppercase tracking-widest text-gray-500 mt-6">Get started today</p>
```

## Detailed Recipes

For component-specific patterns (landing pages, editorial layouts, directories, forms, dark mode), see [references/recipes.md](references/recipes.md).

## Reference Aesthetics

Study these for inspiration (not imitation):

- **Linear** — Precision, monospace accents, dramatic gradients used sparingly
- **Stripe** — Dense information, subtle depth, meticulous alignment
- **Apple** — Typography-led, generous whitespace, cinematic motion
- **Vercel** — High contrast, geometric, developer-focused clarity
- **nan.fyi / svg.guide** — Interactive education, playful but precise, code-as-content
- **Read.cv** — Editorial restraint, type-forward, intentional minimalism

## Final Checklist

Before shipping, ask:

1. Can I describe this design's personality in 2-3 words?
2. If I showed this to someone, would they know it's not a template?
3. Does every color, font choice, and animation have a reason?
4. Is there at least one element that surprises or delights?
5. Would I want this in my portfolio?

If any answer is "no," iterate.
