---
name: new-campaign-plan
description: Generate a complete Google Ads campaign architecture plan for a DTC brand, including campaign structure, naming, budgets, tCPA targets, audience segmentation, and landing page URL templates.
argument-hint: "[product/offer details, target audience, budget]"
allowed-tools: ["Read", "Grep"]
---

# New Campaign Plan Command

Generate a comprehensive Google Ads campaign launch plan based on the DTC Playbook framework.

## Process

1. **Gather requirements.** Ask the user for any missing information:
   - **Product/service:** What is being sold?
   - **Price point(s):** What does the product cost? Any special offer price?
   - **Brand name:** What brand name to use in ads?
   - **Target audiences:** Who are the primary customer segments?
   - **Daily budget:** Total daily ad budget available?
   - **Target CPA:** What CPA is profitable?
   - **Landing page domain:** What domain(s) will be used?
   - **Geographic targeting:** US nationwide, or specific states?
   - **Vertical:** Health, beauty, supplements, pet, etc.?

   If the user has provided most of this, fill in reasonable defaults for anything missing and note the assumptions.

2. **Design campaign architecture.** Using the Campaign Architecture skill, create:

   **Phase 1 campaigns (launch week):**
   - 3-5 PMax campaigns targeting primary audience segments
   - 1-2 phone-exclusion variants of the top segment
   - 1 Demand Gen (YouTube) campaign for the primary segment
   - Total: 5-8 campaigns

   **Phase 2 campaigns (week 2-3, based on data):**
   - Duplication candidates for Phase 1 winners
   - Geographic test campaigns (if applicable)
   - Additional audience segment campaigns
   - More phone-exclusion variants

3. **Output a complete plan** in this format:

```
## Google Ads Launch Plan: [Brand Name]

### Account Configuration
- Conversion tracking: [what to track]
- Attribution model: Data-driven
- Currency: USD
- Geographic targeting: [locations]

### Phase 1 Campaigns (Launch)

| Campaign Name | Type | Audience | Daily Budget | tCPA | Landing Page |
|---------------|------|----------|-------------|------|-------------|
| [full name] | PMax | [segment] | $X,XXX | $XXX | [URL pattern] |
| ... | ... | ... | ... | ... | ... |

### Campaign Details

#### [Campaign Name 1]
- **Audience signals:** [specific signals to configure]
- **Asset groups:** [2-4 asset group themes]
- **Headlines:** [10-15 headlines following the formula]
- **Long headlines:** [4-5 long headlines]
- **Descriptions:** [4-5 descriptions]
- **Negative keywords:** [campaign-level negatives]

[Repeat for each campaign]

### Negative Keyword Lists (Shared)
- **Competitor Brands:** [list]
- **Brand Navigation:** [list]
- **Low Intent:** [list]

### Landing Page URL Templates
[URL pattern with parameter breakdown for each campaign]

### Phase 2 Plan (After Week 1 Data)
[Conditional plans based on Phase 1 performance]

### Budget Allocation Summary
| Phase | Campaign Count | Daily Budget | % of Total |
|-------|---------------|-------------|-----------|
| Phase 1 | X | $X,XXX | 100% |
| Phase 2 | +X | $X,XXX | adjusted |

### KPI Targets
| Metric | Target | Action Threshold |
|--------|--------|-----------------|
| CPA | $XXX | Pause if >$XXX for 5 days |
| ROAS | X.XX | Investigate if <X.XX |
| Conv Rate | X.X% | Audit if <X.X% |
```

4. **Write actual ad copy.** Do not use placeholder text. Write real headlines, descriptions, and long headlines tailored to the specific product and audience using the Ad Copy & Landing Pages skill formulas.

5. **Be opinionated.** Recommend specific budget amounts, specific tCPA targets, and specific audience configurations. The user wants a plan they can execute, not a menu of options.
