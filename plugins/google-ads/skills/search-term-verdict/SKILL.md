---
name: search-term-verdict
description: >-
  This skill should be used when the user asks to "review search terms",
  "find negative keywords", "check search term report",
  "clean up search terms", "what are people searching for",
  "pull my search terms", "SQR", "which search terms are wasting money",
  "irrelevant searches", "bad search terms",
  "what queries am I showing for",
  or mentions search term analysis, n-gram analysis, negative keyword mining,
  query sculpting, or search term triage.
allowed-tools: mcp__google-ads__query, mcp__google-ads__list_accounts
---

# Search Term Verdict — Google Ads

Classify Google Ads search queries into actionable verdicts and produce ready-to-paste negative keyword lists with UI paths for implementation.

**Read-only by design.** This skill does not modify your account. All negative keyword and promotion recommendations are delivered as copy-paste artifacts and Google Ads UI navigation paths.

## Account Context

Read `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md` at the start of every run.
If it exists:
- Use known account IDs -- skip `list_accounts` discovery.
- Apply KPI targets as anomaly detection thresholds (e.g., flag CPA > target CPA).
- Note active tests when interpreting performance shifts.
- Check watch list for follow-up items from prior sessions.
If it doesn't exist, fall back to `list_accounts` and suggest running `platform-setup`.

## Data Access

- `mcp__google-ads__query`: Execute GAQL SELECT queries for term and keyword coverage.
- `mcp__google-ads__list_accounts`: Confirm account context before running analysis.

## Agent Acceleration

When the search term report contains more than 1000 rows, spawn the `search-term-classifier` agent to classify terms in parallel batches. Pass search term rows with metrics in batches of ~500 and collect consolidated verdicts with n-gram analysis. For reports with 1000 or fewer rows, classify sequentially (no agent needed).

## Workflow

### Phase 1: Extract data

1. Run `references/gaql-queries.md` Query A for full search term coverage.
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
- Account-level (shared negative list): if exclusions are universal, recommend adding terms to a shared negative keyword list.

**N-gram analysis:**

When search term volume is high:

1. Build 2-gram and 3-gram frequency tables.
2. Rank grams by total spend and zero-conversion spend.
3. Use high-cost recurring grams to accelerate negative mining candidates.
4. Present top n-grams as a separate section to inform bulk negative decisions.

N-gram output should inform suggestions, not replace row-level judgment.

### Phase 4: Produce action artifacts

Instead of executing mutations, produce ready-to-use artifacts:

#### Copy-paste negative keyword lists

Group negatives by match type for easy pasting into Google Ads:

```
-- PHRASE match negatives (campaign: [Campaign Name]) --
"term one"
"term two"
"term three"

-- EXACT match negatives (campaign: [Campaign Name]) --
[specific query one]
[specific query two]
```

#### UI paths for adding negatives

**At campaign level:**
`Google Ads > Campaigns > [Campaign Name] > Keywords > Negative keywords > + > paste keywords > select 'Campaign' level > Save`

**At ad group level:**
`Google Ads > Campaigns > [Campaign Name] > Ad Groups > [Ad Group Name] > Keywords > Negative keywords > + > paste keywords > select 'Ad group' level > Save`

**Via shared negative keyword list:**
`Google Ads > Tools & Settings > Shared Library > Negative keyword lists > [list name] > + Keywords > paste list > Save`
Then apply to campaigns:
`Google Ads > Campaigns > [Campaign Name] > Settings > Negative keyword lists > + > select list > Save`

#### Promotion candidate actions

For PROMOTE verdicts, provide:
- Recommended keyword text and match type.
- Target ad group name.
- UI path: `Google Ads > Campaigns > [Campaign Name] > Ad Groups > [Ad Group Name] > Keywords > + > enter keyword > select match type > Save`

## Output format

```markdown
## Search Term Verdict - [Date]

### Google Ads: [Name] ([Customer ID])

**Coverage note:** [hidden search-term caveat, data volume, date range]

#### Summary
| Verdict | Count | Spend | Notes |
|---|---:|---:|---|

#### Top N-Grams (by wasted spend)
| N-Gram | Occurrences | Total Spend | Conversions | Suggested Action |
|---|---:|---:|---:|---|

#### Negative Keyword Recommendations
| Keyword | Level | Parent | Match Type | 30d Spend | Reason |
|---|---|---|---|---:|---|

#### Copy-Paste Negative Lists

**Campaign: [Campaign Name]**
```
-- PHRASE match --
"term"
```

**Shared List: [Suggested List Name]**
```
-- PHRASE match --
"universal negative"
```

#### Promotion Candidates
| Search Term | Campaign | Suggested Ad Group | Conv | CPA | Why promote |
|---|---|---|---:|---:|---|

#### Investigate
| Term | Campaign | 30d Spend | Conv | Why review needed |
|---|---|---:|---:|---|
```

## Guardrails

- Flag potential positive-keyword collisions before recommending negatives.
- Mention search-term privacy threshold and estimated data coverage gap.
- When data volume exceeds 10,000 rows, recommend narrower date/campaign scope.
- **Read-only**: This skill produces copy-paste artifacts and UI paths only. No account modifications are made.

## References

- `references/gaql-queries.md`
- `references/verdict-heuristics.md`
