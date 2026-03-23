---
description: Run the full creative strategy pipeline — research, personas, and angles
---

# /full-pipeline [product or category]

Run all three stages of the creative strategy pipeline in sequence:

1. **Research** — Fetch customer voice data from public sources
2. **Personas** — Build buyer personas from the research
3. **Angles** — Generate creative angles from personas

Steps:
1. Check `.claude/creative-strategist.local.md` for existing product context
2. Parse the argument as the research target
3. If no argument provided, ask the user what product/category to research
4. Run customer-research skill, save as `[product-slug]-research.md`
5. Run persona-builder skill using the research output, save as `[product-slug]-personas.md`
6. Run angle-generator skill using research + personas, save as `[product-slug]-angles.md`
7. Present a summary of findings: top personas, top angles, and recommended next steps
