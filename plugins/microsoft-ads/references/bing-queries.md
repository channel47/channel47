# Bing Queries — Microsoft Ads Plugin

All report and query configurations for microsoft-ads skills. Use `mcp__bing-ads__report` for reports and `mcp__bing-ads__query` for structure queries.

## Morning Brief (MB-)

### MB-1: Campaign performance report (30 days)

```json
{
  "report_type": "CampaignPerformance",
  "date_range": "LastThirtyDays",
  "aggregation": "Daily",
  "columns": ["CampaignName", "CampaignId", "CampaignStatus", "Impressions", "Clicks", "Spend", "Conversions", "Revenue", "Ctr", "AverageCpc", "CostPerConversion"]
}
```

### MB-2: Keyword performance report (Yesterday)

```json
{
  "report_type": "KeywordPerformance",
  "date_range": "Yesterday",
  "aggregation": "Daily",
  "columns": ["CampaignName", "AdGroupName", "Keyword", "KeywordId", "MatchType", "BidMatchType", "Impressions", "Clicks", "Spend", "Conversions", "Ctr", "AverageCpc", "QualityScore"]
}
```

### MB-3: Campaign structure query

```json
{
  "entity": "campaigns",
  "fields": ["name", "id", "status", "daily_budget", "bid_strategy_type", "campaign_type", "network_distribution"]
}
```

### MB-4: Search query report (Yesterday)

```json
{
  "report_type": "SearchQuery",
  "date_range": "Yesterday",
  "aggregation": "Daily",
  "columns": ["CampaignName", "AdGroupName", "SearchQuery", "Impressions", "Clicks", "Spend", "Conversions", "Ctr", "DeviceType"]
}
```

## Waste Detector (WD-)

### WD-1: Campaign structure — MSAN check

```json
{
  "entity": "campaigns",
  "fields": ["name", "id", "status", "daily_budget", "campaign_type", "network_distribution"]
}
```

Use `network_distribution` to check for "AudienceAds" or "OwnedAndOperatedAndSyndicatedSearch" settings.

### WD-2: Campaign structure — Search partners check

Same as WD-1. Check `network_distribution` for syndicated search partner settings.

### WD-3: Keyword report (30d) — Broad match audit

```json
{
  "report_type": "KeywordPerformance",
  "date_range": "LastThirtyDays",
  "aggregation": "Summary",
  "columns": ["CampaignName", "CampaignId", "AdGroupName", "Keyword", "MatchType", "BidMatchType", "Impressions", "Clicks", "Spend", "Conversions"]
}
```

Filter results: `MatchType == "Broad"`. Cross-reference with negative keyword presence.

### WD-4: Campaign structure — Auto-import check

Same as WD-1. Compare settings against profile's Import Config section for drift.

### WD-5: Campaign performance — Overnight burn

```json
{
  "report_type": "CampaignPerformance",
  "date_range": "LastSevenDays",
  "aggregation": "Hourly",
  "columns": ["CampaignName", "CampaignId", "TimePeriod", "Impressions", "Clicks", "Spend", "Conversions"]
}
```

Note: Hourly aggregation may not be available for all report types. Fall back to Daily and flag campaigns without ad scheduling as at-risk for overnight burn.

### WD-6: Campaign + keyword performance — Bot traffic signals

```json
{
  "report_type": "CampaignPerformance",
  "date_range": "Yesterday",
  "aggregation": "Daily",
  "columns": ["CampaignName", "CampaignId", "Impressions", "Clicks", "Spend", "Conversions", "Ctr", "DeviceType"]
}
```

Flag: CTR > 15% with zero conversions, clicks > 50 with zero conversions, single device >80% of clicks.

### WD-7: Campaign structure — Location targeting check

```json
{
  "entity": "campaigns",
  "fields": ["name", "id", "status", "location_target_type"]
}
```

Check for "PeopleInOrSearchingForOrViewingPages" vs "PeopleIn".

## Search Term Verdict (STV-)

### STV-A: Search query report (30d)

```json
{
  "report_type": "SearchQuery",
  "date_range": "LastThirtyDays",
  "aggregation": "Summary",
  "columns": ["CampaignName", "CampaignId", "AdGroupName", "AdGroupId", "SearchQuery", "Impressions", "Clicks", "Spend", "Conversions", "Revenue", "Ctr", "AverageCpc"]
}
```

### STV-B: Keyword report — existing coverage

```json
{
  "report_type": "KeywordPerformance",
  "date_range": "LastThirtyDays",
  "aggregation": "Summary",
  "columns": ["CampaignName", "AdGroupName", "Keyword", "MatchType", "BidMatchType", "Impressions", "Clicks", "Spend", "Conversions"]
}
```

## Account Scorecard (AS-)

### AS-1: Campaign structure

Same as WD-1.

### AS-2: Keyword performance (30d)

Same as WD-3.

### AS-3: Ad group ad count

```json
{
  "entity": "ads",
  "fields": ["campaign_name", "ad_group_name", "ad_group_id", "status"]
}
```

Count ENABLED ads per ad group.

### AS-4: Campaign performance (30d)

Same as MB-1.

### AS-5: Ad extensions query

```json
{
  "entity": "ad_extensions",
  "fields": ["campaign_name", "extension_type", "status"]
}
```

## Import Auditor (IA-)

### IA-1: Campaign structure — full settings

Same as WD-1 plus additional fields:

```json
{
  "entity": "campaigns",
  "fields": ["name", "id", "status", "daily_budget", "bid_strategy_type", "campaign_type", "network_distribution", "location_target_type", "ad_schedule"]
}
```

### IA-2: Keyword report (30d) — match types and negatives

Same as WD-3.

### IA-3: Campaign performance (7d) — conversion verification

```json
{
  "report_type": "CampaignPerformance",
  "date_range": "LastSevenDays",
  "aggregation": "Summary",
  "columns": ["CampaignName", "CampaignId", "Impressions", "Clicks", "Spend", "Conversions", "Revenue"]
}
```

### IA-4: Ad extensions query

Same as AS-5.

## Placement Cleaner (PC-)

### PC-1: Publisher URL report (30d)

```json
{
  "report_type": "PublisherUsagePerformance",
  "date_range": "LastThirtyDays",
  "aggregation": "Summary",
  "columns": ["PublisherUrl", "CampaignName", "CampaignId", "AdGroupName", "Impressions", "Clicks", "Spend", "Conversions", "Ctr"]
}
```

### PC-2: Campaign performance — MSAN vs Search

```json
{
  "report_type": "CampaignPerformance",
  "date_range": "LastThirtyDays",
  "aggregation": "Summary",
  "columns": ["CampaignName", "CampaignId", "Network", "Impressions", "Clicks", "Spend", "Conversions", "Ctr"]
}
```
