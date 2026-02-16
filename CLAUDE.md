# Channel 47 Ecosystem

Plugin marketplace, MCP servers, and brand skills for Claude Code.

## Structure

```
.claude-plugin/marketplace.json   # Plugin registry (channel47 marketplace)
plugins/
  media-buyer/                    # Campaign building, creative testing, account audits (v3.1.0)
packages/mcps/                    # MCP servers (npm workspaces)
  dataforseo/                     # DataForSEO keyword research API
  google-ads/                     # Google Ads API
  nano-banana/                    # AI image generation (Gemini)
  substack/                       # Substack scraping
skills/                           # Brand .skill files
```

## Commands

**MCP servers** (cd into `packages/mcps/`):
```bash
npm install
npm run build
npm run test
```

**Plugin install** (from any Claude Code session):
```
/plugin marketplace add channel47/channel47
/plugin install media-buyer@channel47
```

## Brand Skills

Four `.skill` files in `skills/`:
- `brand-voice.skill` — Channel 47 writing voice
- `frontend-design.skill` — Site design system and conventions
- `motion-design.skill` — Animation and interaction patterns
- `positioning.skill` — Positioning and messaging framework

## Plugin Development

Plugins live in `plugins/`. Each plugin has a `.claude-plugin/plugin.json` manifest. The marketplace registry at `.claude-plugin/marketplace.json` indexes all available plugins.

## MCP Servers

Each server in `packages/mcps/` is an independent npm package within a workspaces monorepo. Each has its own README with setup and API details.

## Gotchas

- **npm workspaces** — run `npm install` from `packages/mcps/`, not from individual server dirs.
- **Strategy docs moved** — positioning brief and product marketing context now live in `../site/.claude/`, not here.
- **No `docs/` directory** — despite older references, strategy docs are consolidated in the site repo.
