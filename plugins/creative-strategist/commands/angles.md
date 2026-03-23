---
description: Generate research-backed creative angles with hook copy and a testing roadmap
allowed-tools: ["Read", "Write", "Glob"]
---

# /angles

Produce testable advertising angles from research and persona data. Each angle includes specific hook copy starters, format variants, platform execution notes, and a testing roadmap.

## Orchestration

1. Search the workspace for a research file (`*-research.md`) and a personas file (`*-personas.md`). If neither exists:
   - Tell the user: "No research or persona files found. Run `/research [product]` and `/personas` first."
   - Stop here.
   - If research exists but no personas: "No persona file found. Run `/personas` first — angles are matched to persona creative briefs." (Angles CAN be generated from research alone, but quality is significantly better with personas.)

2. Validate the personas file has creative briefs per persona (lead with, prove with, avoid, CTA style, best platform, hook archetype). These are direct inputs to angle generation. If missing, warn the user.

3. Check `.claude/creative-strategist.local.md` for product positioning.

4. Execute the angle-generator skill. It will:
   - Mine angles from research 🔥3 quotes and persona creative briefs
   - Identify angle combinations (2-category pairings)
   - Score with the 3-gate system (Evidence → Persona Match → Differentiation)
   - Develop 5-8 angles with hook copy starters and format variants
   - Identify angles to avoid
   - Build a testing roadmap with Phase 1-3 priorities

5. Save output as `[product-slug]-angles.md` in the workspace.

6. Present the user with a summary:
   - Tier 1 angles: name, category, target persona, and 1 example hook copy each
   - Testing roadmap Phase 1: which 3 angles to test first, on which platforms, with budget split
   - Angles to avoid and why
   - Suggest the user review the full file for format variants and platform-specific execution
