---
name: search-term-verdict
description: >-
  This skill should be used when the user asks to "review search terms",
  "analyze search queries", "find negative keywords", "check search term
  report", "clean up search terms", "search term audit", "find wasted
  spend on search terms", "what are people searching for", or mentions
  search term analysis, n-gram analysis, negative keyword mining, or
  query sculpting.
allowed-tools: mcp__google-ads__query, mcp__google-ads__mutate, mcp__google-ads__list_accounts
---

# Search Term Verdict

Classify paid-search queries into actionable verdicts and produce ready-to-apply negative keyword and promotion recommendations.

## Data Access

This skill uses the plugin's Google Ads MCP tools for live API access:

- `mcp__google-ads__query`: Execute GAQL SELECT queries for term and keyword coverage.
- `mcp__google-ads__mutate`: Preview and apply negative keyword changes.
- `mcp__google-ads__list_accounts`: Confirm account context before running analysis.

Mutation safety flow:

1. Build operations and run `mcp__google-ads__mutate` with `dry_run: true`.
2. Share the preview with rationale and scope.
3. Ask for explicit approval.
4. Re-run with `dry_run: false` only after approval.

## Workflow

### Phase 1: Extract data

1. Run `references/gaql-queries.md` Query A for full coverage.
2. Run Query B for keyword-level mapping in Search campaigns.
3. Keep date range default at `LAST_30_DAYS` unless user requests a different window.
4. Skip rows where `search_term_view.status = EXCLUDED` for actioning, but count them in coverage notes.

### Phase 2: Classify each search term

Assign one verdict per row:

- `NEGATE`: irrelevant or wasteful term.
- `PROMOTE`: high-intent term that should become a dedicated keyword.
- `INVESTIGATE`: ambiguous term requiring user judgment.
- `KEEP`: term is aligned and performing acceptably.

Use this weight order:

1. Conversion and cost efficiency.
2. Semantic relevance to campaign intent.
3. Match type drift signals.
4. Existing exclusion status.
5. Volume significance.

Use `references/verdict-heuristics.md` for edge cases and conflict checks.

### Phase 3: Build output package

Return three sections:

1. Verdict summary table.
2. Negative keyword package grouped by campaign or ad group level.
3. Promotion candidates with suggested ad group placement.

Every recommendation must include rationale and spend/conversion context.

**Negative match type guidance:**

- Use `EXACT` negative when only a specific phrase should be blocked.
- Use `PHRASE` negative when the core phrase is irrelevant regardless of surrounding words (most common choice).
- Avoid `BROAD` negatives unless the single word is unambiguously irrelevant.

**Level guidance:**

- `ad_group` level: mismatch is scoped to one ad group's theme.
- `campaign` level: mismatch applies across the entire campaign.
- Account-level (shared negative list): if exclusions are universal, recommend adding terms to a shared negative keyword list in the Google Ads UI.

### Phase 4: Mutation execution (approval-gated)

1. Build negative keyword operations with `dry_run: true` first.
2. Show preview table to user and request explicit confirmation.
3. Only run with `dry_run: false` after user approval.

## Output format

```markdown
## Search Term Verdict - [Date]
### Account: [Name] ([Customer ID])

**Coverage note:** [hidden search-term caveat]

### Summary
| Verdict | Count | Spend | Notes |
|---|---:|---:|---|

### Negative Keyword Recommendations
| Keyword | Level | Parent | Match Type | 30d Spend | Reason |
|---|---|---|---|---:|---|

### Promotion Candidates
| Search Term | Campaign | Suggested Ad Group | Conv | CPA | Why promote |
|---|---|---|---:|---:|---|

### Investigate
- [Term] - [why human review is required]
```

## Guardrails

- Never apply live negatives without explicit user confirmation.
- Flag potential positive-keyword collisions before recommending negatives.
- Mention search-term privacy threshold and estimated data coverage gap.
- When data volume exceeds 10,000 rows, recommend narrower date/campaign scope.

## References

- `references/gaql-queries.md`
- `references/verdict-heuristics.md`
- `references/google-campaign-management.md`
