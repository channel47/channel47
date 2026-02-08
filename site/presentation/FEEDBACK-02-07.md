# Slidedeck Feedback — Feb 7 Run-Through

First dry run with Chiara. ~60 min recording.

---

## Section Order (Revised)

The current deck order doesn't match how a beginner needs to learn this. Agreed new flow:

| #   | Section                  | Notes                                                                              |
| --- | ------------------------ | ---------------------------------------------------------------------------------- |
| 1   | **The Ecosystem**        | Quick context — 3 tools, 3 jobs. Emphasize skills, breeze past MCP/sub-agents.     |
| 2   | **What Skills Are**      | Revised sub-order below.                                                           |
| 3   | **Build a Skill (live)** | Move this BEFORE demos. Audience builds one together first.                        |
| 4   | **Live Demos**           | Now the audience understands what they're looking at. Frame with personal stories. |
| 5   | **Safety + Resources**   | Fits naturally after the API-calling demo (ad refresher).                          |
| 6   | **Takeaway**             | Simplified — cut the starter kit cards, keep QR + "now go build something."        |

### "What Skills Are" sub-order (revised)

1. Skills in 60 Seconds
2. How Skills Actually Work (without vs. with, under the hood)
3. Anatomy of a SKILL.md
4. The Best Skills Are Personal
5. Common Skill Mistakes
6. What Skills Are NOT

Previously: 60s → Anatomy → Personal → Instructions → Not → How it works → Remix → Mistakes. The new order builds understanding progressively.

---

## Slides to Cut

| Slide                                   | Reason                                                                                  |
| --------------------------------------- | --------------------------------------------------------------------------------------- |
| **OpenClaw** (s08)                      | Tangent. Confused Chiara. Not relevant to the learning arc. Save time for better stuff. |
| **What Goes in the Instructions** (s13) | Redundant — covered naturally during the build demo.                                    |
| **Skill Starter Kit** (s32)             | Over-explained. Fold into QR code takeaway.                                             |
| **Community Upgrade** (s33)             | Too salesy at the end. If people want more, QR code leads there.                        |

---

## Slides to Move

| Slide                             | From                        | To                                                                                            |
| --------------------------------- | --------------------------- | --------------------------------------------------------------------------------------------- |
| **The Remix Mindset** (s16)       | After "What Skills Are Not" | After 3rd live demo (ad creative refresher) — natural transition since that skill WAS a remix |
| **Common Skill Mistakes** (s17)   | End of section 2            | Before "What Skills Are NOT"                                                                  |
| **What Makes a Good Skill** (s25) | Section 4 (Building)        | Keep in Section 4 but before "Let's Build It"                                                 |

---

## Delivery Notes

### Pacing

- **Ecosystem section took too long.** Should be ~3–5 min max. Quick context, not a deep dive.
- **Timeline slide** — don't read each item. Just say "18 months ago none of this existed" and click through fast.
- **"This Spread Fast" slide** — condense to: "Started at Anthropic, now it's an open standard. Works across all these tools. What you learn today is portable."

### Presentation style

- **Stop reading slides verbatim.** Chiara flagged this multiple times. The slides where Jackson went off-script and explained naturally were the strongest moments.
- **Personal stories are the hook.** Each demo needs a "why I built this" story:
  - Demo 1 (Search Campaign): "I run Google Ads at my day job. I was rebuilding campaigns every week..."
  - Demo 2 (HTML Email): "I have a side business but no time. This skill keeps my emails on-brand without me touching them..."
  - Demo 3 (Ad Refresher): "My coworkers run static ads and constantly need fresh variations of winners..."
- **Do demos live, not pre-recorded.** Chiara was more engaged during live building than slide-reading.

### Building a Skill (live demo)

- **Don't use the Vibe Skill Creator.** It confused Chiara — she thought you needed to download a special file to build skills.
- **Use the default Claude Skill Creator** that's already in Claude Desktop under Settings > Capabilities > Example Skills.
- **Show the path:** Open Claude Desktop → Settings → Capabilities → Skill Creator → "Try in chat" → type a request from the audience.
- **Get audience input.** "What's something you do repeatedly? Turtles? Let's build a turtle skill." Interactive moment.
- **Key message:** Building a skill is as simple as opening Claude and describing what you want. No file downloads, no code.

### Remix

- Best placed after Demo 3 (ad creative refresher) because that skill IS a remix of OpenAI's image-gen skill.
- Show the GitHub source → explain "I wrote 3 sentences and Claude rebuilt the whole thing."
- Keep it brief. The concept clicks once they've seen the build + demos.

---

## Slide-Level Tweaks

### s01 — Title

- Change `~90 MIN` to `~60 MIN` (actual target runtime after cuts)

### s05 — Three Tools, Three Jobs

- Reframe: "AI now has three types of tools. Today we're focusing on skills — the playbook. MCP is wiring, sub-agents are the team, but skills are where you start."
- Don't dwell on MCP/sub-agents. Quick metaphors, move on.

### s06 — Timeline

- Speed run. "None of this existed 18 months ago. Skills launched October, open standard by December. That's how fast this moves."

### s07 — This Spread Fast

- Cut the verbal walkthrough of every tool. Just: "Skills started in Claude, now they work across all of these. Portable."

### s12 — Best Skills Are Personal

- Chiara's favorite slide. Lean into this. "The most useful skills aren't templates — they're YOUR playbook."

### s22 — Ad Creative Refresher (Demo 3)

- Do this live. Show the original ad, run the skill in Claude Code, wait for API call, show the variants.
- Explain the "why" better: "You found a winning ad. You want subtle variations to keep testing without starting from scratch."

### s26 — Let's Build It

- Remove the "INSTALL VIBE SKILL CREATOR" button. Replace with simple steps: "Open Claude → Settings → Capabilities → Skill Creator"
- The `.skill` file download was the #1 source of confusion.

### s34 — One Takeaway

- Strong as-is. Chiara liked the simplicity.

### s35 — Thanks / CTA

- Cut the starter kit pitch. Just: QR code + "Scan for free skills and resources" + "Now go build something."
- Keep it mysterious. "You want to find out more? Go check it out." Forces engagement.

---

## Structural Insight

Chiara's core feedback: **"I would have liked to see you build one before showing me what skills can do."**

The current deck teaches theory → shows results → then builds. The audience needs: theory → build one together → THEN show advanced examples. Building first makes the demos land harder because the audience now understands the mechanics.

---

## Action Items

- [ ] Reorder slides per revised section order above
- [ ] Cut s08 (OpenClaw), s13 (Instructions), s32 (Starter Kit), s33 (Community)
- [ ] Move Remix slide to after Demo 3
- [ ] Rewrite s26 (Build) to reference Claude's built-in Skill Creator, not the .skill download
- [ ] Add personal story context to each demo slide
- [ ] Update slide index numbers after reorder
- [ ] Update nav dot section indices in JS after reorder
- [ ] Run through revised deck at target ~60 min
