# Site Strategy Implementation Plan

This document outlines the comprehensive implementation plan for aligning the Jig website with the strategic framework document. The plan is organized by priority, with dependencies clearly marked.

---

## Implementation Status

| Phase | Status | Completed |
|-------|--------|-----------|
| Phase 1: Tools Infrastructure | ✅ Complete | 2026-01-06 |
| Phase 2: Navigation Restructure | ⏳ Pending | - |
| Phase 3: Homepage Redesign | ⏳ Pending | - |
| Phase 4: Skills Pages Enhancement | ⏳ Pending | - |
| Phase 5: Email Capture Segmentation | ⏳ Pending | - |
| Phase 6: Blog Enhancement | ⏳ Pending | - |
| Phase 7: Contributor/Platform Page | ⏳ Pending | - |
| Phase 8: Low-Level Decisions | ⏳ Pending | - |

---

## Executive Summary: Current State vs. Target State

| Area | Current State | Target State | Gap Severity |
|------|---------------|--------------|--------------|
| Navigation | Skills, Setup, [Google Ads Skills] | Skills, Tools, Blog, [Get Skills] | Medium |
| Homepage | Hero → Body → 2 Paths → Email | Hero (2 CTAs) → Featured → Tools → Email | Medium |
| Skills Index | ✅ Mostly aligned | Product grid + email | Minor |
| Skills Sales | Good structure, missing sticky/trust | Add sticky CTA, trust strip | Medium |
| **Tools Section** | ✅ Implemented | Full /tools index + tool pages | ~~Critical~~ Done |
| Blog | Basic structure | Contextual CTAs + related posts | Medium |
| Email Capture | Single component, no segmentation | Tagged capture by location | Medium |
| Footer | Basic links | Add email signup | Low |
| Contributor | ❌ Does not exist | /contribute page | Low |

---

## Phase 1: Foundation — Tools Infrastructure
**Priority: Critical**
**Dependency: None**
**Status: ✅ COMPLETE**

The strategy document positions free tools as the top-of-funnel lead generation mechanism. Currently, the site has no `/tools` section—only a `/setup` page that provides generic MCP setup instructions.

### Implementation Notes (2026-01-06)

**Files Created:**
- `src/pages/tools/index.astro` — Tools catalog with hero, grid, upsell banner, email signup
- `src/pages/tools/google-ads.astro` — Full setup guide with "The Gap" soft-sell section

**Files Modified:**
- `astro.config.mjs` — Added redirect `/setup` → `/tools/google-ads`

**Files Deleted:**
- `src/pages/setup.astro` — Replaced by redirect and new tool page

**Key Features Implemented:**
- Tools grid with "Free" badge styling (green success color)
- Icon-based tool cards with visual differentiation from skills
- Upsell banner: "Tools give you access. Skills give you judgment."
- "The Gap" section with accent border for soft-sell to skills
- Breadcrumb navigation on tool detail page
- Copy button functionality for MCP URL

**Validation:**
- Build passes with 12 pages generated
- TypeScript check passes
- Redirect generates proper meta refresh HTML
- All links verified correct

### 1.1 Create Tools Index Page (`/tools`)

**File:** `src/pages/tools/index.astro`

**Structure per strategy:**
```
┌─────────────────────────────────────────────────────────────┐
│  HERO                                                       │
│  Free tools. Real capability.                               │
│  Hosted MCP servers you can connect in minutes.             │
├─────────────────────────────────────────────────────────────┤
│  TOOL GRID (similar card design to /skills)                 │
│  - Google Ads MCP (free, available)                         │
│  - Nano Banana MCP (future placeholder)                     │
├─────────────────────────────────────────────────────────────┤
│  UPSELL BANNER                                              │
│  "Tools give you access. Skills give you judgment."         │
│  [Browse Skills →]                                          │
├─────────────────────────────────────────────────────────────┤
│  EMAIL CAPTURE                                              │
│  "New tools in development."                                │
└─────────────────────────────────────────────────────────────┘
```

**Implementation notes:**
- Create data structure for tools (similar to products array in `/skills`)
- Reuse card styling from skills index with visual differentiation
- "Free" badge prominently displayed
- Upsell banner creates natural bridge to paid products

### 1.2 Create Tool Detail Pages (`/tools/[slug]`)

**Files:**
- `src/pages/tools/google-ads.astro` (static, primary tool)
- Consider: `src/pages/tools/[...slug].astro` (for future dynamic tools)

**Structure per strategy:**
```
┌─────────────────────────────────────────────────────────────┐
│  HERO                                                       │
│  Google Ads MCP                                             │
│  Connect in five minutes. Query any account.                │
├─────────────────────────────────────────────────────────────┤
│  QUICK SETUP (migrate from current /setup)                  │
│  1. What you'll need                                        │
│  2. Add the hosted URL                                      │
│  3. Authenticate                                            │
│  4. Test it                                                 │
├─────────────────────────────────────────────────────────────┤
│  THE GAP (soft sell section)                                │
│  "You've got the connection. Now you need the judgment."    │
│  [Get Google Ads Skills — $199]                             │
├─────────────────────────────────────────────────────────────┤
│  EMAIL CAPTURE                                              │
│  "Get updates on this tool."                                │
└─────────────────────────────────────────────────────────────┘
```

**Implementation notes:**
- Migrate content from current `/setup.astro` to `/tools/google-ads.astro`
- Add "The Gap" section for soft-sell (value delivered FIRST, then sell)
- Tool-specific email capture with distinct copy

### 1.3 Handle /setup Redirect

**Options:**
1. **Redirect:** 301 redirect `/setup` → `/tools/google-ads` (preserves SEO)
2. **Keep both:** Maintain `/setup` as generic overview, tool-specific pages for details

**Recommendation:** Option 1 (redirect) — cleaner architecture, single source of truth

**Implementation:**
- Add redirect in `astro.config.mjs` or create redirect page

---

## Phase 2: Navigation Restructure
**Priority: High**
**Dependency: Phase 1 (Tools pages must exist before nav links work)**

### 2.1 Update Header Component

**File:** `src/components/Header.astro`

**Current navigation:**
```
Jig | Skills | Setup | [Google Ads Skills]
```

**Target navigation per strategy:**
```
Jig | Skills | Tools | Blog | [Get Skills]
```

**Changes:**
1. Replace "Setup" link with "Tools" (`/tools`)
2. Add "Blog" link (`/blog`)
3. Change CTA from "Google Ads Skills" to "Get Skills" → `/skills`
4. Update mobile menu to match

**Rationale:**
- "Skills before Tools" — prioritizes paid product
- "Blog" in main nav drives content discovery
- Generic "Get Skills" CTA works as catalog grows beyond one product

### 2.2 Update Footer Component

**File:** `src/components/Footer.astro`

**Current links:** Skills, Setup, Blog, Contact

**Target links:** Skills, Tools, Blog, Contact (+ email capture)

**Changes:**
1. Replace "Setup" with "Tools" link
2. Add email signup section (see Phase 5)

---

## Phase 3: Homepage Redesign
**Priority: High**
**Dependency: Phase 1 (need /tools to exist for secondary CTA)**

### 3.1 Restructure Homepage Sections

**File:** `src/pages/index.astro`

**Current structure:**
1. Hero (title + subtitle, no CTAs)
2. Body section (problem explanation prose)
3. Paths section (2 cards: Google Ads Skills, Setup Guide)
4. Email signup

**Target structure per strategy:**
1. **Hero** — Title + subtitle + TWO CTAs
   - Primary: "Get the Skills" → `/skills`
   - Secondary: "Browse Free Tools" → `/tools`
2. **Featured Product** — Prominent Google Ads Skills card with price anchor
3. **Secondary Path** — Tools teaser section
4. **Email Capture** — "New skills in development"

**Detailed changes:**

#### Hero Section
- Add CTA button group below subtitle
- Primary button: high contrast, links to `/skills`
- Secondary button: outlined/ghost, links to `/tools`

#### Featured Product Section (NEW)
Replace current "body-section" with featured product card:
```html
<section class="featured-section">
  <div class="featured-card">
    <h2>Google Ads Skills</h2>
    <p>Steal my entire Google Ads brain for less than one billable hour.</p>
    <span class="price">$199</span>
    <a href="/skills/google-ads">See what's included →</a>
  </div>
</section>
```

#### Secondary Path Section
Replace current "paths-section" with tools teaser:
```html
<section class="tools-section">
  <h2>Just want the free tools?</h2>
  <p>MCP servers for Google Ads, creative generation, more.</p>
  <a href="/tools">Browse Tools</a>
</section>
```

### 3.2 Remove Body Section

The current prose-heavy "body section" explaining capability vs. competence should be **removed from homepage**. Rationale:
- Homepage job is to route, not educate
- This content belongs on sales pages where it converts
- Keeps homepage scannable and action-oriented

---

## Phase 4: Skills Pages Enhancement
**Priority: Medium**
**Dependency: None**

### 4.1 Skills Index Minor Updates

**File:** `src/pages/skills/index.astro`

Current implementation is mostly aligned with strategy. Minor enhancements:

1. **Card structure:** Ensure each card shows: name, key benefits, price, CTA
2. **"Coming Soon" handling:** Already implemented correctly
3. **Email capture:** ✅ Already present

### 4.2 Skills Sales Page Enhancements

**File:** `src/pages/skills/google-ads.astro`

Strategy requirements not yet implemented:

#### 4.2.1 Sticky CTA Bar

**Component:** Create `StickyBuyBar.astro`

Appears on scroll (after hero exits viewport):
```
┌───────────────────────────────────────────────────────────┐
│  Google Ads Skills    $199    [Get the Skills]            │
└───────────────────────────────────────────────────────────┘
```

**Implementation:**
- Fixed position at bottom of viewport
- Hidden by default, shown via IntersectionObserver
- Smooth slide-up animation
- Mobile: full-width button, smaller text

#### 4.2.2 Trust Strip

Add near pricing section:
```html
<div class="trust-strip">
  <span>$XX million in managed spend</span>
  <span>Used on XX accounts</span>
  <span>10+ years experience</span>
</div>
```

**Note:** Placeholder values — owner needs to provide real numbers

#### 4.2.3 Exit Intent Popup (Optional)

**Component:** `ExitIntentModal.astro`

Triggers on mouse moving toward browser chrome (desktop only):
```
┌─────────────────────────────────────────────────────┐
│  Not ready?                                         │
│  Get notified when we release updates.              │
│  [Email input] [Notify Me]                          │
└─────────────────────────────────────────────────────┘
```

**Implementation considerations:**
- Should be sales pages only
- One-time trigger (cookie/localStorage)
- Disabled on mobile (no reliable exit intent detection)
- Lower priority than other items

---

## Phase 5: Email Capture Segmentation
**Priority: Medium**
**Dependency: None (can be done in parallel)**

### 5.1 Extend EmailSignup Component

**File:** `src/components/EmailSignup.astro`

**Add new prop:** `tag` for segmentation

```typescript
interface Props {
  title?: string;
  description?: string;
  buttonText?: string;
  variant?: 'inline' | 'card';
  tag?: string;  // NEW: for Beehiiv tagging
  class?: string;
}
```

**Implementation:**
- Add hidden input for tag value
- Beehiiv can receive this for list segmentation

### 5.2 Apply Tags Per Location

Per strategy document:

| Capture Location | Tag |
|------------------|-----|
| Homepage | `general` |
| /skills index | `skills-browser` |
| /skills/google-ads | `google-ads-interested` |
| /tools index | `tools-user` |
| /tools/google-ads | `google-ads-tool-user` |
| Blog posts | `content-reader` |
| Footer | `footer-capture` |

### 5.3 Add Footer Email Signup

**File:** `src/components/Footer.astro`

Add inline email capture as "last resort":
```html
<div class="footer__signup">
  <p>Stay in the loop</p>
  <form>
    <input type="email" placeholder="you@example.com" />
    <button type="submit">Subscribe</button>
  </form>
</div>
```

Styling: compact, inline with footer aesthetic

---

## Phase 6: Blog Enhancement
**Priority: Medium**
**Dependency: Phase 5 (email tagging)**

### 6.1 Add Contextual CTAs to Blog Posts

**File:** `src/layouts/ProseLayout.astro` or `src/pages/blog/[...slug].astro`

**Implementation options:**

1. **Automatic:** Detect post tags, show relevant product CTA
   - Post tagged "google-ads" → Show Google Ads Skills CTA
   - Post tagged "mcp" → Show Tools CTA

2. **Manual:** Add frontmatter field for related product
   ```yaml
   relatedProduct: google-ads-skills
   ```

**CTA Component:** `BlogCTA.astro`
```html
<aside class="blog-cta">
  <h3>Want to go deeper?</h3>
  <p>{product.description}</p>
  <a href="{product.href}">{product.cta} →</a>
</aside>
```

### 6.2 Add Related Posts Section

**Location:** End of blog post, before footer

**Implementation:**
- Query posts collection for matching tags
- Display 2-3 related posts as cards
- Fallback to most recent posts if no tag matches

### 6.3 Blog Email Capture

Ensure every blog post has email capture with `content-reader` tag:
```html
<EmailSignup
  title="More like this?"
  description="Subscribe for new posts."
  tag="content-reader"
  variant="card"
/>
```

---

## Phase 7: Contributor/Platform Page
**Priority: Low**
**Dependency: None**

### 7.1 Create Contributor Page

**File:** `src/pages/contribute.astro`

**Not in main nav** — linked from footer only

**Content per strategy:**
```
┌─────────────────────────────────────────────────────────────┐
│  HERO                                                       │
│  Package your expertise. Reach people who need it.          │
├─────────────────────────────────────────────────────────────┤
│  VISION                                                     │
│  Jig is becoming a platform for experts to package          │
│  and sell their expertise.                                  │
├─────────────────────────────────────────────────────────────┤
│  HOW IT WORKS                                               │
│  - You create skill files                                   │
│  - We handle distribution, payments, support                │
│  - Revenue share model                                      │
├─────────────────────────────────────────────────────────────┤
│  EXPRESSION OF INTEREST                                     │
│  [Form or email capture]                                    │
└─────────────────────────────────────────────────────────────┘
```

### 7.2 Add Footer Link

Add "Contribute" or "For Experts" link in footer nav

---

## Phase 8: Low-Level Decisions Implementation
**Priority: Low**
**Dependency: Various**

Per strategy document recommendations:

| Decision | Recommendation | Implementation |
|----------|----------------|----------------|
| Sticky header | Yes, with CTA | ✅ Already implemented |
| Exit intent popup | Yes, sales pages only | Phase 4.2.3 |
| Product card images | Icons for tools, screenshots for skills | Update card components |
| Pricing display | On card | ✅ Already implemented |
| "Coming Soon" handling | Show with email capture | ✅ Already implemented |
| Blog index page | No for now | Current `/blog` is fine |
| Success page | Unified for now | ✅ `/success.astro` exists |
| Footer email signup | Yes | Phase 5.3 |

---

## Implementation Order & Dependencies

```
Week 1: Foundation
├── Phase 1.1: Create /tools index
├── Phase 1.2: Create /tools/google-ads
├── Phase 1.3: Setup redirect
└── Phase 2: Navigation updates (after Phase 1)

Week 2: Core Pages
├── Phase 3: Homepage redesign
├── Phase 4.1: Skills index minor updates
└── Phase 4.2.1-4.2.2: Sticky CTA + Trust strip

Week 3: Email & Blog
├── Phase 5.1-5.2: Email tagging
├── Phase 5.3: Footer email signup
├── Phase 6.1: Blog contextual CTAs
└── Phase 6.2-6.3: Related posts + blog email

Week 4: Polish
├── Phase 4.2.3: Exit intent (optional)
├── Phase 7: Contributor page
└── Phase 8: Remaining low-level items
```

---

## Files to Create

| File | Purpose |
|------|---------|
| `src/pages/tools/index.astro` | Tools catalog page |
| `src/pages/tools/google-ads.astro` | Google Ads MCP setup |
| `src/components/StickyBuyBar.astro` | Scroll-triggered purchase bar |
| `src/components/BlogCTA.astro` | Contextual product CTA for posts |
| `src/components/ExitIntentModal.astro` | Exit intent email capture (optional) |
| `src/pages/contribute.astro` | Contributor/platform page |

## Files to Modify

| File | Changes |
|------|---------|
| `src/components/Header.astro` | Nav links: add Tools, Blog; change CTA |
| `src/components/Footer.astro` | Add email signup, update links |
| `src/components/EmailSignup.astro` | Add tag prop for segmentation |
| `src/pages/index.astro` | Restructure per strategy |
| `src/pages/skills/google-ads.astro` | Add sticky bar, trust strip |
| `src/layouts/ProseLayout.astro` | Add blog CTA and related posts |
| `astro.config.mjs` | Add /setup → /tools/google-ads redirect |

## Files to Delete/Deprecate

| File | Action |
|------|--------|
| `src/pages/setup.astro` | Replace with redirect to /tools/google-ads |

---

## Design Consistency Notes

Per strategy document design principles:

1. **Visual hierarchy follows priority:**
   - Skills > Tools (accent color for skills, neutral for tools)
   - Primary CTAs high contrast (accent background)
   - Secondary CTAs present but subdued (outline/ghost)

2. **Consistency:**
   - Card design identical between /skills and /tools grids
   - CTA button style consistent site-wide
   - Typography hierarchy maintained

3. **Mobile-first:**
   - Already implemented in current design system
   - Touch targets (48px minimum) already enforced
   - All new components should follow same patterns

4. **Existing design tokens:**
   - Use `--color-accent` for primary actions
   - Use `--color-bg-elevated` for cards
   - Use `--radius-xl` for card borders
   - Follow existing spacing scale

---

## Metrics to Track Post-Implementation

1. **Conversion funnel:**
   - Homepage → /skills (direct buyers)
   - Homepage → /tools → /skills (nurtured buyers)

2. **Email capture rates by location**
   - Compare conversion rates across tagged sources

3. **Tool page → Skills upsell rate**
   - Track clicks on "The Gap" section CTA

4. **Blog → Product clicks**
   - Measure contextual CTA effectiveness

---

## Questions for Product Owner

Before implementation, clarify:

1. **Trust strip numbers:** What specific metrics should we display?
   - Managed ad spend total
   - Number of accounts audited
   - Years of experience

2. **Exit intent:** Priority level? Worth the complexity?

3. **Contributor page:** Ready to accept submissions, or just collect interest?

4. **Additional tools:** Are there other MCP servers to add to /tools?
   - Nano Banana mentioned in strategy
   - Others planned?

5. **Email sequences:** Are Beehiiv sequences ready for different tags?

---

*This plan provides a complete roadmap for implementing the site strategy document. Each phase is self-contained with clear dependencies, allowing for incremental deployment and testing.*
