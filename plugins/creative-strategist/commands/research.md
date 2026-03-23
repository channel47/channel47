---
description: Research customer voice data for a product or category
allowed-tools: ["Read", "Write", "Glob", "WebFetch", "WebSearch", "Agent"]
---

# /research [product or category]

Fetch real customer language from Reddit, Amazon, Trustpilot, forums, and review sites. Outputs a structured research file that feeds into `/personas` and `/angles`.

## Orchestration

1. Check `.claude/creative-strategist.local.md` for existing product context. If it exists, read it and use the product name, competitors, and target audience to guide research.

2. Parse the argument as the research target (product name, category, or brand). If no argument provided AND no config file exists, ask the user:
   - What product or category to research
   - Any known competitors (brand names help find reviews)
   - Any specific questions they want answered

3. **Launch the research-crawler agent** to autonomously fetch data from multiple platforms. The agent handles source discovery, fallback chains for blocked platforms, and quote extraction. Pass it the research target and any context from the config file.

4. When the agent returns, verify the output meets quality standards:
   - **P1 coverage**: All three P1 source types attempted. At least 2 of 3 must show thorough extraction (8+ quotes). If fewer than 2 P1 sources are thorough, send the agent back to retry with different URLs and fallback tools.
   - At least 50 quotes with triple-tagging (source + 🔥 intensity + journey stage)
   - At least 3 distinct source types
   - Language clusters populated (frustration, hope, skepticism, urgency, relief)
   - Surprising findings section present with 3+ insights
   - Source coverage log present

5. Save output as `[product-slug]-research.md` in the workspace.

6. Present the user with a summary:
   - Sources accessed and methods used
   - Total quotes captured with intensity distribution (X 🔥3, Y 🔥2, Z 🔥1)
   - Top 3 pain points (with example quotes)
   - Top 3 surprising findings
   - Any data gaps or underrepresented journey stages
   - Suggest running `/personas` next
