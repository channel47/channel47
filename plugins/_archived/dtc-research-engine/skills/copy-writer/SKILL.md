---
name: copy-writer
description: This skill should be used when the user asks to "write ad copy", "write headlines", "write hooks", "Facebook ad copy", "Google ad copy", "primary text", "ad creative copy", "write body copy", "DTC copy", "direct response copy", "landing page copy", "email copy", "write ads for", or mentions writing, creating, or generating text-based advertising copy for DTC products. Trigger after research, personas, and angles are available, or when the user provides an angle and wants it turned into copy.
---

# Copy Writer — Direct Response Ad Copy

This skill generates platform-specific ad copy (headlines, primary text, hooks, descriptions) for DTC products. Every piece of copy is rooted in real customer data, specific angles, and targeted at defined personas.

## Copy Types This Skill Handles

1. **Meta Ad Copy** — Primary text, headlines, descriptions for Facebook/Instagram
2. **Google Search Ads** — Headlines, descriptions, sitelinks, callouts
3. **Google Display/YouTube** — Headlines, descriptions for display and video campaigns
4. **TikTok Ad Copy** — Captions, text overlays, CTA text
5. **Email Subject Lines & Preview Text** — For DTC email marketing
6. **Landing Page Headlines** — Hero headlines, subheadlines, section headers

## Copy Generation Process

### Step 1: Gather Inputs

Read from workspace:
- Research file (`*-research.md`) — customer language
- Personas file (`*-personas.md`) — targeting
- Angles file (`*-angles.md`) — strategic direction

Ask the user (if not specified):
- Which platforms to write for
- Offer specifics (price, discount, guarantee, free shipping, etc.)
- Any compliance restrictions (no health claims, etc.)
- Brand voice (casual/professional/edgy/warm)
- Landing page URL

### Step 2: Write Platform-Specific Copy

#### Meta (Facebook / Instagram) Ad Copy

Write 3-5 variations per angle, varying hook type and length:

**Short-form (under 125 characters):**
```
[Hook — one punchy line that stops the scroll]
[Benefit — what they get]
[CTA — what to do]
```

**Medium-form (125-500 characters):**
```
[Hook — pattern interrupt or pain call-out]

[Problem agitation — 1-2 sentences]

[Solution bridge — introduce the product]

[Proof — one specific result or stat]

[CTA with offer]
```

**Long-form (500+ characters):**
```
[Hook — strong opening line]

[Story or problem expansion — 2-3 sentences that make them feel seen]

[Failed solutions acknowledgment]

[Product introduction with mechanism]

[Proof stack — 2-3 testimonial snippets or data points]

[Offer details]

[CTA with urgency/risk reversal]
```

**Headlines** (40 char max for display):
- Write 5-10 headline variations
- Mix benefit-driven, curiosity-driven, and social-proof headlines
- Include the product name in at least 2

**Descriptions** (30 char recommended):
- Write 3-5 descriptions
- Focus on offer elements (free shipping, guarantee, discount)

#### Google Search Ads

Write for responsive search ad format:

**Headlines** (30 char max each, need 15):
- 3-4 brand/product headlines
- 3-4 benefit headlines
- 3-4 action/CTA headlines
- 2-3 social proof headlines
- 1-2 offer/price headlines

**Descriptions** (90 char max each, need 4):
- 1 problem-solution description
- 1 benefit-focused description
- 1 proof/credibility description
- 1 offer/CTA description

Pin recommendations:
- Pin brand headline to position 1
- Pin CTA headline to position 2 or 3

#### Google Display / YouTube

**Headlines** (30 char max):
- 5 short headlines focused on benefit or curiosity

**Long Headlines** (90 char max):
- 3 expanded headlines with more context

**Descriptions** (90 char max):
- 3 descriptions mixing benefits, proof, and CTA

#### TikTok

**Captions** (write 3-5 variations):
- Keep under 150 characters for visibility
- Include relevant hashtags
- Use casual, native language
- Include a hook and CTA

**Text Overlay Copy**:
- Opening text overlay (the hook — 5-8 words max)
- Key benefit text (mid-video — 5-8 words)
- CTA text (end — with urgency)

#### Email Subject Lines

Write 10 subject line variations across these styles:
- Curiosity gap
- Benefit-driven
- Pain call-out
- Social proof
- Urgency/scarcity
- Question format
- Story teaser

Include preview text for each (40-90 characters).

#### Landing Page Headlines

**Hero headline options** (3-5):
- Lead with the biggest benefit or the sharpest pain point
- 8-12 words max
- Must make sense without any other context

**Subheadline options** (3-5):
- Expand on the hero headline
- Add proof element or mechanism
- 15-25 words

### Step 3: Apply Copy Principles

Every piece of copy should embody these DTC direct response principles:

**Specificity beats generality**
- "Eliminates odor in 30 seconds" beats "Powerful odor elimination"
- "147,000 happy customers" beats "Thousands of satisfied customers"

**Customer language beats marketer language**
- Use exact phrases from the research data
- If customers say "game changer," use "game changer"
- If customers say "I was skeptical but..." use that framing

**One idea per ad**
- Each piece of copy should hammer one angle, one benefit, one emotion
- Don't try to say everything — say one thing powerfully

**The hook does the heavy lifting**
- 80% of the ad's effectiveness is in the first line
- Write 3x more hook variations than body copy variations

**Proof is persuasion**
- Every claim should have a proof element nearby
- Testimonial snippets, statistics, authority mentions
- "As seen on", "Doctor recommended", "100,000+ sold"

### Step 4: Organize and Label

Structure the output clearly:

```markdown
# Ad Copy for [Product]

## Angle: [Angle Name]
### Meta — Primary Text
#### Variation 1 (Short)
#### Variation 2 (Medium)
#### Variation 3 (Long)
### Meta — Headlines
### Meta — Descriptions
### Google Search — Headlines
### Google Search — Descriptions
### TikTok — Captions
### Email — Subject Lines
```

### Step 5: Save Output

Save to the workspace as `[product-slug]-copy.md`.

## Quality Standards

- Every piece of copy must connect to a specific angle and persona
- Customer language from research must appear naturally (not forced)
- Respect platform character limits — exceeding them wastes everyone's time
- Write enough variations to enable testing — minimum 3 per format per angle
- Include at least one "ugly" or unconventional variation — sometimes the weird one wins
- No cliches without self-awareness ("Are you tired of..." is banned unless you're subverting it)

## Additional Resources

### Reference Files
- **`references/platform-specs.md`** — Character limits, format specs, and best practices for every ad platform
- **`references/copy-formulas.md`** — Proven DTC copy formulas and frameworks with examples
