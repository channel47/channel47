# Troubleshooting Guide

## Problem: CPA Spiking on a Previously Good Campaign

### Diagnosis Steps
1. Check if a creative was disapproved (asset group status)
2. Review search terms report for new irrelevant queries
3. Check auction insights for new competitors
4. Verify landing page is loading (check landing page report for mobile speed)
5. Review device breakdown — has one device's CPA blown up?

### Common Fixes
- **Disapproved creative:** Appeal the policy decision, replace creative with compliant variant
- **Bad search terms:** Add negative keywords immediately
- **New competitor:** Raise tCPA by $5-$10 to compete, or accept lower volume
- **Landing page issue:** Fix the page, not the ads
- **Device-specific spike:** Create a device-exclusion campaign variant

## Problem: Campaign Stuck in "Learning" for 7+ Days

### Diagnosis Steps
1. Check if campaign has enough daily budget for 10+ conversions at tCPA
2. Verify tCPA isn't set too low (campaign can't find conversions at that price)
3. Check if audience signals are too narrow
4. Review if the landing page converts at all (check other campaigns hitting the same page)

### Common Fixes
- **Budget too low:** Budget should be at least 10x tCPA daily
- **tCPA too aggressive:** Increase tCPA by 15-25% to give room to learn
- **Narrow audience:** Broaden audience signals or remove overly restrictive ones
- **Landing page broken:** Test the page manually, check GA4

## Problem: High Impressions, Low CTR (PMax)

### Diagnosis Steps
1. Check which placements are generating impressions (placements report)
2. Review image and video assets for quality
3. Verify headlines include specific price/offer hooks
4. Compare CTR across asset groups

### Common Fixes
- **Display/app network dilution:** This is normal in PMax. Focus on conversion metrics, not CTR
- **Weak creative:** Update images with clearer text overlays and value prop
- **Generic headlines:** Replace with price-specific, audience-specific headlines
- **One bad asset group dragging average:** Pause the low-performing asset group

## Problem: Good CPA but ROAS Below 0.80

### Diagnosis Steps
1. Verify conversion value tracking is correct
2. Check if the offer price in the landing page matches what's being tracked
3. Review if the conversion action is configured correctly in Google Ads
4. Compare cost/conv vs conv value — is there a disconnect?

### Common Fixes
- **Tracking issue:** Fix the conversion value parameter in the tag
- **Lower-value conversions:** Some audiences convert to lower-priced offers. Segment.
- **Product mix issue:** If selling multiple products, check which product converts

## Problem: Demand Gen Campaigns Not Converting

### Diagnosis Steps
1. Check if video creative is approved and serving
2. Review tCPA — likely needs to be 2-3x PMax target initially
3. Verify landing page works from YouTube click-through
4. Check frequency — are you over-serving the same users?

### Common Fixes
- **tCPA too low:** Set Demand Gen tCPA at 50-100% above PMax target
- **Video quality:** Bad creative = bad performance. Test new video.
- **Switch to Maximize Conversions:** Remove tCPA entirely to gather data first
- **Audience too broad:** Add specific audience signals (in-market, custom intent)

## Problem: Campaign Spending on Brand Terms

### Diagnosis Steps
1. Pull search terms report and filter for brand name
2. Check if negative keywords for brand are in place
3. Verify negative keyword match types are correct

### Common Fixes
- Add brand terms as exact match negatives on all non-brand campaigns
- Create a shared negative keyword list for brand terms
- If brand terms are converting well, create a dedicated brand campaign at lower tCPA

## Quick-Fix Decision Matrix

| Symptom | First Action | If No Improvement in 3 Days |
|---------|-------------|---------------------------|
| CPA 20%+ above target | Decrease tCPA $5-$8 | Decrease budget 30% |
| CPA 50%+ above target | Decrease budget 40% | Pause campaign |
| Zero conversions 3+ days | Check landing page + creative | Pause and reallocate |
| CTR below 1% | Update headlines + images | Pause weakest asset groups |
| ROAS below 0.60 | Verify tracking setup | Pause and investigate |
| "Limited by budget" + good CPA | Increase budget 50% | Create duplicate campaign |
| "Bidding strategy learning" | Wait (do nothing) | Increase tCPA 10% on day 7 |
