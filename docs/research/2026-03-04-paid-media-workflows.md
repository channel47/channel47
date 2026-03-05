# Paid Media Workflow Research: What Makes a 100x Plugin Suite

*Research compiled: 2026-03-04*
*Sources: r/PPC, r/digital_marketing, r/FacebookAds, industry tools, audit frameworks, agency pricing data*

---

## Executive Summary

After deep research across Reddit practitioner communities, industry tools (Optmyzr, Adalysis, Adspirer), audit frameworks, and agency workflows, the picture is clear: **the highest-value automation opportunities are NOT the ones most tools focus on.** Most tools optimize campaign knobs (bids, budgets, keywords). The real pain -- and the real money -- lives in the gaps between platforms, between data and decisions, and between practitioners and their clients.

The 100x plugin suite doesn't compete with Optmyzr on bid rules or Adspirer on tool calls. It competes with **the agency's junior analyst**, **the Wednesday afternoon audit sprint**, and **the Friday reporting grind**. That's where hours disappear and errors compound.

---

## 1. Top Pain Points for Multi-Platform Media Buyers

### What Practitioners Actually Say (Reddit, verbatim themes)

**Loss of control is the #1 emotional pain point:**
> "My main frustration is just a total lack of control. Between PMax and Advantage+, I spend half my time just... feeding the machine." — r/PPC, 19 comments

> "Real PPC in 2026 is conversion architecture, attribution modeling, and teaching algorithms what success looks like through proper data infrastructure." — 63 upvotes on r/PPC

> "The agencies getting phased out are the ones still thinking their value is campaign babysitting and quarterly ad copy refreshes." — r/PPC

**Conversion tracking breaks constantly:**
> "Just getting conversion tracking to work with 100% uptime and comprehensiveness with lead gen is so annoying, especially tying it to revenue. Something, somewhere, breaks." — r/PPC, 7 upvotes

> "The constant barrage of changes to conversion tracking. This is extremely disruptive to advertising as advertisers are constantly behind the latest change or method." — TTFV (well-known r/PPC contributor)

> "Research shows 30-40% of audits have major tracking problems." — Big Linden audit framework

**First-party data upload is the new leverage, but nobody does it well:**
> "Weekly offline conversion imports is a game changer in google ads... First party data is absolutely your edge in the auction cuz most companies still don't fully understand its value or aren't going to put in the extra effort to do that." — 34 upvotes

> "For my enterprise clients, I spend 70% of time on data infrastructure and 30% on campaign management." — r/PPC

**Google's AI is actively distrusted:**
> "Google ads are a bit...well...rubbish nowadays aren't they? The efficiency of google ads is just nowhere near where they used to be." — 58 upvotes, 70 comments

> "The up to 200% daily budget is such a fucking scam. Oh and AI Max -- I saw today 2 clicks at 40x CPCs." — r/PPC

> "Broad match with a new label" — recurring community meme

### The Time-Sink Hierarchy (where hours actually go)

| Task | Time/week | Error rate | Automatable? |
|------|-----------|-----------|--------------|
| Search term review + negative keywords | 3-5 hrs | High (missed terms) | Highly |
| Cross-platform reporting | 3-5 hrs | Medium (manual errors) | Highly |
| Budget pacing checks | 1-2 hrs | Medium | Highly |
| Conversion tracking audits | 2-4 hrs | Very high (30-40% broken) | Partially |
| Creative performance review | 2-3 hrs | Medium | Partially |
| Bid strategy monitoring | 1-2 hrs | Low (platform handles) | Already automated |
| Client communication/reporting | 3-5 hrs | N/A | Partially |
| Account structure reviews | 2-4 hrs/quarter | Medium | Partially |

**Key insight:** The platform-managed automation (smart bidding, auto-apply) has reduced bid management time but INCREASED time spent on oversight, data quality, and proving value to clients. The job shifted from "doing" to "checking that the machine is doing it right."

---

## 2. Cross-Platform Reporting Needs

### The Core Problem

> "I see the same pattern: copying data from GA4 into a Google Doc, screenshotting Meta Ads dashboards, spending hours formatting something that the client glances at for 30 seconds." — r/digital_marketing, 16 comments

> "The biggest time sink is pulling the data itself -- logging into GA4, Meta Ads Manager, Google Ads, maybe your CRM, copying numbers into a sheet or slides. That part should be automated. The actual insights and recommendations? That's where your expertise shows." — r/digital_marketing

> "Most agencies don't actually want fully automated reports. They want the data pulled automatically but still want to add their own narrative and insights." — r/digital_marketing

### What They Actually Need

1. **Normalized KPIs across platforms** — Each platform defines conversions, attribution, and ROAS differently. Teams spend hours reconciling "Meta says 374 conversions, GA4 says 212, Google Ads says 71" for the same form fill.

2. **Period-over-period comparisons** — Same month last year, not just last month. "Saying 'we got 29 leads' doesn't mean anything without context."

3. **Narrative layer on top of data** — The data pull should be automatic; the insight should be human. Current tools either give raw data or fully automated (bad) summaries.

4. **Client-ready formatting** — Not dashboards clients won't check. Decks, slides, or concise written summaries.

5. **Blended metrics** — Total marketing spend vs. total revenue across all channels, not just per-platform ROAS.

### Current Solutions (and their gaps)

| Tool | What it does | Gap |
|------|-------------|-----|
| Looker Studio + Power My Analytics | Dashboard with multi-source connectors | Manual screenshot-to-deck workflow; no narrative |
| Markifact | Auto-fill Google Slides from ad accounts | Template-bound, limited analysis |
| AgencyAnalytics | Multi-platform dashboards | Dashboard fatigue; clients don't check |
| Manual Google Sheets | Full control | 3-5 hours per client per month |
| n8n / Zapier automations | Pull metrics automatically | Requires technical setup; no analysis |

### The Plugin Opportunity

A Claude plugin that can:
- Pull last 7/30/90 day performance from Google + Meta + Bing in one query
- Normalize metrics (impressions, clicks, conversions, spend, ROAS) into comparable format
- Flag anomalies ("Meta CPA up 40% week-over-week, investigate creative fatigue")
- Generate a written narrative summary with specific callouts
- Compare to same period last year
- Output in a format ready for client delivery

This alone would save 3-5 hours per client per month and represent the single highest-value "show don't tell" moment for adoption.

---

## 3. Creative Workflow Automation

### The Reality of Creative Testing in 2025-2026

**Creative fatigue is the #1 Meta Ads problem:**
> "We keep running into creative fatigue on Meta ads. Testing new video creatives feels very random -- most of them flop and burn budget." — r/FacebookAds

> "Which metrics do you rely on first to say 'this creative is getting fatigued'? Is it CTR decay, CPM increase, CPA trend, frequency, or something else?" — r/FacebookAds

**How practitioners actually detect fatigue:**
- CTR decay over 3-7 days
- CPM increase without audience change
- Frequency above 2.5-3x
- Meta's delivery insights: when % of daily impressions from new users drops below 50%
- CPA trending up while spend remains constant

**The creative testing framework most agencies use:**
1. Hypothesis → Variable isolation (one element at a time)
2. Budget allocation → Test with minimum viable spend
3. Signal reading → CTR, hook rate (3-sec video views / impressions), thumbstop ratio
4. Winner scaling → Gradual budget increase on winners
5. Archive losers → Document learnings
6. Refresh cycle → Every 2-4 weeks for top-funnel

### What's Missing (Plugin Opportunity)

No tool currently:
- Monitors creative performance across Google AND Meta simultaneously
- Alerts when a creative is entering fatigue (predictive, not reactive)
- Generates variation briefs based on what's working (e.g., "Your top performer uses UGC format with a question hook -- here are 5 variations")
- Tracks creative-to-landing-page alignment
- Maintains a creative performance knowledge base across campaigns

**Cross-platform creative intelligence is a white space.** Motion (motionapp.com) does this for Meta but not cross-platform, and costs $500+/mo.

---

## 4. Budget Allocation Across Platforms

### How Teams Actually Decide

From the r/PPC thread on managing $150K+/month across platforms:

> "At $150k monthly with fluctuating budgets, I'd build campaign structures around percentage allocation rather than fixed spend... keeps your channel mix stable when budgets swing 25-105%." — 9 upvotes

> "Use shared CPA targets rather than fixed budgets to stabilize CPAs." — r/PPC

> "Before you do anything, the best question you should ask is: is it a demand capture account or a demand generation account? If it is the former, allocate more funds to paid search. If the latter, allocate more to paid media (Meta, TikTok)." — r/PPC

### The Budget Allocation Problem

| Scenario | Current approach | Pain |
|----------|-----------------|------|
| Monthly budget fluctuations (+/-25%) | Manual reallocation across platforms | Takes hours, algorithm relearning |
| Seasonal swings | Historical intuition | Missed opportunities, overspend in troughs |
| New platform testing | Arbitrary % carve-out | No framework for when to scale up/down |
| Cross-platform diminishing returns | Gut feeling | Over-investing in one platform while another has headroom |
| Multi-location budgets | Spreadsheet per geo | One person (r/PPC poster) manages 40 geos with different availability |

### The Plugin Opportunity

- **Budget pacing with reallocation signals:** "Google is pacing 15% under budget with good CPA. Meta has headroom. Consider shifting $X."
- **Diminishing returns detection:** "Your Google CPA increased 30% at this spend level. Historical data suggests diminishing returns above $X/day."
- **Seasonal budget modeling:** Based on last year's performance data, suggest monthly budget distribution.
- **Multi-location budget optimization:** Pull performance by geo, flag locations where budget exceeds demand or where CPA targets aren't achievable.

This is where media mix modeling meets practitioner workflow. Not MMM software (Northbeam, Measured at $XX,XXX/yr) -- just smart, data-driven budget signals.

---

## 5. Audience Management Across Platforms

### The Current State

- **Meta:** Lookalike audiences still work but Advantage+ Audience is replacing manual targeting. Value-based lookalikes from CRM data outperform basic customer list lookalikes.
- **LinkedIn:** Discontinued Lookalike Audiences (early 2024), replaced with Predictive Audiences and enhanced Audience Expansion. Targeting by job title, industry, seniority, company size.
- **Google:** Customer Match for audience signals. Performance Max uses audience signals as hints, not hard targeting.
- **TikTok:** Lookalike audiences based on customer lists, pixel data, or in-platform engagement.

### Cross-Platform Audience Pain Points

1. **List management is fragmented** — Same customer list must be uploaded to 3-4 platforms in different formats, at different cadences, with different match rates.
2. **Audience overlap is invisible** — No way to know if Meta and Google are showing ads to the same people.
3. **Exclusion management is manual** — Excluding converters from prospecting requires manual list updates across every platform.
4. **Match rates vary wildly** — Google might match 60% of a list, Meta 45%, LinkedIn 30%. No unified view.

### The Plugin Opportunity

- **Audience health check:** "Your customer list on Google Ads was last updated 47 days ago. Meta's list is current. Recommend refreshing Google."
- **Cross-platform audience audit:** Pull audience sizes and overlap indicators across connected platforms.
- **Exclusion validation:** "Your converters exclusion list has 1,200 entries on Meta but only 800 on Google. 400 converters may be seeing prospecting ads on Google."

This is niche but extremely high-value for agencies managing cross-platform campaigns.

---

## 6. Common Audit Frameworks

### The 60-Point PPC Audit (Big Linden / Industry Standard)

Full framework organized into 10 categories:

**A. Governance & Hygiene (4 items)**
- Account ownership, billing, 2FA
- User roles with least-privilege access
- Change history alignment with documented plans
- Account structure mirrors business goals

**B. Measurement & Attribution (8 items)**
- GA4 linked, conversions imported without duplicates
- Primary vs. micro conversions properly defined
- Enhanced Conversions enabled
- Offline conversion imports from CRM (deduplicated on gclid/msclkid)
- Data-driven attribution (retire last-click)
- Conversion windows match sales cycle
- Value-based bidding readiness
- UTM standardization + auto-tagging + full click-to-conversion path testing

**C. Budgeting & Bidding (6 items)**
- Daily budgets aligned to targets; "limited by budget" resolved
- Bid strategies matched to objectives
- Portfolio bid strategies where beneficial
- Seasonality adjustments and data exclusions current
- Learning periods respected; edits batched weekly
- Impression Share and Lost IS monitored

**D. Keywords & Search Terms (8 items)**
- Brand vs. non-brand separated
- Broad match used cautiously with strong negatives
- Negative keyword strategy at account/campaign/ad group levels
- Search Terms reviewed; zero-intent terms paused
- Query-to-ad-group alignment
- Duplicate/near-duplicate keywords consolidated
- "Low search volume" terms cleaned up
- Competitor terms modeled for CPC/conversion economics

**E. Ads, Assets & Extensions (7 items)**
- 2+ RSAs per ad group; good/excellent ad strength
- Test framework with one variable at a time
- All relevant assets populated (sitelinks, callouts, structured snippets, images)
- Ad customizers and countdowns used
- Policy disapprovals cleared
- Ad-to-landing message match
- Creative freshness; new variants rotated, underperformers archived

**F. Audiences & Signals (6 items)**
- Remarketing lists activated (site visitors, cart abandoners, high-value users)
- Customer Match lists built (compliant, segmented by lifecycle value)
- In-market, affinity, custom segments layered with bid modifiers
- Demographic exclusions/adjustments supported by performance data
- RLSA for non-brand search
- Broad match/PMax seeded with high-quality first-party data

**G. Shopping, PMax & Feeds (5 items)**
- Merchant Center healthy; feed diagnostics resolved
- Product feed quality optimized (titles, attributes, GTINs)
- PMax asset groups structured by product/category
- Brand exclusions/safety controls active
- Incrementality and cannibalization vs. Search monitored

**H. Geo, Device & Schedule (4 items)**
- Location targeting set to Presence (not Presence or Interest)
- Geo performance reviewed; bids adjusted by region
- Device performance analyzed
- Ad schedules built; off-hours waste eliminated

**I. Landing Pages & CRO (5 items)**
- Page speed and mobile UX (Core Web Vitals)
- Message match: headline, offer, CTA aligned to query/ad
- Forms optimized (minimal fields, trust signals, tracking confirmed)
- A/B testing running with clean design and adequate sample size
- Post-click funnel tracked; drop-off points identified

**J. Paid Social (7 items)**
- Pixels/Insight Tags installed and verified
- Limited/aggregated tracking handled per platform policy
- Campaigns structured by single objective
- Audience strategy includes lookalikes and value-based audiences
- Creative diversified (video, static, carousel); fatigue tracked
- Placement controls, exclusions, brand safety
- Server-side Conversions API; offline conversion imports

### What Auditors Actually Check (r/PPC practitioner thread)

> "Start with tracking (are conversions firing and importing correctly), then move to structure, bidding, and search terms to find wasted spend fast." — r/PPC

> "My audits are always done personally by me, recorded on a loom video explaining what is wrong, how we will fix it, and what the strategy will be moving forward." — r/PPC

> "Honestly, there aren't many tools that can fully help you with this. Some tools, like WordStream's Grader, can support you with the basics, but ultimately your experience and well-defined SOPs will make the biggest difference." — r/PPC

### The 7 Most Common Audit Findings (from a practitioner who audited 50+ accounts, 133 upvotes on r/PPC)

1. **Conversion tracking broken or non-existent** — "An HVAC company had been running ads for 8 months with zero conversion tracking."
2. **Keyword match types too broad** — "A roofing company paying $47/click for 'roof' broad match, showing up for 'roof of mouth surgery.'"
3. **No negative keywords list** — "One landscaping business was spending 40% of budget on irrelevant terms."
4. **Too many or too few ads per ad group** — RSA testing without structure.
5. **No ad extensions** — Missing sitelinks, callouts, structured snippets.
6. **Landing page misalignment** — Ad promise doesn't match landing page delivery.
7. **No conversion value tracking** — Optimizing for volume, not value.

### The Plugin Opportunity (Massive)

A comprehensive audit workflow that checks 60 items automatically from live account data is worth $2,000-5,000 in consulting value. Currently:
- Manual audits take 4-8 hours
- Agencies charge $500-2,000 per audit
- 95% of accounts have the same fixable mistakes
- No tool automates the full checklist with live data + written narrative

**This is the highest-leverage workflow for Ch47 to build after the core 6.**

---

## 7. What Adspirer Offers (and the Gaps)

### Adspirer's Current Product

| Dimension | What Adspirer has |
|-----------|------------------|
| **Platforms** | Google Ads (39 tools), Meta Ads (20 tools), LinkedIn Ads (28 tools), TikTok Ads (4 tools) |
| **Tool count** | 100+ tools across 4 platforms |
| **Client support** | ChatGPT, Claude, Claude Code, Cursor, Codex, Windsurf, OpenClaw |
| **Skills** | 5 core skills: Ad Campaign Management, Setup, Performance Review, Write Ad Copy, Wasted Spend |
| **Agent** | Performance Marketing Agent that orchestrates skills, maintains STRATEGY.md |
| **Pricing** | Free (15 calls/mo), Plus $49/mo (150), Pro $99/mo (600), Max $199/mo (3000) |
| **Auth** | Hosted OAuth, multi-account |
| **Safety** | Campaigns created in PAUSED status requiring approval |
| **Content** | Aggressive SEO: "Claude for Marketing Guide," "10 Best AI Tools for PPC Managers 2026" |

### Adspirer's Real Strengths
- Multi-platform from day one (Google, Meta, LinkedIn, TikTok)
- Broad client support (not Claude-locked)
- Content SEO capturing search intent Ch47 hasn't started competing for
- Being recommended organically on r/PPC
- Agent-level orchestration with memory and strategy persistence

### Adspirer's Real Gaps

1. **No practitioner credibility** — No named practitioner, no "I manage 25 accounts" story, no workshop presence, no community trust
2. **Tool-call pricing penalizes exploration** — Free tier = 15 calls (one morning brief). Plus = 150 calls ($49/mo, ~3 sessions). Power users hit $199/mo fast.
3. **No workflow intelligence** — 100 tools ≠ knowing what to check first. It's a wrench set, not a mechanic.
4. **No cross-platform analysis** — Tools are per-platform. Can't do "compare my Google and Meta CPA trend over 30 days" in one query.
5. **No audit framework** — Can pull data but doesn't know the 60-point checklist or the 7 common mistakes.
6. **No creative intelligence** — Can manage creatives but doesn't detect fatigue, suggest rotations, or analyze creative-to-performance patterns.
7. **No reporting narrative** — Can pull metrics but doesn't generate client-ready written analysis.
8. **TikTok is barely supported** — Only 4 tools vs. 39 for Google.
9. **No community or education** — No workshops, no newsletter, no practitioner content.
10. **Pricing signals "commodity API"** — Tool-call pricing feels like Twilio, not a professional tool.

### Where Ch47 Can Win Against Adspirer

| Gap | Ch47 plugin opportunity | Value |
|-----|------------------------|-------|
| Practitioner credibility | Built by someone who manages 25+ accounts | Trust (priceless) |
| Cross-platform analysis | "Compare Google vs Meta vs Bing performance" workflow | Saves 2-3 hrs/week |
| Comprehensive audit | 60-point automated audit with written findings | Worth $2K in consulting |
| Creative fatigue detection | Cross-platform creative health monitoring | Prevents wasted spend |
| Client reporting narrative | Written performance summaries, not raw data | Saves 3-5 hrs/client/month |
| Budget allocation signals | Cross-platform budget pacing + reallocation recommendations | Prevents budget waste |
| First-party data quality | Audit CRM-to-platform data pipelines | The new competitive edge |

---

## 8. What Agencies Charge For (Highest-Value Services)

### Agency Pricing Benchmarks

| Model | Typical range |
|-------|--------------|
| Monthly retainer (SMB) | $500 - $2,000/mo |
| Monthly retainer (mid-market) | $2,000 - $10,000/mo |
| Monthly retainer (enterprise) | $10,000 - $50,000+/mo |
| Percentage of ad spend | 10-20% (most common) |
| Hourly rate (US) | $150 - $200/hr |
| Average Clutch project cost | $103,611 |
| Average monthly project cost | $7,165 |

### What Clients Actually Pay For (Ranked by Value)

**1. Strategy & Account Architecture ($$$)**
- Channel selection (Google vs. Meta vs. LinkedIn vs. TikTok)
- Campaign structure design
- Audience strategy
- Budget allocation across platforms
- KPI framework and measurement plan

**2. Initial Account Setup & Launch ($$$)**
- 15-25 hours of front-loaded work
- Keyword research, negative keyword lists
- Ad copy creation
- Conversion tracking implementation
- Campaign configuration

**3. Ongoing Optimization & Monitoring ($$)**
- Search term management
- Bid/budget adjustments
- A/B testing
- Performance monitoring
- Negative keyword updates

**4. Reporting & Analytics ($$)**
- Monthly performance reports
- Cross-platform consolidation
- ROI attribution
- Written insights and recommendations
- Data visualization

**5. Creative Services ($$)**
- Ad copy testing
- Image/video creative direction
- Landing page recommendations
- Creative rotation management

**6. Audits & Assessments ($$)**
- Account health audits
- Competitive analysis
- Conversion tracking audits
- Wasted spend identification

### What Could Be Automated (and What the Plugin Suite Should Target)

| Service | Hours/month | Agency charges | Automatable by plugin? |
|---------|-------------|---------------|----------------------|
| Search term review + negatives | 4-8 hrs | $600-1,600 | **Yes -- highest priority** |
| Performance reporting | 4-8 hrs | $600-1,600 | **Yes -- cross-platform summary** |
| Budget pacing + alerts | 2-4 hrs | $300-800 | **Yes -- already in scope** |
| Account health audit | 4-8 hrs/quarter | $2,000-5,000 | **Yes -- 60-point automated audit** |
| Conversion tracking audit | 2-4 hrs/quarter | $300-800 | **Partially -- can check config** |
| Creative fatigue monitoring | 2-4 hrs | $300-800 | **Yes -- cross-platform creative health** |
| Competitive monitoring | 2-4 hrs | $300-800 | **Partially -- auction insights** |
| Landing page alignment | 1-2 hrs | $150-400 | **Partially -- message match check** |

**Total automatable value per client:** $2,250-6,800/month in agency billable hours.

---

## 9. The Competitive Tool Landscape

### Current PPC Tools and What They Automate

| Tool | Price | What it automates | What it doesn't |
|------|-------|-------------------|-----------------|
| **Optmyzr** | $209+/mo | Rule-based automation, bid management, reporting, PMax control | No AI agent integration, no cross-platform narrative |
| **Adalysis** | $149+/mo | 100+ prebuilt audits/alerts, ad testing | Google-only, no workflow intelligence |
| **Skai** | $90K/yr | Enterprise multi-channel management | Enterprise-only, massive overhead |
| **TrueClicks** | $208+/mo | Auditing, budget pacing | Limited platform support |
| **Madgicx** | $31+/mo | Meta-specific optimization, creative intelligence | Meta-only |
| **NinjaCat** | Custom | Multi-source reporting consolidation | Reporting only, no optimization |
| **Adspirer** | $0-199/mo | MCP-based tool calls across 4 platforms | No workflow intelligence, no practitioner credibility |
| **Adzviser** | $34.99/mo | 18 data sources, MCP connectivity | Broad data focus, not PPC-specialized |

### The White Space for Ch47

None of the above tools combine:
1. AI agent integration (Claude-native)
2. Practitioner-built workflow intelligence
3. Cross-platform analysis in natural language
4. Client-ready narrative output
5. Safety guardrails (read-only default, dry-run mutations)
6. Generous free tier for adoption
7. Open-source transparency

Ch47 doesn't need to compete feature-for-feature. It needs to own the intersection of "Claude + PPC practitioner intelligence."

---

## 10. The 100x Plugin Suite: What to Build

### Tier 1: Ship Now (already in scope, highest adoption impact)

1. **Morning Brief** — Multi-account health check (spend, pacing, anomalies)
2. **Waste Detection** — Bad search terms, zero-conversion keywords, budget misallocations
3. **Search Term Classifier** — Categorize and recommend negatives at scale
4. **PMax Decoder** — Search terms, channel mix, asset performance for the black box
5. **Budget Pacer** — Real-time pacing vs. targets with alerts
6. **Account Audit** — Comprehensive health check (start with top 20 items, expand to 60)

### Tier 2: Build Next (highest differentiation vs. Adspirer)

7. **Cross-Platform Performance Summary** — Unified Google + Bing + Meta metrics in one query, normalized, with written narrative and period-over-period comparison
8. **Client Report Generator** — Written performance summary ready for client delivery, not raw data dumps
9. **Creative Fatigue Monitor** — Track CTR decay, CPM trends, frequency across platforms, alert before performance tanks
10. **Conversion Tracking Auditor** — Verify tracking is firing, check for duplicates, validate enhanced conversions setup, compare platform-reported conversions vs. GA4
11. **Negative Keyword Architect** — Not just recommendations but structured lists by theme, shared across campaigns, with conflict detection

### Tier 3: Build for Moat (what agencies will pay premium for)

12. **60-Point Account Audit** — Full automated audit with written findings document, prioritized recommendations, and estimated waste calculation
13. **Budget Allocation Advisor** — Cross-platform diminishing returns detection, reallocation signals, seasonal modeling
14. **Audience Health Dashboard** — Cross-platform audience freshness, overlap indicators, exclusion validation
15. **Competitor Intelligence** — Auction insights analysis, impression share trends, competitor ad copy monitoring
16. **First-Party Data Quality Checker** — CRM list freshness, match rates across platforms, upload cadence monitoring
17. **Landing Page Alignment Scorer** — Compare ad copy to landing page content, flag mismatches

### Tier 4: Future / Premium

18. **Multi-Account Portfolio View** — Agency-level performance across all clients, flag accounts needing attention
19. **Anomaly Detector** — Background monitoring for spend spikes, CPA changes, impression share drops
20. **QBR Generator** — Quarterly business review document with year-over-year trends, strategy recommendations
21. **Onboarding Auditor** — When an agency takes over a new account, run the full diagnostic and generate the "here's what we found" pitch deck

---

## 11. MCP + Claude in PPC: Current State

### What Practitioners Are Already Doing

> "I use a MCP server with most of Google and Bing's APIs and I now do all my keyword research, competitive analysis on Claude desktop." — r/PPC, 2 upvotes

> "MCP automation in PPC -- I employ it to make bid adjustments and keyword management more efficient... Most of the automated functions are real-time performance alerts." — r/PPC

> "Updating copy at scale. Data analytics is highly questionable with LLMs, let alone MCP." — r/PPC (skeptic)

### The Awareness Gap

MCP awareness in r/PPC is still early but growing. One thread "How are you using MCP automation in PPC?" had 6 comments -- mostly people unsure how to use it. Another commenter said "I have no idea how I would use an MCP with Google Ads."

**This is the education opportunity.** Ch47 can own the "here's how to use Claude for PPC" narrative before it becomes crowded.

### The Trust Barrier

PPC practitioners are deeply skeptical of AI tools because Google's own AI has burned them repeatedly. Any plugin that reads like "AI will manage your ads" will face immediate resistance. The positioning must be:
- "I built this for my own accounts"
- "Read-only by default"
- "It catches things, it doesn't change things"
- "Show me the search terms, not 'we optimized your campaign'"

---

## 12. Key Takeaways for Ch47

### The Biggest Opportunity

**Cross-platform intelligence with practitioner-grade narrative.** Every tool in the market is either:
- Per-platform (Optmyzr = Google, Madgicx = Meta)
- All-platform but raw data (Adspirer = 100 tools, no intelligence)
- All-platform but enterprise-priced (Skai = $90K/yr)

Nobody does cross-platform PPC intelligence accessible to a solo consultant or small agency via Claude. That's the white space.

### The Highest-Value Workflows to Prioritize

1. **Automated account audit** (worth $2-5K in consulting value, highest "wow" moment)
2. **Cross-platform performance summary** (saves 3-5 hrs/client/month, biggest daily value)
3. **Search term classification at scale** (catches $3K+/month in waste, proven value)
4. **Creative fatigue detection** (prevents silent performance decay)
5. **Client report narrative generation** (replaces the most-hated weekly task)

### The Moat Strategy

1. **Workflows are the head start** -- ship opinionated, practitioner-built intelligence that knows what to check
2. **Distribution is the position** -- first paid media plugin in Claude marketplace
3. **Habit is the lock-in** -- daily morning brief becomes indispensable
4. **Trust is the currency** -- practitioner credibility via Reddit, workshops, Build Notes
5. **Content SEO is the long game** -- capture "Claude + PPC" search intent before Adspirer owns it completely

### What NOT to Build

- Don't compete on tool count (Adspirer has 100+, so what)
- Don't build a dashboard (practitioners are drowning in dashboards)
- Don't automate bid management (Google/Meta already do this)
- Don't promise autonomy (practitioners distrust autopilot after Google's AI)
- Don't go enterprise-first (agencies with 5-50 people are the sweet spot)

---

## Sources

### Reddit Threads Referenced
- [What's your biggest day to day frustration in PPC right now?](https://www.reddit.com/r/PPC/comments/1op1f5e/) — r/PPC
- [Does anyone else feel like PPC is a miserable job?](https://www.reddit.com/r/PPC/comments/1qxlnz7/) — r/PPC, 86 upvotes, 104 comments
- [I've audited 50+ Google Ads accounts spending $10K+/month](https://www.reddit.com/r/PPC/comments/1o6hva6/) — r/PPC, 133 upvotes
- [What tools/checklists do you use for an account audit?](https://www.reddit.com/r/PPC/comments/1rdmdjm/) — r/PPC
- [Why feeding Google better data is becoming the biggest lever in PPC](https://www.reddit.com/r/PPC/comments/1nf5wvs/) — r/PPC, 91 upvotes
- [How to manage PPC when budgets shift monthly? ($150k+ spends)](https://www.reddit.com/r/PPC/comments/1n32efn/) — r/PPC, 22 upvotes
- [The problem with uploading first party data to google ads](https://www.reddit.com/r/PPC/comments/1remi2g/) — r/PPC
- [Freelancers and agency owners who send reports to clients](https://www.reddit.com/r/digital_marketing/comments/1qyd5z3/) — r/digital_marketing
- [How are you using MCP automation in PPC?](https://www.reddit.com/r/PPC/comments/1p28qfy/) — r/PPC
- [What AI or Paid Tools you use for Google Ads PPC?](https://www.reddit.com/r/PPC/comments/1mdr672/) — r/PPC, 24 upvotes
- [Meta Ads: How do you actually identify creative fatigue?](https://www.reddit.com/r/FacebookAds/comments/1qk70et/) — r/FacebookAds
- [How do you decide which ad creative to test first on Meta?](https://www.reddit.com/r/FacebookAds/comments/1qgd0ox/) — r/FacebookAds
- [MCP Server + Google Ads + Meta Ads with AI](https://www.reddit.com/r/PPC/comments/1r30hsz/) — r/PPC
- [Google Ads click fraud is killing any confidence](https://www.reddit.com/r/PPC/comments/1qo1hgg/) — r/PPC, 92 upvotes
- [CPL across all major channels is up 40%+ over 2 years](https://www.reddit.com/r/digital_marketing/comments/1rfo2nc/) — r/digital_marketing

### Industry Sources
- [60-Point PPC Audit Checklist](https://biglinden.com/ppc-audit-checklist/) — Big Linden
- [PPC Management Pricing Guide 2025](https://agencyanalytics.com/blog/ppc-pricing) — AgencyAnalytics
- [Best PPC Automation Tools 2026](https://www.optmyzr.com/blog/best-ppc-automation-tools/) — Optmyzr
- [Adalysis vs Optmyzr Comparison](https://adalysis.com/tool-comparisons/optmyzr/) — Adalysis
- [Adspirer Documentation](https://www.adspirer.com/documentation) — Adspirer
- [Adspirer Skill Reference](https://www.adspirer.com/docs/agent-skills/skills) — Adspirer
- [Adspirer Performance Marketing Agent](https://www.adspirer.com/docs/agent-skills/agent) — Adspirer
- [Best Automated Creative Testing Platforms 2026](https://www.admetrics.io/en/post/best-automated-creative-testing-platforms) — Admetrics
- [Creative Fatigue in 2025](https://www.singular.net/blog/creative-fatigue/) — Singular
- [Best Marketing Budget Allocation Software 2026](https://www.cometly.com/post/marketing-budget-allocation-software) — Cometly
- [Cross Platform Ad Tracking Tools 2026](https://www.cometly.com/post/cross-platform-ad-tracking) — Cometly
- [Scaling Paid Media: Claude Code CLI](https://stormy.ai/blog/scaling-paid-media-claude-code-ads-mcp) — Stormy AI
- [PPC Automation with ChatGPT and Claude](https://www.adspirer.com/blog/ppc-automation-chatgpt-claude) — Adspirer
- [5 Paid Media Predictions for 2026](https://befoundonline.com/blog/5-paid-media-predictions-for-2026-why-youre-still-the-boss) — Be Found Online
- [Paid Media Trends for 2026](https://www.greenlanemarketing.com/resources/articles/paid-media-ppc-trends-predictions-for-2026) — Greenlane Marketing
