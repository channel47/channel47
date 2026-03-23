---
description: Build data-driven buyer personas from research data
allowed-tools: ["Read", "Write", "Glob"]
---

# /personas

Transform customer research into actionable buyer personas with creative briefs.

## Orchestration

1. Search the workspace for a research file (`*-research.md`). If multiple exist, ask the user which product to build personas for. If none exist:
   - Tell the user: "No research file found. Run `/research [product]` first to fetch customer voice data."
   - Stop here.

2. Validate the research file has the data the persona-builder needs:
   - Quotes with 🔥 intensity scores (needed for pain point ranking)
   - Journey stage tags (needed for journey entry point clustering)
   - Language clusters (needed for language fingerprint per persona)
   - Competitive positioning data (needed for competitive relationship section)
   - If any are missing, warn the user the research may have been run with an older version of the skill and suggest re-running `/research`.

3. Check `.claude/creative-strategist.local.md` for product context.

4. Execute the persona-builder skill. It will:
   - Cluster by behavior (journey entry, prior solutions, conviction pattern)
   - Build 2-4 personas with decision journey monologues and creative briefs
   - Build 1-2 anti-personas
   - Create a weighted comparison matrix

5. Save output as `[product-slug]-personas.md` in the workspace.

6. Present the user with a summary:
   - Persona names and one-line core tensions
   - Anti-persona name and why they'll never convert
   - The highest-weight differentiating dimension across personas
   - Suggest running `/angles` next
