# Channel 47 Paid Media Plugin Suite — Architecture Map

**Date:** March 4, 2026
**Approach:** Assemble the best existing open-source tools into a coherent, practitioner-grade plugin suite. Build only what doesn't exist. Read-only by design.

---

## Design Philosophy

1. **Curate, don't rebuild.** If someone built a better MCP, use it. If claude-ads has a better audit framework, reference it.
2. **Workflows, not tools.** Each plugin is organized around what practitioners actually do, not API endpoints.
3. **Best-in-class per slot.** For each workflow need (MCP, skill, agent, hook), pick the single best available option.
4. **Separate platforms.** Google and Bing are separate plugins. Each platform stands alone.
5. **Read-only by design.** No mutations, no bid adjustments, no keyword pauses. The plugins read data and produce prioritized, dollar-quantified action plans with exact UI navigation paths. Users execute in the platform UI. This is a trust decision, not a temporary limitation.
6. **Specificity over automation.** Read-only plugins compensate with extreme output specificity: dollar impact per finding, exact UI paths for each fix, copy-paste artifacts (negative keyword lists, CSV exports), time estimates per action, priority ranking by dollar impact.

---

## Plugin Suite Overview

| Plugin | Platform | Primary MCP | Phase |
|--------|----------|-------------|-------|
| `google-ads` | Google Ads | cohnen/mcp-google-ads (439 stars, 12+ read tools) | **P0** |
| `microsoft-ads` | Microsoft/Bing Ads | Duartemartins/microsoft-ads-mcp-server or @channel47/bing-ads-mcp | **P0** |
| `meta-ads` | Facebook + Instagram | pipeboard-co/meta-ads-mcp (563 stars, 10K+ businesses) | **P0** |
| `tiktok-ads` | TikTok | ysntony/tiktok-ads-mcp (read-only, safe) | **P1** |
| `linkedin-ads` | LinkedIn | danielpopamd/linkedin-ads-mcp (14 tools) | **P1** |
| `amazon-ads` | Amazon Sponsored Products/Brands/Display | Amazon Official MCP (open beta, first-party) | **P2** |
| `reddit-ads` | Reddit | sbmeaper/reddit-ad-mcp (read-only) | **P2** |
| `apple-search-ads` | Apple Search Ads | appleadsmcp.com (free read tier) | **P3** |

### Official MCP Landscape

Only 2 of 8 platforms have official first-party MCP servers:

| Platform | Official MCP? | Capabilities | Maturity | Our Use |
|----------|:---:|---|---|---|
| **Google Ads** | Yes | 2 read tools (list accounts, structured GAQL search) | v0.0.1, stale since Oct 2025, API v21 | Too limited. Use cohnen instead. Offer as alternative for max trust. |
| **Amazon Ads** | Yes | Full read + write, campaign CRUD, multi-country expansion | Open beta since Feb 2026, actively developed | **Use as primary.** Best MCP in the suite. |
| Meta Ads | No | — | Meta investing in Manus/Advantage+ internally | Use Pipeboard or brijr |
| Microsoft/Bing Ads | No | — | Microsoft has 18+ MCPs for other products, not ads | Use Duartemartins or @ch47 |
| TikTok Ads | No | — | No signals | Use ysntony |
| LinkedIn Ads | No | — | No signals | Use danielpopamd |
| Reddit Ads | No | — | No signals | Use sbmeaper |
| Apple Search Ads | No | — | No signals | Use appleadsmcp.com |

### MCP Selection Criteria

Since all plugins are read-only, MCP evaluation is purely about read quality:

- Open-source with permissive license (MIT, Apache-2.0)
- Local stdio transport (credentials stay on user's machine)
- Active maintenance (commits within last 6 months)
- Breadth and depth of read tools for the platform's core workflows
- Community trust signals (GitHub stars, usage, issues resolved)
- Write capability is irrelevant — we don't use it

---

## Shared Architecture

Every plugin follows this structure:

```
[platform]-ads/
├── .claude-plugin/plugin.json         # Plugin manifest
├── .mcp.json                          # Curated MCP server(s), pinned versions
├── skills/
│   ├── platform-setup/SKILL.md        # Credential verification, account discovery
│   ├── profile-review/SKILL.md        # Persistent account context
│   ├── morning-brief/SKILL.md         # Daily health check + anomaly detection
│   ├── waste-detector/SKILL.md        # Platform-specific waste categories → action plan
│   ├── account-scorecard/SKILL.md     # Quantified health grade across dimensions
│   └── [platform-specific]/           # Skills unique to this platform
├── hooks/
│   ├── inject-profile.sh             # SessionStart: load account profile
│   └── update-profile.py             # Stop: save watch list + decision log
└── references/
    ├── [query-templates].md           # Platform-specific query templates
    ├── thresholds.md                  # Anomaly detection thresholds + dollar formulas
    ├── benchmarks.md                  # Industry benchmarks
    └── ui-paths.md                    # Platform UI navigation reference
```

### Shared Patterns

- **Account profile persistence** — `profile/account-profile.md` carries session-to-session memory (account IDs, KPI targets, watch list, active tests, decision log)
- **Profile injection at session start** — `inject-profile.sh` hook loads known context so skills skip discovery
- **State save at session end** — `update-profile.py` hook updates watch list and decision log
- **Anomaly detection formulas** — deviation from 7d/30d baselines, dollar impact gating, applies identically across platforms
- **Severity tagging** — HIGH (>$500/mo), MEDIUM ($100-500), LOW ($25-100), INFO (<$25)
- **Priority ranking** — all findings ranked by dollar impact descending, across all waste types

### Read-Only Output Patterns

Every actionable skill produces three types of output that compensate for lack of mutations:

**1. Dollar-quantified priority tables:**
```
| Priority | Action | Where | Est. Monthly Savings |
|----------|--------|-------|---------------------|
| 1 | Pause keyword | Campaign X → AG Y → "keyword z" | $847 |
| 2 | Add 3 negatives | Shared list "Junk Terms" | $612 |
```

**2. Exact UI navigation paths:**
```
Google Ads → Campaign "Brand - Exact" → Ad Group "core-terms" → Keywords → select "running shoes red" → Pause
```

**3. Copy-paste artifacts:**
```
### Negative keywords to add (paste into shared negative list "Brand Exclusions"):
[running shoes red]
[cheap running shoes]
"free running shoes"
```

Reference files include a `ui-paths.md` per platform that maps common actions to their exact click paths. Skills inject these into output.

---

## Supporting Tools (available to all plugins)

| Need | Best Tool | URL |
|------|-----------|-----|
| Competitive intelligence | DataForSEO MCP (@channel47 or official) | github.com/dataforseo/mcp-server-typescript |
| Google Analytics 4 | Official GA4 MCP | github.com/googleanalytics/google-analytics-mcp |
| Tag Manager / tracking | stape-io/google-tag-manager-mcp-server | github.com/stape-io/google-tag-manager-mcp-server |
| Google Sheets (reporting) | xing5/mcp-google-sheets | github.com/xing5/mcp-google-sheets |
| Ad Library (Meta) | trypeggy/facebook-ads-library-mcp | github.com/trypeggy/facebook-ads-library-mcp |
| Ad Library (Google) | talknerdytome-labs/google-ads-library-mcp | github.com/talknerdytome-labs/google-ads-library-mcp |
| Cross-platform audit | AgriciDaniel/claude-ads (186 checks) | github.com/AgriciDaniel/claude-ads |
| Shopping feed optimization | google-marketing-solutions/feedgen | github.com/google-marketing-solutions/feedgen |
| GAQL reference | @channel47/skills/gaql | Already in ch47/skills |
| PMax reporting script | agencysavvy/pmax | github.com/agencysavvy/pmax |
| Looker Studio | Google Official Looker MCP | cloud.google.com/blog/products/business-intelligence/introducing-looker-mcp-server |
| ASO (for Apple SA) | Eronred/aso-skills + dock-aso/aso-optimizer-skill | github.com/Eronred/aso-skills |
| Meta Ads analysis | mathiaschu/meta-ads-analyzer | github.com/mathiaschu/meta-ads-analyzer |
| Marketing skills (general) | coreyhaines31/marketingskills | github.com/coreyhaines31/marketingskills |

---

## 1. GOOGLE ADS PLUGIN

### MCP Decision

| MCP | Stars | Read Tools | Auth | Verdict |
|-----|-------|-----------|------|---------|
| **cohnen/mcp-google-ads** | 439 | 12+ tools: GAQL queries, campaigns, keywords, ads, image assets, account currency. Raw GAQL + structured queries. Table/JSON/CSV output. | OAuth + service acct | **Primary choice.** Broadest read toolset. Most popular. |
| **googleads/google-ads-mcp** | 257 | 2 tools: list accounts, structured GAQL search. | OAuth | Official but too limited. v0.0.1, stale since Oct 2025, API v21. Offer as alternative for max trust. |
| **google-marketing-solutions/google_ads_mcp** | — | 5 tools: list accounts, raw GAQL, GAQL docs, reporting views/fields docs. MCP resources. | OAuth | v0.6.2, API v23. Not officially supported. Better than official but still niche. |

**Recommendation:** `cohnen/mcp-google-ads` as primary. Mention Google's official MCP in setup docs as an alternative for users who prioritize first-party trust over tool breadth.

### Practitioner Workflows → Existing Tools

#### DAILY (15-45 min per account)

| Workflow | What Practitioners Do | Existing Tool | Gap? |
|----------|----------------------|---------------|------|
| **Spend & budget monitoring** | Check yesterday's spend vs. daily budget, flag over/under delivery | MCP query (campaign daily performance) | Write morning-brief SKILL.md |
| **Anomaly detection** | Spot CPC spikes, CTR drops, zero-conversion days | MCP query + thresholds in references/ | Write anomaly-detection logic in SKILL.md |
| **Ad disapprovals** | Check for policy violations | MCP query (ad_group_ad WHERE approval_status) | Include in morning-brief |
| **Conversion tracking verification** | Confirm conversions fired yesterday | MCP query + GA4 MCP cross-reference | GA4 MCP available |
| **Auto-applied recommendation check** | Verify Google hasn't changed settings | MCP query (change_event) | Include in morning-brief |
| **Budget pacing** | Monthly runway projection | MCP query + math in SKILL.md | No existing tool does this as MCP |

#### WEEKLY (2-6 hours per account)

| Workflow | What Practitioners Do | Existing Tool | Read-Only Output |
|----------|----------------------|---------------|-----------------|
| **Search term mining & negatives** | Pull SQR, classify terms, add negatives | MCP query + search-term-verdict SKILL.md | Export promote/negate/monitor lists. Copy-paste ready negative keyword lists grouped by match type. |
| **Keyword management** | Pause high-spend/zero-conv keywords | MCP query | Priority-ranked pause list with UI paths and dollar impact per keyword. |
| **Ad performance review** | RSA asset performance, pause losers | MCP query (asset performance) | Write ad-copy-analyzer SKILL.md — fatigue detection + replacement recommendations. |
| **Display/YouTube placement exclusions** | Exclude junk placements | MCP query | Placement exclusion list with UI path to Placements > Where ads showed. |
| **Device & geo performance** | Review device/geo performance | MCP query (segments by device, geo) | Include in waste-detector — flag segments with spend but no conversions. |

#### MONTHLY (4-12 hours per account)

| Workflow | What Practitioners Do | Existing Tool | Gap? |
|----------|----------------------|---------------|------|
| **Client reporting** | Build monthly performance report with narrative | MCP query + GA4 MCP + Google Sheets MCP | Write client-report SKILL.md |
| **Auction insights & competitive analysis** | Pull auction insights, research competitors | MCP query + DataForSEO MCP + Google Ads Library MCP | Write competitor-intel SKILL.md |
| **Conversion tracking audit** | Verify tags, check for duplicates, audit attribution | GTM MCP (stape-io) + GA4 MCP | Write tracking-audit SKILL.md |
| **Quality Score deep dive** | Export QS, diagnose failing components | MCP query (keyword QS breakdown) | Include in account-scorecard |
| **Account structure review** | Evaluate campaign organization, consolidation | MCP query (full account map) | Include in account-scorecard |
| **Feed optimization (ecom)** | Audit GMC feed, fix disapprovals, optimize titles | feedgen (google-marketing-solutions) | Reference feedgen in SKILL.md |

#### QUARTERLY / AD-HOC

| Workflow | What Practitioners Do | Existing Tool | Gap? |
|----------|----------------------|---------------|------|
| **Full account audit** | 60+ point comprehensive review | **claude-ads (AgriciDaniel, 652 stars)** — 74 Google Ads checks with weighted scoring, industry templates | **Already exists. Best in class.** Reference as companion. |
| **PMax transparency** | Decode PMax asset groups, placements | **pmax-decoder SKILL.md (@ch47)** + agencysavvy/pmax script | **Already built** in paid-search plugin |
| **Click fraud analysis** | Detect bot traffic, file invalid click reports | No MCP. Manual or commercial (Lunio, ClickCease) | **Gap** — no open-source solution |

### Recommended Plugin Assembly

```
google-ads/
├── .mcp.json                          → cohnen/mcp-google-ads (pinned version)
├── skills/
│   ├── platform-setup/SKILL.md        → Verify credentials, discover accounts
│   ├── profile-review/SKILL.md        → Persistent account context (from paid-search)
│   ├── morning-brief/SKILL.md         → Daily health check (from paid-search, adapted)
│   ├── waste-detector/SKILL.md        → 8 waste categories → action plan with UI paths + export lists
│   ├── search-term-verdict/SKILL.md   → Classify → export promote/negate/monitor lists (from paid-search)
│   ├── pmax-decoder/SKILL.md          → PMax transparency (from paid-search)
│   ├── account-scorecard/SKILL.md     → Quantified health grade across 5 dimensions [NEW]
│   ├── ad-copy-analyzer/SKILL.md      → RSA asset performance, fatigue detection [NEW]
│   └── competitor-intel/SKILL.md      → Auction insights + DataForSEO [NEW]
├── hooks/
│   ├── inject-profile.sh             → Load account profile at session start
│   └── update-profile.py             → Save watch list / decision log at session end
└── references/
    ├── gaql-queries.md                → Query templates (from paid-search)
    ├── thresholds.md                  → Anomaly detection thresholds + dollar formulas (from paid-search)
    ├── benchmarks.md                  → 2026 industry benchmarks
    └── ui-paths.md                    → Google Ads UI navigation reference [NEW]
```

**Key decisions:**
- Move existing paid-search skills (morning-brief, waste-detector, search-term-verdict, pmax-decoder) into google-ads plugin
- All skills produce action plans, not mutations — every finding includes UI path, dollar impact, copy-paste artifact
- Reference claude-ads for full audit framework (don't rebuild — their 74 Google checks with industry templates are best-in-class)
- Use DataForSEO MCP for competitive intelligence
- Use GA4 MCP and GTM MCP as optional companions

---

## 2. MICROSOFT ADS PLUGIN

### MCP Decision

| MCP | Read Tools | Auth | Verdict |
|-----|-----------|------|---------|
| **Duartemartins/microsoft-ads-mcp-server** | Campaign mgmt, keyword/search query/geo reports, QS. DuckDuckGo support. Built with Bing Ads Python SDK. | OAuth + Bing SDK | Most complete community option. Evaluate read depth vs. @ch47. |
| **@channel47/bing-ads-mcp** | query, report (CSV parsing), list accounts/stores/products | OAuth | Already built. Has reporting pipeline with CSV parsing. |
| **CData/bing-ads-mcp-server** | Read-only via JDBC | JDBC | Quick data access. Commercial upsell. |

**Recommendation:** Evaluate Duartemartins vs. @channel47/bing-ads-mcp on read tool depth. Pick whichever has stronger reporting and keyword/search query access. No official Microsoft Advertising MCP exists despite Microsoft having 18+ MCPs for other products.

### Practitioner Workflows → Existing Tools

#### DAILY

| Workflow | What Practitioners Do | Existing Tool | Gap? |
|----------|----------------------|---------------|------|
| **Budget pacing check** | Bing burns budgets at odd hours | MCP report | morning-brief SKILL.md |
| **Bot/spam traffic monitoring** | Check search partner/audience network for junk | MCP report (publisher URLs) | Include in morning-brief |
| **Search term quality review** | Bing's close variants are worse than Google | MCP report (search terms) | search-term-verdict adapted for Bing |

#### WEEKLY

| Workflow | What Practitioners Do | Existing Tool | Read-Only Output |
|----------|----------------------|---------------|-----------------|
| **Search term report + negatives** | More aggressive negative management needed on Bing | MCP report + search-term-verdict | Export negative lists. Bing needs more aggressive negation than Google — skill reflects this. |
| **Publisher/placement report** | Find and exclude junk MSAN placements | MCP report (Website URL report) | Exclusion list with publisher URLs + UI path to Settings > Website exclusions. |
| **LinkedIn audience analysis** | Bing's unique B2B targeting via LinkedIn profiles | MCP query (audience performance) | Performance by LinkedIn segment with recommendations. |
| **Auto-import verification** | Check that Google sync hasn't overwritten settings | MCP query (campaign settings) | Diff of settings that diverge from expected. Include in morning-brief. |

#### BING-SPECIFIC WASTE CATEGORIES

1. **MSAN/Audience Network left enabled** — the #1 money drain per practitioners
2. **Search partners enabled** — junk traffic from syndication
3. **Broad match imported from Google** — catastrophic query expansion on Bing
4. **Auto-import overwriting optimizations** — silent changes
5. **Budget burning overnight** — no default ad scheduling
6. **Bot traffic on lead gen forms** — worse than Google
7. **Location targeting expanding silently** — "interest" vs. "physical"

### Recommended Plugin Assembly

```
microsoft-ads/
├── .mcp.json                          → Duartemartins or @channel47/bing-ads-mcp (pinned version)
├── skills/
│   ├── platform-setup/SKILL.md        → Verify credentials, discover accounts
│   ├── profile-review/SKILL.md        → Persistent account context
│   ├── morning-brief/SKILL.md         → Daily health + bot traffic monitoring + import drift
│   ├── waste-detector/SKILL.md        → 7 Bing-specific waste categories → action plan
│   ├── search-term-verdict/SKILL.md   → Adapted for Bing's worse close variants, aggressive negation
│   ├── account-scorecard/SKILL.md     → Quantified health grade [NEW]
│   ├── import-auditor/SKILL.md        → Post-Google-import cleanup with specific fixes [NEW]
│   └── placement-cleaner/SKILL.md     → MSAN/publisher exclusion recommendations [NEW]
├── hooks/
│   ├── inject-profile.sh             → Load account profile at session start
│   └── update-profile.py             → Save watch list / decision log at session end
└── references/
    ├── bing-queries.md                → Report configurations (from paid-search)
    ├── thresholds.md                  → Bing-specific anomaly thresholds
    ├── import-checklist.md            → Post-import cleanup checklist [NEW]
    └── ui-paths.md                    → Microsoft Advertising UI navigation reference [NEW]
```

---

## 3. META ADS PLUGIN

### MCP Decision

| MCP | Stars | Read Tools | Auth | Verdict |
|-----|-------|-----------|------|---------|
| **pipeboard-co/meta-ads-mcp** | 563 | Full campaign/adset/ad/insights. | OAuth, remote | Best overall. 10K+ businesses. Battle-tested. **Note: remote MCP — credentials flow to Pipeboard's servers.** |
| **brijr/meta-mcp** | — | 25 tools: insights, audiences, creatives | Token, local | Most comprehensive local MCP. Credentials stay on user's machine. |
| **ArmavitA (EfrainTorres)** | — | Campaigns, insights, Ad Library search, interest/behavior/demographic targeting search, audience estimation | Token | Best audience/targeting toolset. |
| **GoMarble/facebook-ads-mcp-server** | — | Accounts, campaigns, adsets, ads, creatives, insights | OAuth via GoMarble | Easy setup. Free Ad Analyzer web tool. |

**Recommendation:** Offer both options in documentation:
- **Pipeboard** (remote, most battle-tested, 10K+ businesses) — for users who trust Pipeboard's hosted auth
- **brijr/meta-mcp** (local, 25 tools) — for users who want credentials to stay on their machine

No official Meta MCP exists. Meta is investing in Manus/Advantage+ internally, not developer tooling for external agents.

### Additional Meta Tools

| Tool | What It Does | URL |
|------|-------------|-----|
| **mathiaschu/meta-ads-analyzer** (215 stars) | Breakdown Effect analysis, Learning Phase detection, expert diagnosis | github.com/mathiaschu/meta-ads-analyzer |
| **trypeggy/facebook-ads-library-mcp** | Ad Library competitive research with AI image/video analysis | github.com/trypeggy/facebook-ads-library-mcp |
| **talknerdytome-labs/claude-agents** | Meta Ads Library subagent for multi-competitor benchmarking | github.com/talknerdytome-labs/claude-agents |

### Practitioner Workflows → Existing Tools

#### DAILY

| Workflow | What Practitioners Do | Existing Tool | Gap? |
|----------|----------------------|---------------|------|
| **CPA/ROAS check** | Compare yesterday vs. 7d avg, spot anomalies | MCP query (insights, date presets) | morning-brief SKILL.md |
| **Delivery flags** | "Learning Limited," rejected ads, auto-pauses | MCP query (effective_status, delivery) | Include in morning-brief |
| **CPM/frequency monitoring** | Detect creative fatigue signals | MCP query (frequency, CPM trends) | Include in morning-brief |
| **Pixel/CAPI health** | Check Events Manager diagnostics | No MCP for Events Manager diagnostics | **Gap** — manual check |
| **Ad comment management** | Hide spam, reply to questions (39% reach impact) | No MCP for comment management | **Gap** |

#### WEEKLY

| Workflow | What Practitioners Do | Existing Tool | Read-Only Output |
|----------|----------------------|---------------|-----------------|
| **Creative performance review** | Identify winners, kill losers, graduate to Scale | MCP query (ad-level insights) | Lifecycle classification: Testing → Scaling → Mature → Fatiguing → Dead. Per-creative action recommendation. |
| **Breakdown reports** | Age/gender/placement waste detection | MCP query (insights with breakdowns) | Include in waste-detector — flag segments with spend but no conversions. |
| **Audience overlap check** | Verify adsets aren't competing | Meta Audience Overlap tool (UI only) | **Gap** — no API access. Flag high-frequency adsets as proxy. |
| **Backend reconciliation** | Compare Meta conversions to Shopify/CRM | MCP query + external data source | Partial — needs CRM connector |

#### MONTHLY

| Workflow | What Practitioners Do | Existing Tool | Gap? |
|----------|----------------------|---------------|------|
| **Full account audit** | Structure, tracking, creative, audience review | **claude-ads** (46 Meta checks) + **meta-ads-analyzer** (Breakdown Effect, Learning Phase) | **Already exists** — reference both |
| **Creative audit** | Categorize all ads by concept/format/angle | MCP query (all active ads) | Write creative-audit SKILL.md |
| **Attribution review** | Compare 7d click / 1d view vs. GA4 last-click | MCP query + GA4 MCP | Write attribution-review SKILL.md |
| **Competitor research** | Spy on competitor ads via Ad Library | **trypeggy/facebook-ads-library-mcp** + **talknerdytome-labs agents** | **Already exists** |

#### META-SPECIFIC WASTE CATEGORIES

1. **Audience overlap** — adsets with >30% overlap bidding against each other
2. **Creative fatigue** — frequency >4, CTR declining >20% WoW
3. **Placement waste** — Audience Network / Right Column eating budget
4. **Demographic waste** — age/gender segments with spend but no conversions
5. **Learning Limited drain** — adsets stuck >7 days, still spending
6. **Broad targeting bleed** — interests/lookalikes with high spend, low ROAS
7. **Dayparting opportunity** — hours with spend but 0 conversions
8. **Frequency ceiling** — >3.0 on prospecting = audience exhaustion

### Recommended Plugin Assembly

```
meta-ads/
├── .mcp.json                          → pipeboard-co/meta-ads-mcp (primary, remote)
│                                        OR brijr/meta-mcp (local alternative)
│                                        + trypeggy/facebook-ads-library-mcp (competitive intel)
├── skills/
│   ├── platform-setup/SKILL.md        → Verify token, discover accounts, check pixel health
│   ├── profile-review/SKILL.md        → Persistent account context
│   ├── morning-brief/SKILL.md         → Daily health: CPA, CPM, frequency, delivery, Learning Phase
│   ├── waste-detector/SKILL.md        → 8 Meta-specific waste categories → action plan
│   ├── creative-fatigue/SKILL.md      → CTR/CPA decay detection, lifecycle classification, "days remaining" [KEY DIFFERENTIATOR]
│   ├── creative-audit/SKILL.md        → Categorize ads by concept/format/angle [NEW]
│   ├── account-scorecard/SKILL.md     → Quantified health grade [NEW]
│   ├── audience-analyzer/SKILL.md     → Performance by audience type, saturation detection [NEW]
│   └── competitor-research/SKILL.md   → Orchestrate Ad Library MCP [NEW]
├── agents/
│   ├── creative-analyst.md            → Parallel creative performance analysis
│   └── competitor-scout.md            → Ad Library research (reference talknerdytome-labs pattern)
├── hooks/
│   ├── inject-profile.sh             → Load account profile at session start
│   └── update-profile.py             → Save watch list / decision log at session end
└── references/
    ├── waste-queries.md               → Insight query templates per waste category
    ├── fatigue-model.md               → Decay rate formulas, benchmark fatigue curves
    ├── thresholds.md                  → CPM, CTR, frequency, CPA anomaly thresholds
    ├── benchmarks.md                  → 2026 Meta benchmarks by vertical
    └── ui-paths.md                    → Meta Ads Manager UI navigation reference [NEW]
```

---

## 4. TIKTOK ADS PLUGIN

### MCP Decision

| MCP | Read Tools | Auth | Verdict |
|-----|-----------|------|---------|
| **ysntony/tiktok-ads-mcp** | 6 read-only tools: advertisers, campaigns, ad groups, ads, reports | API token | **Primary choice.** Clean, pure read. Safest. |
| **Seym0n/tiktok-mcp** | Video search, subtitle extraction, engagement metrics | TikNeuron API | Creative research companion — not campaign management. |

**Recommendation:** ysntony/tiktok-ads-mcp as primary. Seym0n/tiktok-mcp as optional companion for creative research. No official TikTok MCP exists.

### Practitioner Workflows → Existing Tools

**TikTok is 70-80% creative production, 20-30% media buying.** The plugin must reflect this.

#### DAILY

| Workflow | What Practitioners Do | Existing Tool | Gap? |
|----------|----------------------|---------------|------|
| **Spend pacing + CPA check** | Flag runaway or stalled campaigns | MCP query (campaign metrics) | morning-brief SKILL.md |
| **Flag underperformers** | Creatives below 25% hook rate should be paused | MCP query (ad-level 3s view rate) | Include in morning-brief — flag with UI path to pause |
| **Ad rejection monitoring** | TikTok suspends aggressively | MCP query (ad status) | Include in morning-brief |

#### WEEKLY

| Workflow | What Practitioners Do | Existing Tool | Read-Only Output |
|----------|----------------------|---------------|-----------------|
| **Creative performance review** | Which hooks, formats, CTAs won | MCP query + creative tracker | Lifecycle classification per creative. Priority-ranked pause/scale recommendations. |
| **Hook rate analysis** | 3s view rate is THE metric | MCP query (video view metrics) | Include in creative-pulse — benchmark against vertical averages |
| **Competitor creative research** | Spy on competitor ads, trending formats | **Seym0n/tiktok-mcp** | Reference for creative research |
| **Creative velocity tracking** | How many new creatives per week vs. recommended 3-5 | MCP query (ad create dates) | Include in creative-pulse — flag stagnation |

#### TIKTOK-SPECIFIC WASTE CATEGORIES

1. **Low hook rate creatives** — <15% 3s view rate still spending
2. **Creative stagnation** — no new creatives in >14 days (TikTok penalizes this)
3. **Audience fatigue** — frequency >5 with declining engagement
4. **Placement waste** — TikTok vs. Pangle vs. News Feed Apps gaps
5. **Bid cap waste** — manual bids leaving daily budget unspent
6. **Polished-brand creative penalty** — non-native-looking ads underperforming

### Recommended Plugin Assembly

```
tiktok-ads/
├── .mcp.json                          → ysntony/tiktok-ads-mcp (read-only, pinned version)
│                                        + Seym0n/tiktok-mcp (creative research, optional)
├── skills/
│   ├── platform-setup/SKILL.md        → Verify API credentials, discover advertisers
│   ├── profile-review/SKILL.md        → Persistent context
│   ├── morning-brief/SKILL.md         → CPA, hook rates, rejections, delivery
│   ├── waste-detector/SKILL.md        → 6 TikTok-specific waste categories → action plan
│   ├── account-scorecard/SKILL.md     → Quantified health grade [NEW]
│   ├── creative-pulse/SKILL.md        → Hook rate analysis, lifecycle classification, velocity [KEY DIFFERENTIATOR]
│   └── trend-scout/SKILL.md           → Competitor ads + trending formats research [NEW]
├── hooks/
│   ├── inject-profile.sh             → Load account profile at session start
│   └── update-profile.py             → Save watch list / decision log at session end
└── references/
    ├── creative-benchmarks.md         → Hook rate, completion rate, CTR by vertical
    ├── thresholds.md                  → TikTok-specific anomaly thresholds
    ├── creative-lifecycle.md          → Testing → Scaling → Mature → Fatiguing → Dead framework
    └── ui-paths.md                    → TikTok Ads Manager UI navigation reference [NEW]
```

---

## 5. LINKEDIN ADS PLUGIN

### MCP Decision

| MCP | Tools | Auth | Verdict |
|-----|-------|------|---------|
| **danielpopamd/linkedin-ads-mcp** | 14 tools: accounts, campaigns, creatives, audiences, conversions, analytics. Human-readable demographic data. | OAuth, auto-refresh | **Primary choice.** Most complete. |
| **radiateb2b/mcp-linkedin-ads** | Performance analysis + benchmark comparison + company-level engagement | API key (GBP 50/mo after trial) | Benchmark comparison is unique. Paid — note as premium alternative. |

**Recommendation:** danielpopamd/linkedin-ads-mcp. No official LinkedIn MCP exists.

### Practitioner Workflows → Existing Tools

**LinkedIn is audience architecture + lead quality optimization.** The most expensive platform — every click costs $5-20.

#### WEEKLY

| Workflow | What Practitioners Do | Existing Tool | Read-Only Output |
|----------|----------------------|---------------|-----------------|
| **Lead quality review** | Download leads, cross-reference with ICP, mark qualified vs. junk | MCP query (lead gen form data) | Lead quality scoring with ICP match analysis. True CPL (qualified) vs. reported CPL. |
| **Campaign Demographics** | Check WHO actually engaged — right titles? Right companies? | MCP query (demographic breakdown) | Include in morning-brief — flag misaligned demographics |
| **Frequency monitoring** | B2B audiences are small, frequency >8 = exhaustion | MCP query (frequency metrics) | Include in waste-detector |

#### MONTHLY

| Workflow | What Practitioners Do | Existing Tool | Gap? |
|----------|----------------------|---------------|------|
| **Full funnel review** | Impressions → clicks → leads → MQLs → SQLs → pipeline | MCP query + CRM data | Write funnel-review SKILL.md |
| **True CPL calculation** | Not just LinkedIn's reported CPL — cost per QUALIFIED lead | MCP query + manual input | Include in lead-quality |
| **ABM engagement reporting** | Which target accounts engaged this month | MCP query (company-level engagement) | Write abm-report SKILL.md |

#### LINKEDIN-SPECIFIC WASTE CATEGORIES

1. **Audience Network enabled by default** — dramatically lower quality
2. **Geo "Recent or Permanent"** — includes travelers, wastes budget
3. **Job seekers + students** — high engagement, zero value
4. **Too-small audiences** — <50K creates artificial scarcity
5. **InMail to C-levels** — executives don't respond; directors/managers do
6. **Single-image fatigue** — same creative >30 days
7. **Frequency ceiling** — >8 on small B2B audiences

### Recommended Plugin Assembly

```
linkedin-ads/
├── .mcp.json                          → danielpopamd/linkedin-ads-mcp (pinned version)
├── skills/
│   ├── platform-setup/SKILL.md        → Verify credentials, discover accounts
│   ├── profile-review/SKILL.md        → Persistent context
│   ├── morning-brief/SKILL.md         → Spend, CPL, delivery, demographic check
│   ├── waste-detector/SKILL.md        → 7 LinkedIn-specific waste categories → action plan
│   ├── account-scorecard/SKILL.md     → Quantified health grade [NEW]
│   ├── lead-quality/SKILL.md          → Lead quality scoring, ICP match analysis [KEY DIFFERENTIATOR]
│   ├── b2b-targeting/SKILL.md         → Audience analysis by function/seniority/industry [NEW]
│   └── abm-report/SKILL.md           → Target account engagement summary [NEW]
├── hooks/
│   ├── inject-profile.sh             → Load account profile at session start
│   └── update-profile.py             → Save watch list / decision log at session end
└── references/
    ├── benchmarks.md                  → LinkedIn CPL/CPC/CTR benchmarks by industry
    ├── thresholds.md                  → LinkedIn-specific anomaly thresholds
    ├── targeting-guide.md             → Job title vs. function+seniority tradeoffs
    └── ui-paths.md                    → LinkedIn Campaign Manager UI navigation reference [NEW]
```

---

## 6. AMAZON ADS PLUGIN

### MCP Decision

| MCP | Read Tools | Auth | Verdict |
|-----|-----------|------|---------|
| **Amazon Ads Official MCP** (open beta) | Performance, reporting, billing, account settings. Multi-country support. | Amazon Ads API credentials | **Primary choice.** First-party, production-grade. The only official ad platform MCP with read+write (we use read only). |
| **KuudoAI/amazon_ads_mcp** | Campaign Mgmt v1, Exports, AMC, DSP | Direct API + OpenBridge OAuth | DSP + AMC coverage that official MCP may not have. Optional companion. |

**Recommendation:** Amazon Official MCP as primary. KuudoAI as optional companion for DSP/AMC. Amazon's MCP is the gold standard — the only official ad platform MCP that's actively developed and feature-rich. We use its read capabilities only.

### Practitioner Workflows → Existing Tools

**Amazon PPC is the most operationally dense — data-heavy, spreadsheet-heavy, process-driven.**

#### WEEKLY (the core loop)

| Workflow | What Practitioners Do | Existing Tool | Read-Only Output |
|----------|----------------------|---------------|-----------------|
| **Search term harvesting** | Pull SQR, find converting terms, graduate to exact match, negate in auto | MCP report + classify | Graduation report: terms ready for exact match, terms to negate, terms to monitor. CSV export for Campaign Manager bulk upload. |
| **Negative keyword pruning** | High-spend/zero-conv terms → add as negatives | MCP report | Negative list with match types, grouped by campaign. Copy-paste ready. |
| **Placement report** | Top of Search vs. Rest of Search vs. Product Pages | MCP report (placement metrics) | Include in morning-brief — flag product page placements with <0.05% CTR |

#### MONTHLY

| Workflow | What Practitioners Do | Existing Tool | Gap? |
|----------|----------------------|---------------|------|
| **ACoS/TACoS trend analysis** | Is ad dependency increasing or decreasing? | MCP report (ACoS trends) | Write acos-optimizer SKILL.md |
| **Campaign structure audit** | Any ASINs without proper coverage? Match type gaps? | MCP query (full structure) | Include in account-scorecard |
| **Organic rank tracking** | Is PPC driving organic improvement? | No MCP for organic rank | **Gap** — use external tools |

#### AMAZON-SPECIFIC WASTE CATEGORIES

1. **Not negating harvested keywords** — bidding against yourself in auto + manual
2. **Broad match without negatives** — Amazon matches aggressively
3. **Ignoring placement data** — product page placements with 0.03% CTR eating budget
4. **Campaigns not separated by ASIN** — optimization impossible
5. **Amazon's inflated recommended bids** — always start 50% lower
6. **Branded overspend** — paying for clicks on own brand terms
7. **SP Brands/Display before SP optimized** — cart before horse

### Recommended Plugin Assembly

```
amazon-ads/
├── .mcp.json                          → Amazon Official MCP (primary, pinned version)
│                                        + KuudoAI/amazon_ads_mcp (DSP/AMC, optional)
├── skills/
│   ├── platform-setup/SKILL.md        → Verify credentials, discover profiles/marketplaces
│   ├── profile-review/SKILL.md        → Persistent context (marketplace-aware)
│   ├── morning-brief/SKILL.md         → ACoS, spend pacing, ASIN-level performance, placement flags
│   ├── waste-detector/SKILL.md        → 7 Amazon-specific waste categories → action plan
│   ├── account-scorecard/SKILL.md     → Quantified health grade [NEW]
│   ├── keyword-harvester/SKILL.md     → Auto→exact graduation pipeline with CSV export [KEY DIFFERENTIATOR]
│   ├── acos-optimizer/SKILL.md        → ACoS/TACoS trend analysis + bid recommendations [NEW]
│   └── campaign-structure/SKILL.md    → Validate auto/broad/exact pipeline per ASIN [NEW]
├── hooks/
│   ├── inject-profile.sh             → Load account profile at session start
│   └── update-profile.py             → Save watch list / decision log at session end
└── references/
    ├── harvesting-workflow.md         → The auto→broad→exact graduation pipeline
    ├── thresholds.md                  → ACoS targets by product lifecycle stage
    ├── campaign-structure-guide.md    → 4-campaign framework (auto, research, performance, product targeting)
    └── ui-paths.md                    → Amazon Ads Console UI navigation reference [NEW]
```

---

## 7. REDDIT ADS PLUGIN

### MCP Decision

| MCP | Read Tools | Auth | Verdict |
|-----|-----------|------|---------|
| **sbmeaper/reddit-ad-mcp** | 5 read-only tools | OAuth 2.0 | **Primary choice.** Safe, read-only by design. |
| **mkerchenski/RedditAdsMcp** | 6 read-only tools | OAuth 2.0 (.NET) | Alternative if .NET is preferred. |

**Recommendation:** sbmeaper/reddit-ad-mcp. No official Reddit MCP exists.

### Key Insight: Reddit ads are fundamentally different

- **80%+ of clicks may be bots** (multiple practitioners report this)
- **Reddit users hate marketing** — native-looking content required
- **Better for awareness/retargeting than direct response**
- **Subreddit (community) targeting is the primary lever**

### Practitioner Workflows → Existing Tools

| Workflow | What Practitioners Do | Existing Tool | Read-Only Output |
|----------|----------------------|---------------|-----------------|
| **Bot traffic monitoring** | Compare Reddit clicks vs. actual site sessions | MCP report + GA4 MCP cross-reference | Bot score: Reddit clicks vs GA4 sessions ratio. Flag when >50% discrepancy. |
| **Comment moderation** | Free-Form ads need active moderation | No MCP for comment management | **Gap** |
| **Subreddit performance** | Which communities convert vs. waste budget | MCP report (by subreddit) | Include in waste-detector — rank subreddits by efficiency, flag underperformers |
| **Creative authenticity check** | Verify ads look native, not corporate | No automated tool | Manual guidance in SKILL.md |

### Recommended Plugin Assembly

```
reddit-ads/
├── .mcp.json                          → sbmeaper/reddit-ad-mcp (read-only, pinned version)
├── skills/
│   ├── platform-setup/SKILL.md        → Verify credentials
│   ├── morning-brief/SKILL.md         → CPC, CTR, subreddit performance, bot traffic flag
│   ├── waste-detector/SKILL.md        → 5 Reddit-specific waste categories → action plan
│   ├── community-targeting/SKILL.md   → Subreddit performance analysis, expansion recommendations [NEW]
│   └── bot-detector/SKILL.md          → Cross-reference Reddit clicks vs. GA4 sessions [KEY DIFFERENTIATOR]
├── hooks/
│   ├── inject-profile.sh             → Load account profile at session start
│   └── update-profile.py             → Save watch list / decision log at session end
└── references/
    ├── creative-guide.md              → Native-looking content best practices, Redditisms
    ├── thresholds.md                  → Reddit-specific benchmarks (CTR 0.2-0.3%, CPC $0.10-0.80)
    └── subreddit-categories.md        → High-converting subreddit categories by vertical
```

---

## 8. APPLE SEARCH ADS PLUGIN

### MCP Decision

| MCP | Read Tools | Auth | Verdict |
|-----|-----------|------|---------|
| **appleadsmcp.com** | Campaign performance, keyword analysis, search terms | Apple Search Ads API | **Primary choice.** Free read tier (100 API calls/day). Has built-in search term harvesting. Note: third-party commercial product, NOT from Apple. |

**Recommendation:** appleadsmcp.com (free read tier). No official Apple MCP exists. Paid tier ($99/mo) adds write access and 1,000 calls/day — unnecessary since we're read-only, but more daily calls could matter for larger accounts.

### Complementary ASO Tools

| Tool | What It Does | URL |
|------|-------------|-----|
| **Eronred/aso-skills** | Keyword research, metadata optimization, competitor analysis | github.com/Eronred/aso-skills |
| **dock-aso/aso-optimizer-skill** | Comprehensive ASO toolkit, multi-language localization | github.com/dock-aso/aso-optimizer-skill |
| **appreply-co/mcp-appstore** | 17 tools for App Store + Google Play analysis | github.com/appreply-co/mcp-appstore |

### Practitioner Workflows → Existing Tools

| Workflow | What Practitioners Do | Existing Tool | Read-Only Output |
|----------|----------------------|---------------|-----------------|
| **Search Match mining** | Download search terms, promote winners to exact, negate losers | appleadsmcp.com (has automated harvesting) | Graduation report: terms for exact match, terms to negate. Similar to Amazon keyword-harvester. |
| **Bid ladder adjustments** | Systematic CPT adjustments based on CPA vs. target | MCP + bid-ladder logic in SKILL.md | Bid recommendation table: current CPT, actual CPA, target CPA, recommended CPT, change %, UI path. |
| **Custom Product Page testing** | Match CPP creative to keyword intent | Apple Ads API (CPP management) | Performance by CPP with recommendations for intent matching. |
| **Cross-campaign negative management** | Prevent Discovery from cannibalizing Performance | MCP + keyword cross-reference | Conflict report: keywords appearing in multiple campaign pillars, with resolution recommendation. |

### Recommended Plugin Assembly

```
apple-search-ads/
├── .mcp.json                          → appleadsmcp.com MCP (pinned version)
│                                        + appreply-co/mcp-appstore (ASO companion)
├── skills/
│   ├── platform-setup/SKILL.md        → Verify Apple API credentials
│   ├── morning-brief/SKILL.md         → CPT, CVR, CPA by campaign pillar (brand/category/competitor/discovery)
│   ├── waste-detector/SKILL.md        → 8 Apple SA-specific waste categories → action plan
│   ├── keyword-harvester/SKILL.md     → Discovery→exact graduation report
│   ├── bid-optimizer/SKILL.md         → Bid ladder framework with recommendation table [NEW]
│   └── campaign-hygiene/SKILL.md      → Cross-campaign negative management [NEW]
├── hooks/
│   ├── inject-profile.sh             → Load account profile at session start
│   └── update-profile.py             → Save watch list / decision log at session end
└── references/
    ├── four-campaign-structure.md     → Brand Defense / Category / Competitor / Discovery framework
    ├── bid-ladder.md                  → Systematic CPT adjustment rules
    ├── waste-categories.md            → 8 waste patterns with thresholds
    └── ui-paths.md                    → Apple Search Ads UI navigation reference [NEW]
```

---

## Build Order

### Phase 1: Split + Ship
1. **google-ads** — Extract from paid-search, adapt skills for read-only output (action plans instead of mutations), add new skills (ad-copy-analyzer, account-scorecard, competitor-intel)
2. **microsoft-ads** — Extract from paid-search, adapt for read-only, add Bing-specific skills (import-auditor, placement-cleaner, account-scorecard)
3. **meta-ads** — Build from skeleton using Pipeboard MCP + meta-ads-analyzer, creative-fatigue as key differentiator

### Phase 2: Social Expansion
4. **tiktok-ads** — Build with ysntony MCP + creative-pulse as differentiator
5. **linkedin-ads** — Build with danielpopamd MCP + lead-quality as differentiator

### Phase 3: Commerce + Niche
6. **amazon-ads** — Build with Amazon Official MCP + keyword-harvester as differentiator
7. **reddit-ads** — Build with sbmeaper MCP + bot-detector as differentiator
8. **apple-search-ads** — Build with appleadsmcp + bid-optimizer as differentiator

---

## What We're NOT Building (because others did it better)

| Need | Don't Build | Use Instead |
|------|-------------|-------------|
| Cross-platform audit framework | New audit skills | **claude-ads** by AgriciDaniel (652 stars, 186 checks) |
| Marketing skills (CRO, copy, email) | Marketing skills | **marketingskills** by coreyhaines31 (10,890 stars) |
| Meta Ads Learning Phase analysis | Learning phase skill | **meta-ads-analyzer** by mathiaschu (215 stars) |
| Competitive ad research | Ad library skills | **trypeggy/facebook-ads-library-mcp** + **talknerdytome-labs agents** |
| Shopping feed optimization | Feed tools | **feedgen** by google-marketing-solutions (237 stars) |
| PMax reporting | PMax script | **agencysavvy/pmax** (276 stars) |
| GAQL reference | GAQL skill | **@channel47/skills/gaql** (already built) |
| GA4 analysis | Analytics MCP | **Official GA4 MCP** (1,389 stars) |
| GTM management | Tag manager tools | **stape-io/google-tag-manager-mcp-server** |
| ASO | ASO skills | **Eronred/aso-skills** + **dock-aso/aso-optimizer-skill** |

---

## What We ARE Building (because nobody else has)

| Plugin | Key Differentiator | Why It Doesn't Exist Yet |
|--------|-------------------|--------------------------|
| **google-ads** | Practitioner-grade morning brief + waste detector with $$ quantification + prioritized action plans with UI paths | MCPs exist but no opinionated *workflow* skills with actionable output |
| **microsoft-ads** | Import auditor + MSAN placement cleaner + Bing-specific waste detection | Nobody treats Bing as a first-class citizen |
| **meta-ads** | Creative fatigue lifecycle classification with "days remaining" estimates | Commercial tools (Motion, Bestever) charge $500+/mo for this |
| **tiktok-ads** | Creative pulse with hook rate analysis + creative velocity tracking | TikTok MCP tools exist but no creative intelligence layer |
| **linkedin-ads** | Lead quality scoring + ABM engagement reporting | LinkedIn MCPs exist but no B2B workflow intelligence |
| **amazon-ads** | Keyword harvester with auto→exact graduation pipeline + CSV export | Amazon's official MCP has raw tools but no harvesting workflow |
| **reddit-ads** | Bot detector + community targeting analysis | Reddit MCPs exist but nobody addresses the bot traffic problem |
| **apple-search-ads** | Bid ladder framework + campaign hygiene (cross-campaign negatives) | Apple SA tooling is the thinnest of all platforms |

---

## Resolved Decisions

### 1. MCP bundling vs. referencing
**Decision: Bundle in `.mcp.json` with pinned versions.** The whole value proposition is "install one plugin, get a working toolkit." Pin exact versions (e.g., `cohnen/mcp-google-ads@1.2.3`) to control the supply chain. Bump pinned versions after testing when upstream MCPs release updates.

### 2. claude-ads integration
**Decision: Reference as a companion, don't fork.** Forking 186 checks creates a maintenance nightmare. Reference it: "For a comprehensive 60+ point audit, install claude-ads." Our skills handle daily/weekly workflows — claude-ads handles quarterly deep audits. Different cadences, complementary tools.

### 3. Versioning strategy
**Decision: Pin versions + quarterly dependency review.** Pin exact versions in `.mcp.json`. Run a quarterly check to see if upstream MCPs released new versions. Bump after testing. Document upstream MCPs and their repos in a `DEPENDENCIES.md` for easy tracking.

### 4. Profile format
**Decision: Shared base format, platform-specific extensions.** Common structure (`account-profile.md` with sections: Account IDs, KPI Targets, Watch List, Active Tests, Decision Log) that all plugins read. Each platform adds its own fields (e.g., Google adds `developer_token_tier`, Meta adds `pixel_id`, Amazon adds `marketplace`). Plugins ignore fields they don't recognize.

### 5. Paid tiers
**Decision: Only recommend free/open-source tools as defaults.** Every default MCP recommendation is free and open-source. Paid tools (radiateb2b, appleadsmcp.com premium) get a single line: "Premium alternative: [tool] — adds [specific feature] for $X/mo." Never make a paid tool the only option.

### 6. Read-only constraint
**Decision: Hard constraint, not temporary.** No mutations in any plugin. Skills produce action plans with dollar-quantified impact, exact UI navigation paths, and copy-paste artifacts. The trust story ("zero risk to your accounts") is more valuable than automation convenience.

### 7. Credential security model
**Decision: Local stdio only for all plugins.** MCP servers run locally via stdio. Credentials stay in user's environment variables. No data flows to Ch47 or any third party. Document the trust model explicitly in each plugin's README. Exception: Pipeboard's Meta MCP is remote — note this and offer brijr/meta-mcp as a local alternative.
