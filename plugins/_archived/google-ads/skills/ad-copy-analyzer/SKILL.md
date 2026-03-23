---
name: ad-copy-analyzer
description: >-
  This skill should be used when the user asks to "analyze my ads",
  "review RSAs", "check ad copy", "ad strength review", "which ads
  need work", "headline analysis", "ad copy audit", "RSA performance",
  "asset performance", "are my ads any good", "ad quality check",
  "which headlines are working", "improve my ad copy",
  "ad strength is poor", "pinning problems", "messaging diversity",
  "how are my RSAs doing", "best performing headlines",
  or mentions ad copy optimization, responsive search ad analysis,
  headline/description review, or asset label performance.
allowed-tools: mcp__google-ads__query, mcp__google-ads__list_accounts
---

# Ad Copy Analyzer -- Google Ads

Analyze Responsive Search Ads (RSAs) for quality gaps, underperforming assets, over-pinning, and messaging diversity. Produces a prioritized replacement plan ranked by ad group spend.

## Account Context

Read `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md` at the start of every run.
If it exists:
- Use known account IDs -- skip `list_accounts` discovery.
- Apply KPI targets when assessing ad performance (e.g., flag ads in ad groups where CPA > target).
- Note active tests -- do not recommend changes to ads currently in a test.
- Check watch list for prior ad copy findings that may need follow-up.
If it doesn't exist, fall back to `list_accounts` and suggest running `platform-setup`.

## Data Access

- `mcp__google-ads__query`: Execute GAQL SELECT queries and return structured rows.
- `mcp__google-ads__list_accounts`: Validate account access before analysis when customer scope is unclear.

Use GAQL templates from `references/gaql-queries.md` directly with `mcp__google-ads__query`.

### Connection verification

1. If the profile has account IDs, use them directly.
2. Otherwise, run `mcp__google-ads__list_accounts` to discover accounts.
3. If it fails, report the connection failure and suggest running `platform-setup`.

## Workflow

### Phase 1: Collect data

Execute two queries from `references/gaql-queries.md`:

| Query ID | What It Returns |
|----------|----------------|
| ACA-1 | All enabled RSAs with headlines, descriptions, ad strength, final URLs, and 30-day performance metrics (impressions, clicks, CTR, cost, conversions, CPA) |
| ACA-2 | Asset-level performance labels, field types (HEADLINE/DESCRIPTION), pinning status, and per-asset metrics |

Run both queries. ACA-2 is at the asset level and may return many rows for large accounts.

**Scope control**: If the user specifies a campaign or ad group, add the appropriate WHERE filter to both queries. Otherwise, analyze the full account.

### Phase 2: Ad strength analysis

Classify all RSAs by ad strength:

| Ad Strength | Health | Action Needed |
|-------------|--------|---------------|
| EXCELLENT | Strong | Monitor |
| GOOD | Acceptable | Optional optimization |
| AVERAGE | Below standard | Improve headlines/descriptions |
| POOR | Critical | Rewrite needed |
| UNSPECIFIED | Insufficient data | Needs more impressions |

Compute the distribution:
- Count and percentage of RSAs at each ad strength level.
- Total spend at each level.
- Average CTR and CPA at each level.

Flag: If >30% of RSAs are AVERAGE or POOR AND those RSAs carry >20% of total ad spend, tag as **HIGH** severity.

### Phase 3: Asset performance analysis

For each RSA, classify assets by performance label:

| Label | Meaning | Action |
|-------|---------|--------|
| BEST | Top performer relative to other assets | Protect -- do not edit |
| GOOD | Above average | Keep |
| LOW | Below average | Replace candidate |
| PENDING | Insufficient data for labeling | Monitor -- needs more impressions |

Build the replacement priority list:

1. Filter to assets with `performance_label = LOW`.
2. Join with ad group spend from ACA-1 to rank by dollar exposure.
3. Prioritize LOW assets in high-spend ad groups (these have the most impact potential).
4. Estimate monthly impact: `ad_group_monthly_spend * estimated_ctr_lift_from_replacement`.
   - Use a conservative 5-15% CTR lift estimate for replacing a LOW asset with a new variant.
   - Label all impact estimates explicitly as estimates.

Assign severity:
- **HIGH** (>$500/mo ad group spend with LOW assets)
- **MEDIUM** ($100-500/mo ad group spend with LOW assets)
- **LOW** ($25-100/mo ad group spend with LOW assets)
- **INFO** (<$25/mo or PENDING-only ad groups)

### Phase 4: Pinning analysis

From ACA-2, identify assets with `pinned_field` values (HEADLINE_1, HEADLINE_2, HEADLINE_3, DESCRIPTION_1, DESCRIPTION_2).

Over-pinning heuristic:
- An RSA is "over-pinned" if >50% of its headline slots AND >50% of its description slots have pinned assets.
- A fully pinned RSA (all slots pinned) effectively disables ad rotation optimization entirely.

For each over-pinned ad:
- Calculate the ad group's 30-day spend.
- Note which assets are pinned to which positions.
- Recommend specific unpinning actions: which pins to remove first (start with lowest-performing pinned assets).
- **UI path:** Google Ads > Campaigns > [Campaign] > Ad groups > [Ad group] > Ads > [Ad] > Edit > Click the pin icon on each asset to unpin.

### Phase 5: Headline and description diversity analysis

For each ad group with active RSAs:

1. Extract all headline texts and description texts across the ad group's RSAs.
2. Cluster headlines by theme:
   - **Brand**: company name, brand terms
   - **Benefit**: value propositions, outcomes
   - **Feature**: product features, specifications
   - **CTA**: calls to action (Get, Try, Start, Buy, etc.)
   - **Social proof**: reviews, awards, numbers
   - **Urgency**: limited time, seasonal, deadlines
   - **Price/Offer**: discounts, pricing, promotions
3. Flag ad groups with:
   - Fewer than 3 distinct themes across all headlines (low diversity).
   - >60% of headlines in a single theme (over-concentration).
   - Duplicate or near-duplicate headlines within the same RSA.
4. Suggest themes to add based on missing categories.

Do not generate specific headline or description copy unless the user explicitly asks for copywriting help. Focus on theme gaps and structural recommendations.

### Phase 6: Build output

Compile all findings into the output format below. Every actionable finding includes:
- A dollar table showing spend exposure.
- A Google Ads UI path for remediation.
- A copy-paste-ready list of entities to act on.

## Output format

```markdown
## Ad Copy Analysis -- [Date]

### Account
- Google Ads: [Account Name] ([Customer ID])
- RSAs analyzed: [N] across [N] ad groups
- 30-day ad spend analyzed: $X,XXX

### Ad Strength Summary

| Ad Strength | Count | % of RSAs | 30d Spend | Avg CTR | Avg CPA |
|-------------|------:|----------:|----------:|--------:|--------:|
| EXCELLENT | X | XX% | $X,XXX | X.XX% | $XX.XX |
| GOOD | X | XX% | $X,XXX | X.XX% | $XX.XX |
| AVERAGE | X | XX% | $X,XXX | X.XX% | $XX.XX |
| POOR | X | XX% | $X,XXX | X.XX% | $XX.XX |

### Priority: LOW Assets in High-Spend Ad Groups

| # | Severity | Campaign | Ad Group | Asset Type | Asset Text | Label | Ad Group 30d Spend | Est. Impact |
|---|----------|----------|----------|-----------|------------|-------|-------------------:|------------:|
| 1 | HIGH | [campaign] | [ad group] | HEADLINE | [text] | LOW | $X,XXX | $XXX/mo |
| 2 | MEDIUM | [campaign] | [ad group] | DESCRIPTION | [text] | LOW | $XXX | $XX/mo |

**UI path:** Google Ads > Campaigns > [Campaign] > Ad groups > [Ad group] > Ads > [Ad] > Edit > Replace the LOW asset with a new variant.

### Pinning Warnings

| Campaign | Ad Group | Ad ID | Pinned Slots | Ad Group 30d Spend | Recommendation |
|----------|----------|-------|-------------|-------------------:|----------------|
| [name] | [name] | [id] | H1, H2, D1 | $X,XXX | Unpin [asset] from [position] |

**UI path:** Google Ads > Campaigns > [Campaign] > Ad groups > [Ad group] > Ads > [Ad] > Edit > Click pin icon to remove pin.

### Diversity Gaps

| Campaign | Ad Group | Active Themes | Missing Themes | 30d Spend |
|----------|----------|--------------|----------------|----------:|
| [name] | [name] | Brand, CTA | Benefit, Social Proof | $X,XXX |

**Suggestion:** Add headlines in the [missing theme] category to improve rotation diversity.

### Replacement Priorities (Summary)

Copy-paste list of ad groups needing work, ordered by spend:

1. **[Campaign] > [Ad Group]** ($X,XXX/mo) -- [N] LOW assets, [ad strength], missing [themes]
2. **[Campaign] > [Ad Group]** ($XXX/mo) -- [N] LOW assets, over-pinned
3. ...

### Notes
- Data freshness: 30-day lookback, performance labels require sufficient impression volume
- Assets with PENDING labels excluded from replacement priorities
- Impact estimates assume 5-15% CTR lift from asset replacement (conservative range)
```

## Guardrails

- **Read-only**: This skill produces analysis and recommendations only. No ad modifications are made. All remediation actions include specific Google Ads UI paths.
- **No copy generation by default**: Do not write new headlines or descriptions unless the user explicitly requests copywriting. Focus on structural analysis (strength, labels, pinning, themes).
- **PENDING assets**: Do not recommend replacing PENDING assets. They need more impression volume before their performance label is meaningful. Note the count of PENDING assets separately.
- **BEST asset protection**: Never recommend modifying or replacing BEST-labeled assets. Call them out as strengths to preserve.
- **Active tests**: If the account profile indicates active ad copy tests, exclude those ad groups from replacement recommendations and note the exclusion.
- **Small ad groups**: For ad groups with <100 impressions in 30 days, asset performance labels are unreliable. Note these ad groups separately as "insufficient data" rather than scoring them.
- **Ad strength caveats**: Ad strength is Google's predictive signal, not a direct performance metric. An EXCELLENT ad strength does not guarantee high CTR or low CPA. Note this distinction in the output when ad strength and actual performance diverge.
- **Conversion lag**: CPA figures use the full 30-day window to minimize conversion lag distortion. Do not compare yesterday's CPA to 30-day CPA without noting the lag.
- **Severity calibration**: All dollar impact figures are labeled as estimates. Distinguish direct spend from modeled improvement potential.

## Profile Maintenance

After completing analysis, if `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md` exists:
1. Update Watch List with HIGH-severity findings (LOW assets in high-spend ad groups, fully pinned ads with significant spend).
2. Update Active Tests if the user mentioned starting an ad copy test during the session.
3. Append to Decision Log if the user acknowledged specific replacement or unpinning actions.
4. Update "Last updated" date.
Present proposed profile changes to the user before writing.

## References

- `references/gaql-queries.md` -- query IDs: ACA-1, ACA-2
