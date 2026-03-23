# Google Campaign Management (Waste Detector)

Use `mcp__google-ads__mutate` for mutation previews and approvals.

## Safety workflow

1. Pull state using `mcp__google-ads__query`.
2. Build candidate operations for pauses/negatives.
3. Run mutation preview with `dry_run: true`.
4. Show preview and request approval.
5. Execute with `dry_run: false` only after explicit consent.

## Common operation targets

- Pause entities with persistent waste (keywords, ad groups, campaigns)
- Add campaign-level or ad-group-level negative keywords
- Leave unsupported changes (network settings, strategy moves) as manual UI actions

## Read-before-write checks

Before a pause or negative action, confirm:

- Entity status is currently enabled
- Entity has recent spend
- Recommendation meets threshold logic from `thresholds.md`

## Mutation payload hygiene

- Keep operation batches small when risk is high.
- Prefer reversible changes (pause before delete).
- Include entity IDs and human-readable names in previews for approval clarity.
