# Implementation Patterns

CSS architecture, theming, responsive design, and production considerations.

For detailed patterns, see the specific implementation files:

| Topic | Reference |
|-------|-----------|
| CSS Architecture | @css-architecture.md — Custom properties, scoping, naming, file organization |
| Theming | @theming.md — Dark mode, theme switching, color schemes |
| Responsive | @responsive.md — Breakpoints, fluid typography, container queries |
| Accessibility | @accessibility.md — Focus states, reduced motion, semantic HTML, performance |

## General Principles

- **Custom properties for everything** — No hardcoded colors or sizes in components
- **Mobile-first responsive** — Base styles are mobile, enhance with media queries
- **System preference respect** — Dark mode, reduced motion, high contrast
- **Performance by default** — GPU-accelerated animations, efficient selectors
