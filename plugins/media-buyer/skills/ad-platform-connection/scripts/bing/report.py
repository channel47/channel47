"""
Microsoft Advertising Reporting Helper
=======================================
Simplifies pulling performance reports from the Microsoft Advertising API.

Usage:
    from scripts.bing.report import pull_report
    df = pull_report(auth_data, account_id, 'CampaignPerformance', 'Last30Days', columns)
"""

import os
import re
from datetime import date

# Valid PredefinedTime enum values for the Bing Ads Reporting API.
# The API rejects values like 'Last7Days' or 'Last30Days' — use these exact strings.
VALID_TIME_PERIODS = {
    'Today', 'Yesterday', 'LastSevenDays', 'ThisWeek', 'LastWeek',
    'LastFourWeeks', 'ThisMonth', 'LastMonth', 'LastThreeMonths',
    'LastSixMonths', 'ThisYear', 'LastYear',
    # Convenience aliases mapped to valid values
}

_TIME_PERIOD_ALIASES = {
    'Last7Days': 'LastSevenDays',
    'Last30Days': 'LastFourWeeks',
    # No exact 14-day predefined period exists in the API.
}

_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def _normalize_time_period(time_period):
    """Normalize common time period aliases to valid API enum values."""
    if time_period in VALID_TIME_PERIODS:
        return time_period
    normalized = _TIME_PERIOD_ALIASES.get(time_period)
    if normalized:
        return normalized
    return time_period


def _configure_report_scope(scope, account_id):
    """Assign account scope and clear optional nested objects that SUDS prepopulates."""
    scope.AccountIds = {'long': [int(account_id)]}
    scope.Campaigns = None
    if hasattr(scope, 'AdGroups'):
        scope.AdGroups = None
    return scope


def _parse_yyyy_mm_dd(value, label):
    if not isinstance(value, str) or not _DATE_RE.match(value):
        raise ValueError(f"{label} must be YYYY-MM-DD format, got: {value!r}")
    try:
        parsed = date.fromisoformat(value)
    except ValueError as exc:
        raise ValueError(f"{label} must be YYYY-MM-DD format, got: {value!r}") from exc
    return parsed.year, parsed.month, parsed.day


def pull_report(auth_data, account_id, report_type, time_period=None,
                start_date=None, end_date=None, columns=None,
                aggregation='Daily', working_dir='./reports',
                environment='production'):
    """
    Pull a performance report from Microsoft Advertising.

    Args:
        auth_data: AuthorizationData from auth.py
        account_id: Account ID to report on
        report_type: One of 'CampaignPerformance', 'AdGroupPerformance',
                     'KeywordPerformance', 'ProductDimensionPerformance',
                     'ProductPartitionPerformance', 'SearchQueryPerformance',
                     'ProductMatchCount'
        time_period: Predefined period. Valid values:
                     'Today', 'Yesterday', 'LastSevenDays', 'ThisWeek', 'LastWeek',
                     'LastFourWeeks', 'ThisMonth', 'LastMonth', 'LastThreeMonths',
                     'LastSixMonths', 'ThisYear', 'LastYear'
                     Also accepts aliases: 'Last7Days' -> 'LastSevenDays',
                     'Last30Days' -> 'LastFourWeeks'
        start_date: Custom start date string 'YYYY-MM-DD' (use instead of time_period)
        end_date: Custom end date string 'YYYY-MM-DD' (use with start_date)
        columns: List of column names for the report
        aggregation: 'Daily', 'Weekly', 'Monthly', 'Hourly', or 'Summary'
        working_dir: Directory to save downloaded report files
        environment: 'production' or 'sandbox'

    Returns:
        pandas DataFrame with report data
    """
    import pandas as pd
    from bingads import ServiceClient
    from bingads.v13.reporting import ReportingServiceManager
    from bingads.v13.reporting.reporting_download_parameters import ReportingDownloadParameters

    env = environment

    # Create reporting service for factory objects
    reporting_service = ServiceClient(
        service='ReportingService',
        version=13,
        authorization_data=auth_data,
        environment=env
    )

    # Map friendly names to request types
    request_type_map = {
        'CampaignPerformance': 'CampaignPerformanceReportRequest',
        'AdGroupPerformance': 'AdGroupPerformanceReportRequest',
        'KeywordPerformance': 'KeywordPerformanceReportRequest',
        'ProductDimensionPerformance': 'ProductDimensionPerformanceReportRequest',
        'ProductPartitionPerformance': 'ProductPartitionPerformanceReportRequest',
        'SearchQueryPerformance': 'SearchQueryPerformanceReportRequest',
        'ProductMatchCount': 'ProductMatchCountReportRequest',
    }

    request_name = request_type_map.get(report_type, report_type)

    # Create the report request
    report_request = reporting_service.factory.create(request_name)
    report_request.Format = 'Csv'
    report_request.Aggregation = aggregation
    report_request.ExcludeColumnHeaders = False
    report_request.ExcludeReportFooter = True
    report_request.ExcludeReportHeader = True
    report_request.ReturnOnlyCompleteData = False

    # Set time period
    report_time = reporting_service.factory.create('ReportTime')
    report_time.ReportTimeZone = 'EasternTimeUSCanada'
    if time_period:
        report_time.PredefinedTime = _normalize_time_period(time_period)
        # Null out custom date fields to prevent SUDS from serializing
        # empty Date objects with Day/Month/Year=None as empty strings,
        # which causes Int32 deserialization errors on the server.
        report_time.CustomDateRangeStart = None
        report_time.CustomDateRangeEnd = None
    elif start_date and end_date:
        custom_start = reporting_service.factory.create('Date')
        start_year, start_month, start_day = _parse_yyyy_mm_dd(
            start_date,
            label='start_date',
        )
        custom_start.Year = start_year
        custom_start.Month = start_month
        custom_start.Day = start_day

        custom_end = reporting_service.factory.create('Date')
        end_year, end_month, end_day = _parse_yyyy_mm_dd(
            end_date,
            label='end_date',
        )
        custom_end.Year = end_year
        custom_end.Month = end_month
        custom_end.Day = end_day

        report_time.CustomDateRangeStart = custom_start
        report_time.CustomDateRangeEnd = custom_end
    else:
        report_time.PredefinedTime = 'LastFourWeeks'
        report_time.CustomDateRangeStart = None
        report_time.CustomDateRangeEnd = None

    report_request.Time = report_time

    # Set scope
    scope_type_map = {
        'CampaignPerformance': 'AccountThroughCampaignReportScope',
        'AdGroupPerformance': 'AccountThroughAdGroupReportScope',
        'KeywordPerformance': 'AccountThroughAdGroupReportScope',
        'ProductDimensionPerformance': 'AccountThroughAdGroupReportScope',
        'ProductPartitionPerformance': 'AccountThroughAdGroupReportScope',
        'SearchQueryPerformance': 'AccountThroughAdGroupReportScope',
        'ProductMatchCount': 'AccountThroughAdGroupReportScope',
    }

    scope_name = scope_type_map.get(report_type, 'AccountThroughCampaignReportScope')
    scope = reporting_service.factory.create(scope_name)
    _configure_report_scope(scope=scope, account_id=account_id)
    report_request.Scope = scope

    # No filter by default
    report_request.Filter = None

    # Set columns
    if columns:
        column_type = f'{request_name.replace("Request", "Column")}'
        array_type = f'ArrayOf{column_type}'
        report_columns = reporting_service.factory.create(array_type)
        getattr(report_columns, column_type).extend(columns)
        report_request.Columns = report_columns

    # Create reporting manager and download
    os.makedirs(working_dir, exist_ok=True)

    reporting_mgr = ReportingServiceManager(
        authorization_data=auth_data,
        working_directory=working_dir,
        poll_interval_in_milliseconds=5000,
        environment=env
    )

    print(f"Requesting {report_type} report...")

    download_params = ReportingDownloadParameters(
        report_request=report_request,
        result_file_name=f'{report_type.lower()}_report.csv',
        overwrite_result_file=True,
        timeout_in_milliseconds=300000
    )

    result = reporting_mgr.download_report(download_params)

    if result is None:
        print("No data returned for the specified criteria.")
        return pd.DataFrame()

    # The SDK returns a _RowReport object. Extract rows via its API.
    rows = []
    cols = result.report_columns
    for record in result.report_records:
        row = {col: record.value(col) for col in cols}
        rows.append(row)

    df = pd.DataFrame(rows, columns=cols)
    print(f"Report contains {len(df)} rows and {len(df.columns)} columns.")

    # Convert numeric columns that may still have formatting issues
    numeric_cols = ['Impressions', 'Clicks', 'Spend', 'Conversions', 'Revenue',
                    'CostPerConversion', 'AverageCpc', 'ReturnOnAdSpend']
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(
                df[col].astype(str).str.replace(',', '').str.replace('%', ''),
                errors='coerce'
            )

    return df


def quick_campaign_summary(auth_data, account_id, time_period='LastSevenDays',
                           environment='production'):
    """Pull a quick campaign performance summary."""
    columns = [
        'CampaignName', 'CampaignStatus', 'CampaignType',
        'Impressions', 'Clicks', 'Ctr', 'Spend',
        'Conversions', 'CostPerConversion', 'Revenue', 'ReturnOnAdSpend'
    ]
    return pull_report(
        auth_data=auth_data,
        account_id=account_id,
        report_type='CampaignPerformance',
        time_period=time_period,
        columns=columns,
        aggregation='Summary',
        environment=environment
    )


def quick_shopping_summary(auth_data, account_id, time_period='LastSevenDays',
                           environment='production'):
    """Pull a quick shopping product performance summary."""
    columns = [
        'Title', 'MerchantProductId', 'Brand', 'Condition',
        'Impressions', 'Clicks', 'Ctr', 'Spend',
        'Conversions', 'Revenue', 'ReturnOnAdSpend'
    ]
    return pull_report(
        auth_data=auth_data,
        account_id=account_id,
        report_type='ProductDimensionPerformance',
        time_period=time_period,
        columns=columns,
        aggregation='Summary',
        environment=environment
    )
