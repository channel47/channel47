# Channel 47 Site

Astro 5 → channel47.dev via Vercel. Static output + one serverless endpoint (`api/subscribe.ts`).

## Commands

```bash
npm run dev      # localhost:4321+
npm run build
npm test         # node --test
```

## Environment

`KIT_API_KEY` required for subscribe endpoint. `PUBLIC_GA_*` / `PUBLIC_META_*` for analytics.

## Pages

- `/` — Landing (hero, stats, why, features, rupture, signup, cta)
- `/plugins` — Marketplace
- `/build` — Skill builder funnel, **no Nav/Footer**
- `/api/subscribe` — POST, proxies to Kit API

## CSS

Pure CSS custom properties — no Tailwind. `design-tokens.css` for variables, `global.css` for base/utilities, component `<style>` blocks are Astro-scoped. Body text is JetBrains Mono (mono-first is intentional). Single accent: amber `#F59E0B`.

## Scroll Reveals (two layers)

1. **Section-level**: `data-section="name"` + IO (threshold 0.15). Adds `.is-visible`. Hero gets it immediately via JS, not IO.
2. **Element-level**: `BaseLayout` observes `[data-animate]` (threshold 0.1). One-time trigger. Stagger with `data-stagger="1..12"`.

## Component Conventions

- Guard double-init with `data-initialized` attribute
- State classes: `.is-visible`, `.is-loading`, `.is-success`, `.is-error`, `.is-server-error`
- Prefer `[data-*]` attributes over classes for JS targeting
- Vanilla JS only — no client frameworks

## Gotchas

- **`:global()` required** for cross-component ancestor selectors in scoped styles
- **`/build`** intentionally omits Nav/Footer
