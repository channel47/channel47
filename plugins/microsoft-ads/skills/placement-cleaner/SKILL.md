---
name: placement-cleaner
description: >-
  This skill should be used when the user asks to "clean up placements",
  "review MSAN placements", "publisher URL report", "exclude bad placements",
  "Bing placement audit", "MSAN cleanup", "website exclusions",
  "Audience Network placement review", "where are my MSAN ads showing",
  "junk placements", "low quality publisher sites",
  "block bad websites on Bing", "MSAN spending on garbage sites",
  "placement quality check", "exclude low quality sites",
  or mentions Microsoft Audience Network placement quality,
  publisher URL analysis, website exclusion recommendations,
  or MSAN placement cleanup.
allowed-tools: mcp__bing-ads__report, mcp__bing-ads__query, mcp__bing-ads__list_accounts
---

# Placement Cleaner — Microsoft Ads

Analyze Microsoft Audience Network (MSAN) and search partner publisher URL performance. Identify low-quality placements and produce ready-to-paste website exclusion lists with dollar impact.

## Why This Exists

Microsoft Audience Network distributes ads across MSN, Outlook, Edge, and third-party publisher sites. Many of these placements have high impression volume but near-zero conversion rates. Without active exclusion management, MSAN can consume 10-30% of campaign budget on low-quality placements.

This skill pulls the publisher URL report, flags low-quality placements, and produces exclusion lists ready to paste into the Microsoft Advertising UI.

## Account Context

Read `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md` at the start of every run.
If it exists:
- Use known account IDs -- skip `list_accounts` discovery.
- Read MSAN policy from Preferences. If MSAN is intentionally enabled, focus on exclusion optimization rather than recommending disable.
- Check watch list for previously flagged placements.
If it doesn't exist, fall back to `list_accounts` and suggest running `platform-setup`.

## Data Access

- `mcp__bing-ads__report`: Generate publisher URL reports for placement analysis.
- `mcp__bing-ads__query`: Query campaign structure for MSAN-enabled campaigns.
- `mcp__bing-ads__list_accounts`: Validate account access.

Use report configurations from `references/bing-queries.md` (PC- prefixed queries).

### Connection verification

1. If the profile has account IDs, use them directly.
2. Otherwise, run `mcp__bing-ads__list_accounts` to discover accounts.
3. If it fails, report the connection failure and suggest running `platform-setup`.

## Agent Acceleration

When MSAN is enabled on more than 3 campaigns, spawn the `placement-scanner` agent to pull and analyze publisher URL reports in parallel across campaigns. The agent returns consolidated placement classifications and exclusion recommendations, which this skill merges into the final report. For 3 or fewer MSAN campaigns, run sequentially (no agent needed).

## Workflow

### Phase 1: Identify MSAN-enabled campaigns

Run **PC-1**: Campaign structure query to identify campaigns with Audience Network enabled.

If no campaigns have MSAN enabled:
- Report that MSAN is disabled across all campaigns.
- Note that this is the recommended state for most search-intent campaigns.
- Offer to check search partner placements instead.
- Stop here unless user requests partner analysis.

### Phase 2: Pull publisher URL data

Run **PC-2**: Publisher URL report (30d) for all MSAN-enabled campaigns.

Data includes:
- Publisher URL / domain
- Campaign and ad group context
- Impressions, clicks, spend
- Conversions (if available)

### Phase 3: Analyze placement quality

For each publisher URL/domain, evaluate:

#### Tier 1: Immediate exclusion candidates

- **Zero-conversion high-spend**: Spend > $25 with 0 conversions over 30 days.
- **Suspicious domains**: Domains that appear to be click farms, parked domains, or low-quality content aggregators. Common patterns:
  - Extremely high CTR (>10%) with zero conversions.
  - Domain name contains random character strings.
  - Domain is a known low-quality publisher (compare against common exclusion lists).
- **Impression farming**: >10,000 impressions with zero clicks (or <0.01% CTR) -- wasting impression budget without engagement.

#### Tier 2: Review candidates

- **Low-quality signals**: Spend $5-$25 with 0 conversions.
- **High bounce domains**: If conversion data shows partial funnel (clicks but no conversions at expected rates).
- **Category mismatch**: Publisher content category unrelated to the advertiser's vertical.

#### Tier 3: Keep (performing)

- **Converting placements**: Any placement with conversions at or below target CPA.
- **Brand-safe, relevant publishers**: MSN, Outlook, and major publisher sites performing within KPI targets.

### Phase 4: Generate exclusion lists

For each MSAN-enabled campaign:

1. Compile Tier 1 exclusions (immediate).
2. Compile Tier 2 candidates (recommend with caveats).
3. Format as copy-paste lists for the Microsoft Advertising website exclusion interface.

Exclusion format (one URL per line):
```
domain1.com
domain2.com
subdomain.domain3.com
```

### Phase 5: Search partner analysis (optional)

If the user requests, or if search partner spend is significant (>20% of total):

1. Analyze partner network performance using campaign-level network data.
2. Flag campaigns where partner network CPA is >2x the search network CPA.
3. Recommend disabling search partners on specific campaigns where partner performance is consistently poor.

## Output format

```markdown
## Placement Report - [Date]

### Microsoft Ads: [Account Name] ([Account ID])

### MSAN Status
- **Campaigns with MSAN enabled**: [N] of [total]
- **Total MSAN spend (30d)**: $X,XXX
- **MSAN conversion rate**: X.X% (vs X.X% search-only)

### Placement Quality Summary
| Tier | Placements | Spend | Conv | Action |
|------|---:|---:|---:|---|
| Immediate Exclude | X | $X,XXX | 0 | Add to exclusion list |
| Review | X | $X,XXX | X | Evaluate individually |
| Keep | X | $X,XXX | X | No action needed |

### Estimated Recoverable Waste: $X,XXX/month

### Immediate Exclusions

| Domain | Campaign | Impressions | Clicks | Spend | Conv | Reason |
|--------|----------|----------:|------:|------:|----:|--------|
| bad-domain.com | [Campaign] | X,XXX | XX | $XX | 0 | Zero conv, high spend |

#### Copy-Paste Exclusion List

**For all MSAN campaigns:**
```
domain1.com
domain2.com
domain3.com
```

**UI path:** Microsoft Advertising > Campaign > Settings > Website exclusions > Add URLs > paste list

### Review Candidates

| Domain | Campaign | Impressions | Clicks | Spend | Conv | Signal |
|--------|----------|----------:|------:|------:|----:|--------|

### Performing Placements (Keep)

| Domain | Campaign | Spend | Conv | CPA | Note |
|--------|----------|------:|----:|----:|------|

### Search Partner Performance (if analyzed)

| Campaign | Search CPA | Partner CPA | Partner Spend | Recommendation |
|----------|---:|---:|---:|---|

### Recommendations

1. **Add exclusion list**: Paste the exclusion list above into Microsoft Advertising > Campaign > Settings > Website exclusions.
2. **Monitor weekly**: Re-run this analysis weekly to catch new low-quality placements.
3. **Consider disabling MSAN**: If MSAN conversion rate is consistently >2x worse than search, recommend disabling MSAN entirely.

### Notes
- Publisher URL data may not capture all placements. Some Audience Network placements are reported at the app/property level rather than URL level.
- Exclusion lists apply at the campaign or account level. Account-level exclusions affect all campaigns.
- This analysis is read-only. No exclusions are applied automatically.
```

## Guardrails

- **Read-only**: This skill produces exclusion recommendations only. No website exclusions are applied. All changes require manual action in the Microsoft Advertising UI.
- If MSAN is intentionally enabled (per profile Preferences), focus on exclusion optimization rather than recommending full disable.
- Publisher URL data may not capture all placements. Note this limitation.
- Zero-conversion placements may be influenced by conversion lag. For placements with recent click activity (<3 days), note potential backfill.
- Do not exclude MSN, Outlook, or Edge properties unless they are genuinely non-performing -- these are Microsoft's premium placements.
- Keep exclusion lists manageable. Cap at 500 URLs per campaign (Microsoft's limit).

## Profile Maintenance

After completing analysis, if `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md` exists:
1. Update Watch List with any new high-spend zero-conversion placements.
2. Update MSAN policy in Preferences if user makes a decision about MSAN.
3. Append to Decision Log when exclusions are applied.
4. Update "Last updated" date.
Present proposed profile changes to the user before writing.

## References

- `references/bing-queries.md` -- query IDs: PC-1, PC-2
- `references/thresholds.md`
- `references/ui-paths.md`
