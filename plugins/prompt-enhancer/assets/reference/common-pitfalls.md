# Common Pitfalls Reference

This document lists common mistakes and red flags to watch for when optimizing prompts.

---

## Common Mistakes to Avoid

| Mistake | Why It Happens | Fix |
|---------|---------------|-----|
| **No XML tags** | Feels like extra syntax | XML tags are Anthropic's #1 recommendation. Always use them. |
| **Mentioning examples without adding them** | Faster to describe than write | If you decide examples would help, write 2-5 actual examples. Takes 2 minutes, massive quality boost. |
| **Using examples for creative writing** | Assumed they always help | Examples limit creative capacity. Skip for creative tasks. |
| **Skipping chain of thought** | Seems unnecessary | Complex tasks need reasoning. Add `<thinking>` tags. |
| **Vague output format** | Assumes Claude will figure it out | Specify exact structure: sections, format, precision, tone. |
| **Generic role** | "helpful assistant" is easy | Specific roles (senior analyst, legal expert) improve outputs. |
| **Time pressure shortcuts** | Demo in 10 minutes | Mandatory techniques take seconds. Never skip. |
| **Settling for "good enough"** | Sunk cost fallacy | Apply ALL mandatory techniques, not just some. |
| **"This task is simple enough"** | Rationalization to skip techniques | MANDATORY techniques apply to ALL prompts, simple or complex. |
| **Assuming Claude 4.x will infer** | Used to Claude 3.x behavior | Claude 4.x takes you literally. Be explicit. |

---

## Red Flags - You're Skipping Best Practices

- Prompt has no XML tags
- Using headers/caps instead of XML tags
- "We could add examples..." without actually adding them (when you've decided they'd help)
- No `<thinking>` tags for complex reasoning
- Data and instructions not clearly separated
- Mentioned "chain of thought" but didn't implement it
- "Under time pressure, so I'll skip mandatory techniques"
- Output format described in prose instead of shown in template
- **"This task is simple enough to skip [mandatory technique]"** - Rationalization detected!
- **"The user wants it short/simple, so I'll skip XML tags/role/format"** - User preferences don't override mandatory techniques
- **"Already has some XML tags, so I'll skip other improvements"** - Partial implementation isn't sufficient
- **"Claude 4.x is smart enough to figure it out"** - These models take you literally!

**All of these mean: Go back and apply the mandatory techniques. Check the Technique Requirements table in SKILL.md.**
