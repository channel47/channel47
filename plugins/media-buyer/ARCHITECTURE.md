# Media Buyer Plugin — Architecture v7

> From 5 skills on 2 platforms to 9 skills on 4 platforms, with parallel subagents and tiered safety hooks.

---

## Design Principles

1. **Dollar impact** — every skill exists because it measurably saves or makes money. No "nice to have" skills.
2. **Parallel by default** — subagents fan out data collection across platforms simultaneously. A morning brief across 3 platforms should not take 3x as long.
3. **Safety scales with risk** — pausing a keyword gets a different approval gate than doubling a campaign budget. Hook strictness is proportional to mutation dollar impact.
4. **Cross-platform first** — unified data model across all platforms. Skills operate on normalized data, not "Google + addendum for others."
5. **Expertise in references, logic in skills** — thresholds, formulas, and heuristics live in reference docs (change frequently, shared across skills). Skills define workflow and orchestration (change rarely).

---

## Layer Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                      9 SKILLS                                │
│          Expertise workflows that solve problems             │
├──────────────────────────────────────────────────────────────┤
│                     3 SUBAGENTS                              │
│         Parallel execution across platforms/campaigns        │
├──────────────────────────────────────────────────────────────┤
│                      3 HOOKS                                 │
│          Safety enforcement at mutation boundary             │
├──────────────────────────────────────────────────────────────┤
│                      4 MCPs                                  │
│       Platform API access (Google / Bing / Meta / GA4)       │
└──────────────────────────────────────────────────────────────┘
```

Skills orchestrate. Subagents parallelize. Hooks enforce. MCPs connect.

---

## MCPs (Platform Access)

### v6 → v7

| MCP | v6 | v7 | What changed |
|-----|----|----|--------------|
| `google-ads` | `^1.0.8` — query, mutate, list_accounts | `^2.0.0` — + batch_mutate | Batch mutations for bulk operations (50+ entities) |
| `bing-ads` | `^1.3.1` — query, report, list_accounts (read-only) | `^2.0.0` — + **mutate** | Mutation support closes biggest v6 gap |
| `meta-ads` | — | `^1.0.0` — query, mutate, insights, list_accounts | **New.** Facebook + Instagram Ads API |
| `ga4` | — | `^1.0.0` — query, list_properties | **New.** Conversion paths, attribution, landing pages |

### Why Meta Ads?

70%+ of media buyers manage Meta alongside Search. Budget allocation decisions require budget data from all platforms. Meta's waste patterns (audience overlap, creative fatigue, frequency) are distinct from Search and need dedicated detection.

### Why GA4?

Ads platforms report conversions but not *conversion context*. GA4 reveals:
- Conversion paths (did the user see a Meta ad, then click a Google ad?)
- Assisted conversions (Google brand campaign getting credit for Meta's work?)
- Landing page performance (bounce rate, engagement by traffic source)
- Real-time conversion data (resolves the "is this a real drop or backfill lag?" problem)

This makes every analytical skill smarter — morning-brief, waste-detector, bid-strategist, and budget-allocator all benefit.

### Environment Variables

```bash
# Google Ads (5)
GOOGLE_ADS_DEVELOPER_TOKEN
GOOGLE_ADS_CLIENT_ID
GOOGLE_ADS_CLIENT_SECRET
GOOGLE_ADS_REFRESH_TOKEN
GOOGLE_ADS_LOGIN_CUSTOMER_ID        # MCC accounts

# Bing Ads (5)
BING_ADS_DEVELOPER_TOKEN
BING_ADS_CLIENT_ID
BING_ADS_REFRESH_TOKEN
BING_ADS_CUSTOMER_ID                # Manager accounts
BING_ADS_ACCOUNT_ID                 # Default account

# Meta Ads (2)
META_ADS_ACCESS_TOKEN
META_ADS_ACCOUNT_ID

# GA4 (1 — shares Google OAuth)
GA4_PROPERTY_ID
```

Configure any subset. Skills detect available platforms at runtime and adapt. A Google-only shop gets full value from day one; adding Bing/Meta/GA4 later unlocks cross-platform features progressively.

---

## Skills (Expertise)

### Skill Map

| # | Skill | Tier | Platform coverage | Mutations? | Primary value |
|---|-------|------|-------------------|------------|---------------|
| 1 | platform-setup | Foundation | All 4 | No | Unblocks everything else |
| 2 | morning-brief | Daily ops | Google + Bing + Meta + GA4 | No | Catch problems before they cost money |
| 3 | waste-detector | Daily ops | Google + Bing + Meta + GA4 | Google + Bing | Stop bleeding spend |
| 4 | search-term-verdict | Daily ops | Google + Bing | Google + Bing | Sculpt traffic, block waste queries |
| 5 | campaign-launcher | Campaign mgmt | Google + Bing + Meta | Google + Bing + Meta | Compress 4-8 hours of setup to a conversation |
| 6 | creative-analyst | Campaign mgmt | Google + Bing + Meta | No (recommendations) | 10-30% CTR improvement from systematic testing |
| 7 | bid-strategist | Campaign mgmt | Google + Bing + GA4 | Google + Bing | Fix silently misconfigured bid strategies |
| 8 | pmax-decoder | Strategic | Google + GA4 | Google (brand negatives) | Transparency into Google's black box |
| 9 | budget-allocator | Strategic | Google + Bing + Meta + GA4 | Google + Bing + Meta | Shift budget from diminishing returns to headroom |

---

### Tier 0 — Foundation

#### 1. platform-setup

Configure credentials and verify API access for all connected platforms.

**Δ from v6**: Add Meta Ads + GA4 setup flows. Move Shopping campaign setup to campaign-launcher where it belongs.

| Aspect | Detail |
|--------|--------|
| Tools | `list_accounts` / `list_properties` on all 4 MCPs |
| References | `google-setup.md`, `bing-setup.md`, `meta-setup.md`, `ga4-setup.md`, `config-patterns.md` |
| Output | Platform connection matrix — connected/disconnected per MCP, account IDs, access level |

Guardrails: Never display secrets. Recommend `.claude/settings.local.json` (gitignored, project-scoped) for credentials. Report exact missing variable on failure.

---

### Tier 1 — Daily Operations

#### 2. morning-brief

Cross-platform daily health narrative with anomaly detection and budget pacing.

**Δ from v6**: Meta Ads data. GA4 conversion context. Parallel collection via subagents. Resolves the conversion-lag false-positive problem.

| Aspect | Detail |
|--------|--------|
| Subagents | Spawn `platform-scout` per connected platform (parallel) |
| Tools | Google: query (5 GAQL). Bing: report (3). Meta: insights (campaign + adset). GA4: query (conversion summary) |
| Detection | Same anomaly formulas (7d + 30d baselines, 20% + $10 gate). GA4 adds conversion-path anomalies |
| References | Platform query docs (per-skill), `anomaly-formulas.md` (shared) |
| Output | Urgent / Watch / Healthy narrative. Platform-labeled. Conversion-path context from GA4 |

**Key enhancement**: GA4 real-time conversion data cross-referenced against ads platform data resolves the "conversion lag" false alarm — the most common morning-brief noise source in v6.

**Subagent flow**:
```
morning-brief
  ├─ spawn platform-scout(google, morning_queries)  ─┐
  ├─ spawn platform-scout(bing, morning_queries)     ├─ parallel
  ├─ spawn platform-scout(meta, morning_queries)     │
  └─ spawn platform-scout(ga4, conversion_summary)   ┘
                                                      │
                                                  merge & analyze
                                                      │
                                                  output narrative
```

---

#### 3. waste-detector

Detect and quantify spend leaks across all platforms. Dollar-ranked remediation with automated fixes.

**Δ from v6**: Meta waste types. Bing mutations (now supported). GA4 bounce-rate signal. Cross-platform waste aggregation.

| Aspect | Detail |
|--------|--------|
| Subagents | `platform-scout` per platform. `campaign-deep-dive` for accounts with 50+ campaigns |
| Tools | All 4 MCPs: query + mutate (Google, Bing, Meta). GA4 for landing page bounce rates |
| References | `thresholds.md` (expanded), `benchmarks.md` (shared), `meta-waste-types.md` |
| Output | Dollar-ranked waste table (cross-platform), severity tags, auto-remediation (Google + Bing) + manual recs (Meta) |

**12 Waste Types** (8 existing + 4 new):

| # | Waste type | Platforms | Detection | Dollar formula |
|---|-----------|-----------|-----------|----------------|
| 1 | Non-converting keywords | Google, Bing | Spend ≥ avg campaign CPA, 0 conversions | Direct: total spend on keyword |
| 2 | Low Quality Score keywords | Google, Bing | QS ≤ 5, $10+ spend | cost × (1 − 1/cpc_multiplier) |
| 3 | Display expansion on Search | Google | Network setting includes Display | Full campaign spend at risk |
| 4 | Budget-limited campaigns | Google, Bing | search_budget_lost_IS > 10% | Missed conversions × CPA |
| 5 | Broad match without negatives | Google, Bing | Broad keywords, no shared negative list | Exposure flag (qualitative) |
| 6 | Single-ad ad groups | Google, Bing | Ad groups with <2 active ads | 10% CTR uplift model on ad group spend |
| 7 | Zero-impression campaigns | Google, Bing | Enabled, 0 impressions 30d | INFO severity |
| 8 | Non-converting search terms | Google, Bing | Semantic mismatch + spend | Direct: spend on mismatched terms |
| 9 | **Audience overlap** | Meta | Ad sets targeting >30% overlapping audiences | Bid inflation estimate from overlap % |
| 10 | **Frequency cap violations** | Meta | Frequency > 8 in 7d window | Incremental cost above optimal frequency |
| 11 | **Placement waste** | Meta | Audience Network / Messenger with 0 conversions | Direct: spend on those placements |
| 12 | **Creative fatigue** | Meta | CTR declined >30% from 14d peak | Excess spend from degraded CTR |

Severity: **HIGH** (>$500/mo), **MEDIUM** ($100–500), **LOW** ($25–100), **INFO** (<$25).

---

#### 4. search-term-verdict

Classify paid-search queries into NEGATE / PROMOTE / INVESTIGATE / KEEP. Ready-to-apply negative packages.

**Δ from v6**: Bing mutations (now supported). Enhanced cross-platform signal.

| Aspect | Detail |
|--------|--------|
| Subagents | `platform-scout` per platform for data collection |
| Tools | Google: query + mutate. Bing: report + query + **mutate** (new). |
| Classification | Same verdict heuristics applied identically. Cross-platform dedup: same term on 2+ platforms = higher-confidence signal |
| Mutations | Google: dry_run gate. Bing: dry_run gate (new). |
| References | `verdict-heuristics.md`, platform query docs |
| Output | Per-platform verdict tables, cross-platform patterns, negative packages, promotion candidates |

**Note on Meta**: Meta doesn't expose search terms the way Search platforms do. Dynamic Ads have limited query data, but this skill is fundamentally a Search skill. Meta audience optimization is handled by waste-detector (audience overlap) and creative-analyst instead.

---

### Tier 2 — Campaign Management (New)

#### 5. campaign-launcher

Build complete campaign structures from a strategy brief — keywords, ad groups, ads, targeting, budgets.

**Why it matters**: Campaign setup is 4–8 hours of manual work per platform. This skill compresses it to a conversation. It's also where mistakes compound — a bad structure silently wastes budget for months.

| Aspect | Detail |
|--------|--------|
| Tools | Google: query + mutate. Bing: query + mutate. Meta: query + mutate |
| Workflow | Detailed below |
| References | `campaign-structures.md`, `keyword-research-patterns.md`, `rsa-best-practices.md`, `meta-campaign-types.md`, `shopping-campaigns.md`, `budget-recommendations.md` |
| Output | Complete campaign tree (visual), all mutations previewed, launch confirmation |

**Workflow**:

```
1. INTAKE
   Goals (leads, sales, awareness), budget, target audience, landing pages.
   Determine platform(s) and campaign type(s).

2. RESEARCH
   Search: keyword themes, volume estimates, competitive density.
   Meta: audience sizing, interest/behavior targeting options.
   Shopping: product feed validation, category mapping.

3. STRUCTURE
   Campaign → ad groups/ad sets → keywords/targeting.
   Apply SKAG, STAG, or themed grouping based on volume.
   Set match types, negative keyword seed lists, bid strategy.

4. CREATIVES
   Google/Bing: RSA headlines (15) + descriptions (4) per ad group.
   Meta: ad copy + creative specs (image/video dimensions, text limits).
   Shopping: feed optimization recommendations.

5. PREVIEW
   Dry-run ALL mutations. Display complete campaign tree.
   Show: budget allocation, estimated reach, structure summary.

6. LAUNCH
   Execute after explicit approval. Verify post-launch status.
   Schedule 24h check-in via morning-brief.
```

---

#### 6. creative-analyst

Analyze ad copy and asset performance. Identify testing gaps. Recommend improvements.

**Why it matters**: Systematic ad testing delivers 10–30% CTR improvement. Most accounts have testing gaps (single-ad ad groups, unpinned RSAs, stale copy). This is the highest-leverage ongoing optimization after waste detection.

| Aspect | Detail |
|--------|--------|
| Tools | Google: query (RSA asset performance, ad strength). Bing: query (ad performance). Meta: query (ad creative insights, creative breakdown) |
| Workflow | Detailed below |
| References | `rsa-analysis-patterns.md`, `creative-fatigue-formulas.md`, `meta-creative-analysis.md`, `copy-testing-frameworks.md` |
| Output | Per-campaign creative health score, testing gap list, fatigue alerts, specific copy recommendations |

**Workflow**:

```
1. ASSET INVENTORY
   Google: Pull RSA asset performance labels (BEST/GOOD/LOW/PENDING).
           Pull headline/description pinning. Pull ad strength score.
   Bing:   Pull ad-level CTR, conversion data per ad group.
   Meta:   Pull creative-level performance (image/video/carousel).
           Pull creative breakdown by placement.

2. TESTING GAP DETECTION
   Flag ad groups with <3 active RSAs (Google/Bing).
   Flag ad sets with <3 active creatives (Meta).
   Flag RSAs with all-PENDING labels (insufficient data, likely low impression share).

3. FATIGUE DETECTION
   Per ad/creative: compare current 7d CTR vs 14d peak CTR.
   Flag when decline >25% AND impressions >5,000 (statistical significance gate).
   Meta: also check frequency (fatigue accelerates above frequency 6).

4. DIVERSITY SCORING
   Headline semantic similarity across RSA variants.
   Flag when >70% of headlines use same core phrase (low diversity = low testing value).
   Meta: flag when all creatives use same format (all static images, no video).

5. RECOMMENDATIONS
   Specific copy variants to test (informed by top-performing assets + gaps).
   Asset replacement priorities (LOW-label assets on Google, low-CTR creatives on Meta).
   Format diversification suggestions.
```

---

#### 7. bid-strategist

Audit bid strategies, detect misconfigurations, recommend optimal strategy per campaign.

**Why it matters**: Wrong bid strategy silently wastes 15–40% of budget. Most accounts have at least one misconfigured strategy — a tCPA set 30% below actual CPA, a manual-CPC campaign with enough conversion data for automation, or a portfolio strategy grouping campaigns with conflicting goals.

| Aspect | Detail |
|--------|--------|
| Tools | Google: query (bid strategy, auction insights, conversion data). Bing: query (bid strategy). GA4: query (conversion lag analysis) |
| Workflow | Detailed below |
| References | `bid-strategy-prerequisites.md`, `strategy-selection-matrix.md`, `auction-analysis-patterns.md`, `conversion-lag-impact.md` |
| Output | Strategy audit table, misconfiguration flags, recommended changes with projected impact |

**Key heuristics**:

| Misconfiguration | Detection | Impact |
|-----------------|-----------|--------|
| tCPA below actual CPA by >20% | `target_cpa < actual_cpa * 0.8` | Over-constrained: limits volume, increases effective CPA |
| Manual CPC + high conversion volume | `bidding_strategy_type = MANUAL_CPC` AND conversions > 30/30d | Leaving money on table — enough data for automated |
| Maximize Conversions without target | `bidding_strategy_type = MAXIMIZE_CONVERSIONS` AND no target | Uncapped spend — algorithm optimizes volume at any CPA |
| Portfolio strategy across mismatched campaigns | Portfolio members with >50% CPA variance | Conflicting goals — recommend splitting |
| tROAS with insufficient value data | `bidding_strategy_type = TARGET_ROAS` AND conversion value = $0 on >20% of conversions | Strategy is blind — missing value data |
| Learning phase thrashing (Meta) | >3 significant edits in 7d on an ad set | Repeated learning resets — consolidate edits |

**Workflow**:

```
1. INVENTORY
   List all bid strategies per campaign across platforms.
   Map portfolio strategies to member campaigns.

2. PREREQUISITE CHECK
   Conversion volume: minimum 30 conversions/30d for tCPA/tROAS.
   Conversion lag: GA4 data reveals true conversion delay.
   Value data completeness: check for missing/zero values.

3. MISCONFIGURATION DETECTION
   Apply heuristics table above.
   Cross-reference auction competitiveness (impression share, top-of-page rate).

4. STRATEGY RECOMMENDATIONS
   Per campaign: current strategy → recommended strategy → rationale → expected impact.
   Migration path for strategy changes (gradual transition, not hard switch).

5. OUTPUT
   Audit table with severity flags.
   Recommended changes with projected CPA/ROAS impact.
```

---

### Tier 3 — Strategic

#### 8. pmax-decoder

Performance Max transparency — search terms, channel distribution, asset performance, brand cannibalization.

**Δ from v6**: GA4 cross-reference for conversion path validation. Minimal structural changes — this skill is mature.

| Aspect | Detail |
|--------|--------|
| Tools | Google: query + mutate (brand negatives). GA4: query (PMax conversion paths) |
| Modules | 5 modules unchanged from v6 |
| References | `pmax-gaql-queries.md` |

**Enhancement**: GA4 conversion path data validates whether PMax is genuinely driving incremental conversions or claiming organic/brand traffic. This is the #1 question every advertiser has about PMax.

---

#### 9. budget-allocator

Recommend cross-campaign and cross-platform budget shifts based on marginal ROI.

**Why it matters**: Most accounts have 20–40% of budget allocated to campaigns past the point of diminishing returns, while other campaigns are budget-limited with strong efficiency. This skill identifies the misallocation and models the fix.

| Aspect | Detail |
|--------|--------|
| Subagents | `platform-scout` per platform (parallel data collection) |
| Tools | All MCPs: query (campaign performance + budget data). GA4: query (assisted conversions for attribution) |
| References | `marginal-roi-formulas.md`, `budget-pacing-patterns.md`, `cross-platform-attribution.md`, `diminishing-returns-model.md` |
| Output | Budget shift table (from → to), projected impact, cross-platform allocation view |

**Workflow**:

```
1. COLLECT
   30-day performance per campaign across all platforms (via parallel scouts).
   GA4 assisted conversion data for attribution context.

2. MARGINAL ROI ANALYSIS
   Per campaign: compute efficiency trend.
     marginal_CPA = cost_last_7d / conversions_last_7d
     baseline_CPA = cost_last_30d / conversions_last_30d
     Rising marginal CPA (>15% above baseline) = diminishing returns.

3. HEADROOM DETECTION
   Budget-limited campaigns: search_budget_lost_IS > 10% (Google/Bing).
   Meta: delivery status = "Learning Limited" with CPA below target.
   Cross-reference: strong CPA + limited delivery = high-priority for budget increase.

4. CROSS-PLATFORM ARBITRAGE
   Same audience, same conversion goal, different CPA across platforms.
   Example: branded search CPA $8 on Google, $5 on Bing → shift branded budget.

5. MODEL SCENARIOS
   For each recommended shift: model ±10% and ±25% budget changes.
   Show projected conversions and CPA at each level.
   Flag risk: campaigns near minimum viable budget.

6. OUTPUT
   Shift recommendation table.
   Before/after budget allocation pie chart (by platform and campaign).
   Projected total conversion impact.
```

**Key formulas**:

| Formula | Purpose |
|---------|---------|
| `marginal_CPA = cost_7d / conversions_7d` vs `baseline_CPA = cost_30d / conversions_30d` | Detect diminishing returns |
| `headroom = search_budget_lost_IS × current_conversions / (1 − search_budget_lost_IS)` | Estimate missed conversions from budget cap |
| `cross_platform_delta = CPA_platform_A − CPA_platform_B` (same audience) | Identify arbitrage opportunities |

---

## Subagents (Parallelism)

### Why Subagents?

v6 skills query platforms sequentially. A morning brief across Google + Bing + Meta takes 3 serial round trips. With subagents, all 3 run simultaneously — the brief completes in the time of the slowest platform, not the sum.

### Defined Subagents

#### 1. platform-scout

| Attribute | Detail |
|-----------|--------|
| Purpose | Query a single platform for a specified dataset. Return normalized results. |
| Spawned by | morning-brief, waste-detector, search-term-verdict, budget-allocator |
| Input | `(platform, query_set, date_range)` |
| Output | Normalized data in unified schema |
| Parallelism | 1 instance per connected platform, all run simultaneously |

**Normalization contract** — all scouts return data in a unified schema:

```json
{
  "platform": "google | bing | meta | ga4",
  "campaigns": [
    {
      "id": "...",
      "name": "...",
      "cost": 1234.56,
      "conversions": 45,
      "ctr": 0.0245,
      "impressions": 50000,
      "cpa": 27.43
    }
  ]
}
```

This is the key design decision: **scouts handle all platform-specific data mapping** (Google micros → dollars, Bing CTR string → decimal, Meta currency handling). Skills never touch raw platform data.

**Platform-specific mappings handled by scout**:

| Field | Google | Bing | Meta |
|-------|--------|------|------|
| Cost | `metrics.cost_micros / 1_000_000` | `Spend` (already dollars) | `spend` (already dollars) |
| CTR | `metrics.ctr` (decimal) | `Ctr` (parse "2.45%" → 0.0245) | `ctr` (decimal) |
| Conversions | `metrics.conversions` | `Conversions` | `actions` (filtered by type) |
| Quality Score | `metrics.quality_score` | `QualityScore` ("--" = null) | N/A |
| Impression Share | `metrics.search_impression_share` | N/A | N/A |

---

#### 2. campaign-deep-dive

| Attribute | Detail |
|-----------|--------|
| Purpose | Run comprehensive analysis on a single campaign (all waste types, search terms, creative health) |
| Spawned by | waste-detector (accounts with 50+ campaigns), creative-analyst (multi-campaign audits) |
| Input | `(platform, campaign_id, analysis_types[])` |
| Output | Campaign-level findings with severity and dollar impact |
| Parallelism | Up to 10 concurrent instances |

When waste-detector encounters an account with 80 campaigns, analyzing them sequentially takes too long. Instead, spawn 10 campaign-deep-dive agents that process 8 campaigns each, in parallel.

---

#### 3. synthesizer

| Attribute | Detail |
|-----------|--------|
| Purpose | Merge outputs from multiple platform-scouts into unified cross-platform view |
| Spawned by | morning-brief, budget-allocator |
| Input | N scout outputs (normalized JSON) |
| Output | Merged analysis with cross-platform totals, deduplication, unified anomaly detection |

**Why a separate subagent?** Cross-platform synthesis is non-trivial:
- **Conversion dedup**: Same conversion counted in Google Ads *and* GA4 — don't double-count.
- **Attribution reconciliation**: GA4 may credit a conversion to Meta that Google Ads also claims (last-click vs data-driven).
- **Unified anomaly detection**: Detect account-wide anomalies that aren't visible per-platform (total spend spike when each platform only moved 10%).

---

## Hooks (Safety)

### v6 → v7

| Hook | v6 | v7 |
|------|----|----|
| mutation-gate | Warns on live mutations (allows all) | **Blocks** Tier 2+ mutations until explicit confirmation |
| budget-ceiling | — | Hard cap on budget modifications per account |
| audit-logger | — | Logs all mutations to reviewable JSONL file |

---

### 1. mutation-gate (enhanced)

**Trigger**: `PreToolUse` on `*__mutate` and `*__batch_mutate`

v6 behavior: Warns but allows everything. User can accidentally approve a destructive change.

v7 behavior: **Tiered blocking.**

| Tier | Risk level | Examples | Gate |
|------|-----------|----------|------|
| **Tier 1** | Low | Pause/enable entities, add negatives | Silent pass (dry_run=true) or single approval (dry_run=false) |
| **Tier 2** | Medium | Budget changes <20%, bid target adjustments | Block until approval + display projected impact |
| **Tier 3** | High | Campaign creation, budget changes >20%, strategy changes, batch mutations | Block until approval + impact summary + 5-second delay |

**Implementation**:

```python
# mutation-gate.py
TIER_2_OPERATIONS = ["update_budget", "update_bid_target", "update_bid_modifier"]
TIER_3_OPERATIONS = ["create_campaign", "batch_mutate", "update_bidding_strategy"]

def classify_mutation(tool_input):
    if tool_input.get("dry_run", True):
        return "allow"  # dry-run always passes

    operation = extract_operation_type(tool_input)

    if operation in TIER_3_OPERATIONS:
        return "block", "HIGH-RISK MUTATION: Requires explicit approval. " + summarize_impact(tool_input)
    elif operation in TIER_2_OPERATIONS:
        return "block", "BUDGET/BID CHANGE: Review impact before proceeding. " + summarize_impact(tool_input)
    else:
        return "allow", "LIVE MUTATION: Changes will be permanent."
```

---

### 2. budget-ceiling

**Trigger**: `PreToolUse` on `*__mutate` where operation modifies budget

**Purpose**: Prevent accidental 10x budget increases from typos or misunderstandings.

**Configuration** (in plugin settings):

```json
{
  "budget_ceilings": {
    "google:123-456-7890": { "daily_max": 500, "monthly_max": 15000 },
    "bing:12345678": { "daily_max": 200, "monthly_max": 6000 },
    "meta:act_123456": { "daily_max": 1000, "monthly_max": 30000 }
  }
}
```

**Behavior**:
- If mutation would set any campaign budget above ceiling → **hard block** (`decision: "block"`).
- No override without changing the ceiling config first (deliberate friction).
- Unconfigured accounts: no ceiling enforced (opt-in, not opt-out).

---

### 3. audit-logger

**Trigger**: `PostToolUse` on all `*__mutate`, `*__batch_mutate`

**Purpose**: Every mutation gets logged. Enables post-session review and accountability.

**Log format** (`~/.claude/media-buyer-audit.jsonl`):

```json
{
  "timestamp": "2026-02-23T14:32:01Z",
  "tool": "mcp__google-ads__mutate",
  "dry_run": false,
  "operation": "pause_keyword",
  "entities_affected": 3,
  "account": "123-456-7890",
  "summary": "Paused 3 non-converting keywords in campaign 'Brand - Exact'",
  "result": "success"
}
```

**Retention**: 90 days, auto-rotation. Human-readable with `jq`.

---

## Shared Reference Strategy

### Problem in v6

References are per-skill. `gaql-queries.md` and `bing-queries.md` are duplicated across multiple skills. Updating a GAQL query means editing 3 files.

### v7 Solution: Two-Tier References

#### Plugin-level shared references (`references/shared/`)

| Doc | Used by | Content |
|-----|---------|---------|
| `data-mapping.md` | All skills (via scouts) | Google ↔ Bing ↔ Meta field mapping, unit conversions |
| `anomaly-formulas.md` | morning-brief, waste-detector | Deviation formulas, baseline windows, threshold gates |
| `benchmarks.md` | waste-detector, bid-strategist, creative-analyst | QS-to-CPC impact, CTR bands, conversion rate bands |
| `mutation-safety.md` | All mutating skills | Dry-run protocol, read-before-write, approval language templates |

#### Skill-level references (only for skill-specific expertise)

| Skill | Skill-specific references |
|-------|--------------------------|
| platform-setup | `google-setup.md`, `bing-setup.md`, `meta-setup.md`, `ga4-setup.md`, `config-patterns.md` |
| morning-brief | `gaql-morning.md`, `bing-morning.md`, `meta-morning.md`, `ga4-morning.md` |
| waste-detector | `thresholds.md`, `meta-waste-types.md` |
| search-term-verdict | `verdict-heuristics.md`, `negative-keyword-safety.md` |
| campaign-launcher | `campaign-structures.md`, `keyword-research-patterns.md`, `rsa-best-practices.md`, `meta-campaign-types.md`, `shopping-campaigns.md`, `budget-recommendations.md` |
| creative-analyst | `rsa-analysis-patterns.md`, `creative-fatigue-formulas.md`, `meta-creative-analysis.md`, `copy-testing-frameworks.md` |
| bid-strategist | `bid-strategy-prerequisites.md`, `strategy-selection-matrix.md`, `auction-analysis-patterns.md`, `conversion-lag-impact.md` |
| pmax-decoder | `pmax-gaql-queries.md` |
| budget-allocator | `marginal-roi-formulas.md`, `budget-pacing-patterns.md`, `cross-platform-attribution.md`, `diminishing-returns-model.md` |

**Result**: 4 shared docs replace ~8 duplicated docs. Update a formula once, all skills pick it up.

---

## Directory Structure

```
plugins/media-buyer/
├── .claude-plugin/
│   └── plugin.json
├── .mcp.json                              # 4 MCP servers
├── hooks/
│   ├── hooks.json                         # PreToolUse + PostToolUse config
│   ├── mutation-gate.py                   # Tiered mutation approval
│   ├── budget-ceiling.py                  # Hard budget caps
│   └── audit-logger.py                    # Mutation logging
├── subagents/
│   ├── platform-scout.md                  # Per-platform data collection
│   ├── campaign-deep-dive.md              # Per-campaign deep analysis
│   └── synthesizer.md                     # Cross-platform merge
├── references/
│   └── shared/
│       ├── data-mapping.md                # Cross-platform field mapping
│       ├── anomaly-formulas.md            # Deviation detection math
│       ├── benchmarks.md                  # Industry benchmarks
│       └── mutation-safety.md             # Dry-run protocol
├── skills/
│   ├── platform-setup/                    # [Foundation]
│   │   ├── SKILL.md
│   │   └── references/                    # 5 docs
│   ├── morning-brief/                     # [Daily Ops]
│   │   ├── SKILL.md
│   │   └── references/                    # 4 docs
│   ├── waste-detector/                    # [Daily Ops]
│   │   ├── SKILL.md
│   │   └── references/                    # 2 docs
│   ├── search-term-verdict/               # [Daily Ops]
│   │   ├── SKILL.md
│   │   └── references/                    # 2 docs
│   ├── campaign-launcher/                 # [Campaign Mgmt] NEW
│   │   ├── SKILL.md
│   │   └── references/                    # 6 docs
│   ├── creative-analyst/                  # [Campaign Mgmt] NEW
│   │   ├── SKILL.md
│   │   └── references/                    # 4 docs
│   ├── bid-strategist/                    # [Campaign Mgmt] NEW
│   │   ├── SKILL.md
│   │   └── references/                    # 4 docs
│   ├── pmax-decoder/                      # [Strategic]
│   │   ├── SKILL.md
│   │   └── references/                    # 1 doc
│   └── budget-allocator/                  # [Strategic] NEW
│       ├── SKILL.md
│       └── references/                    # 4 docs
├── tests/
├── README.md
└── LICENSE
```

---

## v6 → v7 Changelog

| Dimension | v6 | v7 | Why |
|-----------|----|----|-----|
| Platforms | 2 (Google, Bing) | 4 (+ Meta, GA4) | Cross-platform budget decisions need cross-platform data |
| Skills | 5 | 9 | +campaign-launcher, +creative-analyst, +bid-strategist, +budget-allocator |
| Subagents | 0 | 3 | 2–3x faster multi-platform operations |
| Hooks | 1 (warn-only) | 3 (tiered blocking + ceiling + audit) | Actual safety enforcement, not just warnings |
| Bing mutations | Read-only | Full CRUD | Automated remediation on Bing — the #1 user complaint in v6 |
| Reference strategy | Per-skill (duplicated) | Shared + skill-specific | Less duplication, easier maintenance |
| Mutation safety | Binary (dry/live) | 3 tiers by risk | Proportional safety — low-risk changes shouldn't feel like high-risk ones |

---

## What's Not Included (and Why)

| Excluded | Reason |
|----------|--------|
| LinkedIn Ads | Different buying model (B2B lead gen), low overlap with core Search + Social workflow |
| Twitter/X Ads | Small budgets for most advertisers, limited API, low ROI for engineering effort |
| Programmatic / DSP | Entirely different discipline (bidstream, not keyword/audience-based) |
| SEO tools | Different discipline — better served by a separate plugin |
| Landing page builder | Outside scope of ads management |
| CRM integration | Too account-specific — better as a separate plugin or MCP |
| Email/SMS marketing | Different channel, different optimization model |

The boundary is clear: **this plugin manages paid media buying across Search and Social platforms.** Adjacent disciplines (SEO, CRM, landing pages) are better served by dedicated plugins that can integrate via shared MCPs.

---

## Skill Trigger Phrases

| Skill | Trigger phrases |
|-------|----------------|
| platform-setup | "set up Google Ads", "connect Bing", "configure Meta", "verify my accounts", "set up GA4" |
| morning-brief | "morning brief", "daily check", "what happened overnight", "how are my campaigns doing", "account health" |
| waste-detector | "find waste", "audit my accounts", "where am I bleeding money", "spend leaks", "waste analysis" |
| search-term-verdict | "review search terms", "negative keywords", "search term report", "query sculpting", "n-gram analysis" |
| campaign-launcher | "build a campaign", "launch a campaign", "set up a new campaign", "create campaigns for..." |
| creative-analyst | "analyze my ads", "ad copy performance", "creative fatigue", "RSA analysis", "testing gaps", "ad testing" |
| bid-strategist | "audit bid strategies", "check my bidding", "bid strategy recommendations", "am I bidding right" |
| pmax-decoder | "decode PMax", "Performance Max analysis", "what is PMax doing", "PMax search terms", "PMax brand traffic" |
| budget-allocator | "reallocate budget", "budget optimization", "where should I shift budget", "budget recommendations", "diminishing returns" |

---

## Implementation Priority

Build in this order — each phase delivers standalone value:

| Phase | Skills | MCPs | Hooks | Subagents | Value unlocked |
|-------|--------|------|-------|-----------|----------------|
| **Phase 1** | Enhance existing 5 skills with Bing mutations | bing-ads v2 (mutations) | mutation-gate v2 (tiered) | — | Bing parity. Automated remediation on both Search platforms |
| **Phase 2** | + campaign-launcher, + creative-analyst | — | + audit-logger | — | Campaign management. Creative optimization |
| **Phase 3** | + bid-strategist, + budget-allocator | + ga4 | + budget-ceiling | + platform-scout, + synthesizer | Strategic optimization. Cross-platform budget intelligence |
| **Phase 4** | Expand all skills to Meta | + meta-ads | Extend all hooks to Meta | + campaign-deep-dive | Full cross-platform coverage |

Each phase ships independently. No phase depends on a later one.
