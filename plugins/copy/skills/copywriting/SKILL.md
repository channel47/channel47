---
name: copywriting
description: |
  Master copywriting with Schwartz awareness levels, Hemingway economy, and Halbert conversational urgency.
  Use when writing sales copy, emails, landing pages, headlines, or analyzing/improving existing copy.
args:
  - name: awareness
    description: Prospect awareness level (1-5) for Schwartz framework
    required: false
---

# The Copywriter's Arsenal

Three essential frameworks for copy that moves people emotionally AND motivates action.

## Core Frameworks

### 1. Schwartz: Meet Them Where They Are
**Eugene Schwartz's 5 awareness levels** - the foundation of all copy decisions.

| Level | State | Copy Strategy |
|-------|-------|---------------|
| **5** Most Aware | Know you, trust you | Lead with the offer, deal focus |
| **4** Product Aware | Know what you sell | Differentiate, prove superiority |
| **3** Solution Aware | Know solutions exist | Unique mechanism, why you're different |
| **2** Problem Aware | Feel the pain | Agitate problem, introduce solution |
| **1** Unaware | Don't know problem | Lead with story, build awareness |

Load full framework: @frameworks/direct-response/schwartz.md

### 2. Hemingway: Economy of Words
**Ernest Hemingway's iceberg theory** - what you leave out matters more.

- Cut ruthlessly. Every word must earn its place.
- Show, don't tell. Let actions reveal character.
- Use short sentences. They create urgency.
- Avoid adjectives. Strong nouns and verbs suffice.
- Subtext carries meaning. The unsaid speaks loudest.

Load full framework: @frameworks/storytellers/hemingway.md

### 3. Halbert: Conversational Urgency
**Gary Halbert's A-pile approach** - write like you're talking to one person, urgently.

- Personal tone. "You" is the most powerful word.
- Story-driven. Everyone loves a good story.
- Strong P.S. - often read before the body.
- One idea, one reader, one action.
- Create urgency without being sleazy.

Load full framework: @frameworks/direct-response/halbert.md

## Decision Framework

### Step 1: Identify Awareness Level
Use Schwartz's 5 levels to assess where the prospect stands. This determines EVERYTHING.

### Step 2: Choose Your Voice
- **Hemingway** for economy, restraint, sophistication
- **Halbert** for conversational warmth, urgency, personal connection

### Step 3: Weight Story vs. Offer

| Awareness | Story Weight | Offer Weight |
|-----------|--------------|--------------|
| Unaware (1) | 80% | 20% |
| Problem Aware (2) | 60% | 40% |
| Solution Aware (3) | 40% | 60% |
| Product Aware (4) | 20% | 80% |
| Most Aware (5) | 10% | 90% |

## Output Guidelines

When producing copy:
1. **State your approach** - Which framework and why
2. **Match awareness** - Don't oversell to the aware, don't undersell to the unaware
3. **End with options** - Provide 2-3 variations when appropriate
4. **Explain the psychology** - Help the user understand WHY each element works

## Quick Reference: Copy Types

| Copy Type | Primary Framework | Key Focus |
|-----------|------------------|-----------|
| Headlines | Hemingway | Curiosity + Economy |
| Email Subject Lines | Halbert | Urgency + Personal |
| Sales Pages | Schwartz | Awareness Matching |
| Landing Pages | Schwartz | Journey + Proof |
| Email Sequences | Halbert | Story + Connection |

## Utility Scripts

Determine awareness level interactively:
```bash
python skills/copywriting/scripts/awareness_check.py --interactive
```

Quick awareness assessment:
```bash
python skills/copywriting/scripts/awareness_check.py "Description of target audience"
```

Analyze copy structure and patterns:
```bash
python skills/copywriting/scripts/analyze_swipe.py "Your copy here"
python skills/copywriting/scripts/analyze_swipe.py --file /path/to/copy.txt --json
```

These scripts run without loading into context—only their output is used.

## Error Handling

If the user's request is unclear:
1. Ask about the target audience
2. Ask about the awareness level (1-5)
3. Ask about the desired action
4. Ask about existing brand voice

Never guess on these critical elements—they determine everything.
