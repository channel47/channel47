# Microsoft Ads — Claude Code Plugin

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Microsoft Advertising toolkit — 8 skills for daily monitoring, waste detection, search term analysis, import auditing, placement cleaning, and account scoring. Read-only by design.

Built from managing 25+ ad accounts daily. Part of [channel47](https://channel47.dev), the open-source ecosystem of profession plugins for Claude Code. [Get the newsletter](https://channel47.dev/subscribe) for weekly skill breakdowns from production use.

---

## Install

```bash
/plugin marketplace add channel47/plugins
/plugin install microsoft-ads@channel47
```

---

## Version

Current: **1.0.0**

---

## Configuration

The plugin bundles one MCP server via `.mcp.json`. Set these environment variables in your shell profile:

| Variable | Required |
|----------|----------|
| `BING_ADS_DEVELOPER_TOKEN` | Yes |
| `BING_ADS_CLIENT_ID` | Yes |
| `BING_ADS_REFRESH_TOKEN` | Yes |
| `BING_ADS_CUSTOMER_ID` | Yes |
| `BING_ADS_ACCOUNT_ID` | Yes |

The MCP server installs automatically via `npx` — no separate setup.

---

## What's Inside

```text
microsoft-ads/
├── .claude-plugin/
│   └── plugin.json
├── .mcp.json              # Bing Ads MCP
├── CREDITS.md             # Open source attribution
├── hooks/
│   ├── hooks.json         # SessionStart + Stop only
│   ├── inject-profile.sh
│   └── update-profile.py
├── skills/
│   ├── platform-setup/    # Setup + verification
│   ├── profile-review/    # Profile maintenance
│   ├── morning-brief/     # Daily health check
│   ├── waste-detector/    # 7 Bing-specific waste types
│   ├── search-term-verdict/ # Search term classifier
│   ├── account-scorecard/ # 5-dimension health grade
│   ├── import-auditor/    # Post-Google-import cleanup
│   └── placement-cleaner/ # MSAN publisher exclusions
├── references/
│   ├── bing-queries.md    # Report/query configurations
│   ├── thresholds.md      # Detection thresholds + dollar formulas
│   ├── anomaly-formulas.md # Anomaly detection math
│   ├── import-checklist.md # Post-import checklist
│   └── ui-paths.md        # Microsoft Advertising UI paths
├── README.md
└── LICENSE
```

---

## Skills

### platform-setup
Configure Microsoft Advertising credentials and verify API access. Generates an account profile that all other skills use automatically.

### profile-review
Periodic cleanup of account profile — stale watch list entries, lingering tests, bloated decision logs, outdated targets.

### morning-brief
Daily account-health summary with anomaly detection, budget pacing vs monthly targets, bot traffic monitoring, import drift detection, and prioritized Urgent/Watch/Healthy narrative.

### waste-detector
Finds 7 Bing-specific spend leaks: MSAN enabled, search partners, broad match imports, auto-import overwriting, overnight budget burn, bot traffic, location targeting expanding. Quantifies waste in dollars, ranks by impact, and produces action plans with UI paths.

### search-term-verdict
Classifies search terms into NEGATE/PROMOTE/INVESTIGATE/KEEP verdicts with more aggressive negation thresholds for Bing's worse close variant matching. Produces copy-paste negative keyword lists with match type recommendations.

### account-scorecard
5-dimension health grade (Structure, Quality, Efficiency, Coverage, Hygiene). Monthly lightweight check — references [claude-ads](https://github.com/AgriciDaniel/claude-ads) as companion for quarterly deep audits.

### import-auditor
Post-Google-Ads-import cleanup. Runs a pass/fail checklist covering MSAN, search partners, location targeting, negative keyword gaps, ad scheduling, bid strategy compatibility, and conversion tracking verification.

### placement-cleaner
MSAN publisher exclusion recommendations. Pulls publisher URL performance report, flags low-quality placements, and produces copy-paste exclusion lists with UI paths.

---

## Trust Model

This plugin is **read-only by design**:

- No skill's `allowed-tools` includes any mutation tool
- No mutation validation hooks (they're unnecessary)
- Every actionable finding produces: dollar-impact tables, exact Microsoft Advertising UI paths, and copy-paste artifacts

The plugin reads your account data and produces prioritized action plans. It cannot modify your account.

---

## Try It

- "Set up and verify my Microsoft Ads account."
- "Give me this morning's brief for Bing."
- "Find where I'm wasting Bing budget."
- "Review my Bing search terms and draft negatives."
- "Audit my Google Ads import."
- "Clean up my MSAN placements."
- "Grade my Bing account health."

---

## Links

- [channel47](https://channel47.dev) — open-source profession plugins for Claude Code
- [Build Notes](https://channel47.dev/subscribe) — weekly skill breakdowns from production use
- [MCP Server](https://github.com/channel47/mcps) — the Bing Ads MCP this plugin uses
- [CREDITS.md](./CREDITS.md) — open source attribution

## License

MIT
