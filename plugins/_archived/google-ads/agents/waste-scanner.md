---
name: waste-scanner
description: >-
  Subagent for parallel waste detection across campaigns. Launched by waste-detector
  skill when the account has more than 5 campaigns to analyze waste categories
  simultaneously and produce consolidated dollar-ranked findings.
tools: mcp__google-ads__query
---

# Waste Scanner

Parallel waste detection subagent for large Google Ads accounts.

## When Launched

Spawned by the `waste-detector` skill when the account has more than 5 active campaigns.
Without this agent, waste-detector runs all 8 waste queries sequentially across every campaign.
With it, campaigns are batched and scanned in parallel.

**Tell the user:** "Scanning [N] campaigns in [B] parallel batches — this is faster than sequential analysis for larger accounts."

## Invocation Contract

The parent skill passes:

```json
{
  "campaign_ids": ["123456789", "987654321", ...],
  "account_id": "customers/1234567890",
  "kpi_targets": {
    "target_cpa": 40.00,
    "target_roas": 3.5
  }
}
```

## Batch Strategy

- **Batch size:** `ceil(total_campaigns / 3)`, capped at 10 campaigns per batch.
- **Why 3 batches:** Balances parallelization benefit against API quota consumption. Each batch runs 8 queries per campaign, so a 30-campaign account = 3 batches x 10 campaigns x 8 queries = 240 API calls. This stays well within the 15K ops/day quota for a single run.
- **Minimum:** Never batch fewer than 2 campaigns. If total campaigns <= 5, the parent skill runs sequentially — this agent is not spawned.

## Workflow

For each batch:

1. **Run the 8 waste queries** from `references/gaql-queries.md` for each campaign in the batch.
   - WD-1: Non-converting keywords (30d spend > 0, conversions = 0)
   - WD-2: Low quality score keywords (QS <= 5, material spend)
   - WD-3: Display expansion on Search campaigns
   - WD-4: Budget-limited campaigns (search_budget_lost_IS > 10%)
   - WD-5: Broad match without shared negative list coverage
   - WD-6: Single-ad ad groups
   - WD-7: Zero-impression enabled campaigns (7d)
   - WD-8: Non-converting search terms (material spend, 0 conversions)

2. **Quantify each finding** using thresholds from `references/thresholds.md`:
   - Apply the type-specific dollar formula (not a blanket threshold).
   - Use KPI targets from invocation context when available (e.g., CPA > target = waste).
   - Compute monthly extrapolation: `30d_spend` for direct waste, `estimated_savings` for QS/efficiency waste.

3. **Tag severity:**
   - `HIGH`: estimated monthly impact > $500
   - `MEDIUM`: $100-$500
   - `LOW`: $25-$100
   - `INFO`: < $25

4. **Collect negative keyword candidates** (Type 8 findings) with match type recommendations.

## Result Merge Strategy

When the parent skill collects results from multiple batch agents:

1. **Union all findings.** Combine per-campaign findings from all batches into a single list.
2. **Deduplicate shared negatives.** If the same search term appears as a negative candidate across campaigns, consolidate into a shared negative list recommendation (with all source campaigns noted).
3. **Re-sort globally** by dollar impact descending. Batch-level sorting is not sufficient — the final ranking must be cross-batch.
4. **Re-aggregate totals** by waste type across all batches.
5. **Cap top findings at 10** for the executive summary, but include all findings in detailed sections.

## Output Schema

```json
{
  "batch_id": "batch_1_of_3",
  "campaigns_scanned": 10,
  "findings": [
    {
      "waste_type": "non_converting_keywords",
      "waste_type_id": 1,
      "entity_type": "keyword",
      "entity_path": "Campaign 'Brand - Exact' > Ad Group 'core-terms' > 'running shoes red'",
      "campaign_id": "123456789",
      "campaign_name": "Brand - Exact",
      "ad_group_name": "core-terms",
      "entity_name": "running shoes red",
      "match_type": "EXACT",
      "spend_30d": 847.23,
      "clicks_30d": 156,
      "conversions_30d": 0,
      "monthly_impact_estimate": 847.23,
      "severity": "HIGH",
      "recommended_action": "Pause keyword",
      "ui_path": "Google Ads > Campaign 'Brand - Exact' > Ad Group 'core-terms' > Keywords > select 'running shoes red' > Edit > Pause"
    }
  ],
  "negative_candidates": [
    {
      "term": "free running shoes",
      "source_campaigns": ["Brand - Exact", "Generic - Running"],
      "recommended_match_type": "PHRASE",
      "recommended_level": "shared_list",
      "total_spend_30d": 612.40,
      "total_clicks_30d": 89,
      "conversions_30d": 0
    }
  ],
  "totals_by_type": {
    "non_converting_keywords": {"count": 12, "monthly_impact": 2347.00},
    "low_quality_score": {"count": 5, "monthly_impact": 1200.00}
  },
  "batch_total_impact": 4892.50
}
```

## Fallback Behavior

- **If this agent fails** (timeout, MCP error, API quota hit): The parent skill logs the error and falls back to sequential processing for the remaining campaigns. Already-completed batch results are preserved.
- **If a single query fails within a batch:** Skip that waste type for the affected campaign, note it in findings as `"status": "query_failed"`, and continue with remaining queries. Do not abort the entire batch.
- **API quota awareness:** If a query returns a quota error, stop the current batch immediately and return partial results with `"quota_exhausted": true`. The parent skill will not spawn additional batches.

## References

- `references/gaql-queries.md` — Query templates WD-1 through WD-8
- `references/thresholds.md` — Detection thresholds and dollar formulas
- `references/benchmarks.md` — QS-to-CPC pressure multipliers
