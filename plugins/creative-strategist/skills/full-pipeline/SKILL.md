---
name: full-pipeline
description: This skill should be used when the user wants to run the full creative strategy pipeline end-to-end — research, personas, and angles in sequence. Trigger on "run the full pipeline", "full creative strategy", "research to angles", "end-to-end creative", "run all three stages", "complete creative analysis", or when the user wants all three creative-strategist stages run as one workflow.
---

# Full Pipeline — Research to Angles in One Pass

Run all three stages of the creative strategy pipeline in sequence. Each stage's output feeds directly into the next. This skill orchestrates customer-research, persona-builder, and angle-generator — it does not duplicate their methodology.

## Pipeline

```
Research (customer-research)  ->  Personas (persona-builder)  ->  Angles (angle-generator)
        |                                |                               |
[product]-research.md            [product]-personas.md           [product]-angles.md
  40+ triple-tagged quotes         2-4 personas + anti-persona     5-8 angles + testing roadmap
  language clusters                creative briefs per persona     hook copy starters
  surprising findings              attention patterns              format variants
```

## Process

1. Check `.claude/creative-strategist.local.md` for existing product context.

2. Determine the research target from the user's argument or config file. If neither provides a clear target, ask:
   - What product or category to research
   - Any known competitors
   - Any specific questions or hypotheses

3. **Stage 1: Research** — Execute the customer-research skill (which launches the research-crawler agent). Verify the output meets quality standards: 40+ quotes, triple-tagged, language clusters, surprising findings, source coverage log. Verify YAML frontmatter is present with `stage: research`, quote count, and P1 coverage. Save as `[product-slug]-research.md`. Brief the user: "[X] quotes from [Y] sources. Top pain point: [Z]. Proceeding to personas."

4. **Stage 2: Personas** — Execute the persona-builder skill, feeding it the research output. Verify: 2-4 personas with creative briefs, anti-persona, comparison matrix. Verify YAML frontmatter is present with `stage: personas`, persona names, and research file reference. Save as `[product-slug]-personas.md`. Brief the user: "[N] personas built: [names]. Anti-persona: [name]. Proceeding to angles."

5. **Stage 3: Angles** — Execute the angle-generator skill, feeding it both research and personas. Verify: 5-8 angles with tiers, hook copy, format variants, testing roadmap. Verify YAML frontmatter is present with `stage: angles`, tier counts, and upstream file references. Save as `[product-slug]-angles.md`.

6. **Final Summary** — Present a comprehensive pipeline summary:

   **Research** ([X] quotes from [Y] sources)
   - Top 3 surprising findings
   - Biggest data gap (if any)

   **Personas** ([N] personas)
   - Each persona: name + one-sentence core tension
   - Anti-persona: name + why they won't convert

   **Angles** ([N] angles, [X] Tier 1)
   - Each Tier 1 angle: name + category + one hook copy starter
   - Testing roadmap Phase 1: which angles first, which platforms, budget split

   **Files saved:**
   - `[product-slug]-research.md`
   - `[product-slug]-personas.md`
   - `[product-slug]-angles.md`

   **Recommended next steps:**
   - Review the angles file for full hook copy, format variants, and platform execution
   - Start with Phase 1 of the testing roadmap
   - Re-run customer-research with deeper focus if any critical data gaps were flagged
