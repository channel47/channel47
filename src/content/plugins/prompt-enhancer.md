---
featured: false
draft: false
asciiIcon: |
  ╔═══════╗
  ║ OPTIMIZE ║
  ║ PROMPTS  ║
  ╚═══════╝
iconColor: "var(--color-accent-primary)"
---

## What it does

Improve your prompts using Anthropic's 2025 best practices. Get better results from Claude by applying proven techniques: XML tags, role assignment, chain of thought, and more.

Updated for Claude 4.x models (Sonnet 4.5, Haiku 4.5) with literal interpretation and improved instruction following.

## Key Features

- **Systematic optimization**: Applies 8 core techniques automatically (mandatory + contextual)
- **Claude 4.x optimizations**: Model-specific improvements for latest Claude versions
- **Before/after comparisons**: See exactly what changed and why
- **Interactive wizard**: Build prompts from scratch with `/build-prompt`
- **Comprehensive reference library**: Examples, templates, patterns, and techniques on-demand
- **Progressive disclosure**: Loads only what you need to avoid context bloat

## Real-world use cases

Use this plugin when:

- Your prompts produce inconsistent results
- Claude misunderstands your instructions
- You need better structured output (JSON, XML, etc.)
- Complex reasoning tasks need improvement
- You're working with sensitive data that needs separation
- You want to learn prompt engineering best practices

Common scenarios:

- Optimizing API integration prompts for reliable JSON output
- Improving code generation prompts with better examples
- Structuring complex analysis tasks with chain of thought
- Cleaning up ad-hoc prompts that grew organically
- Learning what "good" looks like for different task types

## What makes it different

Most prompt advice is scattered across docs, blog posts, and examples. This plugin packages Anthropic's official best practices into a systematic workflow.

It doesn't just give you tips. It shows you:

1. **What to change** - Specific improvements to your prompt
2. **Why it matters** - Explanation of each technique
3. **How it helps** - Expected impact on Claude's behavior

The `/build-prompt` wizard guides you through creating prompts step-by-step. The optimization skill takes existing prompts and improves them. Both use the same proven techniques.

## Setup

1. Install: `/plugin install prompt-enhancer@channel47`
2. Start optimizing immediately with `/prompt-enhancer`
3. Or build new prompts with `/build-prompt`

No configuration needed. Works out of the box.

## Example workflows

**Optimize an existing prompt:**

```
/prompt-enhancer
```

Paste your current prompt. Get back an improved version with explanations for each change.

**Build a new prompt from scratch:**

```
/build-prompt
```

Interactive 8-phase wizard walks you through:
1. Task Discovery - What are you trying to accomplish?
2. Role Assignment - What role should Claude take?
3. Context Gathering - What background does Claude need?
4. Data Separation - Separate instructions from data
5. Output Format - Define expected response structure
6. Advanced Techniques - Chain of thought, examples, etc.
7. Model Selection - Choose appropriate Claude model
8. Review & Export - Final prompt ready to use

**Get quick reference:**

The skill loads reference materials on-demand:
- Before/after gallery with real examples
- Task-type templates (code generation, analysis, creative, etc.)
- Common patterns (structured output, multi-step, etc.)
- XML tag library
- Claude 4.x specific tips

Just ask for what you need: "Show me examples of good prompts for code generation" or "What XML tags should I use?"

## Available skills & commands

**Main Skills:**

- `/prompt-enhancer` - Optimize existing prompts using systematic best practices

**Commands:**

- `/build-prompt` - Interactive wizard for building prompts step-by-step

**On-Demand Reference:**

Ask the skill to load specific resources:
- Before/after examples
- Task templates
- Common patterns
- XML tag reference
- New techniques (prefilling, extended thinking)
- Claude 4.x optimization tips
- Quick reference cheat sheet

See the [Getting Started Guide](https://github.com/ctrlswing/channel47-marketplace/blob/main/plugins/prompt-enhancer/GETTING_STARTED.md) for detailed usage examples and technique explanations.
