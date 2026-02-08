# Channel 47

Claude Code plugin marketplace. Plugins in `plugins/`, Astro marketing site in `site/`.

## Commands

```bash
npm install            # Install dependencies (workspaces)
npm run dev            # Run site locally
npm run build          # Build site
npm run preview        # Preview production build
npm test               # Run tests (node --test)
```

## Architecture

```
site/src/
  pages/          index.astro, plugins.astro, start.astro, api/subscribe.ts
  layouts/        BaseLayout.astro
  components/     Nav, Footer, EmailSignup, Logo, LogoAnimated, SocialLinks, Prose, ...
  styles/         design-tokens.css (vars), global.css (base + utilities)
plugins/
  ads/            Google Ads plugin (v2.5.0) — skills, agents, hooks, MCP
```

Node >=20 required. Deploys to Vercel (static + one serverless endpoint for newsletter subscribe).

## Plugin Version Sync

When modifying plugins, update version in:
1. `plugins/{plugin}/.claude-plugin/plugin.json`
2. `plugins/{plugin}/package.json` or `pyproject.toml`
3. `.claude-plugin/marketplace.json`

## Environment

Copy `.env.example` to `.env`. Key vars: `KIT_API_KEY` (newsletter), `PUBLIC_GA_MEASUREMENT_ID`, `PUBLIC_GOOGLE_ADS_ID`, `PUBLIC_META_PIXEL_ID` (analytics/tracking). Others (`ANTHROPIC_API_KEY`, `RESEND_API_KEY`, `GEMINI_API_KEY`) used by CI and plugins.

## Content Planning

Content strategy and topic ideas live in `docs/content-planning/`. See that folder's README for the system overview.

## Gotchas

- **Astro scoped CSS**: Cross-component ancestor selectors need `:global()`. E.g. in Nav.astro: `:global([data-section="hero"].is-visible) .nav` — not `[data-section="hero"].is-visible .nav`.
- **Scroll reveals**: Sections use `data-section` + `is-visible` class via IntersectionObserver (threshold 0.15). Hero gets `is-visible` immediately via JS, not IO.
- **Dev server port**: Defaults to 4321 but often lands on 4322/4323 if ports are in use.
