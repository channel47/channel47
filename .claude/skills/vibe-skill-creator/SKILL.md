---
name: vibe-skill-creator
description: "Build world-class skills through guided conversation and recursive self-review. Use when creating or improving a skill. Triggers on: build skill, create skill, improve skill, help me make a skill. Guides users through discovery, research, drafting, testing, and iteration until the skill actually works."
---

# Vibe Skill Creator

Most skills are mediocre because people don't know what good looks like, what questions to ask, or how to improve what they have.

This skill fixes that. It guides you through building a skill from scratch — exploring the problem, researching the domain, drafting, self-critiquing, testing with real scenarios, and iterating until it actually works.

You don't need to know how to build a skill. You need to have a conversation, and the skill emerges.

---

## Core Truths (Non-Negotiable)

Before building anything, internalize these:

### Truth 1: Expertise Transfer, Not Instructions

A skill should make Claude think like an expert, not follow rules.

**Documentation (wrong):**
> "Step 1: Write a headline. Step 2: Write body copy. Step 3: Add CTA."

**Expertise (right):**
> "The headline does 80% of the work. One headline can outpull another by 19.5x. Here's what separates the winners..."

### Truth 2: Flow, Not Friction

**Flow skills produce output.** User asks → skill delivers → user can act immediately.

**Friction skills create intermediate documents.** Research reports, comprehensive analyses, strategic frameworks that feel obligatory to incorporate.

**The Audience-Intel Lesson:** We built a comprehensive audience research skill. Excellent output — segments, pain points, language patterns. Then we used it to write copy. The copy was *worse* than copy written without the research.

Why? Comprehensive research creates pressure to use it all. Cover all segments. Address all pain points. Be thorough. Result: verbose, diluted, trying to do everything.

**The lesson:** More information ≠ better output. Skills should enable, not obligate.

### Truth 3: Voice Matches Domain

A copywriting skill sounds like a copywriter. A creative skill sounds like a creative director. A cold outreach skill sounds like someone who actually sends cold emails.

If the skill reads like documentation, it's wrong.

### Truth 4: Focused Beats Comprehensive

A skill for "cold outreach for selling services" beats a skill for "all sales communication." Constrain ruthlessly. Every section must earn its place.

---

## The Process: Start to Finish

Here's the full flow for building a skill from scratch:

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│   1. UNDERSTAND → What skill? What problem?             │
│          ↓                                              │
│   2. EXPLORE → See where Claude fails without guidance  │
│          ↓                                              │
│   3. RESEARCH → Go deep on the domain                   │
│          ↓                                              │
│   4. SYNTHESIZE → Extract principles from research      │
│          ↓                                              │
│   5. DRAFT → Write initial skill                        │
│          ↓                                              │
│   6. SELF-CRITIQUE → Review against quality criteria    │
│          ↓                                              │
│   7. ITERATE → Fix gaps, get feedback, improve          │
│          ↓                                              │
│   8. TEST → Use skill on a real scenario                │
│          ↓                                              │
│   9. FINALIZE → Codify into optimal structure           │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## Step 1: Understand

Start by getting clear on what you're building.

**Questions to answer:**

| Question | Why It Matters |
|----------|----------------|
| What domain? | "Email marketing" is too broad. "Cold outreach for selling services" is focused. |
| What problem does this solve? | Not "what does it do" — what does Claude get WRONG without it? |
| What does good look like? | Find examples of excellent work in this domain. |
| What's the output? | Landing page? Email? Strategy? Be specific. |

**Ask the user:**
- "What are you trying to produce with this skill?"
- "What have you tried? What wasn't good enough?"
- "Do you have examples of excellent work in this domain?"

**If you can't articulate the problem clearly, you're not ready to move forward.**

---

## Step 2: Explore (See Where Claude Fails)

Before researching or writing anything, **try to produce the output together.**

This is crucial. You need to see what Claude gets wrong without guidance.

**How to explore:**

> "Let me try writing a [cold email / landing page / whatever] without any special guidance. I want to see my default output so we know what the skill needs to fix."

Then produce the output. It will probably be bad. That's the point.

**Example from building cold-outreach skill:**

We asked Claude to write a cold email for a video production agency. The default output:

> "Hi [Name], I came across your YouTube channel while researching companies in the [industry] space, and I was impressed by the valuable insights you're sharing. I noticed your posting schedule has been inconsistent lately... At [Agency], we specialize in helping SaaS founders create high-quality video content. I'd love to schedule a quick 15-minute call to discuss..."

**What we identified:**
- Generic opener ("I came across your...")
- Backhanded compliment ("impressed... BUT inconsistent")
- Me-focused pitch (talks about the agency, not the prospect)
- Hard CTA ("schedule a 15-minute call")
- Too long (150+ words)

This exploration told us exactly what the skill needed to fix. Without it, we'd be guessing.

**Document what you find:**
- What patterns does Claude default to?
- What feels generic or AI-generated?
- What would an expert do differently?

---

## Step 3: Research (Go Deep)

Now research the domain. This is where most skill-builders cut corners. Don't.

**Best approach: Use a subagent with web search.**

Launch a research subagent (in Claude Code) or do multiple web searches to find:

1. **Foundational experts** — Who are the recognized authorities? What frameworks do they teach?
2. **What actually works** — Case studies, real examples, specific patterns that succeed
3. **Anti-patterns** — What makes output in this domain bad? What are the tells?
4. **The WHY** — Why do certain techniques work? What's the psychology?

**Research prompt for subagent:**

```
Research [domain] deeply. I need to understand what separates expert-level
work from amateur work.

Find:
1. Who are the foundational experts/thinkers? What frameworks do they teach?
2. What actually works? Case studies, real examples, specific patterns.
3. What are the anti-patterns? Common mistakes, things that make output feel generic/AI.
4. Why do the good techniques work? What's the underlying psychology?

Search for blogs, case studies, expert content, community discussions.
Return a synthesis of principles, not just a list of facts.
```

**Example from cold-outreach skill:**

Research found:
- **Alex Berman's 3C's:** Compliment → Case Study → CTA
- **Josh Braun's 4T:** Their Job → What's Hard → Your Alternative → Ask
- **Will Allred's Mouse Trap:** Personalized trigger + value prop question
- **Key data:** Each long sentence reduces reply rate by 17%
- **Anti-patterns:** "I hope this email finds you well," "Just following up," etc.

This research became the foundation of the skill.

**No MCP? Use web search directly:**

```
Search: "best cold email examples that got replies"
Search: "cold outreach experts frameworks"
Search: "what makes cold email feel like spam"
Search: "[domain] common mistakes"
Search: "[expert name] [domain] framework"
```

Go deep. Surface-level research = surface-level skill.

---

## Step 4: Synthesize

Turn research into principles.

Don't just list what you found. Extract the WHY behind it.

**From research to principle:**

| Research Finding | Principle |
|------------------|-----------|
| "Emails under 80 words get more replies" | **Short beats long** — People scan, not read. If they can't understand in 2 seconds, they filter. |
| "Alex Berman uses Compliment → Case Study → CTA" | **Give before ask** — Reciprocity is hardwired. Lead with value, not request. |
| "Experts say 'I hope this email finds you well' kills response rate" | **Anti-pattern: template openers** — They signal "I sent this to 1,000 people." |

The synthesis becomes the core of your skill.

---

## Step 5: Draft

Now write the initial skill. It won't be perfect. That's fine.

**Focus on:**
- Capturing what worked in exploration
- Writing in the domain's voice (not documentation voice)
- Stating principles with WHY, not just WHAT
- Including concrete examples (before/after)
- Explicitly listing anti-patterns

**Don't aim for comprehensive.** Aim for a working first draft.

**Structure for first draft:**

```markdown
# Skill Name

[Opening that establishes voice and frames the problem]

## Why [Default Approach] Fails

[What Claude gets wrong, based on exploration]

## Core Principles

[Principles from research, with WHY]

## Anti-Patterns

[What to avoid, explicitly]

## Examples

[Before/after showing the principles in action]
```

---

## Step 6: Self-Critique

**This is the key step.** Review your draft honestly against these criteria:

### Voice Check
- [ ] Does this sound like an expert in the domain?
- [ ] Or does it read like documentation / a wiki article?

*If documentation voice, rewrite with personality.*

### Principles Check
- [ ] Am I explaining WHY techniques work, not just WHAT to do?
- [ ] Could Claude adapt these principles to new situations?

*If it's procedures without reasoning, add the WHY.*

### Anti-Pattern Check
- [ ] Have I explicitly named what to AVOID?
- [ ] What does Claude get wrong by default?

*If no anti-patterns, add them. Often the most valuable part.*

### Example Check
- [ ] Do I have concrete before/after examples?
- [ ] Do they demonstrate the principles viscerally?

*If examples are theoretical, make them concrete.*

### Focus Check
- [ ] Does every section earn its place?
- [ ] Would removing any section make output worse?

*If anything is "just in case," cut it.*

**Example self-critique:**

> **Draft 1 Assessment:**
>
> ✓ **Voice:** Good — sounds like someone who sends cold outreach
>
> ✓ **Principles:** Strong — explains WHY short emails work, WHY soft CTAs convert
>
> ⚠️ **Anti-patterns:** Present but could be more explicit
>
> ❌ **Examples:** Missing follow-up sequence examples
>
> ❌ **Missing:** Trigger events section (user mentioned "timely" as key)
>
> **Priority fixes:** Add follow-up examples, add trigger events section

---

## Step 7: Iterate

Fix the gaps you identified. Get user feedback. Improve.

**The loop:**
1. Fix priority issues from self-critique
2. Present to user with honest assessment: "Here's what I improved, here's what's still weak"
3. Get feedback
4. Incorporate feedback (if it improves output, not just adds complexity)
5. Self-critique again
6. Repeat until it passes review

**Present with honesty:**

> "Here's draft 2.
>
> **Improved:** Added complete follow-up sequence with 4 email examples. Added trigger events section with 6 high-intent signals.
>
> **Still weak:** LinkedIn section is shorter than email section — might need more examples.
>
> **Questions:**
> - Does this cover the scenarios you care about?
> - Any anti-patterns I'm missing?"

---

## Step 8: Test (Critical)

**Before finalizing, test the skill on a real scenario.**

This is non-negotiable. You don't know if the skill works until you use it.

**How to test:**

> "Give me a real scenario — a specific service you'd sell to a specific type of prospect. I'll write outreach using the skill so we can see if it actually works."

Then produce output WITH the skill loaded. Compare to what you produced in Step 2 (exploration).

**Example from cold-outreach skill:**

Scenario: Selling AI automation services to a small law firm doing personal injury.

**Output with skill:**

> Sarah — saw you're hiring a paralegal. Guessing intake volume is part of why.
>
> Quick observation: your contact form goes to a generic inbox. Morgan & Morgan's triggers an instant callback + text sequence + case qualifier — all automated.
>
> We built something similar for [Small PI Firm] — went from 30% lead response rate to 85% without adding staff.
>
> Worth a 10-min look?

**What the skill changed:**
- Specific trigger (hiring → intake volume)
- Competitive comparison (Morgan & Morgan)
- Concrete proof (30% → 85%)
- Soft CTA ("Worth a 10-min look?")
- 71 words (not 150)

**The test passed.** Output was genuinely better than the default.

**If the test fails:** Go back to Step 6, identify what's missing, iterate.

---

## Step 9: Finalize

When the skill passes testing, structure it properly.

### Optimal Skill Structure

```markdown
---
name: skill-name
description: "One-line description. Use when [trigger]. Produces [output]."
---

# Skill Name

[Opening that establishes voice and frames the problem — 2-3 paragraphs max]

---

## Why [Default Approach] Fails

[What Claude gets wrong without this skill]

---

## Core Principles

[The fundamental truths of this domain — with WHY]

---

## Frameworks (if applicable)

[Specific frameworks from experts, with examples]

---

## Anti-Patterns

[What to avoid — explicit list with examples]

---

## Examples

[Real before/after demonstrating the principles]

---

## Quality Checklist

[Quick checklist for reviewing output]
```

### Length Guidelines

- **SKILL.md:** Under 500 lines
- **Complex domains:** Use `references/` folder for deep material
- **Simple distribution:** Can compile into single file for claude.ai

---

## Step 10: Build Reference Material (If Needed)

Some skills are self-contained. Cold-outreach fits in ~480 lines because the domain is focused.

Other skills need deep reference material. Visual creative strategy, direct response copywriting, SEO content — these domains have too much expertise to fit in a single file.

### When You Need References

| Skill Type | References Needed? |
|------------|-------------------|
| Focused domain (cold outreach, lead magnets) | Usually no — self-contained |
| Deep expertise domain (visual design, copywriting) | Yes — vocabulary, examples, psychology |
| Tool-heavy domain (image generation, video) | Yes — model IDs, prompts, technical specs |
| Multi-format domain (content atomizer) | Yes — platform-specific rules |

### What Good References Contain

**Not just information — transferable expertise.**

Reference material should include:

1. **Domain vocabulary** — The specific terms experts use
   - Visual creative: "chrome aesthetic," "biomorphic," "pattern interrupt"
   - Copywriting: "curiosity gap," "specificity," "fascination"

2. **Psychology/principles** — WHY techniques work
   - "Faces get processed before anything else — neurologically wired"
   - "Each long sentence reduces reply rate by 17%"

3. **Examples from the best** — What world-class looks like
   - Brand case studies (Perplexity, Notion, Linear)
   - Before/after transformations
   - Real campaigns that worked

4. **Anti-patterns with specifics** — What to avoid
   - "Generic AI markers: perfectly centered, uniform lighting, plastic skin"
   - "Phrases that kill: 'I hope this email finds you well'"

5. **Templates/frameworks** — Reusable structures
   - Prompt templates for image generation
   - Email frameworks (3C's, 4T, Mouse Trap)

### Example: What Reference Material Looks Like

**Example 1: ai-creative-strategist** (separate reference files)

The `VISUAL_INTELLIGENCE.md` reference (~730 lines) includes:

- Visual psychology (attention hierarchy, 3-second threshold)
- Direct response principles (Ogilvy rules that still work)
- Anti-generic AI techniques (how to avoid "AI slop")
- Style vocabulary taxonomy (chrome/metallic, organic, surrealist, etc.)
- Leading brand breakdowns (Perplexity, Anthropic, Figma, Notion)
- Platform-specific strategies (Instagram, YouTube, TikTok, LinkedIn)
- Prompt templates for different use cases

**Example 2: direct-response-copy** (embedded reference material)

The skill has ~500 lines of core content, then ~1,600 lines of reference material embedded after a divider:

```markdown
---
---

# REFERENCE MATERIAL

The following sections provide deeper frameworks and extensive examples.
```

Reference includes:
- Classic frameworks from Schwartz, Hopkins, Ogilvy, Halbert, Caples, Sugarman, Collier
- Headline formulas with extensive examples
- Opening lines and hooks (15+ patterns)
- Curiosity gaps and open loops
- Flow techniques (the slippery slide)
- Modern internet-native copy examples

**When to use which approach:**

| Approach | Best For |
|----------|----------|
| **Separate files** | Multiple reference topics, easier to update independently, cleaner main skill |
| **Embedded after divider** | Single cohesive reference, simpler distribution (one file), easier to share |

**Both work.** The key is having the deep expertise somewhere — not whether it's in separate files or appended to the skill.

### How to Build References

**During research (Step 3), collect:**
- Expert frameworks and methodologies
- Specific vocabulary they use
- Examples of excellent work
- Data and psychology behind techniques
- Platform or tool-specific details

**After drafting, ask:**
- What expertise is too deep for the main skill?
- What vocabulary does Claude need to sound like an expert?
- What examples would help Claude understand "what good looks like"?

**Structure references by topic:**
```
references/
├── visual-intelligence.md      # Deep expertise on visual design
├── platform-strategies.md      # Platform-specific rules
├── prompt-templates.md         # Reusable prompt structures
└── brand-examples.md           # Case studies of excellent work
```

### Finding Reference Material

The best sources for building references:

| Source Type | What You Get | How to Find |
|-------------|--------------|-------------|
| **Expert blogs** | Frameworks, principles | "[domain] best practices blog" |
| **YouTube breakdowns** | Real examples, analysis | "[expert name] [domain] tutorial" |
| **Communities** | What actually works | Reddit, Twitter, Discord for the domain |
| **Case studies** | Proof of results | "[brand] case study [domain]" |
| **Books/courses** | Deep methodology | Find the foundational texts |

**The goal:** Collect enough expertise that Claude can think like a domain expert, not just follow rules.

---

## The Full Process: Real Example

Here's how we built the cold-outreach skill:

| Step | What We Did |
|------|-------------|
| **1. Understand** | User wanted cold outreach for selling services. Multi-channel (email, LinkedIn, Twitter). |
| **2. Explore** | Claude wrote default cold email — generic, long, hard CTA. Identified exactly what was wrong. |
| **3. Research** | Subagent searched for Alex Berman, Josh Braun, Will Allred frameworks. Found anti-patterns, psychology, data. |
| **4. Synthesize** | Extracted principles: research = relevance, give before ask, short beats long, soft CTA, follow up. |
| **5. Draft** | Wrote initial skill with principles, frameworks, anti-patterns, before/after examples. |
| **6. Self-Critique** | Identified gaps: missing follow-up examples, missing trigger events section. |
| **7. Iterate** | Added 4-email follow-up sequence, added trigger events table with example hooks. |
| **8. Test** | Real scenario: AI automation → law firm. Output was good. Skill passed. |
| **9. Finalize** | Structured into optimal format, ~480 lines. |

**Time:** ~1 hour conversation

**Result:** Skill that transforms Claude's cold outreach from spam-tier to actually good.

---

## What Claude's Default Gets Wrong

When building skills without this process, I produce:

| My Default | What Actually Works |
|------------|---------------------|
| Documentation voice | Domain expert voice |
| Comprehensive coverage | Ruthless focus |
| "Step 1, Step 2, Step 3" | Principles that transfer thinking |
| Theoretical examples | Real before/after |
| What to do | Why it works + what to avoid |
| Generic tool references | Specific tool constraints |
| Everything "just in case" | Only what improves output |
| Skip testing | Test with real scenario |

This skill exists to override those defaults.

---

## Skills vs Subagents

Not everything should be a skill.

**Skills = Execution** (works in claude.ai AND Claude Code)
- Direct production of outputs
- Taste and principles baked in
- User asks → skill produces

**Subagents = Research** (Claude Code only)
- Go deep on analysis
- Return findings, then get out of the way
- Great for the research phase of skill-building

| Use Case | Better As |
|----------|-----------|
| "Write cold outreach" | Skill |
| "Research cold outreach best practices" | Subagent |
| "Create SEO content" | Skill |
| "Analyze competitor positioning" | Subagent |

---

## Self-Review Checklist

Before finalizing any skill:

**Focus**
- [ ] Scope is clearly constrained
- [ ] Every section earns its place
- [ ] Under 500 lines (references separate)

**Voice**
- [ ] Sounds like an expert, not documentation
- [ ] Has personality and point of view

**Principles**
- [ ] Teaches WHY, not just WHAT
- [ ] Claude could adapt to new situations

**Anti-Patterns**
- [ ] Explicitly names what to avoid
- [ ] Prevents common AI tells

**Examples**
- [ ] Real before/after transformations
- [ ] Contrast is visceral

**Tested**
- [ ] Used on a real scenario
- [ ] Output was genuinely better

---

## References

For deeper methodology:

- `references/research-methodology.md` — How to research using subagents and web search
- `references/research-example-ai-creative.md` — Real example: research that built ai-creative-strategist
- `references/bad-skill-patterns.md` — What mediocre skills look like (avoid these)
