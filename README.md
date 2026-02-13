# channel47

Everything that powers the [Channel 47](https://channel47.dev) plugin ecosystem — MCP servers, Claude Code plugins, brand skills, and strategy docs.

## Structure

```
.claude-plugin/       → Marketplace registry (marketplace.json)
plugins/              → Claude Code plugins
  ads-legacy/         → Full Google Ads suite (PMax, Search, Audit)
  media-buyer/        → Streamlined campaign + creative skills
packages/
  mcps/               → MCP servers (npm workspaces)
    dataforseo/       → DataForSEO API
    google-ads/       → Google Ads API
    nano-banana/      → Nano Banana utilities
    substack/         → Substack API
skills/               → Brand .skill files
docs/                 → Strategy, positioning, content planning
```

## Plugin marketplace

This repo is a Claude Code plugin marketplace. To install:

```
/plugin marketplace add channel47/channel47
```

Then install individual plugins:

```
/plugin install media-buyer@channel47
/plugin install ads@channel47
```

## MCP servers

```bash
cd packages/mcps
npm install
npm run build
```
