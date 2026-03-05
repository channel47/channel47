---
name: competitor-intel
description: >-
  This skill should be used when the user asks about "competitors",
  "auction insights", "competitive analysis", "who am I competing with",
  "competitive landscape", "competitor benchmarks", "market position",
  "share of voice", "SOV", "who's outranking me", "am I losing to competitors",
  "impression share by competitor", "overlap rate",
  "who else is bidding on my keywords", "competitive threats",
  "new competitors showing up",
  or mentions competitor research, competitive intelligence,
  auction performance, or share of voice trends.
allowed-tools: mcp__google-ads__query, mcp__google-ads__list_accounts
---

# Competitor Intel -- Google Ads

Competitive intelligence from auction insights data. Identifies top threats, emerging competitors, share-of-voice trends, and coverage opportunities. Produces an action plan with bid strategy adjustments and impression share targets.

## Account Context

Read `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md` at the start of every run.
If it exists:
- Use known account IDs -- skip `list_accounts` discovery.
- Apply impression share targets from the profile as benchmarks for competitive position.
- Note active tests -- bid strategy tests affect competitive metrics.
- Check watch list for prior competitive findings that may need follow-up.
If it doesn't exist, fall back to `list_accounts` and suggest running `platform-setup`.

## Data Access

- `mcp__google-ads__query`: Execute GAQL SELECT queries and return structured rows.
- `mcp__google-ads__list_accounts`: Validate account access before analysis when customer scope is unclear.

Use GAQL templates from `references/gaql-queries.md` directly with `mcp__google-ads__query`.

### Connection verification

1. If the profile has account IDs, use them directly.
2. Otherwise, run `mcp__google-ads__list_accounts` to discover accounts.
3. If it fails, report the connection failure and suggest running `platform-setup`.

## Workflow

### Phase 1: Collect data

Execute the following queries from `references/gaql-queries.md`:

| Query ID | What It Returns |
|----------|----------------|
| CI-1 | Auction insights: impression share, overlap rate, position above rate, top impression %, absolute top impression %, outranking share per campaign |
| MB-2 | Budget pacing and impression share (for your own account's IS context) |
| MB-1 | Campaign daily performance (for spend and conversion context to weight competitive analysis) |

CI-1 is the primary competitive data source. MB-1 and MB-2 provide context for weighting findings by spend significance and identifying budget-constrained campaigns where competitive losses may be self-inflicted.

**Important GAQL note**: Auction insights data via GAQL returns campaign-level aggregates. Per-domain competitive breakdowns require the Google Ads UI Auction Insights report or the `auction_insight` resource. If CI-1 returns only your own campaign metrics without competitor domains, note this limitation and guide the user to the UI for per-domain data.

**Scope control**: If the user specifies a campaign or set of campaigns, add the appropriate WHERE filter. Otherwise, analyze all non-removed campaigns.

### Phase 2: Analyze competitive position

#### 2A: Impression share landscape

For each campaign, compute your competitive position:

| Metric | What It Tells You | Competitive Signal |
|--------|-------------------|-------------------|
| `auction_insight_search_impression_share` | How often your ads appeared vs total eligible auctions | Your market presence |
| `auction_insight_search_overlap_rate` | How often a competitor appeared in the same auctions | Who you compete against most |
| `auction_insight_search_position_above_rate` | How often a competitor's ad was shown above yours | Who is outranking you |
| `auction_insight_search_top_impression_percentage` | How often your ads appeared at the top of the page | Your premium placement rate |
| `auction_insight_search_absolute_top_impression_percentage` | How often your ads appeared in the absolute top position | Your #1 position rate |
| `auction_insight_search_outranking_share` | Net competitive position (you above them minus them above you) | Overall dominance metric |

Build the competitive landscape table (see Output format) with all competitors, sorted by overlap rate descending.

#### 2B: Threat classification

Classify each competitor into a threat tier:

| Tier | Criteria | Implication |
|------|----------|-------------|
| **Primary threat** | Overlap rate >60% AND position above rate >40% | Direct competitor consistently outranking you |
| **Rising challenger** | Overlap rate >30% AND position above rate increasing (if trend data available) | Growing competitive pressure |
| **Parallel player** | Overlap rate >30% AND position above rate <30% | Competing for same auctions but not consistently winning |
| **Peripheral** | Overlap rate <30% | Occasional overlap, low direct competition |

Weight threat classification by campaign spend. A primary threat in a $20K/mo campaign matters more than one in a $500/mo campaign.

#### 2C: Opportunity identification

Identify segments where you are underrepresented:

1. **Budget-constrained gaps**: Campaigns where `search_budget_lost_impression_share` (from MB-2) >15% AND competitors have high overlap rates. You are losing auctions you could win with more budget.
2. **Rank-constrained gaps**: Campaigns where `search_rank_lost_impression_share` (from MB-2) >15% AND competitors have high position-above rates. You are losing auctions due to Ad Rank (bid + quality).
3. **Top impression gaps**: Campaigns where your `top_impression_percentage` is <50% but competitors exceed 60%. You are appearing but not in premium positions.
4. **Absolute top gap**: Campaigns where `absolute_top_impression_percentage` is <20%. You rarely hold the #1 position.

For each gap, estimate the dollar impact:
- Budget gaps: `budget_lost_IS * current_monthly_spend` = approximate additional spend needed.
- Rank gaps: `rank_lost_IS * current_monthly_spend * 0.3` = conservative additional budget needed (assumes 30% bid increase to recover lost rank, actual may vary).
- Note: these are directional estimates. Actual costs depend on competitor behavior and auction dynamics.

Assign severity:
- **HIGH** (>$500/mo estimated recoverable value from closing the gap)
- **MEDIUM** ($100-500/mo)
- **LOW** ($25-100/mo)
- **INFO** (<$25/mo or insufficient data)

### Phase 3: Trend analysis (optional)

If the user requests trend comparison (e.g., "how has my competitive position changed"):

1. Run CI-1 for two periods: current period (default LAST_30_DAYS) and prior period (LAST_30_DAYS offset by 30 days, using explicit date ranges).
2. Compute delta for each competitor across all metrics.
3. Flag competitors with:
   - Impression share increase >5 percentage points (gaining ground).
   - Position above rate increase >10 percentage points (becoming more aggressive).
   - New competitors appearing in the current period that were absent in the prior period.
4. Present trend data in a comparison table (see Output format).

If the user does not request trends, skip this phase and note that trend analysis is available on request.

### Phase 4: Build action plan

For each identified opportunity, produce a concrete recommendation:

| Gap Type | Recommended Action | UI Path |
|----------|-------------------|---------|
| Budget-constrained | Increase daily budget by X% or reallocate from lower-priority campaigns | Google Ads > Campaigns > [Campaign] > Settings > Budget |
| Rank-constrained (quality) | Improve ad relevance and landing page experience to lift Ad Rank | Google Ads > Campaigns > [Campaign] > Ad groups > [Ad group] > Keywords > Quality Score column |
| Rank-constrained (bid) | Increase target CPA/ROAS or switch to target impression share strategy | Google Ads > Campaigns > [Campaign] > Settings > Bidding |
| Top impression gap | Set target impression share with "Top of page" location target | Google Ads > Campaigns > [Campaign] > Settings > Bidding > Target impression share |
| Absolute top gap | Set target impression share with "Absolute top of page" at X% | Same as above, select "Absolute top of the page" |

Every recommendation includes:
- The specific campaign name and ID.
- Current metric value and target value.
- Estimated monthly cost of the adjustment.
- Expected outcome (conservative estimate).

### Phase 5: DataForSEO companion note

If the user has the DataForSEO MCP configured, note that organic + paid cross-referencing is available:
- SERP analysis for competitor domain ranking on shared keywords.
- Backlink and domain authority comparison.
- Content gap analysis for landing page competitiveness.

Do not invoke DataForSEO tools from this skill. Mention the capability and suggest the user run a separate DataForSEO analysis for a complete competitive picture.

## Output format

```markdown
## Competitive Intel -- [Date]

### Account
- Google Ads: [Account Name] ([Customer ID])
- Campaigns analyzed: [N]
- 30-day spend: $X,XXX

### Competitive Landscape

| Competitor | Impression Share | Overlap Rate | Position Above | Top Impr. % | Abs. Top % | Outranking Share | Threat Tier |
|------------|----------------:|-----------:|---------------:|-----------:|---------:|-----------------:|-------------|
| You | XX.X% | -- | -- | XX.X% | XX.X% | -- | -- |
| competitor1.com | XX.X% | XX.X% | XX.X% | XX.X% | XX.X% | XX.X% | Primary |
| competitor2.com | XX.X% | XX.X% | XX.X% | XX.X% | XX.X% | XX.X% | Rising |
| ... | | | | | | | |

### Top Threats

1. **competitor1.com** (Primary threat)
   - Appears in XX% of your auctions, outranks you XX% of the time
   - Strongest overlap in: [Campaign Name] ($X,XXX/mo spend)
   - Outranking share: XX% (they dominate the head-to-head)

2. **competitor2.com** (Rising challenger)
   - Overlap increasing, now at XX%
   - Position above rate: XX% (and growing)

### Opportunities

| # | Severity | Campaign | Gap Type | Current IS | Lost IS | Est. Monthly Value | Action |
|---|----------|----------|----------|----------:|---------:|-------------------:|--------|
| 1 | HIGH | [name] | Budget | XX% | XX% budget-lost | $X,XXX | Increase budget by X% |
| 2 | MEDIUM | [name] | Rank | XX% | XX% rank-lost | $XXX | Improve QS or raise bids |
| 3 | LOW | [name] | Top position | XX% top IS | -- | $XXX | Target impression share |

**UI paths:**
- Budget adjustment: Google Ads > Campaigns > [Campaign] > Settings > Budget
- Bid strategy: Google Ads > Campaigns > [Campaign] > Settings > Bidding
- Quality improvement: Google Ads > Campaigns > [Campaign] > Ad groups > Keywords > Quality Score

### Trend Comparison (if requested)

| Competitor | IS (Current) | IS (Prior) | Delta | Position Above (Current) | Position Above (Prior) | Delta |
|------------|------------:|----------:|------:|------------------------:|----------------------:|------:|
| You | XX.X% | XX.X% | +X.X% | -- | -- | -- |
| competitor1.com | XX.X% | XX.X% | +X.X% | XX.X% | XX.X% | +X.X% |

### Action Plan

1. **[Campaign]** -- [action] -- Est. cost: $XXX/mo -- Expected IS gain: +X%
   **UI path:** Google Ads > [specific path]

2. **[Campaign]** -- [action] -- Est. cost: $XXX/mo -- Expected IS gain: +X%
   **UI path:** Google Ads > [specific path]

### Cross-Channel Note
For a complete competitive picture including organic rankings, backlink profiles,
and content gaps, consider running a DataForSEO analysis alongside this auction
insights review. The DataForSEO MCP can provide SERP competitor overlap data
that complements paid auction insights.

### Notes
- Auction insights data reflects search campaign auctions only (Shopping and PMax have separate competitive dynamics)
- Competitor domains are anonymized in some cases by Google
- Impression share and outranking share are relative metrics -- they shift when competitors change behavior even if you don't
- Dollar impact estimates are directional -- actual costs depend on auction dynamics and competitor responses
```

## Guardrails

- **Read-only**: This skill produces analysis and recommendations only. No account modifications are made. All recommended actions include Google Ads UI paths.
- **Auction insights scope**: GAQL auction insights may return campaign-level aggregates without per-domain breakdowns depending on the resource used. If per-domain data is not available via the API, clearly state the limitation and provide the UI path: Google Ads > Campaigns > [Campaign] > Auction insights (tab).
- **No competitor attribution**: Google anonymizes some competitor domains. Do not attempt to guess or identify anonymized competitors. Report them as-is.
- **Relative metrics caveat**: Impression share and outranking share are zero-sum. Your metrics can worsen even if your performance is stable, simply because a competitor increased their spend. Note this in the output.
- **Budget recommendations**: When recommending budget increases, always show the estimated incremental cost. Do not recommend budget increases without quantifying the investment required.
- **Bid strategy warnings**: Switching to target impression share can significantly increase CPCs. Always note the CPA/ROAS risk when recommending impression share targeting.
- **DataForSEO boundary**: Do not call DataForSEO MCP tools from this skill. Only mention the capability as an optional companion analysis.
- **Trend data reliability**: Period-over-period comparison requires sufficient data in both periods. If a campaign was paused or had <$100 spend in either period, exclude it from trend analysis and note the exclusion.
- **Severity calibration**: All dollar impact figures are labeled as directional estimates. Competitor behavior is unpredictable -- actual costs to close gaps may be higher or lower than estimated.

## Profile Maintenance

After completing analysis, if `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md` exists:
1. Update Watch List with:
   - Primary threats gaining impression share (if trend analysis was run).
   - HIGH-severity budget or rank gaps in top-spend campaigns.
   - New competitors appearing for the first time.
2. Update Active Tests if the user mentioned starting a bid strategy or impression share test during the session.
3. Append to Decision Log if the user acknowledged specific bid or budget adjustment actions.
4. Update "Last updated" date.
Present proposed profile changes to the user before writing.

## References

- `references/gaql-queries.md` -- query IDs: CI-1, MB-1, MB-2
