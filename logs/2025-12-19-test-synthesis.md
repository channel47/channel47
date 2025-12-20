# Test Conversation Log

## Building a Custom Claude Code Skill

**User:** I want to create a custom skill for Claude Code that helps me write better commit messages. How do I start?

**Claude:** Let me help you create a commit message skill. First, we need to understand the structure of a Claude Code skill file.

Skills are markdown files with YAML frontmatter that define:
- name: The skill identifier
- description: When to use this skill
- The actual content/instructions

**User:** Okay, show me an example.

**Claude:** Here's a basic structure for a commit message skill:

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

**User:** This is helpful! Where do I save this file?

**Claude:** Save it in `.claude/skills/` in your project, or in your global Claude Code directory at `~/.claude/skills/`. The filename should match the skill name, so `write-commit-message.md`.

**User:** Got it. And how does Claude know when to use this skill?

**Claude:** The `description` field is key. Claude reads all skill descriptions and picks relevant ones based on the user's request. Make your descriptions specific about when to use the skill.

For example: "Use when user asks to write a commit message, generate a commit, or requests help with git commit"

**User:** Perfect! Let me try creating one now.

## Key Takeaways

- Skills are markdown files with YAML frontmatter
- Save in `.claude/skills/` directory
- Description determines when skill is triggered
- Follow clear, step-by-step instructions in the skill body
