# Waste Detector Detection Thresholds & Dollar Formulas

Apply these thresholds and formulas consistently. Do not invent alternatives.

## Detection thresholds by waste type

### Type 1: Non-converting keywords

- **Threshold**: `metrics.cost > 0` AND `metrics.conversions = 0` AND
  `metrics.cost >= campaign_avg_cpa` (30d window).
- **Fallback** when no CPA available: `metrics.cost >= $25`.
- **Dollar waste**: direct spend on the keyword = `metrics.cost`.

### Type 2: Low quality score keywords spending

- **Threshold**: `quality_score <= 5` AND `metrics.cost > $10` (30d).
- **Dollar waste**: estimate CPC premium using benchmarks.md QS-to-CPC table:
  `waste = metrics.cost * (1 - 1/cpc_multiplier)`.
  Example: QS 3 keyword spending $100 at ~3x CPC → `$100 * (1 - 1/3) = $66.67` waste.

### Type 3: Display expansion on Search

- **Threshold**: `target_content_network = TRUE` on any SEARCH campaign with spend.
- **Dollar waste**: total campaign cost on content network. Since the query already
  filters to these campaigns, use `metrics.cost` as the at-risk amount. Flag the full
  spend as at-risk; actual Display portion requires network-segmented data.

### Type 4: Budget-limited campaigns

- **Threshold**: `search_budget_lost_impression_share > 0.10` (10%+).
- **Dollar waste**: not directly wasted — this is missed opportunity. Estimate:
  `potential_missed_conversions = metrics.conversions * (search_budget_lost_IS / (1 - search_budget_lost_IS))`.
  `potential_missed_value = potential_missed_conversions * avg_conv_value`.
- **Severity**: `HIGH` when IS lost > 25%, `MEDIUM` when 10-25%.

### Type 5: Broad match without negative list

- **Threshold**: campaign has broad-match keywords spending AND no shared negative
  keyword list attached.
- **Dollar waste**: total broad-match spend in unprotected campaigns = at-risk amount.
  Not all is waste, but exposure is unmanaged.

### Type 6: Single-ad ad groups

- **Threshold**: ad group has exactly 1 ENABLED ad (ignore PAUSED).
- **Dollar waste**: estimate via ad testing lift assumption from benchmarks.md.
  `modeled_upside = ad_group_cost * 0.10` (10% CTR lift → 10% efficiency gain).

### Type 7: Zero-impression enabled campaigns

- **Threshold**: `campaign.status = ENABLED` AND `metrics.impressions = 0` over
  LAST_7_DAYS AND `campaign_budget.amount_micros > 0`.
- **Dollar waste**: no direct spend waste, but operational drag. Flag as `INFO`.

### Type 8: Non-converting search terms

- **Threshold**: `metrics.cost > 0` AND `metrics.conversions = 0` AND
  `metrics.cost >= $10` (30d).
- **Dollar waste**: direct spend = `metrics.cost`.
- Note: "semantic mismatch" is determined by comparing search term text against the
  campaign/ad group theme. This requires contextual judgment — look for terms that are
  topically unrelated to the ad group's keyword set, not just non-converting.

## Severity tags

| Dollar Impact (monthly) | Severity |
|--------------------------|----------|
| > $500 | `HIGH` |
| $100 - $500 | `MEDIUM` |
| $25 - $100 | `LOW` |
| < $25 | `INFO` |

## Remediation mapping

| Waste Type | Primary Remediation | Script Function |
|------------|--------------------|-----------------|
| 1. Non-converting keywords | Pause keyword or reduce bid | `pause_entities()` |
| 2. Low QS keywords | Improve ad relevance + landing page; pause if QS <= 3 | `pause_entities()` |
| 3. Display on Search | Disable content network targeting | Manual UI change (recommend) |
| 4. Budget-limited | Increase budget or reduce waste elsewhere to fund | No mutation — recommendation |
| 5. Broad without negatives | Add shared negative list | Manual UI (recommend shared list) |
| 6. Single-ad groups | Create additional RSA variants | `create_rsa()` (if scope warrants) |
| 7. Zero-impression campaigns | Investigate setup; pause if abandoned | `pause_entities()` |
| 8. Non-converting search terms | Add as negative keywords | `add_negative_keywords()` |

## Total waste calculation

```python
total_waste = sum(finding["dollar_waste"] for finding in findings if finding["severity"] != "INFO")
```

Report this as "Total Estimated Recoverable Waste" with a note that estimates use
benchmark assumptions where direct measurement is unavailable.
