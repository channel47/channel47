---
name: search-term-verdict
description: >-
  This skill should be used when the user asks to "review Bing search terms",
  "find Bing negative keywords", "check Bing search term report",
  "clean up search terms", "what are people searching for on Bing",
  "pull my Bing search terms", "Bing SQR", "irrelevant Bing searches",
  "what queries am I showing for on Bing",
  or mentions Bing search term analysis, n-gram analysis,
  negative keyword mining, query sculpting, or search term triage
  for Microsoft Advertising.
allowed-tools: mcp__bing-ads__report, mcp__bing-ads__query, mcp__bing-ads__list_accounts
---

# Search Term Verdict — Microsoft Ads

Classify Microsoft Advertising search queries into actionable verdicts and produce ready-to-paste negative keyword lists and promotion recommendations. Uses more aggressive negation thresholds than Google due to Bing's worse close variant matching.

## Account Context

Read `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md` at the start of every run.
If it exists:
- Use known account IDs -- skip `list_accounts` discovery.
- Apply KPI targets as verdict thresholds (e.g., flag CPA > target CPA).
- Note active tests when interpreting performance shifts.
- Check watch list for follow-up items from prior sessions.
If it doesn't exist, fall back to `list_accounts` and suggest running `platform-setup`.

## Data Access

- `mcp__bing-ads__report`: Generate search query performance reports.
- `mcp__bing-ads__query`: Query keyword structure for match-type context.
- `mcp__bing-ads__list_accounts`: Confirm account access.

Use report configurations from `references/bing-queries.md` (STV- prefixed queries).

### Connection verification

1. If the profile has account IDs, use them directly.
2. Otherwise, run `mcp__bing-ads__list_accounts` to discover accounts.
3. If it fails, report the connection failure and suggest running `platform-setup`.

## Workflow

### Phase 1: Extract data

1. Run **STV-A**: Search query performance report (30d, Summary aggregation) from `references/bing-queries.md`.
2. Run **STV-B**: Keyword structure query per ad group for match-type context.
3. Default date range: `Last30Days`. Respect user-specified windows.
4. Bing does not flag excluded terms in the search query report. Note this gap in coverage.

### Phase 2: Classify each search term

Assign one verdict per row:

- `NEGATE`: irrelevant or wasteful term.
- `PROMOTE`: high-intent term that should become a dedicated keyword.
- `INVESTIGATE`: ambiguous term requiring user judgment.
- `KEEP`: term is aligned and performing acceptably.

#### Bing-specific thresholds (more aggressive than Google)

Bing's close variant matching is less precise than Google's, which means:
- More irrelevant queries slip through on the same keyword set.
- Negation thresholds should be tighter to compensate.

| Verdict | Threshold (Bing) | Threshold (Google equivalent) | Why different |
|---------|-----------------|------------------------------|---------------|
| NEGATE (spend) | Spend >= $15 with 0 conversions | Spend >= $25 with 0 conversions | Lower threshold because Bing close variants are worse |
| NEGATE (semantic) | Any spend on clearly irrelevant term | Same | Same standard |
| PROMOTE | >= 2 conversions AND CPA <= 80% of target | >= 2 conversions AND CPA <= target | More conservative to account for Bing conversion attribution |
| INVESTIGATE | Spend $5-$15 with 0 conversions | Spend $10-$25 with 0 conversions | Lower band to catch Bing drift earlier |

Use this weight order for classification:

1. Conversion and cost efficiency.
2. Semantic relevance to campaign intent.
3. Match type drift signals (especially important on Bing -- broad match triggers more aggressively).
4. Volume significance.

### Phase 3: Match type drift analysis

Bing-specific: Flag search terms where the triggering keyword's match type created obvious drift:

- **Broad match drift**: Search term has 0 words in common with the triggering keyword.
- **Phrase match drift**: Search term changes the meaning of the keyword phrase.
- **Close variant overreach**: Search term is a "close variant" that is semantically different from the keyword.

For each drift finding, note the triggering keyword, its match type, and the actual search term. This informs whether the fix is a negative keyword or a match type change on the source keyword.

### Phase 4: Build output package

Return three sections:

1. **Verdict summary table** -- counts and spend by verdict.
2. **Negative keyword package** -- grouped by campaign/ad group level, with match type guidance.
3. **Promotion candidates** -- with suggested ad group placement.

Every recommendation must include rationale and spend/conversion context.

**Negative match type guidance:**

- Use `EXACT` negative when only a specific phrase should be blocked.
- Use `PHRASE` negative when the core phrase is irrelevant regardless of surrounding words (most common choice).
- Avoid `BROAD` negatives unless the single word is unambiguously irrelevant.

**Level guidance:**

- `ad_group` level: mismatch is scoped to one ad group's theme.
- `campaign` level: mismatch applies across the entire campaign.
- Account-level: if exclusions are universal, recommend adding to a negative keyword list in the UI.

### Phase 5: Generate copy-paste artifacts

For each negative keyword recommendation, produce a ready-to-paste list formatted for the Microsoft Advertising bulk upload:

```
Campaign-level negatives for [Campaign Name]:
-"exact match negative"
-[phrase match negative]
-broad match negative

Ad-group-level negatives for [Campaign] > [Ad Group]:
-"exact match negative"
-[phrase match negative]
```

Include the UI path for adding each level of negatives.

## Output format

```markdown
## Search Term Verdict - [Date]

### Microsoft Ads: [Account Name] ([Account ID])

**Coverage note:** Bing search query reports have privacy thresholds -- low-volume terms may be hidden. Data covers [X]% of total search spend.

#### Summary
| Verdict | Count | Spend | Notes |
|---|---:|---:|---|
| NEGATE | X | $X,XXX | [top reason] |
| PROMOTE | X | $X,XXX | [top opportunity] |
| INVESTIGATE | X | $X,XXX | [requires manual review] |
| KEEP | X | $X,XXX | [aligned and performing] |

#### Match Type Drift Analysis
| Search Term | Triggering Keyword | Match Type | Drift Type | Spend | Conv |
|---|---|---|---|---:|---:|

#### Negative Keyword Recommendations
| Keyword | Level | Parent | Match Type | 30d Spend | Reason |
|---|---|---|---|---:|---|

##### Copy-Paste Negative Lists

**Campaign: [Name]**
```
-[phrase negative 1]
-[phrase negative 2]
-"exact negative 1"
```
**UI path:** Microsoft Advertising > [Campaign] > Keywords > Negative keywords > Add negative keywords > paste list

#### Promotion Candidates
| Search Term | Campaign | Suggested Ad Group | Conv | CPA | Why promote |
|---|---|---|---:|---:|---|

### Investigate
- [Term] - [why human review is required]
```

## Guardrails

- All negative keyword recommendations are manual -- this plugin makes no account modifications.
- Flag potential positive-keyword collisions before recommending negatives.
- Mention search-term privacy threshold and estimated data coverage gap.
- When data volume exceeds 5,000 rows, recommend narrower date/campaign scope.
- Bing close variant matching is more aggressive than Google's. Be more aggressive with negation recommendations to compensate.
- **Read-only**: This skill produces analysis and copy-paste artifacts only. No account modifications are made.

## Profile Maintenance

After completing analysis, if `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md` exists:
1. Update Watch List with any new high-spend non-converting terms flagged.
2. Append to Decision Log if user approves negative keyword additions.
3. Update "Last updated" date.
Present proposed profile changes to the user before writing.

## References

- `references/bing-queries.md`
- `references/thresholds.md`
- `references/ui-paths.md`
