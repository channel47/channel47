# Content Refresh Implementation Plan

## Implementation Summary

**Status:** COMPLETED on 2025-12-24

**Branch:** content-refresh

**Changes:**
- 7 files transformed
- 10 commits made
- Build successful (14 pages)

**Files Modified:**
1. src/pages/index.astro - Homepage hero and email signup
2. src/pages/about.astro - About page with section hierarchy
3. src/content/plugins/creative-writing.md - Plugin page copy
4. src/content/plugins/google-ads.md - Plugin page copy
5. src/content/blog/hello-world.md - "The Beginning" blog post
6. src/content/blog/creative-writing-tooling.md - "Building a Creative Writing Plugin" post
7. src/content/blog/2025-12-22_ai-workflow-branded-search.md - "AI Workflow Branded Search" post

**Key Improvements:**
- Shortened sentences to 15-20 words (was 25-40+ in many places)
- Transformed paragraphs to 2-4 sentences (was 6-10 in many places)
- Added section headings (H2) for better hierarchy and scanability
- Removed hedging language and em-dashes
- Applied Paul Graham-style: lead with the point, conversational but precise
- Preserved technical accuracy and code blocks

**Build Status:**
- Build: PASSED (14 pages generated)
- Preview: All pages render correctly
- No broken formatting or markdown issues

**Next Steps:**
1. Create pull request from content-refresh branch
2. Review changes on GitHub
3. Merge to main when ready

---

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Transform all site content to Paul Graham-style writing with short sentences, 2-4 sentence paragraphs, and clear hierarchy.

**Architecture:** Use the creative-writing plugin's /edit-draft skill with the Channel 47 style guide to systematically transform content. Work through marketing pages first (highest impact), then blog posts, finishing with quality verification.

**Tech Stack:**
- creative-writing@channel47 plugin for content transformation
- Channel 47 style guide at docs/channel47-style-guide.md
- Manual structural adjustments where needed

---

## Phase 1: Marketing Pages

### Task 1: Transform Homepage Hero

**Files:**
- Modify: `src/pages/index.astro:8-24`

**Step 1: Read current homepage content**

Run: `cat src/pages/index.astro`
Expected: See hero section with title and description

**Step 2: Extract and transform hero copy**

Current copy:
```
Claude Code tools I actually use.
I spend way too much time building and testing Claude Code extensions. This is where I publish the ones worth keeping. Skills, plugins, MCP servers. Some I built myself, others I found and verified.
```

Use creative-writing plugin:
```
/edit-draft --style-guide docs/channel47-style-guide.md
[Paste the hero copy]
```

Expected transformation:
- Shorter sentences (15-20 words max)
- Lead with the point
- Remove hedging ("way too much")
- Conversational but precise

**Step 3: Update homepage with transformed copy**

Apply the transformed copy to src/pages/index.astro, updating both title and description in the hero section.

**Step 4: Review visual hierarchy**

Check:
- Title is still h1
- Description text size is appropriate
- Accent span still works stylistically

**Step 5: Commit**

```bash
git add src/pages/index.astro
git commit -m "refactor: transform homepage hero to style guide"
```

### Task 2: Transform Email Signup Copy

**Files:**
- Modify: `src/pages/index.astro:36-41`

**Step 1: Extract current email signup copy**

Current:
```
title="Get notified when I add new tools"
description="Usually once or twice a month. I only send updates when there's something genuinely useful."
```

**Step 2: Transform with style guide**

Use /edit-draft with style guide on the title and description.

Expected: Shorter, more direct value proposition.

**Step 3: Update EmailSignup component props**

Apply transformed copy to the EmailSignup component in src/pages/index.astro.

**Step 4: Commit**

```bash
git add src/pages/index.astro
git commit -m "refactor: simplify email signup copy"
```

### Task 3: Transform About Page

**Files:**
- Modify: `src/pages/about.astro:27-37`

**Step 1: Read current about page content**

Run: `cat src/pages/about.astro`
Expected: Three paragraphs about the site and author

**Step 2: Transform about content**

Current content (extract from lines 27-37):
```
This is a personal collection of Claude Code tools I've built and vetted. I'm a developer who spends too much time in Claude Code, so I built the extensions I wanted to exist.

Everything here is free and open source. Some plugins I built myself. Others I found, tested thoroughly, and recommend. If it's listed here, I use it in my own work.

The blog covers workflows, patterns, and occasional deep dives into how these tools actually work under the hood.
```

Use /edit-draft with style guide.

Expected:
- Break long sentences
- Remove hedging ("too much time")
- Each paragraph 2-4 sentences
- Lead with key points

**Step 3: Add section headings for hierarchy**

The about page should have better hierarchy. Consider adding H2 headings:
- "What This Is"
- "What You'll Find"

This improves scanability.

**Step 4: Update about page with transformed copy and headings**

Apply transformed copy and new H2 headings to src/pages/about.astro.

**Step 5: Commit**

```bash
git add src/pages/about.astro
git commit -m "refactor: transform about page with better hierarchy"
```

### Task 4: Transform Creative Writing Plugin Page

**Files:**
- Modify: `src/content/plugins/creative-writing.md:6-94`

**Step 1: Read current plugin page**

Run: `cat src/content/plugins/creative-writing.md`

**Step 2: Transform "What it does" section**

Current (lines 6-8):
```
Transform your writing from AI-generated patterns to clear, honest prose. This plugin helps you write with your own voice—whether you're editing AI drafts or creating content from scratch.
```

Use /edit-draft with style guide.

Expected: Break into 2-3 shorter sentences, remove em-dash.

**Step 3: Transform "What makes it different" section**

Current (lines 29-38) has multiple paragraphs explaining differences.

Use /edit-draft on this entire section.

Expected:
- Shorter sentences
- 2-4 sentence paragraphs
- Remove list headers that aren't H3s
- Lead with insights

**Step 4: Transform "Real-world use cases" section**

Current (lines 19-27) is a bulleted list with preamble.

Transform the preamble sentence, keep list concise.

**Step 5: Review and apply all transformations**

Apply all transformed sections to src/content/plugins/creative-writing.md.

Check hierarchy:
- H2s are properly used
- Code blocks are still formatted correctly
- Bulleted lists remain readable

**Step 6: Commit**

```bash
git add src/content/plugins/creative-writing.md
git commit -m "refactor: transform creative-writing plugin page copy"
```

### Task 5: Transform Google Ads Plugin Page

**Files:**
- Modify: `src/content/plugins/google-ads.md:6-131`

**Step 1: Read current plugin page**

Run: `cat src/content/plugins/google-ads.md`

**Step 2: Transform "What it does" section**

Current (lines 6-10) has two paragraphs.

Use /edit-draft with style guide.

Expected:
- Break long sentences (the 37-word first sentence is too long)
- Each paragraph 2-4 sentences
- Remove em-dashes

**Step 3: Transform "Real-world use cases" section**

Current (lines 21-36) has preamble + bulleted list + follow-up explanation.

Transform preamble and follow-up paragraphs.
Keep bulleted list concise.

**Step 4: Transform "What makes it different" section**

Current (lines 38-47) contrasts old vs new approach.

Transform to:
- Shorter sentences
- Remove "Instead of:" header if it's not an H3
- Tighten the comparison

**Step 5: Transform "Setup" section**

Current (lines 49-67) explains time investment and steps.

Transform preamble paragraphs while keeping numbered list intact.

**Step 6: Review and apply all transformations**

Apply transformed sections to src/content/plugins/google-ads.md.

Verify:
- Code blocks unchanged
- Numbered steps unchanged
- H2/H3 hierarchy makes sense

**Step 7: Commit**

```bash
git add src/content/plugins/google-ads.md
git commit -m "refactor: transform google-ads plugin page copy"
```

---

## Phase 2: Blog Posts

### Task 6: Transform "The Beginning" Blog Post

**Files:**
- Modify: `src/content/blog/hello-world.md:8-14`

**Step 1: Read current blog post**

Run: `cat src/content/blog/hello-world.md`

**Step 2: Transform entire post content**

Current post is 3 paragraphs (lines 8-14).

Use /edit-draft with style guide on all content.

Expected:
- Shorter sentences (some are 30+ words)
- Break long paragraphs into 2-4 sentence chunks
- Lead with insights
- Keep conversational tone but precise words

**Step 3: Review paragraph breaks**

The transformed content should have 5-7 shorter paragraphs instead of 3 long ones.

Each paragraph should start with the point.

**Step 4: Apply transformations**

Update src/content/blog/hello-world.md with transformed copy.

**Step 5: Commit**

```bash
git add src/content/blog/hello-world.md
git commit -m "refactor: transform 'The Beginning' blog post"
```

### Task 7: Transform "Building a Creative Writing Plugin" Blog Post

**Files:**
- Modify: `src/content/blog/creative-writing-tooling.md:24-46`

**Step 1: Read current blog post**

Run: `cat src/content/blog/creative-writing-tooling.md`

**Step 2: Identify sections needing transformation**

The post is long (47 paragraphs). Focus on sections with:
- Sentences over 25 words
- Paragraphs over 6 sentences
- Em-dashes or hedging language

**Step 3: Transform opening section (lines 24-28)**

Current opening has very long sentences and paragraphs.

Use /edit-draft with style guide on the first 5 paragraphs.

**Step 4: Transform middle narrative (lines 29-36)**

This section explains the subagent process.

Transform to:
- Break long sentences describing workflow
- Keep paragraphs to 2-4 sentences
- Lead with what happened, then explain

**Step 5: Transform conclusion (lines 40-46)**

Final paragraphs reflect on the approach.

Use /edit-draft to tighten and clarify.

**Step 6: Add H2 section headings for hierarchy**

Consider adding:
- "The Problem"
- "The Approach"
- "What Actually Happened"
- "The Trade-offs"

This improves scanability for long posts.

**Step 7: Apply all transformations**

Update src/content/blog/creative-writing-tooling.md with:
- Transformed copy
- New H2 headings
- Better paragraph breaks

**Step 8: Commit**

```bash
git add src/content/blog/creative-writing-tooling.md
git commit -m "refactor: transform creative writing plugin blog post with better hierarchy"
```

### Task 8: Transform "AI Workflow Branded Search" Blog Post

**Files:**
- Modify: `src/content/blog/2025-12-22_ai-workflow-branded-search.md:25-44`

**Step 1: Read current blog post**

Run: `cat src/content/blog/2025-12-22_ai-workflow-branded-search.md`

**Step 2: Transform opening hook (lines 25-26)**

Current opening is one very long paragraph.

Use /edit-draft to:
- Break into 3-4 shorter paragraphs
- Lead with the frustration, then explain
- Shorter sentences

**Step 3: Transform main narrative (lines 27-43)**

Multiple long paragraphs explaining the workflow.

Transform to:
- 2-4 sentence paragraphs
- Lead with what happened
- Break complex explanations into steps

**Step 4: Transform conclusion (line 44)**

Final paragraph wraps up the lesson.

Tighten to 2-3 sentences.

**Step 5: Add H2 section headings**

Consider:
- "The Old Way"
- "Treating It Like Code"
- "What It Did"
- "Why It Worked"

**Step 6: Apply all transformations**

Update src/content/blog/2025-12-22_ai-workflow-branded-search.md with:
- Transformed copy
- Section headings
- Paragraph breaks

**Step 7: Commit**

```bash
git add src/content/blog/2025-12-22_ai-workflow-branded-search.md
git commit -m "refactor: transform AI workflow blog post with section hierarchy"
```

---

## Phase 3: Quality Check

### Task 9: Verify Sentence Length Across All Content

**Step 1: Spot check sentence lengths**

Read through transformed content and verify:
- Most sentences are 15-20 words
- No sentences exceed 25 words unless absolutely necessary

**Step 2: Check for common violations**

Look for:
- Em-dashes joining thoughts (should be periods)
- Hedging words ("probably," "maybe," "I think")
- Unnecessary intensifiers ("very," "really")

**Step 3: Fix any violations**

Make manual edits to fix any remaining issues.

**Step 4: Commit any fixes**

```bash
git add [affected files]
git commit -m "refactor: final sentence length cleanup"
```

### Task 10: Verify Paragraph Structure

**Step 1: Check paragraph lengths**

Scan all transformed content for:
- Paragraphs over 6 sentences (break them up)
- Paragraphs that don't lead with the point

**Step 2: Verify hierarchy makes sense**

Check:
- H2s mark major section shifts
- H3s are used sparingly
- No H4s (keep it simple)

**Step 3: Make structural adjustments**

Add or adjust headings as needed.

**Step 4: Commit adjustments**

```bash
git add [affected files]
git commit -m "refactor: final paragraph and hierarchy cleanup"
```

### Task 11: Final Build Test

**Step 1: Run build**

```bash
npm run build
```

Expected: Successful build with 14 pages

**Step 2: Preview site locally**

```bash
npm run preview
```

**Step 3: Spot check pages**

Visit:
- Homepage
- About page
- 2-3 plugin pages
- 2-3 blog posts

Verify:
- Content renders correctly
- No broken formatting
- Headings look good
- Readability is improved

**Step 4: Document any issues**

If any rendering issues, note them for fixes.

### Task 12: Final Commit and Summary

**Step 1: Check git status**

```bash
git status
```

Expected: All changes committed

**Step 2: Review commit history**

```bash
git log --oneline -15
```

Expected: Clean commit history with descriptive messages

**Step 3: Push branch**

```bash
git push -u origin content-refresh
```

**Step 4: Document transformation**

Add a summary to the top of this plan documenting:
- Total files changed
- Key improvements
- Any remaining manual work needed

---

## Execution Notes

**Style guide location:** `docs/channel47-style-guide.md`

**Creative writing plugin usage:**
```
/edit-draft --style-guide docs/channel47-style-guide.md
[paste content to transform]
```

**Common transformation patterns:**
- Break sentences at em-dashes → use periods instead
- Remove hedging → "I think" becomes declarative statement
- Lead with point → move insight from middle to start
- Break long paragraphs → 2-4 sentences per paragraph

**Manual review needed:**
- Section headings (H2/H3 placement)
- Code block formatting preserved
- Bulleted/numbered lists still readable
- Technical accuracy maintained

**Testing:**
- Run `npm run build` after each phase
- Spot check pages in `npm run preview`
- Verify no broken markdown rendering
