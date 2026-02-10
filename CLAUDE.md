# Channel 47

Claude Code plugin marketplace. Site in `site/`, plugins in `plugins/`, skills in `skills/` and `.claude/skills/`, docs in `docs/`.

## Commands

```bash
npm install   # Workspaces
npm run dev   # Site on port 4321+
npm run build
npm test      # node --test
```

Node >=20. Deploys to Vercel (static + one serverless endpoint `/api/subscribe`).

## Plugin Version Sync

When modifying plugins, update version in all three:
1. `plugins/{plugin}/.claude-plugin/plugin.json`
2. `plugins/{plugin}/package.json`
3. `.claude-plugin/marketplace.json`

## Environment

Copy `.env.example` to `.env`.

## Gotchas

- **Site patterns**: See `site/CLAUDE.md` for Astro-specific gotchas.
