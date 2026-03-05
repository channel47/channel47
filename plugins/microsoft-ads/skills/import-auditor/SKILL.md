---
name: import-auditor
description: >-
  This skill should be used when the user asks to "audit my Google import",
  "check import settings", "post-import cleanup", "review Bing import",
  "what did Google import break", "import audit", "check auto-import",
  "fix import defaults", "import drift", "are my imports synced",
  "Google to Bing import", "import health check",
  "did the import mess anything up", "compare Google vs Bing settings",
  "MSAN got auto-enabled", "import brought wrong bid strategy",
  or mentions Google Ads import, auto-import cleanup, import verification,
  import drift detection, or post-import review for Microsoft Advertising.
allowed-tools: mcp__bing-ads__query, mcp__bing-ads__report, mcp__bing-ads__list_accounts
---

# Import Auditor — Microsoft Ads

Post-Google-Ads-import cleanup and verification. Checks every setting that Google Ads import commonly misconfigures and produces a pass/fail checklist with exact UI paths to fix each issue.

## Why This Exists

Google Ads import is the most common way accounts get created in Microsoft Advertising. But the import process silently enables settings that waste budget:
- MSAN gets turned on by default (Google has no equivalent).
- Search partners get enabled.
- "People in or searching for" location targeting is the default (Google defaults differ per campaign).
- Negative keyword lists don't transfer (Google shared lists are platform-specific).
- Bid strategies may not map 1:1 (Google Smart Bidding != Bing equivalents).
- Ad scheduling is lost (imports default to 24/7).

This skill catches all of these in one pass.

## Account Context

Read `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md` at the start of every run.
If it exists:
- Use known account IDs -- skip `list_accounts` discovery.
- Read Import Config for last import date and auto-import settings.
- Check Decision Log for prior import audit results.
If it doesn't exist, fall back to `list_accounts` and suggest running `platform-setup`.

## Data Access

- `mcp__bing-ads__query`: Query campaign structure, keywords, ads, ad extensions.
- `mcp__bing-ads__report`: Generate performance reports for conversion verification.
- `mcp__bing-ads__list_accounts`: Validate account access.

Use query and report configurations from `references/bing-queries.md` (IA- prefixed queries).

### Connection verification

1. If the profile has account IDs, use them directly.
2. Otherwise, run `mcp__bing-ads__list_accounts` to discover accounts.
3. If it fails, report the connection failure and suggest running `platform-setup`.

## Agent Acceleration

When the account has imported campaigns, spawn the `import-checker` agent to check each campaign's settings in parallel. Pass campaign IDs and the checklist from `references/import-checklist.md`. The agent returns a pass/fail matrix per campaign, which this skill consolidates into the final audit report.

## Workflow

### Phase 1: Collect campaign structure

Execute queries from `references/bing-queries.md`:

1. **IA-1**: Campaign structure query -- all campaigns with settings (network, targeting, scheduling, budget, bid strategy).
2. **IA-2**: Keyword report (30d) -- match types and negative keyword presence.
3. **IA-3**: Campaign performance report (7d) -- verify conversions are tracking.
4. **IA-4**: Ad extensions query -- verify extensions imported correctly.

### Phase 2: Run the import checklist

Use `references/import-checklist.md` as the master checklist. Evaluate each item:

#### Critical (fix immediately)

| Check | How to Detect | Pass Criteria |
|-------|--------------|---------------|
| MSAN disabled | IA-1: check ad distribution settings | Audience Network not enabled on search campaigns |
| Search partners appropriate | IA-1: check search partner settings | Partners disabled or intentionally enabled (per profile Preferences) |
| Location targeting: "People in" only | IA-1: check location targeting type | All campaigns set to "People in your targeted locations" |
| Conversion tracking verified | IA-3: check for conversions > 0 in 7d data | At least one campaign has conversions, indicating UET is active |

#### Important (fix within 48h)

| Check | How to Detect | Pass Criteria |
|-------|--------------|---------------|
| Broad match keywords reviewed | IA-2: count broad match keywords | No broad match keywords, OR broad match with negative coverage |
| Negative keyword lists imported | IA-2: check for negative keywords | Campaigns have negative keywords (Google shared lists don't transfer) |
| Ad scheduling applied | IA-1: check ad schedule settings | Campaigns have scheduling if profile indicates non-24/7 intent |
| Device bid adjustments reviewed | IA-1: check device bid modifiers | Device adjustments present (Google modifiers don't always map) |

#### Optimization (fix within 1 week)

| Check | How to Detect | Pass Criteria |
|-------|--------------|---------------|
| Bid strategy compatibility | IA-1: check bid strategy type | Strategy is a native Bing type, not an unmapped Google import |
| Ad extensions imported | IA-4: check extension presence | Sitelinks, callouts, and structured snippets present |
| Campaign naming consistent | IA-1: analyze campaign name patterns | Consistent naming convention across campaigns |

### Phase 3: Score and prioritize

For each failed check:

1. Estimate dollar impact using the same formulas from `references/thresholds.md`:
   - MSAN enabled: total campaign spend at-risk.
   - Search partners: partner network spend estimate.
   - Location targeting: 5-15% of spend on out-of-area traffic.
   - Missing negatives: broad match spend without negative protection.
   - Missing scheduling: overnight spend estimate.
2. Tag severity:
   - **HIGH** (>$500/mo): Critical items that failed.
   - **MEDIUM** ($100-500/mo): Important items that failed.
   - **LOW** ($25-100/mo): Optimization items.
   - **INFO** (<$25/mo): Minor findings.
3. Provide the exact Microsoft Advertising UI path to fix each issue.
4. Generate copy-paste artifacts where applicable (negative keyword lists, scheduling templates).

## Output format

```markdown
## Import Audit - [Date]

### Microsoft Ads: [Account Name] ([Account ID])
**Import Status:** [X] of [Y] checks passed

### Audit Summary
| Priority | Total | Passed | Failed | Estimated Waste |
|----------|------:|-------:|-------:|----------------:|
| Critical | X | X | X | $X,XXX/mo |
| Important | X | X | X | $X,XXX/mo |
| Optimization | X | X | X | $X,XXX/mo |

### Critical Items

#### MSAN Distribution — [PASS/FAIL]
- **Status**: [enabled/disabled] on [N] campaigns
- **Impact**: $X,XXX/month at-risk
- **Fix**: Microsoft Advertising > Campaign > Settings > Ad distribution > uncheck "Microsoft Audience Network"
- **Campaigns to fix**: [list]

#### Search Partners — [PASS/FAIL]
- **Status**: [enabled/disabled] on [N] campaigns
- **Impact**: $X,XXX/month at-risk
- **Fix**: Microsoft Advertising > Campaign > Settings > Ad distribution > uncheck search partners

#### Location Targeting — [PASS/FAIL]
- **Status**: [N] campaigns using "People in or searching for"
- **Impact**: $X,XXX/month at-risk on out-of-area traffic
- **Fix**: Microsoft Advertising > Campaign > Settings > Locations > Advanced > select "People in your targeted locations"
- **Campaigns to fix**: [list]

#### Conversion Tracking — [PASS/FAIL]
- **Status**: [N] conversions recorded in last 7 days
- **Note**: If zero conversions, verify UET tag is installed and conversion goals are configured.
- **Fix**: Microsoft Advertising > Tools > UET tags > verify tag status

### Important Items

#### Broad Match Keywords — [PASS/FAIL]
- **Status**: [N] broad match keywords without negative coverage
- **Impact**: $X,XXX/month unprotected spend
- **Fix**: Microsoft Advertising > Campaign > Keywords > Negative keywords
- **Copy-paste negatives** (suggested based on search term analysis):
  ```
  [negative keyword list]
  ```

#### Negative Keyword Lists — [PASS/FAIL]
- **Status**: [N] campaigns missing negative keywords
- **Fix**: Microsoft Advertising > Campaign > Keywords > Negative keywords > Add negative keywords

#### Ad Scheduling — [PASS/FAIL]
- **Status**: [N] campaigns running 24/7
- **Impact**: $X,XXX/month estimated overnight waste
- **Fix**: Microsoft Advertising > Campaign > Settings > Ad scheduling

#### Device Bid Adjustments — [PASS/FAIL]
- **Status**: [N] campaigns with default device bids
- **Fix**: Microsoft Advertising > Campaign > Settings > Device bid adjustments

### Optimization Items

#### Bid Strategy Compatibility — [PASS/FAIL]
- **Status**: [current strategies and any compatibility notes]
- **Fix**: Microsoft Advertising > Campaign > Settings > Bid strategy

#### Ad Extensions — [PASS/FAIL]
- **Status**: [present/missing] sitelinks, callouts, structured snippets
- **Fix**: Microsoft Advertising > Ads & extensions > Extensions

#### Naming Conventions — [PASS/FAIL]
- **Status**: [consistency assessment]

### Auto-Import Recommendation
[If auto-import is detected as enabled, recommend reviewing the schedule or switching to manual import to prevent recurring drift.]

**UI path:** Microsoft Advertising > Import > Google Ads > Schedule and settings

### Notes
- This audit checks settings only. It does not modify the account.
- Dollar estimates assume waste patterns from industry benchmarks where direct data is unavailable.
- Re-run this audit after applying fixes to verify resolution.
```

## Guardrails

- **Read-only**: This skill produces a checklist and recommendations only. No account modifications are made.
- All recommended actions include exact Microsoft Advertising UI paths.
- Dollar estimates are clearly labeled as estimates based on industry benchmarks.
- If the account was not imported from Google (no import history), note that the checklist still applies for general Bing hygiene but some checks (auto-import, bid strategy mapping) may not be relevant.
- Recommend disabling auto-import or switching to manual import to prevent recurring issues.

## Profile Maintenance

After completing analysis, if `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md` exists:
1. Update Import Config section with current import status.
2. Update Watch List with any Critical or Important failed checks.
3. Append to Decision Log when user addresses specific items.
4. Update "Last updated" date.
Present proposed profile changes to the user before writing.

## References

- `references/bing-queries.md` -- query IDs: IA-1 through IA-4
- `references/import-checklist.md`
- `references/thresholds.md`
- `references/ui-paths.md`
