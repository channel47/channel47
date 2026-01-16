# Changelog

All notable changes to the frontend-design plugin.

## [1.2.0] - 2026-01-16

### Changed

- **Progressive disclosure improvements**
  - Restructured reference loading in SKILL.md files to be situational, not blanket
  - Added "Always Consult" / "Load By Task" / "Deep Dives" tiers for reference architecture
  - Moved mandatory boilerplate code from SKILL.md to `@reference/performance.md`
  - Added "Core Requirements" section with principles instead of code templates

- **Softened prescriptive rules**
  - Transformed "NOT using X" checkboxes to "X choice is INTENTIONAL" checks
  - Added "The Exception Rule" to anti-patterns.md for legitimate overrides
  - Updated Meta-Rule to question defaults rather than ban common patterns

- **Added context-override guidance**
  - New "When to Override These Guidelines" sections in both SKILL.md files
  - Covers matching existing design systems, brand guidelines, user requests, constraints

- **Split large reference files for finer-grained loading**
  - `components.md` (481 lines) → `buttons.md`, `forms.md`, `cards.md`, `navigation.md`, `modals.md` + index
  - `implementation.md` (488 lines) → `css-architecture.md`, `theming.md`, `responsive.md`, `accessibility.md` + index
  - `examples.md` (428 lines) → `example-lines.md`, `example-grid.md`, `example-matrix.md`, `example-wireframe.md`, `example-combining.md` + index
  - Updated SKILL.md reference tables to point to specific files

## [1.1.0] - 2026-01-15

### Added

- `frontend-design` skill for creating distinctive UI components and layouts
  - Design thinking framework (purpose, tone, constraints, differentiation)
  - Mandatory pre-flight checklist against AI anti-patterns
  - Output contracts for React/Vue/Svelte/HTML
  - Standalone HTML demo option
- Component reference documentation
  - Button patterns (brutalist, minimal, technical)
  - Form field architecture with accessibility
  - Card patterns (elevated, bordered, subtle)
  - Navigation patterns (top nav, sidebar)
  - Modal/dialog with native `<dialog>` element
- Layout reference documentation
  - Asymmetric layouts (2:1, golden ratio)
  - Grid systems with masonry option
  - Spatial rhythm and whitespace scale
  - Hero section alternatives (not centered gradient)
  - Dashboard layouts
- Implementation reference documentation
  - CSS custom properties structure
  - Dark mode with system preference and manual toggle
  - Responsive patterns with container queries
  - Accessibility requirements (focus, reduced motion, contrast)
  - Performance patterns (CSS loading, fonts, animations)

## [1.0.0] - 2026-01-14

### Added

- Initial release
- `creating-canvas-animations` skill for HTML5 Canvas 2D animations
  - Primitives reference (lines, shapes, text, particles, grids, noise)
  - Composition reference (layering, color, density, choreography)
  - Easing functions library
  - Performance patterns (DPI, visibility, resize, cleanup)
  - Worked examples (Interface Craft style)
- Shared design system frameworks
  - Typography (font selection, pairing, scale)
  - Color (palette generation, CSS variables, dark mode)
  - Motion (timing, easing, staggered reveals)
  - Anti-patterns ("AI slop" avoidance checklist)
- TypeScript ES module output by default
- Standalone HTML demo output option
