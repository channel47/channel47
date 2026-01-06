---
title: "GAQL Queries Every Google Ads Manager Should Know"
description: "A practical guide to Google Ads Query Language. Learn the queries that surface wasted spend, find optimization opportunities, and automate your reporting."
date: 2026-01-06
tags:
  - google-ads
  - gaql
  - automation
author: Channel47
---

If you've ever wished you could just *ask* Google Ads what's going wrong with your account, GAQL is the closest thing to that. It's the query language that powers the Google Ads API, and learning it changes how you work.

This isn't a comprehensive reference. It's the queries I actually use—the ones that find problems faster than clicking through the UI ever could.

## What Is GAQL?

Google Ads Query Language (GAQL) is a SQL-like language for extracting data from Google Ads accounts. Unlike the web interface, which shows you what Google thinks you want to see, GAQL lets you ask specific questions and get precise answers.

```sql
SELECT
  campaign.name,
  metrics.cost_micros,
  metrics.conversions
FROM campaign
WHERE metrics.cost_micros > 0
  AND segments.date DURING LAST_30_DAYS
```

That query returns every campaign that spent money in the last 30 days, with its cost and conversions. Simple, direct, no clicking around.

## Why This Matters for AI Workflows

Here's where it gets interesting: when you connect Claude to the Google Ads API via [MCP](/tools/google-ads), GAQL becomes your primary interface. Instead of navigating a complex UI or building reports manually, you write queries—or better, you describe what you want to know and let Claude write the queries for you.

The combination is powerful:

- **You** understand your business goals
- **GAQL** extracts the exact data you need
- **Claude** analyzes patterns humans miss

But Claude can only work with the data you give it. Bad queries produce bad analysis. That's why understanding GAQL fundamentals matters even if you never write a query manually.

## The Queries That Actually Matter

### Finding Wasted Spend

The first thing I run on any account audit:

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
WHERE metrics.cost_micros > 10000000
  AND metrics.conversions = 0
  AND segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC
LIMIT 100
```

This surfaces search terms that have spent more than $10 (cost is in micros, so 10000000 = $10) without a single conversion. It's usually shocking how much spend accumulates on irrelevant queries.

**Pro tip:** When working with the [Google Ads Audit skill](/skills/google-ads), this query is automated. The skill knows to run it early and flag the worst offenders.

### Quality Score Decay

Quality Score problems compound over time. This query finds keywords where your QS has dropped:

```sql
SELECT
  campaign.name,
  ad_group.name,
  ad_group_criterion.keyword.text,
  ad_group_criterion.quality_info.quality_score,
  ad_group_criterion.quality_info.creative_relevance,
  ad_group_criterion.quality_info.landing_page_experience,
  ad_group_criterion.quality_info.search_predicted_ctr,
  metrics.impressions,
  metrics.clicks,
  metrics.cost_micros
FROM keyword_view
WHERE ad_group_criterion.quality_info.quality_score < 5
  AND metrics.impressions > 1000
  AND segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC
```

Low Quality Score + high spend = money on fire. The query also pulls the component scores (creative relevance, landing page experience, predicted CTR) so you know *where* to fix things.

### Performance Max Visibility

Performance Max campaigns are black boxes, but GAQL opens them slightly:

```sql
SELECT
  campaign.name,
  asset_group.name,
  asset_group_listing_group_filter.type,
  metrics.impressions,
  metrics.clicks,
  metrics.conversions,
  metrics.cost_micros
FROM asset_group_listing_group_filter
WHERE campaign.advertising_channel_type = 'PERFORMANCE_MAX'
  AND segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC
```

This shows which asset groups and listing group filters are actually driving performance. It won't tell you everything, but it tells you more than the UI does.

### Budget Pacing

Nothing kills a campaign like running out of budget at 2pm:

```sql
SELECT
  campaign.name,
  campaign.budget.amount_micros,
  campaign.budget.delivery_method,
  metrics.cost_micros
FROM campaign
WHERE campaign.status = 'ENABLED'
  AND segments.date = TODAY
```

Run this throughout the day to see which campaigns are pacing fast. Compare `metrics.cost_micros` to `campaign.budget.amount_micros` to calculate percentage spent.

### Audience Performance Deep Dive

For campaigns using audience targeting:

```sql
SELECT
  campaign.name,
  ad_group.name,
  ad_group_criterion.audience.audience,
  metrics.impressions,
  metrics.clicks,
  metrics.conversions,
  metrics.cost_micros,
  metrics.conversions_value
FROM audience_view
WHERE metrics.impressions > 100
  AND segments.date DURING LAST_30_DAYS
ORDER BY metrics.conversions_value DESC
```

This reveals which audiences actually convert versus which ones just burn budget. Essential for refining targeting.

## Common GAQL Patterns

A few patterns that come up constantly:

### Date Ranges

```sql
-- Predefined ranges
segments.date DURING LAST_7_DAYS
segments.date DURING LAST_30_DAYS
segments.date DURING THIS_MONTH
segments.date DURING LAST_MONTH

-- Custom range
segments.date BETWEEN '2026-01-01' AND '2026-01-31'
```

### Filtering Enabled Items Only

```sql
WHERE campaign.status = 'ENABLED'
  AND ad_group.status = 'ENABLED'
```

Always include this unless you specifically want paused/removed entities.

### Conversion Thresholds

```sql
-- At least some conversions
metrics.conversions > 0

-- Significant conversion volume
metrics.conversions >= 10

-- Conversion rate calculation (do this in post-processing)
metrics.conversions / metrics.clicks
```

### Cost Calculations

Remember that all cost values are in micros (millionths of the currency unit):

```sql
-- $100 minimum spend
metrics.cost_micros > 100000000

-- Or filter in your code after retrieving
cost_dollars = metrics.cost_micros / 1000000
```

## Building Your Query Toolkit

Start with these five queries and you'll handle 80% of account analysis:

1. **Wasted spend finder** (search terms with spend, no conversions)
2. **Quality Score audit** (keywords with QS < 5 and significant spend)
3. **Budget pacing check** (today's spend vs. daily budget)
4. **Audience performance** (which audiences convert)
5. **Campaign overview** (all enabled campaigns with core metrics)

Once you're comfortable with these, the [official GAQL documentation](https://developers.google.com/google-ads/api/docs/query/overview) covers every available field and resource.

## From Queries to Insights

Raw GAQL output is just data. The value comes from interpretation. That's where the combination of GAQL + Claude becomes more than the sum of its parts.

When you use the [Google Ads MCP server](/tools/google-ads), you can run these queries and immediately ask Claude to:

- Identify patterns across multiple queries
- Compare current performance to historical benchmarks
- Prioritize which issues to fix first based on potential impact
- Generate specific recommendations with supporting data

The [Google Ads Audit skill](/skills/google-ads) packages this workflow into a repeatable process. It knows which queries to run, what the outputs mean, and how to present findings in a way that's actually actionable.

## What's Next

If you're new to GAQL, start with the wasted spend query. Run it on any account and I guarantee you'll find money being wasted on irrelevant search terms. That immediate win builds confidence.

Then explore the [tools](/tools) that make this workflow seamless. The goal isn't to become a GAQL expert—it's to get insights faster and act on them sooner.
