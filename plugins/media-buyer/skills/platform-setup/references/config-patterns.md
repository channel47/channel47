# Config Patterns (Environment Variable First)

Use environment variables for all ad-platform credentials. Avoid JSON files for runtime auth.

## Google Ads mapping

| Legacy JSON field | Environment variable |
|---|---|
| `developer_token` | `GOOGLE_ADS_DEVELOPER_TOKEN` |
| `client_id` | `GOOGLE_ADS_CLIENT_ID` |
| `client_secret` | `GOOGLE_ADS_CLIENT_SECRET` |
| `refresh_token` | `GOOGLE_ADS_REFRESH_TOKEN` |
| `default_mcc` / `login_customer_id` | `GOOGLE_ADS_LOGIN_CUSTOMER_ID` |

## Bing Ads mapping

| Legacy JSON field | Environment variable |
|---|---|
| `developer_token` | `BING_ADS_DEVELOPER_TOKEN` |
| `client_id` | `BING_ADS_CLIENT_ID` |
| `client_secret` | `BING_ADS_CLIENT_SECRET` |
| `refresh_token` | `BING_ADS_REFRESH_TOKEN` |
| `customer_id` | `BING_ADS_CUSTOMER_ID` |
| `account_id` | `BING_ADS_ACCOUNT_ID` |

## Pattern rules

- Keep secrets in shell environment, not checked-in files.
- Use one canonical variable name per credential.
- Validate by executing a read-only account-listing operation before any report or mutation task.
