---
name: conversation-logger
description: This skill should be used when the user asks to "log this conversation", "save this conversation", "capture this conversation", "save this to logs", "log this session", or wants to preserve a conversation transcript for future content creation.
version: 0.1.0
---

# Conversation Logger Skill

## Purpose

The conversation-logger skill captures valuable conversation transcripts and saves them to the repository's `logs/` directory as markdown files. These transcripts serve as raw material for the content synthesis pipeline, which transforms them into polished blog posts and social media content.

This skill is part of the Channel 47 content creation system, where work sessions naturally generate the raw material for build-in-public content.

## When to Use This Skill

Use this skill when:

- A conversation contains valuable insights, problem-solving, or learning moments worth preserving
- The user explicitly requests to log or save the current conversation
- The discussion demonstrates interesting techniques, workflows, or patterns
- The conversation could become a blog post, tutorial, or social media thread
- The session involves building, debugging, or exploring something worth sharing

## How to Use This Skill

### 1. Determine the Conversation Topic

Analyze the conversation to identify:
- The main topic or problem being addressed
- Key insights or solutions discovered
- Technical domains involved (e.g., "astro-setup", "claude-code-skills", "api-integration")

### 2. Generate the Log Filename

Create a filename using this format:
```
YYYY-MM-DD-brief-topic-description.md
```

Examples:
- `2025-12-19-astro-content-collections-setup.md`
- `2025-12-19-claude-skill-development-workflow.md`
- `2025-12-19-debugging-vercel-deployment.md`

Guidelines:
- Use today's date in ISO format (YYYY-MM-DD)
- Use kebab-case for the topic description
- Keep the filename concise but descriptive (3-6 words for topic)
- Focus on the technical subject matter

### 3. Format the Conversation Transcript

Structure the markdown file with:

**Header:**
```markdown
# [Topic Title]

**Date:** YYYY-MM-DD
**Tags:** tag1, tag2, tag3

---
```

**Body:**
- Include the full conversation transcript
- Preserve the original message structure
- Use `>` blockquotes for user messages
- Use regular paragraphs for Claude's responses
- Include code blocks with proper language tags
- Preserve tool calls and results when relevant to understanding

**Example format:**
```markdown
# Setting Up Astro Content Collections

**Date:** 2025-12-19
**Tags:** astro, content-collections, blog-setup

---

> User: I need to set up content collections for my blog posts.

To set up content collections in Astro, start by creating the `src/content/config.ts` file...

[Continued conversation...]
```

### 4. Save to the Logs Directory

Write the file to:
```
logs/YYYY-MM-DD-topic-description.md
```

Confirm the save location and filename to the user.

### 5. Provide Next Steps

After saving, inform the user:

1. The log has been saved successfully
2. The filename and location
3. Optional: Suggest whether this conversation would make good content
4. Optional: Note that the synthesis pipeline will process it on the next run

## Content Quality Guidelines

Save conversations that demonstrate:

- **Problem-solving:** Debugging, troubleshooting, overcoming obstacles
- **Learning:** Discovering new techniques, understanding complex concepts
- **Building:** Creating features, tools, or systems from scratch
- **Exploration:** Investigating codebases, APIs, or architectures
- **Decision-making:** Evaluating options, choosing approaches, trade-off analysis

Avoid logging:
- Trivial fixes or single-line changes
- Conversations with no valuable insights
- Sessions that are purely administrative
- Repetitive troubleshooting without resolution

## Integration with Synthesis Pipeline

The saved logs feed into the content synthesis system:

```
conversation-logger → logs/ → GitHub Actions → Claude API synthesis → PR with drafts
```

The synthesis pipeline:
1. Detects new files in `logs/`
2. Calls Claude API to generate blog post + social content
3. Creates a PR with drafts in `drafts/blog/` and `drafts/x/`
4. User reviews and merges (or edits) the generated content
5. Merged posts auto-publish to the live site

## Technical Notes

- **Repository:** Assumes a Git repository with a `logs/` directory at the root
- **File format:** Markdown (.md) only
- **Permissions:** Requires write access to the repository
- **Git workflow:** The skill saves files but does not commit them - user should commit and push manually or via a separate commit flow

## Examples

### Example 1: Development Session

**Trigger:** "Save this conversation to logs"

**Action:**
1. Review conversation about implementing Astro content collections
2. Create filename: `2025-12-19-astro-content-collections.md`
3. Format conversation with header and proper markdown
4. Save to `logs/2025-12-19-astro-content-collections.md`
5. Confirm to user

### Example 2: Debugging Session

**Trigger:** "Log this debugging session"

**Action:**
1. Review conversation about fixing Vercel deployment issues
2. Create filename: `2025-12-19-vercel-deployment-debugging.md`
3. Include problem description, investigation steps, and solution
4. Save to `logs/2025-12-19-vercel-deployment-debugging.md`
5. Suggest this would make a good troubleshooting post

### Example 3: Learning Session

**Trigger:** "Capture this conversation"

**Action:**
1. Review conversation exploring Claude Code skill development
2. Create filename: `2025-12-19-claude-skill-development.md`
3. Preserve the exploration and learning arc
4. Save to `logs/2025-12-19-claude-skill-development.md`
5. Note the meta nature (conversation about creating the logger skill itself)

## Best Practices

1. **Be selective:** Not every conversation deserves logging - focus on quality over quantity
2. **Preserve context:** Include enough context for the conversation to make sense standalone
3. **Clean formatting:** Ensure markdown is properly formatted for readability
4. **Descriptive filenames:** Make it easy to identify content at a glance
5. **Consistent dating:** Always use ISO date format (YYYY-MM-DD)
6. **Tag appropriately:** Add 2-5 relevant tags in the header for categorization
7. **Complete narratives:** Log conversations that have a clear arc or resolution

## Workflow Integration

This skill works best when:
- Invoked at the end of valuable sessions
- Part of a regular content creation rhythm (3-5 logs per week target)
- Followed by periodic synthesis runs (weekly or bi-weekly)
- Integrated with the user's blogging and social media strategy

The goal is to make content creation effortless by capturing raw material as it naturally occurs during real work.
