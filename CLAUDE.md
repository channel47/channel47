# Channel 47

Claude Code plugin marketplace. Plugins live in `plugins/`, marketing site in `site/`.

## Commands

```bash
npm install            # Install dependencies (workspaces)
npm run dev            # Run site locally
npm run build          # Build site
```

## Plugin Version Sync

When modifying plugins, update version in:
1. `plugins/{plugin}/.claude-plugin/plugin.json`
2. `plugins/{plugin}/package.json` or `pyproject.toml`
3. `.claude-plugin/marketplace.json`

## Environment

Copy `.env.example` to `.env`. Site needs `KIT_API_KEY` for newsletter.

## Content Planning

Content strategy and topic ideas live in `docs/content-planning/`. See that folder's README for the system overview.
