---
title: "Building a Creative Writing Plugin: From Concept to Implementation in One Session"
description: "How we went from design document to fully implemented Claude plugin with 7 writing skills, complete testing, and a merged PR in a single development session."
date: 2025-12-21
tags: ["claude-plugins","ai-development","subagent-driven-development","creative-writing","automation"]
draft: true
heroImages:
  styleA: "/images/blog-heroes/conversation_2025-12-21_14-59-44/style-a.png"
  styleD: "/images/blog-heroes/conversation_2025-12-21_14-59-44/style-d.png"
  selected: null
visualMetaphor: "An orchestra conductor's podium with sheet music scattered around, transforming into neat, organized musical scores flowing in perfect harmony."
visualMetaphorReasoning: "Captures the coordination of multiple specialized agents working in orchestrated harmony."
---

I've been testing this subagent-driven development approach for a while now, mostly on small throwaway projects. The kind where you're just seeing if something works, not really caring about the outcome. But last week I decided to use it for something real—a creative writing plugin for Claude with 7 distinct skills, style guide integration, full documentation, and proper testing workflows.

The whole thing took one afternoon. Design document to merged pull request. I'm still a bit surprised it worked.

Most development projects don't go this way. You start strong, then hit the middle where everything's half-done and interconnected. You're switching between writing code, updating docs, testing edge cases, and trying to remember what you decided three hours ago about error handling. By the time you actually ship, you've lost most of your initial momentum.

The creative writing plugin needed seven different writing skills—things like edit-draft, review-writing, generate-content. Each one had to work with a style guide system that could chunk long documents intelligently. Settings templates for customization. Documentation with examples. Quality checks across everything. Normally I'd build one skill, get distracted fixing something in another part, come back, forget what I was doing. The usual mess.

Here's what I did differently. I told the main Claude instance to execute the plan in this session, then watched it spin up specialized subagents for each piece. One subagent built the basic plugin structure. Two more immediately reviewed it—one checking spec compliance, one checking code quality. When they found issues, another subagent got dispatched just to fix those specific problems. Then the reviewers ran again.

Each subagent had one job. The implementers only built things. The spec reviewers only checked adherence to requirements. The quality reviewers only looked at code standards. Nobody tried to do everything at once.

By the fourth task, the system started batching similar work. "I'll now batch process the next several skill files since they follow similar patterns." The seven writing skills got handled efficiently without losing quality. Documentation tasks got bundled together near the end. README files, getting started guides, testing procedures, changelog, licensing, example configurations—all done by subagents that knew exactly what they were responsible for.

The final count was 17 commits across a complete plugin structure. All in one session. No half-finished branches. No "I'll come back to the docs later." Just done.

I'm not saying this approach is perfect. The coordination overhead is real—you're constantly managing handoffs between specialists instead of just grinding through the work yourself. And if your plan is bad, the subagents will happily build the wrong thing very efficiently. The quality of what you get completely depends on how well you decomposed the problem up front.

But here's what pushed me over the edge on this. Traditional development fails when one person tries to hold too much in their head at once. You forget things. You make inconsistent decisions. You get tired and start cutting corners. When each piece gets handled by a fresh perspective with a single clear focus, those problems mostly disappear. The implementer isn't thinking about code style. The reviewer isn't thinking about implementation details. Everything gets proper attention because nobody's trying to multitask.

Whether you use AI subagents or actual humans, the pattern is the same. Break the work into discrete chunks. Give each chunk to someone with a single responsibility. Put quality gates between major steps. Make the handoffs clean.

---

**Tools Used:** [Creative Writing Plugin](/plugins/creative-writing) - The plugin built using the process described in this article.

---

I'm curious if this matches anyone else's experience. Have you found ways to prevent the mid-project entropy where everything's half-done and interconnected? Does deliberate specialization actually work at scale, or does it only feel good on these focused afternoon sessions?
