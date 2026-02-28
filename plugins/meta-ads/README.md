# Meta Ads — Claude Code Plugin

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Meta Ads toolkit for Facebook and Instagram — creative analysis, audience building, reporting, and campaign optimization via MCP.

Part of [Channel 47](https://channel47.dev), the open-source ecosystem of profession plugins for Claude Code.

---

## Status

**Skeleton** — plugin structure and skill definitions are complete. Requires `@channel47/meta-ads-mcp` to be built and published for full functionality.

---

## Configuration

The plugin bundles one MCP server via `.mcp.json`. Set these environment variables:

| Variable | Required |
|----------|----------|
| `META_ADS_ACCESS_TOKEN` | Yes |
| `META_ADS_APP_ID` | Yes |
| `META_ADS_APP_SECRET` | Yes |
| `META_ADS_ACCOUNT_ID` | Yes |

---

## What's Inside

```text
meta-ads/
├── .claude-plugin/
│   └── plugin.json
├── .mcp.json              # Meta Ads MCP server (placeholder)
├── hooks/
│   ├── hooks.json
│   └── validate-mutations.py
├── skills/
│   ├── platform-setup/
│   ├── morning-brief/
│   ├── waste-detector/
│   ├── creative-analyzer/
│   └── audience-builder/
├── README.md
└── LICENSE
```

---

## Skills

### platform-setup
Configure Meta Business Manager credentials and verify API access.

### morning-brief
Daily Meta Ads account health — CPM, frequency, creative fatigue, budget pacing, and anomaly detection.

### waste-detector
Find Meta-specific spend leaks — audience overlap, creative fatigue, placement bleed, frequency violations.

### creative-analyzer
Evaluate ad creative performance — hook rate, hold rate, thumb-stop ratio, fatigue signals, winner/loser classification.

### audience-builder
Design audience strategies — lookalikes, custom audiences, retargeting funnels, exclusion hygiene.

---

## Safety Model

Same protocol as all Channel 47 plugins:

1. Query and analyze first.
2. Preview mutations with `dry_run: true`.
3. Request explicit user approval.
4. Execute with `dry_run: false` only after approval.

---

## Links

- [Channel 47](https://channel47.dev)
- [Build Notes](https://channel47.dev/subscribe)

## License

MIT
