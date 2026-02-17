---
name: search-term-verdict
description: >-
  This skill should be used when the user asks to "review search terms",
  "analyze search queries", "find negative keywords", "check search term
  report", "clean up search terms", "search term audit", "find wasted
  spend on search terms", "what are people searching for", or mentions
  search term analysis, n-gram analysis, negative keyword mining, or
  query sculpting.
---

# Search Term Verdict

Classify paid-search queries into actionable verdicts and produce ready-to-apply
negative keyword and promotion recommendations.

## Foundation Dependency

This skill depends on `skills/ad-platform-connection` for auth, GAQL execution,
and mutations. Scripts live in that skill's directory — add it to `sys.path`
before importing:

```python
import sys, os
skill_root = os.path.join(os.environ.get("CLAUDE_PLUGIN_ROOT", "."), "skills", "ad-platform-connection")
sys.path.insert(0, skill_root)

from scripts.google.auth import get_auth
from scripts.google.report import pull_report
from scripts.google.mutate import add_negative_keywords, execute_mutation
```

## Workflow

### Phase 1: Extract data

1. Run `references/gaql-queries.md` Query A for full coverage.
2. Run Query B for keyword-level mapping in Search campaigns.
3. Keep date range default at `LAST_30_DAYS` unless user requests a different
   window.
4. Skip rows where `search_term_view.status = EXCLUDED` for actioning, but count
   them in coverage notes.

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
- Use `PHRASE` negative when the core phrase is irrelevant regardless of surrounding
  words (most common choice).
- Avoid `BROAD` negatives unless the single word is unambiguously irrelevant — broad
  negatives block any query containing that word.

**Level guidance:**

- `ad_group` level: mismatch is scoped to one ad group's theme.
- `campaign` level: mismatch applies across the entire campaign.
- Account-level (shared negative list): `add_negative_keywords()` does not support
  account-level negatives. For universal exclusions, recommend the user add terms to
  a shared negative keyword list via the Google Ads UI and note the limitation.

### Phase 4: Mutation execution (approval-gated)

1. Build draft mutations with `dry_run=True` first:

```python
result = add_negative_keywords(
    client, customer_id,
    keywords=[{"text": "free widgets", "match_type": "PHRASE"}],
    level="campaign",       # or "ad_group"
    parent_id=campaign_id,  # campaign or ad_group ID (numeric)
    dry_run=True,
)
```

2. Show preview table to user and request explicit confirmation.
3. Only run with `dry_run=False` after user approval.

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
