---
name: script-writer
description: This skill should be used when the user asks to "write ad scripts", "write a VSL", "UGC script", "video ad script", "write a script for", "YouTube ad script", "TikTok script", "Facebook ad script", "create video scripts", "direct response script", "sales script", or mentions writing, creating, or generating video or audio ad scripts for DTC products. Trigger after research, personas, and angles are available, or when the user provides an angle and wants it turned into a script.
---

# Script Writer — Direct Response Ad Scripts

This skill generates production-ready video and audio ad scripts for DTC products across all major platforms. Scripts are built on top of research data, personas, and angles — never from thin air.

## Script Types This Skill Handles

1. **UGC Scripts** (30-90 sec) — Casual, first-person, "real person talking to camera" format for Meta/TikTok
2. **VSL Scripts** (3-15 min) — Long-form video sales letters for dedicated landing pages or YouTube
3. **YouTube Pre-Roll** (15-30 sec) — Quick-hit scripts designed to hook before the skip button
4. **TikTok Native** (15-60 sec) — Platform-native scripts that feel organic, not ad-like
5. **Podcast/Audio** (30-60 sec) — Host-read or produced audio ad scripts

## The Script Generation Process

### Step 1: Gather Inputs

Read from workspace:
- Research file (`*-research.md`) — for customer language
- Personas file (`*-personas.md`) — for targeting
- Angles file (`*-angles.md`) — for strategic direction

If the user provides a specific angle to script, use that. Otherwise, script the top 2-3 angles.

Ask the user (if not specified):
- Which script format(s) they want
- Any brand voice guidelines or restrictions
- Offer details (price, guarantee, bonuses)
- Call-to-action (URL, discount code, etc.)

### Step 2: Apply the Script Framework

Every direct response script follows a core structure. The proportions shift by format, but the bones are the same:

#### Universal DR Script Framework

**1. HOOK (first 3-5 seconds)**
The single most important part. Must stop the scroll/skip. Three proven hook types:
- **Pattern Interrupt**: Something unexpected that breaks autopilot browsing
- **Problem Call-Out**: Directly name the pain the viewer is experiencing right now
- **Curiosity Gap**: Open a loop that can only be closed by watching

Use the exact language from the research data. If customers say "I've tried everything and nothing works," the hook can literally start with that phrase.

**2. PROBLEM AGITATION (next 10-30 seconds)**
Expand on the pain. Make the viewer feel seen and understood. This is where persona data is critical — describe their specific situation, not a generic one.

Stack 2-3 pain points in escalating intensity:
- Surface pain → Deeper consequence → Emotional core

**3. FAILED SOLUTIONS (10-20 seconds)**
Acknowledge what they've already tried. This builds credibility and positions the product as different.
- "You've probably tried X... and Y... maybe even Z..."
- Brief explanation of why each didn't work

**4. BRIDGE / MECHANISM (10-30 seconds)**
Introduce the product — but lead with the mechanism (HOW it works), not the product name.
- What's unique about the approach?
- Why is this different from what they've tried?
- Use "discovery" language if the mechanism is novel

**5. PROOF (15-60 seconds, scales with format)**
Stack credibility:
- Customer testimonials/results (use language from research)
- Authority endorsements if available
- Demonstrations or before/afters
- Specificity (numbers, timeframes, percentages)

**6. OFFER (10-20 seconds)**
Present the deal:
- What they get
- Bonuses (if any)
- Price anchoring (compare to alternatives or cost-of-problem)
- Risk reversal (guarantee)

**7. CTA (5-10 seconds)**
Clear, urgent, specific:
- Tell them exactly what to do
- Repeat the key benefit one more time
- Create gentle urgency (without being sleazy)

### Step 3: Format-Specific Adaptation

#### UGC Script (30-90 sec)
```
[VISUAL NOTE: Person talking directly to camera, casual setting]

HOOK: [3-5 seconds — conversational, like telling a friend]

"Okay so I have to tell you about this because I literally
[pain point in their own words]..."

PROBLEM + FAILED SOLUTIONS: [15-25 seconds — compressed]

BRIDGE: [10-15 seconds — "then I found..." energy]

PROOF: [10-20 seconds — personal result, show product in use]

CTA: [5-10 seconds — "link in bio" / "I'll put the link below"]
```

Key principles:
- Write like people actually talk — contractions, filler words, run-on sentences
- Include stage directions for visual beats
- Keep it under 200 words for 60-sec version
- Open loops early (e.g., "wait till I show you what happened")

#### VSL Script (3-15 min)
```
HOOK: [Strong pattern interrupt or curiosity hook — 15-30 seconds]

STORY/PROBLEM: [Personal or relatable story that mirrors the customer's situation — 2-3 min]

FAILED SOLUTIONS: [What they've tried, why it didn't work — 1-2 min]

MECHANISM/DISCOVERY: [Detailed explanation of how the product works differently — 2-3 min]

PROOF STACK: [Multiple testimonials, data points, demonstrations — 2-3 min]

OFFER PRESENTATION: [Full offer stack with bonuses and guarantee — 1-2 min]

CLOSE: [Urgency, final CTA, pain/pleasure contrast — 1-2 min]
```

Key principles:
- Every 30-60 seconds must contain a reason to keep watching
- Use "open loops" — tease upcoming reveals
- Longer proof section than any other format
- Write section headers as internal notes, not spoken text

#### YouTube Pre-Roll (15-30 sec)
```
[FIRST 5 SECONDS — before skip button]
HOOK: [Must be so compelling they don't skip]

[REMAINING 10-25 SECONDS]
PROBLEM: [One sharp pain point]
SOLUTION: [One clear benefit]
CTA: [Visit URL / Search for brand]
```

Key principles:
- The first 5 seconds ARE the ad — everything after is bonus
- No slow builds — hit hard immediately
- Brand name must appear visually even if not spoken early

#### TikTok Native (15-60 sec)
```
[HOOK — pattern interrupt, green screen, stitch format]
"Wait — if you [audience identifier], you NEED to know this..."

[CONTENT — fast-paced, cuts every 3-5 seconds]
[Problem → Discovery → Proof → CTA]

[CTA — native to platform]
"Link in bio" / "Comment [word] and I'll send you the link"
```

Key principles:
- Must feel native, not produced
- Use trending formats/sounds when relevant
- Quick cuts maintain attention
- Comments section strategy (pin a comment, encourage engagement)

### Step 4: Write Multiple Versions

For each angle being scripted:
- Write 2-3 hook variations (different hook types)
- Write 1 full script per format requested
- Include stage directions and visual notes
- Note where B-roll, text overlays, or graphics should appear

### Step 5: Save Output

Save to the workspace as `[product-slug]-scripts.md`.

Organize by angle, then by format within each angle:

```
# Scripts for [Product]

## Angle: [Angle Name]
### UGC Script (60 sec)
### YouTube Pre-Roll (15 sec)

## Angle: [Angle Name 2]
### UGC Script (60 sec)
### TikTok Native (30 sec)
```

## Quality Standards

- Every script must trace back to a specific angle, which traces back to real research
- Customer language from the research should appear naturally in the scripts
- Hooks must be genuinely compelling — not generic "Are you tired of..." openers
- Scripts must be the right length for their format (time it by reading aloud at natural pace)
- Include visual/stage direction notes — scripts aren't just words, they're production blueprints

## Additional Resources

### Reference Files
- **`references/script-frameworks.md`** — Expanded frameworks, formula variations, and examples for each script type
