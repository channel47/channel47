---
name: morning-brief
description: >-
  This skill should be used when the user asks for a "Meta morning brief",
  "Facebook ads daily check", "how are my Meta campaigns doing",
  "Instagram ads performance", "Meta account health", "social ads daily
  summary", or mentions Meta Ads monitoring, Facebook campaign health,
  or social ads anomaly detection.
allowed-tools: mcp__meta-ads__query, mcp__meta-ads__list_accounts
---

# Meta Ads Morning Brief

Produce a daily, prioritized account-health narrative for Meta Ads (Facebook + Instagram) with actionable items.

## Status

Skeleton — requires `@channel47/meta-ads-mcp` to be built and published before this skill is functional.

## Key Metrics (differ from paid search)

- **CPM** (cost per thousand impressions) — primary cost metric
- **Frequency** — ad fatigue signal (flag when >3.0 in 7d)
- **CTR** — click-through rate
- **CPA / ROAS** — conversion efficiency
- **Relevance Score / Quality Ranking** — Meta's ad quality indicators
- **Hook Rate** — % of video viewers past 3 seconds
- **ThruPlay Rate** — % of video viewers to completion

## Workflow

### Phase 1: Collect data

Query Meta Ads API for:
1. Campaign daily performance (30d) — spend, impressions, CPM, clicks, CTR, conversions, CPA, ROAS
2. Ad set frequency and delivery status
3. Ad-level performance with creative breakdown
4. Account-level spend pacing

### Phase 2: Detect anomalies

Same anomaly detection framework as paid-search:
- Baseline: 7d and 30d windows
- Flag when `|deviation_pct| > 0.20` AND `|dollar_impact| > $10`
- Additional Meta-specific flag: frequency > 3.0 in any ad set

### Phase 3: Budget pacing

- Daily budget and lifetime budget tracking
- Campaign budget optimization (CBO) vs ad set budgets
- Flag overpacing (>1.10) and underpacing (<0.85)

### Phase 4: Draft prioritized narrative

Structure: Urgent / Watch / Healthy with platform label and concrete next actions.

## Output format

Same contract as paid-search morning-brief:
```
## Morning Brief - [Date]
### Platforms
### Urgent
### Watch
### Healthy
### Notes
```

## Guardrails

- Creative fatigue: flag when frequency > 3.0 and CTR declining
- Attribution window: note Meta's default 7-day click / 1-day view window
- iOS privacy impact: note potential underreporting from ATT opt-outs
- Learning phase: do not flag campaigns in learning phase (<50 conversions/week) as underperforming

## References

- `references/` — to be populated when MCP server is built
