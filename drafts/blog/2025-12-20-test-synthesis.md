---
title: "Building Your First Custom Claude Code Skill: A Commit Message Assistant"
description: "A step-by-step guide to creating a custom skill that helps Claude Code write better git commit messages."
date: 2025-12-20
tags: ["claude-code","custom-skills","git","commit-messages","ai-development"]
draft: true
---

# Building Your First Custom Claude Code Skill: A Commit Message Assistant

If you've been using Claude Code for development work, you've probably noticed how it adapts to different tasks. But did you know you can teach it new skills specific to your workflow?

Today, I needed a better way to write consistent commit messages. Instead of manually crafting them each time or relying on generic templates, I decided to create a custom Claude Code skill that would analyze my staged changes and generate conventional commit messages.

## Why Custom Skills Matter

Out of the box, Claude Code is incredibly capable, but every development team has unique patterns and preferences. Custom skills let you codify your team's best practices and make them instantly available whenever you're working with Claude.

Commit messages are a perfect example. We all know good commits are important, but writing them consistently takes mental energy that could be spent on actual code. A custom skill can automate this while maintaining your team's standards.

## The Discovery Process

When I asked Claude how to get started, the response was refreshingly straightforward:

> Let me help you create a commit message skill. First, we need to understand the structure of a Claude Code skill file.
> 
> Skills are markdown files with YAML frontmatter that define:
> - name: The skill identifier
> - description: When to use this skill  
> - The actual content/instructions

The simplicity hit me immediately. No complex APIs, no JSON schemas—just markdown files with some YAML metadata. This is exactly the kind of approachable design that makes Claude Code feel natural to extend.

## Building the Skill

The basic structure looks like this:

```markdown
---
name: write-commit-message
description: Generate conventional commit messages based on staged changes
---

# Writing Commit Messages

When the user asks for a commit message:

1. Review the staged changes with `git diff --staged`
2. Identify the type: feat, fix, chore, docs, refactor, test
3. Write a concise subject line (50 chars max)
4. Add detailed body if changes are complex
5. Follow conventional commits format
```

What I love about this approach is how declarative it is. Instead of writing code, I'm writing instructions for Claude to follow. The skill becomes documentation that Claude can execute.

## The Critical Details

Two things make or break a custom skill:

**Location matters:** Skills need to live in `.claude/skills/` in your project directory, or globally at `~/.claude/skills/`. The filename should match the skill name.

**Description is everything:** This is how Claude decides when to use your skill. As Claude explained:

> The `description` field is key. Claude reads all skill descriptions and picks relevant ones based on the user's request. Make your descriptions specific about when to use the skill.

A vague description means your skill might never get used. A specific one like "Use when user asks to write a commit message, generate a commit, or requests help with git commit" ensures it triggers at the right moments.

## What This Enables

Once you understand this pattern, you can create skills for anything:
- Code review checklists specific to your tech stack
- Documentation templates for your APIs
- Deployment scripts that follow your infrastructure patterns
- Testing strategies that match your quality standards

Each skill becomes a piece of institutional knowledge that any team member can access through natural language.

## The Bigger Picture

Custom skills represent something bigger than just automation—they're a way to encode your team's collective wisdom. Instead of hoping everyone remembers to write good commit messages or follows the right testing patterns, you can capture these practices as skills that Claude can apply consistently.

The next time you find yourself repeating the same instructions to Claude, or wishing it knew about your specific workflow, consider turning that knowledge into a skill. It's a small investment that pays dividends every time you work.

Start with something simple, like the commit message skill above. Once you see how natural it feels to extend Claude Code this way, you'll start seeing opportunities everywhere.