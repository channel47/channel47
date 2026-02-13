# Homepage Redesign Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Replace the current long-form homepage with a tight, audience-first funnel matching `channel47-site-brief.md`, including updated copy, links, subtle texture, and minimal reveal motion.

**Architecture:** Keep the Astro site structure; redesign is mostly `index.astro` + shared component styling. Add a small Node smoke test to lock the funnel sections + link destinations.

**Tech Stack:** Astro 5, plain CSS, Node 20 `node:test`, Kit subscribe endpoint.

---

### Task 1: Add a failing homepage smoke test (RED)

**Files:**
- Create: `site/tests/homepage.test.mjs`
- Modify: `site/package.json`
- Modify: `package.json`

**Step 1: Write the failing test**

Create `site/tests/homepage.test.mjs`:

```js
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { dirname, resolve } from 'node:path';

test('homepage has tight-funnel sections', async () => {
  const __dirname = dirname(fileURLToPath(import.meta.url));
  const indexPath = resolve(__dirname, '../src/pages/index.astro');
  const source = await readFile(indexPath, 'utf8');

  for (const section of ['hero', 'mission', 'build', 'signup', 'links', 'footer']) {
    assert.match(source, new RegExp(`data-section=\\"${section}\\"`));
  }
});
```

**Step 2: Add test scripts**

- Add `test` script to `site/package.json`: `node --test`
- Add `test` script to root `package.json`: `npm run test --workspace=site`

**Step 3: Run tests to verify it fails**

Run: `npm test`  
Expected: FAIL because current `index.astro` doesn’t include `data-section="..."`.

---

### Task 2: Rebuild `index.astro` as a new tight funnel (GREEN)

**Files:**
- Modify: `site/src/pages/index.astro`

**Step 1: Implement the new homepage structure**

- Replace the current homepage with a single-column layout.
- Add stable section markers:
  - `data-section="hero"`
  - `data-section="mission"`
  - `data-section="build"`
  - `data-section="signup"`
  - `data-section="links"`
  - `data-section="footer"`

**Step 2: Add the approved copy**

Use the copy from: `docs/plans/2026-02-05-homepage-redesign-design.md`.

**Step 3: Run tests to verify they pass**

Run: `npm test`  
Expected: PASS.

---

### Task 3: Update shared components to match the new aesthetic

**Files:**
- Modify: `site/src/components/EmailSignup.astro`
- Modify: `site/src/components/SocialLinks.astro`

**Step 1: Email signup**

- Allow customizing button label (prop) for homepage usage.
- Adjust layout to be stacked on mobile and inline on desktop.
- Keep the `/api/subscribe` POST behavior unchanged.

**Step 2: Social links**

- Update link set to: X, Substack, GitHub, LinkedIn.
- Style as quiet monospace utilities (text, not loud icons).

**Step 3: Verify**

Run: `npm run build`  
Expected: exit 0.

---

### Task 4: Global polish (texture + vignette + typography defaults)

**Files:**
- Modify: `site/src/styles/global.css`
- (Optional) Modify: `site/src/styles/design-tokens.css`

**Step 1: Typography**

- Default headings to monospace.
- Keep body copy serif.

**Step 2: Texture**

- Ensure noise overlay is present but subtle.
- Add a vignette layer to focus the reading column.

**Step 3: Motion**

- Use the existing `[data-animate="fade-up"]` system.
- Confirm reduced motion renders everything immediately.

**Step 4: Verify**

Run: `npm test` and `npm run build`  
Expected: both succeed.

