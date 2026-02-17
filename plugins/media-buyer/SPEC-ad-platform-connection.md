# Ad Platform Connection Skill — Detailed Spec

> **Status:** Draft v2 — awaiting approval before implementation
> **Scope:** Bing + Google (initial). Meta + TikTok deferred.
> **Plugin:** `media-buyer` v3.1.0 → v4.0.0
> **Architecture:** Self-contained Python scripts per platform. No MCP dependency.

---

## 1. Purpose

A unified skill that enables Claude — or any agent — to **connect to, manage, and report on** paid advertising accounts across multiple platforms. It acts as a routing layer: detect the user's target platform, load platform-specific references and scripts, and execute operations through bundled Python scripts.

**What this skill IS:**
- A self-contained connection and management layer (auth, CRUD, reporting, bulk ops)
- A platform-aware router that loads only what's needed
- The operational backbone that other media-buyer skills build on
- Portable — works with any agent that can run Python, not just Claude Code with MCP

**What this skill IS NOT:**
- A campaign strategy builder (that's `search-campaign`)
- A creative generator (that's `creative-variants`)
- An audit framework (that's `audit`)

---

## 2. Relationship to Existing Skills

```
┌─────────────────────────────────────────────────────┐
│                  media-buyer plugin                  │
│                                                     │
│  ┌──────────────┐  ┌──────────────┐  ┌───────────┐ │
│  │   search-     │  │  creative-   │  │   audit   │ │
│  │   campaign    │  │  variants    │  │           │ │
│  │  (strategy)   │  │  (creative)  │  │ (analyze) │ │
│  └──────┬───────┘  └──────────────┘  └─────┬─────┘ │
│         │                                   │       │
│         │  "build this in the account"      │       │
│         ▼                                   ▼       │
│  ┌─────────────────────────────────────────────┐    │
│  │         ad-platform-connection              │    │
│  │  (auth · manage · report · bulk ops)        │    │
│  │                                             │    │
│  │   Google ──► Bundled Python scripts          │   │
│  │              (google-ads SDK)                │   │
│  │   Bing ───► Bundled Python scripts           │   │
│  │              (bingads SDK)                   │   │
│  └─────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────┘
```

The connector is the **execution layer**. Other skills produce strategy and analysis; this skill pushes changes into accounts and pulls data out.

**Integration points:**
- `search-campaign` produces a campaign spec → connector creates it in Google/Bing
- `audit` needs account data → connector's reporting capabilities feed it
- `creative-variants` produces images → connector uploads them as ad assets

**Relationship to Google Ads MCP server:**
The MCP server at `ch47/ecosystem/packages/mcps/google-ads/` remains a standalone product. This skill's Google scripts are the portable, self-contained equivalent — same API capabilities, no MCP dependency. The MCP server's GAQL templates and mutation patterns inform the reference docs and script design, but the skill does not depend on or call the MCP server.

---

## 3. Directory Structure

```
skills/ad-platform-connection/
├── SKILL.md                           # Lean router (~1,800 words)
│
├── scripts/
│   ├── google/
│   │   ├── auth.py                    # OAuth2 + google-ads SDK client init
│   │   ├── report.py                  # GAQL queries → pandas DataFrames
│   │   └── mutate.py                  # Write operations (dry_run=True default)
│   └── bing/
│       ├── auth.py                    # Ported from fouram (OAuth2 + token rotation)
│       └── report.py                  # Ported from fouram (pandas DataFrame reporting)
│
└── references/
    ├── shared/
    │   └── config-patterns.md         # Cross-platform: config files, auth rotation,
    │                                  #   bulk thresholds, account mapping, setup guide
    ├── google/
    │   ├── campaign-management.md     # GAQL patterns for campaign/ad group/keyword/ad CRUD
    │   ├── shopping-campaigns.md      # Shopping campaign setup + product partition trees
    │   └── reporting.md               # GAQL query patterns for common reports + segmentation
    └── bing/
        ├── campaign-management.md     # Ported from fouram — SDK patterns for CRUD
        ├── shopping-campaigns.md      # Ported from fouram — ShoppingSetting, partition trees
        ├── content-api.md             # Ported from fouram — Merchant Center REST API
        └── bulk-operations.md         # Ported from fouram — CSV bulk upload/download
```

### Design decisions

- **Symmetrical scripts per platform.** Both Google and Bing have `auth.py` + `report.py`. Google adds `mutate.py` because mutations are complex enough to warrant a dedicated helper; Bing mutations go through SDK calls documented in references.
- **No examples/ directory.** Reference docs embed inline examples. Standalone example files add maintenance burden without clear value here.
- **No MCP dependency.** The Google Ads MCP server is a separate product. This skill is fully self-contained.
- **No Meta or TikTok directories yet.** Deferred to v4.1.0+. The structure accommodates them when ready (`references/meta/`, `scripts/meta/`).
- **Google `mutation-patterns.md` merged into `campaign-management.md`.** With scripts handling the mechanics, the reference docs focus on GAQL patterns and entity relationships. Mutation details (temp IDs, bidding strategies, entity types) live in `mutate.py` docstrings and `campaign-management.md` inline examples. One fewer file to maintain.

---

## 4. SKILL.md Draft

```markdown
---
name: ad-platform-connection
description: >-
  This skill should be used when the user asks to "connect to Google Ads",
  "connect to Bing Ads", "set up ad account", "pull ad performance",
  "create a campaign in Google", "create a campaign in Bing",
  "upload products to Merchant Center", "pause keywords",
  "bulk update ads", "manage ad account", or mentions
  Microsoft Advertising, Google Ads API, GAQL, or Bing Ads SDK.
version: 1.0.0
---

# Ad Platform Connection

Unified connection and management layer for paid advertising platforms.
Detect the target platform, load platform-specific references, and execute
operations through bundled Python scripts.

## Supported Platforms

| Platform | SDK | Auth Config | Scripts |
|----------|-----|-------------|---------|
| Google Ads | `google-ads` (Python) | `~/.google_ads_config.json` | `scripts/google/{auth,report,mutate}.py` |
| Bing Ads | `bingads` (Python) | `~/.msads_config.json` | `scripts/bing/{auth,report}.py` |

## Platform Detection

Identify the target platform from user intent before loading references:

- **Google signals:** "Google Ads", "GAQL", "Google Shopping", "Performance Max", "RSA"
- **Bing signals:** "Bing", "Microsoft Advertising", "Microsoft Merchant Center", "MSAN"
- **Ambiguous:** Ask which platform. Default to Google if context suggests paid search generally.

## Routing Table

### Google Ads

| Intent | Reference | Script |
|--------|-----------|--------|
| Auth / account setup | `references/shared/config-patterns.md` | `scripts/google/auth.py` |
| List accounts | — | `scripts/google/auth.py` → `verify_connection()` |
| Campaign/ad group/keyword CRUD | `references/google/campaign-management.md` | `scripts/google/mutate.py` |
| Shopping campaigns | `references/google/shopping-campaigns.md` | `scripts/google/mutate.py` |
| Pull reports / performance data | `references/google/reporting.md` | `scripts/google/report.py` |
| Write operations (create/update/pause) | `references/google/campaign-management.md` | `scripts/google/mutate.py` |

### Bing Ads

| Intent | Reference | Script |
|--------|-----------|--------|
| Auth / account setup | `references/shared/config-patterns.md` | `scripts/bing/auth.py` |
| Campaign/ad group/keyword CRUD | `references/bing/campaign-management.md` | via `bingads` SDK |
| Shopping campaigns | `references/bing/shopping-campaigns.md` | via `bingads` SDK |
| Merchant Center / product catalog | `references/bing/content-api.md` | REST API calls |
| Pull reports / performance data | `references/bing/campaign-management.md` | `scripts/bing/report.py` |
| Bulk operations (50+ entities) | `references/bing/bulk-operations.md` | via `BulkServiceManager` |

## Script Interface Pattern

Both platforms follow the same script pattern:

### Authentication

```python
from scripts.{platform}.auth import get_auth, verify_connection

client, config = get_auth()           # Load config, build client
accounts = verify_connection(client)   # List accessible accounts
```

Google config: `~/.google_ads_config.json`
Bing config: `~/.msads_config.json`

Consult `references/shared/config-patterns.md` for config file setup instructions.

### Reporting

```python
from scripts.{platform}.report import pull_report, quick_campaign_summary

df = quick_campaign_summary(client, customer_id)     # Standard KPIs
df = pull_report(client, customer_id, query_or_type)  # Custom query
```

Both return pandas DataFrames with cleaned numeric columns.

### Mutations (Google)

```python
from scripts.google.mutate import execute_mutation, create_campaign, pause_entities

# Always dry_run=True first
result = execute_mutation(client, customer_id, operations, dry_run=True)
# Review with user, then:
result = execute_mutation(client, customer_id, operations, dry_run=False)
```

### Mutations (Bing)

Bing mutations use SDK service calls documented in `references/bing/campaign-management.md`.
Read the reference for code patterns. For 50+ entity changes, use bulk operations
per `references/bing/bulk-operations.md`.

## Key Constraints

### Google

- `customer_id` is 10 digits, no dashes
- Monetary values are in micros (÷ 1,000,000 for dollars)
- RSA content updates use `ads/{ad_id}` resource names
- RSA status changes use `adGroupAds/{ag_id}~{ad_id}` resource names
- Campaign creation requires atomic budget + campaign operations using temp IDs

### Bing

- SOAP-based SDK — always null default enum/object fields on factory-created
  objects before API calls to avoid empty-string serialization errors
- `ReportTimeZone` is required or the API throws a deserialization error
- Report CSV numbers are comma-formatted — `report.py` handles cleanup
- Use individual service calls for < 50 entities, bulk CSV for 50+

## Safety Protocol

1. **Read before write.** Always query current state before modifying.
2. **Dry run first.** Google: `dry_run=True` (default). Bing: preview operations before executing.
3. **Confirm with user.** Surface what will change and get explicit approval.
4. **Small batches.** For bulk operations, start with a small batch to verify, then scale.
5. **Never delete without confirmation.** Pause is reversible. Delete is not.

## Dependencies

| Package | Platform | Install |
|---------|----------|---------|
| `google-ads` | Google | `pip install google-ads` |
| `bingads` | Bing | `pip install bingads` |
| `pandas` | Both | `pip install pandas` |

## Additional Resources

### Reference Files

**Shared:**
- **`references/shared/config-patterns.md`** — Config file setup, auth rotation, account mapping, bulk thresholds

**Google:**
- **`references/google/campaign-management.md`** — GAQL patterns for entity CRUD, mutation formats, entity types
- **`references/google/shopping-campaigns.md`** — Shopping campaign and product partition setup
- **`references/google/reporting.md`** — Common GAQL report queries, segmentation, date filtering

**Bing:**
- **`references/bing/campaign-management.md`** — SDK patterns for campaign/ad group/keyword/ad operations
- **`references/bing/shopping-campaigns.md`** — Shopping campaigns and product partition trees
- **`references/bing/content-api.md`** — Merchant Center REST API for product catalogs
- **`references/bing/bulk-operations.md`** — CSV-based bulk upload/download patterns

### Scripts

**Google:**
- **`scripts/google/auth.py`** — OAuth2 + `google-ads` client initialization
- **`scripts/google/report.py`** — GAQL queries → pandas DataFrames
- **`scripts/google/mutate.py`** — Write operations with dry_run default

**Bing:**
- **`scripts/bing/auth.py`** — OAuth2 with auto-rotating refresh tokens
- **`scripts/bing/report.py`** — Reporting helper returning pandas DataFrames
```

---

## 5. Scripts — Detailed Design

### Google Scripts (NEW)

#### `scripts/google/auth.py`

**Config file:** `~/.google_ads_config.json`

```json
{
  "client_id": "...",
  "client_secret": "...",
  "developer_token": "...",
  "refresh_token": "...",
  "login_customer_id": "",
  "default_customer_id": "..."
}
```

**Functions:**

| Function | Signature | Purpose |
|----------|-----------|---------|
| `get_auth` | `(config_path=None) → (GoogleAdsClient, dict)` | Load config, build `GoogleAdsClient` from `google-ads` library, auto-rotate refresh token if changed, persist back to config. |
| `switch_customer` | `(client, customer_id) → GoogleAdsClient` | Return new client instance targeting different customer. |
| `verify_connection` | `(client, customer_id=None) → list[dict]` | List accessible accounts via `CustomerService`. Returns list of `{id, name, is_manager, currency, timezone, status}`. |
| `list_accounts` | `(client, include_managers=False) → list[dict]` | Query `customer_client` resource. Mirrors MCP's `list_accounts` tool output. |

**Implementation notes:**
- Uses `google-ads` Python client library (Google's official SDK, `google.ads.googleads.client.GoogleAdsClient`)
- Client init via `GoogleAdsClient.load_from_dict()` with config dict
- Refresh token rotation: compare token before/after `refresh()`, write back if different (same pattern as Bing)
- `login_customer_id` used for MCC access (optional, empty string if not needed)

**Source material:** Google Ads MCP's `server/auth.js` (translated from Node.js/Opteo to Python/official SDK)

#### `scripts/google/report.py`

**Functions:**

| Function | Signature | Purpose |
|----------|-----------|---------|
| `pull_report` | `(client, customer_id, query, limit=100) → pd.DataFrame` | Execute GAQL SELECT query. Flatten nested objects to dot-notation. Auto-convert `_micros` fields. Return cleaned DataFrame. |
| `quick_campaign_summary` | `(client, customer_id, date_range='LAST_30_DAYS') → pd.DataFrame` | Pre-wired: impressions, clicks, CTR, spend, conversions, CPA, ROAS at campaign level. |
| `quick_adgroup_summary` | `(client, customer_id, date_range='LAST_30_DAYS') → pd.DataFrame` | Pre-wired: ad group level KPIs. |
| `quick_keyword_performance` | `(client, customer_id, date_range='LAST_30_DAYS') → pd.DataFrame` | Pre-wired: keyword level with match type and quality score. |
| `quick_search_terms` | `(client, customer_id, date_range='LAST_30_DAYS') → pd.DataFrame` | Pre-wired: search term report with spend and conversion data. |
| `quick_shopping_summary` | `(client, customer_id, date_range='LAST_30_DAYS') → pd.DataFrame` | Pre-wired: product-level shopping KPIs. |
| `quick_wasted_spend` | `(client, customer_id, date_range='LAST_30_DAYS') → pd.DataFrame` | Pre-wired: high-cost zero-conversion keywords and search terms. |

**Implementation notes:**
- Uses `GoogleAdsService.SearchStream()` for efficient streaming
- Flattens protobuf response objects to dict with dot-notation keys (e.g., `campaign.name`, `metrics.clicks`)
- Micros conversion: for any field ending in `_micros`, adds a derived field without suffix (e.g., `metrics.cost_micros` → `metrics.cost`)
- Date range handling: accepts GAQL date predicates or friendly names (`LAST_7_DAYS`, `LAST_30_DAYS`, `THIS_MONTH`, etc.)
- Quick functions embed GAQL queries derived from the MCP server's 19 GAQL templates

**Source material:** Google Ads MCP's `server/utils/gaql-templates.js` (19 templates) + Bing's `report.py` pattern

#### `scripts/google/mutate.py`

**Functions:**

| Function | Signature | Purpose |
|----------|-----------|---------|
| `execute_mutation` | `(client, customer_id, operations, dry_run=True, partial_failure=True) → dict` | Execute mutations via `GoogleAdsService.Mutate()`. Returns `{success, results, errors}`. **dry_run=True by default.** |
| `create_campaign` | `(client, customer_id, campaign_spec, dry_run=True) → dict` | Atomic budget + campaign creation using temp resource names. Accepts a structured campaign spec dict. |
| `pause_entities` | `(client, customer_id, resource_names, dry_run=True) → dict` | Batch pause any entity type (campaigns, ad groups, keywords, ads). |
| `add_negative_keywords` | `(client, customer_id, keywords, level, parent_id, dry_run=True) → dict` | Add negatives at campaign or ad group level. |
| `create_rsa` | `(client, customer_id, ad_group_id, headlines, descriptions, final_urls, dry_run=True) → dict` | Create responsive search ad with proper asset structure. |
| `update_bids` | `(client, customer_id, bid_changes, dry_run=True) → dict` | Batch bid adjustments with safety validation (max 50% change default). |

**Implementation notes:**
- All functions default to `dry_run=True` — live execution requires explicit `dry_run=False`
- Uses `GoogleAdsService.Mutate()` with `MutateOperation` protobuf messages
- Temp resource names for atomic operations: `customers/{id}/campaignBudgets/-1` referenced by `customers/{id}/campaigns/-2`
- Entity type inferred from resource name URL segments (same mapping as MCP's `operation-transform.js`)
- `create_campaign` handles the EU political advertising field (`contains_eu_political_advertising`)
- `update_bids` includes safety check: rejects changes > 50% by default (configurable)

**Entity type mapping (from resource name URL segments):**

| URL Segment | Entity |
|-------------|--------|
| `campaigns` | `campaign` |
| `adGroups` | `ad_group` |
| `adGroupCriteria` | `ad_group_criterion` |
| `campaignCriteria` | `campaign_criterion` |
| `campaignBudgets` | `campaign_budget` |
| `biddingStrategies` | `bidding_strategy` |
| `ads` | `ad` (content) |
| `adGroupAds` | `ad_group_ad` (status) |
| `assets` | `asset` |
| `labels` | `label` |
| `sharedSets` | `shared_set` |
| `sharedCriteria` | `shared_criterion` |
| `conversionActions` | `conversion_action` |
| `customerNegativeCriteria` | `customer_negative_criterion` |
| `userLists` | `user_list` |

**Supported bidding strategies:**
`manual_cpc`, `manual_cpm`, `manual_cpv`, `maximize_conversions`, `maximize_conversion_value`, `target_cpa`, `target_roas`, `target_spend`, `target_impression_share`, `percent_cpc`, `commission`, `bidding_strategy` (portfolio)

**Source material:** Google Ads MCP's `server/tools/mutate.js`, `server/utils/operation-transform.js`, `server/utils/mutations.js`, `server/utils/image-asset.js`

### Bing Scripts (PORT from fouram)

#### `scripts/bing/auth.py` — PORT

Port `fouram/.claude/skills/bing-ads/scripts/auth.py` with these changes:

| Change | Reason |
|--------|--------|
| Update internal doc comments | Reference media-buyer plugin context instead of fouram |
| No functional changes | The auth logic is battle-tested and correct |

**Config file:** `~/.msads_config.json` (unchanged — user-level config)

**Functions:**
- `get_auth(config_path=None)` → `(auth_data, content_api_headers, config)`
- `switch_account(auth_data, config, new_account_id)` — swap account without re-auth
- `get_merchant_id(config, product_slug)` — lookup Merchant Center store ID
- `verify_connection(auth_data, config)` — connectivity check via `GetAccount`

#### `scripts/bing/report.py` — PORT

Port `fouram/.claude/skills/bing-ads/scripts/report.py` with these changes:

| Change | Reason |
|--------|--------|
| Update import path for auth | Adjust relative import to new location |
| Update doc comments | Reference media-buyer plugin context |
| No functional changes | Report logic is clean and correct |

**Functions:**
- `pull_report(auth_data, account_id, report_type, ...)` → `pd.DataFrame`
- `quick_campaign_summary(auth_data, account_id, ...)` → `pd.DataFrame`
- `quick_shopping_summary(auth_data, account_id, ...)` → `pd.DataFrame`

---

## 6. Reference Files — Content Plan

### `references/shared/config-patterns.md` (~1,000 words) — NEW

| Section | Content |
|---------|---------|
| Overview | Both platforms use JSON config files with OAuth2 credentials. No env vars required. |
| Google setup | Create `~/.google_ads_config.json`. Fields: `client_id`, `client_secret`, `developer_token`, `refresh_token`, `login_customer_id`, `default_customer_id`. How to get each credential (Google Cloud Console → OAuth2 client, Google Ads API Center → developer token). |
| Bing setup | Create `~/.msads_config.json`. Fields: `client_id`, `developer_token`, `refresh_token`, `customer_id`, `account_id`, `merchant_stores`. Re-auth flow when token expires. |
| Auth token rotation | Both scripts auto-rotate refresh tokens. Pattern: compare token before/after refresh, persist if changed. |
| Account switching | Google: `switch_customer(client, id)`. Bing: `switch_account(auth_data, config, id)`. |
| Account/product mapping | Bing's `merchant_stores` dict pattern. Google's `default_customer_id` pattern. Per-product account IDs in `meta.yaml`. |
| Report abstraction | Common KPI set: impressions, clicks, CTR, spend, conversions, CPA, ROAS. Both platforms return pandas DataFrames. |
| Bulk thresholds | < 50 entities → individual calls. 50+ → bulk API. Google: batch mutate. Bing: CSV bulk upload. |
| Dependencies | `pip install google-ads bingads pandas` |

### `references/google/campaign-management.md` (~2,000 words) — NEW

| Section | Content |
|---------|---------|
| Entity hierarchy | Account → Campaign (+ Budget) → Ad Group → Keywords, Ads, Criteria |
| GAQL query patterns | SELECT patterns for each entity with common WHERE filters and date ranges |
| Campaign CRUD | Create via `mutate.py` `create_campaign()` — atomic budget + campaign. Update status, pause/enable via `pause_entities()`. |
| Ad Group CRUD | Create under campaign, CPC bid management, status changes |
| Keyword management | Add with match types (EXACT, PHRASE, BROAD), pause/remove, negative keywords at campaign + ad group level via `add_negative_keywords()` |
| Ad management | RSA creation via `create_rsa()` — headlines + descriptions as assets. Status changes via `pause_entities()`. Content updates via `execute_mutation()`. |
| Bid management | `update_bids()` with safety validation. Bidding strategy selection table. |
| Mutation format | How to construct operation dicts for `execute_mutation()`. Entity type inference from resource names. Temp ID pattern for atomic creates. |
| Safety patterns | dry_run workflow, bid change limits, EU political advertising field |

**Source:** Google Ads MCP's GAQL templates, mutation patterns, entity type mapping — translated to script-based workflow.

### `references/google/shopping-campaigns.md` (~1,200 words) — NEW

| Section | Content |
|---------|---------|
| Shopping campaign creation | Campaign type, shopping settings, feed linkage via `create_campaign()` |
| Product partition trees | Subdivision vs. unit nodes, building trees via `execute_mutation()` |
| Performance Max | Setup patterns, asset groups |
| Product feed health | GAQL status queries via `report.py` |
| Shopping reporting | `quick_shopping_summary()` usage |

**Source:** Google Ads MCP's shopping GAQL templates + Google Ads API docs.

### `references/google/reporting.md` (~1,200 words) — NEW

| Section | Content |
|---------|---------|
| Quick functions | `quick_campaign_summary()`, `quick_adgroup_summary()`, `quick_keyword_performance()`, `quick_search_terms()`, `quick_shopping_summary()`, `quick_wasted_spend()` — when to use each |
| Custom GAQL queries | GAQL syntax reference for `pull_report()`. Resource types, field names, WHERE clauses, ORDER BY, LIMIT. |
| Date filtering | GAQL date range syntax. Predefined periods vs. custom ranges. |
| Segmentation | By device, hour, day of week, geo, audience — GAQL segment fields |
| Micros conversion | `report.py` auto-converts `_micros` fields. Manual pattern documented. |
| Wasted spend analysis | `quick_wasted_spend()` for high-cost zero-conversion identification |
| Quality Score | GAQL patterns for QS components (expected CTR, ad relevance, landing page) |

**Source:** Google Ads MCP's 19 built-in GAQL templates.

### `references/bing/campaign-management.md` (~2,000 words) — PORT from fouram

Direct port of fouram's `references/campaign_management.md` with:
- Auth section updated to reference `scripts/bing/auth.py` at plugin path
- Code patterns for campaigns, ad groups, keywords, ads
- RSA creation with AssetLink/TextAsset pattern
- Operations summary table

### `references/bing/shopping-campaigns.md` (~1,800 words) — PORT from fouram

Direct port of fouram's `references/shopping_campaigns.md`:
- Shopping campaign creation with ShoppingSetting
- Product partition tree building
- `null_criterion_fields()` helper pattern
- Smart Shopping setup
- Limits documentation

### `references/bing/content-api.md` (~1,500 words) — PORT from fouram

Direct port of fouram's `references/content_api.md`:
- Catalog CRUD
- Product CRUD with pagination
- Batch operations (2,000 items / 4MB chunks)
- Product schema
- Error code table

### `references/bing/bulk-operations.md` (~1,200 words) — PORT from fouram

Direct port of fouram's `references/bulk_operations.md`:
- Download/upload patterns
- Entity types available for bulk
- CSV format documentation
- Batch pause and bid adjustment patterns
- Limits (100MB, 15-minute timeout)

---

## 7. Plugin Manifest Update

```json
{
  "name": "media-buyer",
  "version": "4.0.0",
  "description": "Multi-platform paid advertising: build campaigns, generate creative variants, connect and manage ad accounts (Google + Bing), and audit performance. Fully self-contained — no MCP servers required.",
  "author": { "name": "Jackson Dean", "url": "https://channel47.dev" },
  "homepage": "https://channel47.dev/plugins/media-buyer",
  "repository": "https://github.com/channel47/channel47",
  "keywords": [
    "google-ads", "bing-ads", "microsoft-advertising",
    "search-campaign", "ad-creative", "media-buying",
    "ppc", "creative-testing", "account-audit",
    "ad-platform", "paid-ads"
  ],
  "license": "MIT"
}
```

Changes: version bump to 4.0.0, description updated (mentions self-contained), keywords expanded.

---

## 8. Implementation Sequence

### Phase 1: Scaffold + Port Bing

1. Create directory structure:
   ```
   skills/ad-platform-connection/
   ├── SKILL.md
   ├── scripts/{google,bing}/
   └── references/{shared,google,bing}/
   ```

2. Port Bing scripts from fouram:
   - `scripts/bing/auth.py` (adjust comments only)
   - `scripts/bing/report.py` (adjust import path)

3. Port Bing references from fouram:
   - `references/bing/campaign-management.md`
   - `references/bing/shopping-campaigns.md`
   - `references/bing/content-api.md`
   - `references/bing/bulk-operations.md`

### Phase 2: Build Google Scripts

4. Write `scripts/google/auth.py`:
   - `GoogleAdsClient.load_from_dict()` initialization
   - Config file load/save with token rotation
   - `get_auth()`, `switch_customer()`, `verify_connection()`, `list_accounts()`

5. Write `scripts/google/report.py`:
   - `SearchStream()` based GAQL execution
   - Protobuf → dict flattening with dot-notation
   - Micros auto-conversion
   - `pull_report()` + 6 quick functions

6. Write `scripts/google/mutate.py`:
   - `MutateOperation` protobuf construction
   - Entity type inference from resource names
   - Temp resource name pattern for atomic creates
   - `execute_mutation()` + 5 convenience functions

### Phase 3: References + SKILL.md

7. Write `references/shared/config-patterns.md`

8. Write Google reference docs:
   - `references/google/campaign-management.md`
   - `references/google/shopping-campaigns.md`
   - `references/google/reporting.md`

9. Write final `SKILL.md` (routing table, platform detection, safety protocol)

10. Update `plugin.json` (version, description, keywords)

### Phase 4: Validation

11. Validate skill structure and trigger phrases
12. Verify all referenced files exist
13. Test Bing auth + reporting flow with live account
14. Test Google auth + reporting + mutation (dry_run) with live account
15. Verify cross-skill integration: search-campaign output → connector execution

---

## 9. Future Expansion (v4.1.0+)

### Meta Ads
- `scripts/meta/auth.py` — Facebook Marketing API OAuth
- `scripts/meta/report.py` — Insights API → DataFrames
- `references/meta/campaign-management.md` — Campaign, ad set, ad CRUD
- `references/meta/catalog-api.md` — Product catalog for dynamic ads

### TikTok Ads
- `scripts/tiktok/auth.py` — TikTok Marketing API auth
- `scripts/tiktok/report.py` — Reporting → DataFrames
- `references/tiktok/campaign-management.md` — Campaign, ad group, ad CRUD

### Structural additions
- Add platform directories under `scripts/` and `references/`
- Extend SKILL.md routing table with new platform sections
- Add platform detection signals (Meta: "Facebook Ads", "Instagram Ads", "CAPI"; TikTok: "TikTok Ads", "Spark Ads")
- Each new platform follows the same pattern: `auth.py` + `report.py` + references

The directory structure and SKILL.md routing table pattern already accommodate this — adding a platform is additive, not architectural.

---

## 10. Audit Skill Migration Path

The existing `audit` skill directly calls Google Ads MCP tools (`mcp__google-ads__query`). With the connector skill providing script-based Google access, the audit skill can be updated to use `scripts/google/report.py` instead.

**Migration plan (v4.1.0):**
1. Update audit's GAQL queries to use `report.py`'s `pull_report()` and quick functions
2. Remove MCP tool references from audit skill
3. Audit skill gains Bing support for free (just add Bing-specific queries using `scripts/bing/report.py`)
4. The audit skill's `references/performance-benchmarks.md` remains unchanged

This is not a v4.0.0 blocker — the audit skill continues to work via MCP for Google-only users. The migration happens when Bing audit support is added.

---

## 11. File Count Summary

| Category | Files | Status |
|----------|-------|--------|
| SKILL.md | 1 | New |
| Google scripts | 3 | New (`auth.py`, `report.py`, `mutate.py`) |
| Bing scripts | 2 | Port from fouram (`auth.py`, `report.py`) |
| Shared references | 1 | New (`config-patterns.md`) |
| Google references | 3 | New (`campaign-management.md`, `shopping-campaigns.md`, `reporting.md`) |
| Bing references | 4 | Port from fouram |
| **Total** | **14** | **6 new, 6 ported, 1 SKILL.md, 1 plugin.json update** |

---

## 12. Open Questions

1. **Should the Bing scripts be copied or symlinked from fouram?**
   Recommendation: **copy**. The fouram skill serves a different context (day job). The media-buyer plugin should be self-contained for distribution.

2. **Should `mutate.py` exist for Bing too?**
   Recommendation: **not yet**. Bing mutations are documented in references and use SDK calls directly. If Bing mutation patterns prove complex enough to warrant a helper script, add `scripts/bing/mutate.py` in a later version.

3. **Python version requirement?**
   Recommendation: **Python 3.9+**. The `google-ads` library requires 3.8+, `bingads` requires 3.6+. Target 3.9+ for consistency with the existing `creative-variants` skill.
