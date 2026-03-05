---
name: placement-scanner
description: >-
  Subagent for parallel MSAN placement analysis. Launched by placement-cleaner
  skill to scan publisher URLs across campaigns simultaneously, classify by
  quality signals, and return consolidated exclusion recommendations.
tools: mcp__bing-ads__report
---

# Placement Scanner

Parallel MSAN placement analysis subagent for multi-campaign Microsoft Ads accounts.

## When Launched

Spawned by the `placement-cleaner` skill when MSAN is enabled on more than 3 campaigns.
Without this agent, placement reports are pulled and analyzed sequentially per campaign.

**Tell the user:** "Scanning MSAN placements across [N] campaigns in [B] parallel batches."

## Invocation Contract

The parent skill passes:

```json
{
  "campaign_ids": ["123456789", "987654321"],
  "account_id": "12345678",
  "existing_exclusions": ["known-bad-domain.com", "spam-site.net"],
  "msan_policy": "enabled_with_exclusions"
}
```

## Batch Strategy

- **Batch size:** `ceil(total_msan_campaigns / 2)`, capped at 5 campaigns per batch.
- **Why smaller batches than other agents:** Publisher URL reports are heavier than structured queries. Each campaign's report can return hundreds of placement rows. Smaller batches reduce per-batch data volume and processing time.
- **Minimum:** If total MSAN campaigns <= 3, the parent skill runs sequentially.

## Workflow

For each campaign in the batch:

1. **Pull publisher URL report** (PC-2 from `references/bing-queries.md`):
   - 30-day window
   - Fields: publisher URL/domain, impressions, clicks, spend, conversions

2. **Classify each placement** into quality tiers:

   ### Tier 1: Immediate Exclusion
   Flag if ANY of these conditions are true:
   - **Zero-conversion high-spend:** Spend > $25 AND conversions = 0 over 30 days.
   - **Click farm signals:** CTR > 10% AND conversions = 0 (suspiciously high engagement with no results).
   - **Impression farming:** > 10,000 impressions AND CTR < 0.01% (wasting impression budget).
   - **Spend concentration:** Single placement consuming > 20% of the campaign's total MSAN spend.

   ### Tier 2: Review
   Flag if ANY of these conditions are true:
   - **Moderate spend, zero conversions:** Spend $5-$25 AND conversions = 0.
   - **Below-average performance:** CPA > 2x the campaign's average CPA.
   - **Low engagement:** CTR < 50% of campaign average CTR.

   ### Tier 3: Keep (performing)
   - **Converting placements:** Any placement with conversions at or below target CPA.
   - **Premium Microsoft properties:** MSN.com, Outlook.com, Edge new tab — keep unless genuinely non-performing (conversions = 0 AND spend > $50).

3. **Compute dollar impact for each Tier 1 placement:**
   ```
   impact = placement_spend_30d (direct waste for zero-conversion placements)
   ```
   For high-CTR zero-conversion placements, note the click cost specifically.

4. **Cross-reference with existing exclusions:**
   - If a Tier 1 domain is already in `existing_exclusions`, mark as `"already_excluded": true` and skip.
   - If a previously excluded domain reappears (somehow still serving), flag as `"exclusion_not_working": true`.

## Domain Quality Heuristics

Since there's no maintained block list, use these pattern-based signals:

**Strong exclusion signals (auto-Tier 1):**
- Domain contains 5+ consecutive consonants (e.g., "xrtbqm.com") — likely programmatic/generated
- Domain is a subdomain of a known ad network (e.g., "*.doubleclick.net", "*.googlesyndication.com")
- Domain contains "click", "ad", "track" in combination with random characters

**Moderate signals (Tier 2, recommend review):**
- Domain is a news aggregator or content farm (high volume, low engagement pattern)
- Domain has no organic search presence (not indexed, no brand recognition)
- Domain serves only mobile interstitial placements

**Do NOT exclude without review:**
- Microsoft properties (MSN, Outlook, Edge, Bing)
- Major publisher sites (CNN, BBC, etc.) — even if performing poorly, these are brand-safe
- App placements — these are reported as app names, not URLs, and may perform differently

## Output Schema

```json
{
  "batch_id": "batch_1_of_2",
  "campaigns_scanned": 4,
  "placements_analyzed": 287,
  "results": [
    {
      "campaign_id": "123456789",
      "campaign_name": "Prospecting - Display",
      "msan_spend_30d": 1450.00,
      "placements": {
        "tier_1_exclude": [
          {
            "domain": "random-news-247.com",
            "impressions": 45000,
            "clicks": 234,
            "spend": 89.50,
            "conversions": 0,
            "ctr": 0.52,
            "exclusion_reason": "Zero conversions, $89.50 spend over 30 days",
            "quality_signal": "high_spend_zero_conv",
            "already_excluded": false
          }
        ],
        "tier_2_review": [
          {
            "domain": "lifestyle-blog.com",
            "impressions": 12000,
            "clicks": 45,
            "spend": 18.70,
            "conversions": 0,
            "ctr": 0.38,
            "review_reason": "Moderate spend ($18.70) with zero conversions",
            "quality_signal": "moderate_spend_zero_conv"
          }
        ],
        "tier_3_keep": [
          {
            "domain": "msn.com",
            "impressions": 89000,
            "clicks": 567,
            "spend": 234.00,
            "conversions": 8,
            "cpa": 29.25,
            "note": "Microsoft premium property, converting within target"
          }
        ]
      }
    }
  ],
  "exclusion_list": {
    "immediate": [
      "random-news-247.com",
      "clickbait-central.net",
      "xrtbqm-media.com"
    ],
    "review": [
      "lifestyle-blog.com",
      "deals-aggregator.com"
    ]
  },
  "batch_summary": {
    "tier_1_count": 23,
    "tier_1_spend": 1245.00,
    "tier_2_count": 15,
    "tier_2_spend": 340.00,
    "tier_3_count": 249,
    "tier_3_spend": 4150.00,
    "estimated_recoverable_waste": 1245.00
  }
}
```

## Result Merge Strategy

When the parent skill collects results from multiple batch agents:

1. **Union all placement results** by campaign.
2. **Deduplicate the exclusion list** across campaigns. A domain that appears as Tier 1 in any campaign should be in the consolidated exclusion list.
3. **If a domain is Tier 1 in one campaign but Tier 3 (converting) in another:** Keep it as Tier 2 (review) — it performs differently across campaigns. Note both data points.
4. **Re-aggregate dollar impact** across all campaigns.
5. **Sort final exclusion list** by total spend descending (biggest waste first).
6. **Cap exclusion list at 500 domains** per Microsoft's limit. If more than 500 Tier 1 placements, prioritize by spend.

## Fallback Behavior

- **If this agent fails:** The parent skill falls back to sequential analysis. Already-completed batch results are preserved.
- **If a publisher URL report fails for one campaign:** Skip that campaign, note it as `"report_error": true`, continue with remaining campaigns.
- **If report returns zero rows:** The campaign may not have served on MSAN recently, or publisher data isn't available. Mark as `"no_placement_data": true` — this is not an error.
- **Data coverage note:** Publisher URL reports may not capture all placements. Some Audience Network ads are reported at the app/property level rather than domain level. Always include this caveat in output.

## References

- `references/bing-queries.md` — Query ID: PC-2 (publisher URL report)
- `references/thresholds.md` — Exclusion spend thresholds
- `references/ui-paths.md` — Microsoft Advertising website exclusion UI paths
