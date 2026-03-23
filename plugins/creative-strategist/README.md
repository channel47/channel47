# creative-strategist

Customer voice research, persona building, and angle generation from real public data. Turns Reddit threads, Amazon reviews, and forum posts into actionable creative strategy with specific hook copy, testing roadmaps, and platform execution plans.

Part of [channel47](https://channel47.dev), open-source role-based plugins for Claude Code.

## What it does

Three-stage pipeline that takes a product or category and produces testable creative angles backed by real customer data:

1. **Customer Research** — Scrapes real customer language from Reddit, Amazon, Trustpilot, forums, and review sites. Every quote is triple-tagged with source quality, emotional intensity (🔥1-3), and buying journey stage. Outputs language clusters, competitive positioning maps, and surprising findings.

2. **Persona Builder** — Synthesizes research into 2-4 data-driven buyer personas clustered by behavior (not demographics). Each persona includes a decision journey monologue, language fingerprint, attention patterns, and a mini creative brief. Also builds anti-personas to prevent wasted ad spend.

3. **Angle Generator** — Produces scored, ranked advertising angles with specific hook copy starters, short-form and long-form format variants, platform execution notes, and a phased testing roadmap. Angles are scored through a 3-gate system (Evidence → Persona Match → Differentiation) and include angle combinations and angles to avoid.

## Install

```
claude plugin install creative-strategist@channel47
```

## Configuration

Create `.claude/creative-strategist.local.md` in your project:

```markdown
---
product: "Product name"
category: "Product category"
url: "https://yourproduct.com"
price: "$49"
competitors: ["Competitor A", "Competitor B"]
target_audience: "Brief audience description"
---

Additional context about the product, brand voice, positioning,
or anything else that should guide research and creative strategy.
```

This file is read by all skills and the research-crawler agent. It's git-ignored (`.claude/*.local.md`).

## Commands

| Command | What it does |
|---------|-------------|
| `/research [product]` | Fetch customer voice data from public sources. Launches the research-crawler agent, validates output quality, presents a summary with intensity distribution and data gaps. |
| `/personas` | Build buyer personas from research data. Validates upstream research format, builds behavioral clusters, outputs personas with creative briefs and anti-personas. |
| `/angles` | Generate creative angles from personas. Validates persona creative briefs, scores angles through 3-gate system, outputs hook copy starters, format variants, and a testing roadmap. |
| `/full-pipeline [product]` | Run all three stages in sequence with stage-by-stage briefings and a comprehensive final summary. |

## Skills

| Skill | Auto-triggers on | Key outputs |
|-------|-----------------|-------------|
| customer-research | "research a product", "pull reviews", "voice of customer" | 40+ triple-tagged quotes, language clusters, competitive positioning map, surprising findings |
| persona-builder | "build personas", "buyer persona", "target customer" | 2-4 behavioral personas with creative briefs, anti-persona, weighted comparison matrix |
| angle-generator | "find angles", "creative strategy", "ad angles" | 5-8 tiered angles with hook copy, format variants, platform execution, testing roadmap |

## Agent

**research-crawler** — Autonomous web research subagent that fetches data from multiple platforms. Equipped with WebFetch, WebSearch, Playwright, Chrome browser automation, and Bash. Uses fallback chains when sources block access — a 403 is never a dead end. Automatically installs browser tools if needed.

## Pipeline data flow

```
Research                    →  Personas                    →  Angles
───────                        ────────                       ──────
40+ triple-tagged quotes       2-4 behavioral personas        5-8 scored angles
  source + 🔥 intensity          decision journey monologue     hook copy starters (3-5 per angle)
  + journey stage                 creative brief per persona    short-form + long-form variants
language clusters                 anti-persona                  platform execution notes
competitive positioning map       attention patterns            angles to avoid
surprising findings               weighted comparison matrix    testing roadmap (Phase 1-3)
source coverage log                                             priority matrix
```

## License

MIT
