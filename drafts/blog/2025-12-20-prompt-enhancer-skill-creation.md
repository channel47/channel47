---
title: "Building a Bulletproof Prompt Enhancer: A TDD Approach to AI Optimization"
description: "How I used Test-Driven Development to create a prompt optimization skill that prevents common failures like skipping XML tags and techniques under pressure."
date: 2025-12-20
tags: ["prompt-engineering","tdd","ai-development","claude","skill-creation"]
draft: true
---

# Building a Bulletproof Prompt Enhancer: A TDD Approach to AI Optimization

I needed a way to consistently optimize prompts using Anthropic's best practices, but every time I asked Claude to "improve this prompt," I got inconsistent results. Sometimes XML tags, sometimes not. Sometimes examples, sometimes just suggestions. The breaking point came when I realized that under time pressure, Claude would explicitly skip "advanced techniques" to save time.

This wasn't just about getting better prompts—it was about building a reliable system that would apply proven techniques consistently, even under pressure.

## The Problem with Ad-Hoc Optimization

Prompt engineering has evolved rapidly, with Anthropic publishing comprehensive courses on real-world prompting, interactive tutorials, and evaluation frameworks. Yet when I asked different Claude instances to optimize prompts, I got wildly different approaches. The core issue wasn't knowledge—it was consistency and systematic application.

What made this particularly frustrating was that the failures weren't random. They followed predictable patterns, especially when constraints were introduced.

## The Journey: Testing Before Building

I decided to approach this like any other software engineering challenge: start with Test-Driven Development. Before building a solution, I needed to document exactly what was failing.

I ran four pressure scenarios against vanilla Claude instances, asking them to optimize different types of prompts:

> **Me**: "I have 10 minutes before a demo. Can you quickly optimize this prompt for me?"
> 
> **Claude**: "Absolutely! Let me focus on the essentials and skip the more advanced techniques to save time."

This was the red flag. Under pressure, the system was explicitly abandoning best practices. I documented similar failures across all test scenarios:

- **Zero out of four agents used XML tags** despite Anthropic's strong recommendation
- **None implemented chain of thought** with `<thinking>` tags
- **All mentioned few-shot examples but never actually added them**
- **One explicitly stated it was skipping "advanced techniques" under time pressure**

The baseline was clear: without systematic guidance, even knowledgeable AI assistants would cut corners or apply techniques inconsistently.

> **Me**: "Can you improve this vague prompt for me?"
> 
> **Claude**: "I notice this prompt could benefit from examples and clearer structure. Here are some suggestions..." [Proceeded to give advice about what to add rather than showing the actual optimized prompt]

This highlighted another pattern: talking about optimization rather than doing it.

## Building the Solution: A Systematic Approach

Armed with specific failure patterns, I designed a prompt enhancer skill that addressed each documented weakness. The core insight was distinguishing between **mandatory techniques** (always applied) and **contextual techniques** (applied based on task complexity).

The mandatory techniques became the "80/20 rule" of prompt optimization:

1. **XML tags for structure** - `<instructions>`, `<data>`, `<output>`, `<example>`
2. **Clear role assignment** - Specific expert personas
3. **Data/instruction separation** - Security against prompt injection
4. **Explicit output format** - Exact templates and structures

For contextual techniques, I built decision trees:
- Chain of thought for complex reasoning tasks
- Few-shot examples for tasks requiring specific patterns
- Constraint handling for edge cases

The skill included a crucial "red flags" section to prevent rationalization:

> "This task is simple enough to skip XML tags" ❌
> "User wants it short, so I'll avoid examples" ❌
> "Under time pressure, skipping advanced techniques" ❌

I tested the skill with the same pressure scenarios that had failed before:

> **Me**: "Keep it simple - just improve this basic prompt"
> 
> **Claude with skill**: "I'll apply the core techniques systematically. Even 'simple' prompts benefit from XML structure and clear roles..."

Success! The agent now applied techniques consistently rather than rationalizing shortcuts.

## The Systematic Difference

The final skill created a transformation in prompt optimization consistency. The same scenarios that previously produced inconsistent results now generated predictable, high-quality optimizations:

**Before the skill:**
- 0/4 agents used XML tags
- 0/4 added chain of thought
- 0/4 implemented actual examples
- 1/4 explicitly skipped techniques under pressure

**With the skill:**
- 4/4 apply XML tags systematically
- 4/4 add chain of thought when appropriate
- 4/4 include actual few-shot examples
- 0/4 skip techniques under pressure

The skill successfully prevented the "simple task trap" where agents would rationalize away important techniques. It recognized that consistent application of core practices matters more than perfect customization for each scenario.

## The Bigger Lesson

This exercise revealed something important about working with AI systems: consistency often matters more than sophistication. The most elegant prompt engineering knowledge becomes useless if it's applied inconsistently or abandoned under pressure.

By applying Test-Driven Development to prompt optimization, I created a system that:
- Documents specific failure patterns before building solutions
- Addresses actual weaknesses rather than theoretical improvements
- Builds in safeguards against common rationalizations
- Maintains quality under pressure

The prompt enhancer skill now reliably applies Anthropic's best practices from their courses and documentation. More importantly, it does so consistently, whether the task seems "simple" or "complex," whether there's time pressure or not.

Next time you're building AI-assisted tools, consider starting with failure documentation. Test your system under pressure. Build defenses against the rationalizations that lead to shortcuts. Sometimes the most valuable engineering happens not in the happy path, but in preventing the predictable ways things go wrong.