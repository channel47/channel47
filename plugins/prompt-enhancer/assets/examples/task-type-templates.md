# Task-Type Templates

Three battle-tested templates for common prompt engineering tasks. Copy, customize, and use immediately.

---

## Template 1: Document Analysis

**Use for:** Analyzing contracts, reports, research papers, technical docs

```xml
<document type="[document_type]">
[Your document content here]
</document>

<analysis_task>
[What you want to learn from the document]
</analysis_task>

<focus_areas>
1. [First area of interest]
2. [Second area of interest]
3. [Third area of interest]
</focus_areas>

<output_format>
## Summary
[High-level overview in 2-3 sentences]

## Key Findings
- [Finding 1 with supporting evidence]
- [Finding 2 with supporting evidence]
- [Finding 3 with supporting evidence]

## Recommendations
[If applicable]
</output_format>

<constraints>
- Focus on [specific aspect]
- Highlight any [concerns/risks/opportunities]
- Use [technical/business/general] language
</constraints>
```

**Example use:**
```xml
<document type="vendor_contract">
[45-page SaaS vendor contract]
</document>

<analysis_task>
Identify potential risks and non-standard terms that legal should review.
</analysis_task>

<focus_areas>
1. Financial obligations and payment terms
2. Liability caps and indemnification
3. Data security and privacy requirements
4. Termination and exit clauses
</focus_areas>
```

---

## Template 2: Code Review

**Use for:** Security review, code quality, architecture feedback

```xml
<role>
You are a [seniority] [specialization] engineer conducting a code review
focused on [focus_area].
</role>

<code language="[language]" file="[filename]">
[Your code here]
</code>

<context>
- Purpose: [What this code does]
- Environment: [Production/dev, scale, constraints]
- Recent changes: [What changed and why]
</context>

<review_criteria>
Evaluate for:
1. [Criterion 1 - e.g., Security vulnerabilities]
2. [Criterion 2 - e.g., Performance issues]
3. [Criterion 3 - e.g., Maintainability]
4. [Criterion 4 - e.g., Best practices]
5. [Criterion 5 - e.g., Error handling]
</review_criteria>

<output_format>
## Overall Assessment
[High-level summary and risk rating]

## Critical Issues
- [Issue]: [Description, location, fix]

## Moderate Issues
- [Issue]: [Description, location, fix]

## Minor Issues / Suggestions
- [Issue]: [Description, location, fix]

## Positive Aspects
[What's done well]

## Recommendations
[Prioritized action items]
</output_format>
```

**Example use:**
```xml
<role>
You are a senior backend engineer conducting a security-focused code review.
</role>

<code language="python" file="api/auth.py">
def login(username, password):
    query = f"SELECT * FROM users WHERE username='{username}'"
    user = db.execute(query)
    # ... rest of code
</code>

<review_criteria>
Evaluate for:
1. SQL injection and other security vulnerabilities
2. Authentication best practices
3. Error handling and logging
4. Input validation
</review_criteria>
```

---

## Template 3: Data Analysis

**Use for:** Analyzing datasets, finding patterns, generating insights

```xml
<context>
You are analyzing [data_type] for [business_purpose].
Key questions: [Main questions to answer]
</context>

<data format="[csv/json/table]">
[Your data here]
</data>

<analysis_objectives>
1. [Objective 1 - e.g., Identify trends]
2. [Objective 2 - e.g., Find anomalies]
3. [Objective 3 - e.g., Compare segments]
4. [Objective 4 - e.g., Generate recommendations]
</analysis_objectives>

<output_format>
## Executive Summary
[2-3 sentences with most important findings]

## Key Metrics
- [Metric 1]: [Value and significance]
- [Metric 2]: [Value and significance]

## Trend Analysis
[Patterns observed with supporting data]

## Insights
1. [Insight with data support]
2. [Insight with data support]
3. [Insight with data support]

## Recommendations
- [Action 1]: [Expected impact]
- [Action 2]: [Expected impact]
</output_format>

<constraints>
- Focus on actionable insights
- Support claims with specific data points
- Highlight anything urgent or surprising
</constraints>
```

**Example use:**
```xml
<context>
You are analyzing e-commerce sales data for Q4 2024.
Key questions: Why did conversion rate drop in November? Which products drove revenue?
</context>

<data format="csv">
date,visits,conversions,revenue,cart_abandonment_rate
2024-10-01,15000,750,125000,0.35
...
</data>

<analysis_objectives>
1. Identify causes of conversion rate decline
2. Determine top revenue drivers
3. Analyze cart abandonment patterns
4. Recommend optimization opportunities
</analysis_objectives>
```

---

## How to Use

1. **Choose template** matching your task type
2. **Replace bracketed placeholders** with your specifics
3. **Add your content** (documents, code, data)
4. **Test and refine** based on output quality
