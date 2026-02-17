# Media Buyer — Claude Code Plugin

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Operational paid-search toolkit for Google Ads and Bing Ads with MCP-native workflows for setup, reporting, analysis, and guarded mutations.

Built from managing 25+ ad accounts daily. Part of [Channel 47](https://channel47.dev), the open-source ecosystem of profession plugins for Claude Code. [Get the newsletter](https://channel47.dev/subscribe) for weekly skill breakdowns from production use.

---

## Install

```bash
/plugin marketplace add channel47/channel47
/plugin install media-buyer@channel47
```

---

## Version

Current: **6.0.0**

---

## Configuration

The plugin bundles Google Ads MCP via `.mcp.json`. Set these environment variables in your shell profile:

| Variable | Required |
|----------|----------|
| `GOOGLE_ADS_DEVELOPER_TOKEN` | Yes |
| `GOOGLE_ADS_CLIENT_ID` | Yes |
| `GOOGLE_ADS_CLIENT_SECRET` | Yes |
| `GOOGLE_ADS_REFRESH_TOKEN` | Yes |
| `GOOGLE_ADS_LOGIN_CUSTOMER_ID` | For MCC accounts |

The MCP server installs automatically via `npx` — no separate setup.

---

## What's Inside

```text
media-buyer/
├── .claude-plugin/
│   └── plugin.json
├── .mcp.json
├── hooks/
│   ├── hooks.json
│   └── validate-mutations.py
├── skills/
│   ├── platform-setup/
│   ├── morning-brief/
│   ├── waste-detector/
│   ├── search-term-verdict/
│   └── pmax-decoder/
├── tests/
├── README.md
└── LICENSE
```

---

## Skills

### platform-setup

Setup and verification for Google Ads and Bing Ads credentials. Validates API access via `mcp__google-ads__list_accounts`.

### morning-brief

Daily account-health summary from GAQL queries via `mcp__google-ads__query`. Flags anomalies, pacing issues, and budget drift.

### waste-detector

Finds high-impact spend leaks and prepares remediation actions using `mcp__google-ads__query` and `mcp__google-ads__mutate` (dry-run first).

### search-term-verdict

Classifies search terms and builds negative keyword packages. Uses `mcp__google-ads__query` with approval-gated `mcp__google-ads__mutate`.

### pmax-decoder

Cracks open Performance Max campaign transparency data. Analyzes asset performance, audience signals, and search themes via `mcp__google-ads__query`.

---

## Safety Model

Every write operation follows the same protocol:

1. Query and analyze first.
2. Preview mutations with `dry_run: true`.
3. Request explicit user approval.
4. Execute with `dry_run: false` only after approval.

`hooks/validate-mutations.py` intercepts `mcp__google-ads__mutate` to enforce this.

---

## Try It

- "Set up and verify my Google Ads access."
- "Give me this morning's account brief."
- "Find where I'm wasting budget this month."
- "Review search terms and draft negatives."
- "Decode what my PMax campaign is actually doing."

---

## Links

- [Channel 47](https://channel47.dev) — open-source profession plugins for Claude Code
- [Build Notes Newsletter](https://channel47.dev/subscribe) — weekly skill breakdowns from production use
- [MCP Servers](https://github.com/channel47/mcps) — the Google Ads MCP this plugin uses
- [Build Your First Skill](https://channel47.dev/build) — interactive skill builder

## License

MIT
