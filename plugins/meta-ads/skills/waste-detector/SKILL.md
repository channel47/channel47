---
name: waste-detector
description: >-
  This skill should be used when the user asks to "find Meta waste",
  "audit my Facebook account", "where am I wasting Meta budget",
  "Meta ads audit", "Facebook spend leaks", "Instagram waste",
  "social ads optimization", or mentions Meta Ads waste analysis,
  Facebook budget efficiency, or social ad spend optimization.
allowed-tools: mcp__meta-ads__query, mcp__meta-ads__mutate, mcp__meta-ads__list_accounts
---

# Meta Ads Waste Detector

Scan Meta Ads accounts for spend leaks and quantify each in dollars with an action plan.

## Status

Skeleton — requires `@channel47/meta-ads-mcp` to be built and published before this skill is functional.

## Meta-Specific Waste Types

| # | Waste Type | Signal |
|---|-----------|--------|
| 1 | Audience overlap | Multiple ad sets targeting overlapping audiences, driving up CPM via self-competition |
| 2 | Creative fatigue | Frequency > 3.0 with declining CTR — audience has seen the ad too many times |
| 3 | Placement bleed | Audience Network or low-quality placements consuming disproportionate spend with poor CPA |
| 4 | Non-converting ad sets | Spend above target CPA threshold with zero conversions |
| 5 | Learning phase churn | Ad sets repeatedly entering and exiting learning phase due to budget/targeting changes |
| 6 | Broad targeting without exclusions | Prospecting campaigns missing customer list exclusions |
| 7 | Frequency cap violations | No frequency cap set on reach/awareness campaigns |
| 8 | Stale lookalike seeds | Lookalike audiences based on outdated or small source lists |

## Severity Tags

Same scale as paid-search: `HIGH` (>$500/mo), `MEDIUM` ($100-500), `LOW` ($25-100), `INFO` (<$25).

## Workflow

### Phase 1: Run waste queries
Query Meta Ads API for each waste type signal.

### Phase 2: Quantify impact
Dollar-denominate each finding. Rank by impact across all waste types.

### Phase 3: Build remediation package
Map findings to specific actions (pause, adjust targeting, refresh creative, add exclusions).

## Output format

Same contract as paid-search waste-detector:
```
## Waste Report - [Date]
### Meta Ads: [Name] ([Account ID])
### Detailed Findings
### Ready-to-Apply Changes
```

## Guardrails

- Mutation safety: dry-run first, user approval required
- Creative pause warning: pausing a Meta creative kills its learnings permanently (unlike pausing a keyword)
- Learning phase: do not flag ad sets in learning phase as waste

## References

- `references/` — to be populated when MCP server is built
