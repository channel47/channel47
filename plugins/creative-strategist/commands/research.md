---
description: Research customer voice data for a product or category
---

# /research [product or category]

Run the customer-research skill to fetch real customer language from Reddit, Amazon, Trustpilot, forums, and review sites.

Steps:
1. Check `.claude/creative-strategist.local.md` for existing product context
2. Parse the argument as the research target (product name, category, or brand)
3. If no argument provided, ask the user what to research
4. Execute the customer-research skill
5. Save output as `[product-slug]-research.md`
