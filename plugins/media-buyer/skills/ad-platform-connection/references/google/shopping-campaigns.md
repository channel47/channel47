# Google Shopping Campaigns

This reference covers Shopping-specific setup patterns using the Google scripts.

## Campaign Setup Basics

A Shopping implementation usually includes:

1. Campaign with Shopping channel settings.
2. Ad group(s) for product groups.
3. Product partition tree criteria.
4. Shopping performance reporting.

Use `create_campaign()` for initial budget + campaign creation, then add Shopping-specific criteria with `execute_mutation()`.

## Minimum Campaign Spec

```python
campaign_spec = {
    "name": "Shopping - US",
    "budget_amount": 150,
    "status": "PAUSED",
    "advertising_channel_type": "SHOPPING",
}
```

Run as dry-run first:

```python
preview = create_campaign(client, customer_id, campaign_spec, dry_run=True)
```

## Product Partition Trees

Partition trees are managed through criterion mutations:
- root subdivision node (`All products`)
- biddable unit nodes (brand/category/product filters)
- optional excluded branch (everything else)

When building trees:
- keep one root per ad group
- create root and children in one mutation batch when possible
- verify resource names and parent relationships before live run

## Performance Max Note

Performance Max and standard Shopping differ in campaign/ad group semantics.
For PMax, treat asset-group setup as a distinct flow and verify required asset fields before mutation.

## Shopping Reporting Patterns

Use `quick_shopping_summary()` for standard product-level KPIs.

```python
df = quick_shopping_summary(client, customer_id, date_range="LAST_30_DAYS")
```

Useful fields:
- `segments.product_item_id`
- `segments.product_title`
- `metrics.impressions`
- `metrics.clicks`
- `metrics.cost`
- `metrics.conversions`
- `metrics.conversions_value`

## Feed Health Checks

Combine reporting and account checks:
- identify products with spend and no conversions
- identify top-spend products by category/brand
- compare product coverage against Merchant Center inventory

## Safety Checklist

- Validate campaign structure with `dry_run=True` first.
- Apply small partition batches before full tree rollout.
- Keep campaigns paused until review is complete.
- Prefer pause over delete for reversibility.
