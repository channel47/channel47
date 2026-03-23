---
description: Run the complete research-to-creative pipeline for a DTC product (research → personas → angles → scripts → copy)
argument-hint: [product or category name]
allowed-tools: Read, Write, Edit, Grep, Glob, WebFetch, WebSearch, Agent
---

Run the complete DTC research-to-creative pipeline for: $ARGUMENTS

Execute all five stages in sequence, using the output of each stage as input for the next:

**Stage 1: Customer Research**
Use the customer-research skill. Fetch real customer voice data from Reddit, Amazon reviews, Trustpilot, and other public sources. Save as [product-slug]-research.md.

**Stage 2: Persona Building**
Use the persona-builder skill. Build 2-4 data-driven customer personas from the research. Save as [product-slug]-personas.md.

**Stage 3: Angle Generation**
Use the angle-generator skill. Generate 5-8 scored and ranked advertising angles. Save as [product-slug]-angles.md.

**Stage 4: Script Writing**
Use the script-writer skill. Write UGC and TikTok scripts for the top 2-3 angles. Save as [product-slug]-scripts.md.

**Stage 5: Copy Writing**
Use the copy-writer skill. Write Meta and Google Search ad copy for the top angles. Save as [product-slug]-copy.md.

After completing all stages, provide a summary of:
- Key personas identified
- Top 3 angles discovered
- Number of scripts and copy variations generated
- Links to all output files
