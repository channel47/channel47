# Blog and Plugin Editorial Pages Design

**Date:** 2025-12-23
**Status:** Design Complete, Ready for Implementation
**Context:** Following the editorial redesign of index pages, this document specifies the magazine feature treatment for individual blog posts and plugin pages.

---

## Design Philosophy

Individual blog and plugin pages receive full magazine feature treatment. Each page is an editorial moment with generous whitespace, display-scale typography, and integrated functional elements that maintain aesthetic purity.

Reference the Channel 47 style guide principle: "refined but strange" - editorial elegance with intentional design decisions that create visual interest without decoration.

---

## Architecture

### Page Structure

Both blog posts and plugin pages follow the same editorial foundation:

```
[Hero Area: 128px top padding]
  - Metadata (small caps)
  - Title (display scale)
  - Lead paragraph
  - 96px bottom padding
  - 1px rule

[Content Sections: 96px between each]
  - Installation (plugins only)
  - Body content
  - Tools mentioned (blog) / Related posts (plugins)

[Footer: 64px top padding]
  - Back navigation link
```

### Content Width

- All content: 65ch max-width (per style guide)
- Centered on page with generous side margins
- No elements break wider - not code blocks, not editorial blocks
- Creates strong vertical rhythm and consistent eye tracking

### Section Spacing

- Hero top padding: 128px (--space-10)
- Between sections: 96px (--space-9)
- Hero bottom: 96px (--space-9)
- Footer top: 64px (--space-8)
- Editorial block margins: 64px (--space-8) top/bottom

---

## Typography

### Display Typography (Titles)

**Blog titles and Plugin titles:**
- Font size: --text-5xl (96px) desktop
- Weight: 800 (bold, consistent throughout - no weight mixing)
- Line height: 1.1 (--leading-tight)
- Letter spacing: -0.02em
- Color: var(--color-text)
- Mobile: scales to --text-3xl (48px)

**Design note:** Weight mixing is reserved for collection pages (indexes). Individual pages use consistent weight for cleaner reading experience.

### Lead Paragraphs

- Font size: --text-xl (24px)
- Weight: 400 (regular)
- Line height: 1.6 (--leading-relaxed)
- Color: var(--color-text-muted)
- Position: immediately below title
- Mobile: scales to --text-lg (20px)

**Purpose:** Functions as article summary/hook that could stand alone.

### Metadata

**Date, category, version info:**
- Font size: --text-xs (12px)
- Text transform: uppercase
- Letter spacing: 0.1em
- Color: var(--color-text-muted)
- Position: above title in hero area

**Format examples:**
- Blog: `NOVEMBER 15, 2025`
- Plugin: `v1.2.3 • PRODUCTIVITY`

### Editorial Block Headers

**Section headers like "Installation", "Tools Mentioned":**
- Font size: --text-sm (14px)
- Text transform: uppercase
- Letter spacing: 0.1em
- Weight: 600 (semibold)
- Margin bottom: --space-4 (16px)

### Body Copy

- Font size: --text-base (16px)
- Line height: 1.6
- Max width: 65ch (enforced by container)
- Uses existing prose styles from BlogPost.astro

---

## Editorial Blocks & Functional Elements

### Editorial Block Treatment

**Used for:** Installation sections, callouts, special content areas

**Style:**
- No background fills
- No rounded corners
- No shadows
- Border: 1px solid var(--color-border)
- Padding: --space-6 (32px) all sides
- Margin: --space-8 (64px) top and bottom
- Max width: 65ch (same as prose)

**Design note:** Feels like a ruled-off section in a magazine, not a UI card.

### Code Blocks

**Style:**
- Background: var(--color-gray-100) light mode, var(--color-gray-200) dark mode
- Border: 1px solid var(--color-border)
- Padding: --space-5 (24px)
- Font: monospace, --text-sm (14px)
- No syntax highlighting colors - muted editorial treatment
- Respect 65ch width, wrap long lines
- No copy button overlays

### Inline Code

- Background: var(--color-gray-100)
- Padding: 2px 4px
- Border radius: 2px (subtle)
- Same as existing BlogPost prose styles

### Links

- Color: var(--color-accent)
- No underline default
- Underline on hover
- Transition: 200ms ease-out

### Rules/Dividers

- 1px solid var(--color-border)
- Full width within 65ch container
- Used between major sections

---

## Section-Specific Treatments

### Hero Area (Both Blog & Plugin)

**Structure:**
```
Padding top: 128px
Metadata: DATE or VERSION • CATEGORY
Space: 16px
Title: Display scale, bold
Space: 24px
Lead paragraph: Large, muted
Padding bottom: 96px
1px rule
```

**Blog example:**
```
NOVEMBER 15, 2025

Debugging MCP Servers Without Losing Your Mind

A practical guide to troubleshooting Model Context Protocol
servers when they fail silently, refuse to connect, or return
cryptic error messages.
```

**Plugin example:**
```
v2.1.0 • PRODUCTIVITY

Google Ads

Ask questions about your Google Ads data in plain English
and get answers instantly. No GAQL syntax to memorize, no
clicking through dashboards.
```

### Installation Section (Plugins Only)

**Position:** Immediately after hero

**Structure:**
```
INSTALLATION

[Brief instruction prose if needed]

[Editorial block with border containing:]
  Install plugin:
  /plugin install google-ads@channel47

  [Optional collapsed details for marketplace setup]
```

**Design note:** Keep collapsed "first time" marketplace instructions subtle, not prominent.

### Tools Mentioned Section (Blog Posts)

**Position:** After body content, before footer

**Structure:**
```
[96px space or rule]

TOOLS MENTIONED

- Tool Name - Brief one-line description
- Another Tool - Brief description
```

**Style:**
- Simple list, no cards
- Tool names as links
- Descriptions in muted text
- No editorial block border

### Related Posts Section (Plugin Pages)

**Position:** After body content, before footer

**Structure:**
```
[96px space or rule]

SEE IT IN ACTION

- Post Title (Nov 15, 2025)
- Another Post (Dec 10, 2025)
```

**Style:**
- Simple list, no cards
- Post titles as links
- Dates in muted text, small
- No editorial block border

### Footer Navigation

**Structure:**
```
[1px rule]
[64px padding top]

← Back to blog
```

**Style:**
- Minimal treatment
- Font size: --text-sm
- Color: var(--color-accent)
- Underline on hover

---

## Responsive Behavior

### Mobile (< 768px)

**Typography scales:**
- Title: 96px → 48px (--text-5xl → --text-3xl)
- Lead: 24px → 20px (--text-xl → --text-lg)
- Body: 16px (unchanged)
- Editorial headers: 14px (unchanged)

**Spacing compresses:**
- Hero top: 128px → 64px
- Section breaks: 96px → 48px
- Editorial block padding: 32px → 24px
- Editorial block margin: 64px → 48px
- Side padding: 48px → 24px

**Layout:**
- Single column stack
- Same order, same hierarchy
- Content respects 65ch but uses full available width with padding
- No layout restructuring

### Tablet (768px - 1024px)

- Uses desktop typography and spacing
- Narrower viewport, content scales naturally
- No special breakpoint treatment

**Design principle:** Mobile is the same editorial treatment at appropriate scale, not a compressed desktop. Magazine quality remains intact.

---

## Implementation Approach

### Files to Modify

1. **Blog Post Layout**
   - `src/layouts/BlogPost.astro` - Complete rebuild
   - New styles: `src/styles/components/blog-post.css`

2. **Plugin Page Template**
   - `src/pages/plugins/[...slug].astro` - Complete rebuild
   - New styles: `src/styles/components/plugin-page.css`

3. **Shared Components**
   - `src/components/ToolsMentioned.astro` - Simplify to list
   - Consider creating: `src/components/EditorialBlock.astro` for reusable block treatment

### Style Organization

Create component-specific CSS files that import global tokens:

```css
/* blog-post.css or plugin-page.css */
.article-hero {
  padding-top: var(--space-10);
  max-width: 65ch;
  margin: 0 auto;
}

.article-title {
  font-size: var(--text-5xl);
  font-weight: 800;
  line-height: var(--leading-tight);
  letter-spacing: -0.02em;
  color: var(--color-text);
}

/* etc. */
```

### Component Hierarchy

**BlogPost.astro structure:**
```astro
<BaseLayout>
  <article class="editorial-article">
    <div class="article-hero">
      <time class="article-meta">DATE</time>
      <h1 class="article-title">TITLE</h1>
      <p class="article-lead">DESCRIPTION</p>
    </div>

    <div class="article-content">
      <slot />
    </div>

    {toolsUsed && <ToolsMentioned />}

    <footer class="article-footer">
      <a href="/blog">← Back to blog</a>
    </footer>
  </article>
</BaseLayout>
```

**Plugin page structure:**
```astro
<BaseLayout>
  <article class="editorial-article">
    <div class="article-hero">
      <div class="article-meta">v{version} • {category}</div>
      <h1 class="article-title">{name}</h1>
      <p class="article-lead">{description}</p>
    </div>

    <section class="article-section">
      <h2 class="section-header">Installation</h2>
      <EditorialBlock>
        <!-- install code -->
      </EditorialBlock>
    </section>

    <div class="article-content">
      <slot />
    </div>

    {relatedPosts && <RelatedPosts />}

    <footer class="article-footer">
      <a href="/plugins">← Back to plugins</a>
    </footer>
  </article>
</BaseLayout>
```

---

## Design Decisions & Rationale

### Why no weight mixing on individual pages?

Weight mixing creates visual interest on collection pages (indexes) where you're scanning multiple titles. On individual pages, you're reading linearly - consistent weight provides better readability. The "strange" element is already present in the scale (96px titles) and generous spacing.

### Why 65ch for everything?

Consistency creates rhythm. When code blocks and editorial blocks respect the same width as prose, the eye tracks a single vertical line down the page. This is more editorial than breaking wide for code (which feels more like documentation).

### Why such large section spacing?

96px between sections creates distinct editorial moments. Each section exists independently rather than flowing continuously. This is magazine spread thinking - your eye completes one section, then moves to the next distinct area.

### Why simple borders instead of cards?

Cards (rounded corners, shadows, backgrounds) are UI patterns that signal "interactive element" or "component." Editorial blocks use traditional print design language: rules, whitespace, and hierarchy. A 1px border is a typographic element, not a UI affordance.

---

## Success Criteria

- [ ] Blog posts feel like magazine features, not blog articles
- [ ] Plugin pages balance editorial treatment with functional clarity
- [ ] Display typography creates strong opening impact
- [ ] Installation instructions remain clear despite editorial treatment
- [ ] Code blocks integrate aesthetically while staying readable
- [ ] 65ch width creates consistent vertical rhythm
- [ ] Section spacing provides generous breathing room
- [ ] Mobile experience maintains editorial quality at smaller scale
- [ ] No UI card patterns - only editorial blocks with rules
- [ ] Works in both light and dark mode
- [ ] Related content sections feel integrated, not appended

---

## Open Questions for Implementation

- Should we add pull quotes for blog posts with particularly good snippets?
- Do we want margin annotations for technical asides? (would require wider layout)
- Should code blocks have any visual flourish (subtle rule on left?) or stay completely minimal?
- Do plugin pages need a "Quick Start" vs "Full Installation" treatment?

---

*Design validated through iterative review. Ready for implementation planning.*
