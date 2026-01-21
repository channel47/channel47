# Channel 47

Claude Code plugin marketplace for Google Ads marketers. Plugins live in `plugins/`, marketing site in `site/`.

## Commands

```bash
npm install            # Install dependencies (workspaces)
npm run dev            # Run site locally
npm run build          # Build site
```

## Plugin Version Sync

When modifying plugins, update version in:
1. `plugins/{plugin}/.claude-plugin/plugin.json`
2. `plugins/{plugin}/package.json`
3. `.claude-plugin/marketplace.json`

Add changelog entry for non-trivial changes.

## Environment

Copy `.env.example` to `.env`. Site needs `BEEHIIV_*` vars for newsletter.
