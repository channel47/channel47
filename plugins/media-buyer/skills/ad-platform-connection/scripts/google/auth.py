"""Google Ads authentication helpers for the ad-platform-connection skill."""

from __future__ import annotations

import json
import os
import stat
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple

DEFAULT_CONFIG_PATH = Path("~/.google_ads_config.json").expanduser()
REQUIRED_CONFIG_FIELDS = (
    "client_id",
    "client_secret",
    "developer_token",
    "refresh_token",
)


def _sanitize_customer_id(customer_id: Any) -> str | None:
    if customer_id is None:
        return None
    digits = "".join(ch for ch in str(customer_id) if ch.isdigit())
    if not digits:
        raise ValueError(f"Invalid customer ID: {customer_id!r}")
    return digits


def _load_config(config_path: Path) -> Dict[str, Any]:
    if not config_path.exists():
        raise FileNotFoundError(
            f"Google Ads config not found at {config_path}. "
            "Create ~/.google_ads_config.json before connecting."
        )

    with config_path.open("r", encoding="utf-8") as handle:
        config = json.load(handle)

    missing = [key for key in REQUIRED_CONFIG_FIELDS if not config.get(key)]
    if missing:
        raise ValueError(
            "Missing required Google Ads config field(s): " + ", ".join(missing)
        )

    if config.get("login_customer_id"):
        config["login_customer_id"] = _sanitize_customer_id(config["login_customer_id"])
    if config.get("default_customer_id"):
        config["default_customer_id"] = _sanitize_customer_id(
            config["default_customer_id"]
        )

    return config


def _save_config(config_path: Path, config: Dict[str, Any]) -> None:
    with config_path.open("w", encoding="utf-8") as handle:
        json.dump(config, handle, indent=2, sort_keys=True)
        handle.write("\n")
    config_path.chmod(stat.S_IRUSR | stat.S_IWUSR)


def _build_client_payload(config: Dict[str, Any]) -> Dict[str, Any]:
    payload = {
        "developer_token": config["developer_token"],
        "client_id": config["client_id"],
        "client_secret": config["client_secret"],
        "refresh_token": config["refresh_token"],
        "use_proto_plus": True,
    }

    if config.get("login_customer_id"):
        payload["login_customer_id"] = config["login_customer_id"]

    return payload


def _extract_client_config(client: Any) -> Dict[str, Any]:
    source = getattr(client, "configuration", None)
    if source is None:
        source = getattr(client, "_configuration", None)

    if source is None:
        return {}

    keys = (
        "developer_token",
        "client_id",
        "client_secret",
        "refresh_token",
        "login_customer_id",
        "linked_customer_id",
        "use_proto_plus",
    )
    result: Dict[str, Any] = {}
    for key in keys:
        if isinstance(source, dict):
            value = source.get(key)
        else:
            value = getattr(source, key, None)
        if value not in (None, ""):
            result[key] = value
    return result


def _maybe_rotate_refresh_token(
    client: Any,
    config: Dict[str, Any],
    config_path: Path,
) -> None:
    credentials = getattr(client, "_credentials", None)
    if credentials is None:
        return
    if not hasattr(credentials, "refresh") or not hasattr(credentials, "refresh_token"):
        return

    before = config.get("refresh_token")
    try:
        import google.auth.transport.requests as google_auth_requests

        request = google_auth_requests.Request()
        credentials.refresh(request)
    except ImportError:
        return
    except Exception:
        # Refresh failures should not block callers from using existing credentials.
        return

    after = getattr(credentials, "refresh_token", None)

    if after and after != before:
        config["refresh_token"] = after
        _save_config(config_path, config)


def _search_stream(service: Any, customer_id: str, query: str) -> Iterable[Any]:
    if hasattr(service, "search_stream"):
        return service.search_stream(customer_id=customer_id, query=query)
    if hasattr(service, "SearchStream"):
        return service.SearchStream(customer_id=customer_id, query=query)
    raise AttributeError("GoogleAdsService does not expose search_stream/SearchStream")


def _enum_to_name(value: Any) -> str:
    if hasattr(value, "name"):
        return str(value.name)
    return str(value)


def _resolve_seed_customer_id(client: Any) -> str:
    explicit = getattr(client, "_default_customer_id", None)
    if explicit:
        return _sanitize_customer_id(explicit) or ""

    config = _extract_client_config(client)
    for key in ("login_customer_id", "default_customer_id"):
        if config.get(key):
            return _sanitize_customer_id(config[key]) or ""

    raise ValueError(
        "No customer ID found. Provide customer_id explicitly or set "
        "default_customer_id/login_customer_id in config."
    )


def get_auth(config_path: str | os.PathLike[str] | None = None) -> Tuple[Any, Dict[str, Any]]:
    """Load config and return an initialized GoogleAdsClient with config dict."""
    from google.ads.googleads.client import GoogleAdsClient

    resolved_path = Path(config_path).expanduser() if config_path else DEFAULT_CONFIG_PATH
    config = _load_config(resolved_path)

    client = GoogleAdsClient.load_from_dict(
        _build_client_payload(config),
        version=config.get("api_version"),
    )

    default_customer_id = config.get("default_customer_id") or config.get("login_customer_id")
    if default_customer_id:
        setattr(client, "_default_customer_id", default_customer_id)

    _maybe_rotate_refresh_token(client, config, resolved_path)
    return client, config


def switch_customer(client: Any, customer_id: str | int) -> Any:
    """Create a new client instance and set a different default customer context."""
    from google.ads.googleads.client import GoogleAdsClient

    sanitized_customer_id = _sanitize_customer_id(customer_id)
    if not sanitized_customer_id:
        raise ValueError("A valid customer ID is required")

    base_config = _extract_client_config(client)
    if not base_config:
        raise ValueError(
            "Unable to extract Google Ads client configuration. Use get_auth() first."
        )

    switched = GoogleAdsClient.load_from_dict(
        base_config,
        version=getattr(client, "api_version", None),
    )
    setattr(switched, "_default_customer_id", sanitized_customer_id)
    return switched


def list_accounts(client: Any, include_managers: bool = False) -> List[Dict[str, Any]]:
    """List accessible accounts from the current login/default customer context."""
    customer_id = _resolve_seed_customer_id(client)
    ga_service = client.get_service("GoogleAdsService")

    query = """
        SELECT
          customer_client.id,
          customer_client.descriptive_name,
          customer_client.manager,
          customer_client.currency_code,
          customer_client.time_zone,
          customer_client.status
        FROM customer_client
        WHERE customer_client.level <= 1
    """

    accounts: List[Dict[str, Any]] = []
    stream = _search_stream(ga_service, customer_id=customer_id, query=query)
    for batch in stream:
        for row in getattr(batch, "results", []):
            customer_client = getattr(row, "customer_client", None)
            if customer_client is None:
                continue

            entry = {
                "id": str(getattr(customer_client, "id", "")),
                "name": getattr(customer_client, "descriptive_name", ""),
                "is_manager": bool(getattr(customer_client, "manager", False)),
                "currency": getattr(customer_client, "currency_code", None),
                "timezone": getattr(customer_client, "time_zone", None),
                "status": _enum_to_name(getattr(customer_client, "status", "")),
            }

            if entry["is_manager"] and not include_managers:
                continue
            accounts.append(entry)

    return accounts


def verify_connection(client: Any, customer_id: str | int | None = None) -> List[Dict[str, Any]]:
    """Verify API connectivity by listing accessible accounts."""
    accounts = list_accounts(client, include_managers=True)
    if customer_id is None:
        return accounts

    target_id = _sanitize_customer_id(customer_id)
    return [account for account in accounts if account.get("id") == target_id]


__all__ = [
    "get_auth",
    "switch_customer",
    "verify_connection",
    "list_accounts",
]
