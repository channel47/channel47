---
name: pmax-decoder
description: >-
  This skill should be used when the user asks about "Performance Max",
  "PMax", "PMax search terms", "PMax insights", "what is PMax doing",
  "PMax transparency", "PMax placements", "PMax asset performance",
  "decode my PMax", "PMax brand traffic", "PMax cannibalization", or
  mentions Performance Max analysis, PMax audit, PMax search queries,
  asset group performance, or PMax negative keywords.
---

# PMax Decoder

Generate operational transparency for Performance Max campaigns and convert that
analysis into concrete actions.

## Foundation Dependency

Scripts live in `skills/ad-platform-connection` — add it to `sys.path` before
importing:

```python
import sys, os
skill_root = os.path.join(os.environ.get("CLAUDE_PLUGIN_ROOT", "."), "skills", "ad-platform-connection")
sys.path.insert(0, skill_root)

from scripts.google.auth import get_auth
from scripts.google.report import pull_report
from scripts.google.mutate import add_negative_keywords
```

## Workflow

### Module 1: Search term extraction

The `campaign_search_term_insight` resource requires single-campaign filtering.
Follow this loop pattern:

```python
# Step 1: Get all PMax campaigns (Module 1A query)
campaigns_df = pull_report(client, customer_id, QUERY_1A)

# Step 2: For each campaign, get insight categories (Module 1B query)
all_categories = []
for _, row in campaigns_df.iterrows():
    cid = str(int(row["campaign.id"]))
    query_1b = QUERY_1B.replace("CAMPAIGN_ID", cid)
    cat_df = pull_report(client, customer_id, query_1b)
    if not cat_df.empty:
        all_categories.append(cat_df)

# Step 3: Optionally drill into top categories by clicks (Module 1C)
top_categories = pd.concat(all_categories).nlargest(50, "metrics.clicks")
for _, cat_row in top_categories.iterrows():
    cid = str(int(cat_row["campaign_search_term_insight.campaign_id"]))
    cat_id = cat_row["campaign_search_term_insight.id"]
    query_1c = QUERY_1C.replace("CAMPAIGN_ID", cid).replace("CATEGORY_ID", cat_id)
    terms_df = pull_report(client, customer_id, query_1c)
```

Default cap: top 50 categories by clicks. Warn user that large PMax accounts
with many campaigns will generate many API calls.

### Module 2: Channel distribution (requires API v23+)

**IMPORTANT**: `segments.ad_network_type` on `asset_group` returns meaningful
channel data (SEARCH, YOUTUBE, DISPLAY, SHOPPING) only in API v23+. For dates
before June 1, 2025, it returns `MIXED` and is not useful. Verify the client's
API version before running this module. If pre-v23, skip and note the limitation.

Use `asset_group` with `segments.ad_network_type` to estimate spend and conversion
mix by channel. Flag concentration risks when one channel exceeds 70% of spend.

### Module 3: Asset group and asset label review

- Summarize asset-group level performance (Module 3A: impressions, clicks, cost, conversions).
- Pull `asset_group_asset.performance_label` per asset (Module 3B).
- Labels are relative rankings (`BEST`, `GOOD`, `LOW`, `PENDING`), NOT cost metrics.
  Do NOT claim a `LOW` label means the asset is "wasting money" — it means the asset
  underperforms relative to other assets in the same group.
- Recommend replacement priorities for `LOW` assets. Do not generate creative copy
  unless the user explicitly requests it.

### Module 4: Brand traffic detection

- Require user-provided brand terms before running this module.
- Classify Module 1C search terms against that brand list.
- `campaign_search_term_insight` does not include cost metrics. Use **click share**
  as the proxy (not spend share). Report this limitation clearly.
- Flag cannibalization risk when brand click share exceeds 30% of PMax clicks.
- Generate dry-run negative keyword package for review:

```python
result = add_negative_keywords(
    client, customer_id,
    keywords=[{"text": brand_term, "match_type": "EXACT"}],
    level="campaign",
    parent_id=campaign_id,
    dry_run=True,
)
```

### Module 5: Placement review

Use `performance_max_placement_view` for inventory visibility.
Placement view returns **impressions only** — no clicks, cost, or conversions.
Do not estimate placement-level cost or CPA. Treat findings as quality-risk
diagnostics (e.g., flag low-quality placements like parked domains or children's
apps by name/type).

## Output format

```markdown
## PMax Decoder - [Date]
### Campaign: [Name] ([ID])

### Quick Stats (from Module 1A campaign data)
- Spend, conversions, CPA (cost/conversions), ROAS (conversions_value/cost)

### Channel Distribution
| Channel | Spend | % Spend | Conversions | CPA |
|---|---:|---:|---:|---:|

### Brand Traffic Analysis
- [brand click share, click volume, top branded terms]
- [negative keyword package preview]

### Search Term Insight Categories
| Category | Clicks | Conversions | Notes |
|---|---:|---:|---|

### Asset Performance
| Asset Group | Ad Strength | LOW Assets | Action |
|---|---|---:|---|

### Placement Summary
- [top placement types and quality risks]

### Recommended Actions
1. [prioritized action]
```

## Guardrails

- `campaign_search_term_insight` requires single-campaign filtering.
- Channel-level `segments.ad_network_type` data is available only for dates after
  June 1, 2025.
- Placement view provides impressions only; do not claim placement-level cost.
- Never execute live negatives without explicit user confirmation.
- **Empty results**: when a module query returns zero rows, report it explicitly
  (e.g., "No search term insight data available for this campaign") rather than
  silently omitting the section. Common causes: new campaigns, privacy thresholds,
  API version mismatch.

## References

- `references/gaql-queries.md`
