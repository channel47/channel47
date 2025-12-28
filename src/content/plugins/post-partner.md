---
featured: true
draft: false
asciiIcon: |
  ╔═══════════╗
  ║  THOUGHT  ║
  ║  PARTNER  ║
  ╚═══════════╝
iconColor: "var(--color-accent-primary)"
---

## What it does

A thinking tool for turning raw material into posts worth sharing. You bring the raw material—a Claude Code log, voice memo transcript, draft, or rough idea. The tool helps you find the interesting part, pressure test whether it matters, and land on what you actually want to say.

The output is a **brief**—not the post itself. The brief holds your thinking so you can write the post now or later.

## Key Features

- **Adaptive conversation**: Adjusts based on what you bring (dense logs vs rough ideas)
- **Insight excavation**: Surfaces candidate insights for you to react to
- **Pressure testing**: Validates whether your take actually matters
- **Audience discovery**: Helps identify who specifically will care
- **Brief generation**: Structured output ready for writing

## Real-world use cases

Use this when:

- You have interesting raw material but can't find the angle
- You know there's something worth sharing but can't articulate it
- You've drafted something but it feels hollow
- You want to batch-process ideas for future posts
- You need to decide if an idea is worth writing up at all

Common scenarios:

- Processing a Claude Code session into a tutorial or insight
- Turning a voice memo ramble into a focused post
- Pressure testing a hot take before publishing
- Finding the shareable insight in technical work
- Building a queue of briefs for when you have writing energy

## What makes it different

Current options for turning ideas into posts are unsatisfying. You either do all the thinking yourself—which is slow and often results in ideas dying in drafts—or you hand it to an LLM and get back something that feels hollow.

Post Partner sits in the middle. It's a structured conversation that draws the post out of you. The model does real work—surfacing insights, proposing audiences, pressure testing claims—but you stay in control of the actual thinking. The words end up being yours.

This is explicitly **not a content generator**. It's a thinking tool that produces clarity, not copy.

## Setup

1. Install: `/plugin install post-partner@channel47`
2. Start immediately with `/post`

No configuration needed.

## Example workflow

**Start with raw material:**

```
/post
```

Paste your raw material. The conversation adapts:

- **Dense material** (logs, transcripts): Surfaces candidate insights for you to react to
- **Sparse material** (rough ideas): Asks questions to draw out more context
- **Draft posts**: Skips straight to pressure testing what you're trying to say

**What you get:**

A brief containing:

- **Raw material** — What you started with
- **The insight** — The interesting thing, in 1-2 sentences
- **Why it matters** — Who cares and why
- **The audience** — Who this is for, specifically
- **Your take** — Labeled as claim, observation, question, or provocation
- **The entry point** — The angle for your post

**Adaptive behavior:**

The model knows where it needs to end up (a complete brief) but how it gets there adapts:

- If you say "the interesting part is X"—it skips excavation and moves to pressure testing
- If you're circling and uncertain—it stays in exploration mode longer
- If something you say later changes the insight—it adjusts
- If you go quiet—it does more lifting; if you're riffing—it stays out of your way

Sometimes there's no post. That's fine. The tool makes it easy to exit without feeling like failure.

## Available commands

- `/post` - Start the brief generation process

See the [README](https://github.com/ctrlswing/channel47-marketplace/blob/main/plugins/post-partner/README.md) for more details.
