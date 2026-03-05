# Google Ads — Claude Code Plugin

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Google Ads toolkit — 9 skills for daily monitoring, waste detection, search term analysis, PMax transparency, account scoring, ad copy analysis, and competitive intel. Read-only by design.

Built from managing 25+ ad accounts daily. Part of [channel47](https://channel47.dev), the open-source ecosystem of profession plugins for Claude Code. [Get the newsletter](https://channel47.dev/subscribe) for weekly skill breakdowns from production use.

---

## Install

```bash
/plugin marketplace add channel47/plugins
/plugin install google-ads@channel47
```

---

## Version

Current: **1.0.0**

---

## Configuration

The plugin bundles one MCP server via `.mcp.json` with `GOOGLE_ADS_READ_ONLY=true`. Set these environment variables in your shell profile:

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
google-ads/
├── .claude-plugin/
│   └── plugin.json
├── .mcp.json              # Google Ads MCP (read-only)
├── CREDITS.md             # Open source attribution
├── hooks/
│   ├── hooks.json         # SessionStart + Stop only
│   ├── inject-profile.sh
│   └── update-profile.py
├── skills/
│   ├── platform-setup/    # Setup + verification
│   ├── profile-review/    # Profile maintenance
│   ├── morning-brief/     # Daily health check
│   ├── waste-detector/    # Spend leak finder
│   ├── search-term-verdict/ # Search term classifier
│   ├── pmax-decoder/      # PMax transparency
│   ├── account-scorecard/ # 5-dimension health grade
│   ├── ad-copy-analyzer/  # RSA performance review
│   └── competitor-intel/  # Auction insights analysis
├── references/
│   ├── gaql-queries.md    # Consolidated GAQL queries
│   ├── thresholds.md      # Detection thresholds + dollar formulas
│   ├── benchmarks.md      # Industry benchmarks
│   ├── anomaly-formulas.md # Anomaly detection math
│   └── ui-paths.md        # Google Ads UI navigation paths
├── README.md
└── LICENSE
```

---

## Skills

### platform-setup
Configure Google Ads credentials and verify API access. Generates an account profile that all other skills use automatically.

### profile-review
Periodic cleanup of account profile — stale watch list entries, lingering tests, bloated decision logs, outdated targets.

### morning-brief
Daily account-health summary with anomaly detection, budget pacing vs monthly targets, and prioritized Urgent/Watch/Healthy narrative.

### waste-detector
Finds 8 types of spend leaks across Google Ads campaigns. Quantifies waste in dollars, ranks by impact, and produces action plans with UI paths.

### search-term-verdict
Classifies search terms into NEGATE/PROMOTE/INVESTIGATE/KEEP verdicts. Produces copy-paste negative keyword lists with match type recommendations.

### pmax-decoder
Cracks open Performance Max campaign transparency — search terms, channel distribution, asset performance, brand traffic detection, and placement review.

### account-scorecard
5-dimension health grade (Structure, Quality, Efficiency, Coverage, Hygiene). Monthly lightweight check — references [claude-ads](https://github.com/AgriciDaniel/claude-ads) as companion for quarterly 60-point deep audits.

### ad-copy-analyzer
RSA asset performance review — ad strength distribution, LOW asset replacement priorities, pinning analysis, headline/description diversity.

### competitor-intel
Auction insights analysis — competitive positioning, impression share trends, overlap rates, and outranking share. References DataForSEO MCP as optional companion.

---

## Trust Model

This plugin is **read-only by design**:

- `GOOGLE_ADS_READ_ONLY=true` is enforced at the MCP server level
- No skill's `allowed-tools` includes any mutation tool
- No mutation validation hooks (they're unnecessary)
- Every actionable finding produces: dollar-impact tables, exact Google Ads UI paths, and copy-paste artifacts

The plugin reads your account data and produces prioritized action plans. It cannot modify your account.

---

## Try It

- "Set up and verify my Google Ads account."
- "Give me this morning's brief."
- "Find where I'm wasting budget."
- "Review my search terms and draft negatives."
- "Decode what my PMax campaign is actually doing."
- "Grade my account health."
- "Analyze my RSA ad copy."
- "Show me my competitive landscape."

---

## Links

- [channel47](https://channel47.dev) — open-source profession plugins for Claude Code
- [Build Notes](https://channel47.dev/subscribe) — weekly skill breakdowns from production use
- [MCP Server](https://github.com/channel47/mcps) — the Google Ads MCP this plugin uses
- [CREDITS.md](./CREDITS.md) — open source attribution

## License

MIT
