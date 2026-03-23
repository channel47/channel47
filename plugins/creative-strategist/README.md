# creative-strategist

Customer voice research, persona building, and angle generation from real public data. Turns Reddit threads, Amazon reviews, and forum posts into actionable creative strategy.

Part of [channel47](https://channel47.dev), open-source role-based plugins for Claude Code.

## What it does

Three-stage pipeline that takes a product or category and produces testable creative angles backed by real customer data:

1. **Customer Research** — scrapes real customer language from Reddit, Amazon, Trustpilot, forums, and review sites
2. **Persona Builder** — synthesizes research into 2-4 data-driven buyer personas
3. **Angle Generator** — produces scored, ranked advertising angles tied to personas

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
| `/research [product]` | Fetch customer voice data from public sources |
| `/personas` | Build buyer personas from research data |
| `/angles` | Generate creative angles from personas |
| `/full-pipeline [product]` | Run all three stages in sequence |

## Skills

| Skill | Auto-triggers on |
|-------|-----------------|
| customer-research | "research a product", "pull reviews", "voice of customer" |
| persona-builder | "build personas", "buyer persona", "target customer" |
| angle-generator | "find angles", "creative strategy", "ad angles" |

## Agent

**research-crawler** — autonomous web research subagent that fetches data from multiple platforms in parallel. Uses browser automation (Playwright) for blocked sites like Reddit and Amazon.

## License

MIT
