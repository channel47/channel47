---
name: import-checker
description: >-
  Subagent for parallel import drift detection. Launched by import-auditor skill
  to check each imported campaign's settings simultaneously — MSAN status,
  search partners, bid strategies, negative list coverage — and return a pass/fail matrix.
tools: mcp__bing-ads__query, mcp__bing-ads__report
---

# Import Checker

Parallel import drift detection subagent for Microsoft Ads accounts with Google Ads imports.

## When Launched

Spawned by the `import-auditor` skill to check each imported campaign's settings
simultaneously. Without this agent, each campaign is checked sequentially which
is slow for accounts with many imported campaigns.

**Tell the user:** "Checking [N] imported campaigns in [B] parallel batches against the import health checklist."

## Invocation Contract

The parent skill passes:

```json
{
  "campaign_ids": ["123456789", "987654321"],
  "account_id": "12345678",
  "checklist": [
    {
      "id": "IC-1",
      "name": "MSAN Distribution",
      "priority": "Critical",
      "check": "Audience Network not enabled on search-intent campaigns",
      "expected": "disabled",
      "detect_field": "ad_distribution",
      "detect_value_fail": "audience_network_enabled"
    }
  ],
  "profile_preferences": {
    "msan_policy": "disabled",
    "search_partners": "disabled",
    "location_targeting": "people_in_only",
    "ad_schedule": "business_hours"
  }
}
```

## Batch Strategy

- **Batch size:** `ceil(total_campaigns / 3)`, capped at 10 campaigns per batch.
- **Why 3 batches:** Each campaign requires 1 structure query + 1 keyword check + 1 performance check + 1 extension check = 4 API calls. 30 campaigns = 3 batches x 10 x 4 = 120 calls. Manageable within quota.
- **Minimum:** If total campaigns <= 3, the parent skill runs sequentially.

## Workflow

For each campaign in the batch:

1. **Query campaign structure** (IA-1 from `references/bing-queries.md`):
   - Ad distribution settings (MSAN on/off)
   - Search partner settings
   - Location targeting type ("People in" vs "People in or searching for")
   - Bid strategy type and values
   - Ad scheduling settings
   - Device bid adjustments

2. **Check keyword coverage** (IA-2):
   - Count broad match keywords without negative keyword protection
   - Check for presence of negative keyword lists

3. **Verify conversions** (IA-3):
   - Pull 7-day performance data
   - Confirm at least 1 conversion recorded (UET tag is active)

4. **Check ad extensions** (IA-4):
   - Verify sitelinks, callouts, and structured snippets transferred

5. **Evaluate each check against expected values:**

   For each check in the checklist:
   ```
   actual_value = query_result[detect_field]
   expected_value = checklist_item.expected OR profile_preferences[setting]
   status = "PASS" if actual matches expected, "FAIL" otherwise
   ```

   **Import drift detection logic:**
   - If `profile_preferences` exist for a setting, compare against user's stated preference.
   - If no preference exists, compare against safe defaults:
     - MSAN: disabled (safe default for search campaigns)
     - Search partners: disabled
     - Location targeting: "People in your targeted locations"
     - Scheduling: not 24/7 (unless profile says otherwise)

6. **Estimate dollar impact for each failure:**
   - MSAN enabled on search campaign: campaign's total spend is "at-risk" (10-30% typically goes to MSAN). Use 20% as midpoint estimate.
   - Search partners enabled: estimate 10-15% of campaign spend goes to partners. Use 12% as midpoint.
   - Wrong location targeting: estimate 5-15% of spend on out-of-area traffic. Use 10% as midpoint.
   - Missing negatives on broad match: flag total broad match spend as "unprotected."
   - Missing scheduling: estimate overnight waste using `references/thresholds.md` formula (33% of daily budget for 10pm-6am default window, adjusted for profile timezone if available).

## Output Schema

```json
{
  "batch_id": "batch_1_of_2",
  "campaigns_checked": 8,
  "results": [
    {
      "campaign_id": "123456789",
      "campaign_name": "Brand - Exact [Imported]",
      "checks": [
        {
          "check_id": "IC-1",
          "name": "MSAN Distribution",
          "priority": "Critical",
          "status": "FAIL",
          "expected": "disabled",
          "actual": "enabled",
          "dollar_impact_monthly": 340.00,
          "impact_basis": "20% of campaign $1,700/mo spend",
          "ui_path": "Microsoft Advertising > Campaign 'Brand - Exact [Imported]' > Settings > Ad distribution > uncheck 'Microsoft Audience Network'"
        },
        {
          "check_id": "IC-2",
          "name": "Search Partners",
          "priority": "Critical",
          "status": "PASS",
          "expected": "disabled",
          "actual": "disabled",
          "dollar_impact_monthly": 0,
          "ui_path": null
        }
      ],
      "pass_count": 7,
      "fail_count": 2,
      "total_monthly_impact": 540.00,
      "campaign_health_pct": 78
    }
  ],
  "batch_summary": {
    "total_checks_run": 72,
    "total_passed": 58,
    "total_failed": 14,
    "failures_by_priority": {
      "Critical": 4,
      "Important": 7,
      "Optimization": 3
    },
    "total_monthly_impact": 2840.00
  }
}
```

## Result Merge Strategy

When the parent skill collects results from multiple batch agents:

1. **Union all campaign results.** Campaign IDs are unique across batches.
2. **Re-aggregate failure counts** by priority tier (Critical/Important/Optimization).
3. **Re-compute total monthly impact** across all campaigns.
4. **Sort campaigns** by total monthly impact descending (worst first).
5. **Generate consolidated fix list** — group by check type so user can fix all MSAN issues at once, then all location targeting issues, etc. (batch fixes are faster than per-campaign fixes).

## Fallback Behavior

- **If this agent fails:** The parent skill falls back to sequential checking. Already-completed batch results are preserved.
- **If a query fails for one campaign:** Mark all checks for that campaign as `"status": "QUERY_ERROR"` with `"error": "Campaign query failed"`. Continue with remaining campaigns.
- **If the profile has no preferences:** Use safe defaults for all comparisons. Note in output that results are based on defaults, not user-stated preferences.
- **Conversion check ambiguity:** If a campaign has zero conversions but low spend (<$50/week), mark conversion check as `"status": "INSUFFICIENT_DATA"` rather than `"FAIL"` — the campaign may simply lack volume.

## References

- `references/bing-queries.md` — Query IDs: IA-1 through IA-4
- `references/import-checklist.md` — Master checklist with expected values
- `references/thresholds.md` — Dollar impact estimation formulas
- `references/ui-paths.md` — Microsoft Advertising UI navigation paths
