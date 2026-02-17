# Bing Ads Reporting

Report helper at `scripts/bing/report.py`. All functions return pandas DataFrames.

## Quick Helpers

```python
from scripts.bing.report import quick_campaign_summary, quick_shopping_summary

df = quick_campaign_summary(auth_data, account_id)
df = quick_shopping_summary(auth_data, account_id)
```

Both default to `LastSevenDays` and `Summary` aggregation.

## Custom Reports

```python
from scripts.bing.report import pull_report

df = pull_report(
    auth_data=auth_data,
    account_id=account_id,
    report_type='KeywordPerformance',
    time_period='LastFourWeeks',
    columns=['KeywordText', 'MatchType', 'Impressions', 'Clicks', 'Spend', 'Conversions'],
    aggregation='Daily',
)
```

## Report Types

| Friendly Name | API Request Type | Scope |
|---------------|-----------------|-------|
| `CampaignPerformance` | `CampaignPerformanceReportRequest` | `AccountThroughCampaignReportScope` |
| `AdGroupPerformance` | `AdGroupPerformanceReportRequest` | `AccountThroughAdGroupReportScope` |
| `KeywordPerformance` | `KeywordPerformanceReportRequest` | `AccountThroughAdGroupReportScope` |
| `ProductDimensionPerformance` | `ProductDimensionPerformanceReportRequest` | `AccountThroughAdGroupReportScope` |
| `ProductPartitionPerformance` | `ProductPartitionPerformanceReportRequest` | `AccountThroughAdGroupReportScope` |
| `SearchQueryPerformance` | `SearchQueryPerformanceReportRequest` | `AccountThroughAdGroupReportScope` |
| `ProductMatchCount` | `ProductMatchCountReportRequest` | `AccountThroughAdGroupReportScope` |

## Time Periods

### Predefined Periods

| Value | Coverage |
|-------|----------|
| `Today` | Current day |
| `Yesterday` | Previous day |
| `LastSevenDays` | Past 7 days |
| `ThisWeek` | Current week |
| `LastWeek` | Previous week |
| `LastFourWeeks` | Past 28 days |
| `ThisMonth` | Current month |
| `LastMonth` | Previous month |
| `LastThreeMonths` | Past 3 months |
| `LastSixMonths` | Past 6 months |
| `ThisYear` | Current year |
| `LastYear` | Previous year |

### Convenience Aliases

| Alias | Maps To |
|-------|---------|
| `Last7Days` | `LastSevenDays` |
| `Last30Days` | `LastFourWeeks` (28 days, not 30) |

No 14-day predefined period exists. For a custom 14-day window, use `start_date` and `end_date` instead.

### Custom Date Ranges

Pass `start_date` and `end_date` as `YYYY-MM-DD` strings instead of `time_period`:

```python
df = pull_report(
    auth_data, account_id, 'CampaignPerformance',
    start_date='2026-01-01', end_date='2026-01-14',
    columns=['CampaignName', 'Impressions', 'Clicks', 'Spend'],
)
```

## Aggregation Options

| Value | Granularity |
|-------|-------------|
| `Summary` | Single row per entity (no date breakdown) |
| `Daily` | One row per entity per day |
| `Weekly` | One row per entity per week |
| `Monthly` | One row per entity per month |
| `Hourly` | One row per entity per hour |

## Common Columns by Report Type

### CampaignPerformance

`CampaignName`, `CampaignStatus`, `CampaignType`, `Impressions`, `Clicks`, `Ctr`, `Spend`, `Conversions`, `CostPerConversion`, `Revenue`, `ReturnOnAdSpend`

### AdGroupPerformance

`CampaignName`, `AdGroupName`, `AdGroupStatus`, `Impressions`, `Clicks`, `Ctr`, `Spend`, `Conversions`, `CostPerConversion`

### KeywordPerformance

`KeywordText`, `MatchType`, `BidMatchType`, `QualityScore`, `Impressions`, `Clicks`, `Ctr`, `Spend`, `Conversions`, `CostPerConversion`

### SearchQueryPerformance

`SearchQuery`, `CampaignName`, `AdGroupName`, `KeywordText`, `Impressions`, `Clicks`, `Spend`, `Conversions`

### ProductDimensionPerformance

`Title`, `MerchantProductId`, `Brand`, `Condition`, `Impressions`, `Clicks`, `Ctr`, `Spend`, `Conversions`, `Revenue`, `ReturnOnAdSpend`

## Numeric Column Handling

The script auto-cleans these columns by stripping commas and percent signs, then converting to numeric:

`Impressions`, `Clicks`, `Spend`, `Conversions`, `Revenue`, `CostPerConversion`, `AverageCpc`, `ReturnOnAdSpend`

## SUDS Gotchas

- `ReportTimeZone` is required on every request — the script sets `EasternTimeUSCanada` by default.
- When using predefined time periods, `CustomDateRangeStart` and `CustomDateRangeEnd` must be explicitly set to `None` to prevent SUDS from serializing empty Date objects with default empty-string fields.
- For `AccountThroughAdGroupReportScope`, both `Campaigns` and `AdGroups` must be set to `None` after creation. The script's `_configure_report_scope()` helper handles this.
