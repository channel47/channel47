# Bing Setup

Use this guide to prepare Microsoft Advertising credentials for future MCP execution support.

## Current status

Bing setup guidance is available, but Bing MCP execution is a placeholder until the Bing MCP server is added.

## Recommended environment variables

```bash
export BING_ADS_DEVELOPER_TOKEN="your_developer_token"
export BING_ADS_CLIENT_ID="your_azure_app_client_id"
export BING_ADS_CLIENT_SECRET="your_azure_app_client_secret"
export BING_ADS_REFRESH_TOKEN="your_refresh_token"
export BING_ADS_CUSTOMER_ID="your_manager_customer_id"
export BING_ADS_ACCOUNT_ID="your_default_account_id"
```

## Credential sources

- Azure app registration credentials (`BING_ADS_CLIENT_ID`, `BING_ADS_CLIENT_SECRET`)
- Microsoft Advertising developer token
- OAuth refresh token for Microsoft Advertising scope
- Default customer/account IDs used for request context

## Verification guidance

- Confirm credentials are set in environment variables.
- Once Bing MCP is available, verification should list accounts and run a read-only query.
