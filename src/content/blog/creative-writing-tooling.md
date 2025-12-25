---
title: "Building a Creative Writing Plugin"
description: "How we went from design document to fully implemented Claude plugin with 7 writing skills, complete testing, and a merged PR in a single development session."
date: 2025-12-21
tags:
  [
    "claude-plugins",
    "ai-development",
    "subagent-driven-development",
    "creative-writing",
    "automation",
  ]
toolsUsed:
  - slug: "creative-writing"
    source: "channel47"
heroImages:
  styleA: "/images/blog-heroes/conversation_2025-12-21_14-59-44/style-a.png"
  styleD: "/images/blog-heroes/conversation_2025-12-21_14-59-44/style-d.png"
  selected: null
visualMetaphor: "An orchestra conductor's podium with sheet music scattered around, transforming into neat, organized musical scores flowing in perfect harmony."
visualMetaphorReasoning: "Captures the coordination of multiple specialized agents working in orchestrated harmony."
---

I've been testing subagent-driven development on throwaway projects. Small experiments where the outcome doesn't matter. Last week I used it for something real.

I built a creative writing plugin for Claude. It needed 7 distinct skills, style guide integration, full documentation, and proper testing workflows. The whole thing took one afternoon. Design document to merged pull request. It worked.

## The Problem

Most development projects don't go this way. You start strong. Then you hit the middle where everything's half-done and interconnected. You're switching between writing code, updating docs, testing edge cases. You're trying to remember what you decided three hours ago about error handling. By the time you ship, you've lost most of your initial momentum.

## What I Built

The plugin needed seven writing skills. Edit-draft, review-writing, generate-content. Each one had to work with a style guide system that could chunk long documents intelligently. Settings templates for customization. Documentation with examples. Quality checks across everything.

Normally I'd build one skill, get distracted fixing something else, come back, and forget what I was doing. The usual mess.

## The Approach

I told the main Claude instance to execute the plan. It spun up specialized subagents for each piece. One subagent built the basic plugin structure. Two more immediately reviewed it. One checked spec compliance. One checked code quality.

When they found issues, another subagent got dispatched to fix those specific problems. Then the reviewers ran again.

Each subagent had one job. The implementers only built things. The spec reviewers only checked adherence to requirements. The quality reviewers only looked at code standards. Nobody tried to do everything at once.

## What Happened

By the fourth task, the system started batching similar work. The seven writing skills got handled efficiently without losing quality. Documentation tasks got bundled together near the end. This included README files, getting started guides, testing procedures, changelog, licensing, and example configurations. All done by subagents that knew exactly what they were responsible for.

The final count was 17 commits across a complete plugin structure. All in one session. No half-finished branches. No "I'll come back to the docs later." Just done.

## The Trade-offs

This approach isn't perfect. The coordination overhead is real. You're constantly managing handoffs between specialists instead of grinding through the work yourself. If your plan is bad, the subagents will build the wrong thing very efficiently. The quality depends entirely on how well you decomposed the problem up front.

But traditional development fails when one person tries to hold too much in their head at once. You forget things. You make inconsistent decisions. You get tired and start cutting corners.

When each piece gets handled by a fresh perspective with a single clear focus, those problems mostly disappear. The implementer isn't thinking about code style. The reviewer isn't thinking about implementation details. Everything gets proper attention because nobody's trying to multitask.

## The Pattern

The pattern works whether you use AI subagents or actual humans. Break the work into discrete chunks. Give each chunk to someone with a single responsibility. Put quality gates between major steps. Make the handoffs clean.

I'm curious if this matches anyone else's experience. Have you found ways to prevent the mid-project entropy where everything's half-done and interconnected? Does deliberate specialization work at scale, or does it only feel good on these focused afternoon sessions?
