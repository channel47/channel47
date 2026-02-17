# channel47

Open-source profession plugins, MCP servers, and brand skills for [Channel 47](https://channel47.dev).

## Structure

```
.claude-plugin/       → Marketplace registry (marketplace.json)
plugins/
  media-buyer/        → Paid-search toolkit: platform connection, search-term verdicting, waste detection, morning briefs, PMax decoding
packages/
  mcps/               → MCP servers (npm workspaces)
    dataforseo/       → DataForSEO API
    google-ads/       → Google Ads API
    nano-banana/      → AI image generation (Gemini)
    substack/         → Substack scraping
skills/               → Brand .skill files (voice, positioning, design, motion)
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
