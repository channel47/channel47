# Detection Thresholds & Dollar Formulas — Microsoft Ads

Apply these thresholds and formulas consistently. Do not invent alternatives.

## Detection thresholds by waste type

### Type 1: MSAN enabled

- **Detection**: Campaign has Audience Network distribution enabled on search-intent campaigns.
- **Dollar waste**: Total MSAN spend = at-risk amount. If network-segmented data is available, use actual Audience Network spend. Otherwise, estimate 10-30% of total campaign spend.
- **Severity**: HIGH when campaign spend > $500/mo, MEDIUM when $100-500/mo.

### Type 2: Search partners enabled

- **Detection**: Campaign has syndicated search partner network enabled.
- **Dollar waste**: Partner network spend. Estimate using network-level performance if available, otherwise flag 10-20% of campaign spend as at-risk.
- **Severity**: MEDIUM for most campaigns.

### Type 3: Broad match without negatives

- **Detection**: Keywords with match_type = Broad spending money AND campaign lacks negative keyword coverage.
- **Dollar waste**: Total broad match keyword spend in unprotected campaigns.
- **Why critical on Bing**: Google Ads shared negative keyword lists do not transfer during import. Bing's close variant matching is more aggressive than Google's.

### Type 4: Auto-import overwriting

- **Detection**: Compare campaign settings against profile Import Config. Look for settings that reverted to Google defaults.
- **Dollar waste**: Sum of Type 1 + Type 2 waste that was re-enabled by import, plus any bid strategy drift.

### Type 5: Budget burning overnight

- **Detection**: Campaigns without ad scheduling running 24/7 with overnight spend and zero/near-zero conversions.
- **Dollar waste**: Overnight spend estimate. Use ratio of overnight hours (e.g., 10pm-6am = 33% of day) applied to daily spend when hourly data is unavailable.

### Type 6: Bot traffic

- **Detection**:
  - CTR > 15% combined with zero conversions.
  - Clicks > 50/day from campaigns with zero conversions.
  - Single device type > 80% of clicks with zero conversions.
- **Dollar waste**: Total spend on flagged entities.
- **Note**: Signals only, not confirmations. Check Microsoft's Invalid Clicks report.

### Type 7: Location targeting expanding

- **Detection**: Campaigns set to "People in or searching for" instead of "People in".
- **Dollar waste**: Estimate 5-15% of campaign spend reaching users outside physical target area.

## Severity tags

| Dollar Impact (monthly) | Severity |
|--------------------------|----------|
| > $500 | `HIGH` |
| $100 - $500 | `MEDIUM` |
| $25 - $100 | `LOW` |
| < $25 | `INFO` |

## Remediation mapping

| Waste Type | Primary Action | UI Path |
|------------|---------------|---------|
| 1. MSAN enabled | Disable Audience Network | See ui-paths.md > Campaign Settings > Disable MSAN |
| 2. Search partners | Disable syndicated search | See ui-paths.md > Campaign Settings > Disable search partners |
| 3. Broad without negatives | Add negative keywords | See ui-paths.md > Negative Keywords > Add campaign-level negatives |
| 4. Auto-import overwriting | Review/disable auto-import | See ui-paths.md > Import > Review auto-import schedule |
| 5. Overnight burn | Set ad scheduling | See ui-paths.md > Campaign Settings > Set ad scheduling |
| 6. Bot traffic | Review publisher URLs, file dispute | See ui-paths.md > Reports > Publisher URL report |
| 7. Location targeting | Change to "People in" | See ui-paths.md > Campaign Settings > Set physical location targeting |

## Total waste calculation

```python
total_waste = sum(finding["dollar_waste"] for finding in findings if finding["severity"] != "INFO")
```

Report as "Total Estimated Recoverable Waste" with a note that estimates use benchmark assumptions where direct measurement is unavailable.

## Import-specific thresholds

For import-auditor, use the same severity tags. Additional context:

- **Critical items** (MSAN, search partners, location targeting, conversion tracking): Flag as HIGH regardless of spend if the setting is wrong. These affect all future spend.
- **Important items** (broad match, negatives, scheduling, device bids): Use spend-based severity.
- **Optimization items** (bid strategy, extensions, naming): Flag as LOW or INFO.
