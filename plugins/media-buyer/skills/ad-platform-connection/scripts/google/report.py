"""Google Ads reporting helpers for the ad-platform-connection skill."""

from __future__ import annotations

import re
from datetime import date
from typing import Any, Dict, Iterable, List, Mapping, Sequence

PREDEFINED_DATE_RANGES = {
    "TODAY",
    "YESTERDAY",
    "LAST_7_DAYS",
    "LAST_14_DAYS",
    "LAST_30_DAYS",
    "LAST_WEEK_MON_SUN",
    "LAST_WEEK_SUN_SAT",
    "THIS_WEEK_MON_TODAY",
    "THIS_WEEK_SUN_TODAY",
    "THIS_MONTH",
    "LAST_MONTH",
    "LAST_90_DAYS",
    "LAST_60_DAYS",
    "LAST_BUSINESS_WEEK",
    "ALL_TIME",
}


def _sanitize_customer_id(customer_id: str | int) -> str:
    digits = "".join(ch for ch in str(customer_id) if ch.isdigit())
    if not digits:
        raise ValueError(f"Invalid customer ID: {customer_id!r}")
    return digits


def _build_date_clause(date_range: Any = "LAST_30_DAYS") -> str:
    if isinstance(date_range, (tuple, list)) and len(date_range) == 2:
        start, end = date_range
        return f"segments.date BETWEEN '{start}' AND '{end}'"

    if isinstance(date_range, date):
        return f"segments.date = '{date_range.isoformat()}'"

    text = str(date_range or "LAST_30_DAYS").strip()
    upper = text.upper()

    if upper in PREDEFINED_DATE_RANGES:
        return f"segments.date DURING {upper}"

    if text.lower().startswith("segments.date"):
        return text

    if upper.startswith("DURING ") or upper.startswith("BETWEEN "):
        return f"segments.date {text}"

    if text.startswith((">", "<", "=")):
        return f"segments.date {text}"

    if re.match(r"^\d{4}-\d{2}-\d{2}$", text):
        return f"segments.date = '{text}'"

    return f"segments.date DURING {upper}"


def _search_stream(service: Any, customer_id: str, query: str) -> Iterable[Any]:
    if hasattr(service, "search_stream"):
        return service.search_stream(customer_id=customer_id, query=query)
    if hasattr(service, "SearchStream"):
        return service.SearchStream(customer_id=customer_id, query=query)
    raise AttributeError("GoogleAdsService does not expose search_stream/SearchStream")


def _flatten_record(value: Any, prefix: str = "", out: Dict[str, Any] | None = None) -> Dict[str, Any]:
    if out is None:
        out = {}

    if value is None:
        if prefix:
            out[prefix] = None
        return out

    if isinstance(value, (str, int, float, bool)):
        if prefix:
            out[prefix] = value
        return out

    if isinstance(value, Mapping):
        for key, nested in value.items():
            key_name = f"{prefix}.{key}" if prefix else str(key)
            _flatten_record(nested, key_name, out)
        return out

    if hasattr(value, "to_dict") and callable(value.to_dict):
        return _flatten_record(value.to_dict(), prefix, out)

    if hasattr(value, "name") and hasattr(value, "value") and not isinstance(value, Mapping):
        if prefix:
            out[prefix] = getattr(value, "name", str(value))
        return out

    if isinstance(value, (list, tuple)):
        if not prefix:
            return out
        if all(item is None or isinstance(item, (str, int, float, bool)) for item in value):
            out[prefix] = "; ".join(str(item) for item in value)
        else:
            for idx, nested in enumerate(value):
                _flatten_record(nested, f"{prefix}.{idx}", out)
        return out

    attrs = [
        name
        for name in dir(value)
        if not name.startswith("_")
        and name not in {"ByteSize", "Clear", "ClearField", "CopyFrom", "ListFields"}
    ]
    used_attr = False
    for attr in attrs:
        try:
            nested_value = getattr(value, attr)
        except Exception:
            continue

        if callable(nested_value):
            continue

        key_name = f"{prefix}.{attr}" if prefix else attr
        _flatten_record(nested_value, key_name, out)
        used_attr = True

    if prefix and not used_attr:
        out[prefix] = str(value)

    return out


def _ensure_query_limit(query: str, limit: int | None) -> str:
    if limit is None:
        return query.strip().rstrip(";")

    normalized = query.strip().rstrip(";")
    if re.search(r"\blimit\b", normalized, flags=re.IGNORECASE):
        return normalized
    return f"{normalized} LIMIT {int(limit)}"


def pull_report(client: Any, customer_id: str | int, query: str, limit: int | None = None):
    """Run a GAQL query and return a pandas DataFrame with flattened columns."""
    import pandas as pd

    resolved_customer_id = _sanitize_customer_id(customer_id)
    ga_service = client.get_service("GoogleAdsService")
    gaql = _ensure_query_limit(query, limit)

    rows: List[Dict[str, Any]] = []
    for batch in _search_stream(ga_service, resolved_customer_id, gaql):
        for result in getattr(batch, "results", []):
            rows.append(_flatten_record(result))

    df = pd.DataFrame(rows)
    if df.empty:
        return df

    for column in list(df.columns):
        if column.endswith("_micros"):
            df[column] = pd.to_numeric(df[column], errors="coerce")
            converted_column = column[: -len("_micros")]
            if converted_column not in df.columns:
                df[converted_column] = df[column] / 1_000_000

    return df


def quick_campaign_summary(client: Any, customer_id: str | int, date_range: Any = "LAST_30_DAYS"):
    date_clause = _build_date_clause(date_range)
    query = f"""
        SELECT
          campaign.id,
          campaign.name,
          campaign.status,
          campaign.advertising_channel_type,
          metrics.impressions,
          metrics.clicks,
          metrics.ctr,
          metrics.cost_micros,
          metrics.conversions,
          metrics.cost_per_conversion,
          metrics.conversions_value
        FROM campaign
        WHERE campaign.status != 'REMOVED' AND {date_clause}
        ORDER BY metrics.cost_micros DESC
    """
    return pull_report(client, customer_id, query)


def quick_adgroup_summary(client: Any, customer_id: str | int, date_range: Any = "LAST_30_DAYS"):
    date_clause = _build_date_clause(date_range)
    query = f"""
        SELECT
          campaign.name,
          ad_group.id,
          ad_group.name,
          ad_group.status,
          metrics.impressions,
          metrics.clicks,
          metrics.ctr,
          metrics.cost_micros,
          metrics.conversions,
          metrics.cost_per_conversion,
          metrics.average_cpc
        FROM ad_group
        WHERE ad_group.status != 'REMOVED' AND {date_clause}
        ORDER BY metrics.cost_micros DESC
    """
    return pull_report(client, customer_id, query)


def quick_keyword_performance(
    client: Any,
    customer_id: str | int,
    date_range: Any = "LAST_30_DAYS",
):
    date_clause = _build_date_clause(date_range)
    query = f"""
        SELECT
          campaign.name,
          ad_group.name,
          ad_group_criterion.criterion_id,
          ad_group_criterion.keyword.text,
          ad_group_criterion.keyword.match_type,
          metrics.impressions,
          metrics.clicks,
          metrics.ctr,
          metrics.cost_micros,
          metrics.conversions,
          metrics.cost_per_conversion,
          metrics.historical_quality_score
        FROM keyword_view
        WHERE ad_group_criterion.status != 'REMOVED' AND {date_clause}
        ORDER BY metrics.cost_micros DESC
    """
    return pull_report(client, customer_id, query)


def quick_search_terms(client: Any, customer_id: str | int, date_range: Any = "LAST_30_DAYS"):
    date_clause = _build_date_clause(date_range)
    query = f"""
        SELECT
          campaign.name,
          ad_group.name,
          search_term_view.search_term,
          metrics.impressions,
          metrics.clicks,
          metrics.ctr,
          metrics.cost_micros,
          metrics.conversions,
          metrics.cost_per_conversion
        FROM search_term_view
        WHERE {date_clause}
        ORDER BY metrics.cost_micros DESC
    """
    return pull_report(client, customer_id, query)


def quick_shopping_summary(client: Any, customer_id: str | int, date_range: Any = "LAST_30_DAYS"):
    date_clause = _build_date_clause(date_range)
    query = f"""
        SELECT
          segments.product_item_id,
          segments.product_title,
          campaign.name,
          ad_group.name,
          metrics.impressions,
          metrics.clicks,
          metrics.ctr,
          metrics.cost_micros,
          metrics.conversions,
          metrics.conversions_value
        FROM shopping_performance_view
        WHERE {date_clause}
        ORDER BY metrics.cost_micros DESC
    """
    return pull_report(client, customer_id, query)


def quick_wasted_spend(client: Any, customer_id: str | int, date_range: Any = "LAST_30_DAYS"):
    """Return a combined report for high-spend/zero-conversion keywords and terms."""
    import pandas as pd

    keyword_query = f"""
        SELECT
          campaign.name,
          ad_group.name,
          ad_group_criterion.keyword.text,
          ad_group_criterion.keyword.match_type,
          metrics.clicks,
          metrics.cost_micros,
          metrics.conversions
        FROM keyword_view
        WHERE {_build_date_clause(date_range)}
          AND metrics.cost_micros > 0
          AND metrics.conversions = 0
        ORDER BY metrics.cost_micros DESC
    """

    term_query = f"""
        SELECT
          campaign.name,
          ad_group.name,
          search_term_view.search_term,
          metrics.clicks,
          metrics.cost_micros,
          metrics.conversions
        FROM search_term_view
        WHERE {_build_date_clause(date_range)}
          AND metrics.cost_micros > 0
          AND metrics.conversions = 0
        ORDER BY metrics.cost_micros DESC
    """

    keyword_df = pull_report(client, customer_id, keyword_query)
    term_df = pull_report(client, customer_id, term_query)

    if keyword_df.empty and term_df.empty:
        return pd.DataFrame()

    if not keyword_df.empty:
        keyword_df["source"] = "keyword"
    if not term_df.empty:
        term_df["source"] = "search_term"

    return pd.concat([keyword_df, term_df], ignore_index=True, sort=False)


__all__ = [
    "pull_report",
    "quick_campaign_summary",
    "quick_adgroup_summary",
    "quick_keyword_performance",
    "quick_search_terms",
    "quick_shopping_summary",
    "quick_wasted_spend",
]
