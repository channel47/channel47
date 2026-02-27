# Channel 47 Ecosystem

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Open-source profession plugins for Claude Code, Claude Cowork, and Codex. Each plugin packages the complete skill set a practitioner needs — organized by profession, built from real workflows.

Season 01 ships the media buyer plugin. Built from managing 25+ ad accounts daily.

[channel47.dev](https://channel47.dev) | [Build Notes](https://channel47.dev/subscribe) | [Build your first skill](https://channel47.dev/build) | [X](https://x.com/ctrlswing) | [LinkedIn](https://www.linkedin.com/in/jackson-d-9979a7a0/)

## Plugins

| Plugin | Version | What it does |
|--------|---------|-------------|
| [media-buyer](./plugins/media-buyer/) | 6.1.0 | Google Ads + Bing Ads toolkit — setup verification, morning briefs, waste detection, search-term verdicting, PMax decoding. MCP-native with guarded mutations. |

## Install

From any Claude Code session:

```
/plugin marketplace add channel47/plugins
/plugin install media-buyer@channel47
```

Set your API credentials as environment variables. The plugin bundles its own MCP servers — no separate install.

## How it works

Each plugin is self-contained. Install it and it works (modulo API keys). No shared infrastructure, no cross-plugin dependencies.

**Skills** are markdown files that teach AI your process. Two tiers:

- **Tier 1** — Pure knowledge. A SKILL.md with references. Frameworks, checklists, domain expertise. If you can explain how you do something, you can write one.
- **Tier 2** — Knowledge + tools. SKILL.md bundled with MCP integrations that call APIs, process data, and return structured results.

**Hooks** intercept write operations before they execute. Every mutation goes through dry-run preview and explicit approval.

## MCP Servers

MCP servers live in their own repo: [channel47/mcps](https://github.com/channel47/mcps)

Plugins bundle the MCP servers they need via `.mcp.json` — you don't install them separately.

## Contributing

Tier 1 contributions are markdown. If you can write a checklist, you can build a skill.

Tier 2 contributions add scripts for deterministic logic. Claude helps you write the script — that's part of the point.

Fork the repo, add your skill to the relevant plugin, submit a PR.

## License

MIT
