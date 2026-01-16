# XML Tag Library: Essential Tags

XML tags are Claude's primary method for structured prompting. They provide clear boundaries, improve parsing accuracy, and enable complex prompt architectures.

## When to Use XML Tags

- Multi-part prompts with distinct sections
- Long documents or data sets
- Complex instructions with multiple steps
- When you need clear separation of concerns
- Templates and reusable prompt patterns

**Simple prompts don't need tags:**
- "Summarize this article in 3 sentences"
- "What's the capital of France?"
- "Write a haiku about programming"

---

## Core Tags (Use These)

### `<instructions>`
Define clear, actionable steps for Claude to follow.

```xml
<instructions>
1. Read the entire document carefully
2. Identify the main argument in each section
3. Extract key supporting evidence
4. Summarize findings in bullet points
</instructions>
```

### `<context>`
Provide background information Claude needs.

```xml
<context>
You are analyzing customer feedback for a SaaS product.
The product targets small businesses (10-50 employees).
We recently released v2.0 with a redesigned UI.
</context>
```

### `<data>`
Provide structured data for processing. Always separate user data from instructions.

```xml
<data format="json">
{
  "users": 15234,
  "active_users": 8901,
  "churn_rate": 0.12
}
</data>
```

### `<examples>` / `<example>`
Show Claude exactly what you want through demonstrations.

```xml
<examples>
<example>
<input>Customer said: "The app crashes when I upload photos"</input>
<output>Category: Bug Report | Severity: High | Sentiment: Frustrated</output>
</example>
</examples>
```

### `<output_format>`
Define exact structure, style, and format of response.

```xml
<output_format>
## Summary
[2-3 sentences]

## Key Findings
- [Finding 1]
- [Finding 2]

## Recommendations
[Actionable items]
</output_format>
```

### `<thinking>`
Request step-by-step reasoning for complex problems.

```xml
<thinking>
[Your step-by-step analysis here]
</thinking>

<answer>
[Your final answer]
</answer>
```

### `<role>`
Define Claude's persona and expertise.

```xml
<role>
You are a senior DevOps engineer with 10 years of experience.
You specialize in AWS, Kubernetes, and CI/CD pipelines.
</role>
```

### `<constraints>`
Define boundaries, limitations, and rules.

```xml
<constraints>
- Response must be under 300 words
- Use only information from provided documents
- If uncertain, state your confidence level
</constraints>
```

### `<document>`
Delineate text to be analyzed or processed.

```xml
<document id="contract" type="legal">
[Document content here]
</document>
```

### `<answer>`
Mark the final response (pairs with `<thinking>`).

```xml
<answer>
The capital of France is Paris.
</answer>
```

---

## Quick Selection Guide

| Task Type | Recommended Tags |
|-----------|------------------|
| Document analysis | `<document>`, `<instructions>`, `<output_format>` |
| Data processing | `<data>`, `<constraints>`, `<output_format>` |
| Code review | `<code>`, `<instructions>`, `<output_format>` |
| Complex reasoning | `<thinking>`, `<context>`, `<answer>` |
| Classification | `<examples>`, `<data>`, `<output_format>` |

---

## Best Practices

1. **Use descriptive names**: `<user_feedback>` not `<uf>`
2. **Be consistent**: Pick one tag name and stick with it
3. **Nest logically**: `<examples><example>...</example></examples>`
4. **Keep instructions outside data tags**: Don't mix them
5. **Start simple**: Add tags as complexity grows
