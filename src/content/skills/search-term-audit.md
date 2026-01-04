---
title: Search Term Audit
description: Analyze search terms for wasted spend, identify negative keyword opportunities, and surface high-converting queries you should add as exact match.
version: "1.0.0"
category: google-ads
tags:
  - search terms
  - negative keywords
  - wasted spend
  - optimization
tier: free
featured: true
publishedAt: 2025-01-04
---

## What This Skill Does

The Search Term Audit skill analyzes your Google Ads search term reports to find:

- **Wasted spend** — Terms that cost money but never convert
- **Negative keyword candidates** — Irrelevant queries to block
- **Exact match opportunities** — High-converting terms to add as keywords
- **Pattern recognition** — Common modifiers that signal intent (or lack thereof)

## How It Works

When invoked, the skill will:

1. Request access to your Google Ads search term data (via API or export)
2. Analyze performance metrics (cost, conversions, CTR, ROAS)
3. Apply heuristics to categorize each term
4. Generate a prioritized action list

## Sample Output

```
## Search Term Audit Results

### Immediate Action: Block These Terms (Est. $847/mo savings)
- "free [product]" — 47 clicks, $312, 0 conversions
- "[competitor] reviews" — 23 clicks, $189, 0 conversions
- "how to [task] without [product]" — 31 clicks, $256, 0 conversions

### Add as Exact Match (High Converting)
- "[product] for [use case]" — 12 clicks, $89, 8 conversions (67% CVR)
- "best [product] [year]" — 8 clicks, $62, 4 conversions (50% CVR)

### Monitor (Borderline Performance)
- "[product] alternative" — 18 clicks, $142, 1 conversion
```

## Configuration

The skill accepts optional parameters:

- `lookback_days` — How far back to analyze (default: 30)
- `min_cost` — Minimum cost threshold for analysis (default: $10)
- `conversion_goal` — Primary conversion action to optimize for

## Requirements

- Google Ads account with search campaigns
- Search terms data access (via API or exported CSV)
- At least 30 days of data recommended

## Installation

Add this skill to your Claude Code environment:

```bash
claude skills install channel47/search-term-audit
```

Or manually add the skill file to your `.claude/skills/` directory.
