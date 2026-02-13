# Channel47 Homepage Redesign - Design Document

**Date:** 2026-02-05  
**Status:** Approved (ready for implementation)  
**Author:** Jackson + Codex

---

## Overview

Redesign `channel47.dev` to be a single-page, audience-first funnel that communicates the builder mission clearly, earns trust through specificity, and captures emails without feeling like a SaaS landing page.

**Mission statement (truthful + audience-oriented):** Build an autonomous AI agent that can manage Google Ads accounts as well as a senior media buyer, then open-source the whole thing so any media buyer can run it themselves.

The site is not the product. It’s the signpost + build log.

---

## Requirements (from `channel47-site-brief.md`)

- **Single page** at `/` with no nav clutter
- **Primary CTA:** email capture (one field, one button)
- **Links row:** X, Substack, GitHub, LinkedIn (optional but included)
- **Design:** dark palette, single-column, utilitarian/editorial, minimal motion
- **No stock / no AI hero art**

---

## Vibe / Direction

**“Monospace utilitarian with editorial warmth.”**

Technical bones:
- Monospace headings / labels
- Dark palette, terminal-adjacent spacing
- Simple components, hairline rules

Warmth:
- Personal first-person voice
- Serif body copy for reading comfort
- Subtle texture (paper grain) + vignette

Rawness is intentional, not sloppy.

---

## IA (Information Architecture)

Tight funnel, one column:

1. **Overline**: “BUILDING IN PUBLIC”
2. **Hero**: H1 + subhead (the whole thesis in 2 lines)
3. **Mission**: who I am + why this exists (short, specific, first person)
4. **What I’m building**: the loop + guardrails (concrete, non-salesy)
5. **Email capture**: “Get build notes” + one sentence promise
6. **Links row**: X / Substack / GitHub / LinkedIn
7. **Footer**: minimal attribution + year

---

## Copy (v1, approved)

**Overline**  
BUILDING IN PUBLIC

**H1**  
Stop clicking. Start supervising.

**Subhead**  
I’m building an autonomous AI agent that can manage Google Ads like a senior media buyer—then I’ll open‑source it so any media buyer can run it themselves.

**Mission (who I am + why)**  
I’m Jackson. I oversee 25+ accounts across multiple MCCs.  
Most of the job isn’t “strategy.” It’s repetition: audits, fixes, pacing, extensions, queries, copy… and the same mistakes showing up again next week.  
I started with a Claude Code plugin to automate pieces of that. It worked—but it was too narrow. The real goal is the agent.

**What I’m building**  
A system that can run the loop: **audit → decide → execute → report**.  
It should catch the boring misses (and the expensive ones), explain what it’s doing in plain English, and operate with guardrails—so you can approve changes instead of living in the UI.  
I’m building it on top of the skills and connectors I’ve already made, and pushing toward real autonomy step by step.

**Email CTA**  
Get build notes.  
Short emails when something real ships: progress, failures, releases, and runnable steps.

**Links**  
X: https://x.com/ctrlswing  
Substack: https://substack.com/@ctrlswing  
GitHub: https://github.com/ctrlswing  
LinkedIn: https://www.linkedin.com/in/jackson-d-9979a7a0/

---

## Visual System

### Typography

- **Headings / labels:** Geist Mono (monospace, utilitarian)
- **Body:** Lora (serif, editorial warmth)

### Layout

- Single column, max width ~680–720px
- Generous vertical rhythm, “terminal margins”
- No nav; top area uses overline + hero only

### Color

- Keep existing warm-dark palette tokens
- One accent (terracotta/rust) for links + focus + CTA

---

## Subtle Touches (Package A: Editorial Warmth)

- **Paper grain** noise overlay (low opacity, fixed, pointer-events none)
- **Soft vignette** to focus the column
- **Minimal reveal motion:** `fade-up` on section entry, runs once, respects `prefers-reduced-motion`
- **Micro interactions:** hover underline for links, 1–2px lift for CTA, quiet focus rings

---

## Out of Scope (for this pass)

- `/skills` page (can be added after homepage ships)
- Long-form narrative sections, terminal demo, canvas animations
- Renaming/branding the agent (no working title on homepage yet)

