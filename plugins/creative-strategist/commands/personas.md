---
description: Build data-driven buyer personas from research data
---

# /personas

Run the persona-builder skill to transform customer research into actionable buyer personas.

Steps:
1. Check for an existing research file (`*-research.md`) in the workspace
2. If no research file exists, inform the user and suggest running `/research` first
3. Check `.claude/creative-strategist.local.md` for product context
4. Execute the persona-builder skill
5. Save output as `[product-slug]-personas.md`
