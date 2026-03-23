---
name: search-term-verdict
description: >-
  This skill should be used when the user asks to "review search terms",
  "analyze search queries", "find negative keywords", "check search term
  report", "clean up search terms", "search term audit", "find wasted
  spend on search terms", "what are people searching for", or mentions
  search term analysis, n-gram analysis, negative keyword mining, or
  query sculpting.
allowed-tools: mcp__google-ads__query, mcp__google-ads__mutate, mcp__google-ads__list_accounts, mcp__bing-ads__report, mcp__bing-ads__query, mcp__bing-ads__list_accounts
---

# Search Term Verdict

Classify paid-search queries into actionable verdicts across Google Ads and Bing Ads and produce ready-to-apply negative keyword and promotion recommendations.

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

- `mcp__google-ads__query`: Execute GAQL SELECT queries for term and keyword coverage.
- `mcp__google-ads__mutate`: Preview and apply negative keyword changes.
- `mcp__google-ads__list_accounts`: Confirm account context before running analysis.

### Bing Ads

- `mcp__bing-ads__report`: Generate search query performance reports.
- `mcp__bing-ads__query`: Query keyword structure for match-type context.
- `mcp__bing-ads__list_accounts`: Confirm account access.

### Platform detection

Try both platforms. Run whichever responds. If only one is configured, analyze that platform alone.

### Mutation safety flow (Google only)

1. Build operations and run `mcp__google-ads__mutate` with `dry_run: true`.
2. Share the preview with rationale and scope.
3. Ask for explicit approval.
4. Re-run with `dry_run: false` only after approval.

For Bing findings, present negative keyword recommendations as manual action items.

## Workflow

### Phase 1: Extract data

#### Google Ads

1. Run `references/gaql-queries.md` Query A for full coverage.
2. Run Query B for keyword-level mapping in Search campaigns.
3. Keep date range default at `LAST_30_DAYS` unless user requests a different window.
4. Skip rows where `search_term_view.status = EXCLUDED` for actioning, but count them in coverage notes.

#### Bing Ads

1. Run the search query report from `references/bing-queries.md`.
2. Run the keyword structure query for match-type context.
3. Default date range: `Last30Days`.

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

The verdict logic applies identically to both platforms. Classify Google and Bing search terms using the same heuristics.

### Phase 3: Build output package

Return three sections per platform:

1. Verdict summary table.
2. Negative keyword package grouped by campaign or ad group level.
3. Promotion candidates with suggested ad group placement.

Every recommendation must include rationale and spend/conversion context.

**Cross-platform insight**: If the same search term appears on both Google and Bing, note it. A term that wastes money on both platforms is a higher-confidence NEGATE. A term that converts on one but not the other may indicate platform-specific intent differences.

**Negative match type guidance:**

- Use `EXACT` negative when only a specific phrase should be blocked.
- Use `PHRASE` negative when the core phrase is irrelevant regardless of surrounding words (most common choice).
- Avoid `BROAD` negatives unless the single word is unambiguously irrelevant.

**Level guidance:**

- `ad_group` level: mismatch is scoped to one ad group's theme.
- `campaign` level: mismatch applies across the entire campaign.
- Account-level (shared negative list): if exclusions are universal, recommend adding terms to a shared negative keyword list in the platform's UI.

### Phase 4: Mutation execution (approval-gated)

#### Google Ads

1. Build negative keyword operations with `dry_run: true` first.
2. Show preview table to user and request explicit confirmation.
3. Only run with `dry_run: false` after user approval.

#### Bing Ads

Present Bing negative keyword recommendations as manual action items with the specific campaign/ad group and match type. Note: Bing MCP does not yet support mutations.

## Output format

```markdown
## Search Term Verdict - [Date]

### Google Ads: [Name] ([Customer ID])

**Coverage note:** [hidden search-term caveat]

#### Summary
| Verdict | Count | Spend | Notes |
|---|---:|---:|---|

#### Negative Keyword Recommendations
| Keyword | Level | Parent | Match Type | 30d Spend | Reason |
|---|---|---|---|---:|---|

#### Promotion Candidates
| Search Term | Campaign | Suggested Ad Group | Conv | CPA | Why promote |
|---|---|---|---:|---:|---|

### Bing Ads: [Name] ([Account ID])

**Coverage note:** [hidden search-term caveat]

#### Summary
| Verdict | Count | Spend | Notes |
|---|---:|---:|---|

#### Negative Keyword Recommendations (Manual)
| Keyword | Level | Parent | Match Type | 30d Spend | Reason |
|---|---|---|---|---:|---|

#### Promotion Candidates
| Search Term | Campaign | Suggested Ad Group | Conv | CPA | Why promote |
|---|---|---|---:|---:|---|

### Cross-Platform Patterns
- [terms appearing on both platforms with divergent performance]

### Investigate
- [Term] - [platform] - [why human review is required]
```

## Guardrails

- Never apply live negatives without explicit user confirmation.
- Flag potential positive-keyword collisions before recommending negatives.
- Mention search-term privacy threshold and estimated data coverage gap.
- When data volume exceeds 10,000 rows, recommend narrower date/campaign scope.
- **Bing limitations**: Note that Bing negative keyword recommendations require manual implementation.

## References

- `references/gaql-queries.md`
- `references/bing-queries.md`
- `references/verdict-heuristics.md`
- `references/google-campaign-management.md`
