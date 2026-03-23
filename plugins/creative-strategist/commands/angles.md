---
description: Generate research-backed creative angles from personas
---

# /angles

Run the angle-generator skill to produce testable advertising angles from research and persona data.

Steps:
1. Check for research file (`*-research.md`) and personas file (`*-personas.md`) in the workspace
2. If neither exists, inform the user and suggest running `/research` and `/personas` first
3. Check `.claude/creative-strategist.local.md` for product positioning
4. Execute the angle-generator skill
5. Save output as `[product-slug]-angles.md`
