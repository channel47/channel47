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

Current: **6.1.0**

---

## Configuration

The plugin bundles two MCP servers via `.mcp.json`. Set these environment variables in your shell profile:

### Google Ads (required for Google features)

| Variable | Required |
|----------|----------|
| `GOOGLE_ADS_DEVELOPER_TOKEN` | Yes |
| `GOOGLE_ADS_CLIENT_ID` | Yes |
| `GOOGLE_ADS_CLIENT_SECRET` | Yes |
| `GOOGLE_ADS_REFRESH_TOKEN` | Yes |
| `GOOGLE_ADS_LOGIN_CUSTOMER_ID` | For MCC accounts |

### Bing Ads (required for Bing features)

| Variable | Required |
|----------|----------|
| `BING_ADS_DEVELOPER_TOKEN` | Yes |
| `BING_ADS_CLIENT_ID` | Yes |
| `BING_ADS_CLIENT_SECRET` | Yes |
| `BING_ADS_REFRESH_TOKEN` | Yes |
| `BING_ADS_CUSTOMER_ID` | For manager accounts |
| `BING_ADS_ACCOUNT_ID` | Default account |

Both MCP servers install automatically via `npx` — no separate setup. Configure one platform or both — skills gracefully adapt to whatever's available.

---

## What's Inside

```text
media-buyer/
├── .claude-plugin/
│   └── plugin.json
├── .mcp.json              # Google Ads + Bing Ads MCP servers
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

Setup and verification for Google Ads and Bing Ads credentials. Validates API access via `mcp__google-ads__list_accounts` and `mcp__bing-ads__list_accounts`.

### morning-brief

Cross-platform daily account-health summary. Pulls data from both Google and Bing, detects anomalies, assesses budget pacing, and produces a unified Urgent/Watch/Healthy narrative.

### waste-detector

Finds high-impact spend leaks across Google and Bing. Quantifies waste in dollars, ranks by impact, and prepares remediation — automated mutations for Google, manual action items for Bing.

### search-term-verdict

Classifies search terms from both platforms into NEGATE/PROMOTE/INVESTIGATE/KEEP verdicts. Builds negative keyword packages with cross-platform pattern detection (same term wasting money on both platforms = high-confidence NEGATE).

### pmax-decoder

Cracks open Performance Max campaign transparency data. Google Ads only (PMax is a Google product). Analyzes search terms, channel distribution, asset performance, brand traffic, and placements.

---

## Safety Model

Every write operation follows the same protocol:

1. Query and analyze first.
2. Preview mutations with `dry_run: true`.
3. Request explicit user approval.
4. Execute with `dry_run: false` only after approval.

`hooks/validate-mutations.py` intercepts both `mcp__google-ads__mutate` and `mcp__bing-ads__mutate` to enforce this.

Bing Ads MCP is currently read-only (query + report). Bing mutation support will be added in a future release.

---

## Try It

- "Set up and verify my Google and Bing accounts."
- "Give me this morning's account brief."
- "Find where I'm wasting budget across all platforms."
- "Review search terms and draft negatives for Google and Bing."
- "Decode what my PMax campaign is actually doing."

---

## Links

- [Channel 47](https://channel47.dev) — open-source profession plugins for Claude Code
- [Build Notes](https://channel47.dev/subscribe) — weekly skill breakdowns from production use
- [MCP Servers](https://github.com/channel47/mcps) — the Google Ads and Bing Ads MCPs this plugin uses
- [Build Your First Skill](https://channel47.dev/build) — interactive skill builder
- [X](https://x.com/ctrlswing) / [LinkedIn](https://www.linkedin.com/in/jackson-d-9979a7a0/) / [GitHub](https://github.com/channel47)

## License

MIT
