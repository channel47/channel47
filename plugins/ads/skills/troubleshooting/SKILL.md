---
name: troubleshooting
description: Plugin-specific Google Ads errors. Use when hitting auth, format, or hook issues.
---

# Google Ads Plugin Troubleshooting

## Customer ID Format
- Must be 10 digits without dashes: `1234567890`
- Wrong: `123-456-7890`
- Set default: `GOOGLE_ADS_DEFAULT_CUSTOMER_ID` env var

## Authentication Errors
- "AUTHENTICATION_ERROR": Refresh token expired - re-run `/ads:setup`
- "PERMISSION_DENIED": Account not accessible under current MCC
- "DEVELOPER_TOKEN_NOT_APPROVED": Token still pending Google approval

## Dry Run Validation
- `dry_run: true` (default) validates but doesn't execute
- Set `dry_run: false` explicitly for live mutations
- Hook will warn on live mutations

## Common Mutation Failures
- "MUTATE_ERROR": Check operation structure matches resource type
- "RESOURCE_NOT_FOUND": Verify resource name format: `customers/{id}/campaigns/{id}`
- "INVALID_OPERATION": Can't update immutable fields

## Rate Limits
- Basic access: 15,000 operations/day
- If hitting limits: batch operations, reduce query frequency

For GAQL syntax errors, see: [Google GAQL Reference](https://developers.google.com/google-ads/api/docs/query/overview)
