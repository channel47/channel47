---
name: waste-detector
description: >-
  This skill should be used when the user asks to "find waste",
  "audit my Google Ads account", "where am I wasting budget",
  "am I wasting money", "where's my budget going",
  "which keywords are bleeding money", "why is my CPA so high",
  "what's eating my budget", "ROAS check", "budget leaks",
  or mentions Google Ads optimization, spend analysis, budget efficiency,
  non-converting keywords, or quality score waste.
allowed-tools: mcp__google-ads__query, mcp__google-ads__list_accounts
---

# Google Ads Waste Detector

Scan a Google Ads account for the most common spend leaks, quantify each leak in dollars, and produce a prioritized action plan with UI paths and copy-paste artifacts.

**Read-only by design.** This skill does not modify your account. All remediation is delivered as action plans you execute in the Google Ads UI.

## Account Context

Read `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md` at the start of every run.
If it exists:
- Use known account IDs -- skip `list_accounts` discovery.
- Apply KPI targets as anomaly detection thresholds (e.g., flag CPA > target CPA).
- Note active tests when interpreting performance shifts.
- Check watch list for follow-up items from prior sessions.
If it doesn't exist, fall back to `list_accounts` and suggest running `platform-setup`.

## Data Access

- `mcp__google-ads__query`: Execute GAQL SELECT queries for waste detection.
- `mcp__google-ads__list_accounts`: Validate account visibility before running audits.

## Agent Acceleration

When the account has more than 5 active campaigns, spawn the `waste-scanner` agent to run waste queries in parallel across campaign batches. Pass campaign IDs in batches and collect consolidated findings. For accounts with 5 or fewer campaigns, run sequentially (no agent needed).

## Workflow

### Phase 1: Run waste queries

Execute the eight query groups from `references/gaql-queries.md`.

Waste types covered:

| # | Waste Type | Detection Method |
|---|-----------|-----------------|
| 1 | Non-converting keywords | GAQL: keywords with spend, zero conversions |
| 2 | Low-quality-score keywords still spending | GAQL: QS <= 5 with material spend |
| 3 | Search campaigns with Display network expansion | GAQL: target_content_network = TRUE on Search |
| 4 | Budget-limited campaigns | GAQL: search_budget_lost_impression_share > 10% |
| 5 | Broad match without shared negative list coverage | GAQL: broad keywords + campaign_shared_set check |
| 6 | Single-ad ad groups | GAQL: ad groups with exactly 1 enabled ad |
| 7 | Enabled campaigns with zero impressions | GAQL: enabled campaigns, 0 impressions over 7d |
| 8 | Semantic mismatch in search terms | GAQL: non-converting search terms with material spend |

### Phase 2: Quantify impact

Use `references/thresholds.md` for exact detection thresholds and dollar formulas per waste type. Summary:

1. Apply the specific threshold for each waste type (not a single blanket rule).
2. Compute dollar waste using the formula specified per type.
3. Rank all findings by dollar impact descending.
4. Tag severity: `HIGH` (>$500/mo), `MEDIUM` ($100-500), `LOW` ($25-100), `INFO` (<$25).

Use `references/benchmarks.md` for QS-to-CPC pressure multipliers and CTR bands.

### Phase 3: Build action plans

For every finding, produce a concrete action plan instead of API mutations. Each action plan includes:

1. **Dollar table** -- priority-ranked findings with entity path and spend.
2. **UI path** -- step-by-step navigation in Google Ads to fix the issue.
3. **Copy-paste artifacts** -- negative keyword lists, settings values, or other text ready to paste.

#### Action plan format per waste type

**Type 1 -- Non-converting keywords (pause):**
- Dollar table: keyword, campaign > ad group, match type, 30d spend, 30d clicks, action (Pause).
- UI path: `Google Ads > Campaign '[name]' > Ad Group '[name]' > Keywords > select '[keyword]' > Edit > Pause`

**Type 2 -- Low quality score keywords (pause or improve):**
- Dollar table: keyword, campaign > ad group, QS, QS sub-scores, 30d spend, estimated CPC premium, action.
- UI path: `Google Ads > Campaign '[name]' > Ad Group '[name]' > Keywords > select '[keyword]' > Edit > Pause`
- For QS improvement: note which sub-score (ad relevance, landing page, expected CTR) is dragging.

**Type 3 -- Display expansion on Search (disable):**
- Dollar table: campaign name, 30d spend, channel type, action (Disable content network).
- UI path: `Google Ads > Campaign '[name]' > Settings > Networks > uncheck 'Include Google Display Network'`

**Type 4 -- Budget-limited campaigns (increase budget or reallocate):**
- Dollar table: campaign, daily budget, IS lost to budget, estimated missed conversions, action.
- UI path: `Google Ads > Campaign '[name]' > Settings > Budget > Edit daily budget`
- Note: this is missed opportunity, not direct waste.

**Type 5 -- Broad match without negative list (add shared negative list):**
- Dollar table: campaign, broad match spend (30d), negative list status, action.
- UI path: `Google Ads > Tools & Settings > Shared Library > Negative keyword lists > + New list`
- Then: `Google Ads > Campaign '[name]' > Settings > Negative keyword lists > Apply list`

**Type 6 -- Single-ad ad groups (add RSA variants):**
- Dollar table: campaign > ad group, 30d spend, ad count, action (Create additional RSA).
- UI path: `Google Ads > Campaign '[name]' > Ad Group '[name]' > Ads > + New ad > Responsive search ad`

**Type 7 -- Zero-impression enabled campaigns (investigate or pause):**
- Dollar table: campaign, status, daily budget, 7d impressions, action.
- UI path: `Google Ads > Campaign '[name]' > check status, targeting, ad approval`

**Type 8 -- Non-converting search terms (add as negatives):**
- Dollar table: search term, campaign > ad group, 30d spend, 30d clicks, action (Add negative).
- UI path: `Google Ads > Campaign '[name]' > Ad Group '[name]' > Search terms > select term > Add as negative keyword`
- Copy-paste artifact: negative keyword list organized by match type.

#### Negative keyword copy-paste format

When search term negatives are recommended, group them for easy pasting:

```
-- PHRASE match negatives --
"term one"
"term two"
"term three"

-- EXACT match negatives --
[specific query one]
[specific query two]
```

Include the UI path for bulk adding: `Google Ads > Tools & Settings > Shared Library > Negative keyword lists > [list name] > + Keywords > paste list`

## Output format

```markdown
## Waste Report - [Date]

### Google Ads: [Name] ([Customer ID])
**Estimated Recoverable Waste: $X,XXX/month**

### Priority Action Table

| # | Priority | Waste Type | Entity | Campaign > Ad Group | 30d Spend | Action |
|---|---|---|---|---|---:|---|

### Detailed Findings

#### [Waste Type Name]
**Monthly Impact: $X,XXX | Severity: HIGH/MEDIUM/LOW**

[Dollar table for this waste type]

**How to fix:**
[UI path steps]

[Copy-paste artifact if applicable]

---

### Summary
| Severity | Count | Monthly Impact |
|---|---:|---:|
| HIGH | X | $X,XXX |
| MEDIUM | X | $X,XXX |
| LOW | X | $XXX |
| INFO | X | $XX |
| **Total** | **X** | **$X,XXX** |

### Notes
- Dollar figures are estimates where noted; benchmark assumptions are called out.
- This report is read-only. No account changes were made.
```

## Guardrails

- Call out where dollar figures are estimates vs direct spend totals.
- Keep assumptions explicit for model-based calculations.
- Distinguish "true zero" from omitted zero-value GAQL rows.
- **Read-only**: This skill produces action plans only. No account modifications are made. All remediation requires manual execution in the Google Ads UI.

## Profile Maintenance

After completing analysis, if `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md` exists:
1. Update Watch List with any new anomalies flagged in this run.
2. Update Active Tests if user mentioned starting or completing a test.
3. Append to Decision Log if actions were taken (pauses, negatives added, etc.).
4. Update "Last updated" date.
Present proposed profile changes to the user before writing.

## References

- `references/gaql-queries.md`
- `references/thresholds.md`
- `references/benchmarks.md`
- `references/ui-paths.md`
