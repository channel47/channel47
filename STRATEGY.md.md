# Channel 47: Comprehensive Strategy

*Personal brand, practitioner tools, and the long game*

---

## The Bet

Build audience through personal essays. Capture practitioners through free tools. Monetize through high-ticket consulting. Let the email list become distribution for whatever comes next.

**The flywheel:**

```
Personal essays (trust) → Some readers are marketers → They discover Channel 47
                                                              ↓
Standing offer ← Email capture ← Free plugins (utility) ← Claude marketplace
($2,500 audit)     (Kit)           (credibility)           GitHub, SEO
```

This is a 2-3 year play. Year one builds assets. Year two builds audience. Year three (maybe) produces meaningful revenue.

---

## The Honest Reality

Before execution, acknowledge what the market data shows:

| Challenge | Reality |
|-----------|---------|
| MCP ecosystem | Launched October 2025. Fragmented discovery. Top monetized servers make ~£400 MRR. Market doesn't fully exist yet. |
| Google Ads tools | Crowded with Optmyzr ($249-499/mo), Adalysis ($149-349/mo), groas ($99/mo). Years of development, established users, marketing budgets. |
| Newsletter growth | 3% average paid conversion on Substack. Median creator earns ~$4,000/year. 0-3 new subs/day in foundation phase. Most quit here. |
| Free → Revenue | Open source users rarely convert to paying customers. "Good commercial customers are often not in your open source community." |
| Niche size | Claude-using Google Ads practitioners comfortable with MCP installation is a small population. |
| Standing offer | High-ticket typically requires 10,000+ followers before reliable conversion. Year one may see zero inquiries. |

**These are not reasons to quit. They're reasons to set expectations correctly.**

The strategy is sound if you can sustain the effort for 2-3 years before payoff. If you need faster returns, this isn't the right play.

---

## Part 1: Two-Channel Publishing

### The Separation

| | Personal Brand | Channel 47 |
|---|---------------|------------|
| **Purpose** | Trust, voice, audience | Product, utility, capture |
| **Content** | Essays, narratives, reflections | Docs, changelogs, tutorials |
| **Platforms** | Substack, X | channel47.dev, Kit |
| **Cadence** | Biweekly essay | As-needed (when you ship) |
| **Traffic** | X algorithm, Substack recs, word of mouth | GitHub, MCP directories, SEO, your essays |

### What Lives Where

**Personal:** Japan bikepacking story. Fungushead origin and near-failure. Learning to code after 4 years of failing. Building Chiara's ballet site in 3 days. Seneca and philosophy. The PlayStation jailbreak at 12.

**Channel 47:** Google Ads plugin installation guide. Changelog when you fix a bug. Technical walkthrough of a workflow. Plugin documentation.

**Bridge content (monthly):** Building-in-public posts about what you're making, what broke, what you learned. These live on Substack but explicitly connect to Channel 47.

### Publishing Rhythm

**Ongoing:** Capture voice memos. Maintain essay seeds list.

**Every two weeks:** Pick idea → Voice-to-Draft → Edit → Publish to Substack → Extract thread for X.

**Monthly:** One building-in-public essay bridging personal brand and Channel 47.

**As-needed:** Plugin updates → Changelog → Kit email → X post.

### Platform Decisions

- **Single X account** until product content clutters the personal feed
- **Substack** for essays (recommendation engine, built-in audience)
- **Kit** for Channel 47 (product-focused, no personality required)
- **Typefully** for scheduling threads

---

## Part 2: Channel 47 Product

### Foundation: Two MCP Servers

**Google Ads MCP Server** (already built)

| Tool | Purpose |
|------|---------|
| `list_accounts` | Get accessible accounts under authenticated user or MCC |
| `run_query` | Execute any GAQL query — all data retrieval flows through this |
| `mutate` | Make changes with dry-run safety |

**DataForSEO MCP Server** (to build)

| Tool | Purpose |
|------|---------|
| `keyword_data` | Search volume, difficulty, related keywords |
| `serp_analysis` | Who's ranking, ad positions, SERP features |
| `competitor_ads` | Historical ad copy, landing pages, estimated spend |
| `domain_metrics` | Authority, backlinks for landing page context |

DataForSEO solves the Auction Insights problem (deprecated/whitelisted only) and adds keyword research the Google Ads API doesn't provide.

### Plugin Architecture

Each workflow phase becomes its own plugin:

```
channel47/
├── google-ads-mcp/        ← Required dependency
├── dataforseo-mcp/        ← Required for Discovery
├── optimize/              ← Daily optimization work
├── report/                ← Performance narratives
├── discovery/             ← Research and planning
├── build/                 ← Campaign creation
└── monitor/               ← Health checks and alerts
```

### Plugin 1: Optimize

**The daily work.** Where practitioners spend 80% of their time.

| Skill | Trigger | Output |
|-------|---------|--------|
| search-term-miner | "analyze search terms", "find wasted spend", "negative keywords" | Categorized terms, ready-to-apply negatives |
| quality-score-doctor | "why is QS low", "improve quality score" | Diagnosis per keyword, specific fixes, impact estimate |
| bid-advisor | "should I change bidding", "bid adjustments" | Strategy recommendation, device/location modifiers |
| budget-optimizer | "how should I allocate budget", "limited by budget" | Reallocation recommendations, projected impact |

**Agent:** weekly-optimization — Autonomous pass: search terms → QS check → budget review → prioritized action list.

### Plugin 2: Report

**Turn data into narrative.** Second biggest time sink.

| Skill | Trigger | Output |
|-------|---------|--------|
| performance-narrator | "how did the account perform", "summarize last week" | Plain-English narrative, wins/losses, trend direction |
| anomaly-explainer | "why did CPA spike", "what happened Tuesday" | Correlation with changes, confidence-rated explanation |
| client-report | "create client report", "monthly report" | Formatted report with metrics, recommendations |

**Agent:** weekly-report — Pull data → Narrate → Check anomalies → Generate report → Draft email.

### Plugin 3: Discovery

**Research before you build.** Requires DataForSEO MCP.

| Skill | Trigger | Output |
|-------|---------|--------|
| keyword-expansion | "find keywords for", "expand these seeds" | Clustered groups, match type recs, budget estimate |
| competitor-intel | "who are my competitors", "what ads are they running" | Competitor mapping, positioning gaps |
| market-sizing | "how big is this market", "what budget do I need" | Total demand, budget recommendations |

### Plugin 4: Build

**Campaign creation.**

| Skill | Trigger | Output |
|-------|---------|--------|
| campaign-architect | "how should I structure", "plan a campaign" | Structure diagram, naming conventions, budget allocation |
| ad-copy-generator | "write ads for", "generate headlines" | 15 headlines, 4 descriptions, policy check, pin strategy |
| landing-page-auditor | "is this landing page good", "why is LP experience low" | Message match score, friction points, QS prediction |
| launch-checklist | "is this ready to launch", "check my setup" | Pass/fail checklist, risk flags |

### Plugin 5: Monitor

**Proactive health checks.**

| Skill | Trigger | Output |
|-------|---------|--------|
| account-health | "is this account healthy", "what's wrong" | Red/yellow/green flags, prioritized actions |
| opportunity-finder | "where can I grow", "what am I missing" | Untapped audiences, competitive gaps, unused extensions |

### Build Order

| Phase | What | Why |
|-------|------|-----|
| **1: Core** | Google Ads MCP ✓, Optimize plugin | Daily work, highest frequency |
| **2: Reporting** | Report plugin | Second biggest time sink |
| **3: Research** | DataForSEO MCP, Discovery plugin | Adds planning capabilities |
| **4: Complete** | Build plugin, Monitor plugin | Completes the suite |

### Distribution

```bash
# Register Channel 47 marketplace
/plugin marketplace add channel47/google-ads

# Install plugins
/plugin install optimize@channel47
/plugin install report@channel47
```

Traffic sources: Claude marketplace (passive), GitHub (search/stars), MCP directories, SEO on channel47.dev, personal essays (bridge content), word of mouth.

---

## Part 3: Internal Workbench

Skills and tools for creating content and assets. Three layers:

### Layer 1: Capture & Triage

| Skill | Input | Output |
|-------|-------|--------|
| **Essay Seeds Manager** | Rough idea, question | 3 angles, emotional core, hook, connection score |
| **Voice Memo Triage** | Multiple transcripts | Heat ranking, timeliness, effort estimate, recommendation |
| **Story Beat Extractor** | Raw transcript | Key beats, emotional turn, suggested cuts |

### Layer 2: Creation & Transformation

**For Essays:**

| Skill | Input | Output |
|-------|-------|--------|
| **Voice-to-Draft** | Raw transcript | Structured essay draft |
| **Essay Polish** | Draft | Clean draft, AI tells removed, specificity check |
| **Metaphor Generator** | Concept to explain | Analogies from different domains |
| **Audience Bridge Detector** | Draft essay | Flagged bridge points, suggested phrasing |

**For Channel 47:**


| Skill | Input | Output |
|-------|-------|--------|
| **Plugin Docs Generator** | Tool definitions | Installation docs, usage examples |
| **Landing Page Copy** | Plugin docs + audience | Headlines, problem/solution framing |
| **Case Study Extractor** | Rough notes | Structured case study, pull quotes, metrics |
| **Changelog Writer** | Git diff or notes | GitHub release, Kit email, X post versions |
| **Email Sequence Builder** | Purpose | Email draft, subject lines, timing |

### Layer 3: Distribution & Feedback

| Skill | Input | Output |
|-------|-------|--------|
| **X Thread Extractor** | Published essay | Hook tweet, standalone points, closing with link |
| **Remix Engine** | Existing content | Thread version, newsletter excerpt, talk material |
| **Weekly Review Prompter** | What you published, metrics | What worked, what to double down on, seeds |
| **Win Collector** | Quick note | Formatted testimonial, tagged for use |
| **Objection Bank** | Objection heard | Reframe, proof point, added to bank |

### Build Order for Workbench

| Phase | What | When |
|-------|------|------|
| **Now** | Voice-to-Draft, Essay Seeds Manager | First 4-6 weeks |
| **When friction demands** | Essay Polish, X Thread Extractor, Changelog Writer | After workflow is established |
| **When consulting picks up** | Case Study Extractor, Objection Bank | When you have wins to document |
| **When scale matters** | MCP servers for Substack, Kit, Typefully | When manual publishing is friction |

---

## Part 4: Monetization

### Standing Offer

A high-priced consulting offer that exists from day one. Priced above market so the price does the qualifying.

| Offer | Price | Deliverable | Your Time |
|-------|-------|-------------|-----------|
| Strategy Call | $750/hour | Live account review, recorded, action items | 1-2 hours |
| **Full Audit** | **$2,500** | AI-powered analysis, prioritized recs, 30-min walkthrough | 3-4 hours |
| Implementation | $5,000+ | You make the changes | Scoped |

**The differentiator:** "I'll audit your account using the same AI tools I built for my own work. You get a prioritized list of what's actually wrong, not a generic checklist."

**Where it lives:**
- Footer on channel47.dev
- Mentioned once in Substack welcome email
- Occasionally referenced in building-in-public essays

**The signal it sends:** Free tools from someone who does $2,500 audits reads differently than free tools from a hobbyist.

### Monetization Expectations

| Timeframe | Realistic Expectation |
|-----------|----------------------|
| Year 1 | 0-2 audit inquiries. Offer exists for positioning, not revenue. |
| Year 2 | 2-5 audits possible if audience reaches 2,000+ engaged subscribers. |
| Year 3+ | Sustainable consulting income possible. Other products (courses, templates) may emerge based on what audience wants. |

The email list is the real asset. Monetization adapts to what the list wants to buy.

---

## Part 5: Execution Phases

### Phase 1: Foundation (Now - Month 3)

**Publishing:**
- Single X account
- Biweekly essays on Substack
- Voice-to-Draft skill built and in use
- Essay seeds list maintained

**Channel 47:**
- Google Ads MCP server (done)
- Optimize plugin: search-term-miner, quality-score-doctor
- Basic documentation on channel47.dev
- Standing offer live (no hard selling)

**Metrics to track:**
- Essays published (target: 6)
- Substack subscribers
- Plugin installs (GitHub stars as proxy)
- Standing offer page views

### Phase 2: Traction (Month 4-9)

**Publishing:**
- Continue biweekly essays
- Add Essay Polish skill when style slippage noticed
- Add X Thread Extractor when essays worth distributing
- One building-in-public essay per month

**Channel 47:**
- Report plugin: performance-narrator, client-report
- Changelog Writer skill for updates
- Kit email for significant updates

**Decision points:**
- If product content clutters X feed → Spin up @channel47
- If audit inquiries come in → Document the process, build case studies

### Phase 3: Expansion (Month 10-18)

**Publishing:**
- Evaluate weekly cadence if capacity allows
- Remix Engine for repurposing backlog
- Substack/Kit MCP servers if manual publishing is friction

**Channel 47:**
- DataForSEO MCP server
- Discovery plugin: keyword-expansion, competitor-intel
- Build plugin: campaign-architect, ad-copy-generator
- Monitor plugin: account-health, opportunity-finder

**Decision points:**
- If standing offer converting → Consider productized service or course
- If newsletter at 2,000+ → Evaluate paid tier or sponsorships

### Phase 4: Maturity (Month 18+)

**What this looks like:**
- Complete plugin suite
- 2,000-5,000 email subscribers
- Occasional consulting income from standing offer
- Distribution asset for future products

**Adaptation based on what's working:**
- If consulting demand high → Raise prices or productize
- If plugin adoption high → Consider enterprise features or support tiers
- If essay engagement high → Double down on personal brand
- If none of the above → Honest reassessment of the strategy

---

## Part 6: Risk Management

| Risk | Signal | Response |
|------|--------|----------|
| MCP ecosystem stalls | No meaningful growth in Claude Code adoption after 12 months | Diversify to other AI platforms (Cursor, Windsurf) |
| No standing offer inquiries | Zero after 12 months | Lower price to $1,500 or add gateway offer ($200 mini-audit) |
| Newsletter growth stalls | Under 500 after 6 months | Increase frequency or narrow topic focus |
| Plugin development consumes all time | No essays published for 2+ months | Time-box plugin work, protect essay time |
| Burnout | Quality declining, balls being dropped | Cut scope ruthlessly, focus on one channel |
| Competitor ships similar tools | Well-funded player enters the space | Differentiate on practitioner credibility and community |

---

## Part 7: Success Metrics

### Leading Indicators (track weekly/monthly)

| Metric | What It Indicates |
|--------|-------------------|
| Essays published | Habit sustainability |
| Voice memos captured | Pipeline health |
| Plugin commits | Product momentum |
| X engagement on threads | Content resonance |
| Substack open rate | Audience quality |

### Lagging Indicators (track quarterly)

| Metric | Year 1 Target | Year 2 Target |
|--------|---------------|---------------|
| Substack subscribers | 500-1,000 | 2,000-3,000 |
| Kit subscribers | 200-500 | 1,000-2,000 |
| GitHub stars (total) | 100-300 | 500-1,000 |
| Plugin installs | Track, no target | Establish baseline |
| Standing offer inquiries | 0-2 | 5-10 |
| Audit revenue | $0-5,000 | $10,000-25,000 |

### The Real Success Metric

Can you sustain this for 24 months without external validation?

If yes, the compounding effects will eventually manifest. If no, better to know now and adjust the strategy.

---

## Appendix: Key Decisions Made

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Scope | Google Ads plugins only | Focus beats breadth |
| Architecture | Plugins stay modular | Discoverability, selective adoption |
| Publishing cadence | Biweekly not weekly | Sustainability over ambition |
| X accounts | Single account initially | Avoid orphaned accounts |
| Skills build order | Voice-to-Draft first | Friction informs what comes next |
| Monetization | Standing offer from day one | Positioning value even with zero conversions |
| Timeline | 2-3 year horizon | Realistic expectations |

---

## The Closing Frame

This strategy optimizes for:
- **Sustainability over growth-hacking** — Biweekly beats burnout
- **Assets over attention** — Tools and essays compound; tweets don't
- **Patience over pressure** — Year one is planting, not harvesting
- **Optionality over commitment** — Email list enables pivots

It does not optimize for:
- Fast revenue
- Viral growth
- Venture-scale outcomes
- Platform dependency

**For now:** Biweekly essays, free tools, and one premium offer that exists quietly in the background.

**The bet:** If you show up consistently for 2-3 years, something will work. You just don't know which thing yet.

---

*Last updated: January 2025*
