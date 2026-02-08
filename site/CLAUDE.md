# Channel 47 Site

Astro 5 site deploying to channel47.dev via Vercel.

## Commands

```bash
npm run dev      # localhost:4321
npm run build    # Production build
npm run preview  # Preview production build
npm test         # node --test (tests/homepage.test.mjs)
```

## Environment

```bash
KIT_API_KEY=
PUBLIC_GA_MEASUREMENT_ID=
PUBLIC_GOOGLE_ADS_ID=
PUBLIC_META_PIXEL_ID=
```

Static output with one serverless endpoint (`api/subscribe.ts`).

## Pages

- `/` — Landing page (hero, mission, build, status, signup, links, footer sections)
- `/plugins` — Plugin marketplace display
- `/start` — CTA landing page with section-based layout

## CSS

Pure CSS custom properties. No Tailwind.
- `src/styles/design-tokens.css` — Colors, typography, spacing, animation tokens
- `src/styles/global.css` — Base styles, utilities, prose formatting
- Component `<style>` blocks are Astro-scoped

## Key Patterns

- **Scroll reveals**: `data-section` + `is-visible` via IntersectionObserver (0.15 threshold). Hero section gets `is-visible` immediately via JS.
- **Animations**: `data-animate="fade-up|fade-in|scale-in|..."` with `data-delay="1..12"` for stagger.
- **Astro scoping gotcha**: Cross-component ancestor selectors need `:global()` wrapper.
