---
name: waste-detector
description: >-
  This skill should be used when the user asks to "find waste", "audit my
  account", "where am I wasting money", "account audit", "find wasted
  spend", "check for waste", "money leaks", "account health", "what's
  costing me money", "optimization opportunities", or mentions account
  optimization, spend analysis, waste analysis, or budget efficiency.
allowed-tools: mcp__google-ads__query, mcp__google-ads__mutate, mcp__google-ads__list_accounts
---

# Waste Detector

Scan a Google Ads account for the most common spend leaks and quantify each leak in dollars with an action plan.

## Data Access

This skill uses the plugin's Google Ads MCP tools for live API access:

- `mcp__google-ads__query`: Execute GAQL SELECT queries for waste detection.
- `mcp__google-ads__mutate`: Stage and apply mutation operations.
- `mcp__google-ads__list_accounts`: Validate account visibility before running audits.

Mutation safety flow:

1. Always run `mcp__google-ads__mutate` with `dry_run: true` first.
2. Show exactly what would change.
3. Require explicit user approval.
4. Re-run with `dry_run: false` only after approval.

## Workflow

### Phase 1: Run waste queries

Execute the eight query groups from `references/gaql-queries.md`.

Waste types covered:

1. Non-converting keywords.
2. Low-quality-score keywords still spending.
3. Search campaigns with Display network expansion.
4. Budget-limited campaigns.
5. Broad match without shared negative list coverage.
6. Single-ad ad groups.
7. Enabled campaigns with zero impressions.
8. Semantic mismatch in search terms.

### Phase 2: Quantify impact

Use `references/thresholds.md` for exact detection thresholds and dollar formulas per waste type. Summary:

1. Apply the specific threshold for each waste type (not a single blanket rule).
2. Compute dollar waste using the formula specified per type.
3. Rank all findings by dollar impact descending.
4. Tag severity: `HIGH` (>$500/mo), `MEDIUM` ($100-500), `LOW` ($25-100), `INFO` (<$25).

Use `references/benchmarks.md` for QS-to-CPC pressure multipliers and CTR bands.

### Phase 3: Build remediation package

Map each finding to its remediation action using `references/thresholds.md` remediation mapping. Key patterns:

- **Types 1, 2, 7**: build pause operations and preview with `mcp__google-ads__mutate` dry run.
- **Type 8**: build negative-keyword operations and preview with `mcp__google-ads__mutate` dry run.
- **Types 3, 4, 5**: recommend manual UI changes (cannot be mutated via API).
- **Type 6**: recommend creating additional RSA variants.

All mutations must follow dry-run first semantics. Show preview, get user approval.

## Output format

```markdown
## Waste Report - [Date]
### Account: [Name] ([Customer ID])

**Total Estimated Recoverable Waste: $X,XXX/month**

| # | Waste Type | Monthly Cost | Severity | Action |
|---|---|---:|---|---|

### Detailed Findings
- [Entity], [problem], [dollar impact], [recommended action]

### Ready-to-Apply Changes
- [mutation preview]
```

## Guardrails

- Call out where dollar figures are estimates vs direct spend totals.
- Keep assumptions explicit for model-based calculations.
- Do not run live mutations without explicit user approval.
- Distinguish "true zero" from omitted zero-value GAQL rows.

## References

- `references/gaql-queries.md`
- `references/thresholds.md`
- `references/benchmarks.md`
- `references/google-campaign-management.md`
