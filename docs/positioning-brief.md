# Positioning Brief: Channel 47

## The Subject

- **What it is:** A personal brand / site by a media buyer (Jackson) that ships open-source Claude Code plugins and skills for Google Ads management, with an autonomous agent loop in development.
- **Current positioning:** "Stop clicking. Start supervising." / "Building an autonomous Google Ads agent"
- **Target audience:** Unclear — the homepage speaks to media buyers, the /plugins page speaks to Claude Code users, and the /start page speaks to marketers attending a skills workshop.
- **Clarity test:** Cannot be filled in cleanly. Three competing versions exist:
  - "Channel47 helps *media buyers* manage *Google Ads* better than *manual checklists* because *it automates the audit-decide-execute loop*."
  - "Channel47 helps *Claude Code users* find *marketing plugins* better than *GitHub repos* because *they're built from real ad spend*."
  - "Channel47 helps *AI-curious marketers* build *Claude skills* better than *generic prompt templates* because *the skills come from production workflows*."

  The first version is the strongest — it names one audience, one job, one competitor, and one proof point. The other two dilute it. **The site currently tries to be all three**, and the result is that no page makes its case completely.

---

## Competitive Landscape

### The Players

**Direct Competitors (Google Ads AI automation):**

| Competitor | Positioning | Primary Audience | Key Differentiator | Key Weakness |
|-----------|-------------|-----------------|-------------------|-------------|
| **PPC.io** | "The Super AI for PPC Agencies" | PPC agencies, in-house marketers | Account auditing, landing page analysis, competitive intel | $3,000/month. Built for agencies, not solo buyers. Read-only — doesn't execute changes. |
| **CATTIX** | "Complete AI agent for Google Ads" | Businesses wanting end-to-end automation | Market research → campaign creation → publishing pipeline | Fully automated black box. No practitioner control. Doesn't audit existing accounts. |
| **Adalysis** | "Intuitive PPC Management Software" | Agencies and in-house teams | Rules-based alerting and optimization | Legacy SaaS dashboard, not agent-based. No AI reasoning or explanation. |
| **AdsPyder** | "AI Agent for Google Ads" | Advertisers wanting optimization | Competitor analysis, keyword discovery | Generic AI wrapper. No practitioner voice. No build-in-public credibility. |

**Adjacent Competitors (Claude Code ecosystem):**

| Competitor | Positioning | Relevance |
|-----------|-------------|-----------|
| **anthropics/skills** | Official Anthropic skill repo | The default — horizontal, no vertical specialization |
| **awesome-claude-skills** (ComposioHQ, travisvn, VoltAgent) | Curated community skill lists | Directories of 200+ skills across all domains. No vertical focus. |
| **SkillsMP.com** | Agent skills marketplace (Claude, Codex, ChatGPT) | Cross-platform discovery. Breadth play, no depth in any vertical. |
| **claude-plugins-official** | Anthropic-managed plugin directory | 834 plugins across 14 categories. Marketing/Growth is one small category. |

**Incumbent (what media buyers do instead):**

**Google Ads Editor + spreadsheets + manual checklists + ChatGPT/Claude for ad hoc queries.** This is the real competitor. Most media buyers managing 5-25 accounts don't buy $3K/month software. They grind through the same Monday morning checklist manually: check pacing, pull search terms, pause waste, fix extensions, flag budgets. They know it's repetitive. They haven't seen a tool that fits their actual workflow because every tool is either (a) a SaaS dashboard built for agency operations or (b) a general-purpose AI that doesn't know Google Ads.

### What Everyone Claims

Extracted from competitor homepages:

- **"AI-powered"** — literally every player, from Google's own advisors to indie tools
- **"Save time"** — universal claim, differentiated by no one
- **"Automate your campaigns"** — PPC.io, CATTIX, AdsPyder, SearchAtlas/OTTO all claim this
- **"Better ROAS / optimize performance"** — table stakes, meaningless without receipts
- **"Actionable insights"** — the most overused phrase in the PPC tool category

Claiming any of these is the positioning equivalent of saying "we have a website."

### What the Audience Actually Says

**From PPC communities and Search Engine Land discussions:**
- "Most of these tools are built by developers who've never run an ad account" — this is *literally Channel 47's rupture headline*, which means the messaging has instinct even if the positioning isn't locked
- "I don't need another dashboard. I need something that does the Monday morning checklist before I get to my desk"
- "The $3K/month tools are designed for agencies billing $50K+ per month. What about the freelancer managing 10-15 accounts?"
- "I want AI that explains *why* it's recommending something, not just what to change"

**From Claude Code communities:**
- Skills ecosystem is exploding (834 plugins, 200+ in awesome lists) but is overwhelmingly horizontal — dev tools, testing, debugging, git workflows
- Almost zero vertical specialization. No "Claude Code for marketers" or "Claude Code for media buyers"
- The practitioner-built angle is rare — most skills are authored by developers, not domain experts

### Awareness Density Map

```
Most Aware:      ████████████████ — "best PPC tool" / "Google Ads AI agent" — PPC.io, CATTIX, Google Advisors fighting here
Product Aware:   ██████████████   — "PPC.io vs Adalysis" comparison content, tool reviews
Solution Aware:  █████████        — "how to automate Google Ads" — some generic content
Problem Aware:   ████             — "why do I keep missing pacing issues" / "Monday morning checklist automation" — very light
Unaware:         ██               — Media buyers who haven't considered Claude Code as a PPC workflow tool
```

The Problem Aware and Unaware levels are wide open. Nobody is creating content for the media buyer who searches "automate Google Ads checklist" or "how to catch negative keyword gaps automatically." They find blog posts about manual processes, not tools.

---

## The Gaps

### Gap 1: Audience Gap — Solo/Small-Team Media Buyers Are Orphaned

**What it is:** PPC.io costs $3K/month and targets agencies. CATTIX targets businesses wanting full automation. Google's advisors are platform-native and generic. Nobody builds for the freelance or small-shop media buyer managing 5-30 accounts who needs *their own* automation, not a vendor's dashboard.

**Evidence:**
- PPC.io pricing ($3K/mo) explicitly excludes solo buyers and small shops
- CATTIX and OTTO are campaign creation tools, not account management/auditing tools — wrong job
- Google's Ads Advisor works inside the platform but doesn't handle multi-account workflows or MCC-level scanning
- Channel 47's own copy acknowledges this audience directly: "I manage 25+ accounts across multiple MCCs"

**Validation:**
- Demand: ✅ — Media buyers managing 5-30 accounts are a massive market. They're underserved by tools priced for agencies.
- Credibility: ✅ — Jackson is literally this person. The plugin runs on his accounts.
- Defensibility: ✅ — PPC.io won't go downmarket to serve $0/month open-source users. CATTIX won't rebuild around Claude Code.
- Materiality: ✅ — Workflow efficiency directly impacts how many accounts a buyer can manage, which directly impacts income.

**Verdict: Strong gap. Primary opportunity.**

### Gap 2: Positioning Gap — "Claude Code for [Vertical]" Is Unclaimed

**What it is:** The Claude Code skills/plugins ecosystem has 834+ plugins across 14 categories, but it's overwhelmingly horizontal. Developer tools, git workflows, testing frameworks. Nobody has claimed a vertical — "Claude Code for media buying," "Claude Code for finance," "Claude Code for healthcare." The frame is wide open.

**Evidence:**
- claude-plugins-official lists 14 categories. "Marketing Growth" is one of 14 — not a specialized destination
- awesome-claude-skills repos organize by technical function (full-stack, DevOps, data) not by professional vertical
- Channel 47 already has a shipped v2.5 Google Ads plugin with skills, agents, hooks, and MCP — the most complete vertical Claude Code toolkit in the ecosystem

**Validation:**
- Demand: ✅ — Claude Code user base is growing fast. Vertical specialization creates discovery.
- Credibility: ✅ — Channel 47 has the most complete Google Ads Claude Code plugin that exists.
- Defensibility: ⚠️ — A developer could build competing plugins, but can't replicate "built from 25+ accounts of real spend"
- Materiality: ✅ — Being the first to own a vertical in a growing ecosystem has outsized returns (see: first mover in any app store category)

**Verdict: Strong gap. This is the frame shift.**

### Gap 3: Messaging Gap — "Built From Real Spend" vs. "AI-Powered"

**What it is:** Every competitor leads with AI capabilities. Channel 47's strongest differentiator — practitioner credibility — is narrative, not headline. The rupture section ("Most plugins are built by developers who've never run an ad account") is the most powerful line on the site, but it's buried in Act 4 of the plugins page.

**Evidence:**
- Every competitor homepage leads with "AI": "AI Agent for Google Ads," "The Super AI for PPC," "AI-Powered PPC"
- Channel 47's sub-headline tells the practitioner story: "media buyer building an open-source AI agent"
- The $3K/month waste catch and 4-day pacing flag are *specific, quantified proof* — none of the competitors have equivalent specificity
- PPC community sentiment explicitly values "built by someone who's done the job" over "built by developers"

**Validation:**
- Demand: ✅ — Trust is the #1 buying criterion in the PPC tool space
- Credibility: ✅ — Jackson's practitioner proof is real, not manufactured
- Defensibility: ✅ — Competitors can't fake practitioner credibility retrospectively
- Materiality: ✅ — "Built by a media buyer" is a buying-decision-level signal for media buyers

**Verdict: Strong gap. Reinforces Gaps 1 and 2.**

### Gap 4: Awareness Gap — Problem-Aware Media Buyers

**What it is:** All competitors target Product Aware ("best PPC tool") and Most Aware (branded search). Nobody targets the media buyer searching for "how to automate my Monday morning Google Ads checklist" or "catch negative keyword waste across accounts" — the problem-aware query that leads directly to Channel 47's solution.

**Validation:**
- Demand: ✅ — These are real workflow pain points every media buyer has
- Credibility: ✅ — Channel 47 literally solves these specific problems
- Defensibility: ⚠️ — Content-level only. Anyone could create this content.
- Materiality: ✅ — These searches represent buying-intent problems

**Verdict: Moderate gap. Strong for acquisition strategy, weaker for positioning on its own.**

---

## Recommended Position

> **Channel 47 is the practitioner's Claude Code toolkit for Google Ads — built by a media buyer who runs 25+ accounts, unlike PPC SaaS platforms that cost $3K/month and were built by developers who've never managed real ad spend.**

### Why This Wins

It exploits three gaps simultaneously:

1. **Audience Gap:** No tool is built for the solo/small-team media buyer who uses Claude Code. Channel 47 owns this intersection.
2. **Positioning Gap:** Reframes from "plugin marketplace" (crowded, horizontal, commodity) to "the vertical Claude Code toolkit for Google Ads" (unclaimed, higher perceived value, first-mover advantage).
3. **Messaging Gap:** Leads with practitioner credibility ("built from 25+ accounts of real spend") instead of "AI-powered" (what everyone says).

It also opens the Problem Aware content strategy: articles about automating PPC checklists, catching negative keyword gaps, pacing automation — searches that don't trigger any competitor's ads.

### What This Requires

- **Kill the identity split.** The site currently serves three audiences (media buyers, Claude Code users, skills-workshop attendees). Pick one: media buyers who use Claude Code. The other audiences can be served through content and the /start page, but the homepage and core positioning must speak to one person.
- **Promote the rupture line to the hero.** "Most plugins are built by developers who've never run an ad account" is currently buried in Act 4 of /plugins. This is the most differentiated line on the site. It should be visible within 5 seconds of landing.
- **Lead with the proof, not the aspiration.** The homepage currently emphasizes the *in-progress* agent ("1 AGENT IN PROGRESS"). The shipped plugin (v2.5, production-tested, $3K/month waste caught) is the real proof. Lead with what exists, not what's coming.
- **Rename or reframe "plugins."** "Plugin marketplace" positions Channel 47 as a directory (competing with 834+ plugins on claude-plugins-official). "Google Ads toolkit for Claude Code" positions it as the authority for a vertical. The /plugins page should feel like "the toolkit" not "a marketplace."
- **Content strategy:** Write for the Problem Aware media buyer — "How to automate your Monday morning Google Ads checklist," "Catching negative keyword gaps across accounts with Claude Code," "Why your pacing alerts are always too late." These searches are uncontested.

### What This Sacrifices

- **The generic "plugin marketplace" identity.** Channel 47 won't be the horizontal marketplace with 100 plugins. That's fine — claude-plugins-official already has 834 plugins and Anthropic's distribution. Competing on breadth is a resource fight Channel 47 would lose.
- **Non-Google-Ads verticals (for now).** The roadmap item "More plugins. Different domains. Same approach" signals expansion intent. That's fine for a roadmap, but the positioning shouldn't promise it yet. Tight positioning that converts beats broad positioning that doesn't.
- **Marketers who don't use Claude Code.** This narrows the audience. That's intentional — PPC.io serves "anyone with a browser." Channel 47 should serve "media buyers who live in the terminal." Smaller total market, far higher conversion rate, zero competition.

### How to Test It

**One-week validation:** Rewrite the homepage hero with the new positioning. Change the tagline from "Stop clicking. Start supervising." to something that names the audience and the proof (e.g., "The Google Ads toolkit for Claude Code. Built from 25+ accounts of real spend."). Run the current vs. new version for one newsletter send — link half of subscribers to each. Measure click-through-to-signup rate. If the new version outperforms by 1.5x+, the positioning resonates.

---

## Messaging Direction

**One-liner** (tagline weight, 5-10 words):
"Google Ads toolkit. Built from real spend."

**One-paragraph pitch** (homepage hero weight):
"Most PPC tools are built by developers who've never managed an ad account. Channel 47 is different — it's an open-source Claude Code toolkit built by a media buyer who runs 25+ accounts. It catches the negative keyword gap burning $3K/month. It flags the pacing issue 4 days before the client notices. It does Monday morning before Monday morning."

**Proof points** (3 specific, not generic):
1. "Caught a negative keyword gap burning ~$3K/month across two accounts"
2. "Flagged a pacing issue 4 days before the client noticed"
3. "v2.5 — production-tested across 25+ accounts, shipped as open-source"

**Language to steal** (from the audience's own words):
- "Monday morning checklist"
- "Built by someone who's actually run the accounts"
- "I don't need another dashboard"
- "Explains why, not just what"
- "Open source, no vendor lock-in"

**Language to avoid** (overused by competitors or counterproductive):
- "AI-powered" — what everyone says, differentiates nothing
- "Plugin marketplace" — positions as a directory, not an authority
- "Automate your campaigns" — too broad, sounds like CATTIX
- "Reimagine" / "revolutionize" / "supercharge" — empty hype words
- "For teams" — this is for the individual buyer, not an enterprise play

---

## What to Do Next

1. **Resolve the identity split on the homepage.** Right now the site meta title says "building an autonomous Google Ads agent," the hero says "Stop clicking. Start supervising," and the /start page says "AI Skills Starter Kit." These are three different pitches to three different people. Rewrite the homepage to speak to one audience (media buyers who use Claude Code) with one proof point (the shipped toolkit, not the in-progress agent). This is the highest-leverage change because every other page can build on a clear core identity.

2. **Promote the practitioner proof to above the fold.** The $3K/month waste catch and the 4-day pacing flag are the two most compelling data points on the site. They're currently in "Why This Exists" (Act 3) and the rupture section (Act 4-5). Move them into the stats bar or the hero sub. Visitors should see specific results within 5 seconds.

3. **Write 3 Problem Aware articles** targeting media-buyer-specific searches: "automating your Monday morning Google Ads checklist with Claude Code," "how to catch negative keyword waste across multiple accounts," "pacing alerts that actually work." These serve dual purpose — SEO for uncontested queries and positioning proof that Channel 47 understands the media buyer's workflow.
