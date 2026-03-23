# DTC Google Ads Playbook

A Claude Code plugin that codifies proven Google Ads strategies for DTC brands into reusable skills, commands, and agents. Derived from analysis of a $6M+ Google Ads account generating 16,800+ conversions at $362 avg CPA.

## What's Inside

### Skills (auto-activate on relevant conversations)

- **Campaign Architecture** — PMax-first account structure, audience segmentation, naming conventions, device splits, campaign duplication & scaling
- **Daily Optimization** — tCPA/budget adjustment cadence, performance thresholds, pause/scale decision frameworks, Demand Gen management
- **Ad Copy & Landing Pages** — Headline/description formulas, offer naming, landing page URL architecture with tracking params, negative keyword strategy

### Commands

- `/campaign-audit` — Paste campaign data or point to a file, get a structured diagnosis against the playbook
- `/new-campaign-plan` — Input product/offer details, get a full campaign architecture plan with real ad copy
- `/optimization-checklist` — Generate a daily or weekly optimization checklist for active campaigns

### Agent

- **Performance Analyst** — Reads CSV/XLSX campaign data, cross-references metrics, identifies underperformers, and recommends specific budget/tCPA/pause actions with exact numbers

## Installation

```bash
claude --plugin-dir /path/to/dtc-google-ads-playbook
```

Or copy to your project's plugins directory.

## Usage Examples

**Get a campaign plan for a new DTC brand:**
```
/new-campaign-plan Skincare serum, $49 price point, $30K/day budget, target CPA $45, women 25-55
```

**Audit existing campaign data:**
```
/campaign-audit [paste CSV data or provide file path]
```

**Generate daily checklist:**
```
/optimization-checklist daily
```

**Analyze performance data (triggers analyst agent):**
```
"Analyze my Google Ads export and tell me what to scale and what to pause"
```

## Core Principles

1. **PMax-first** — 85-95% of budget to Performance Max
2. **Audience segmentation** — separate campaigns per persona (women, seniors, moms, men, geo)
3. **Scale via duplication** — clone winners with variations, don't just increase budgets
4. **Device isolation** — phone-exclusion campaigns capture cheaper desktop traffic
5. **Daily optimization** — 100+ budget/bid adjustments per day on large accounts
6. **Small tCPA moves** — $3-$8 increments, never large jumps
7. **Named offers** — create campaign-level offer brands (e.g., "Her Reset 2026")
8. **Systematic naming** — `{platform}-{price}-{audience}-{sequence}-{modifier}`
