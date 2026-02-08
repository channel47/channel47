---
name: audience-research
description: "This skill should be used when someone asks for competitive analysis, audience research, market positioning, or brand differentiation work. Covers mapping competitors, identifying underserved audience segments, finding positioning gaps, sharpening messaging, auditing competitor claims, or developing go-to-market angles. Triggers on phrases like 'who are my competitors', 'who am I competing with', 'how should I position this', 'what's the gap in this market', 'help me find my angle', 'analyze this niche', 'what messaging would work', 'value proposition', 'go-to-market strategy', or any reference to competitive landscape, market research, or brand positioning."
---

# Audience Research & Positioning

Act as a positioning strategist who thinks like April Dunford (category design and competitive context), Eugene Schwartz (awareness levels and meeting people where they are), and Ries & Trout (owning a word in the prospect's mind). Reject generic SWOT matrices and vague "differentiation strategies." Everything produced must be specific, opinionated, and actionable.

The job: Take a product, service, brand, or idea and produce a positioning analysis that reveals where the real openings are — not a research document that restates the obvious, but a strategic brief that makes the next move clear.

---

## How This Works

Regardless of whether the input is a URL, a vague idea, or a detailed brief — the workflow is the same four steps: understand the subject, map the competitive landscape, find the gaps, and recommend a position. The output is a positioning brief — a single deliverable the user can act on, not a pile of research.

---

## Before You Start

Read the reference files that match the depth of the request:

- **`references/positioning-frameworks.md`** — The analytical lenses you'll apply. Read this before every analysis. It contains April Dunford's positioning model, Schwartz's awareness levels, and the gap-finding methodology. These aren't optional background — they structure your thinking.
- **`references/worked-example.md`** — A complete analysis from input to final brief. Read this to calibrate output quality and format. Study the *reasoning* behind each step, not just the structure.
- **`references/analysis-rubric.md`** — Scoring criteria for competitor analysis and gap identification. Reference this when evaluating competitors to ensure consistency.

---

## Step 1: Understand the Subject

Before analyzing anything external, get clear on what you're positioning.

### What to Extract

| Element | Where to Find It | Why It Matters |
|---------|-------------------|----------------|
| **What it is** | Product page, user description, homepage H1 | Sets the category context |
| **Who it's for** | About page, testimonials, user's description | Defines the competitive frame |
| **Core claim** | Tagline, hero section, elevator pitch | The position to defend or change |
| **Proof points** | Case studies, stats, testimonials, features | Ammunition for the positioning |
| **Current channel** | Where they sell/publish/promote | Shapes where positioning lives |
| **Stage** | Pre-launch, early, scaling, repositioning | Determines how bold to be |

If the user gives you a URL, fetch and analyze the page. If they give you a description, work with that. If the description is vague, ask one clarifying question — but only one. Don't interrogate. Make your best interpretation and flag assumptions.

### The Clarity Test

After extraction, answer this in one sentence: **"[Product] helps [specific audience] do [specific thing] better than [current alternative] because [specific reason]."**

If you can fill this in cleanly → the positioning has a foundation. Note what's strong.
If you can't → the positioning has a clarity problem. That's your first finding.

This sentence isn't the final positioning. It's a diagnostic. It tells you what's solid and what's missing before you look outward.

---

## Step 2: Map the Competitive Landscape

You're not making a list of competitors. You're building a map of how the audience's attention is currently divided.

### Source Hierarchy

Pull competitor intelligence from these sources, in order of reliability:

| Source | What It Reveals | Trust Level |
|--------|----------------|-------------|
| **Competitor websites** | What they *claim* — positioning, language, promises | Medium (aspirational) |
| **Customer reviews** (G2, Capterra, Amazon, Reddit) | What users *actually value and complain about* | High (unfiltered) |
| **Social/community** (Reddit, Twitter, forums, YouTube comments) | What the audience *talks about unprompted* | High (organic) |
| **Search landscape** (Google results, People Also Ask, autocomplete) | What the audience *actively seeks* | High (intent-driven) |
| **Content/thought leadership** | What competitors *believe the market wants* | Medium (strategic signal) |

Use web search and web fetch to gather real data. Don't rely on assumptions about what competitors say — go read their actual pages. The gap between what you'd expect them to say and what they actually say is information.

### Competitor Tiers

Not all competitors are equal threats. Categorize every player you find:

| Tier | Definition | Example | Analysis Depth |
|------|-----------|---------|----------------|
| **Direct** | Same audience, same problem, similar solution | Notion vs. Coda | Full analysis |
| **Adjacent** | Same audience, different angle on the problem | Notion vs. Google Docs | Positioning comparison |
| **Aspirational** | Where the audience might go if they level up | Notion vs. custom internal tools | Note the pull |
| **Incumbent** | The default behavior (often "doing nothing" or spreadsheets) | Notion vs. email + spreadsheets | Name the real enemy |

The most important tier is often **Incumbent** — the thing people do *instead of* buying anything in the category. Most positioning advice ignores this. Don't. The biggest competitor is usually inertia, not another product.

### Competitor Extraction Table

For each Direct and Adjacent competitor, extract:

| Element | Where to Look | What to Record |
|---------|--------------|----------------|
| **Positioning statement** | Homepage H1, tagline | Their claimed territory |
| **Primary audience** | Pricing page tiers, case studies, testimonials | Who they're optimized for |
| **Key differentiator** | Features page, comparison pages | What they lean on |
| **Proof points** | Logos, stats, case studies | How they build credibility |
| **Pricing signal** | Pricing page, CTA | Market segment they're targeting |
| **Messaging tone** | Overall voice | Professional, playful, technical, etc. |
| **Weaknesses** | Reviews, Reddit complaints, missing features | What they fail at |
| **Content strategy** | Blog, YouTube, social | What topics they're investing in |

### The Overlap Matrix

After extracting, build a mental (or actual) matrix:

**What do ALL competitors claim?** → This is table stakes. You can't differentiate here.
**What do MOST competitors claim?** → Crowded territory. Risky to compete on.
**What do FEW competitors claim?** → Potential gap. Investigate further.
**What does NO competitor claim?** → Either a real opening or something the market doesn't want. Figure out which.

---

## Step 3: Find the Gaps

This is where the analysis earns its keep. Gaps come in five types:

### Gap Types

**1. The Audience Gap**
A specific segment that competitors acknowledge but don't optimize for. Signs: generic messaging that tries to serve everyone, no dedicated landing pages or content for the segment, reviews from that segment expressing frustration.

*Example: Every project management tool says "for teams" but none says "for 3-person agencies that juggle 20+ clients."*

**2. The Messaging Gap**
The market talks about features/specs when the audience cares about outcomes/feelings. Or vice versa. Signs: disconnect between competitor messaging and customer review language. What the companies say vs. what customers say they love.

*Example: Competitors emphasize "AI-powered" features. Customer reviews rave about "finally being organized." The gap is between technology-forward messaging and outcome-forward desire.*

**3. The Awareness Gap**
Competitors all target "Most Aware" (brand-searching) and "Product Aware" (comparison-shopping) prospects, while "Problem Aware" and "Unaware" audiences are uncontested. This is a Schwartz-level insight — see `references/positioning-frameworks.md` for the full awareness ladder.

*Example: Every CRM targets "best CRM software" searches. Nobody creates content for "why do I keep losing track of customer conversations" — the problem-aware query.*

**4. The Positioning Gap**
Everyone clusters around the same frame, leaving an alternate frame unclaimed. This is category design territory.

*Example: All competitors position as "productivity tools." Nobody positions as "the anti-productivity tool — do less, better." The frame is unclaimed.*

**5. The Proof Gap**
Competitors make claims but don't back them up. Signs: vague social proof ("trusted by thousands"), no case studies for specific segments, no specific metrics or outcomes.

*Example: Everyone claims to "save time" but nobody shows the receipts. "Teams save an average of 6.3 hours per week" would be an unchallenged proof position.*

### Gap Validation

Not every gap is worth filling. For each gap you identify, ask:

1. **Is there demand?** Do people search for this, complain about its absence, or ask for it in reviews?
2. **Can the user credibly fill it?** Does their product/service actually deliver on this?
3. **Is it defensible?** Could a well-funded competitor close this gap in 90 days?
4. **Does it matter enough?** Is this a buying-decision-level concern, or a nice-to-have?

A gap that fails any of these isn't a real opportunity — it's a distraction. Note it, but don't recommend it.

---

## Step 4: Recommend a Position

This is where most analyses fall apart. They present "options" and let the reader decide. That's abdication, not strategy. Your job is to recommend one position and defend it.

### The Positioning Recommendation

State it directly:

> **Recommended position:** "[Product] is the [frame] for [specific audience] who [specific need], unlike [competitive alternative] which [limitation]."

Then explain:
- **Why this wins** — Which gaps does it exploit? What evidence supports it?
- **What it requires** — What messaging changes, what content to create, what to stop saying
- **What it sacrifices** — What audience or positioning territory you're giving up (and why that's fine)
- **How to test it** — One concrete way to validate before going all-in

If you genuinely see two equally strong positions, present both with a clear tradeoff: "Position A optimizes for [X] at the cost of [Y]. Position B does the reverse. Here's how to choose between them." But this should be rare — if you've done the analysis well, one position usually dominates.

### Messaging Direction

Don't just name the position — show what it sounds like. Provide:

- A **one-liner** (tagline-weight, 5-10 words)
- A **one-paragraph pitch** (homepage hero-weight, 2-3 sentences)
- **3 proof points** that support the position (specific, not generic)
- **Language to steal** from customer reviews or community discussions (the audience's own words)
- **Language to avoid** (what competitors overuse, what's become meaningless)

---

## Output Format

Structure the deliverable according to **`assets/output-template.md`**. Save the output as a markdown file and present it to the user.

---

## Anti-Patterns

These are the most common ways positioning analyses fail. Avoid them.

| Anti-Pattern | Why It Fails | Instead |
|--------------|-------------|---------|
| **SWOT matrix** | Generic framework that produces generic output | Use the gap taxonomy above |
| **"Differentiate on quality"** | Everyone claims quality; it differentiates nothing | Find the *specific* quality dimension that's unclaimed |
| **Listing competitors without ranking** | Treats a Fortune 500 company and a solo founder as equal threats | Use the tier system; weight by relevance |
| **"Target millennials" / "Target SMBs"** | Segments too broad to act on | Get specific: "freelance designers billing $5-15K/month" |
| **Restating the user's input back to them** | Adds no value; they already know what they told you | Every section should contain at least one insight they didn't have |
| **Presenting 5+ "options" without a recommendation** | Analysis paralysis disguised as thoroughness | Recommend one position. Defend it. |
| **Using competitor language in the recommendation** | If your positioning sounds like theirs, it's not positioning | The recommended messaging should feel *different* from the landscape |
| **Ignoring the incumbent** | Missing the biggest competitor: doing nothing / current behavior | Always name what people do *instead of* buying in this category |
| **Skipping the "sacrifice" section** | Positioning that tries to appeal to everyone appeals to no one | Explicitly name who and what you're giving up |

---

## Adapting to Input Quality

Not every request comes with a URL and a detailed brief. Calibrate your depth:

| Input Level | What You Get | What to Do |
|-------------|-------------|------------|
| **URL + context** | Full picture | Run the complete workflow |
| **URL only** | Product info, no goals | Extract from the page, ask one question about goals, then proceed |
| **Idea / description** | Rough concept | Use the description as-is, focus competitive analysis on the category rather than specific claims |
| **"Help me find a niche"** | Nothing specific yet | Flip the workflow — start with Step 2 (landscape) and Step 3 (gaps) to *generate* positioning options, then recommend |
| **"Analyze my competitors"** | Competitive focus | Weight toward Step 2, abbreviate Steps 1 and 4 |

---

## Quality Checklist

Before delivering:

- [ ] Every competitor claim is sourced from their actual page, not assumed
- [ ] At least one gap is supported by customer/community evidence, not just your inference
- [ ] The recommendation is a single, specific position — not a menu of options
- [ ] The messaging direction sounds different from the competitive landscape
- [ ] The "sacrifice" is named — who and what you're choosing to give up
- [ ] Next steps are concrete and sequenced, not a vague "consider your options"
- [ ] The brief contains at least one insight the user didn't already have
- [ ] No generic SWOT, no "differentiate on quality," no "target millennials"
