"""Google Ads mutation helpers for the ad-platform-connection skill."""

from __future__ import annotations

import logging
from typing import Any, Dict, Iterable, List, Mapping, Sequence

LOGGER = logging.getLogger(__name__)

ENTITY_SEGMENT_MAP = {
    "campaigns": "campaign",
    "adgroups": "ad_group",
    "adgroupcriteria": "ad_group_criterion",
    "campaigncriteria": "campaign_criterion",
    "campaignbudgets": "campaign_budget",
    "biddingstrategies": "bidding_strategy",
    "ads": "ad",
    "adgroupads": "ad_group_ad",
    "assets": "asset",
    "labels": "label",
    "sharedsets": "shared_set",
    "sharedcriteria": "shared_criterion",
    "conversionactions": "conversion_action",
    "customernegativecriteria": "customer_negative_criterion",
    "userlists": "user_list",
}


def _sanitize_numeric_id(identifier: str | int, label: str = "ID") -> str:
    if "/" in str(identifier):
        raise ValueError(f"{label} must be numeric, not a resource name: {identifier!r}")
    digits = "".join(ch for ch in str(identifier) if ch.isdigit())
    if not digits:
        raise ValueError(f"Invalid {label}: {identifier!r}")
    return digits


def _sanitize_customer_id(customer_id: str | int) -> str:
    return _sanitize_numeric_id(customer_id, label="customer ID")


def _normalize_segment(segment: str) -> str:
    return "".join(ch.lower() for ch in segment if ch.isalnum())


def infer_entity_type(resource_name: str) -> str:
    parts = resource_name.split("/")
    if len(parts) < 3:
        raise ValueError(f"Invalid resource name: {resource_name!r}")

    segment = _normalize_segment(parts[2])
    entity_type = ENTITY_SEGMENT_MAP.get(segment)
    if not entity_type:
        raise ValueError(f"Unsupported resource segment {parts[2]!r} in {resource_name!r}")
    return entity_type


def _operation_field(entity_type: str) -> str:
    return f"{entity_type}_operation"


def _assign_message_fields(message: Any, values: Mapping[str, Any]) -> None:
    for key, value in values.items():
        if value is None:
            continue

        target = getattr(message, key)

        if isinstance(value, Mapping):
            _assign_message_fields(target, value)
            continue

        if isinstance(value, list):
            if hasattr(target, "add") and value and isinstance(value[0], Mapping):
                for item in value:
                    child = target.add()
                    _assign_message_fields(child, item)
                continue

            if hasattr(target, "extend"):
                target.extend(value)
                continue

            if hasattr(target, "add"):
                for item in value:
                    child = target.add()
                    if isinstance(item, Mapping):
                        _assign_message_fields(child, item)
                    else:
                        # Asset and similar messages often expose a `text` field.
                        if hasattr(child, "text"):
                            child.text = item
                        elif hasattr(child, "value"):
                            child.value = item
                        else:
                            raise ValueError(
                                f"Cannot assign list scalar to {key}; unsupported message type"
                            )
                continue

        setattr(message, key, value)


def _set_update_mask(mask: Any, field_paths: Iterable[str]) -> None:
    paths = [path for path in field_paths if path and path != "resource_name"]
    if hasattr(mask, "paths"):
        del mask.paths[:]
        mask.paths.extend(paths)


def _build_mutate_operation(client: Any, operation: Any) -> Any:
    if not isinstance(operation, Mapping):
        return operation

    entity = operation.get("entity")
    action = str(operation.get("action", "")).lower()

    if not entity:
        raise ValueError("Dictionary operations must define an 'entity' field")
    if action not in {"create", "update", "remove"}:
        raise ValueError("Dictionary operations must use action=create|update|remove")

    mutate_operation = client.get_type("MutateOperation")
    op_container = getattr(mutate_operation, _operation_field(str(entity)))

    payload = dict(operation.get("data") or {})
    resource_name = operation.get("resource_name")

    if action == "create":
        _assign_message_fields(op_container.create, payload)
        return mutate_operation

    if action == "remove":
        if not resource_name:
            raise ValueError("Remove operations require resource_name")
        op_container.remove = resource_name
        return mutate_operation

    # action == update
    if resource_name and "resource_name" not in payload:
        payload["resource_name"] = resource_name
    _assign_message_fields(op_container.update, payload)

    update_mask = operation.get("field_mask") or sorted(payload.keys())
    _set_update_mask(op_container.update_mask, update_mask)

    return mutate_operation


def _extract_mutation_result(response: Any) -> Dict[str, Any]:
    mutate_responses = list(getattr(response, "mutate_operation_responses", []) or [])
    results = []
    for item in mutate_responses:
        resource_name = None
        descriptor = getattr(item, "DESCRIPTOR", None)
        descriptor_fields = getattr(descriptor, "fields", None) if descriptor else None
        if descriptor_fields:
            for field in descriptor_fields:
                if not str(getattr(field, "name", "")).endswith("_result"):
                    continue
                nested = getattr(item, field.name, None)
                if nested is None:
                    continue
                resource_name = getattr(nested, "resource_name", None)
                if resource_name:
                    break
        else:
            LOGGER.warning(
                "Mutation response item lacks DESCRIPTOR metadata; "
                "falling back to direct resource_name lookup for %s",
                type(item).__name__,
            )
        if resource_name is None:
            resource_name = getattr(item, "resource_name", None)
        results.append({"resource_name": resource_name})

    errors: List[str] = []
    partial_failure_error = getattr(response, "partial_failure_error", None)
    if partial_failure_error:
        details = getattr(partial_failure_error, "details", None)
        if details:
            errors.extend(str(detail) for detail in details)
        else:
            errors.append(str(partial_failure_error))

    return {
        "success": not errors,
        "results": results,
        "errors": errors,
    }


def execute_mutation(
    client: Any,
    customer_id: str | int,
    operations: Sequence[Any],
    dry_run: bool = True,
    partial_failure: bool = True,
) -> Dict[str, Any]:
    """Execute one or more mutate operations, validate-only by default."""
    resolved_customer_id = _sanitize_customer_id(customer_id)
    ga_service = client.get_service("GoogleAdsService")
    mutate_operations = [_build_mutate_operation(client, operation) for operation in operations]

    if hasattr(ga_service, "mutate"):
        response = ga_service.mutate(
            customer_id=resolved_customer_id,
            mutate_operations=mutate_operations,
            partial_failure=partial_failure,
            validate_only=dry_run,
        )
    elif hasattr(ga_service, "Mutate"):
        try:
            response = ga_service.Mutate(
                customer_id=resolved_customer_id,
                mutate_operations=mutate_operations,
                partial_failure=partial_failure,
                validate_only=dry_run,
            )
        except TypeError:
            response = ga_service.Mutate(
                request={
                    "customer_id": resolved_customer_id,
                    "mutate_operations": mutate_operations,
                    "partial_failure": partial_failure,
                    "validate_only": dry_run,
                }
            )
    else:
        raise AttributeError("GoogleAdsService does not expose mutate/Mutate")

    return _extract_mutation_result(response)


def create_campaign(
    client: Any,
    customer_id: str | int,
    campaign_spec: Mapping[str, Any],
    dry_run: bool = True,
) -> Dict[str, Any]:
    """Create campaign budget + campaign atomically using temporary resource names."""
    resolved_customer_id = _sanitize_customer_id(customer_id)

    campaign_name = campaign_spec.get("name") or "New Campaign"
    budget_name = campaign_spec.get("budget_name") or f"{campaign_name} Budget"

    budget_amount_micros = campaign_spec.get("budget_amount_micros")
    if budget_amount_micros is None:
        budget_amount = float(campaign_spec.get("budget_amount", 0))
        budget_amount_micros = int(budget_amount * 1_000_000)

    budget_resource = f"customers/{resolved_customer_id}/campaignBudgets/-1"
    campaign_resource = f"customers/{resolved_customer_id}/campaigns/-2"

    operations = [
        {
            "entity": "campaign_budget",
            "action": "create",
            "data": {
                "resource_name": budget_resource,
                "name": budget_name,
                "delivery_method": str(campaign_spec.get("budget_delivery_method", "STANDARD")).upper(),
                "amount_micros": int(budget_amount_micros),
                "explicitly_shared": bool(campaign_spec.get("explicitly_shared", False)),
            },
        },
        {
            "entity": "campaign",
            "action": "create",
            "data": {
                "resource_name": campaign_resource,
                "name": campaign_name,
                "status": str(campaign_spec.get("status", "PAUSED")).upper(),
                "advertising_channel_type": str(
                    campaign_spec.get("advertising_channel_type", "SEARCH")
                ).upper(),
                "campaign_budget": budget_resource,
                "contains_eu_political_advertising": str(
                    campaign_spec.get("contains_eu_political_advertising", "DOES_NOT_CONTAIN_EU_POLITICAL_ADVERTISING")
                ).upper(),
            },
        },
    ]

    if campaign_spec.get("start_date"):
        operations[1]["data"]["start_date"] = campaign_spec["start_date"]
    if campaign_spec.get("end_date"):
        operations[1]["data"]["end_date"] = campaign_spec["end_date"]

    return execute_mutation(
        client=client,
        customer_id=resolved_customer_id,
        operations=operations,
        dry_run=dry_run,
        partial_failure=True,
    )


def pause_entities(
    client: Any,
    customer_id: str | int,
    resource_names: Sequence[str],
    dry_run: bool = True,
) -> Dict[str, Any]:
    """Pause supported entities by resource name."""
    operations = []
    for resource_name in resource_names:
        operations.append(
            {
                "entity": infer_entity_type(resource_name),
                "action": "update",
                "resource_name": resource_name,
                "data": {"status": "PAUSED"},
                "field_mask": ["status"],
            }
        )

    return execute_mutation(
        client=client,
        customer_id=customer_id,
        operations=operations,
        dry_run=dry_run,
        partial_failure=True,
    )


def add_negative_keywords(
    client: Any,
    customer_id: str | int,
    keywords: Sequence[str | Mapping[str, Any]],
    level: str,
    parent_id: str | int,
    dry_run: bool = True,
) -> Dict[str, Any]:
    """Add negative keywords at campaign or ad group level."""
    resolved_customer_id = _sanitize_customer_id(customer_id)
    resolved_parent_id = _sanitize_numeric_id(parent_id, label="parent ID")
    level_normalized = level.strip().lower()

    if level_normalized not in {"campaign", "ad_group"}:
        raise ValueError("level must be 'campaign' or 'ad_group'")

    entity = "campaign_criterion" if level_normalized == "campaign" else "ad_group_criterion"
    parent_resource_name = (
        f"customers/{resolved_customer_id}/campaigns/{resolved_parent_id}"
        if level_normalized == "campaign"
        else f"customers/{resolved_customer_id}/adGroups/{resolved_parent_id}"
    )

    operations = []
    for keyword in keywords:
        if isinstance(keyword, Mapping):
            text = str(keyword["text"])
            match_type = str(keyword.get("match_type", "PHRASE")).upper()
        else:
            text = str(keyword)
            match_type = "PHRASE"

        data = {
            level_normalized if level_normalized == "campaign" else "ad_group": parent_resource_name,
            "negative": True,
            "keyword": {
                "text": text,
                "match_type": match_type,
            },
        }
        operations.append({"entity": entity, "action": "create", "data": data})

    return execute_mutation(
        client=client,
        customer_id=resolved_customer_id,
        operations=operations,
        dry_run=dry_run,
        partial_failure=True,
    )


def create_rsa(
    client: Any,
    customer_id: str | int,
    ad_group_id: str | int,
    headlines: Sequence[str],
    descriptions: Sequence[str],
    final_urls: Sequence[str],
    dry_run: bool = True,
) -> Dict[str, Any]:
    """Create a Responsive Search Ad and keep it paused by default."""
    resolved_customer_id = _sanitize_customer_id(customer_id)
    resolved_ad_group_id = _sanitize_numeric_id(ad_group_id, label="ad group ID")

    ad_group_resource = f"customers/{resolved_customer_id}/adGroups/{resolved_ad_group_id}"
    operations = [
        {
            "entity": "ad_group_ad",
            "action": "create",
            "data": {
                "status": "PAUSED",
                "ad_group": ad_group_resource,
                "ad": {
                    "final_urls": list(final_urls),
                    "responsive_search_ad": {
                        "headlines": [{"text": text} for text in headlines],
                        "descriptions": [{"text": text} for text in descriptions],
                    },
                },
            },
        }
    ]

    return execute_mutation(
        client=client,
        customer_id=resolved_customer_id,
        operations=operations,
        dry_run=dry_run,
        partial_failure=True,
    )


def update_bids(
    client: Any,
    customer_id: str | int,
    bid_changes: Sequence[Mapping[str, Any]],
    dry_run: bool = True,
    max_change_ratio: float = 0.5,
) -> Dict[str, Any]:
    """Update CPC bids with guardrails (default max +/-50% per change)."""
    operations = []
    for change in bid_changes:
        resource_name = str(change["resource_name"])
        current_bid_micros = int(change["current_bid_micros"])
        new_bid_micros = int(change["new_bid_micros"])

        if current_bid_micros > 0:
            ratio = abs(new_bid_micros - current_bid_micros) / current_bid_micros
            if ratio > max_change_ratio:
                raise ValueError(
                    f"Bid change for {resource_name} exceeds {max_change_ratio:.0%} safety threshold"
                )

        entity = infer_entity_type(resource_name)
        if entity not in {"ad_group", "ad_group_criterion"}:
            raise ValueError(f"Unsupported entity for bid updates: {entity}")

        operations.append(
            {
                "entity": entity,
                "action": "update",
                "resource_name": resource_name,
                "data": {"cpc_bid_micros": new_bid_micros},
                "field_mask": ["cpc_bid_micros"],
            }
        )

    return execute_mutation(
        client=client,
        customer_id=customer_id,
        operations=operations,
        dry_run=dry_run,
        partial_failure=True,
    )


__all__ = [
    "execute_mutation",
    "create_campaign",
    "pause_entities",
    "add_negative_keywords",
    "create_rsa",
    "update_bids",
    "infer_entity_type",
]
