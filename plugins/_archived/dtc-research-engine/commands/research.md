---
description: Research customer voice data for a DTC product from Reddit, Amazon, Trustpilot, and other public sources
argument-hint: [product or category name]
allowed-tools: Read, Write, Edit, Grep, Glob, WebFetch, WebSearch, Agent
---

Run the customer-research skill for the product/category: $ARGUMENTS

Use the research-crawler agent to autonomously fetch data from multiple public sources (Reddit, Amazon reviews, Trustpilot, forums). Cast a wide net — search at least 5 different threads/pages across at least 2 platforms.

After fetching, synthesize the data into a structured research document with:
- Top pain points (ranked by frequency)
- Customer language patterns (exact phrases)
- Objection map
- Desire map
- Trigger events
- Demographic clusters
- Competitor landscape

Save the output as a markdown file in the current workspace directory.
