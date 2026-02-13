# Homepage Revised Copy Integration Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Integrate the copy from `channel47-revised-copy.md` into the existing homepage funnel (`site/src/pages/index.astro`) while keeping the current UI system. Add a hero CTA that scrolls to the signup section (Option A), plus small UI/UX upgrades for scannability and trust.

**Architecture:** Keep changes localized to `site/src/pages/index.astro` (HTML/CSS only) + update the existing Node smoke test (`site/tests/homepage.test.mjs`) to lock in the new section markers and hero CTA anchor. No new routes, no new components.

**Tech Stack:** Astro 5, plain CSS, Node 20 `node:test`.

---

## Copy-to-Section Mapping (target structure)

Keep the existing section markers so the current funnel and test remain stable:

- `data-section="hero"` → “BUILDING IN PUBLIC” + headline + revised positioning + **CTA button → `#signup`**
- `data-section="mission"` → rename kicker to **WHY THIS EXISTS** + checklist/repetition + proof callout + “this is an agent”
- `data-section="build"` → rename kicker to **WHAT IT ACTUALLY DOES** + loop pill + 3-item “In practice” list + guardrails/control framing
- `data-section="status"` (new) → **WHERE IT STANDS** + “not vaporware / in production / building in public / open source”
- `data-section="signup"` → revised “GET BUILD NOTES” copy + “what you’ll get” bullets + microcopy (“No spam…”)
- `data-section="links"` / `footer` unchanged

---

### Task 1: Extend the homepage smoke test (RED)

**Files:**
- Modify: `site/tests/homepage.test.mjs:1-17`

**Step 1: Update the test to require the new structure**

Edit `site/tests/homepage.test.mjs`:

```js
for (const section of ['hero', 'mission', 'build', 'status', 'signup', 'links', 'footer']) {
  assert.match(source, new RegExp(`data-section="${section}"`));
}

assert.match(source, /href="#signup"/);
assert.match(source, /id="signup"/);
```

**Step 2: Run tests to verify it fails**

Run: `npm test`  
Expected: FAIL (because `status` section + `#signup` anchor don’t exist yet).

---

### Task 2: Update page metadata + hero copy + hero CTA (GREEN)

**Files:**
- Modify: `site/src/pages/index.astro:12-24`

**Step 1: Update `<BaseLayout />` props**

Keep the title close to current, but refresh the description to match revised positioning:

- `title`: keep or slightly tighten (e.g., “Channel47 — open-source Google Ads agent”)
- `description`: align to “media buyer building an open-source AI agent… audits, fixes, pacing, queries…”

**Step 2: Update hero subhead with revised positioning**

Replace the hero paragraph with the revised “media buyer building an open-source AI agent…” framing (keep first-person voice).

**Step 3: Add hero CTA button that scrolls to signup**

Insert directly under the hero subhead:

```astro
<div class="home__hero-cta">
  <a class="home__cta" href="#signup">Get the build notes</a>
  <p class="home__cta-note">
    Working automations, prompt templates, and real results as I ship them. No fluff.
  </p>
</div>
```

**Step 4: Run tests**

Run: `npm test`  
Expected: still FAIL (status section + id still missing until later tasks).

---

### Task 3: Replace “MISSION” with “WHY THIS EXISTS” + add proof callout (GREEN)

**Files:**
- Modify: `site/src/pages/index.astro:28-41`

**Step 1: Update section kicker**

Change `MISSION` → `WHY THIS EXISTS`.

**Step 2: Restructure for scannability**

In `.home__prose`, use:

- Paragraph: “I manage 25+ accounts…” + “same checklist on repeat”
- Short checklist as a bulleted list (instead of one dense sentence)
- Proof as a callout block for the “~$3K/month” + “4 days early” anecdotes
- Close with: “These aren’t one-off scripts. This is an agent.”

**Step 3: Run tests**

Run: `npm test`  
Expected: still FAIL (status section + signup id not yet done).

---

### Task 4: Replace “WHAT I’M BUILDING” with “WHAT IT ACTUALLY DOES” + 3-item feature list (GREEN)

**Files:**
- Modify: `site/src/pages/index.astro:43-57`

**Step 1: Update section kicker**

Change `WHAT I’M BUILDING` → `WHAT IT ACTUALLY DOES`.

**Step 2: Keep the loop pill, update the copy around it**

Keep:

- `Loop: audit → decide → execute → report`

Update paragraphs:

- Guardrails + “approve changes instead of living in the UI”
- “In practice, that means:” followed by 3 items:
  - expensive miss (broad match, garbage queries, pacing drift)
  - Monday work (STRs, negatives, extensions, RSAs)
  - explains itself (reasoning + approve/override)

Implement the 3 items as a simple list with bold “lead sentences” for fast scanning.

**Step 3: Run tests**

Run: `npm test`  
Expected: still FAIL until status + signup id exist.

---

### Task 5: Add “WHERE IT STANDS” section (new `data-section="status"`) (GREEN)

**Files:**
- Modify: `site/src/pages/index.astro:58-71` (insert between build + signup)

**Step 1: Insert a new section**

Add:

- `class="home__section"`
- `data-section="status"`
- `data-animate="fade-up"`
- Update `data-stagger` values to keep them sequential (recommended).

Copy should cover:

- “This isn’t vaporware”
- foundation plugin runs in production
- building in public (GitHub/Substack)
- ships open-source / no lock-in

**Step 2: Run tests**

Run: `npm test`  
Expected: still FAIL until signup id exists (hero CTA expects it).

---

### Task 6: Update signup section copy + add `id="signup"` + microcopy (GREEN)

**Files:**
- Modify: `site/src/pages/index.astro:59-70` (existing signup section)

**Step 1: Add the anchor target**

Add `id="signup"` to the signup `<section … data-section="signup" …>`.

**Step 2: Update copy to revised “GET BUILD NOTES” block**

Update the body text to:

- “Short emails when something real ships…”
- “You’ll get the working pieces… prompt templates, automation scripts, architecture decisions…”
- Optional final line: “No spam. Unsubscribe anytime.”

Optional but recommended: add a tiny “You’ll get:” bullet list above the form for quick scanning.

**Step 3: Run tests**

Run: `npm test`  
Expected: PASS.

---

### Task 7: Add minimal CSS for CTA + lists + callout (GREEN)

**Files:**
- Modify: `site/src/pages/index.astro:89-243`

**Step 1: Add styles (use existing tokens/patterns)**

Add styles for:

- `.home__hero-cta` (stack on mobile, row on larger screens)
- `.home__cta` (button-like anchor using `--color-accent`)
- `.home__cta-note` (quiet serif support line)
- `.home__list` / `.home__feature-list` (list spacing + type)
- `.home__callout` (border + elevated background, similar to `.home__loop`)
- `.home__microcopy` (small, subtle line under signup)

Keep all typography consistent with the page: mono for UI labels, serif for prose.

**Step 2: Build**

Run: `npm run build`  
Expected: exit 0.

---

### Task 8: Visual verification (manual)

**Step 1: Run dev server**

Run: `npm run dev`

**Step 2: Check UX details**

- Hero CTA scrolls to signup and feels “intentional” (not jarring).
- Mobile (375px): CTA stacks nicely, lists don’t overflow, callout doesn’t feel loud.
- Desktop (1280px): CTA row aligns cleanly; section rhythm stays airy.
- Keyboard: hero CTA + all links have visible focus; form usable end-to-end.
- Reduced motion: animations don’t hide content (global observer already handles this).

---

## Optional UX Enhancements (only if wanted)

1) **EmailSignup accessible feedback** (`site/src/components/EmailSignup.astro`):
   - Add a visually-hidden status line with `aria-live="polite"` that mirrors success/error states.

2) **Section heading semantics** (`site/src/pages/index.astro`):
   - Change kickers to headings (e.g., `h2`) while keeping the same visual styling.

