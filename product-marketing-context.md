# Product Marketing Context

*Last updated: 2026-03-04*

## Product Overview

**One-liner:** Open-source Claude plugins that make paid media practitioners dangerous.

**What it does:** channel47 curates the best open-source MCP servers, skills, and subagents into practitioner-grade Claude plugins — one per ad platform. Each plugin connects Claude to live account data and ships with opinionated workflows that turn raw API access into actionable intelligence: morning briefs, waste detection, search term classification, creative fatigue analysis, budget pacing.

**What it doesn't do:** Change anything. Every plugin is read-only by design. No mutations, no bid adjustments, no keyword pauses, no campaign changes. The plugins tell you exactly what to fix, where to fix it, and how much it's costing you. You do the clicking.

**How it works:**
1. Install a plugin (`claude plugin install google-ads@channel47`)
2. Connect your ad accounts (your credentials, your machine, your data)
3. Run workflows in natural language ("run my morning brief", "find waste in this account")
4. Get prioritized action plans with dollar-quantified impact and exact UI navigation paths
5. Execute the recommendations yourself in the platform UI

**Product category:** Paid media intelligence plugins for Claude Code and Claude Cowork.

**License:** MIT. Every plugin, skill, and reference file is open-source.

## Design Philosophy

### Read-only by design

This is a hard constraint, not a temporary limitation. The plugins cannot modify ad accounts. This is intentional:

- **Zero risk to user accounts.** Nothing to break, nothing to undo. The scariest thing a plugin can do is show you numbers you don't like.
- **Trust barrier drops to zero.** "It can read your data" is a fundamentally different conversation than "it can change your bids."
- **The intelligence layer IS the value.** The 80/20 of paid media management: knowing what to do takes 2 hours, doing it takes 5 minutes. These plugins eliminate the 2 hours.
- **Credential safety simplifies.** Users' API credentials stay on their machine in environment variables. The MCP server runs locally via stdio. No credentials flow to Ch47 or any third party. We never see your data.

### Curate, don't rebuild

If someone built a better MCP server, skill, or audit framework — use it. The open-source community has built excellent ad platform tooling. Ch47's job is to assemble the best tools into coherent, opinionated workflows that practitioners can install and use immediately.

We build the workflow intelligence layer: morning briefs, waste detectors, search term classifiers, creative fatigue models. We don't rebuild the plumbing.

### One plugin per platform

Google Ads and Bing Ads are separate plugins. Each platform stands alone, is independently installable, and carries only its own context. This keeps context windows clean, makes each plugin discoverable by platform name, and lets practitioners install only what they need.

### Specificity over automation

Read-only plugins must compensate with extreme specificity of output:

- **Dollar-quantified impact** — not "you have waste" but "$2,347/month on these 12 keywords"
- **Exact UI navigation paths** — "Campaign X > Ad Group Y > Keywords > select 'running shoes red' > Pause"
- **Copy-paste artifacts** — negative keyword lists grouped by match type, ready to paste into shared lists
- **Priority-ranked action plans** — work top to bottom, highest dollar impact first
- **Time estimates** — "~30 seconds" or "~2 minutes" per fix

## Target Audience

**Primary:** Media buyers who use Claude and manage ad accounts daily. They touch the accounts — review search terms, manage budgets, present results to clients. Not executives reviewing dashboards.

**Segments:**
- Solo PPC consultants managing 5-15 client accounts
- Agency account managers on 3-8 accounts each
- In-house paid media leads running campaigns across platforms
- Growth engineers comfortable with CLI tools and API credentials

**Prerequisite:** Users need their own API credentials for each platform (developer tokens, OAuth clients, API keys). These plugins don't provide account access — they provide intelligence on top of access you already have.

**Anti-persona:** Marketers who don't manage accounts hands-on. People who want a fully autonomous AI that makes decisions for them. Teams already happy with Optmyzr or similar.

## Phase 1 Plugins

### Google Ads

**MCP:** `cohnen/mcp-google-ads` (439 stars, 12+ read tools, raw GAQL support) — best community MCP for Google Ads. Alternative: Google's official MCP (`googleads/google-ads-mcp`) for maximum trust, but limited to 2 tools and stale at v0.0.1.

**Workflows:**
| Skill | What it does | Cadence |
|-------|-------------|---------|
| morning-brief | Anomaly detection, budget pacing, ad disapprovals, auto-applied changes | Daily |
| waste-detector | 8 waste categories with dollar quantification and prioritized action plan | Weekly |
| search-term-verdict | Classify search terms into promote / negate / monitor with export lists | Weekly |
| pmax-decoder | PMax transparency — search terms, channel mix, asset performance | Weekly |
| account-scorecard | Quantified health grade across 5 dimensions | Monthly |
| ad-copy-analyzer | RSA asset performance, fatigue detection | Monthly |
| competitor-intel | Auction insights + competitive research via DataForSEO | Monthly |

**Key differentiator:** Practitioner-grade morning brief with dollar-quantified anomaly detection. Nobody else packages daily PPC monitoring as a Claude workflow.

### Microsoft Ads

**MCP:** `Duartemartins/microsoft-ads-mcp-server` (most complete community option — campaigns, keywords, reporting, QS) or `@channel47/bing-ads-mcp` (built-in reporting pipeline with CSV parsing). Evaluate which has stronger read capabilities.

**Workflows:**
| Skill | What it does | Cadence |
|-------|-------------|---------|
| morning-brief | Budget pacing, bot traffic monitoring, search partner quality | Daily |
| waste-detector | 7 Bing-specific waste categories (MSAN, search partners, broad match imports) | Weekly |
| search-term-verdict | Adapted for Bing's worse close variant matching | Weekly |
| import-auditor | Post-Google-import cleanup checklist with specific fixes | Ad hoc |
| placement-cleaner | MSAN/publisher exclusion recommendations | Weekly |

**Key differentiator:** Nobody treats Bing as a first-class platform. The import auditor alone saves hours of post-import cleanup.

### Meta Ads

**MCP:** `pipeboard-co/meta-ads-mcp` (563 stars, 10K+ businesses, battle-tested) as primary. `trypeggy/facebook-ads-library-mcp` for competitive research. No official Meta MCP exists — Meta is investing in Manus/Advantage+ internally, not developer tooling for external agents.

**Workflows:**
| Skill | What it does | Cadence |
|-------|-------------|---------|
| morning-brief | CPA/ROAS check, delivery flags, CPM/frequency monitoring, Learning Phase status | Daily |
| waste-detector | 8 Meta-specific waste categories (audience overlap, creative fatigue, placement waste) | Weekly |
| creative-fatigue | CTR/CPA decay detection, lifecycle classification, "days remaining" estimates | Weekly |
| creative-audit | Categorize all active ads by concept, format, angle | Monthly |
| audience-analyzer | Performance by audience type, saturation detection | Monthly |
| competitor-research | Ad Library research via dedicated MCP | Ad hoc |

**Key differentiator:** Creative fatigue lifecycle classification with "days remaining" estimates. Commercial tools (Motion, Bestever) charge $500+/month for this.

## Competitive Landscape

### Direct competitors

| Competitor | Price | What they offer | Our take |
|-----------|-------|----------------|----------|
| **Adspirer** | $0-199/mo | Hosted MCP for Google, Meta, TikTok, LinkedIn. 100+ tools. Aggressive content SEO. | Pure plumbing. No workflow intelligence. Free tier is 15 tool calls — barely one session. But: capturing search intent we haven't started competing for. |
| **Adzviser** | $34.99/mo | 18 data sources, Supermetrics replacement positioning. | Broad data focus, not PPC-specialized. |
| **cohnen/mcp-google-ads** | Free | Best community Google Ads MCP. 300+ stars. | We bundle this as our Google MCP. Complementary, not competitive. |
| **Pipeboard** | Free + enterprise | Meta/Google Ads MCP. Security-forward. | We bundle their Meta MCP. Complementary. |
| **Composio** | $0-229/mo | 500+ integrations including Google Ads. | Generalist. Context window bloat from 40+ tools degrades model performance. |
| **Google Official MCP** | Free | Official, v0.0.1, 2 read tools. | Minimal. We offer it as an alternative for maximum trust. |

### Secondary competitors (skills, no account access)

| Competitor | Note |
|-----------|------|
| **claude-ads** (652 stars) | 186 audit checks across 6 platforms. Best audit framework — we reference it, don't rebuild. |
| **marketingskills** (10.8K stars) | 34 marketing skills. Recipes without a kitchen — no API connections. |
| **meta-ads-analyzer** (215 stars) | Breakdown Effect analysis, Learning Phase detection. Complementary to our Meta plugin. |

### Our position

MCP servers are commodity. Adspirer has one, cohnen has one, Google has one. "We connect to Google Ads" is table stakes.

**We don't build better plumbing. We curate the best existing plumbing and add the intelligence layer on top.** Morning briefs that catch anomalies. Waste detectors that quantify leaks in dollars. Search term classifiers that export paste-ready negative lists. Creative fatigue models that estimate days until decay.

Nobody else packages practitioner-grade PPC workflows as Claude plugins. That's the gap.

## Differentiation

1. **Curated best-in-class tools** — Each plugin bundles the best available MCP for its platform. We evaluated every option. Users get a tested, working configuration instead of researching MCPs themselves.

2. **Read-only by design** — Not a limitation we'll fix later. A trust decision. Zero risk to accounts. Nothing to undo. The safest way to get intelligence from your ad data.

3. **Workflow intelligence** — Not raw API wrappers. Opinionated, frequency-organized workflows built from managing real accounts. The skills know what to look for and how to prioritize findings.

4. **Dollar-quantified output** — Every finding comes with estimated monthly impact. Not "this keyword has low QS" but "this keyword's QS of 3 is costing you an estimated $847/month in CPC inflation."

5. **Actionable specificity** — UI navigation paths, copy-paste negative keyword lists, CSV exports for bulk upload. The output is a prioritized to-do list, not a report.

6. **Platform-specific expertise** — Bing-specific waste categories (MSAN, search partner junk). Meta-specific creative fatigue models. Amazon keyword harvesting pipelines. Each plugin reflects how practitioners actually work on that platform, not a generic template applied across platforms.

7. **Open-source and transparent** — Every skill is a markdown file you can read, fork, and modify. No black box. Inspect the logic, disagree with a threshold, change it.

## Architecture

```
[platform]-ads/
├── .mcp.json                      # Curated MCP server(s) for this platform
├── skills/
│   ├── platform-setup/SKILL.md    # Credential verification, account discovery
│   ├── profile-review/SKILL.md    # Persistent account context
│   ├── morning-brief/SKILL.md     # Daily health check
│   ├── waste-detector/SKILL.md    # Platform-specific waste categories
│   └── [platform-specific]/       # Skills unique to this platform
├── hooks/
│   ├── inject-profile.sh          # Load account profile at session start
│   └── update-profile.py          # Save watch list and decision log at session end
└── references/
    ├── [query-templates].md       # Platform-specific query templates
    ├── thresholds.md              # Anomaly detection thresholds
    ├── benchmarks.md              # Industry benchmarks
    └── ui-paths.md                # Platform UI navigation reference
```

**Shared patterns across all plugins:**
- Account profile persistence (session-to-session memory via `account-profile.md`)
- Profile injection at session start, state save at session end
- Anomaly detection formulas (deviation from 7d/30d baselines, dollar impact gating)
- Priority ranking by dollar impact descending
- Severity tagging: HIGH (>$500/mo), MEDIUM ($100-500), LOW ($25-100), INFO (<$25)
- Copy-paste export artifacts in every actionable skill

**MCP selection criteria:**
- Open-source with permissive license (MIT, Apache-2.0)
- Local stdio transport (credentials stay on user's machine)
- Active maintenance (commits within last 6 months)
- Adequate read tool coverage for the platform's core workflows
- Community trust signals (GitHub stars, usage, issues resolved)

## Brand Voice

**Tone:** Practitioner-casual. Specific with numbers. Anti-corporate. Honest about what the plugins can and can't do.

**Positioning line:** "The paid media plugins for Claude."

**How we talk about read-only:**
- Not: "Currently read-only, write support coming soon"
- Yes: "Read-only by design. Zero risk to your accounts."

**How we talk about curation:**
- Not: "We leverage synergies from the open-source ecosystem"
- Yes: "We evaluated every Google Ads MCP out there. cohnen's is the best. We ship it."

**How we talk about output:**
- Not: "Get insights into your ad performance"
- Yes: "It told me I was wasting $2,347/month on 12 keywords across two accounts. Took me 3 minutes to pause them."

**Words to use:** connect, read, analyze, catch, flag, waste, action plan, UI path, paste, prioritize, dollar impact, practitioner-built, read-only, open-source

**Words to avoid:** autonomous, autopilot, AI-powered, revolutionary, game-changer, magic, disrupt, leverage, synergy, MCP (in user-facing copy), GAQL (in user-facing copy)

## Distribution

**Primary channels:**
1. **Anthropic Plugin Registry** — Zero paid media plugins exist in the official directory. First-mover advantage.
2. **Content SEO on channel47.dev** — Cornerstone guides: "How to Connect Google Ads to Claude," workflow walkthroughs with real output and dollar amounts.
3. **Reddit (r/PPC, r/googleads, r/digital_marketing)** — Workflow walkthrough posts, not product pitches. Show real output. Let the tool sell itself.
4. **Build Notes newsletter** — 500+ subscribers. Document the build, share workflow examples.
5. **Workshops / Skills Labs** — ~250 attendees per session. Live demos catching real waste.

**Agency distribution:** Claude Team/Enterprise admins can install plugins for their entire org. One agency founder installs = every account manager gets the workflows. This is live infrastructure today.

## Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Third-party MCP breaks or is abandoned | Medium | High — plugin stops working | Pin versions. Monitor upstream repos quarterly. Have fallback MCP options identified for each platform. |
| Adspirer adds workflow intelligence | Medium | High — erodes primary differentiator | Ship fast. Build community trust before they can replicate. |
| Credential setup friction deters non-technical users | High | Medium — limits addressable audience | Write best-in-class setup guides. Consider hosted convenience layer later. |
| npm supply chain compromise of bundled MCP | Low | Critical — user credentials exposed | Minimize dependencies. Pin versions. Document trust model explicitly. |
| Users want write access | Medium | Low — intentional constraint, not a gap | Hold the line. Read-only is the trust story. If mutation demand is overwhelming, consider it as a separate premium product, never in the free open-source suite. |
| Platform API changes break queries | Medium | Medium — skills produce errors | Reference files (query templates, thresholds) are easy to update. Monitor platform API changelogs. |

## Relationship to Channel 47

The plugin suite IS channel47's product. Ch47 = open-source Claude plugins for paid media. The plugins build audience, trust, and distribution. PaidBrief (paidbrief.com) is the separate commercial product that monetizes this distribution.

The flywheel: Day job (real accounts, real data) > plugins (free, open-source, builds audience) > PaidBrief (monetization) > Ch47 brand (distribution + trust).

The plugins don't need their own revenue model. They're the distribution layer.
