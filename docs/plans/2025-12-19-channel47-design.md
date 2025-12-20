# Channel 47 - Design Document

**Date:** 2025-12-19
**Status:** Approved

---

## Overview

Channel 47 is a digital assets marketplace and content hub targeting Claude Code / agentic IDE power users. The site serves two functions:

1. **Blog** - AI-assisted "build-in-public" content derived from real work sessions
2. **Marketplace** - Claude Code skills, plugins, MCP servers, and prompts

### Core Insight

Instead of traditional build-in-public (daily updates, constant sharing), Channel 47 captures valuable conversations as they happen naturally, then uses an LLM pipeline to transform them into polished content. Work becomes marketing.

### Strategic Positioning

- **Primary audience:** Claude Code and Cursor power users (115k-1M+ and growing)
- **Differentiation:** Performance marketing expertise + practitioner credibility
- **Moat:** First-mover SEO advantage in low-competition, high-growth keyword space
- **Business model:** Audience-first, marketplace as monetization layer
- **Distribution:** Blog/SEO (organic), X/Twitter (engagement), Reddit (community)

---

## Market Analysis

### Total Addressable Market Funnel

```
Global developers:                          ~30,000,000
AI coding tool users (any):                 ~20,000,000
Agentic tool users (Claude Code + Cursor):  ~1,200,000
Power users willing to pay:                 ~120,000-240,000
Actively seeking third-party tools:         ~12,000-24,000
```

### Realistic Addressable Market

- **Primary:** Claude Code power users - 50,000-100,000
- **Secondary:** Performance marketers using AI tools - 5,000-15,000
- **Total:** 55,000-115,000 people

### Revenue Projections

| Scenario | Market Capture | Paying Customers | Avg Revenue | Annual Revenue |
|----------|---------------|------------------|-------------|----------------|
| Conservative | 1% | 550-1,150 | $50/year | $27k-$57k |
| Moderate | 3% | 1,650-3,450 | $100/year | $165k-$345k |
| Optimistic | 5% | 2,750-5,750 | $150/year | $412k-$862k |

### Strategic Value Beyond Revenue

The real play is compounding effects:
- X audience in AI/dev niche (attention is scarce)
- SEO authority for Claude Code content (low competition now)
- Personal brand as "the Claude Code guy" (career optionality)
- Performance marketing + AI expertise intersection (consulting opportunities)

---

## Brand Identity

- **Name:** Channel 47
- **Mascot:** Retro TV-headed robot (warm coral/red palette, friendly CRT face)
- **Aesthetic:** Clean minimalist, Apple-inspired restraint
- **Palette:** Coral/red, cream/white, charcoal
- **Voice:** Practitioner sharing real work, not guru dispensing advice

---

## System Architecture

### Three Core Systems

```
┌──────────────┐    ┌──────────────┐    ┌──────────────────────────┐
│   CAPTURE    │    │  SYNTHESIS   │    │        PUBLISH           │
│   SYSTEM     │───▶│   PIPELINE   │───▶│        LAYER             │
└──────────────┘    └──────────────┘    └──────────────────────────┘

conversation-       GitHub Actions      Astro site on Vercel
logger skill        + Claude API        + Stripe payments
```

### 1. Capture System (Existing)

- Existing `conversation-logger` skill
- Saves markdown transcripts to GitHub repository
- Triggered manually when valuable content emerges

### 2. Synthesis Pipeline (To Build)

- GitHub Action watches `logs/` directory
- On new log: calls Claude API to generate blog post + X content
- Creates PR with drafts for review
- On merge: triggers site rebuild

### 3. Publish Layer (To Build)

- **Astro static site** - blog posts, product pages, landing pages
- **Vercel hosting** - auto-deploys on push, serverless functions for payments
- **Stripe integration** - checkout, subscriptions, license delivery

### Repository Structure

```
channel47/
├── logs/              # Raw conversation transcripts
├── drafts/            # LLM-generated drafts (PRs created here)
├── src/               # Astro site source
│   ├── content/
│   │   ├── blog/      # Published posts (markdown)
│   │   └── products/  # Product listings (markdown + metadata)
│   └── pages/
├── functions/         # Vercel serverless (Stripe webhooks)
└── .github/workflows/ # Synthesis pipeline
```

---

## Content Pipeline

### Flow

```
conversation-logger → logs/ repo → GitHub Action triggers
                                        │
                                        ▼
                                  LLM synthesizes:
                                   ├─ Blog post draft
                                   └─ X content drafts
                                        │
                                        ▼
                                    Creates PR
                                        │
                                        ▼
                                  You review/merge
                                   ├─ Blog auto-publishes
                                   └─ X drafts → manual posting
```

### Content Format

Hybrid format - polished narrative with embedded conversation snippets:

```markdown
# How I Built a Claude Code Skill for X

[Polished intro - the problem, why it matters]

[Narrative section - what I tried first]

> **Me:** How do I handle the edge case where...
> **Claude:** You could approach this three ways...

[Analysis - why I chose option 2]

[Conclusion - what I learned, link to skill in marketplace]
```

### Expected Cadence

- **Input:** 3-5 meaningful conversations per week
- **Output:** 2-3 blog posts per week + daily X presence

### Distribution Channels

**Blog/SEO (Primary)**
- Organic search traffic from Claude Code keywords
- Long-form content optimized for discovery
- Builds authority over time

**X/Twitter (Engagement)**
- Daily presence with conversation snippets
- Thread format for key insights
- Link back to blog posts
- Build personal brand

**Reddit (Community)**
- Target subreddits: r/ClaudeAI, r/ChatGPT, r/LocalLLaMA, r/artificial, r/MachineLearning
- Share valuable tools and insights (no spam)
- Participate authentically in discussions
- Link to tools and blog posts when contextually relevant
- Community-first approach builds trust

---

## Marketplace Structure

### Pricing Strategy

**Phase 1: All Free (List Building)**

```
ALL PRODUCTS FREE
─────────────────
• All skills, plugins, MCP servers, prompts
• Email gate for downloads
• Focus on audience growth
• Establish authority and trust
```

**Phase 2: Introduce Paid Tiers (Future)**

```
FREE TIER              ONE-TIME PURCHASE        SUBSCRIPTION
──────────             ─────────────────        ────────────
• Basic skills         • Premium skills         • All products
• Starter prompts      • MCP servers            • Early access
• Email gate only      • Plugin bundles         • Private Discord?
                       • $10-50 each            • $15-20/month

Goal: List building    Goal: Revenue            Goal: Recurring rev
```

**Rationale:** Build audience first, monetize later. Free products with email gates maximize distribution while building the list that will convert to paid products in Phase 2.

### Positioning: Curated Directory

Channel 47 is both a **creator** and **curator**:
- List own tools alongside third-party community tools
- Give full credit to original creators
- One-stop shop for Claude Code ecosystem
- Build authority through curation, not just creation

### Product Content Structure

```yaml
# src/content/products/smart-commit-skill.md
---
title: "Smart Commit Skill"
description: "AI-powered commit messages that actually make sense"
price: 0               # Phase 1: all free
tier: "free"           # free only for Phase 1
category: "skill"      # skill | plugin | mcp-server | prompt
author: "Your Name"    # NEW: Creator attribution
authorUrl: "https://x.com/yourhandle"  # NEW: Creator link
sourceUrl: "https://github.com/you/repo"  # NEW: Source repository
downloadFile: "smart-commit-skill.zip"
featured: true         # NEW: Highlight quality picks
---

Full product description, screenshots, usage instructions...
```

### Download Flow

**Phase 1: Email Gate (All Free)**

```
Product page → Email signup → Delivery email → Download link
  (Download)     (capture)      (instant)        (direct)
```

**Phase 2: Paid Products (Future)**

```
Product page → Stripe Checkout → Webhook confirms → Delivery email
    (Buy)                          payment            + download link
```

### Key Components (Phase 1)

1. **Email capture form** - Collect email before download
2. **Delivery email** - Send download link via Resend
3. **Direct download** - Simple file delivery (no tokens needed initially)
4. **List building** - All emails added to newsletter list

### Key Components (Phase 2 - Future)

1. **Checkout** - Vercel serverless creates Stripe Checkout session
2. **Webhook handler** - Listens for `checkout.session.completed`
3. **License generation** - Creates unique download token
4. **Delivery** - Sends email with secure, time-limited download link
5. **Subscription portal** - Stripe Customer Portal for management

---

## Tech Stack

| Component | Choice | Cost |
|-----------|--------|------|
| Site framework | Astro | Free |
| Hosting | Vercel | Free tier |
| Payments | Stripe | 2.9% + $0.30/tx |
| Email | ConvertKit / Buttondown | Free tier |
| Analytics | Vercel Analytics / Plausible | Free / $9/mo |
| LLM API | Claude API | ~$10-30/mo |
| Domain | channel47.com (or similar) | ~$12/year |

**Estimated monthly cost at launch:** $10-50/month

---

## Phased Rollout

### Phase 1: Foundation (MVP)

**Infrastructure:**
- Set up GitHub repo structure
- Astro site scaffold with brand styling
- Deploy to Vercel
- Basic pages: home, blog index, about

**Content Pipeline:**
- GitHub Action for log detection
- Claude API integration for synthesis
- PR creation workflow
- Auto-deploy on merge

**Marketplace (Basic):**
- Product listing pages
- Email gate for downloads
- Delivery via Resend
- 5-10 products live (mix of own + curated third-party tools)

**Launch:**
- 5+ blog posts queued
- X presence established
- Email capture working
- Soft launch, gather feedback

### Phase 2: Monetization & Scale

- **Introduce paid tiers** (Stripe integration: one-time + subscriptions)
- **Premium products** (advanced skills, plugin bundles, exclusive MCP servers)
- **Subscription tier** (all products + early access + private community)
- Podcast generation (NotebookLM / ElevenLabs integration)
- X auto-scheduling (Typefully/Buffer integration)
- Product catalog expansion (30+ items)
- SEO optimization (based on search console data)
- Referral/affiliate program

### Out of Scope

- User accounts / login system (use Stripe Customer Portal)
- Comments / community features
- Multiple contributors
- Mobile app

---

## Success Metrics

### Leading Indicators (Weekly)

- Conversations logged
- Blog posts published
- X impressions/engagement
- Site visitors
- Email signups

### Lagging Indicators (Monthly)

- Total revenue
- Email list size
- Paying customers
- Subscriber count
- Search rankings

### 90-Day Targets

| Metric | Target |
|--------|--------|
| Blog posts published | 20-30 |
| Email list | 500 |
| X followers | 1,000 |
| Free downloads | 200 |
| Paid customers | 20-50 |
| Revenue | $500-2,000 |

### 12-Month Targets

| Metric | Target |
|--------|--------|
| Monthly visitors | 5,000-10,000 |
| Email list | 3,000-5,000 |
| X followers | 5,000-10,000 |
| Paying customers (cumulative) | 300-500 |
| Monthly revenue | $2,000-5,000 |

### Pivot Signal

If after 90 days: <100 email signups and <10 paid customers, revisit positioning. The content pipeline remains valuable, but marketplace may need adjustment.

---

## Decisions Summary

| Category | Decision |
|----------|----------|
| Goal | Audience-first, marketplace as monetization |
| Primary channel | Blog/SEO, X promotes, Reddit community |
| Content format | Hybrid (narrative + conversation snippets) |
| Cadence | 3-5 conversations/week → 2-3 posts/week |
| Site framework | Astro (static) |
| Hosting | Vercel |
| Payments | None (Phase 1), Stripe (Phase 2) |
| Pipeline | GitHub Actions + Claude API |
| Capture | Existing conversation-logger skill |
| Review flow | PR workflow, approve before publish |
| Pricing model | All free (Phase 1), Hybrid tiers (Phase 2) |
| Phase 1 | All free, email gate, list building |
| Positioning | Curated directory + own tools |
| Attribution | Full credit to third-party creators |
| Brand | Clean minimalist, Apple-inspired |

---

## Changelog

### 2025-12-19 - Strategic Updates

**1. All Content Free Initially**
- **Change:** Removed paid tiers from Phase 1
- **Rationale:** Focus on audience building first, monetization later
- **Impact:**
  - All skills, plugins, MCP servers, and prompts will be free
  - Email gate for downloads to build list
  - No Stripe integration needed for Phase 1
  - Simplifies MVP implementation

**2. Add Reddit as Distribution Channel**
- **Change:** Added Reddit to content distribution strategy
- **Target subreddits:** r/ClaudeAI, r/ChatGPT, r/LocalLLaMA, r/artificial, r/MachineLearning
- **Content format:** Share blog posts, tools, and insights
- **Approach:** Community-first, value-first (no spam)

**3. Curated Directory Model**
- **Change:** Include third-party tools alongside own tools
- **Positioning shift:** From "my marketplace" to "curated directory + my tools"
- **Implementation:**
  - List other builders' plugins, skills, MCP servers
  - Give full credit to original creators
  - Link to their repos/sites
  - Intermix with own tools (not segregated)
  - Add metadata: `author`, `authorUrl`, `sourceUrl` to product schema
- **Benefits:**
  - More valuable to users (one-stop shop)
  - Builds authority as curator
  - Drives more traffic (people searching for any Claude Code tool)
  - Community goodwill
  - Own tools discovered alongside ecosystem
- **Content strategy:**
  - Blog posts can feature other people's tools too
  - "Tool of the week" series
  - Comparison posts
  - Integration guides
