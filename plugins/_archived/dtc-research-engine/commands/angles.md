---
description: Generate research-backed advertising angles from research and persona data
argument-hint: [product name] (optional — will auto-detect files)
allowed-tools: Read, Write, Edit, Grep, Glob
---

Run the angle-generator skill.

Locate the research file (*-research.md) and personas file (*-personas.md) in the workspace. If $ARGUMENTS is provided, match against that product name.

Generate 5-8 scored and ranked advertising angles across these categories:
- Pain-Agitation
- Failed-Solution
- Trigger-Event
- Identity
- Social Proof
- Discovery/Secret
- Comparison
- Specificity

For each angle, provide:
- Strategic frame and supporting evidence (real customer quotes)
- Example hook directions
- Platform fit assessment (Meta, YouTube, TikTok, Google)
- Risk/watch-out notes

Include a prioritization matrix ranking all angles.

Save as [product-slug]-angles.md in the workspace.
