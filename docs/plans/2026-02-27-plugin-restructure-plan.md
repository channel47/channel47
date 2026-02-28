# Plugin Restructure Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Restructure the monolithic media-buyer plugin into a paid-search plugin (refactored) and a meta-ads plugin (skeleton).

**Architecture:** Platform-native, self-contained plugins. Each owns its MCP servers, hooks, and skills. No cross-plugin dependencies. Universal skills (morning-brief, waste-detector, platform-setup) exist independently in each plugin with platform-specific implementations.

**Tech Stack:** Claude Code plugins (SKILL.md, plugin.json, .mcp.json, hooks.json)

**Design doc:** `docs/plans/2026-02-27-plugin-restructure-design.md`

---

## Phase 1: Refactor media-buyer → paid-search

### Task 1: Rename directory and update plugin.json

**Files:**
- Rename: `plugins/media-buyer/` → `plugins/paid-search/`
- Modify: `plugins/paid-search/.claude-plugin/plugin.json`

**Step 1: Rename the directory**

```bash
cd /Users/jackson/Documents/a_projects/ch47/plugins
mv plugins/media-buyer plugins/paid-search
```

**Step 2: Update plugin.json**

Replace contents of `plugins/paid-search/.claude-plugin/plugin.json` with:

```json
{
  "name": "paid-search",
  "version": "7.0.0",
  "description": "Paid search toolkit for Google Ads and Bing Ads — setup, reporting, analysis, and guarded mutations via MCP.",
  "author": {
    "name": "Jackson Dean",
    "url": "https://channel47.dev"
  },
  "homepage": "https://channel47.dev/plugins/paid-search",
  "repository": "https://github.com/channel47/plugins",
  "keywords": [
    "google-ads",
    "bing-ads",
    "microsoft-advertising",
    "paid-search",
    "ppc",
    "search-ads",
    "campaign-management",
    "ad-reporting",
    "search-term-analysis",
    "waste-detection",
    "performance-max",
    "anomaly-detection"
  ],
  "license": "MIT"
}
```

Changes: name → paid-search, version → 7.0.0 (major bump for rename), description updated, homepage updated, keywords swapped media-buying/ad-platform for paid-search/search-ads.

**Step 3: Verify**

```bash
cat plugins/paid-search/.claude-plugin/plugin.json | python3 -m json.tool
```

Expected: Valid JSON, name = "paid-search"

---

### Task 2: Update SKILL.md descriptions for paid-search context

**Files:**
- Modify: `plugins/paid-search/skills/platform-setup/SKILL.md`
- Modify: `plugins/paid-search/skills/morning-brief/SKILL.md`
- Modify: `plugins/paid-search/skills/waste-detector/SKILL.md`
- Modify: `plugins/paid-search/skills/search-term-verdict/SKILL.md`
- Modify: `plugins/paid-search/skills/pmax-decoder/SKILL.md`

**Step 1: Update platform-setup SKILL.md frontmatter**

In `skills/platform-setup/SKILL.md`, update the `description` field:

```yaml
description: >-
  This skill should be used when the user asks to "connect to Google Ads",
  "set up Bing", "verify connection", "configure my search ad accounts",
  "set up Microsoft Advertising", "check my paid search access", or
  "connect my paid search platforms".
```

No changes to the body — it's already scoped to Google + Bing.

**Step 2: Update morning-brief SKILL.md frontmatter**

In `skills/morning-brief/SKILL.md`, update the `description` field:

```yaml
description: >-
  This skill should be used when the user asks for a "morning brief",
  "daily check", "what happened overnight", "paid search health check",
  "what should I worry about", "how are my search campaigns doing",
  "daily summary", "search performance check", or mentions daily
  monitoring, anomaly detection, or paid search account health.
```

In the body, update the h1 heading:

```markdown
# Paid Search Morning Brief
```

And update the first line:

```markdown
Produce a daily, prioritized account-health narrative across Google Ads and Bing Ads paid search campaigns with actionable items.
```

**Step 3: Update waste-detector SKILL.md frontmatter**

In `skills/waste-detector/SKILL.md`, update the `description` field:

```yaml
description: >-
  This skill should be used when the user asks to "find search waste",
  "audit my search account", "where am I wasting search budget",
  "paid search audit", "find wasted spend", "check for waste",
  "search money leaks", "paid search health", "what's costing me money
  in search", "optimization opportunities", or mentions paid search
  optimization, search spend analysis, or budget efficiency.
```

In the body, update the h1 heading:

```markdown
# Paid Search Waste Detector
```

And update the first line:

```markdown
Scan Google Ads and Bing Ads paid search accounts for the most common spend leaks and quantify each leak in dollars with an action plan.
```

**Step 4: Update search-term-verdict SKILL.md frontmatter**

No changes needed — already fully search-scoped.

**Step 5: Update pmax-decoder SKILL.md frontmatter**

No changes needed — already Google-only and search-adjacent.

**Step 6: Verify no "media-buyer" or "media buyer" strings remain**

```bash
cd /Users/jackson/Documents/a_projects/ch47/plugins
grep -ri "media.buyer" plugins/paid-search/skills/ --include="*.md"
```

Expected: No results.

---

### Task 3: Remove image-gen stub

**Files:**
- Delete: `plugins/paid-search/skills/image-gen/` (entire directory)

**Step 1: Remove the stub**

```bash
rm -rf /Users/jackson/Documents/a_projects/ch47/plugins/plugins/paid-search/skills/image-gen
```

**Step 2: Verify**

```bash
ls /Users/jackson/Documents/a_projects/ch47/plugins/plugins/paid-search/skills/
```

Expected: platform-setup, morning-brief, waste-detector, search-term-verdict, pmax-decoder (no image-gen)

---

### Task 4: Update README

**Files:**
- Modify: `plugins/paid-search/README.md`

**Step 1: Rewrite README**

Replace entire contents of `plugins/paid-search/README.md` with:

```markdown
# Paid Search — Claude Code Plugin

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Paid search toolkit for Google Ads and Bing Ads — setup, reporting, analysis, and guarded mutations via MCP.

Built from managing 25+ ad accounts daily. Part of [Channel 47](https://channel47.dev), the open-source ecosystem of profession plugins for Claude Code. [Get the newsletter](https://channel47.dev/subscribe) for weekly skill breakdowns from production use.

---

## Install

```bash
/plugin marketplace add channel47/plugins
/plugin install paid-search@channel47
```

---

## Version

Current: **7.0.0**

---

## Configuration

The plugin bundles two MCP servers via `.mcp.json`. Set these environment variables in your shell profile:

### Google Ads (required for Google features)

| Variable | Required |
|----------|----------|
| `GOOGLE_ADS_DEVELOPER_TOKEN` | Yes |
| `GOOGLE_ADS_CLIENT_ID` | Yes |
| `GOOGLE_ADS_CLIENT_SECRET` | Yes |
| `GOOGLE_ADS_REFRESH_TOKEN` | Yes |
| `GOOGLE_ADS_LOGIN_CUSTOMER_ID` | For MCC accounts |

### Bing Ads (required for Bing features)

| Variable | Required |
|----------|----------|
| `BING_ADS_DEVELOPER_TOKEN` | Yes |
| `BING_ADS_CLIENT_ID` | Yes |
| `BING_ADS_REFRESH_TOKEN` | Yes |
| `BING_ADS_CUSTOMER_ID` | For manager accounts |
| `BING_ADS_ACCOUNT_ID` | Default account |

Both MCP servers install automatically via `npx` — no separate setup. Configure one platform or both — skills gracefully adapt to whatever's available.

---

## What's Inside

```text
paid-search/
├── .claude-plugin/
│   └── plugin.json
├── .mcp.json              # Google Ads + Bing Ads MCP servers
├── hooks/
│   ├── hooks.json
│   └── validate-mutations.py
├── skills/
│   ├── platform-setup/
│   ├── morning-brief/
│   ├── waste-detector/
│   ├── search-term-verdict/
│   └── pmax-decoder/
├── tests/
├── README.md
└── LICENSE
```

---

## Skills

### platform-setup

Setup and verification for Google Ads and Bing Ads credentials. Validates API access via `mcp__google-ads__list_accounts` and `mcp__bing-ads__list_accounts`.

### morning-brief

Daily paid search account-health summary. Pulls data from both Google and Bing, detects anomalies, assesses budget pacing, and produces a unified Urgent/Watch/Healthy narrative.

### waste-detector

Finds high-impact spend leaks across Google and Bing search campaigns. Quantifies waste in dollars, ranks by impact, and prepares remediation — automated mutations for Google, manual action items for Bing.

### search-term-verdict

Classifies search terms from both platforms into NEGATE/PROMOTE/INVESTIGATE/KEEP verdicts. Builds negative keyword packages with cross-platform pattern detection.

### pmax-decoder

Cracks open Performance Max campaign transparency data. Google Ads only. Analyzes search terms, channel distribution, asset performance, brand traffic, and placements.

---

## Safety Model

Every write operation follows the same protocol:

1. Query and analyze first.
2. Preview mutations with `dry_run: true`.
3. Request explicit user approval.
4. Execute with `dry_run: false` only after approval.

`hooks/validate-mutations.py` intercepts both `mcp__google-ads__mutate` and `mcp__bing-ads__mutate` to enforce this.

---

## Try It

- "Set up and verify my Google and Bing accounts."
- "Give me this morning's paid search brief."
- "Find where I'm wasting search budget."
- "Review search terms and draft negatives for Google and Bing."
- "Decode what my PMax campaign is actually doing."

---

## Links

- [Channel 47](https://channel47.dev) — open-source profession plugins for Claude Code
- [Build Notes](https://channel47.dev/subscribe) — weekly skill breakdowns from production use
- [MCP Servers](https://github.com/channel47/mcps) — the Google Ads and Bing Ads MCPs this plugin uses

## License

MIT
```

---

### Task 5: Update repo-level CLAUDE.md

**Files:**
- Modify: `/Users/jackson/Documents/a_projects/ch47/plugins/CLAUDE.md`

**Step 1: Update references from media-buyer to paid-search**

In the Structure section, update the tree and description:

```
plugins/
  paid-search/                    # Google Ads + Bing Ads paid search toolkit (v7.0.0)
```

Update plugin install command:

```
/plugin install paid-search@channel47
```

Update the Vision line to mention paid-search instead of media-buyer.

---

### Task 6: Update tests

**Files:**
- Modify: `plugins/paid-search/tests/*.py`

**Step 1: Check test files for "media-buyer" references**

```bash
grep -ri "media.buyer" /Users/jackson/Documents/a_projects/ch47/plugins/plugins/paid-search/tests/
```

**Step 2: Replace any "media-buyer" or "media_buyer" references with "paid-search" or "paid_search"**

Update test file names if they reference media-buyer. Update string literals in test assertions.

**Step 3: Run tests to verify**

```bash
cd /Users/jackson/Documents/a_projects/ch47/plugins/plugins/paid-search
python3 -m pytest tests/ -v
```

Expected: All tests pass with updated references.

---

### Task 7: Commit Phase 1

```bash
cd /Users/jackson/Documents/a_projects/ch47/plugins
git add plugins/paid-search/ CLAUDE.md
git add -u  # catch the deletion of media-buyer/
git commit -m "refactor: rename media-buyer to paid-search

Rename plugin to match platform scope. Update plugin.json (v7.0.0),
all SKILL.md descriptions, README, repo CLAUDE.md, and tests.
Remove image-gen stub.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

## Phase 2: Scaffold meta-ads skeleton

### Task 8: Create meta-ads directory structure

**Step 1: Create all directories**

```bash
cd /Users/jackson/Documents/a_projects/ch47/plugins/plugins
mkdir -p meta-ads/.claude-plugin
mkdir -p meta-ads/hooks
mkdir -p meta-ads/skills/platform-setup/references
mkdir -p meta-ads/skills/morning-brief/references
mkdir -p meta-ads/skills/waste-detector/references
mkdir -p meta-ads/skills/creative-analyzer/references
mkdir -p meta-ads/skills/audience-builder/references
```

**Step 2: Verify**

```bash
find plugins/meta-ads -type d | sort
```

Expected: All directories created.

---

### Task 9: Write meta-ads plugin.json

**Files:**
- Create: `plugins/meta-ads/.claude-plugin/plugin.json`

```json
{
  "name": "meta-ads",
  "version": "0.1.0",
  "description": "Meta Ads toolkit for Facebook and Instagram — creative analysis, audience building, reporting, and campaign optimization via MCP.",
  "author": {
    "name": "Jackson Dean",
    "url": "https://channel47.dev"
  },
  "homepage": "https://channel47.dev/plugins/meta-ads",
  "repository": "https://github.com/channel47/plugins",
  "keywords": [
    "meta-ads",
    "facebook-ads",
    "instagram-ads",
    "social-ads",
    "demand-generation",
    "creative-testing",
    "audience-targeting",
    "lookalike-audiences",
    "campaign-management",
    "ad-reporting",
    "creative-fatigue",
    "cpm-optimization"
  ],
  "license": "MIT"
}
```

---

### Task 10: Write meta-ads .mcp.json placeholder

**Files:**
- Create: `plugins/meta-ads/.mcp.json`

```json
{
  "meta-ads": {
    "command": "npx",
    "args": ["-y", "@channel47/meta-ads-mcp@latest"],
    "env": {
      "META_ADS_ACCESS_TOKEN": "${META_ADS_ACCESS_TOKEN}",
      "META_ADS_APP_ID": "${META_ADS_APP_ID}",
      "META_ADS_APP_SECRET": "${META_ADS_APP_SECRET}",
      "META_ADS_ACCOUNT_ID": "${META_ADS_ACCOUNT_ID}"
    }
  }
}
```

Note: `@channel47/meta-ads-mcp` does not exist yet. This is a placeholder for future development.

---

### Task 11: Write meta-ads hooks

**Files:**
- Create: `plugins/meta-ads/hooks/hooks.json`
- Create: `plugins/meta-ads/hooks/validate-mutations.py`

**Step 1: Write hooks.json**

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "mcp__meta-ads__mutate",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PLUGIN_ROOT}/hooks/validate-mutations.py",
            "timeout": 5
          }
        ]
      }
    ]
  }
}
```

**Step 2: Write validate-mutations.py**

Copy from paid-search and simplify (remove Bash path since meta-ads won't have legacy scripts):

```python
#!/usr/bin/env python3
"""
PreToolUse hook: Flag live mutations before execution.

Checks mcp__meta-ads__mutate calls for dry_run parameter.
Queries and dry-run mutations pass through silently.
"""
import json
import sys


def main():
    input_data = json.load(sys.stdin)
    tool_name = input_data.get("tool_name", "")
    tool_input = input_data.get("tool_input", {})

    if "mutate" in tool_name.lower():
        if not tool_input.get("dry_run", True):
            print(json.dumps({
                "decision": "allow",
                "message": "LIVE MUTATION: dry_run=false. Changes will be permanent."
            }))
            return
        print(json.dumps({"decision": "allow"}))
        return

    print(json.dumps({"decision": "allow"}))


if __name__ == "__main__":
    main()
```

---

### Task 12: Write meta-ads SKILL.md files — platform-setup

**Files:**
- Create: `plugins/meta-ads/skills/platform-setup/SKILL.md`

```markdown
---
name: platform-setup
description: >-
  This skill should be used when the user asks to "connect to Meta Ads",
  "set up Facebook Ads", "configure Instagram Ads", "verify Meta connection",
  "set up my Meta ad account", or "check my Meta Ads access".
allowed-tools: mcp__meta-ads__list_accounts
---

# Platform Setup

Configure Meta Ads credentials and verify account access.

## Status

Skeleton — requires `@channel47/meta-ads-mcp` to be built and published before this skill is functional.

## Workflow

### Step 1: Identify setup requirements

Guide the user through:
- Meta Business Manager account access
- App creation in Meta for Developers
- Access token generation (long-lived token)
- Pixel and Conversions API (CAPI) verification

### Step 2: Configure environment variables

Set in `.claude/settings.local.json` or shell profile:
- `META_ADS_ACCESS_TOKEN`
- `META_ADS_APP_ID`
- `META_ADS_APP_SECRET`
- `META_ADS_ACCOUNT_ID`

### Step 3: Verify access

Run `mcp__meta-ads__list_accounts` and report:
- Whether account listing succeeds
- Which ad account IDs and names are visible
- Any missing credentials or auth failures

## Guardrails

- Never ask users to paste secrets into chat logs.
- Recommend `.claude/settings.local.json` (gitignored) for credentials.

## References

- `references/` — to be populated when MCP server is built
```

---

### Task 13: Write meta-ads SKILL.md files — morning-brief

**Files:**
- Create: `plugins/meta-ads/skills/morning-brief/SKILL.md`

```markdown
---
name: morning-brief
description: >-
  This skill should be used when the user asks for a "Meta morning brief",
  "Facebook ads daily check", "how are my Meta campaigns doing",
  "Instagram ads performance", "Meta account health", "social ads daily
  summary", or mentions Meta Ads monitoring, Facebook campaign health,
  or social ads anomaly detection.
allowed-tools: mcp__meta-ads__query, mcp__meta-ads__list_accounts
---

# Meta Ads Morning Brief

Produce a daily, prioritized account-health narrative for Meta Ads (Facebook + Instagram) with actionable items.

## Status

Skeleton — requires `@channel47/meta-ads-mcp` to be built and published before this skill is functional.

## Key Metrics (differ from paid search)

- **CPM** (cost per thousand impressions) — primary cost metric
- **Frequency** — ad fatigue signal (flag when >3.0 in 7d)
- **CTR** — click-through rate
- **CPA / ROAS** — conversion efficiency
- **Relevance Score / Quality Ranking** — Meta's ad quality indicators
- **Hook Rate** — % of video viewers past 3 seconds
- **ThruPlay Rate** — % of video viewers to completion

## Workflow

### Phase 1: Collect data

Query Meta Ads API for:
1. Campaign daily performance (30d) — spend, impressions, CPM, clicks, CTR, conversions, CPA, ROAS
2. Ad set frequency and delivery status
3. Ad-level performance with creative breakdown
4. Account-level spend pacing

### Phase 2: Detect anomalies

Same anomaly detection framework as paid-search:
- Baseline: 7d and 30d windows
- Flag when `|deviation_pct| > 0.20` AND `|dollar_impact| > $10`
- Additional Meta-specific flag: frequency > 3.0 in any ad set

### Phase 3: Budget pacing

- Daily budget and lifetime budget tracking
- Campaign budget optimization (CBO) vs ad set budgets
- Flag overpacing (>1.10) and underpacing (<0.85)

### Phase 4: Draft prioritized narrative

Structure: Urgent / Watch / Healthy with platform label and concrete next actions.

## Output format

Same contract as paid-search morning-brief:
```
## Morning Brief - [Date]
### Platforms
### Urgent
### Watch
### Healthy
### Notes
```

## Guardrails

- Creative fatigue: flag when frequency > 3.0 and CTR declining
- Attribution window: note Meta's default 7-day click / 1-day view window
- iOS privacy impact: note potential underreporting from ATT opt-outs
- Learning phase: do not flag campaigns in learning phase (<50 conversions/week) as underperforming

## References

- `references/` — to be populated when MCP server is built
```

---

### Task 14: Write meta-ads SKILL.md files — waste-detector

**Files:**
- Create: `plugins/meta-ads/skills/waste-detector/SKILL.md`

```markdown
---
name: waste-detector
description: >-
  This skill should be used when the user asks to "find Meta waste",
  "audit my Facebook account", "where am I wasting Meta budget",
  "Meta ads audit", "Facebook spend leaks", "Instagram waste",
  "social ads optimization", or mentions Meta Ads waste analysis,
  Facebook budget efficiency, or social ad spend optimization.
allowed-tools: mcp__meta-ads__query, mcp__meta-ads__mutate, mcp__meta-ads__list_accounts
---

# Meta Ads Waste Detector

Scan Meta Ads accounts for spend leaks and quantify each in dollars with an action plan.

## Status

Skeleton — requires `@channel47/meta-ads-mcp` to be built and published before this skill is functional.

## Meta-Specific Waste Types

| # | Waste Type | Signal |
|---|-----------|--------|
| 1 | Audience overlap | Multiple ad sets targeting overlapping audiences, driving up CPM via self-competition |
| 2 | Creative fatigue | Frequency > 3.0 with declining CTR — audience has seen the ad too many times |
| 3 | Placement bleed | Audience Network or low-quality placements consuming disproportionate spend with poor CPA |
| 4 | Non-converting ad sets | Spend above target CPA threshold with zero conversions |
| 5 | Learning phase churn | Ad sets repeatedly entering and exiting learning phase due to budget/targeting changes |
| 6 | Broad targeting without exclusions | Prospecting campaigns missing customer list exclusions |
| 7 | Frequency cap violations | No frequency cap set on reach/awareness campaigns |
| 8 | Stale lookalike seeds | Lookalike audiences based on outdated or small source lists |

## Severity Tags

Same scale as paid-search: `HIGH` (>$500/mo), `MEDIUM` ($100-500), `LOW` ($25-100), `INFO` (<$25).

## Workflow

### Phase 1: Run waste queries
Query Meta Ads API for each waste type signal.

### Phase 2: Quantify impact
Dollar-denominate each finding. Rank by impact across all waste types.

### Phase 3: Build remediation package
Map findings to specific actions (pause, adjust targeting, refresh creative, add exclusions).

## Output format

Same contract as paid-search waste-detector:
```
## Waste Report - [Date]
### Meta Ads: [Name] ([Account ID])
### Detailed Findings
### Ready-to-Apply Changes
```

## Guardrails

- Mutation safety: dry-run first, user approval required
- Creative pause warning: pausing a Meta creative kills its learnings permanently (unlike pausing a keyword)
- Learning phase: do not flag ad sets in learning phase as waste

## References

- `references/` — to be populated when MCP server is built
```

---

### Task 15: Write meta-ads SKILL.md files — creative-analyzer

**Files:**
- Create: `plugins/meta-ads/skills/creative-analyzer/SKILL.md`

```markdown
---
name: creative-analyzer
description: >-
  This skill should be used when the user asks to "analyze my Meta creatives",
  "review ad performance", "which ads are working", "creative fatigue check",
  "ad creative audit", "best performing ads", "worst performing ads",
  "creative testing results", "hook rate analysis", or mentions creative
  performance, ad fatigue, thumb-stop ratio, or video ad metrics.
allowed-tools: mcp__meta-ads__query, mcp__meta-ads__list_accounts
---

# Creative Analyzer

Evaluate Meta Ads creative performance at the ad level — identify winners, flag fatigue, and surface replacement priorities.

## Status

Skeleton — requires `@channel47/meta-ads-mcp` to be built and published before this skill is functional.

## Key Creative Metrics

| Metric | What It Measures | Good Benchmark |
|--------|-----------------|----------------|
| Hook Rate | % of viewers past 3 seconds (video) | >25% |
| Hold Rate | % of hook viewers to 50% completion | >30% |
| ThruPlay Rate | % to completion or 15s | >15% |
| Thumb-Stop Ratio | 3s views / impressions | >20% |
| CTR | Click-through rate | >1.0% (feed) |
| Outbound CTR | Clicks to external URL / impressions | >0.8% |
| Frequency | Avg times shown per person | <3.0 per 7d |
| CPA | Cost per conversion | Varies by vertical |

## Workflow

### Phase 1: Pull creative performance data

For each active campaign, pull ad-level data:
- Performance metrics (impressions, clicks, CTR, CPA, ROAS)
- Video metrics (hook rate, hold rate, ThruPlay rate)
- Creative asset details (format, copy, thumbnail)
- Frequency and delivery status

### Phase 2: Classify creatives

Assign each ad a status:
- **Winner**: CPA below target, CTR above benchmark, sufficient volume
- **Fatigued**: Was performing well, now declining (frequency > 3, CTR dropped >20% from peak)
- **Underperformer**: Never hit benchmarks with sufficient spend
- **Testing**: Insufficient data to classify (<1,000 impressions or <$50 spend)
- **New**: Less than 3 days old

### Phase 3: Generate recommendations

- Replacement priorities for fatigued and underperforming creatives
- Winning creative patterns (what format, hook style, copy angle works)
- Budget reallocation suggestions (shift spend to winners)

## Output format

```markdown
## Creative Analysis - [Date]
### Campaign: [Name]

### Winners
| Ad | Format | CTR | CPA | ROAS | Hook Rate | Notes |

### Fatigued (Replace Soon)
| Ad | Format | Frequency | CTR Decline | Days Active | Priority |

### Underperformers (Consider Pausing)
| Ad | Format | Spend | CPA | vs Target | Recommendation |

### Testing (Insufficient Data)
| Ad | Format | Spend | Impressions | Status |

### Creative Patterns
- Top-performing format: [image/video/carousel]
- Best hook style: [question/stat/pain point]
- Winning copy angle: [benefit/social proof/urgency]
```

## Guardrails

- Do not recommend pausing creatives without noting the learning-loss tradeoff
- Minimum data thresholds before classifying (1,000 impressions or $50 spend)
- Note that Meta's ad-level metrics can lag 24-48 hours
- Creative performance is heavily audience-dependent — note this context

## References

- `references/` — to be populated when MCP server is built
```

---

### Task 16: Write meta-ads SKILL.md files — audience-builder

**Files:**
- Create: `plugins/meta-ads/skills/audience-builder/SKILL.md`

```markdown
---
name: audience-builder
description: >-
  This skill should be used when the user asks to "build an audience",
  "create a lookalike", "targeting strategy", "audience recommendations",
  "who should I target", "custom audience setup", "audience overlap check",
  "exclusion lists", "retargeting setup", or mentions Meta audience building,
  Facebook targeting, lookalike audiences, or audience segmentation.
allowed-tools: mcp__meta-ads__query, mcp__meta-ads__list_accounts
---

# Audience Builder

Design and evaluate Meta Ads audience strategies — lookalike modeling, custom audiences, interest stacks, exclusion hygiene, and retargeting funnels.

## Status

Skeleton — requires `@channel47/meta-ads-mcp` to be built and published before this skill is functional.

## Audience Types

| Type | Source | Best For |
|------|--------|----------|
| Custom Audience — Customer List | CRM upload (emails, phones) | Retargeting existing customers, seed for lookalikes |
| Custom Audience — Website | Pixel/CAPI events | Retargeting visitors by funnel stage |
| Custom Audience — Engagement | On-platform actions (video views, page likes) | Warming cold audiences |
| Lookalike | Seeded from custom audience | Prospecting at scale |
| Interest/Behavior | Meta's targeting categories | Cold prospecting without seed data |
| Broad (Advantage+) | Algorithmic, minimal targeting | Letting Meta's algorithm find converters |

## Workflow

### Phase 1: Audit existing audiences

Pull current audience configuration:
- Active custom audiences and their sizes
- Lookalike audiences and their seed quality
- Interest targeting in use
- Exclusion lists applied

### Phase 2: Identify gaps

- Missing exclusions (existing customers not excluded from prospecting)
- Stale seed audiences (not refreshed in 90+ days)
- Audience overlap between ad sets (self-competition)
- Missing retargeting layers (website visitors, video viewers, engagers)

### Phase 3: Recommend audience strategy

Build a layered funnel:
1. **Prospecting**: Lookalikes (1-3%) seeded from best customers by LTV
2. **Interest stacks**: Grouped by theme, not individual interests
3. **Retargeting — warm**: Engagers, video viewers (7-30d)
4. **Retargeting — hot**: Website visitors, cart abandoners (1-7d)
5. **Exclusions**: Existing customers, recent converters (14d), bounced visitors

### Phase 4: Generate implementation plan

For each recommended audience:
- Exact audience definition
- Suggested ad set budget allocation
- Expected audience size
- Refresh cadence

## Output format

```markdown
## Audience Strategy - [Date]
### Account: [Name] ([Account ID])

### Current State
| Audience | Type | Size | Last Updated | Status |

### Gaps Identified
1. [Gap + impact + fix]

### Recommended Funnel
| Layer | Audience | Est. Size | Budget % | Notes |

### Exclusion Checklist
- [ ] Existing customers excluded from prospecting
- [ ] Recent converters (14d) excluded
- [ ] Bounced visitors (<10s) excluded

### Implementation Steps
1. [specific action]
```

## Guardrails

- Minimum audience size: 1,000 for custom audiences, 100 for lookalike seeds
- Note iOS ATT impact on custom audience match rates
- Lookalike quality degrades above 3% — flag if wider is recommended
- Interest targeting is Meta's least durable targeting method — note deprecation risk
- Customer list uploads require consent/compliance — remind user

## References

- `references/` — to be populated when MCP server is built
```

---

### Task 17: Write meta-ads README and LICENSE

**Files:**
- Create: `plugins/meta-ads/README.md`
- Create: `plugins/meta-ads/LICENSE`

**Step 1: Write README**

```markdown
# Meta Ads — Claude Code Plugin

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Meta Ads toolkit for Facebook and Instagram — creative analysis, audience building, reporting, and campaign optimization via MCP.

Part of [Channel 47](https://channel47.dev), the open-source ecosystem of profession plugins for Claude Code.

---

## Status

**Skeleton** — plugin structure and skill definitions are complete. Requires `@channel47/meta-ads-mcp` to be built and published for full functionality.

---

## Configuration

The plugin bundles one MCP server via `.mcp.json`. Set these environment variables:

| Variable | Required |
|----------|----------|
| `META_ADS_ACCESS_TOKEN` | Yes |
| `META_ADS_APP_ID` | Yes |
| `META_ADS_APP_SECRET` | Yes |
| `META_ADS_ACCOUNT_ID` | Yes |

---

## What's Inside

```text
meta-ads/
├── .claude-plugin/
│   └── plugin.json
├── .mcp.json              # Meta Ads MCP server (placeholder)
├── hooks/
│   ├── hooks.json
│   └── validate-mutations.py
├── skills/
│   ├── platform-setup/
│   ├── morning-brief/
│   ├── waste-detector/
│   ├── creative-analyzer/
│   └── audience-builder/
├── README.md
└── LICENSE
```

---

## Skills

### platform-setup
Configure Meta Business Manager credentials and verify API access.

### morning-brief
Daily Meta Ads account health — CPM, frequency, creative fatigue, budget pacing, and anomaly detection.

### waste-detector
Find Meta-specific spend leaks — audience overlap, creative fatigue, placement bleed, frequency violations.

### creative-analyzer
Evaluate ad creative performance — hook rate, hold rate, thumb-stop ratio, fatigue signals, winner/loser classification.

### audience-builder
Design audience strategies — lookalikes, custom audiences, retargeting funnels, exclusion hygiene.

---

## Safety Model

Same protocol as all Channel 47 plugins:

1. Query and analyze first.
2. Preview mutations with `dry_run: true`.
3. Request explicit user approval.
4. Execute with `dry_run: false` only after approval.

---

## Links

- [Channel 47](https://channel47.dev)
- [Build Notes](https://channel47.dev/subscribe)

## License

MIT
```

**Step 2: Copy LICENSE from paid-search**

```bash
cp /Users/jackson/Documents/a_projects/ch47/plugins/plugins/paid-search/LICENSE /Users/jackson/Documents/a_projects/ch47/plugins/plugins/meta-ads/LICENSE
```

---

### Task 18: Update repo-level CLAUDE.md for meta-ads

**Files:**
- Modify: `/Users/jackson/Documents/a_projects/ch47/plugins/CLAUDE.md`

Add meta-ads to the structure section alongside paid-search.

---

### Task 19: Commit Phase 2

```bash
cd /Users/jackson/Documents/a_projects/ch47/plugins
git add plugins/meta-ads/
git add CLAUDE.md
git commit -m "feat: scaffold meta-ads plugin skeleton

Directory structure, plugin.json, .mcp.json placeholder,
hooks, and SKILL.md stubs for 5 skills: platform-setup,
morning-brief, waste-detector, creative-analyzer, audience-builder.
MCP server not yet built — skills are structural only.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```
