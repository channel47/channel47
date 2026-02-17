---
name: ad-platform-connection
description: >-
  This skill should be used when the user asks to "connect to Google Ads",
  "connect to Bing Ads", "set up my ad account", "pull campaign performance",
  "create a search campaign", "check my Bing account", "update keyword bids",
  "set up a shopping campaign", "pull a search term report", "add negative
  keywords", "upload products to Merchant Center", "bulk update keywords",
  "pause my campaigns", "check ad performance", or mentions Google Ads API,
  GAQL, Microsoft Advertising, Bing Ads SDK, or Merchant Center.
---

# Ad Platform Connection

Unified connection and execution layer for paid ad platforms inside the media-buyer plugin.
This skill routes to Google or Bing scripts and references based on user intent.

## Supported Platforms

| Platform | SDK | Config | Scripts |
|----------|-----|--------|---------|
| Google Ads | `google-ads` | `~/.google_ads_config.json` | `scripts/google/{auth,report,mutate}.py` |
| Bing Ads | `bingads` | `~/.msads_config.json` | `scripts/bing/{auth,report}.py` |

## Platform Detection

- Google signals: `Google Ads`, `GAQL`, `Performance Max`, `RSA`, `Google Shopping`
- Bing signals: `Bing`, `Microsoft Advertising`, `MSAN`, `Microsoft Merchant Center`
- Ambiguous intent: ask platform; default to Google for generic paid-search phrasing.

## Routing Table

### Google

| Intent | Reference | Script |
|--------|-----------|--------|
| Auth and account setup | `references/shared/config-patterns.md` | `scripts/google/auth.py` |
| List / verify accounts | `references/shared/config-patterns.md` | `scripts/google/auth.py` |
| Campaign/ad group/keyword/ad CRUD | `references/google/campaign-management.md` | `scripts/google/mutate.py` |
| Shopping setup | `references/google/shopping-campaigns.md` | `scripts/google/mutate.py` |
| Reporting | `references/google/reporting.md` | `scripts/google/report.py` |

### Bing

| Intent | Reference | Script |
|--------|-----------|--------|
| Auth and account setup | `references/shared/config-patterns.md` | `scripts/bing/auth.py` |
| Campaign/ad group/keyword/ad CRUD | `references/bing/campaign-management.md` | Bing SDK service calls |
| Shopping setup | `references/bing/shopping-campaigns.md` | Bing SDK service calls |
| Merchant Center catalog management | `references/bing/content-api.md` | Content API REST |
| Reporting | `references/bing/reporting.md` | `scripts/bing/report.py` |
| Bulk changes (50+) | `references/bing/bulk-operations.md` | `BulkServiceManager` |

## Script Interface Pattern

### Authentication - Google

```python
from scripts.google.auth import get_auth, verify_connection

client, config = get_auth()
accounts = verify_connection(client)
```

### Authentication - Bing

```python
from scripts.bing.auth import get_auth, verify_connection

auth_data, content_api_headers, config = get_auth()
success = verify_connection(auth_data, config)
```

### Reporting - Google

```python
from scripts.google.report import pull_report, quick_campaign_summary

df = quick_campaign_summary(client, customer_id)
df = pull_report(client, customer_id, gaql_query)
```

### Reporting - Bing

```python
from scripts.bing.report import pull_report, quick_campaign_summary

df = quick_campaign_summary(auth_data, account_id)
df = pull_report(auth_data, account_id, report_type, time_period)
```

### Google Mutations

```python
from scripts.google.mutate import execute_mutation

# Always validate first
preview = execute_mutation(client, customer_id, operations, dry_run=True)
# Then apply after confirmation
live = execute_mutation(client, customer_id, operations, dry_run=False)
```

## Safety Protocol

1. Read before write.
2. Dry run first (`dry_run=True` default in Google mutate helpers).
3. Confirm planned changes with the user before live execution.
4. Use small batches first, then scale.
5. Avoid deletes unless explicitly confirmed.

## Dependencies

```bash
pip install google-ads bingads pandas
```

## References

- Shared: `references/shared/config-patterns.md`
- Google: `references/google/{campaign-management,shopping-campaigns,reporting}.md`
- Bing: `references/bing/{campaign-management,shopping-campaigns,content-api,bulk-operations,reporting}.md`
