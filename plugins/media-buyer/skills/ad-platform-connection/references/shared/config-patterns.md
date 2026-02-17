# Config Patterns (Google + Bing)

Both platforms use local JSON config files for OAuth and account routing.

## Google Config

Path: `~/.google_ads_config.json`

```json
{
  "client_id": "...",
  "client_secret": "...",
  "developer_token": "...",
  "refresh_token": "...",
  "login_customer_id": "",
  "default_customer_id": "1234567890"
}
```

Field notes:
- `client_id`, `client_secret`: OAuth credentials from Google Cloud Console.
- `developer_token`: Google Ads API Center token.
- `refresh_token`: OAuth refresh token for the API user.
- `login_customer_id`: optional MCC manager account ID used for child account access.
- `default_customer_id`: optional default target account (10 digits, no dashes).

## Bing Config

Path: `~/.msads_config.json`

```json
{
  "client_id": "...",
  "developer_token": "...",
  "refresh_token": "...",
  "customer_id": "...",
  "account_id": "...",
  "merchant_stores": {
    "product-slug": 1234567
  },
  "environment": "production"
}
```

Field notes:
- `client_id`: Azure app ID for Microsoft Ads OAuth.
- `developer_token`: Microsoft Advertising developer token.
- `refresh_token`: long-lived refresh token (rotates over time).
- `customer_id` / `account_id`: default account context for SDK operations.
- `merchant_stores`: map product slugs to Merchant Center store IDs.

## Token Rotation

Both auth scripts support refresh-token rotation:
- refresh access token
- compare refresh token before/after
- persist config when the token changes

This prevents stale token drift between sessions.

## Account Switching

- Google: `switch_customer(client, customer_id)`
- Bing: `switch_account(auth_data, config, new_account_id)`

Use this when one login accesses multiple child accounts.

## Report Abstraction

Both report helpers return pandas DataFrames with normalized numeric columns.
Common KPI columns: impressions, clicks, CTR, spend, conversions, CPA, ROAS.

## Bulk Threshold Guidance

- `< 50` entity changes: standard mutate/service calls.
- `>= 50` entity changes: use batch APIs.
  - Google: batch mutate operations.
  - Bing: CSV bulk upload/download (`BulkServiceManager`).

## Dependencies

```bash
pip install google-ads bingads pandas
```
