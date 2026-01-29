---
name: audit
description: |
  Audit Google Ads accounts for performance issues, wasted spend, and optimization opportunities. Generates actionable recommendations report.
---

# Google Ads Account Audit

Comprehensive account health check with actionable optimization recommendations.

## Reference Files

This skill uses:
- [Performance Benchmarks](./performance-benchmarks.md) - Industry averages by vertical for comparison

---

## Required Inputs

Before starting, you MUST have:

1. **Google Ads MCP configured** - Run `/ads:setup` if not connected
2. **Customer ID** - The account to audit (10-digit ID)
3. **Date range** - Period to analyze (default: last 30 days)
4. **Industry/vertical** - For benchmark comparison

If MCP not configured:

> "Google Ads MCP is required for auditing. Run `/ads:setup` to configure credentials, then try again."

If customer ID not provided:

> "Which account should I audit? I need the 10-digit Customer ID.
>
> Use 'List my Google Ads accounts' to see available accounts."

---

## Phase 1: Account Overview

### Pull Account Summary

Use `mcp__google-ads__query` with GAQL:

```sql
SELECT
  customer.descriptive_name,
  customer.id,
  metrics.impressions,
  metrics.clicks,
  metrics.cost_micros,
  metrics.conversions,
  metrics.conversions_value
FROM customer
WHERE segments.date DURING LAST_30_DAYS
```

### Calculate Key Metrics

From the data, calculate:
- Total spend
- Total conversions
- Average CPA (cost / conversions)
- Average ROAS (conversion value / cost)
- Average CTR (clicks / impressions)

### Account Health Score

Reference: [Performance Benchmarks](./performance-benchmarks.md)

Compare account metrics to industry benchmarks:
- Green: Meeting or exceeding benchmark
- Yellow: Within 20% of benchmark
- Red: More than 20% below benchmark

---

## Phase 2: Campaign Analysis

### Pull Campaign Performance

```sql
SELECT
  campaign.name,
  campaign.id,
  campaign.status,
  campaign.advertising_channel_type,
  campaign.bidding_strategy_type,
  metrics.impressions,
  metrics.clicks,
  metrics.cost_micros,
  metrics.conversions,
  metrics.conversions_value,
  metrics.search_impression_share,
  metrics.search_budget_lost_impression_share,
  metrics.search_rank_lost_impression_share
FROM campaign
WHERE campaign.status = 'ENABLED'
  AND segments.date DURING LAST_30_DAYS
```

### Campaign Health Checks

For each enabled campaign, evaluate:

**Budget Efficiency:**
- Is daily budget being fully spent?
- Is budget lost impression share > 20%?

**Bidding Strategy:**
- Is strategy appropriate for campaign maturity?
- Are there enough conversions for target CPA/ROAS?

**Performance:**
- CTR vs benchmark
- Conversion rate vs benchmark
- CPA vs target/benchmark

### Flag Issues

| Issue | Severity | Criteria |
|-------|----------|----------|
| Budget limited | High | Budget lost IS > 30% |
| Low CTR | Medium | CTR < 50% of benchmark |
| No conversions | High | 0 conversions with $100+ spend |
| High CPA | Medium | CPA > 150% of target |
| Manual bidding | Low | Manual CPC with 30+ conversions/month |

---

## Phase 3: Ad Group Analysis

### Pull Ad Group Data

```sql
SELECT
  campaign.name,
  ad_group.name,
  ad_group.id,
  ad_group.status,
  metrics.impressions,
  metrics.clicks,
  metrics.cost_micros,
  metrics.conversions,
  metrics.average_cpc
FROM ad_group
WHERE campaign.status = 'ENABLED'
  AND ad_group.status = 'ENABLED'
  AND segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC
LIMIT 50
```

### Ad Group Health Checks

**Structure Issues:**
- Ad groups with 0 impressions
- Ad groups with high spend, 0 conversions
- CTR significantly below campaign average

**Recommendations:**
- Pause non-performing ad groups
- Restructure large ad groups
- Review keyword relevance

---

## Phase 4: Keyword Analysis (Search Campaigns)

### Pull Keyword Performance

```sql
SELECT
  campaign.name,
  ad_group.name,
  ad_group_criterion.keyword.text,
  ad_group_criterion.keyword.match_type,
  metrics.impressions,
  metrics.clicks,
  metrics.cost_micros,
  metrics.conversions,
  metrics.historical_quality_score
FROM keyword_view
WHERE campaign.status = 'ENABLED'
  AND ad_group.status = 'ENABLED'
  AND ad_group_criterion.status = 'ENABLED'
  AND segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC
LIMIT 100
```

### Keyword Health Checks

**Quality Score:**
- Keywords with QS < 5
- Keywords with QS = null (no data)

**Performance:**
- High-spend, zero-conversion keywords
- Low CTR keywords (< 1%)
- High CPC vs average

**Structure:**
- Duplicate keywords across ad groups
- Single-word broad match keywords

### Wasted Spend Calculation

Sum cost of:
- Keywords with 0 conversions and $50+ spend
- Keywords with QS < 4 and $100+ spend

---

## Phase 5: Search Terms Analysis

### Pull Search Terms Report

```sql
SELECT
  campaign.name,
  ad_group.name,
  search_term_view.search_term,
  metrics.impressions,
  metrics.clicks,
  metrics.cost_micros,
  metrics.conversions
FROM search_term_view
WHERE campaign.status = 'ENABLED'
  AND segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC
LIMIT 200
```

### Search Term Analysis

**Find Waste:**
- Irrelevant search terms with spend
- Search terms that should be negatives
- High-cost, zero-conversion terms

**Find Opportunities:**
- Converting search terms not in keywords
- High-CTR terms to add as exact match

**Negative Keyword Recommendations:**
- Group irrelevant terms by theme
- Recommend match type for each

---

## Phase 6: Ad Copy Analysis

### Pull Ad Performance

```sql
SELECT
  campaign.name,
  ad_group.name,
  ad_group_ad.ad.id,
  ad_group_ad.ad.type,
  ad_group_ad.ad_strength,
  metrics.impressions,
  metrics.clicks,
  metrics.conversions
FROM ad_group_ad
WHERE campaign.status = 'ENABLED'
  AND ad_group.status = 'ENABLED'
  AND ad_group_ad.status = 'ENABLED'
  AND segments.date DURING LAST_30_DAYS
```

### Ad Health Checks

**RSA Strength:**
- Ads with "Poor" or "Average" strength
- Ad groups with only 1 RSA

**Performance:**
- Ads with 0 conversions and 1000+ clicks
- Low CTR ads

**Recommendations:**
- Add more headline/description variations
- Test new messaging angles
- Pause underperformers

---

## Phase 7: Audience Analysis

### Pull Audience Performance

```sql
SELECT
  campaign.name,
  ad_group.name,
  ad_group_criterion.type,
  ad_group_criterion.user_list.user_list,
  metrics.impressions,
  metrics.clicks,
  metrics.conversions,
  metrics.cost_micros
FROM ad_group_audience_view
WHERE campaign.status = 'ENABLED'
  AND segments.date DURING LAST_30_DAYS
```

### Audience Analysis

**Check for:**
- Campaigns with no audience signals
- Audiences with high spend, low conversion
- Remarketing lists not being used

---

## Phase 8: Recommendations Report

### Output Format

Generate comprehensive report:

```markdown
# Google Ads Account Audit

**Account:** [Name] ([Customer ID])
**Period:** [Date range]
**Industry:** [Vertical]

---

## Executive Summary

**Account Health Score:** [X/100]

| Metric | Actual | Benchmark | Status |
|--------|--------|-----------|--------|
| CTR | X% | Y% | [status] |
| Conv Rate | X% | Y% | [status] |
| CPA | $X | $Y | [status] |
| ROAS | X | Y | [status] |

**Estimated Monthly Waste:** $[amount]
**Top Opportunities:** [1-2 sentence summary]

---

## Critical Issues (Fix Immediately)

### 1. [Issue Title]
**Impact:** [High/Medium/Low]
**Affected:** [campaigns/ad groups/keywords]
**Recommendation:** [specific action]

### 2. [Issue Title]
...

---

## Optimization Opportunities

### Campaign Level
- [Recommendation 1]
- [Recommendation 2]

### Ad Group Level
- [Recommendation 1]
- [Recommendation 2]

### Keyword Level
- [Recommendation 1]
- [Recommendation 2]

### Ad Copy
- [Recommendation 1]
- [Recommendation 2]

---

## Wasted Spend Analysis

### Keywords to Pause
| Keyword | Spend | Conversions | Reason |
|---------|-------|-------------|--------|
| [kw] | $X | 0 | [reason] |

**Total potential savings:** $[amount]/month

### Negative Keywords to Add
| Term | Match Type | Reason |
|------|------------|--------|
| [term] | [type] | [reason] |

---

## Search Terms Opportunities

### Add as Keywords
| Search Term | Current Conv | Recommended Match |
|-------------|--------------|-------------------|
| [term] | X | Exact |

### Add as Negatives
| Search Term | Spend | Reason |
|-------------|-------|--------|
| [term] | $X | [reason] |

---

## Next Steps

**This Week:**
1. [ ] [Action item]
2. [ ] [Action item]

**This Month:**
1. [ ] [Action item]
2. [ ] [Action item]

**Ongoing:**
1. [ ] [Action item]

---

## Appendix: Raw Data

[Include key data tables if requested]
```

---

## Quality Checklist

Before delivering:
- [ ] All GAQL queries executed successfully
- [ ] Metrics compared to industry benchmarks
- [ ] Wasted spend identified and quantified
- [ ] Specific action items provided
- [ ] Recommendations prioritized by impact
- [ ] No generic advice - all specific to this account

---

## What You Don't Do

- Audit without MCP connection
- Use generic recommendations not based on data
- Ignore industry context
- Recommend changes without explaining why
- Run mutations (audit is read-only)
- Promise specific performance improvements
