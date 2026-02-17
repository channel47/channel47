# Media Buyer Plugin v5 Architecture

## Vision

The media buyer plugin is the operational toolkit for paid search practitioners. It connects to live ad platforms and performs the daily work: analyzing search terms, detecting waste, surfacing anomalies, and decoding black-box campaign types. Every skill produces actionable artifacts — negative keyword lists, prioritized action items, dollar-quantified waste reports — not dashboards.

The plugin assumes Corey Haines' `marketing-skills` plugin handles the strategy layer (frameworks, psychology, planning). This plugin handles execution against live accounts.

## Plugin Structure

```
media-buyer/
├── .claude-plugin/
│   └── plugin.json
├── hooks/
│   ├── hooks.json                          # Mutation safety gate
│   └── validate-mutations.py
├── skills/
│   ├── ad-platform-connection/             # FOUNDATION — auth, reporting, mutations
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   │   ├── google/{auth,report,mutate}.py
│   │   │   └── bing/{auth,report}.py
│   │   └── references/
│   │       ├── shared/config-patterns.md
│   │       ├── google/{campaign-management,shopping-campaigns,reporting}.md
│   │       └── bing/{campaign-management,shopping-campaigns,content-api,bulk-operations,reporting}.md
│   │
│   ├── search-term-verdict/                # Categorize, negate, promote search terms
│   │   ├── SKILL.md
│   │   └── references/
│   │       ├── gaql-queries.md             # Verified GAQL for search term extraction
│   │       └── verdict-heuristics.md       # Classification logic and edge cases
│   │
│   ├── morning-brief/                      # Daily account health narrative
│   │   ├── SKILL.md
│   │   └── references/
│   │       └── gaql-queries.md             # Anomaly detection, budget pacing, disapprovals
│   │
│   ├── waste-detector/                     # Dollar-quantified leak finder
│   │   ├── SKILL.md
│   │   └── references/
│   │       ├── gaql-queries.md             # 8 waste-type detection queries
│   │       └── benchmarks.md               # Industry QS and CPA benchmarks
│   │
│   └── pmax-decoder/                       # PMax transparency + recommendations
│       ├── SKILL.md
│       └── references/
│           └── gaql-queries.md             # PMax-specific resources and limitations
│
├── README.md
└── LICENSE
```

## Dependency Chain

```
ad-platform-connection (foundation)
├── search-term-verdict    (uses: report.py → pull_report, mutate.py → add_negative_keywords)
├── morning-brief          (uses: report.py → pull_report, quick_campaign_summary, quick_wasted_spend)
├── waste-detector         (uses: report.py → pull_report, quick_wasted_spend, quick_keyword_performance)
└── pmax-decoder           (uses: report.py → pull_report, mutate.py → add_negative_keywords)
```

All four skills depend on `ad-platform-connection` for auth and data access. None depend on each other. They can be built in any order.

## Build Sequence (Recommended)

1. **search-term-verdict** — Highest frequency use case, highest dollar impact, exercises the full read-analyze-write loop
2. **morning-brief** — Daily use case, proves the plugin's value every morning
3. **waste-detector** — The "holy shit" moment that justifies installing the plugin
4. **pmax-decoder** — Massive demand, no good alternatives, most complex to implement

---

# Skill 1: Search Term Verdict Engine

## Purpose

Pull the search term report from Google Ads, reason through each term against campaign intent and business context, and produce a categorized verdict with ready-to-apply negative keyword lists.

This is the #1 time sink in PPC management. Media buyers spend 2-4 hours per week per account on manual search term review. The task is perfectly suited for an LLM because it requires semantic understanding of intent — not pattern matching.

## Trigger Patterns

```yaml
name: search-term-verdict
description: >-
  This skill should be used when the user asks to "review search terms",
  "analyze search queries", "find negative keywords", "check search term
  report", "clean up search terms", "search term audit", "find wasted
  spend on search terms", "what are people searching for", or mentions
  search term analysis, n-gram analysis, negative keyword mining, or
  query sculpting.
```

## How It Works

### Phase 1: Extract

Pull search term data using verified GAQL queries against `ad-platform-connection/scripts/google/report.py`.

**Query A — Full search term report (all campaign types):**

```sql
SELECT
  search_term_view.search_term,
  search_term_view.status,
  segments.search_term_match_type,
  campaign.id,
  campaign.name,
  campaign.advertising_channel_type,
  ad_group.id,
  ad_group.name,
  metrics.impressions,
  metrics.clicks,
  metrics.ctr,
  metrics.cost_micros,
  metrics.average_cpc,
  metrics.conversions,
  metrics.conversions_value,
  metrics.cost_per_conversion
FROM search_term_view
WHERE segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC
LIMIT 10000
```

**Query B — With triggering keyword text (Search campaigns only):**

```sql
SELECT
  search_term_view.search_term,
  search_term_view.status,
  segments.keyword.info.text,
  segments.keyword.info.match_type,
  segments.search_term_match_type,
  campaign.id,
  campaign.name,
  ad_group.id,
  ad_group.name,
  metrics.impressions,
  metrics.clicks,
  metrics.ctr,
  metrics.cost_micros,
  metrics.conversions,
  metrics.conversions_value,
  metrics.cost_per_conversion
FROM search_term_view
WHERE segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC
LIMIT 10000
```

> **API limitation:** Adding `segments.keyword.info.text` restricts results to Search Network keyword-based ad groups only. Shopping, DSA, and PMax rows are excluded. Run both queries: A for breadth, B for keyword-level mapping.

**Execution pattern:**

```python
from scripts.google.auth import get_auth
from scripts.google.report import pull_report

client, config = get_auth()
customer_id = config["customer_id"]

# Full breadth
df_all = pull_report(client, customer_id, QUERY_A)

# With keyword mapping (Search only)
df_search = pull_report(client, customer_id, QUERY_B)
```

### Phase 2: Analyze

For each search term, classify into one of four verdicts:

| Verdict | Meaning | Action |
|---------|---------|--------|
| **NEGATE** | Irrelevant or wasteful | Add as negative keyword (specify level: ad group, campaign, or account) |
| **PROMOTE** | High-intent term deserving dedicated targeting | Create as keyword in existing or new ad group |
| **INVESTIGATE** | Ambiguous — needs human judgment | Flag with reasoning for user review |
| **KEEP** | Performing as expected | No action needed |

Classification factors (ordered by weight):

1. **Conversion data** — Terms with conversions at acceptable CPA → KEEP. Terms with significant spend and zero conversions → likely NEGATE.
2. **Semantic relevance** — Does the term match the campaign's stated purpose? "Cheap running shoes" in a premium brand campaign → NEGATE regardless of cost.
3. **Match type drift** — Exact-match keyword triggering on a loosely related term → flag the match type issue.
4. **Already-excluded status** — `search_term_view.status = 'EXCLUDED'` → already handled, skip.
5. **Volume significance** — Low-impression terms (< 10 impressions) may not warrant action. Focus on terms with meaningful spend.

### Phase 3: Output

Produce a structured report with three sections:

**1. Verdict Summary Table**
- Total search terms analyzed
- Count per verdict category
- Total wasted spend identified (sum of cost on NEGATE terms)
- Top opportunities (PROMOTE terms with conversion data)

**2. Negative Keyword List (ready to apply)**
- Grouped by recommended level (campaign vs. ad group)
- Each with the reason and the spend it would have saved
- Generated as dry-run mutations via `add_negative_keywords()`

**3. Promotion Candidates**
- Terms that converted well but aren't dedicated keywords
- Suggested ad group placement
- Estimated impact of dedicated targeting

### Phase 4: Execute (with user approval)

After user reviews and approves the negative keyword list:

```python
from scripts.google.mutate import add_negative_keywords

# Apply approved negatives
result = add_negative_keywords(
    client, customer_id,
    keywords=approved_negatives,
    level="campaign",
    parent_id=campaign_id,
    dry_run=False,  # Only after explicit user confirmation
)
```

## Known Limitations

- **Privacy threshold:** Google hides search terms below a minimum search volume threshold. Typically 20-80% of actual search terms may be hidden depending on the account's niche. The skill should note the coverage gap in output.
- **PMax search terms:** Not available via `search_term_view`. Use the pmax-decoder skill for PMax-specific analysis.
- **10,000 row limit:** Large accounts may need date range narrowing or campaign filtering to stay under the GAQL LIMIT cap.
- **No cross-device attribution:** Search term data uses last-click within Google Ads. Cross-device and assisted conversions are not reflected.

## Reference Files

### `references/gaql-queries.md`
Contains the verified GAQL queries above, execution patterns, and field reference tables for `search_term_view`, including all available metrics and segments.

### `references/verdict-heuristics.md`
Contains the classification logic in detail:
- Industry-specific negative keyword seed lists (from former `search-campaign` skill's `negative-keywords.md`)
- Common false-positive patterns (terms that look irrelevant but convert)
- Match type drift detection patterns
- N-gram analysis approach (2-gram and 3-gram frequency for pattern detection)
- Conflict checking: ensure proposed negatives don't block positive keywords

---

# Skill 2: Morning Brief

## Purpose

One command that answers "what should I worry about today?" Pull overnight performance, detect anomalies ranked by dollar impact, check for disapproved ads and budget issues, and deliver a prioritized narrative.

This replaces the 30-60 minute morning ritual of clicking through the Google Ads UI. Every media buyer does this every day.

## Trigger Patterns

```yaml
name: morning-brief
description: >-
  This skill should be used when the user asks for a "morning brief",
  "daily check", "what happened overnight", "account health check",
  "what should I worry about", "how are my campaigns doing", "daily
  summary", "performance check", or mentions daily monitoring, anomaly
  detection, or account health. Also trigger on general questions about
  current campaign performance when no specific campaign or metric is
  specified.
```

## How It Works

### Data Collection (5 GAQL queries, run in sequence)

**Query 1 — Campaign performance with daily segmentation (30 days):**

```sql
SELECT
  campaign.id,
  campaign.name,
  campaign.status,
  campaign.advertising_channel_type,
  segments.date,
  metrics.impressions,
  metrics.clicks,
  metrics.ctr,
  metrics.cost_micros,
  metrics.conversions,
  metrics.conversions_value,
  metrics.cost_per_conversion
FROM campaign
WHERE campaign.status != 'REMOVED'
  AND segments.date DURING LAST_30_DAYS
ORDER BY segments.date DESC
```

> Use `segments.date` to get daily rows. Compute in Python: yesterday vs. trailing 7d average vs. trailing 30d average. One API call covers all three comparisons.

**Query 2 — Budget pacing and impression share:**

```sql
SELECT
  campaign.id,
  campaign.name,
  campaign.status,
  campaign_budget.amount_micros,
  metrics.cost_micros,
  metrics.search_impression_share,
  metrics.search_budget_lost_impression_share,
  metrics.search_rank_lost_impression_share
FROM campaign
WHERE campaign.status != 'REMOVED'
  AND segments.date DURING YESTERDAY
```

> **Limitation:** Impression share metrics are non-aggregable — they cannot be combined with `segments.date` for daily time series. Separate query required.

**Query 3 — Disapproved ads:**

```sql
SELECT
  campaign.id,
  campaign.name,
  ad_group.id,
  ad_group.name,
  ad_group_ad.ad.id,
  ad_group_ad.ad.type,
  ad_group_ad.policy_summary.approval_status,
  ad_group_ad.policy_summary.policy_topic_entries
FROM ad_group_ad
WHERE ad_group_ad.policy_summary.approval_status IN ('DISAPPROVED', 'AREA_OF_INTEREST_ONLY')
  AND ad_group_ad.status != 'REMOVED'
```

**Query 4 — High-spend zero-conversion keywords (yesterday):**

```sql
SELECT
  campaign.name,
  ad_group.name,
  ad_group_criterion.keyword.text,
  ad_group_criterion.keyword.match_type,
  metrics.clicks,
  metrics.cost_micros,
  metrics.conversions
FROM keyword_view
WHERE segments.date DURING YESTERDAY
  AND ad_group_criterion.status != 'REMOVED'
  AND metrics.cost_micros > 0
  AND metrics.conversions = 0
ORDER BY metrics.cost_micros DESC
```

**Query 5 — Recent account changes (last 24 hours):**

```sql
SELECT
  change_event.change_date_time,
  change_event.change_resource_name,
  change_event.user_email,
  change_event.change_resource_type,
  change_event.resource_change_operation,
  change_event.changed_fields
FROM change_event
WHERE change_event.change_date_time >= 'YESTERDAY_DATE'
  AND change_event.change_date_time <= 'TODAY_DATE'
ORDER BY change_event.change_date_time DESC
LIMIT 10000
```

> **Limitation:** `change_event` requires a LIMIT clause (max 10,000). Date range must be within last 30 days. Changes can take up to 3 minutes to appear.

### Analysis

Process the collected data into a prioritized briefing:

**Anomaly detection approach:**
1. For each campaign, compare yesterday's metrics to trailing 7d average
2. Calculate the **dollar impact** of each deviation: `|yesterday_cost - avg_7d_cost|` or `|yesterday_CPA - avg_7d_CPA| * yesterday_conversions`
3. Rank anomalies by dollar impact, not percentage deviation
4. Threshold: only surface deviations where the dollar impact exceeds $10 (configurable) or percentage exceeds 20%

**Budget pacing calculation:**
1. Day of month / total days in month = expected spend fraction
2. Month-to-date spend / monthly budget = actual spend fraction
3. Projected month-end spend = (actual_fraction / expected_fraction) * monthly_budget
4. Flag campaigns projected to underspend by >15% or overspend by >10%

### Output Format

Deliver as a structured narrative:

```
## Morning Brief — [Date]
### Account: [Account Name] ([Customer ID])

**Overall:** [1-sentence summary — "3 items need attention, 2 urgent"]

### Urgent
1. [Campaign X] CPA spiked 45% yesterday ($X → $Y). Dollar impact: $Z/day.
   Likely cause: [hypothesis based on data]. Recommended action: [specific step].

### Watch
2. [Campaign Y] is pacing to overspend by $X this month (projected $A vs budget $B).
3. 2 ads disapproved in [Campaign Z] — policy: [violation type].

### Healthy
- 12 campaigns performing within normal ranges
- No budget-limited campaigns with significant opportunity
- No unauthorized account changes detected
```

### Integration with ad-platform-connection

```python
from scripts.google.auth import get_auth
from scripts.google.report import pull_report, quick_campaign_summary

client, config = get_auth()
customer_id = config["customer_id"]

# Query 1: Daily campaign data
daily_df = pull_report(client, customer_id, QUERY_1)

# Query 2: Budget/IS (separate due to non-aggregable metrics)
budget_df = pull_report(client, customer_id, QUERY_2)

# Query 3: Disapproved ads
disapproved_df = pull_report(client, customer_id, QUERY_3)

# Query 4: Yesterday's wasted spend
waste_df = pull_report(client, customer_id, QUERY_4)

# Query 5: Recent changes
changes_df = pull_report(client, customer_id, QUERY_5)
```

## Known Limitations

- **Impression share is non-aggregable:** Cannot get a daily time series of IS in one query. Query 2 runs separately with a YESTERDAY date range.
- **Change event delay:** Up to 3-minute lag. Morning brief should note "changes as of [timestamp]."
- **No cross-platform:** This skill covers Google Ads only. Bing morning brief would use `scripts/bing/report.py` separately. A combined brief across platforms is a future enhancement.
- **Conversion lag:** Conversions attributed to yesterday may continue to trickle in for days (depending on conversion window). Note this in output when conversion-based metrics look unusually low.

## Reference Files

### `references/gaql-queries.md`
All 5 queries above with field references, known gotchas (zero-row omission, non-aggregable metrics), and date range handling patterns.

---

# Skill 3: Waste Detector

## Purpose

Comprehensive scan for the eight most common money leaks in a Google Ads account. Produce a dollar-quantified report with specific fixes for each leak — not a score or a checklist, but a dollar figure and an action plan.

This is the "holy shit" moment. Every account has waste. Most account managers know this but can't check everything systematically. Existing audit tools (TrueClicks at $99-249/mo, Optmyzr at $250+/mo) show checklists of issues. This skill tells you how much each issue costs and generates the fix.

## Trigger Patterns

```yaml
name: waste-detector
description: >-
  This skill should be used when the user asks to "find waste", "audit my
  account", "where am I wasting money", "account audit", "find wasted
  spend", "check for waste", "money leaks", "account health", "what's
  costing me money", "optimization opportunities", or mentions account
  optimization, spend analysis, waste analysis, or budget efficiency. Also
  trigger when the user expresses concern about overspending or
  underperformance.
```

## How It Works

### The Eight Waste Types

Each waste type has a verified GAQL query, a detection method, and a remediation path.

#### Waste Type 1: Non-Converting Keywords

Keywords with significant spend and zero conversions.

```sql
SELECT
  campaign.id,
  campaign.name,
  ad_group.id,
  ad_group.name,
  ad_group_criterion.criterion_id,
  ad_group_criterion.keyword.text,
  ad_group_criterion.keyword.match_type,
  metrics.impressions,
  metrics.clicks,
  metrics.cost_micros,
  metrics.conversions,
  metrics.average_cpc
FROM keyword_view
WHERE segments.date DURING LAST_30_DAYS
  AND ad_group_criterion.status != 'REMOVED'
  AND metrics.cost_micros > 0
  AND metrics.conversions = 0
ORDER BY metrics.cost_micros DESC
```

**Detection:** Filter in Python for `cost > threshold` (default: $50, configurable).
**Remediation:** Pause keywords or reduce bids. Generate `pause_entities()` dry-run for top offenders.
**Dollar calculation:** Direct sum of `metrics.cost` on qualifying keywords.

#### Waste Type 2: Low Quality Score Keywords Still Spending

```sql
SELECT
  campaign.name,
  ad_group.name,
  ad_group_criterion.criterion_id,
  ad_group_criterion.keyword.text,
  ad_group_criterion.keyword.match_type,
  ad_group_criterion.quality_info.quality_score,
  ad_group_criterion.quality_info.creative_quality_score,
  ad_group_criterion.quality_info.post_click_quality_score,
  ad_group_criterion.quality_info.search_predicted_ctr,
  metrics.impressions,
  metrics.clicks,
  metrics.cost_micros,
  metrics.conversions,
  metrics.average_cpc
FROM keyword_view
WHERE ad_group_criterion.status != 'REMOVED'
  AND segments.date DURING LAST_30_DAYS
ORDER BY ad_group_criterion.quality_info.quality_score ASC
```

**Detection:** Filter for `quality_score < 4` AND `cost > threshold`.
**Remediation:** For each low-QS keyword, diagnose the component scores (`creative_quality_score`, `post_click_quality_score`, `search_predicted_ctr`). Recommend specific fix: improve ad relevance, improve landing page, or improve CTR.
**Dollar calculation:** Estimate CPC premium. Industry average CPC at QS 10 = X. Current CPC at QS 4 = ~2.5X. Excess cost = `(current_cpc - estimated_fair_cpc) * clicks`.

> QS component values are enums: `BELOW_AVERAGE`, `AVERAGE`, `ABOVE_AVERAGE`. Quality score is 1-10, null means insufficient data.

#### Waste Type 3: Display Network on Search Campaigns

```sql
SELECT
  campaign.id,
  campaign.name,
  campaign.status,
  campaign.advertising_channel_type,
  campaign.network_settings.target_google_search,
  campaign.network_settings.target_search_network,
  campaign.network_settings.target_content_network,
  campaign.network_settings.target_partner_search_network,
  metrics.cost_micros,
  metrics.conversions
FROM campaign
WHERE campaign.status != 'REMOVED'
  AND campaign.advertising_channel_type = 'SEARCH'
  AND campaign.network_settings.target_content_network = TRUE
  AND segments.date DURING LAST_30_DAYS
```

**Detection:** Any results = Search campaigns with Display expansion on.
**Remediation:** Disable content network targeting. Generate mutation to set `target_content_network = FALSE`.
**Dollar calculation:** Estimate wasted Display spend. Pull Display-specific cost with `segments.ad_network_type = 'CONTENT'` on those campaigns.

#### Waste Type 4: Campaigns Limited by Budget (Impression Share Lost)

```sql
SELECT
  campaign.id,
  campaign.name,
  campaign.status,
  campaign_budget.amount_micros,
  metrics.cost_micros,
  metrics.impressions,
  metrics.conversions,
  metrics.search_impression_share,
  metrics.search_budget_lost_impression_share
FROM campaign
WHERE campaign.status != 'REMOVED'
  AND segments.date DURING LAST_30_DAYS
```

**Detection:** `search_budget_lost_impression_share > 0.20` (20%+ lost to budget).
**Remediation:** Two paths — if the campaign is profitable (CPA below target), recommend budget increase. If CPA is above target, recommend bid reduction instead of budget increase.
**Dollar calculation:** `potential_additional_conversions = current_conversions * (budget_lost_IS / current_IS)`. Value = additional conversions at current conversion value.

> **Limitation:** Impression share is non-aggregable. This query returns one value for the full date range, not a daily breakdown.

#### Waste Type 5: Broad Match Without Negative Keyword Coverage

Two queries required (GAQL cannot cross-resource JOIN):

**Query A — Broad match keywords:**

```sql
SELECT
  campaign.id,
  campaign.name,
  ad_group.name,
  ad_group_criterion.keyword.text,
  ad_group_criterion.keyword.match_type,
  metrics.cost_micros,
  metrics.conversions
FROM keyword_view
WHERE ad_group_criterion.keyword.match_type = 'BROAD'
  AND ad_group_criterion.status != 'REMOVED'
  AND segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC
```

**Query B — Shared negative keyword list coverage:**

```sql
SELECT
  campaign.id,
  campaign.name,
  shared_set.id,
  shared_set.name,
  shared_set.type
FROM campaign_shared_set
WHERE shared_set.type = 'NEGATIVE_KEYWORDS'
```

**Detection:** Join in Python — find broad match keywords in campaigns that have no shared negative keyword list attached.
**Remediation:** Flag as high-risk. Recommend creating a negative keyword list or switching to phrase match.
**Dollar calculation:** Report total spend on unprotected broad match keywords as "at-risk spend."

#### Waste Type 6: Single-Ad Ad Groups

```sql
SELECT
  campaign.id,
  campaign.name,
  ad_group.id,
  ad_group.name,
  ad_group_ad.ad.id,
  ad_group_ad.ad.type,
  ad_group_ad.status
FROM ad_group_ad
WHERE ad_group_ad.status IN ('ENABLED', 'PAUSED')
  AND campaign.status != 'REMOVED'
```

**Detection:** Group by ad group in Python. Flag ad groups with only 1 enabled ad.

> GAQL has no `COUNT()` or `GROUP BY`. Aggregation must happen in Python:
> ```python
> counts = df.groupby(['ad_group.id']).size().reset_index(name='ad_count')
> single_ad = counts[counts['ad_count'] == 1]
> ```

**Remediation:** Cannot quantify dollar impact directly. Flag as optimization opportunity — "These ad groups have no A/B testing. Expected improvement from ad testing: 5-15% CTR lift."
**Dollar calculation:** Estimated potential savings = `current_spend * 0.10` (conservative 10% improvement assumption).

#### Waste Type 7: Zero-Impression Enabled Campaigns

```sql
SELECT
  campaign.id,
  campaign.name,
  campaign.status,
  campaign.advertising_channel_type,
  campaign_budget.amount_micros,
  metrics.impressions
FROM campaign
WHERE campaign.status = 'ENABLED'
  AND segments.date DURING LAST_7_DAYS
```

**Detection:** Filter in Python for `impressions == 0` or campaigns absent from results entirely (GAQL may omit zero-value rows).
**Remediation:** Diagnose why — is it a targeting issue, budget issue, or policy issue? Flag for user review.
**Dollar calculation:** No direct waste, but represents wasted setup time and unused budget allocation.

#### Waste Type 8: Search Terms with Semantic Mismatch

Uses the same search term data from the search-term-verdict skill. The waste detector focuses specifically on terms with spend > $0 and zero conversions:

```sql
SELECT
  search_term_view.search_term,
  campaign.name,
  ad_group.name,
  metrics.clicks,
  metrics.cost_micros,
  metrics.conversions
FROM search_term_view
WHERE segments.date DURING LAST_30_DAYS
  AND metrics.cost_micros > 0
  AND metrics.conversions = 0
ORDER BY metrics.cost_micros DESC
```

**Detection:** LLM reads each high-cost zero-conversion search term and assesses semantic relevance to the campaign.
**Remediation:** Generate negative keyword list (same as search-term-verdict Phase 4).
**Dollar calculation:** Direct sum of spend on irrelevant terms.

### Output Format

```
## Waste Report — [Date]
### Account: [Account Name] ([Customer ID])

**Total Estimated Recoverable Waste: $X,XXX/month**

| # | Waste Type | Monthly Cost | Severity | Action |
|---|-----------|-------------|----------|--------|
| 1 | Non-converting keywords (12 keywords) | $2,340 | HIGH | Pause keywords |
| 2 | Search term bleed (47 irrelevant terms) | $1,890 | HIGH | Add negatives |
| 3 | Display Network on Search (2 campaigns) | $780 | MEDIUM | Disable content network |
| 4 | Low QS keywords (8 keywords, avg QS 3.2) | $560 | MEDIUM | Improve ad relevance |
| 5 | Budget-limited profitable campaigns (3) | -$1,200 potential | OPPORTUNITY | Increase budgets |
| 6 | Broad match without negatives (15 keywords) | $3,400 at risk | WARNING | Add negative lists |
| 7 | Single-ad ad groups (9 ad groups) | ~$890 potential | LOW | Add ad variants |
| 8 | Zero-impression campaigns (2) | $0 (setup waste) | INFO | Investigate |

### Detailed Findings
[Expand each waste type with specific entities, reasons, and ready-to-apply mutations]
```

### Integration with ad-platform-connection

```python
from scripts.google.auth import get_auth
from scripts.google.report import pull_report, quick_wasted_spend, quick_keyword_performance

client, config = get_auth()
customer_id = config["customer_id"]

# Run all 8 waste detection queries
# Queries 1, 2, 5A, 6, 7, 8 can reuse existing helpers
waste_df = quick_wasted_spend(client, customer_id)
keyword_df = quick_keyword_performance(client, customer_id)

# Custom queries for QS, network settings, IS, shared sets
qs_df = pull_report(client, customer_id, QUERY_QS)
network_df = pull_report(client, customer_id, QUERY_NETWORK)
is_df = pull_report(client, customer_id, QUERY_IS)
shared_df = pull_report(client, customer_id, QUERY_SHARED_SETS)
ads_df = pull_report(client, customer_id, QUERY_ADS)
campaigns_df = pull_report(client, customer_id, QUERY_ZERO_IMPRESSIONS)
```

## Known Limitations

- **GAQL has no GROUP BY/COUNT:** Ad counting per ad group requires Python post-processing.
- **Impression share is campaign-level only:** Cannot drill down to keyword-level IS.
- **QS can be null:** Keywords with insufficient data return null quality scores. Filter these out.
- **Cross-resource joins impossible in GAQL:** Broad match + negative list coverage requires two queries joined in Python.
- **Dollar calculations are estimates:** QS-based CPC premium uses industry heuristics, not exact pricing.

## Reference Files

### `references/gaql-queries.md`
All 8+ queries above with field references and Python post-processing patterns.

### `references/benchmarks.md`
Industry benchmarks for contextualizing waste findings:
- Average QS by industry vertical
- Average CPA by industry vertical
- Expected CTR ranges by match type
- QS-to-CPC multiplier table (QS 1 = ~400% of QS 10 CPC)

---

# Skill 4: PMax Decoder

## Purpose

Extract actionable transparency from Performance Max campaigns — the fastest-growing and most opaque campaign type in Google Ads. Surface search terms, channel distribution, asset performance, brand traffic leakage, and placement data that Google intentionally obscures in the UI.

The PMax Non-Converting Search Terms script by Nils Rooijmans is the #1 most popular Google Ads script. Demand for PMax visibility is enormous. But scripts only surface data — they can't interpret it or generate fixes. This skill does both.

## Trigger Patterns

```yaml
name: pmax-decoder
description: >-
  This skill should be used when the user asks about "Performance Max",
  "PMax", "PMax search terms", "PMax insights", "what is PMax doing",
  "PMax transparency", "PMax placements", "PMax asset performance",
  "decode my PMax", "PMax brand traffic", "PMax cannibalization", or
  mentions Performance Max analysis, PMax audit, PMax search queries,
  asset group performance, or PMax negative keywords.
```

## How It Works

### Module 1: Search Term Extraction

PMax uses a different GAQL resource than standard Search campaigns.

**Step 1 — Get PMax campaign IDs:**

```sql
SELECT
  campaign.id,
  campaign.name,
  campaign.status,
  metrics.cost_micros,
  metrics.conversions
FROM campaign
WHERE campaign.advertising_channel_type = 'PERFORMANCE_MAX'
  AND campaign.status = 'ENABLED'
  AND segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC
```

**Step 2 — Get search term categories per campaign (requires single campaign filter):**

```sql
SELECT
  campaign_search_term_insight.campaign_id,
  campaign_search_term_insight.category_label,
  campaign_search_term_insight.id,
  metrics.clicks,
  metrics.impressions,
  metrics.conversions,
  metrics.conversions_value
FROM campaign_search_term_insight
WHERE segments.date DURING LAST_30_DAYS
  AND campaign_search_term_insight.campaign_id = 'CAMPAIGN_ID'
```

> **CRITICAL LIMITATION:** Must filter by a single `campaign_id`. Querying all PMax campaigns at once throws `REQUIRES_FILTER_BY_SINGLE_RESOURCE`. Loop through campaigns from Step 1.

**Step 3 — Get individual search terms within a category:**

```sql
SELECT
  segments.search_subcategory,
  segments.search_term,
  metrics.impressions,
  metrics.clicks,
  metrics.conversions,
  metrics.conversions_value
FROM campaign_search_term_insight
WHERE segments.date DURING LAST_30_DAYS
  AND campaign_search_term_insight.campaign_id = 'CAMPAIGN_ID'
  AND campaign_search_term_insight.id = 'CATEGORY_ID'
```

> **LIMITATION:** Large PMax campaigns can have thousands of categories. Implement a cost-ranked approach: process top categories by spend first, with a configurable depth limit (default: top 50 categories).

### Module 2: Channel Distribution (API v23+)

This data is available via the API but NOT in the Google Ads UI — a major differentiator.

```sql
SELECT
  campaign.name,
  asset_group.id,
  asset_group.name,
  segments.ad_network_type,
  metrics.impressions,
  metrics.clicks,
  metrics.cost_micros,
  metrics.conversions,
  metrics.conversions_value
FROM asset_group
WHERE campaign.advertising_channel_type = 'PERFORMANCE_MAX'
  AND segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC
```

> `segments.ad_network_type` returns: SEARCH, YOUTUBE_WATCH, CONTENT (Display), MIXED, SEARCH_PARTNERS. Channel-level data only available for dates after June 1, 2025.

**Analysis:** Calculate spend distribution across channels per asset group. Flag if >70% of spend goes to a single channel (e.g., "your PMax is essentially a Display campaign").

### Module 3: Asset Group Performance

```sql
SELECT
  asset_group.id,
  asset_group.name,
  asset_group.primary_status,
  asset_group.ad_strength,
  metrics.impressions,
  metrics.clicks,
  metrics.cost_micros,
  metrics.conversions,
  metrics.conversions_value
FROM asset_group
WHERE campaign.advertising_channel_type = 'PERFORMANCE_MAX'
  AND segments.date DURING LAST_30_DAYS
```

**Asset-level labels (limited but useful):**

```sql
SELECT
  asset_group_asset.asset,
  asset_group_asset.performance_label,
  asset_group_asset.status
FROM asset_group_asset
WHERE asset_group.id = 'ASSET_GROUP_ID'
  AND asset_group_asset.status != 'REMOVED'
```

> **LIMITATION:** No per-asset click/cost/conversion metrics. Google only provides relative labels: `BEST`, `GOOD`, `LOW`, `PENDING`. The skill should flag `LOW`-performing assets and recommend replacements.

### Module 4: Brand Traffic Detection

Identify whether PMax is cannibalizing brand search campaigns.

**Approach:** Pull PMax search terms (Module 1), then classify each against a user-provided brand term list.

```python
brand_terms = ["acme", "acme inc", "acme software"]  # User provides these
pmax_search_terms = [...]  # From Module 1

brand_traffic = [t for t in pmax_search_terms if any(b in t.lower() for b in brand_terms)]
brand_spend = sum(t.cost for t in brand_traffic)
brand_pct = brand_spend / total_pmax_spend
```

If brand traffic exceeds 30% of PMax spend, flag as cannibalization risk and recommend adding brand terms as PMax negative keywords.

**Adding PMax negative keywords (available since API v20, June 2025):**

```python
from scripts.google.mutate import add_negative_keywords

add_negative_keywords(
    client, customer_id,
    keywords=brand_terms,
    level="campaign",
    parent_id=pmax_campaign_id,
    dry_run=True,
)
```

> PMax supports up to 10,000 negative keywords per campaign (increased from 100 in March 2025). Negatives only apply to Search and Shopping inventory, not Display/YouTube/Discover.

### Module 5: Placement Analysis

```sql
SELECT
  performance_max_placement_view.display_name,
  performance_max_placement_view.placement,
  performance_max_placement_view.placement_type,
  performance_max_placement_view.target_url,
  metrics.impressions,
  campaign.id
FROM performance_max_placement_view
WHERE campaign.id = 'CAMPAIGN_ID'
  AND segments.date DURING LAST_30_DAYS
```

> **MAJOR LIMITATION:** Only `metrics.impressions` is available. No clicks, cost, or conversions on this view. The skill should note this limitation and focus on flagging low-quality placements by type (e.g., mobile app placements in a B2B context).

### Output Format

```
## PMax Decoder — [Date]
### Campaign: [Campaign Name] ([Campaign ID])

**Quick Stats (Last 30 Days)**
- Total spend: $X,XXX | Conversions: XX | CPA: $XX | ROAS: X.Xx

### Channel Distribution
| Channel | Spend | % of Total | Conversions | CPA |
|---------|-------|-----------|-------------|-----|
| Search | $X,XXX | 45% | XX | $XX |
| YouTube | $X,XXX | 25% | XX | $XX |
| Display | $X,XXX | 20% | XX | $XX |
| Other | $X,XXX | 10% | XX | $XX |

[Interpretation: "Your PMax is primarily a Search campaign (45% of spend). Consider whether a dedicated Search campaign would give you more control at similar CPA."]

### Brand Traffic Analysis
- Brand search terms: XX terms, $X,XXX spend (X% of total)
- [If >30%: "WARNING: PMax is cannibalizing your brand search. Recommended: add brand terms as PMax negatives."]
- Ready-to-apply negative keyword list: [generated]

### Search Term Insights (Top Categories)
| Category | Clicks | Conversions | Non-Converting Terms |
|----------|--------|-------------|---------------------|
| [category] | XX | XX | XX terms flagged |

### Asset Performance
| Asset Group | Status | Ad Strength | Spend | Conv | LOW Assets |
|-------------|--------|-------------|-------|------|------------|
| [group] | ELIGIBLE | GOOD | $X,XXX | XX | 2 headlines, 1 image |

### Placement Summary
- Top placement types: [website: XX%, YouTube: XX%, app: XX%]
- [If app placements >20%: "Consider adding mobile app category exclusions if B2B."]

### Recommended Actions
1. [Prioritized, specific action with ready-to-apply mutation]
2. [...]
```

## Known Limitations

- **Search term extraction is expensive.** Large PMax campaigns with thousands of search categories require many API calls. Implement a depth-limited approach.
- **Asset metrics are labels only.** No per-asset click/cost data. Can only say "this asset is LOW-performing" not "this asset costs $X with 0 conversions."
- **Placement data is impressions-only.** Cannot quantify placement-level waste in dollars.
- **Channel data requires API v23+.** Ensure the `google-ads` client library version supports it.
- **Brand detection requires user input.** The skill needs the user to provide brand terms for classification. Consider pulling from account-level brand settings as a starting point.
- **Privacy threshold applies.** Low-volume search terms are hidden. The skill should report the estimated coverage gap.

## Reference Files

### `references/gaql-queries.md`
All queries above with the two-step PMax search term extraction pattern, field references for `campaign_search_term_insight`, `asset_group`, `asset_group_asset`, `performance_max_placement_view`, and `asset_group_signal`. Include known limitations and the per-campaign filter requirement.

---

# Cross-Cutting Concerns

## Authentication Pattern

All skills share the same authentication flow via `ad-platform-connection`:

```python
from scripts.google.auth import get_auth, verify_connection

client, config = get_auth()
accounts = verify_connection(client)
customer_id = config["customer_id"]
```

If auth fails, the skill should direct the user to the `ad-platform-connection` skill for setup: "Run the ad-platform-connection setup to configure your Google Ads credentials first."

## Safety Protocol

All mutations follow the same pattern established by the existing `hooks/validate-mutations.py`:

1. All queries (reads) execute freely
2. All mutations default to `dry_run=True`
3. Dry-run results are shown to the user with a clear preview
4. Live mutations (`dry_run=False`) require explicit user confirmation
5. The `PreToolUse` hook intercepts any `mcp__google-ads__mutate` call with `dry_run=false` and flags it with a warning

Skills should never set `dry_run=False` without user approval in the conversation.

## Error Handling

Common GAQL errors and how skills should handle them:

| Error | Cause | Handling |
|-------|-------|----------|
| `REQUIRES_FILTER_BY_SINGLE_RESOURCE` | PMax insight queries without campaign filter | Loop through campaigns individually |
| `RESOURCE_EXHAUSTED` | Rate limit hit | Back off and retry, or reduce query scope |
| `QUERY_ERROR` | Invalid GAQL syntax or field combination | Log the query, show error to user |
| `AUTHENTICATION_ERROR` | Expired or invalid credentials | Direct user to re-run auth setup |
| Zero rows returned | No data matching filters, OR zero-value row omission | Distinguish between "no issues found" and "data may be incomplete" |

## Bing Support

The four new skills are designed primarily for Google Ads. Bing equivalents are possible using `scripts/bing/report.py` but with reduced capability:

- **Morning Brief:** Bing supports campaign performance reporting. Can provide a parallel brief.
- **Waste Detector:** Most waste types are detectable via Bing SDK reporting, but QS is not available via Bing API.
- **Search Term Verdict:** Bing search term reports are available via `ReportingServiceManager`.
- **PMax Decoder:** Not applicable — Bing does not have Performance Max.

Bing support should be a follow-up enhancement, not a blocker for the initial build.

## Context Size Management

Skills should be designed with context window efficiency in mind:

- **SKILL.md** stays under 5,000 words. It contains the workflow, trigger patterns, and output format.
- **Reference files** contain GAQL queries and detailed heuristics. Loaded only when the skill triggers.
- **DataFrames** from `pull_report()` can be large. Skills should summarize data (top N rows, aggregates) rather than dumping full DataFrames into conversation context.
- **Multi-account workflows** should process accounts sequentially, summarizing each before moving to the next.

## Metric Definitions Reference

For consistent interpretation across all skills:

| Metric | GAQL Field | Unit | Notes |
|--------|-----------|------|-------|
| Cost | `metrics.cost_micros` / 1M | Dollars | `pull_report()` auto-creates `metrics.cost` |
| CPA | `metrics.cost_per_conversion` | Dollars | Null if no conversions |
| ROAS | `metrics.conversions_value / metrics.cost` | Ratio | Compute in Python |
| CTR | `metrics.ctr` | Ratio (0-1) | Multiply by 100 for percentage |
| Quality Score | `ad_group_criterion.quality_info.quality_score` | 1-10 | Null = insufficient data |
| Impression Share | `metrics.search_impression_share` | Ratio (0-1) | Campaign-level only, non-aggregable |
| IS Lost to Budget | `metrics.search_budget_lost_impression_share` | Ratio (0-1) | Campaign-level only, non-aggregable |

---

# Implementation Notes

## What Already Exists

The `ad-platform-connection` skill provides:

**report.py** — 7 functions:
- `pull_report(client, customer_id, query)` — generic GAQL executor, auto-flattens protobuf, converts micros
- `quick_campaign_summary()` — campaign-level metrics
- `quick_adgroup_summary()` — ad group-level metrics
- `quick_keyword_performance()` — keyword metrics with historical QS
- `quick_search_terms()` — search term report (basic fields)
- `quick_shopping_summary()` — shopping performance
- `quick_wasted_spend()` — zero-conversion keywords + search terms

**mutate.py** — 6 functions:
- `execute_mutation(client, customer_id, operations, dry_run=True)` — generic mutator
- `create_campaign()` — atomic budget + campaign creation
- `pause_entities()` — pause by resource name
- `add_negative_keywords()` — campaign or ad group level negatives
- `create_rsa()` — responsive search ad creation
- `update_bids()` — CPC bid updates with 50% safety guardrail

These cover ~80% of the data access and mutation needs of the four new skills. The remaining ~20% requires custom GAQL queries via `pull_report()` for PMax-specific resources, quality score components, impression share, network settings, change events, and ad counting.

## What Needs to Be Built

For each new skill:
1. `SKILL.md` — Workflow instructions, trigger patterns, output format
2. `references/gaql-queries.md` — Verified queries with field references and limitations
3. Additional reference files as specified per skill

No new Python scripts are needed. All four skills use `pull_report()` with custom GAQL and the existing mutation helpers. The intelligence lives in the SKILL.md instructions that teach Claude how to interpret the data and generate prescriptions.

## Version Bump

Adding four skills warrants a minor version bump: `4.0.0` → `5.0.0`. Update:
- `.claude-plugin/plugin.json` — version, description, keywords
- `README.md` — skill inventory and usage examples
- Marketplace registry if publishing
