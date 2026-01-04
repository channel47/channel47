---
title: Design Philosophy
description: The system and principles behind ch47's intentionally simple design.
date: 2026-01-04
tags:
  - design
  - philosophy
  - css
author: Channel 47
---

The blog follows a "less is more" design philosophy centered on intentional simplicity. Every element earns its place by serving a purpose, with decorative touches kept minimal and purposeful rather than ornamental.

## Color System

A warm dark mode palette using OKLCH color space for perceptually uniform colors.

| Element | Description |
|---------|-------------|
| **Background** | Warm charcoal — not pure black, but a subtle warm undertone |
| **Foreground** | Soft cream — gentler than pure white, easier on the eyes |
| **Accent** | Muted coral — used sparingly for CTAs, logo, and highlights |

```css
--color-bg: oklch(15% 0.01 60);      /* Warm charcoal */
--color-fg: oklch(93% 0.02 90);      /* Soft cream */
--color-accent: oklch(70% 0.15 30);  /* Muted coral */
```

OKLCH provides perceptually uniform color adjustments — changing the lightness value creates predictable, visually consistent results across different hues.

## Typography

A dual-font system with clear roles for maximum readability and visual impact.

### Geist Sans

Headlines, navigation, UI elements. Used at extreme weights with tight tracking for bold, impactful headlines.

```css
h1 {
  font-family: var(--font-display); /* Geist */
  font-weight: var(--font-black);   /* 900 */
  letter-spacing: var(--tracking-tightest);
}
```

### Lora Serif

Body text for long-form reading. Set at comfortable sizes with generous line-height for optimal readability.

```css
body {
  font-family: var(--font-body);    /* Lora */
  font-size: var(--text-lg);        /* 18px */
  line-height: var(--leading-relaxed); /* 1.7 */
}
```

## Hand-Drawn Aesthetic

A signature visual language using intentionally imperfect SVG strokes. Each element features varying stroke widths and organic curves to simulate hand-drawn lettering.

- **Logo**: Hand-drawn "ch47" with orange asterisk accent
- **CTA Underlines**: Wavy, rough, and scribble variants
- **Menu Icon**: Morphing hand-drawn paths
- **Decorative Elements**: Asterisks and dividers at low opacity (15%)

```css
--stroke-width-thin: 1.5px;
--stroke-width-base: 2px;
--decorative-opacity: 0.15;
```

## Layout Principles

- **Maximum width**: 672px for optimal reading line length
- **Generous whitespace**: Consistent vertical rhythm that scales responsively
- **Mobile-first**: Tighter padding on mobile (16px), larger on desktop (32px)
- **Safe areas**: Proper insets for notched devices

```css
--content-width: 672px;
--padding-mobile: var(--space-4);  /* 16px */
--padding-desktop: var(--space-8); /* 32px */
```

## Interactive Elements

### Scroll Animations

Content fades up with staggered delays for a natural reveal effect.

```css
.animate-fade-up {
  animation: fade-up var(--duration-normal) var(--ease-out) both;
}

.stagger-1 { animation-delay: 0ms; }
.stagger-2 { animation-delay: 50ms; }
.stagger-3 { animation-delay: 100ms; }
```

### Header Behavior

Hides on scroll down to maximize reading space, reappears on scroll up for easy navigation.

### Touch Targets

Minimum 48px for all interactive elements, ensuring comfortable touch interaction on mobile devices.

```css
--touch-target-min: 48px;
```

### Micro-interactions

Scale feedback for tactile response — elements subtly shrink on press and lift on hover.

```css
--scale-press: 0.98;
--scale-hover: 1.02;
```

## Image Treatment

- **Hero integration**: Images layered behind headlines with gradient fades
- **Low opacity**: Images at 50% serve as atmospheric backgrounds
- **Hand-drawn borders**: Corner accent SVGs at 15% opacity

```css
--image-bg-opacity: 0.5;
--image-corner-opacity: 0.15;
```

## Implementation

All tokens are defined in `src/styles/design-tokens.css` and applied through `src/styles/global.css`. Components reference these tokens rather than hard-coded values, creating a cohesive visual experience that's easy to maintain and evolve.

The system prioritizes:

1. **Consistency** — Every element uses the same values
2. **Maintainability** — Change a token, update everywhere
3. **Purposeful simplicity** — Nothing decorative without function
