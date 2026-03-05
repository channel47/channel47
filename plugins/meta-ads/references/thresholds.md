# Detection Thresholds — Meta Ads

Apply these thresholds consistently. Do not invent alternatives.

## Creative fatigue thresholds

| Metric | Warning | Critical | Action |
|--------|---------|----------|--------|
| Frequency (7d) | > 3.0 | > 5.0 | Refresh creative or narrow audience |
| CTR decline from peak | > 20% drop | > 40% drop | Replace creative |
| CPM increase from baseline | > 30% increase | > 50% increase | Refresh creative or expand audience |
| CPA increase from baseline | > 25% increase | > 50% increase | Pause ad or refresh |

## Lifecycle stage definitions

Used by creative-fatigue skill. See `fatigue-model.md` for full model.

| Stage | Criteria |
|-------|----------|
| Testing | < 500 impressions or < 3 days live |
| Rising | CTR trending up, CPA trending down, frequency < 2.0 |
| Peak | Best 7d CPA window, frequency 1.5-3.0, stable CTR |
| Fatiguing | CTR declining > 15% from peak, frequency > 3.0, CPA rising |
| Dead | CTR < 50% of peak OR frequency > 6.0 OR CPA > 2x target |

## Waste detection thresholds

### Type 1: High-frequency, low-conversion ad sets
- **Detection**: Frequency > 4.0 AND conversions = 0 in 7 days
- **Dollar waste**: Total ad set spend in the high-frequency period

### Type 2: Audience Network placements
- **Detection**: Audience Network placement enabled with poor performance
- **Dollar waste**: Audience Network spend where CPA > 2x campaign average or zero conversions
- **Threshold**: Flag when Audience Network CPA > 150% of other placements

### Type 3: Broad audience with no exclusions
- **Detection**: Audience size > 10M with no custom audience exclusions
- **Dollar waste**: Estimate 10-20% of spend on irrelevant reach

### Type 4: Learning Limited campaigns
- **Detection**: Campaign/ad set status = "Learning Limited"
- **Dollar waste**: CPA premium during extended learning. Estimate 20-30% CPA inflation vs post-learning baseline.

### Type 5: Overlapping audiences
- **Detection**: Multiple ad sets targeting audiences with > 30% overlap
- **Dollar waste**: Internal auction competition premium. Estimate 10-15% of overlapping ad set spend.

### Type 6: Non-converting placements
- **Detection**: Specific placements (Instant Articles, Right Column, etc.) with spend > $25 and zero conversions
- **Dollar waste**: Direct spend on non-converting placements

### Type 7: Stale creative (> 30 days, declining performance)
- **Detection**: Ad running > 30 days with CTR < 50% of first-week CTR
- **Dollar waste**: Current daily spend × estimated remaining run days at degraded efficiency

### Type 8: Conversion window mismatch
- **Detection**: 1-day click attribution on campaigns with > 7-day consideration cycle
- **Dollar waste**: Not direct waste — but underreporting leads to premature pausing of working campaigns. Flag as INVESTIGATE.

## Anomaly detection thresholds

Same formula structure as Google/Bing (see anomaly logic in morning-brief skill):

| Condition | Flag |
|-----------|------|
| `abs(deviation_pct) > 0.20` AND `abs(dollar_impact) > $10` | Anomaly |
| `abs(ctr_deviation_pct) > 0.25` | CTR anomaly (no dollar gate) |
| Frequency spike > 50% day-over-day | Audience saturation warning |
| CPM spike > 40% from 7d baseline | Auction competition alert |

## Severity tags

| Dollar Impact (monthly) | Severity |
|--------------------------|----------|
| > $500 | `HIGH` |
| $100 - $500 | `MEDIUM` |
| $25 - $100 | `LOW` |
| < $25 | `INFO` |

## Learning phase thresholds

- Standard campaigns: ~50 conversions in 7 days to exit learning
- Value optimization: ~50 purchase events in 7 days
- Lead gen: ~50 leads in 7 days
- "Learning Limited" = insufficient volume to exit learning in expected timeframe

## Frequency benchmarks by objective

| Objective | Acceptable Frequency (7d) | Warning | Critical |
|-----------|--------------------------|---------|----------|
| Conversions | 1.5 - 3.0 | 3.0 - 5.0 | > 5.0 |
| Traffic | 1.0 - 2.5 | 2.5 - 4.0 | > 4.0 |
| Awareness | 2.0 - 4.0 | 4.0 - 7.0 | > 7.0 |
| Engagement | 1.5 - 3.0 | 3.0 - 5.0 | > 5.0 |
