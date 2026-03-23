# Meta Insight Query Templates — Waste Detection

Query templates for each of the 8 waste types. These map to brijr/meta-mcp tools.

## 1. Audience Overlap

**Tool:** `mcp__meta-ads__list_ad_sets` + `mcp__meta-ads__get_audience_insights`

**What to pull:**
- All active ad sets with targeting details.
- Custom audience IDs and interest targeting per ad set.
- Compare targeting across ad sets within same campaign and across campaigns.

**Detection logic:**
- Same custom audience used in multiple ad sets without mutual exclusions.
- Overlapping interest stacks (>50% shared interests).
- Same lookalike audience at different percentages without exclusions (e.g., 1% and 3% both active without 1% excluded from 3%).

**Metrics:** CPM per overlapping ad set pair, impressions overlap estimate.

## 2. Creative Fatigue

**Tool:** `mcp__meta-ads__list_ads` + `mcp__meta-ads__get_creative_performance`

**What to pull:**
- All active ads with 7d and 30d metrics.
- Fields: frequency, CTR, impressions, CPM, spend.

**Detection logic:**
- 7d frequency > 3.0 AND 7d CTR < 80% of 30d CTR.
- CPM rising >10% (7d vs 30d) while audience size stable.

**Date ranges:** 7d (this_week), 30d (last_30d), compare 7d vs prior 7d for trend.

## 3. Placement Bleed

**Tool:** `mcp__meta-ads__get_insights` with placement breakdown

**What to pull:**
- Campaign-level insights broken down by placement (publisher_platform + platform_position).
- Fields: spend, impressions, clicks, CTR, conversions, CPA, CPM per placement.

**Detection logic:**
- Audience Network spend > 10% of campaign spend AND CPA > 2x campaign average.
- Any placement with spend > 15% of campaign AND CPA > 1.5x campaign average.

**Date range:** last_30d for reliable volume.

## 4. Non-Converting Ad Sets

**Tool:** `mcp__meta-ads__list_ad_sets` + `mcp__meta-ads__get_insights`

**What to pull:**
- All active ad sets with 7d and 14d performance.
- Fields: spend, conversions, CPA.

**Detection logic:**
- 7d spend > 2x target CPA AND 0 conversions.
- 14d spend > 5x target CPA AND <2 conversions.
- Exclude ad sets in Learning phase (delivery_info status).

**Date ranges:** 7d (primary), 14d (secondary for borderline cases).

## 5. Learning Phase Churn

**Tool:** `mcp__meta-ads__list_ad_sets`

**What to pull:**
- All ad sets with delivery status.
- Edit history / configuration change indicators.

**Detection logic:**
- Delivery status = "Learning Limited".
- Multiple status transitions in past 14 days (entering/exiting Learning).
- Budget or targeting changes >2x in past 7 days.

**Quantification:** Spend during Learning at estimated 20-30% CPA premium.

## 6. Broad Targeting Without Exclusions

**Tool:** `mcp__meta-ads__list_ad_sets` + `mcp__meta-ads__list_audiences`

**What to pull:**
- All ad sets targeting criteria.
- Custom audience exclusion lists per ad set.
- Campaign objective (identify prospecting vs retargeting).

**Detection logic:**
- Prospecting campaigns (non-retargeting objective) with no Custom Audience exclusions.
- Ad sets using Broad/Advantage+ without any exclusions.

**Quantification:** Estimated % of impressions reaching existing customers * CPA.

## 7. Frequency Cap Violations

**Tool:** `mcp__meta-ads__list_campaigns` + `mcp__meta-ads__list_ad_sets`

**What to pull:**
- Campaigns with Reach or Brand Awareness objective.
- Ad set level frequency cap settings.
- 7d frequency metrics.

**Detection logic:**
- Reach/Awareness campaign with no frequency cap setting.
- 7d average frequency > 2.0 on uncapped campaigns.

**Quantification:** Excess impressions beyond 2.0 frequency * CPM / 1000.

## 8. Stale Lookalike Seeds

**Tool:** `mcp__meta-ads__list_audiences` + `mcp__meta-ads__get_audience_insights`

**What to pull:**
- All lookalike audiences with source audience details.
- Source audience creation date, last updated date, size.

**Detection logic:**
- Source audience last updated >90 days ago.
- Source audience size <1,000.
- Lookalike percentage >5% (poor signal quality at high percentages).

**Quantification:** Spend on stale-seeded lookalikes * estimated 10-25% CPA premium vs fresh seeds.
