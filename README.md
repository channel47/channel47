# channel47

Plugin ecosystem for [Channel 47](https://channel47.dev). MCP servers, Claude Code plugins, brand skills, strategy docs.

## Structure

```
.claude-plugin/       → Marketplace registry (marketplace.json)
plugins/
  media-buyer/        → Campaign building, creative testing, account audits
packages/
  mcps/               → MCP servers (npm workspaces)
    dataforseo/       → DataForSEO API
    google-ads/       → Google Ads API
    nano-banana/      → AI image generation (Gemini)
    substack/         → Substack scraping
skills/               → Brand .skill files
docs/                 → Strategy, positioning, content planning
```

## Install

```
/plugin marketplace add channel47/channel47
/plugin install media-buyer@channel47
```

## MCP Servers

```bash
cd packages/mcps
npm install
npm run build
```

Four servers. Each has its own README in `packages/mcps/`.
