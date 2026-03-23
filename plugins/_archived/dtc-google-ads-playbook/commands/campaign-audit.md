---
name: campaign-audit
description: Audit Google Ads campaign data against the DTC playbook. Paste campaign data or point to a CSV/spreadsheet and get a structured diagnosis with specific recommendations.
argument-hint: "[paste data or file path]"
allowed-tools: ["Read", "Glob", "Grep", "Bash"]
---

# Campaign Audit Command

Perform a structured audit of Google Ads campaign data against the DTC Google Ads Playbook best practices. Analyze the data provided by the user and produce actionable findings.

## Process

1. **Ingest the data.** Accept campaign data in any format: pasted CSV/table, file path to xlsx/csv, or screenshot. If a file path is given, read it. If xlsx, use Python with openpyxl to convert and parse.

2. **Extract key metrics per campaign.** For each campaign, identify:
   - Campaign name, type, status
   - Daily budget, tCPA target
   - Cost, conversions, CPA, ROAS, CTR, conversion rate
   - Google Ads status/warnings (limited by budget, learning, constrained, etc.)

3. **Audit against the playbook.** Check each campaign against these criteria:

   **Architecture audit:**
   - Does the naming convention follow `{platform}-{offer}-{audience}-{sequence}-{modifier}` pattern?
   - Are audiences properly segmented (women, seniors, moms, etc.)?
   - Are there phone-exclusion variants for top performers?
   - Is the campaign type mix appropriate (85-95% PMax)?

   **Performance audit:**
   - CPA vs target: flag any campaign >120% of target CPA
   - ROAS: flag any campaign below 0.80
   - Conversion rate: flag any campaign below 1.5%
   - Zero-conversion campaigns with significant spend (>$500)
   - Campaigns stuck in "learning" for 7+ days

   **Budget audit:**
   - Campaigns showing "limited by budget" with good CPA (scale opportunity)
   - Campaigns overspending with bad CPA (cut opportunity)
   - Budget allocation: are top performers getting enough budget?
   - Test campaigns consuming too much budget

   **Optimization audit:**
   - tCPA appropriateness (new campaigns should have higher tCPA)
   - Device segmentation opportunities
   - Campaign duplication candidates (good CPA + hitting budget)
   - Campaigns that should be paused (high CPA for 5+ days)

4. **Output a structured report** with these sections:

```
## Campaign Audit Report

### Account Summary
[Total spend, conversions, avg CPA, campaign count by type/status]

### Top Performers (Scale These)
[Campaigns with best CPA/ROAS, specific scaling recommendations]

### Underperformers (Fix or Pause)
[Campaigns with worst CPA/ROAS, specific diagnosis and fix/pause recommendation]

### Quick Wins
[Immediate actions: budget increases, tCPA adjustments, negative keywords, duplications]

### Architecture Gaps
[Missing audience segments, device variants, naming issues]

### Recommended Next Steps
[Prioritized action items numbered 1-10]
```

5. **Be specific.** Include exact campaign names, exact recommended budget amounts, exact tCPA adjustments (e.g., "Increase gpm-$149-women-4 budget from $8,888 to $12,888" not "increase budget on top campaigns").
