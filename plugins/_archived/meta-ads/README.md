# Meta Ads — Claude Code Plugin

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version: 1.0.0](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://channel47.dev/plugins/meta-ads)

Meta Ads toolkit for Facebook and Instagram — 9 skills for daily monitoring, waste detection, creative fatigue analysis, audience intelligence, and competitive research. Read-only by design.

Part of [channel47](https://channel47.dev), the open-source ecosystem of profession plugins for Claude Code.

---

## Install

Add this plugin to your Claude Code configuration. The plugin bundles [brijr/meta-mcp](https://github.com/brijr/meta-mcp) (44 tools for Meta Ads API) via `.mcp.json`.

### Configuration

Set one environment variable in your shell profile (`~/.zshrc` or `~/.bashrc`):

```bash
export META_ACCESS_TOKEN="your-meta-access-token"
```

That's it. No app ID, no app secret, no account ID required at the environment level. The MCP server uses the access token to discover your accounts.

**How to get a token:**
1. Go to [Meta for Developers — Graph API Explorer](https://developers.facebook.com/tools/explorer/).
2. Add permissions: `ads_read`, `ads_management` (read scope), `read_insights`.
3. Generate a long-lived User or System User token.
4. Add to your shell profile and restart Claude Code.

Run `/platform-setup` to verify access and generate your account profile.

---

## Skills (9)

| Skill | What It Does |
|-------|-------------|
| **platform-setup** | Configure credentials, verify API access, generate account profile |
| **morning-brief** | Daily account health — anomaly detection, budget pacing, Learning Limited flags |
| **waste-detector** | 8 Meta waste types — audience overlap, creative fatigue, placement bleed, non-converting ad sets, learning churn, missing exclusions, frequency violations, stale seeds |
| **creative-fatigue** | Lifecycle classification (Testing/Rising/Peak/Fatiguing/Dead) with days-remaining estimates |
| **creative-audit** | Format x Concept x Angle creative matrix, gap analysis, testing roadmap |
| **account-scorecard** | 5-dimension account grade (Structure, Creative Health, Audience Quality, Efficiency, Tracking) |
| **audience-analyzer** | Audience performance by type, saturation detection, overlap signals, efficiency ranking |
| **competitor-research** | Own account vs benchmarks + Meta Ad Library research guidance |
| **profile-review** | Account profile cleanup — stale watch items, lingering tests, outdated targets |

## Agents (2)

| Agent | What It Does |
|-------|-------------|
| **creative-analyst** | Subagent for parallel creative performance analysis across ad sets |
| **competitor-scout** | Subagent for Meta Ad Library research and competitor creative categorization |

---

## Safety Model

**Read-only by design.** This plugin cannot modify your Meta Ads account. No mutations, no write operations, no budget changes.

Every skill produces:
- Dollar-quantified findings with severity tags (HIGH/MEDIUM/LOW/INFO).
- Exact Meta Ads Manager UI paths for every recommended action.
- Copy-paste artifacts where applicable (audience names, frequency cap values, etc.).

You execute the changes manually in Meta Ads Manager. The plugin gives you the analysis and the action plan.

---

## Account Profile

The plugin maintains an account profile at `profile/account-profile.md`:
- **SessionStart hook** injects the profile into every conversation automatically.
- **Stop hook** updates the profile's watch list and decision log based on session findings.
- Skills read KPI targets, active tests, and watch items from the profile.

Run `/platform-setup` to generate your initial profile, and `/profile-review` periodically to keep it clean.

---

## Structure

```
meta-ads/
├── .claude-plugin/
│   └── plugin.json          # Plugin manifest (v1.0.0)
├── .mcp.json                # brijr/meta-mcp (meta-ads-mcp@^1.7.0)
├── hooks/
│   ├── hooks.json           # SessionStart + Stop hooks
│   ├── inject-profile.sh    # Injects account profile on session start
│   └── update-profile.py    # Updates profile watch list on session end
├── skills/
│   ├── platform-setup/      # Setup and verification
│   ├── morning-brief/       # Daily health check
│   ├── waste-detector/      # 8-type waste analysis
│   ├── creative-fatigue/    # Creative lifecycle classification
│   ├── creative-audit/      # Creative mix and gap analysis
│   ├── account-scorecard/   # 5-dimension account grading
│   ├── audience-analyzer/   # Audience performance and saturation
│   ├── competitor-research/  # Competitive intelligence
│   └── profile-review/      # Profile maintenance
├── agents/
│   ├── creative-analyst.md  # Parallel creative analysis subagent
│   └── competitor-scout.md  # Ad Library research subagent
├── references/
│   ├── fatigue-model.md     # Creative fatigue lifecycle model and formulas
│   ├── waste-queries.md     # Query templates per waste type
│   ├── thresholds.md        # Detection thresholds for all skills
│   ├── benchmarks.md        # 2026 Meta benchmarks by objective/vertical
│   └── ui-paths.md          # Meta Ads Manager UI paths for every action
├── CREDITS.md               # Open source attribution
├── README.md
└── LICENSE
```

---

## MCP Server

This plugin bundles [brijr/meta-mcp](https://github.com/brijr/meta-mcp) (npm: `meta-ads-mcp`), which provides 44 tools for the Meta Ads API. The MCP runs locally via stdio — no remote servers, no data leaves your machine except direct Meta API calls.

Pinned version: `meta-ads-mcp@^1.7.0`

---

## Companion Tools

- **[claude-ads](https://github.com/AgriciDaniel/claude-ads)** — 186 cross-platform audit checks (46 Meta-specific). Recommended as a quarterly deep audit companion to the `account-scorecard` skill.
- **[trypeggy/facebook-ads-library-mcp](https://github.com/trypeggy/facebook-ads-library-mcp)** — Optional companion MCP for automated Ad Library queries. Referenced by the `competitor-research` skill and `competitor-scout` agent.

---

## Links

- [channel47](https://channel47.dev)
- [Plugin Docs](https://channel47.dev/plugins/meta-ads)
- [Build Notes (Newsletter)](https://channel47.dev/subscribe)
- [brijr/meta-mcp](https://github.com/brijr/meta-mcp) — The underlying MCP server

## License

MIT
