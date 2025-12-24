# Editorial Pages Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Rebuild individual blog post and plugin pages with full magazine feature treatment - display typography, generous whitespace, editorial blocks, and 65ch reading width.

**Architecture:** Create new CSS component files for blog and plugin editorial styles. Rebuild BlogPost.astro layout and plugins/[...slug].astro page with hero treatment, editorial blocks, and consistent vertical rhythm. Simplify ToolsMentioned component to list format.

**Tech Stack:** Astro, CSS custom properties, TypeScript

---

## Task 1: Create Blog Post Styles

**Files:**
- Create: `src/styles/components/blog-post.css`

**Step 1: Create blog post component styles**

Create `src/styles/components/blog-post.css` with the following content:

```css
/* Blog Post Editorial Layout */

.editorial-article {
  max-width: 65ch;
  margin: 0 auto;
  padding: 0 var(--space-7);
}

/* Hero Area */
.article-hero {
  padding-top: var(--space-10);
  padding-bottom: var(--space-9);
  border-bottom: 1px solid var(--color-border);
}

.article-meta {
  display: block;
  font-size: var(--text-xs);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--color-text-muted);
  margin-bottom: var(--space-4);
}

.article-title {
  font-size: var(--text-5xl);
  font-weight: 800;
  line-height: var(--leading-tight);
  letter-spacing: -0.02em;
  color: var(--color-text);
  margin-bottom: var(--space-5);
}

.article-lead {
  font-size: var(--text-xl);
  font-weight: 400;
  line-height: var(--leading-relaxed);
  color: var(--color-text-muted);
}

/* Content Area */
.article-content {
  padding-top: var(--space-9);
  padding-bottom: var(--space-9);
}

/* Section Spacing */
.article-section {
  margin-top: var(--space-9);
  margin-bottom: var(--space-9);
}

.section-header {
  font-size: var(--text-sm);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  font-weight: 600;
  color: var(--color-text);
  margin-bottom: var(--space-4);
}

/* Footer */
.article-footer {
  padding-top: var(--space-8);
  padding-bottom: var(--space-10);
  border-top: 1px solid var(--color-border);
}

.article-footer a {
  font-size: var(--text-sm);
  color: var(--color-accent);
  transition: opacity 200ms ease-out;
}

.article-footer a:hover {
  text-decoration: underline;
}

/* Responsive */
@media (max-width: 768px) {
  .editorial-article {
    padding: 0 var(--space-5);
  }

  .article-hero {
    padding-top: var(--space-8);
    padding-bottom: var(--space-7);
  }

  .article-title {
    font-size: var(--text-3xl);
  }

  .article-lead {
    font-size: var(--text-lg);
  }

  .article-content {
    padding-top: var(--space-7);
    padding-bottom: var(--space-7);
  }

  .article-section {
    margin-top: var(--space-7);
    margin-bottom: var(--space-7);
  }

  .article-footer {
    padding-top: var(--space-7);
    padding-bottom: var(--space-8);
  }
}
```

**Step 2: Verify file created**

Run: `cat src/styles/components/blog-post.css | wc -l`
Expected: File exists with ~100+ lines

**Step 3: Commit**

```bash
git add src/styles/components/blog-post.css
git commit -m "feat: create blog post editorial styles"
```

---

## Task 2: Create Plugin Page Styles

**Files:**
- Create: `src/styles/components/plugin-page.css`

**Step 1: Create plugin page component styles**

Create `src/styles/components/plugin-page.css` with the following content:

```css
/* Plugin Page Editorial Layout */

/* Reuse article structure from blog-post.css */
.editorial-article {
  max-width: 65ch;
  margin: 0 auto;
  padding: 0 var(--space-7);
}

.article-hero {
  padding-top: var(--space-10);
  padding-bottom: var(--space-9);
  border-bottom: 1px solid var(--color-border);
}

.article-meta {
  display: block;
  font-size: var(--text-xs);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--color-text-muted);
  margin-bottom: var(--space-4);
}

.article-title {
  font-size: var(--text-5xl);
  font-weight: 800;
  line-height: var(--leading-tight);
  letter-spacing: -0.02em;
  color: var(--color-text);
  margin-bottom: var(--space-5);
}

.article-lead {
  font-size: var(--text-xl);
  font-weight: 400;
  line-height: var(--leading-relaxed);
  color: var(--color-text-muted);
}

.article-content {
  padding-top: var(--space-9);
  padding-bottom: var(--space-9);
}

.article-section {
  margin-top: var(--space-9);
  margin-bottom: var(--space-9);
}

.section-header {
  font-size: var(--text-sm);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  font-weight: 600;
  color: var(--color-text);
  margin-bottom: var(--space-4);
}

.article-footer {
  padding-top: var(--space-8);
  padding-bottom: var(--space-10);
  border-top: 1px solid var(--color-border);
}

.article-footer a {
  font-size: var(--text-sm);
  color: var(--color-accent);
  transition: opacity 200ms ease-out;
}

.article-footer a:hover {
  text-decoration: underline;
}

/* Editorial Block - Installation, etc. */
.editorial-block {
  border: 1px solid var(--color-border);
  padding: var(--space-6);
  margin-top: var(--space-8);
  margin-bottom: var(--space-8);
}

.editorial-block__intro {
  font-size: var(--text-base);
  color: var(--color-text-muted);
  line-height: var(--leading-relaxed);
  margin-bottom: var(--space-4);
}

.editorial-block__code {
  background: var(--color-gray-100);
  border: 1px solid var(--color-border);
  padding: var(--space-5);
  font-family: 'JetBrains Mono', 'Monaco', 'Courier New', monospace;
  font-size: var(--text-sm);
  color: var(--color-text);
  overflow-x: auto;
  white-space: pre-wrap;
  word-wrap: break-word;
}

.editorial-block__meta {
  margin-top: var(--space-4);
  font-size: var(--text-xs);
  color: var(--color-text-muted);
  display: flex;
  gap: var(--space-3);
  align-items: center;
}

/* Collapsible Details (marketplace setup) */
.editorial-block details {
  margin-bottom: var(--space-4);
}

.editorial-block summary {
  font-size: var(--text-sm);
  color: var(--color-accent);
  cursor: pointer;
  transition: opacity 200ms ease-out;
}

.editorial-block summary:hover {
  opacity: 0.7;
}

.editorial-block details > div {
  margin-top: var(--space-3);
  padding: var(--space-4);
  background: var(--color-bg);
  border: 1px solid var(--color-border);
}

/* Related Posts List */
.related-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.related-list__item {
  margin-bottom: var(--space-4);
}

.related-list__item:last-child {
  margin-bottom: 0;
}

.related-list__link {
  color: var(--color-accent);
  transition: opacity 200ms ease-out;
}

.related-list__link:hover {
  text-decoration: underline;
}

.related-list__date {
  font-size: var(--text-sm);
  color: var(--color-text-muted);
  margin-left: var(--space-2);
}

/* Responsive */
@media (max-width: 768px) {
  .editorial-article {
    padding: 0 var(--space-5);
  }

  .article-hero {
    padding-top: var(--space-8);
    padding-bottom: var(--space-7);
  }

  .article-title {
    font-size: var(--text-3xl);
  }

  .article-lead {
    font-size: var(--text-lg);
  }

  .article-content {
    padding-top: var(--space-7);
    padding-bottom: var(--space-7);
  }

  .article-section {
    margin-top: var(--space-7);
    margin-bottom: var(--space-7);
  }

  .editorial-block {
    padding: var(--space-5);
    margin-top: var(--space-7);
    margin-bottom: var(--space-7);
  }

  .article-footer {
    padding-top: var(--space-7);
    padding-bottom: var(--space-8);
  }
}
```

**Step 2: Verify file created**

Run: `cat src/styles/components/plugin-page.css | wc -l`
Expected: File exists with ~180+ lines

**Step 3: Commit**

```bash
git add src/styles/components/plugin-page.css
git commit -m "feat: create plugin page editorial styles"
```

---

## Task 3: Rebuild Blog Post Layout

**Files:**
- Modify: `src/layouts/BlogPost.astro`

**Step 1: Replace BlogPost.astro with editorial layout**

Replace entire contents of `src/layouts/BlogPost.astro`:

```astro
---
// src/layouts/BlogPost.astro
import BaseLayout from './BaseLayout.astro';
import ToolsMentioned from '../components/ToolsMentioned.astro';
import '../styles/components/blog-post.css';

interface Props {
  title: string;
  description: string;
  date: Date;
  tags?: string[];
  toolsUsed?: Array<{
    slug: string;
    source: 'channel47' | 'external';
    installCommand?: string;
  }>;
}

const { title, description, date, tags = [], toolsUsed } = Astro.props;

// Format date for display - uppercase month
const formattedDate = date.toLocaleDateString('en-US', {
  year: 'numeric',
  month: 'long',
  day: 'numeric'
}).toUpperCase();
---

<BaseLayout title={title} description={description}>
  <article class="editorial-article">
    <!-- Hero Area -->
    <div class="article-hero">
      <time class="article-meta" datetime={date.toISOString()}>
        {formattedDate}
      </time>
      <h1 class="article-title">{title}</h1>
      <p class="article-lead">{description}</p>
    </div>

    <!-- Content -->
    <div class="article-content">
      <div class="prose prose-lg max-w-none
        prose-headings:font-semibold prose-headings:text-[var(--color-text)]
        prose-p:text-[var(--color-text)] prose-p:leading-relaxed
        prose-a:text-[var(--color-accent)] prose-a:no-underline hover:prose-a:underline
        prose-code:bg-[var(--color-gray-100)] prose-code:text-[var(--color-text)] prose-code:px-1 prose-code:py-0.5 prose-code:rounded prose-code:text-sm
        prose-pre:bg-[var(--color-gray-100)] prose-pre:text-[var(--color-text)] prose-pre:border prose-pre:border-[var(--color-border)] prose-pre:p-6
        prose-blockquote:border-l-[var(--color-accent)] prose-blockquote:pl-4 prose-blockquote:italic
        prose-strong:text-[var(--color-text)] prose-strong:font-semibold
        prose-ul:text-[var(--color-text)] prose-ol:text-[var(--color-text)]
        prose-li:text-[var(--color-text)]">
        <slot />
      </div>
    </div>

    <!-- Tools Mentioned Section -->
    {toolsUsed && toolsUsed.length > 0 && (
      <section class="article-section">
        <ToolsMentioned tools={toolsUsed} />
      </section>
    )}

    <!-- Footer -->
    <footer class="article-footer">
      <a href="/blog">&larr; Back to blog</a>
    </footer>
  </article>
</BaseLayout>
```

**Step 2: Test blog post in browser**

Run: `npm run dev`
Open: http://localhost:4321/blog/[any-post-slug]
Expected: Large display title (96px desktop), lead paragraph below, generous spacing, 65ch reading width

**Step 3: Test responsive**

Resize browser to mobile width
Expected: Title scales to 48px, lead to 20px, spacing compresses appropriately

**Step 4: Commit**

```bash
git add src/layouts/BlogPost.astro
git commit -m "feat: rebuild blog post layout with editorial treatment"
```

---

## Task 4: Rebuild Plugin Page

**Files:**
- Modify: `src/pages/plugins/[...slug].astro`

**Step 1: Replace plugin page with editorial layout**

Replace entire contents of `src/pages/plugins/[...slug].astro`:

```astro
---
// src/pages/plugins/[...slug].astro
import { getCollection } from 'astro:content';
import BaseLayout from '../../layouts/BaseLayout.astro';
import mergedPlugins from '../../data/merged-plugins.json';
import '../../styles/components/plugin-page.css';

export async function getStaticPaths() {
  const plugins = await getCollection('plugins', ({ data }) => !data.draft);

  return plugins.map(plugin => {
    const marketplaceData = mergedPlugins.find(p => p.name === plugin.slug);

    return {
      params: { slug: plugin.slug },
      props: {
        plugin,
        marketplaceData,
      },
    };
  });
}

const { plugin, marketplaceData } = Astro.props;
const { Content } = await plugin.render();

type RelatedPost = {
  title: string;
  slug: string;
  date: string;
};

const relatedPosts = (marketplaceData?.relatedPosts || []) as RelatedPost[];

// Format metadata
const version = marketplaceData?.version || '1.0.0';
const category = marketplaceData?.category || 'tools';
const name = marketplaceData?.name || plugin.slug;
const description = marketplaceData?.description || '';
---

<BaseLayout title={name} description={description}>
  <article class="editorial-article">
    <!-- Hero Area -->
    <div class="article-hero">
      <div class="article-meta">
        v{version} • {category.toUpperCase()}
      </div>
      <h1 class="article-title">{name}</h1>
      <p class="article-lead">{description}</p>
    </div>

    <!-- Installation Section -->
    <section class="article-section">
      <h2 class="section-header">Installation</h2>
      <div class="editorial-block">
        <details>
          <summary>First time? Add Channel 47 marketplace first</summary>
          <div>
            <p style="font-size: var(--text-sm); color: var(--color-text-muted); margin-bottom: var(--space-3);">
              Step 1: Add marketplace
            </p>
            <code class="editorial-block__code">
              /plugin marketplace add ctrlswing/channel47-marketplace
            </code>
          </div>
        </details>

        <p class="editorial-block__intro">Install plugin:</p>
        <code class="editorial-block__code">
          /plugin install {name}@channel47
        </code>

        <div class="editorial-block__meta">
          <span>v{version}</span>
          <span>•</span>
          <span style="text-transform: capitalize;">{category}</span>
        </div>
      </div>
    </section>

    <!-- Content -->
    <div class="article-content">
      <div class="prose prose-lg max-w-none
        prose-headings:font-semibold prose-headings:text-[var(--color-text)]
        prose-p:text-[var(--color-text)] prose-p:leading-relaxed
        prose-a:text-[var(--color-accent)] prose-a:no-underline hover:prose-a:underline
        prose-code:bg-[var(--color-gray-100)] prose-code:text-[var(--color-text)] prose-code:px-1 prose-code:py-0.5 prose-code:rounded prose-code:text-sm
        prose-pre:bg-[var(--color-gray-100)] prose-pre:text-[var(--color-text)] prose-pre:border prose-pre:border-[var(--color-border)] prose-pre:p-6
        prose-blockquote:border-l-[var(--color-accent)] prose-blockquote:pl-4 prose-blockquote:italic
        prose-strong:text-[var(--color-text)] prose-strong:font-semibold
        prose-ul:text-[var(--color-text)] prose-ol:text-[var(--color-text)]
        prose-li:text-[var(--color-text)]">
        <Content />
      </div>
    </div>

    <!-- Related Posts Section -->
    {relatedPosts.length > 0 && (
      <section class="article-section">
        <h2 class="section-header">See it in action</h2>
        <ul class="related-list">
          {relatedPosts.map(post => (
            <li class="related-list__item">
              <a href={`/blog/${post.slug}`} class="related-list__link">
                {post.title}
              </a>
              <span class="related-list__date">
                {new Date(post.date).toLocaleDateString('en-US', {
                  month: 'short',
                  day: 'numeric',
                  year: 'numeric'
                })}
              </span>
            </li>
          ))}
        </ul>
      </section>
    )}

    <!-- Footer -->
    <footer class="article-footer">
      <a href="/plugins">&larr; Back to plugins</a>
    </footer>
  </article>
</BaseLayout>
```

**Step 2: Test plugin page in browser**

Run: `npm run dev`
Open: http://localhost:4321/plugins/google-ads (or any plugin)
Expected: Large display title, metadata line above, editorial installation block, 65ch width

**Step 3: Test installation block**

Click "First time?" details element
Expected: Expands smoothly to show marketplace add command

**Step 4: Test responsive**

Resize to mobile width
Expected: Typography and spacing scale appropriately

**Step 5: Commit**

```bash
git add src/pages/plugins/[...slug].astro
git commit -m "feat: rebuild plugin page with editorial treatment"
```

---

## Task 5: Simplify Tools Mentioned Component

**Files:**
- Modify: `src/components/ToolsMentioned.astro`

**Step 1: Replace with simple list format**

Replace entire contents of `src/components/ToolsMentioned.astro`:

```astro
---
// src/components/ToolsMentioned.astro
import mergedPlugins from '../data/merged-plugins.json';

interface Props {
  tools: Array<{
    slug: string;
    source: 'channel47' | 'external';
    installCommand?: string;
  }>;
}

const { tools } = Astro.props;

const enrichedTools = tools.map(tool => {
  if (tool.source === 'channel47') {
    const pluginData = mergedPlugins.find(p => p.name === tool.slug);
    return {
      ...tool,
      name: pluginData?.name || tool.slug,
      description: pluginData?.description,
      url: `/plugins/${tool.slug}`,
    };
  }
  return {
    ...tool,
    name: tool.slug,
    description: undefined,
    url: null,
  };
});
---

<div>
  <h2 class="section-header">Tools Mentioned</h2>
  <ul class="related-list">
    {enrichedTools.map(tool => (
      <li class="related-list__item">
        {tool.url ? (
          <a href={tool.url} class="related-list__link">
            {tool.name}
          </a>
        ) : (
          <span style="color: var(--color-text);">{tool.name}</span>
        )}
        {tool.description && (
          <span style="font-size: var(--text-sm); color: var(--color-text-muted); margin-left: var(--space-2);">
            — {tool.description}
          </span>
        )}
      </li>
    ))}
  </ul>
</div>
```

**Step 2: Test tools mentioned section**

Find a blog post with toolsUsed in frontmatter
Open in browser
Expected: Simple list with tool names as links, descriptions inline, no cards

**Step 3: Commit**

```bash
git add src/components/ToolsMentioned.astro
git commit -m "feat: simplify tools mentioned to editorial list format"
```

---

## Task 6: Test Dark Mode

**Files:**
- None (testing only)

**Step 1: Test blog post in dark mode**

Run: `npm run dev`
Open: http://localhost:4321/blog/[any-slug]
Click "Dark" in footer theme toggle
Expected: All colors invert properly, code blocks remain readable, borders visible

**Step 2: Test plugin page in dark mode**

Open: http://localhost:4321/plugins/google-ads
Verify dark mode
Expected: Editorial blocks have visible borders, code readable, metadata visible

**Step 3: Test both themes on mobile**

Resize to mobile width
Toggle between light and dark
Expected: Both themes work at mobile scale

---

## Task 7: Production Build Test

**Files:**
- None (testing only)

**Step 1: Run production build**

Run: `npm run build`
Expected: Build completes without errors or warnings

**Step 2: Preview production build**

Run: `npm run preview`
Open: http://localhost:4321
Navigate to blog post and plugin page
Expected: All styles work in production build, no missing CSS

**Step 3: Check for CSS issues**

Inspect elements in browser dev tools
Expected: All CSS custom properties resolve correctly, no layout shifts

---

## Task 8: Final Verification and Commit

**Files:**
- None (testing only)

**Step 1: Verify all pages**

Test these pages:
- /blog → index should still work
- /blog/[any-post] → editorial treatment
- /plugins → index should still work
- /plugins/[any-plugin] → editorial treatment

Expected: Index pages unchanged, individual pages have new editorial treatment

**Step 2: Verify design specs**

Check against design doc:
- [ ] Titles at 96px desktop, 48px mobile
- [ ] Lead paragraphs at 24px desktop, 20px mobile
- [ ] Metadata in small caps, 12px
- [ ] 65ch max-width on all content
- [ ] 128px top padding on hero (desktop)
- [ ] 96px spacing between sections (desktop)
- [ ] Editorial blocks have 1px border, no backgrounds
- [ ] Code blocks respect 65ch width
- [ ] Footer has border and back link

**Step 3: Final commit if any adjustments**

```bash
git add .
git commit -m "chore: final editorial pages verification"
```

---

## Success Criteria Checklist

- [ ] Blog posts use display typography (96px titles desktop)
- [ ] Plugin pages use display typography (96px titles desktop)
- [ ] All content respects 65ch max-width
- [ ] Hero areas have 128px top padding (desktop)
- [ ] Sections separated by 96px spacing (desktop)
- [ ] Installation blocks use editorial block treatment (border, no background)
- [ ] Code blocks have subtle background and border
- [ ] Metadata in uppercase small caps above titles
- [ ] Lead paragraphs in larger, muted text
- [ ] Related posts and tools mentioned use simple list format
- [ ] Footer has border and back navigation link
- [ ] Responsive scaling works (48px titles, 20px lead on mobile)
- [ ] Dark mode works on all pages
- [ ] Production build succeeds
- [ ] No UI card patterns - only editorial blocks

---

## Notes for Executor

- Each task takes 5-15 minutes
- Test in browser after each file change
- The design prioritizes editorial quality over conventional UI
- 65ch width is sacred - nothing breaks wider
- Editorial blocks feel like magazine rules, not app components
- Commit frequently with descriptive messages
- Reference design doc at `docs/plans/2025-12-23-blog-plugin-editorial-pages-design.md`

---

*Implementation plan complete. Ready for execution.*
