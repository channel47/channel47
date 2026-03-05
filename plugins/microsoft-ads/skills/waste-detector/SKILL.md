---
name: waste-detector
description: >-
  This skill should be used when the user asks to "find Bing waste",
  "audit my Microsoft Ads account", "where am I wasting budget",
  "MSAN waste", "search partner waste", "am I wasting money on Bing",
  "where's my budget going", "which keywords are bleeding money",
  "why is my Bing CPA so high", "what's eating my Bing budget",
  or mentions Microsoft Advertising optimization, Bing spend analysis,
  budget efficiency, or MSAN spend leaks.
allowed-tools: mcp__bing-ads__report, mcp__bing-ads__query, mcp__bing-ads__list_accounts
---

# Microsoft Ads Waste Detector

Scan Microsoft Advertising accounts for the 7 most common Bing-specific spend leaks and quantify each leak in dollars with an action plan. Every finding includes a dollar table, Microsoft Advertising UI path, and copy-paste artifact.

## Account Context

Read `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md` at the start of every run.
If it exists:
- Use known account IDs -- skip `list_accounts` discovery.
- Apply KPI targets as waste thresholds (e.g., flag CPA > target CPA).
- Note active tests when interpreting performance shifts.
- Check watch list for follow-up items from prior sessions.
- Read MSAN policy and search partners policy from Preferences.
If it doesn't exist, fall back to `list_accounts` and suggest running `platform-setup`.

## Data Access

- `mcp__bing-ads__report`: Generate performance reports for waste analysis.
- `mcp__bing-ads__query`: Query campaign structure (campaigns, ad groups, keywords, ads).
- `mcp__bing-ads__list_accounts`: Validate account access.

Use report configurations from `references/bing-queries.md`.

### Connection verification

1. If the profile has account IDs, use them directly.
2. Otherwise, run `mcp__bing-ads__list_accounts` to discover accounts.
3. If it fails, report the connection failure and suggest running `platform-setup`.

## Workflow

### Phase 1: Run waste queries

Execute query groups from `references/bing-queries.md` (WD- prefixed queries):

| # | Waste Type | Query | Detection Method |
|---|-----------|-------|-----------------|
| 1 | MSAN enabled | WD-1: Campaign structure query | Check ad distribution settings for Audience Network |
| 2 | Search partners enabled | WD-2: Campaign structure query | Check search partner network settings |
| 3 | Broad match imports | WD-3: Keyword report (30d) | Filter match_type = Broad, check negative coverage |
| 4 | Auto-import overwriting | WD-4: Campaign structure + profile comparison | Compare current settings vs last known manual state |
| 5 | Budget burning overnight | WD-5: Campaign performance report (hourly if available, daily as fallback) | Identify campaigns with no ad scheduling spending 24/7 |
| 6 | Bot traffic | WD-6: Campaign + keyword performance (yesterday) | High clicks, zero conversions, suspicious patterns |
| 7 | Location targeting expanding | WD-7: Campaign structure query | Check "People in or searching for" vs "People in" |

### Phase 2: Quantify impact

Use `references/thresholds.md` for detection thresholds and dollar formulas. For each waste type:

#### Type 1: MSAN (Microsoft Audience Network) enabled

- **Detection**: Campaign has Audience Network distribution enabled.
- **Dollar waste**: Total MSAN spend = at-risk amount. If network-segmented data is available, use actual Audience Network spend. Otherwise, estimate 10-30% of total campaign spend based on industry averages.
- **Why it matters**: MSAN serves ads on low-quality partner sites (MSN, Outlook, Edge). For most search-intent campaigns, MSAN burns budget on display-like placements with poor conversion rates.
- **UI path**: Microsoft Advertising > Campaign > Settings > Ad distribution > uncheck "Microsoft Audience Network"

#### Type 2: Search partners enabled

- **Detection**: Campaign has search partner network enabled.
- **Dollar waste**: Search partner network spend. Estimate using network-level performance if available, otherwise flag total campaign spend as partially at-risk.
- **Why it matters**: Partner sites (DuckDuckGo, Yahoo, AOL) often have lower intent and higher CPAs than Bing Search proper.
- **UI path**: Microsoft Advertising > Campaign > Settings > Ad distribution > uncheck search partners

#### Type 3: Broad match imports

- **Detection**: Keywords with match_type = Broad spending money, especially those imported from Google without corresponding negative keyword lists.
- **Dollar waste**: Total broad match keyword spend in campaigns without negative keyword coverage.
- **Why it matters**: Google Ads shared negative keyword lists do not transfer during import. Broad match keywords imported without negatives are unprotected. Bing's close variant matching is more aggressive than Google's, making negatives even more critical.
- **UI path**: Microsoft Advertising > Campaign > Keywords > Negative keywords > Add negative keywords

#### Type 4: Auto-import overwriting

- **Detection**: Compare current campaign settings against the profile's Import Config. Look for settings that reverted to Google defaults after an import.
- **Dollar waste**: Indirect -- quantify as the sum of Type 1 + Type 2 waste that was re-enabled by import, plus any bid strategy changes.
- **Why it matters**: Google Ads auto-import can silently re-enable MSAN, search partners, and overwrite manual bid adjustments on every sync.
- **UI path**: Microsoft Advertising > Import > Google Ads > Schedule and settings > Review or disable auto-import

#### Type 5: Budget burning overnight

- **Detection**: Campaigns without ad scheduling (running 24/7) that show overnight spend with zero or near-zero conversions.
- **Dollar waste**: Spend during low-conversion hours (estimate using the ratio of overnight impressions to total, applied to total spend).
- **Why it matters**: B2B campaigns especially waste budget overnight. Without day-parting, Bing will spend evenly across 24 hours.
- **UI path**: Microsoft Advertising > Campaign > Settings > Ad scheduling > Set hours

#### Type 6: Bot traffic

- **Detection**: Campaigns or keywords with suspicious click patterns:
  - Click-through rate > 15% combined with zero conversions.
  - Clicks > 50/day from campaigns with zero conversions.
  - Single device type accounting for >80% of clicks with zero conversions.
- **Dollar waste**: Total spend on flagged entities.
- **Why it matters**: Microsoft's invalid click detection catches most fraud, but some patterns slip through, especially on partner networks.
- **UI path**: Microsoft Advertising > Reports > Performance > Publisher URL report (to identify suspect placements). File an invalid click review if patterns persist.

#### Type 7: Location targeting expanding

- **Detection**: Campaigns set to "People in or searching for your targeted locations" instead of "People in your targeted locations".
- **Dollar waste**: Estimate 5-15% of campaign spend reaching users outside physical target area. Flag total campaign spend as at-risk.
- **Why it matters**: The default "People in or searching for" includes users who merely search about your location, not users physically there. For local businesses and geo-restricted services, this inflates spend on irrelevant traffic.
- **UI path**: Microsoft Advertising > Campaign > Settings > Locations > Advanced > select "People in your targeted locations"

### Phase 3: Build severity and remediation

For each finding:

1. Compute dollar waste using the formula specified per type.
2. Tag severity:
   - **HIGH** (>$500/mo): Immediate action required.
   - **MEDIUM** ($100-500/mo): Fix within 48 hours.
   - **LOW** ($25-100/mo): Fix within 1 week.
   - **INFO** (<$25/mo): Awareness only.
3. Generate a copy-paste artifact for each actionable finding:
   - Negative keyword lists (for Type 3).
   - Campaign settings checklist (for Types 1, 2, 5, 7).
   - Publisher exclusion list (for Type 6).
4. Include the exact Microsoft Advertising UI navigation path.

## Output format

```markdown
## Waste Report - [Date]

### Microsoft Ads: [Account Name] ([Account ID])
**Estimated Recoverable Waste: $X,XXX/month**

| # | Waste Type | Monthly Cost | Severity | Action |
|---|---|---:|---|---|

### Detailed Findings

#### 1. MSAN Enabled — [severity]
- **Impact**: $X,XXX/month at-risk
- **Campaigns affected**: [list]
- **UI path**: Microsoft Advertising > Campaign > Settings > Ad distribution > uncheck "Microsoft Audience Network"

#### 2. Search Partners Enabled — [severity]
- **Impact**: $X,XXX/month at-risk
- **Campaigns affected**: [list]
- **UI path**: Microsoft Advertising > Campaign > Settings > Ad distribution > uncheck search partners

#### 3. Broad Match Without Negatives — [severity]
- **Impact**: $X,XXX/month at-risk
- **Keywords**: [top 10 by spend]
- **Copy-paste negatives**:
  ```
  [negative keyword list]
  ```
- **UI path**: Microsoft Advertising > Campaign > Keywords > Negative keywords

#### 4. Auto-Import Overwriting — [severity]
- **Impact**: $X,XXX/month (sum of re-enabled waste)
- **Settings affected**: [list of overwritten settings]
- **UI path**: Microsoft Advertising > Import > Google Ads > Schedule and settings

#### 5. Overnight Budget Burn — [severity]
- **Impact**: $X,XXX/month estimated overnight waste
- **Campaigns**: [list with overnight spend estimates]
- **UI path**: Microsoft Advertising > Campaign > Settings > Ad scheduling

#### 6. Bot Traffic Signals — [severity]
- **Impact**: $X,XXX/month on flagged entities
- **Suspicious patterns**: [list]
- **UI path**: Microsoft Advertising > Reports > Performance > Publisher URL report

#### 7. Location Targeting Expanding — [severity]
- **Impact**: $X,XXX/month at-risk
- **Campaigns**: [list using "searching for" targeting]
- **UI path**: Microsoft Advertising > Campaign > Settings > Locations > Advanced

### Summary
| Total Waste | HIGH Items | MEDIUM Items | LOW Items |
|---:|---:|---:|---:|
| $X,XXX/mo | X | X | X |
```

## Guardrails

- Call out where dollar figures are estimates vs direct spend totals.
- Keep assumptions explicit for model-based calculations.
- Distinguish "true zero" from omitted zero-value rows in reports.
- All recommendations are manual action items with UI paths -- this plugin makes no account modifications.
- Bot traffic signals are signals, not confirmations. Recommend checking Microsoft's Invalid Clicks report before filing disputes.
- **Read-only**: This skill produces analysis and recommendations only. No account modifications are made.

## Profile Maintenance

After completing analysis, if `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md` exists:
1. Update Watch List with any HIGH or MEDIUM severity findings.
2. Update Active Tests if user mentioned starting or completing a test.
3. Append to Decision Log if actions were taken.
4. Update "Last updated" date.
Present proposed profile changes to the user before writing.

## References

- `references/bing-queries.md`
- `references/thresholds.md`
- `references/ui-paths.md`
