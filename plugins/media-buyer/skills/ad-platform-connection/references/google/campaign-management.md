# Google Campaign Management

Use `scripts/google/mutate.py` for write operations and `scripts/google/report.py` for read-before-write checks.

## Entity Hierarchy

`Customer -> Campaign (+ Budget) -> Ad Group -> Keywords / Ads / Criteria`

## Read Before Write (GAQL Patterns)

### Campaign snapshot

```sql
SELECT
  campaign.id,
  campaign.name,
  campaign.status,
  campaign.advertising_channel_type,
  metrics.cost_micros,
  metrics.conversions
FROM campaign
WHERE campaign.status != 'REMOVED'
  AND segments.date DURING LAST_30_DAYS
```

### Ad group snapshot

```sql
SELECT
  campaign.name,
  ad_group.id,
  ad_group.name,
  ad_group.status,
  metrics.cost_micros,
  metrics.conversions
FROM ad_group
WHERE ad_group.status != 'REMOVED'
  AND segments.date DURING LAST_30_DAYS
```

## Campaign Create Pattern

Use `create_campaign()` for atomic budget + campaign creation.

```python
from scripts.google.mutate import create_campaign

preview = create_campaign(
    client,
    customer_id="1234567890",
    campaign_spec={
        "name": "Search - US - Core",
        "budget_amount": 100,
        "status": "PAUSED",
        "advertising_channel_type": "SEARCH",
    },
    dry_run=True,
)
```

It creates temporary resources (`campaignBudgets/-1`, `campaigns/-2`) in a single request.

## Pause / Enable Entities

Use `pause_entities()` with full resource names:

```python
pause_entities(client, customer_id, [
    "customers/1234567890/campaigns/111",
    "customers/1234567890/adGroups/222",
])
```

## Negative Keywords

Use `add_negative_keywords()` with `level='campaign'` or `level='ad_group'`.

```python
add_negative_keywords(
    client,
    customer_id="1234567890",
    keywords=["free", "jobs"],
    level="campaign",
    parent_id="111",
    dry_run=True,
)
```

## Responsive Search Ads

Use `create_rsa()`:

```python
create_rsa(
    client,
    customer_id="1234567890",
    ad_group_id="222",
    headlines=["Fast Shipping", "Shop Today", "Top Rated"],
    descriptions=[
        "High-performance products with quick delivery.",
        "Order now and get free returns.",
    ],
    final_urls=["https://example.com"],
    dry_run=True,
)
```

## Bid Updates With Guardrails

`update_bids()` rejects bid deltas above 50% by default.

```python
update_bids(
    client,
    customer_id="1234567890",
    bid_changes=[
        {
            "resource_name": "customers/1234567890/adGroupCriteria/222~333",
            "current_bid_micros": 2000000,
            "new_bid_micros": 2500000,
        }
    ],
    dry_run=True,
)
```

Override threshold with `max_change_ratio` only when needed.

## Resource Segment -> Entity Mapping

`mutate.py` infers entity type from resource segment:

- `campaigns` -> `campaign`
- `adGroups` -> `ad_group`
- `adGroupCriteria` -> `ad_group_criterion`
- `campaignCriteria` -> `campaign_criterion`
- `campaignBudgets` -> `campaign_budget`
- `adGroupAds` -> `ad_group_ad`
- `ads` -> `ad`

## Safety Workflow

1. Pull current state (`report.py` or direct GAQL).
2. Build mutations.
3. Execute with `dry_run=True`.
4. Show preview to user.
5. Re-run with `dry_run=False` only after explicit approval.
