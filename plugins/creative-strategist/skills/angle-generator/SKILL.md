---
name: angle-generator
description: This skill should be used when the user asks to "find angles", "generate angles", "ad angles", "selling angles", "creative angles", "hook ideas", "what angles should I test", "brainstorm ad concepts", "creative strategy", "angle brainstorm", or mentions generating advertising angles from research or persona data. Trigger after customer-research or persona-builder has been run, or when the user provides their own research.
---

# Angle Generator — Executable Creative Angles from Research

Transform customer research and personas into concrete, testable advertising angles with specific hook copy, format variants, and a testing roadmap. Each angle is immediately executable — not a strategic concept, but a creative springboard with starter copy a team can test today.

## Orchestration

1. Search the workspace for a research file (`*-research.md`) and a personas file (`*-personas.md`).
   - If neither exists: "No research or persona files found. Run customer-research and persona-builder first."
   - If research exists but no personas: "No persona file found. Run persona-builder first — angles are matched to persona creative briefs." (Angles CAN be generated from research alone, but quality is significantly better with personas.)

2. Read YAML frontmatter from both files for a quick validation pass — check `stage` values (`research` and `personas`), confirm `product` slugs match, and note `persona_names` and `fire3_count`. Then validate the personas file body has creative briefs per persona (Lead with, Prove with, Avoid, CTA style, Best platform, Hook archetype). These are direct inputs to angle generation. If missing, warn the user.

3. Check `.claude/creative-strategist.local.md` for product positioning.

4. Generate angles following the process below.

5. Save output as `[product-slug]-angles.md` in the workspace.

6. Present a summary:
   - Tier 1 angles: name, category, target persona, and 1 example hook copy each
   - Testing roadmap Phase 1: which 3 angles to test first, on which platforms, with budget split
   - Angles to avoid and why
   - Suggest reviewing the full file for format variants and platform-specific execution

## Inputs

### Upstream data to consume

- **Persona creative briefs** — each persona ends with a table (Field | Value) containing: Lead with, Prove with, Avoid, CTA style, Best platform, Hook archetype. Use these as direct constraints when generating angles.
- **🔥3 quotes** — high-intensity quotes from research are hook material. Prioritize angles built on 🔥3 evidence.
- **Language clusters** — frustration, hope, skepticism, urgency, relief phrases. Pull hook language directly from these.
- **Journey stage distribution** — angles should cover the stages where quotes exist. Note stage gaps.
- **Anti-persona** — angles must not accidentally appeal to the anti-persona.
- **Surprising findings** — check if any non-obvious insight supports an unexpected angle.

## Angle Categories

Read `references/angle-frameworks.md` for deep dives, sub-types, and combination patterns. The eight core categories:

| Category | Core Mechanism | Best When |
|----------|---------------|-----------|
| **Pain-Agitation** | Product as antidote to visceral pain | Research has 🔥3 pain quotes with cascading consequences |
| **Failed-Solution** | Product as what works after everything else failed | Persona has extensive "tried everything" history |
| **Trigger-Event** | Ad starts at the moment they go from passive to active | Research has clear, specific trigger events |
| **Identity** | Product enables who they want to be (or stops who they don't) | Research reveals self-perception language |
| **Social Proof** | Evidence from other people like them | Persona's conviction pattern requires peer validation |
| **Discovery** | Product as hidden or novel solution | Product has genuinely novel mechanism or ingredient |
| **Comparison** | Direct or indirect contrast with alternatives | Competitive positioning map shows clear advantages |
| **Specificity** | Concrete data point builds instant credibility | Product has surprising stats, timeframes, or counts |

Skip categories without evidence in the research. Never force an angle the data doesn't support.

## Process

### 1. Mine angles from research and persona briefs

For each persona's creative brief table, check which angle categories align:
- The persona's "Lead with" row — which category frames that pain/desire best?
- The persona's "Prove with" row — which category naturally includes that proof type?
- The persona's "Hook archetype" row — which categories match that archetype?

Then scan the research for 🔥3 quotes that could anchor each angle. An angle without at least one 🔥3 quote behind it is weak.

### 2. Identify angle combinations

The strongest ads combine two angle categories. Check for natural pairings:

| Combination | Why It Works | Example |
|-------------|-------------|---------|
| Failed-Solution + Discovery | "Nothing worked... until this" | Validates frustration, introduces novelty |
| Trigger-Event + Pain-Agitation | Start at the moment, deepen the stakes | Instant recognition + emotional escalation |
| Identity + Social Proof | "Become the person who... join thousands who already did" | Aspiration + validation |
| Comparison + Specificity | "X is 3x faster than Y" | Concrete + competitive |
| Pain-Agitation + Identity | "Stop being the person who..." | Pain + identity shift |

Flag combinations where research supports both sides. These become the highest-priority angles.

### 3. Score with the 3-gate system

**Gate 1 — Evidence (must pass)**
Does this angle have at least one 🔥3 quote AND 2+ supporting quotes from the research?
- PASS: Strong research foundation
- FAIL: Angle is speculative — demote to "speculative" tier or discard

**Gate 2 — Persona Match (must pass)**
Does this angle align with at least one persona's creative brief (lead with, prove with, hook archetype)?
- PASS: Clear audience-angle fit
- FAIL: Angle may work generically but isn't targeted — demote or discard

**Gate 3 — Differentiation (separates good from great)**
Does this angle avoid what competitors are already running? Does it leverage a surprising finding or underused category?
- PASS: Fresh angle with competitive separation
- PARTIAL: Solid but competitors likely running similar
- FAIL: Commodity angle — keep only if Gates 1-2 are exceptionally strong

**Tier assignment:**
- All 3 gates pass — **Tier 1** (test first)
- Gates 1-2 pass, Gate 3 partial — **Tier 2** (test second)
- Gate 1 passes, others partial — **Tier 3** (test if Tier 1-2 saturate)
- Any gate fails — discard or note as speculative

### 4. Develop top angles

Develop 5-8 angles (aim for 3+ Tier 1). For each:

```markdown
## Angle: [Name]
**Category**: [Primary + Secondary if combination]
**Tier**: [1/2/3]
**Target Persona**: [Which persona(s) + why]
**Journey Stage**: [Which stage this angle targets]

### The Strategic Frame
2-3 sentences: what story does this ad tell? What belief does it create or shift?

### Anchor Evidence
🔥3 quotes from research that this angle is built on:
- "[Quote]" — [source]
- "[Quote]" — [source]

### Hook Copy Starters
Specific, testable first lines a creative team can use TODAY. Write 3-5 actual hooks, not descriptions of hooks:
1. "[Exact hook copy — first 1-2 sentences of an ad]"
2. "[Exact hook copy — different approach, same angle]"
3. "[Exact hook copy — variation]"

These should use language directly from research language clusters. Each hook should be different enough to test as an independent variable.

### Format Variants

**Short-form (static image / story / 15s video)**
- Visual: [What the image or opening frame shows]
- Copy: [1-3 lines — the complete short-form ad text]
- CTA: [Specific call to action]

**Long-form (60s+ video / article / landing page)**
- Opening: [First 5-10 seconds / first paragraph]
- Arc: [How the story builds — what comes after the hook]
- Proof section: [What evidence appears and in what format]
- Close: [How it resolves — CTA and final frame/paragraph]

### Platform Execution
Platform doesn't just determine WHERE — it determines HOW the angle is executed:

- **Meta (feed)**: [Hook structure for scroll-stopping. What stops the thumb? Image-first or text-first? Video or static?]
- **Meta (story/reel)**: [Vertical format. First 2 seconds are everything. How does this angle open in 9:16?]
- **TikTok**: [Must feel native. UGC or produced? Trending format fit? How does this NOT look like an ad?]
- **YouTube (pre-roll)**: [5 seconds before skip. What's the non-skippable hook? How does it earn the next 25 seconds?]
- **Google Search**: [Intent-aligned. What keyword does this angle match? Headline + description that wins the click.]

Only include platforms where this angle genuinely works. Don't force fit.

### Risks & Failure Modes
- **If you lean too hard**: [What breaks — e.g., "pain-agitation becomes fear-mongering, audience feels manipulated"]
- **Audience it alienates**: [Which persona or segment — especially check against anti-persona]
- **Competitor response**: [Will this invite direct comparison? Does it open a vulnerability?]
- **Tone trap**: [Where the line is between compelling and cringe for this angle]
```

### 5. Identify angles to AVOID

List 2-3 angles that would work generically but should NOT be used for this specific product/audience:

```markdown
## Angles to Avoid

### [Angle Name] — [Category]
**Why it seems obvious**: [Why a generic creative team would try this]
**Why it backfires here**: [What the research reveals about why this specific audience would reject it]
**Anti-persona risk**: [If applicable — does this angle attract the anti-persona?]
```

### 6. Build the testing roadmap

```markdown
## Testing Roadmap

### Phase 1: Prove the angle (Week 1-2)
Test these angles first — strongest evidence, clearest persona match:
| Priority | Angle | Persona | Platform | Format | Budget % |
|----------|-------|---------|----------|--------|----------|
| 1 | [name] | [persona] | [platform] | [format] | 40% |
| 2 | [name] | [persona] | [platform] | [format] | 35% |
| 3 | [name] | [persona] | [platform] | [format] | 25% |

**Success signal**: [What metric indicates this angle is working — CTR > X%, hook rate > Y%, CPA < $Z]
**Kill signal**: [When to stop testing — after how many impressions with what threshold]

### Phase 2: Expand winners (Week 3-4)
For angles that pass Phase 1:
- Test additional hook variants (3-5 per winning angle)
- Expand to secondary platforms
- Test long-form variant if short-form won

### Phase 3: Combination testing (Week 5+)
Test angle combinations on winning angles:
- Combine winning primary angle with secondary category
- Test on the second-best persona match
```

### 7. Priority matrix

| Rank | Angle | Category | Tier | Persona | Platform | Journey Stage | Phase |
|------|-------|----------|------|---------|----------|---------------|-------|
| 1 | | | | | | | 1 |
| 2 | | | | | | | 1 |
| ... | | | | | | | |

### 8. Save output

Save as `[product-slug]-angles.md` in the workspace. Include YAML frontmatter:

```yaml
---
product: "[product-slug]"
stage: angles
generated: "[YYYY-MM-DD]"
angle_count: [N]
tier1_count: [N]
tier2_count: [N]
personas_file: "[product-slug]-personas.md"
research_file: "[product-slug]-research.md"
---
```

## Quality Standards

- Every angle passes at least Gates 1-2 of the scoring system
- Hook copy starters are specific enough to run as ads, not strategic descriptions
- At least one angle is a combination (two categories working together)
- Format variants included for every Tier 1 angle (short-form + long-form)
- Platform execution notes explain HOW the angle works on each platform, not just which platforms
- Angles to Avoid section populated with research-backed reasons
- Testing roadmap includes specific success/kill signals
- At least one angle leverages a Surprising Finding from the research
- No angle accidentally appeals to the anti-persona

## Reference Files

- **`references/angle-frameworks.md`** — Deep dive into each angle category with sub-types, combination patterns, and execution guidance across verticals
