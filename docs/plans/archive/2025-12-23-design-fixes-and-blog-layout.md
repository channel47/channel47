# Design Fixes and Blog Layout Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Fix theme toggle functionality, improve typography weight contrast, and implement editorial blog index layout.

**Architecture:** Three independent fixes: (1) Simplify dark mode CSS selectors for proper theme switching, (2) Update typography weight mixing to avoid mid-word splits and increase logo contrast, (3) Create feature + archive hybrid blog index following editorial style guide.

**Tech Stack:** Astro, CSS custom properties, vanilla JavaScript

---

## Task 1: Fix Dark Mode Theme Toggle

**Files:**
- Modify: `src/styles/global.css:87-107`

**Step 1: Replace dark mode CSS selector**

In `src/styles/global.css`, replace lines 87-107:

Old:
```css
/* Dark Mode */
[data-theme="dark"],
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    /* Adjusted grays for dark mode */
    --color-gray-100: #1a1a1a;
    --color-gray-200: #303030;
    --color-gray-300: #404040;
    --color-gray-400: #606060;
    --color-gray-500: #909090;
    --color-gray-600: #c0c0c0;
    --color-gray-700: #e0e0e0;
    --color-gray-800: #f0f0f0;

    /* Semantic tokens - Dark Mode */
    --color-bg: var(--color-black);
    --color-text: var(--color-white);
    --color-text-muted: var(--color-gray-500);
    --color-border: var(--color-gray-200);
  }
}
```

New:
```css
/* Dark Mode - Explicit Selection */
[data-theme="dark"] {
  /* Adjusted grays for dark mode */
  --color-gray-100: #1a1a1a;
  --color-gray-200: #303030;
  --color-gray-300: #404040;
  --color-gray-400: #606060;
  --color-gray-500: #909090;
  --color-gray-600: #c0c0c0;
  --color-gray-700: #e0e0e0;
  --color-gray-800: #f0f0f0;

  /* Semantic tokens - Dark Mode */
  --color-bg: var(--color-black);
  --color-text: var(--color-white);
  --color-text-muted: var(--color-gray-500);
  --color-border: var(--color-gray-200);
}

/* Dark Mode - System Preference (only when no explicit theme set) */
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]):not([data-theme="dark"]) {
    /* Adjusted grays for dark mode */
    --color-gray-100: #1a1a1a;
    --color-gray-200: #303030;
    --color-gray-300: #404040;
    --color-gray-400: #606060;
    --color-gray-500: #909090;
    --color-gray-600: #c0c0c0;
    --color-gray-700: #e0e0e0;
    --color-gray-800: #f0f0f0;

    /* Semantic tokens - Dark Mode */
    --color-bg: var(--color-black);
    --color-text: var(--color-white);
    --color-text-muted: var(--color-gray-500);
    --color-border: var(--color-gray-200);
  }
}
```

**Step 2: Test theme toggle in browser**

Run: `npm run dev`
Open: http://localhost:4321
Test: Click "Light" / "Dark" / "Auto" buttons in footer
Expected: Colors change immediately when selecting theme

**Step 3: Test persistence**

Test: Select "Dark", refresh page
Expected: Page loads in dark mode, "Dark" button shows active

**Step 4: Commit**

```bash
git add src/styles/global.css
git commit -m "fix: theme toggle now properly applies dark mode colors"
```

---

## Task 2: Increase Logo Weight Contrast

**Files:**
- Modify: `src/styles/components/header.css:30-36`

**Step 1: Update logo font weights**

In `src/styles/components/header.css`, replace lines 30-36:

Old:
```css
.header__wordmark-light {
  font-weight: 400;
}

.header__wordmark-bold {
  font-weight: 700;
}
```

New:
```css
.header__wordmark-light {
  font-weight: 200;
}

.header__wordmark-bold {
  font-weight: 800;
}
```

**Step 2: Test logo in browser**

Run: `npm run dev`
Expected: "Channel" appears much lighter (200), "47" appears bolder (800)

**Step 3: Commit**

```bash
git add src/styles/components/header.css
git commit -m "feat: increase logo weight contrast (200/800)"
```

---

## Task 3: Fix Plugin Name Weight Mixing

**Files:**
- Modify: `src/pages/plugins/index.astro:40-52`

**Step 1: Simplify splitName function**

In `src/pages/plugins/index.astro`, replace lines 40-52:

Old:
```javascript
// Split plugin names for weight mixing
function splitName(name: string): { first: string; second: string } {
  const words = name.split(' ');
  if (words.length === 1) {
    const mid = Math.ceil(name.length / 2);
    return { first: name.slice(0, mid), second: name.slice(mid) };
  }
  const midIndex = Math.ceil(words.length / 2);
  return {
    first: words.slice(0, midIndex).join(' '),
    second: words.slice(midIndex).join(' ')
  };
}
```

New:
```javascript
// Split plugin names for weight mixing - first word bold, rest regular
function splitName(name: string): { first: string; second: string } {
  const words = name.split(' ');
  if (words.length === 1) {
    return { first: name, second: '' };
  }
  return {
    first: words[0],
    second: words.slice(1).join(' ')
  };
}
```

**Step 2: Update font weights in template**

In `src/pages/plugins/index.astro`, replace lines 97-100:

Old:
```astro
<h2 class="plugin-spread__name">
  <span style="font-weight: 700;">{nameParts.first}</span>
  {nameParts.second && (
    <span style="font-weight: 400;"> {nameParts.second}</span>
```

New:
```astro
<h2 class="plugin-spread__name">
  <span style="font-weight: 800;">{nameParts.first}</span>
  {nameParts.second && (
    <span style="font-weight: 400;"> {nameParts.second}</span>
```

**Step 3: Test plugin names**

Run: `npm run dev`
Open: http://localhost:4321/plugins
Expected: First word of each plugin name is bold (800), rest is regular (400), no mid-word splits

**Step 4: Commit**

```bash
git add src/pages/plugins/index.astro
git commit -m "fix: plugin name weight mixing - first word only, no mid-word splits"
```

---

## Task 4: Create Blog Styles

**Files:**
- Create: `src/styles/components/blog-index.css`

**Step 1: Create blog index component styles**

Create `src/styles/components/blog-index.css`:

```css
/* Blog Index Component */
.blog-index {
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 var(--space-7);
}

/* Featured Section - Latest Post */
.blog-featured {
  padding: var(--space-10) 0;
  max-width: 65ch;
}

.blog-featured__date {
  font-size: var(--text-xs);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--color-text-muted);
  margin-bottom: var(--space-4);
}

.blog-featured__title {
  font-size: var(--text-4xl);
  line-height: var(--leading-tight);
  letter-spacing: -0.02em;
  margin-bottom: var(--space-5);
  color: var(--color-text);
  transition: color 200ms ease-out;
}

.blog-featured__title:hover {
  color: var(--color-accent);
}

.blog-featured__excerpt {
  font-size: var(--text-lg);
  color: var(--color-text-muted);
  line-height: var(--leading-relaxed);
}

/* Archive Section - Older Posts */
.blog-archive {
  border-top: 1px solid var(--color-border);
  padding-top: var(--space-8);
  padding-bottom: var(--space-10);
}

.blog-archive__title {
  font-size: var(--text-sm);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--color-text-muted);
  margin-bottom: var(--space-7);
}

.blog-archive__list {
  display: flex;
  flex-direction: column;
  gap: 0;
}

.blog-archive__item {
  border-top: 1px solid var(--color-border);
  padding: var(--space-7) 0;
}

.blog-archive__item:first-child {
  border-top: none;
}

.blog-archive__item-date {
  font-size: var(--text-xs);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--color-text-muted);
  margin-bottom: var(--space-3);
}

.blog-archive__item-title {
  font-size: var(--text-xl);
  line-height: var(--leading-tight);
  color: var(--color-text);
  margin-bottom: var(--space-3);
  transition: color 200ms ease-out;
}

.blog-archive__item:hover .blog-archive__item-title {
  color: var(--color-accent);
}

.blog-archive__item-description {
  font-size: var(--text-base);
  color: var(--color-text-muted);
  line-height: var(--leading-relaxed);
  max-width: 65ch;
}

/* Responsive */
@media (max-width: 768px) {
  .blog-index {
    padding: 0 var(--space-6);
  }

  .blog-featured {
    padding: var(--space-8) 0;
  }

  .blog-featured__title {
    font-size: var(--text-3xl);
  }

  .blog-archive__item {
    padding: var(--space-6) 0;
  }

  .blog-archive__item-title {
    font-size: var(--text-lg);
  }
}
```

**Step 2: Verify file created**

Run: `cat src/styles/components/blog-index.css | wc -l`
Expected: File exists with content

**Step 3: Commit**

```bash
git add src/styles/components/blog-index.css
git commit -m "feat: create blog index component styles"
```

---

## Task 5: Rebuild Blog Index Page

**Files:**
- Modify: `src/pages/blog/index.astro`

**Step 1: Replace blog index with new layout**

Replace entire contents of `src/pages/blog/index.astro`:

```astro
---
// src/pages/blog/index.astro
import { getCollection } from 'astro:content';
import BaseLayout from '../../layouts/BaseLayout.astro';
import '../../styles/components/blog-index.css';

const posts = await getCollection('blog', ({ data }) => !data.draft);
const sortedPosts = posts.sort((a, b) => b.data.date.valueOf() - a.data.date.valueOf());

// Split into featured (latest) and archive (rest)
const [featuredPost, ...archivePosts] = sortedPosts;

// Weight mixing helper - first word bold, rest regular
function splitTitle(title: string): { first: string; second: string } {
  const words = title.split(' ');
  if (words.length === 1) {
    return { first: title, second: '' };
  }
  return {
    first: words[0],
    second: words.slice(1).join(' ')
  };
}

// Format date
function formatDate(date: Date): string {
  return date.toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  });
}
---

<BaseLayout
  title="Blog"
  description="Insights and tutorials from building with Claude Code."
>
  <div class="blog-index">
    {featuredPost && (
      <section class="blog-featured">
        <a href={`/blog/${featuredPost.slug}`}>
          <time class="blog-featured__date">
            {formatDate(featuredPost.data.date)}
          </time>
          <h1 class="blog-featured__title">
            {(() => {
              const titleParts = splitTitle(featuredPost.data.title);
              return (
                <>
                  <span style="font-weight: 800;">{titleParts.first}</span>
                  {titleParts.second && (
                    <span style="font-weight: 400;"> {titleParts.second}</span>
                  )}
                </>
              );
            })()}
          </h1>
          <p class="blog-featured__excerpt">
            {featuredPost.data.description}
          </p>
        </a>
      </section>
    )}

    {archivePosts.length > 0 && (
      <section class="blog-archive">
        <h2 class="blog-archive__title">Archive</h2>
        <div class="blog-archive__list">
          {archivePosts.map((post) => (
            <article class="blog-archive__item">
              <a href={`/blog/${post.slug}`}>
                <time class="blog-archive__item-date">
                  {formatDate(post.data.date)}
                </time>
                <h3 class="blog-archive__item-title">
                  {post.data.title}
                </h3>
                <p class="blog-archive__item-description">
                  {post.data.description}
                </p>
              </a>
            </article>
          ))}
        </div>
      </section>
    )}

    {sortedPosts.length === 0 && (
      <section class="blog-featured">
        <p style="color: var(--color-text-muted);">
          Posts coming soon. Check back later.
        </p>
      </section>
    )}
  </div>
</BaseLayout>
```

**Step 2: Test blog index in browser**

Run: `npm run dev`
Open: http://localhost:4321/blog
Expected: Featured post (if exists) displays large, archive posts display below with clean list treatment

**Step 3: Test responsive**

Resize browser to mobile width
Expected: Typography scales down but maintains hierarchy

**Step 4: Commit**

```bash
git add src/pages/blog/index.astro
git commit -m "feat: rebuild blog index with feature + archive hybrid layout"
```

---

## Task 6: Final Verification

**Files:**
- None (testing only)

**Step 1: Test all fixes together**

Run: `npm run dev`
Test each fix:
1. Toggle theme (Light/Dark/Auto) - colors should change immediately
2. Check logo weight contrast (Channel: 200, 47: 800)
3. Check plugin names (first word bold, no mid-word splits)
4. Check blog layout (featured + archive sections)

**Step 2: Test in both themes**

Switch to Dark mode, verify:
- All pages render correctly
- Blog layout maintains readability
- Logo contrast works in dark mode

**Step 3: Test production build**

Run: `npm run build`
Expected: Build succeeds without errors

**Step 4: Final commit if any adjustments needed**

```bash
git add .
git commit -m "chore: final verification and adjustments"
```

---

## Success Criteria Checklist

- [ ] Theme toggle changes colors immediately (no refresh needed)
- [ ] Theme persists across page navigation
- [ ] Logo shows high weight contrast (200/800)
- [ ] Plugin names split only on word boundaries
- [ ] No mid-word splits like "googl e-ads"
- [ ] Blog index shows featured post with display typography
- [ ] Blog archive section displays older posts cleanly
- [ ] All changes work in both light and dark mode
- [ ] Responsive design works on mobile/tablet/desktop
- [ ] Production build succeeds

---

## Notes for Executor

- Each task is independent and takes 2-5 minutes
- Test visually in browser after each change
- Commit frequently with descriptive messages
- The design follows the "refined but strange" style guide
- Weight mixing is intentional: logo (200/800), content (800/400)
- Blog layout emphasizes latest post, practical archive below

---

*Implementation plan complete. Ready for execution.*
