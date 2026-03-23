---
description: Build data-driven customer personas from existing research
argument-hint: [product name] (optional — will auto-detect research file)
allowed-tools: Read, Write, Edit, Grep, Glob
---

Run the persona-builder skill.

First, locate the research file in the workspace (look for *-research.md files). If $ARGUMENTS is provided, look for a research file matching that product name.

If no research file is found, inform the user they need to run /research first.

Build 2-4 distinct, data-driven customer personas from the research data. Each persona must include:
- A vivid name and snapshot
- Internal monologue written in the customer's actual language
- Trigger events, pain points, desired outcomes
- Objections and prior failed solutions
- Language fingerprint (exact phrases from research)
- Ad responsiveness signals

Include a persona comparison matrix at the end.

Save the output as [product-slug]-personas.md in the workspace.
