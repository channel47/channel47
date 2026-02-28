---
name: audience-builder
description: >-
  This skill should be used when the user asks to "build an audience",
  "create a lookalike", "targeting strategy", "audience recommendations",
  "who should I target", "custom audience setup", "audience overlap check",
  "exclusion lists", "retargeting setup", or mentions Meta audience building,
  Facebook targeting, lookalike audiences, or audience segmentation.
allowed-tools: mcp__meta-ads__query, mcp__meta-ads__list_accounts
---

# Audience Builder

Design and evaluate Meta Ads audience strategies — lookalike modeling, custom audiences, interest stacks, exclusion hygiene, and retargeting funnels.

## Status

Skeleton — requires `@channel47/meta-ads-mcp` to be built and published before this skill is functional.

## Audience Types

| Type | Source | Best For |
|------|--------|----------|
| Custom Audience — Customer List | CRM upload (emails, phones) | Retargeting existing customers, seed for lookalikes |
| Custom Audience — Website | Pixel/CAPI events | Retargeting visitors by funnel stage |
| Custom Audience — Engagement | On-platform actions (video views, page likes) | Warming cold audiences |
| Lookalike | Seeded from custom audience | Prospecting at scale |
| Interest/Behavior | Meta's targeting categories | Cold prospecting without seed data |
| Broad (Advantage+) | Algorithmic, minimal targeting | Letting Meta's algorithm find converters |

## Workflow

### Phase 1: Audit existing audiences

Pull current audience configuration:
- Active custom audiences and their sizes
- Lookalike audiences and their seed quality
- Interest targeting in use
- Exclusion lists applied

### Phase 2: Identify gaps

- Missing exclusions (existing customers not excluded from prospecting)
- Stale seed audiences (not refreshed in 90+ days)
- Audience overlap between ad sets (self-competition)
- Missing retargeting layers (website visitors, video viewers, engagers)

### Phase 3: Recommend audience strategy

Build a layered funnel:
1. **Prospecting**: Lookalikes (1-3%) seeded from best customers by LTV
2. **Interest stacks**: Grouped by theme, not individual interests
3. **Retargeting — warm**: Engagers, video viewers (7-30d)
4. **Retargeting — hot**: Website visitors, cart abandoners (1-7d)
5. **Exclusions**: Existing customers, recent converters (14d), bounced visitors

### Phase 4: Generate implementation plan

For each recommended audience:
- Exact audience definition
- Suggested ad set budget allocation
- Expected audience size
- Refresh cadence

## Output format

```markdown
## Audience Strategy - [Date]
### Account: [Name] ([Account ID])

### Current State
| Audience | Type | Size | Last Updated | Status |

### Gaps Identified
1. [Gap + impact + fix]

### Recommended Funnel
| Layer | Audience | Est. Size | Budget % | Notes |

### Exclusion Checklist
- [ ] Existing customers excluded from prospecting
- [ ] Recent converters (14d) excluded
- [ ] Bounced visitors (<10s) excluded

### Implementation Steps
1. [specific action]
```

## Guardrails

- Minimum audience size: 1,000 for custom audiences, 100 for lookalike seeds
- Note iOS ATT impact on custom audience match rates
- Lookalike quality degrades above 3% — flag if wider is recommended
- Interest targeting is Meta's least durable targeting method — note deprecation risk
- Customer list uploads require consent/compliance — remind user

## References

- `references/` — to be populated when MCP server is built
