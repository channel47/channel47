# channel47

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Legacy Claude Code plugin packaging for Channel47 systems.

[channel47.dev](https://channel47.dev) | [X](https://x.com/ctrlswing) | [LinkedIn](https://www.linkedin.com/in/jackson-d-9979a7a0/)

## Status

The public, agent-discoverable skills now live in [`channel47/skills`](https://github.com/channel47/skills). This repo is kept for plugin manifests, compatibility, and historical source material while Channel47 moves toward standalone skills plus MCP connectors.

New flagship marketing skills should be added to `channel47/skills` first. Only update this repo when plugin packaging itself needs to change.

## Plugins

| Plugin | What it does |
|--------|-------------|
| [media-buyer](./plugins/media-buyer/) | Query and manage Google Ads, Bing Ads, and Meta Ads accounts with Claude as your media buying copilot. |
| [frontend-designer](./plugins/frontend-designer/) | Design, build, review, and polish beautiful web UIs — from design system to final animation. 7 skills, 2 agents. |
| [creative-strategist](./plugins/creative-strategist/) | Customer voice research, persona building, and angle generation from real public data. 3 skills, 4 commands, 1 agent. |

## Successor Repos

- [`channel47/skills`](https://github.com/channel47/skills) — standalone skills: creative strategist, customer research, persona builder, angle generator, advertorial builder, media buyer, and supporting utilities.
- [`channel47/mcps`](https://github.com/channel47/mcps) — MCP servers for Google Ads, Bing Ads, and Meta Ads.
- [`channel47/site-v1`](https://github.com/channel47/site-v1) — current channel47.dev site.

## Contributing

Plugins are markdown-based. If you can write a checklist or a framework, you can contribute a skill.

Fork the repo, add your contribution, submit a PR.

## License

MIT
