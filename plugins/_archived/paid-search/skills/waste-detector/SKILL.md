---
name: waste-detector
description: >-
  This skill should be used when the user asks to "find search waste",
  "audit my search account", "where am I wasting search budget",
  "paid search audit", "find wasted spend", "check for waste",
  "search money leaks", "paid search health", "what's costing me money
  in search", "optimization opportunities", or mentions paid search
  optimization, search spend analysis, or budget efficiency.
allowed-tools: mcp__google-ads__query, mcp__google-ads__mutate, mcp__google-ads__list_accounts, mcp__bing-ads__report, mcp__bing-ads__query, mcp__bing-ads__list_accounts
---

# Paid Search Waste Detector

Scan Google Ads and Bing Ads paid search accounts for the most common spend leaks and quantify each leak in dollars with an action plan.

## Account Context

Read `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md` at the start of every run.
If it exists:
- Use known account IDs — skip `list_accounts` discovery.
- Apply KPI targets as anomaly detection thresholds (e.g., flag CPA > target CPA).
- Note active tests when interpreting performance shifts.
- Check watch list for follow-up items from prior sessions.
If it doesn't exist, fall back to `list_accounts` and suggest running `platform-setup`.

## Data Access

### Google Ads

- `mcp__google-ads__query`: Execute GAQL SELECT queries for waste detection.
- `mcp__google-ads__mutate`: Stage and apply mutation operations.
- `mcp__google-ads__list_accounts`: Validate account visibility before running audits.

### Bing Ads

- `mcp__bing-ads__report`: Generate performance reports for waste analysis.
- `mcp__bing-ads__query`: Query campaign structure (campaigns, ad groups, keywords, ads).
- `mcp__bing-ads__list_accounts`: Validate account access.

### Platform detection

Follow the same pattern as morning-brief: try both platforms, run whichever responds, gracefully skip the other.

### Mutation safety flow (Google only — Bing MCP does not yet support mutations)

1. Always run `mcp__google-ads__mutate` with `dry_run: true` first.
2. Show exactly what would change.
3. Require explicit user approval.
4. Re-run with `dry_run: false` only after approval.

For Bing waste findings, present recommendations as manual action items (no automated mutations available yet).

## Workflow

### Phase 1: Run waste queries

#### Google Ads

Execute the eight query groups from `references/gaql-queries.md`.

#### Bing Ads

Execute the equivalent Bing queries from `references/bing-queries.md`.

Waste types covered (both platforms where data is available):

| # | Waste Type | Google | Bing |
|---|-----------|--------|------|
| 1 | Non-converting keywords | GAQL query | keyword report |
| 2 | Low-quality-score keywords still spending | GAQL query | keyword report (QualityScore column) |
| 3 | Search campaigns with Display network expansion | GAQL query | N/A (Bing doesn't have network expansion toggle) |
| 4 | Budget-limited campaigns | GAQL query | campaign query (status + budget) |
| 5 | Broad match without shared negative list coverage | GAQL query | keyword query (match type check) |
| 6 | Single-ad ad groups | GAQL query | ads query per ad group |
| 7 | Enabled campaigns with zero impressions | GAQL query | campaign report (filter Impressions = 0) |
| 8 | Semantic mismatch in search terms | GAQL query | search_query report |

### Phase 2: Quantify impact

Use `references/thresholds.md` for exact detection thresholds and dollar formulas per waste type. Summary:

1. Apply the specific threshold for each waste type (not a single blanket rule).
2. Compute dollar waste using the formula specified per type.
3. Rank all findings by dollar impact descending, **across both platforms**.
4. Tag severity: `HIGH` (>$500/mo), `MEDIUM` ($100-500), `LOW` ($25-100), `INFO` (<$25).

Use `references/benchmarks.md` for QS-to-CPC pressure multipliers and CTR bands. These benchmarks apply to both Google and Bing (industry-standard metrics).

### Phase 3: Build remediation package

Map each finding to its remediation action using `references/thresholds.md` remediation mapping.

#### Google Ads (automated mutations available)

- **Types 1, 2, 7**: build pause operations and preview with `mcp__google-ads__mutate` dry run.
- **Type 8**: build negative-keyword operations and preview with `mcp__google-ads__mutate` dry run.
- **Types 3, 4, 5**: recommend manual UI changes (cannot be mutated via API).
- **Type 6**: recommend creating additional RSA variants.

All mutations must follow dry-run first semantics. Show preview, get user approval.

#### Bing Ads (manual recommendations only)

All Bing waste findings are presented as actionable recommendations with specific steps to take in the Microsoft Advertising UI. Format each as: entity name, problem, dollar impact, and the exact UI path to fix it.

## Output format

```markdown
## Waste Report - [Date]

### Google Ads: [Name] ([Customer ID])
**Estimated Recoverable Waste: $X,XXX/month**

| # | Waste Type | Monthly Cost | Severity | Action |
|---|---|---:|---|---|

### Bing Ads: [Name] ([Account ID])
**Estimated Recoverable Waste: $X,XXX/month**

| # | Waste Type | Monthly Cost | Severity | Action |
|---|---|---:|---|---|

### Cross-Platform Summary
**Total Recoverable Waste: $X,XXX/month** (Google: $X,XXX + Bing: $X,XXX)

### Detailed Findings
- **[Google/Bing]** [Entity], [problem], [dollar impact], [recommended action]

### Ready-to-Apply Changes (Google Ads)
- [mutation preview]

### Manual Action Items (Bing Ads)
- [recommendation with UI path]
```

## Guardrails

- Call out where dollar figures are estimates vs direct spend totals.
- Keep assumptions explicit for model-based calculations.
- Do not run live mutations without explicit user approval.
- Distinguish "true zero" from omitted zero-value GAQL rows.
- **Bing limitations**: Note that Bing waste findings cannot be auto-remediated. Present clear manual steps.

## Profile Maintenance

After completing analysis, if `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md` exists:
1. Update Watch List with any new anomalies flagged in this run.
2. Update Active Tests if user mentioned starting or completing a test.
3. Append to Decision Log if actions were taken (pauses, negatives added, etc.).
4. Update "Last updated" date.
Present proposed profile changes to the user before writing.

## References

- `references/gaql-queries.md`
- `references/bing-queries.md`
- `references/thresholds.md`
- `references/benchmarks.md`
- `references/google-campaign-management.md`
