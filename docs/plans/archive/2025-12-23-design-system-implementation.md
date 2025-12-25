# Design System Overhaul Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Implement complete design system overhaul with editorial aesthetic, starting with plugin index as proof-of-concept.

**Architecture:** Remove Tailwind CSS completely, build custom design system with CSS custom properties, BEM-ish component styles, asymmetric grid layout for plugin spreads, auto-hide navigation, and dark mode support.

**Tech Stack:** Astro, CSS custom properties, vanilla JavaScript for interactions

---

## Task 1: Remove Tailwind Dependencies

**Files:**
- Modify: `package.json`
- Delete: `tailwind.config.mjs`
- Modify: `src/styles/global.css`

**Step 1: Remove Tailwind packages from package.json**

Edit `package.json`, remove these lines:
```json
"@astrojs/tailwind": "^6.0.2",
"tailwindcss": "^3.4.19"
```

And from devDependencies:
```json
"@tailwindcss/typography": "^0.5.19",
```

**Step 2: Run npm install to update dependencies**

Run: `npm install`
Expected: Dependencies updated, Tailwind removed

**Step 3: Delete Tailwind config**

Run: `rm tailwind.config.mjs`
Expected: File deleted

**Step 4: Clear global.css**

Replace `src/styles/global.css` with empty file (we'll rebuild it next):
```css
/* Design system foundation - will be populated in next task */
```

**Step 5: Commit**

```bash
git add package.json package-lock.json tailwind.config.mjs src/styles/global.css
git commit -m "chore: remove tailwind css dependencies"
```

---

## Task 2: Create Design Token Foundation

**Files:**
- Modify: `src/styles/global.css`

**Step 1: Add color tokens to global.css**

```css
/* Design Tokens */
:root {
  /* Neutrals - Light Mode */
  --color-black: #0a0a0a;
  --color-white: #fafafa;
  --color-gray-100: #f0f0f0;
  --color-gray-200: #e0e0e0;
  --color-gray-300: #c0c0c0;
  --color-gray-400: #909090;
  --color-gray-500: #606060;
  --color-gray-600: #404040;
  --color-gray-700: #303030;
  --color-gray-800: #1a1a1a;

  /* Accent */
  --color-accent: #0047ff;
  --color-accent-muted: rgba(0, 71, 255, 0.12);

  /* Semantic tokens - Light Mode */
  --color-bg: var(--color-white);
  --color-text: var(--color-black);
  --color-text-muted: var(--color-gray-500);
  --color-border: var(--color-gray-200);
}
```

**Step 2: Add typography tokens**

Append to `src/styles/global.css`:
```css
  /* Typography Scale */
  --text-xs: 0.75rem;      /* 12px */
  --text-sm: 0.875rem;     /* 14px */
  --text-base: 1rem;       /* 16px */
  --text-lg: 1.25rem;      /* 20px */
  --text-xl: 1.5rem;       /* 24px */
  --text-2xl: 2rem;        /* 32px */
  --text-3xl: 3rem;        /* 48px */
  --text-4xl: 4.5rem;      /* 72px */
  --text-5xl: 6rem;        /* 96px */

  /* Line Heights */
  --leading-tight: 1.1;
  --leading-normal: 1.4;
  --leading-relaxed: 1.6;
```

**Step 3: Add spacing tokens**

Append to `src/styles/global.css`:
```css
  /* Spacing Scale */
  --space-1: 0.25rem;   /* 4px */
  --space-2: 0.5rem;    /* 8px */
  --space-3: 0.75rem;   /* 12px */
  --space-4: 1rem;      /* 16px */
  --space-5: 1.5rem;    /* 24px */
  --space-6: 2rem;      /* 32px */
  --space-7: 3rem;      /* 48px */
  --space-8: 4rem;      /* 64px */
  --space-9: 6rem;      /* 96px */
  --space-10: 8rem;     /* 128px */
}
```

**Step 4: Add base styles**

Append to `src/styles/global.css`:
```css
/* Base Styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

body {
  background-color: var(--color-bg);
  color: var(--color-text);
  font-size: var(--text-base);
  line-height: var(--leading-relaxed);
}

a {
  color: inherit;
  text-decoration: none;
}
```

**Step 5: Check in browser**

Run: `npm run dev`
Open: http://localhost:4321
Expected: Site loads (will look broken - that's ok)

**Step 6: Commit**

```bash
git add src/styles/global.css
git commit -m "feat: add design system tokens and base styles"
```

---

## Task 3: Add Dark Mode Support

**Files:**
- Modify: `src/styles/global.css`

**Step 1: Add dark mode color tokens**

Append to `src/styles/global.css`:
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

**Step 2: Check dark mode in browser**

Change system preference to dark mode
Expected: Site background should be black, text white

**Step 3: Commit**

```bash
git add src/styles/global.css
git commit -m "feat: add dark mode color tokens"
```

---

## Task 4: Update Font Loading

**Files:**
- Modify: `src/layouts/BaseLayout.astro`

**Step 1: Update font links in BaseLayout**

Replace the Google Fonts link in `src/layouts/BaseLayout.astro` (around line 21-23):

Old:
```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono&display=swap" rel="stylesheet">
```

New:
```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
```

**Step 2: Remove Tailwind classes from body**

In `src/layouts/BaseLayout.astro`, change:

Old (line 26):
```html
<body class="min-h-screen flex flex-col">
```

New:
```html
<body>
```

**Step 3: Add basic layout styles to global.css**

Append to `src/styles/global.css`:
```css
body {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

main {
  flex: 1;
}
```

**Step 4: Check in browser**

Run: `npm run dev`
Expected: Fonts load properly, layout still works

**Step 5: Commit**

```bash
git add src/layouts/BaseLayout.astro src/styles/global.css
git commit -m "feat: update font loading for full Inter weight range"
```

---

## Task 5: Create Component Styles Directory

**Files:**
- Create: `src/styles/components/header.css`
- Create: `src/styles/components/plugin-spread.css`

**Step 1: Create components directory**

Run: `mkdir -p src/styles/components`

**Step 2: Create empty header.css**

Create `src/styles/components/header.css`:
```css
/* Header Component Styles */
```

**Step 3: Create empty plugin-spread.css**

Create `src/styles/components/plugin-spread.css`:
```css
/* Plugin Spread Component Styles */
```

**Step 4: Commit**

```bash
git add src/styles/components/
git commit -m "chore: create component styles directory"
```

---

## Task 6: Build New Header Component

**Files:**
- Modify: `src/components/Header.astro`
- Modify: `src/styles/components/header.css`

**Step 1: Write header styles**

Replace `src/styles/components/header.css`:
```css
/* Header Component */
.header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 50;
  background-color: var(--color-bg);
  transition: transform 200ms ease-out;
}

.header--hidden {
  transform: translateY(-100%);
}

.header__nav {
  max-width: 1280px;
  margin: 0 auto;
  padding: var(--space-4) var(--space-7);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.header__wordmark {
  font-size: var(--text-lg);
  color: var(--color-text);
}

.header__wordmark-light {
  font-weight: 400;
}

.header__wordmark-bold {
  font-weight: 700;
}

.header__links {
  display: flex;
  gap: var(--space-6);
  font-size: var(--text-sm);
  line-height: var(--leading-normal);
}

.header__link {
  color: var(--color-text-muted);
  transition: color 200ms ease-out;
}

.header__link:hover {
  color: var(--color-accent);
}

@media (max-width: 768px) {
  .header__nav {
    padding: var(--space-4) var(--space-6);
  }

  .header__links {
    gap: var(--space-5);
  }
}
```

**Step 2: Rebuild Header component**

Replace `src/components/Header.astro`:
```astro
---
// src/components/Header.astro
import '../styles/components/header.css';
---
<header class="header" id="main-header">
  <nav class="header__nav">
    <a href="/" class="header__wordmark">
      <span class="header__wordmark-light">Channel</span>
      <span class="header__wordmark-bold">47</span>
    </a>
    <div class="header__links">
      <a href="/blog" class="header__link">Blog</a>
      <a href="/plugins" class="header__link">Tools</a>
      <a href="/about" class="header__link">About</a>
    </div>
  </nav>
</header>

<script>
  let lastScroll = 0;
  const header = document.getElementById('main-header');

  window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;

    if (currentScroll <= 0) {
      header?.classList.remove('header--hidden');
      return;
    }

    if (currentScroll > lastScroll && currentScroll > 100) {
      // Scrolling down
      header?.classList.add('header--hidden');
    } else {
      // Scrolling up
      header?.classList.remove('header--hidden');
    }

    lastScroll = currentScroll;
  });
</script>
```

**Step 3: Add spacing for fixed header**

Append to `src/styles/global.css`:
```css
/* Account for fixed header */
main {
  padding-top: 80px;
}
```

**Step 4: Check in browser**

Run: `npm run dev`
Test: Scroll down (header hides), scroll up (header shows)
Expected: Auto-hide works, typography matches design

**Step 5: Commit**

```bash
git add src/components/Header.astro src/styles/components/header.css src/styles/global.css
git commit -m "feat: rebuild header with auto-hide scroll behavior"
```

---

## Task 7: Add Theme Toggle to Footer

**Files:**
- Modify: `src/components/Footer.astro`
- Create: `src/styles/components/footer.css`

**Step 1: Create footer styles**

Create `src/styles/components/footer.css`:
```css
/* Footer Component */
.footer {
  border-top: 1px solid var(--color-border);
  padding: var(--space-8) var(--space-7);
}

.footer__content {
  max-width: 1280px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.footer__theme-toggle {
  display: flex;
  gap: var(--space-3);
  font-size: var(--text-sm);
}

.footer__theme-option {
  background: none;
  border: none;
  color: var(--color-text-muted);
  cursor: pointer;
  font-family: inherit;
  font-size: inherit;
  transition: color 200ms ease-out;
}

.footer__theme-option:hover {
  color: var(--color-text);
}

.footer__theme-option--active {
  color: var(--color-accent);
  font-weight: 600;
}

@media (max-width: 768px) {
  .footer__content {
    flex-direction: column;
    gap: var(--space-6);
  }
}
```

**Step 2: Rebuild Footer component**

Replace `src/components/Footer.astro`:
```astro
---
// src/components/Footer.astro
import '../styles/components/footer.css';
---
<footer class="footer">
  <div class="footer__content">
    <p style="font-size: var(--text-sm); color: var(--color-text-muted);">
      © 2025 Channel 47
    </p>
    <div class="footer__theme-toggle">
      <button class="footer__theme-option" data-theme-option="light">Light</button>
      <span style="color: var(--color-text-muted);">/</span>
      <button class="footer__theme-option" data-theme-option="dark">Dark</button>
      <span style="color: var(--color-text-muted);">/</span>
      <button class="footer__theme-option footer__theme-option--active" data-theme-option="auto">Auto</button>
    </div>
  </div>
</footer>

<script>
  const THEME_KEY = 'channel47-theme';

  function applyTheme(theme: string) {
    const html = document.documentElement;

    if (theme === 'auto') {
      html.removeAttribute('data-theme');
    } else {
      html.setAttribute('data-theme', theme);
    }

    // Update active state
    document.querySelectorAll('.footer__theme-option').forEach(btn => {
      const btnTheme = btn.getAttribute('data-theme-option');
      if (btnTheme === theme) {
        btn.classList.add('footer__theme-option--active');
      } else {
        btn.classList.remove('footer__theme-option--active');
      }
    });
  }

  function initTheme() {
    const saved = localStorage.getItem(THEME_KEY) || 'auto';
    applyTheme(saved);
  }

  // Apply theme immediately (before page renders)
  initTheme();

  // Add click handlers
  document.querySelectorAll('.footer__theme-option').forEach(btn => {
    btn.addEventListener('click', () => {
      const theme = btn.getAttribute('data-theme-option') || 'auto';
      localStorage.setItem(THEME_KEY, theme);
      applyTheme(theme);
    });
  });
</script>
```

**Step 3: Test theme toggle**

Run: `npm run dev`
Test: Click Light/Dark/Auto buttons
Expected: Theme changes immediately, persists on refresh

**Step 4: Commit**

```bash
git add src/components/Footer.astro src/styles/components/footer.css
git commit -m "feat: add theme toggle to footer"
```

---

## Task 8: Create Plugin Spread Styles Foundation

**Files:**
- Modify: `src/styles/components/plugin-spread.css`

**Step 1: Write base grid system**

Replace `src/styles/components/plugin-spread.css`:
```css
/* Plugin Index Grid */
.plugin-index {
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 var(--space-7);
}

.plugin-index__hero {
  padding-top: var(--space-9);
  padding-bottom: var(--space-7);
}

.plugin-index__title {
  font-size: var(--text-4xl);
  font-weight: 700;
  line-height: var(--leading-tight);
  letter-spacing: -0.02em;
  margin-bottom: var(--space-5);
}

.plugin-index__subtitle {
  font-size: var(--text-lg);
  color: var(--color-text-muted);
  max-width: 65ch;
  line-height: var(--leading-relaxed);
}

.plugin-index__filters {
  padding-bottom: var(--space-8);
  display: flex;
  gap: var(--space-4);
  flex-wrap: wrap;
}

.plugin-filter {
  background: none;
  border: none;
  font-family: inherit;
  font-size: var(--text-sm);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--color-gray-400);
  cursor: pointer;
  transition: color 200ms ease-out;
  padding: var(--space-2) 0;
}

.plugin-filter:hover {
  color: var(--color-accent);
}

.plugin-filter--active {
  color: var(--color-text);
  font-weight: 600;
}

/* Plugin Spreads Grid */
.plugin-spreads {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: var(--space-6);
}

/* Spread Size Variants */
.plugin-spread {
  display: block;
  padding: var(--space-7) 0;
  border-top: 1px solid var(--color-border);
}

.plugin-spread:first-child {
  border-top: none;
}

.plugin-spread--featured {
  grid-column: span 12;
  padding: var(--space-9) 0;
}

.plugin-spread--large {
  grid-column: span 8;
}

.plugin-spread--medium {
  grid-column: span 6;
}

.plugin-spread--small {
  grid-column: span 4;
}
```

**Step 2: Add spread anatomy styles**

Append to `src/styles/components/plugin-spread.css`:
```css
/* Spread Anatomy */
.plugin-spread__category {
  font-size: var(--text-xs);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--color-text-muted);
  margin-bottom: var(--space-3);
}

.plugin-spread__name {
  margin-bottom: var(--space-4);
  line-height: var(--leading-tight);
  letter-spacing: -0.02em;
  color: var(--color-text);
  transition: color 200ms ease-out;
}

.plugin-spread:hover .plugin-spread__name {
  color: var(--color-accent);
}

.plugin-spread--featured .plugin-spread__name {
  font-size: var(--text-4xl);
}

.plugin-spread--large .plugin-spread__name {
  font-size: var(--text-2xl);
}

.plugin-spread--medium .plugin-spread__name {
  font-size: var(--text-xl);
}

.plugin-spread--small .plugin-spread__name {
  font-size: var(--text-lg);
}

.plugin-spread__description {
  color: var(--color-text-muted);
  line-height: var(--leading-relaxed);
  max-width: 65ch;
  margin-bottom: var(--space-4);
}

.plugin-spread--featured .plugin-spread__description {
  font-size: var(--text-lg);
}

.plugin-spread--large .plugin-spread__description {
  font-size: var(--text-base);
}

.plugin-spread--medium .plugin-spread__description,
.plugin-spread--small .plugin-spread__description {
  font-size: var(--text-base);
}

.plugin-spread__meta {
  font-size: var(--text-xs);
  color: var(--color-gray-400);
  display: flex;
  gap: var(--space-3);
}

.plugin-spread__code {
  margin-top: var(--space-5);
  font-family: 'JetBrains Mono', monospace;
  font-size: var(--text-sm);
  background-color: var(--color-gray-100);
  padding: var(--space-4);
  border-radius: 4px;
  color: var(--color-text);
}
```

**Step 3: Add responsive styles**

Append to `src/styles/components/plugin-spread.css`:
```css
/* Responsive */
@media (max-width: 1023px) {
  .plugin-spread--large,
  .plugin-spread--medium,
  .plugin-spread--small {
    grid-column: span 12;
  }

  .plugin-spread--large .plugin-spread__name {
    font-size: var(--text-2xl);
  }

  .plugin-spread--medium .plugin-spread__name,
  .plugin-spread--small .plugin-spread__name {
    font-size: var(--text-xl);
  }
}

@media (max-width: 768px) {
  .plugin-index {
    padding: 0 var(--space-6);
  }

  .plugin-index__hero {
    padding-top: var(--space-8);
    padding-bottom: var(--space-6);
  }

  .plugin-index__title {
    font-size: var(--text-3xl);
  }

  .plugin-spreads {
    display: block;
  }

  .plugin-spread {
    padding: var(--space-6) 0;
  }

  .plugin-spread--featured {
    padding: var(--space-8) 0;
  }

  .plugin-spread--featured .plugin-spread__name {
    font-size: var(--text-3xl);
  }
}
```

**Step 4: Check styles exist**

Run: `cat src/styles/components/plugin-spread.css | wc -l`
Expected: File has content

**Step 5: Commit**

```bash
git add src/styles/components/plugin-spread.css
git commit -m "feat: create plugin spread component styles"
```

---

## Task 9: Rebuild Plugin Index Page

**Files:**
- Modify: `src/pages/plugins/index.astro`

**Step 1: Backup current file**

Run: `cp src/pages/plugins/index.astro src/pages/plugins/index.astro.backup`

**Step 2: Replace plugin index with new layout**

Replace `src/pages/plugins/index.astro`:
```astro
---
// src/pages/plugins/index.astro
import { getCollection } from 'astro:content';
import BaseLayout from '../../layouts/BaseLayout.astro';
import mergedPlugins from '../../data/merged-plugins.json';
import '../../styles/components/plugin-spread.css';

const plugins = await getCollection('plugins', ({ data }) => !data.draft);

// Merge with marketplace data
const enrichedPlugins = plugins.map(plugin => {
  const marketplaceData = mergedPlugins.find(p => p.name === plugin.slug);
  return {
    ...plugin,
    marketplaceData,
    featured: data.featured || false
  };
});

// Sort: featured first, then by slug
enrichedPlugins.sort((a, b) => {
  if (a.featured && !b.featured) return -1;
  if (!a.featured && b.featured) return 1;
  return a.slug.localeCompare(b.slug);
});

// Get unique categories
const categories = ['all', ...new Set(mergedPlugins.map(p => p.category))];

// Assign spread sizes for asymmetric layout
function getSpreadSize(index: number, isFeatured: boolean): string {
  if (isFeatured) return 'featured';

  const pattern = index % 5;
  if (pattern === 0) return 'large';
  if (pattern === 1 || pattern === 2) return 'medium';
  return 'small';
}

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
---

<BaseLayout
  title="Plugins"
  description="Battle-tested Claude Code plugins from daily workflows."
>
  <div class="plugin-index">
    <header class="plugin-index__hero">
      <h1 class="plugin-index__title">
        <span style="font-weight: 700;">Tools</span>
        <span style="font-weight: 300;">that work</span>
      </h1>
      <p class="plugin-index__subtitle">
        Battle-tested Claude Code plugins from daily workflows. All free. Quality over quantity.
      </p>
    </header>

    <div class="plugin-index__filters">
      <button class="plugin-filter plugin-filter--active" data-filter="all">
        All
      </button>
      {categories.slice(1).map(cat => (
        <button class="plugin-filter" data-filter={cat}>
          {cat}
        </button>
      ))}
    </div>

    <div class="plugin-spreads">
      {enrichedPlugins.map(({ slug, data, marketplaceData, featured }, index) => {
        const size = getSpreadSize(index, featured);
        const name = marketplaceData?.name || slug;
        const nameParts = splitName(name);

        return (
          <a
            href={`/plugins/${slug}`}
            class={`plugin-spread plugin-spread--${size}`}
            data-category={marketplaceData?.category || 'uncategorized'}
          >
            <div class="plugin-spread__category">
              {marketplaceData?.category || 'plugin'}
            </div>

            <h2 class="plugin-spread__name">
              <span style="font-weight: 700;">{nameParts.first}</span>
              {nameParts.second && (
                <span style="font-weight: 400;"> {nameParts.second}</span>
              )}
            </h2>

            <p class="plugin-spread__description">
              {marketplaceData?.description || ''}
            </p>

            <div class="plugin-spread__meta">
              <span>by {marketplaceData?.author || 'Unknown'}</span>
              <span>·</span>
              <span>v{marketplaceData?.version || '0.0.0'}</span>
            </div>

            {size === 'featured' && marketplaceData?.name && (
              <div class="plugin-spread__code">
                claude plugins install {marketplaceData.name}
              </div>
            )}
          </a>
        );
      })}
    </div>
  </div>
</BaseLayout>

<script>
  // Category filter functionality
  const filters = document.querySelectorAll('.plugin-filter');
  const spreads = document.querySelectorAll('.plugin-spread');

  filters.forEach(filter => {
    filter.addEventListener('click', () => {
      const category = filter.getAttribute('data-filter');

      // Update active state
      filters.forEach(f => f.classList.remove('plugin-filter--active'));
      filter.classList.add('plugin-filter--active');

      // Filter spreads
      spreads.forEach(spread => {
        const spreadCategory = spread.getAttribute('data-category');
        if (category === 'all' || spreadCategory === category) {
          (spread as HTMLElement).style.display = 'block';
        } else {
          (spread as HTMLElement).style.display = 'none';
        }
      });
    });
  });
</script>
```

**Step 3: Test in browser**

Run: `npm run dev`
Open: http://localhost:4321/plugins
Expected: New asymmetric layout, weight mixing in titles, category filters work

**Step 4: Test responsive**

Resize browser to mobile width
Expected: Stacks to single column, maintains typography hierarchy

**Step 5: Commit**

```bash
git add src/pages/plugins/index.astro
git commit -m "feat: rebuild plugin index with asymmetric spreads"
```

---

## Task 10: Fix Homepage Styles

**Files:**
- Modify: `src/pages/index.astro`
- Create: `src/styles/components/home.css`

**Step 1: Create home page styles**

Create `src/styles/components/home.css`:
```css
/* Home Page */
.home-section {
  max-width: 1280px;
  margin: 0 auto;
  padding: var(--space-9) var(--space-7);
}

.home-hero {
  max-width: 42rem;
}

.home-hero__title {
  font-size: var(--text-4xl);
  font-weight: 700;
  line-height: var(--leading-tight);
  letter-spacing: -0.02em;
  margin-bottom: var(--space-6);
}

.home-hero__accent {
  color: var(--color-accent);
  font-weight: 400;
}

.home-hero__description {
  font-size: var(--text-lg);
  color: var(--color-text-muted);
  line-height: var(--leading-relaxed);
  margin-bottom: var(--space-8);
}

.home-hero__actions {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-4);
}

.button {
  display: inline-flex;
  align-items: center;
  padding: var(--space-4) var(--space-6);
  font-size: var(--text-base);
  font-weight: 500;
  border-radius: 4px;
  transition: all 200ms ease-out;
  cursor: pointer;
}

.button--primary {
  background-color: var(--color-accent);
  color: var(--color-white);
  border: none;
}

.button--primary:hover {
  background-color: #0039cc;
}

.button--secondary {
  background-color: transparent;
  color: var(--color-text);
  border: 1px solid var(--color-border);
}

.button--secondary:hover {
  border-color: var(--color-text);
}

.section-divider {
  border-top: 1px solid var(--color-border);
}

.section-title {
  font-size: var(--text-2xl);
  font-weight: 600;
  margin-bottom: var(--space-8);
}

@media (max-width: 768px) {
  .home-section {
    padding: var(--space-8) var(--space-6);
  }

  .home-hero__title {
    font-size: var(--text-3xl);
  }
}
```

**Step 2: Rebuild homepage**

Replace `src/pages/index.astro`:
```astro
---
// src/pages/index.astro
import BaseLayout from '../layouts/BaseLayout.astro';
import EmailSignup from '../components/EmailSignup.astro';
import '../styles/components/home.css';
---
<BaseLayout title="Home">
  <section class="home-section">
    <div class="home-hero">
      <h1 class="home-hero__title">
        Claude Code tools<br />
        <span class="home-hero__accent">I actually use.</span>
      </h1>
      <p class="home-hero__description">
        I spend way too much time building and testing Claude Code extensions. This is where I publish the ones worth keeping. Skills, plugins, MCP servers. Some I built myself, others I found and verified.
      </p>
      <div class="home-hero__actions">
        <a href="/plugins" class="button button--primary">
          Browse Tools
        </a>
        <a href="/blog" class="button button--secondary">
          Read the Blog
        </a>
      </div>
    </div>
  </section>

  <section class="section-divider">
    <div class="home-section">
      <h2 class="section-title">Latest from the blog</h2>
      <p style="color: var(--color-text-muted);">Posts coming soon...</p>
    </div>
  </section>

  <section class="section-divider">
    <div class="home-section">
      <div style="max-width: 32rem; margin: 0 auto;">
        <EmailSignup
          title="Get notified when I add new tools"
          description="Usually once or twice a month. I only send updates when there's something genuinely useful."
          source="homepage"
        />
      </div>
    </div>
  </section>
</BaseLayout>
```

**Step 3: Test homepage**

Run: `npm run dev`
Open: http://localhost:4321
Expected: Homepage styled with new design system

**Step 4: Commit**

```bash
git add src/pages/index.astro src/styles/components/home.css
git commit -m "feat: rebuild homepage with new design system"
```

---

## Task 11: Update EmailSignup Component

**Files:**
- Modify: `src/components/EmailSignup.astro`
- Create: `src/styles/components/email-signup.css`

**Step 1: Create email signup styles**

Create `src/styles/components/email-signup.css`:
```css
/* Email Signup Component */
.email-signup {
  text-align: center;
}

.email-signup__title {
  font-size: var(--text-xl);
  font-weight: 600;
  margin-bottom: var(--space-4);
}

.email-signup__description {
  color: var(--color-text-muted);
  margin-bottom: var(--space-6);
  line-height: var(--leading-relaxed);
}

.email-signup__form {
  display: flex;
  gap: var(--space-3);
}

.email-signup__input {
  flex: 1;
  padding: var(--space-4);
  font-family: inherit;
  font-size: var(--text-base);
  background-color: var(--color-bg);
  border: 1px solid var(--color-border);
  border-radius: 4px;
  color: var(--color-text);
}

.email-signup__input:focus {
  outline: none;
  border-color: var(--color-accent);
}

.email-signup__button {
  padding: var(--space-4) var(--space-6);
  font-family: inherit;
  font-size: var(--text-base);
  font-weight: 500;
  background-color: var(--color-accent);
  color: var(--color-white);
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 200ms ease-out;
}

.email-signup__button:hover {
  background-color: #0039cc;
}

@media (max-width: 768px) {
  .email-signup__form {
    flex-direction: column;
  }
}
```

**Step 2: Update EmailSignup component**

Replace `src/components/EmailSignup.astro` to remove Tailwind classes:
```astro
---
// src/components/EmailSignup.astro
import '../styles/components/email-signup.css';

interface Props {
  title?: string;
  description?: string;
  source?: string;
}

const {
  title = 'Get notified of new tools',
  description = 'Updates when I publish something new.',
  source = 'unknown'
} = Astro.props;
---

<div class="email-signup">
  <h3 class="email-signup__title">{title}</h3>
  <p class="email-signup__description">{description}</p>
  <form class="email-signup__form" method="POST" action="/api/subscribe">
    <input
      type="email"
      name="email"
      placeholder="your@email.com"
      required
      class="email-signup__input"
    />
    <input type="hidden" name="source" value={source} />
    <button type="submit" class="email-signup__button">
      Subscribe
    </button>
  </form>
</div>
```

**Step 3: Test email signup**

Run: `npm run dev`
Expected: Email signup form styled correctly

**Step 4: Commit**

```bash
git add src/components/EmailSignup.astro src/styles/components/email-signup.css
git commit -m "feat: update email signup component styles"
```

---

## Task 12: Fix About Page

**Files:**
- Modify: `src/pages/about.astro`

**Step 1: Update about page**

Replace `src/pages/about.astro` to remove Tailwind:
```astro
---
import BaseLayout from '../layouts/BaseLayout.astro';
import '../styles/components/home.css';
---

<BaseLayout
  title="About"
  description="About Channel 47 and these Claude Code tools."
>
  <div class="home-section">
    <div style="max-width: 42rem;">
      <h1 style="
        font-size: var(--text-4xl);
        font-weight: 700;
        line-height: var(--leading-tight);
        letter-spacing: -0.02em;
        margin-bottom: var(--space-6);
      ">
        About Channel 47
      </h1>

      <div style="
        font-size: var(--text-lg);
        color: var(--color-text-muted);
        line-height: var(--leading-relaxed);
      ">
        <p style="margin-bottom: var(--space-6);">
          This is a personal collection of Claude Code tools I've built and vetted. I'm a developer who spends too much time in Claude Code, so I built the extensions I wanted to exist.
        </p>

        <p style="margin-bottom: var(--space-6);">
          Everything here is free and open source. Some plugins I built myself. Others I found, tested thoroughly, and recommend. If it's listed here, I use it in my own work.
        </p>

        <p>
          The blog covers workflows, patterns, and occasional deep dives into how these tools actually work under the hood.
        </p>
      </div>
    </div>
  </div>
</BaseLayout>
```

**Step 2: Test about page**

Run: `npm run dev`
Open: http://localhost:4321/about
Expected: About page styled correctly

**Step 3: Commit**

```bash
git add src/pages/about.astro
git commit -m "feat: update about page styling"
```

---

## Task 13: Clean Up Build Config

**Files:**
- Modify: `astro.config.mjs`

**Step 1: Check Astro config**

Run: `cat astro.config.mjs`

**Step 2: Remove Tailwind integration if present**

If `@astrojs/tailwind` is imported in `astro.config.mjs`, remove it:

Old:
```javascript
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  integrations: [tailwind()],
});
```

New:
```javascript
export default defineConfig({
  integrations: [],
});
```

**Step 3: Test build**

Run: `npm run build`
Expected: Build succeeds without Tailwind

**Step 4: Commit if changed**

```bash
git add astro.config.mjs
git commit -m "chore: remove tailwind from astro config"
```

---

## Task 14: Add Scroll Fade-In Animation (Optional)

**Files:**
- Modify: `src/styles/components/plugin-spread.css`
- Modify: `src/pages/plugins/index.astro`

**Step 1: Add animation styles**

Append to `src/styles/components/plugin-spread.css`:
```css
/* Scroll Fade Animation (Optional) */
.plugin-spread {
  opacity: 1;
  transform: translateY(0);
  transition: opacity 400ms ease-out, transform 400ms ease-out;
}

.plugin-spread--animate {
  opacity: 0.7;
  transform: translateY(20px);
}

.plugin-spread--visible {
  opacity: 1;
  transform: translateY(0);
}
```

**Step 2: Add intersection observer script**

Add to the bottom of `src/pages/plugins/index.astro`, before closing `</BaseLayout>`:

```astro
<script>
  // Scroll-triggered fade-in (optional)
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry, index) => {
        if (entry.isIntersecting) {
          setTimeout(() => {
            entry.target.classList.add('plugin-spread--visible');
            entry.target.classList.remove('plugin-spread--animate');
          }, index * 50); // Stagger by 50ms
        }
      });
    },
    { threshold: 0.1 }
  );

  document.querySelectorAll('.plugin-spread').forEach((spread) => {
    spread.classList.add('plugin-spread--animate');
    observer.observe(spread);
  });
</script>
```

**Step 3: Test animation**

Run: `npm run dev`
Scroll plugin index page
Expected: Spreads fade in as they enter viewport

**Step 4: Commit**

```bash
git add src/styles/components/plugin-spread.css src/pages/plugins/index.astro
git commit -m "feat: add scroll-triggered fade-in animation"
```

---

## Task 15: Final Testing and Documentation

**Files:**
- Create: `docs/design-system.md`

**Step 1: Test all pages**

Visit each page and test:
- http://localhost:4321 (homepage)
- http://localhost:4321/plugins (plugin index)
- http://localhost:4321/about (about page)
- http://localhost:4321/blog (blog index)

**Step 2: Test dark mode**

Toggle theme in footer: Light / Dark / Auto
Expected: All pages work in both modes

**Step 3: Test responsive**

Resize browser to mobile, tablet, desktop
Expected: Layout adapts properly at each breakpoint

**Step 4: Test auto-hide header**

Scroll down on any page
Expected: Header hides smoothly, shows on scroll up

**Step 5: Create design system docs**

Create `docs/design-system.md`:
```markdown
# Design System Documentation

## Using Design Tokens

All design tokens are defined in `src/styles/global.css` as CSS custom properties.

### Colors

```css
var(--color-bg)          /* Background */
var(--color-text)        /* Primary text */
var(--color-text-muted)  /* Secondary text */
var(--color-accent)      /* Blue accent */
var(--color-border)      /* Borders */
```

### Typography

```css
var(--text-xs)    /* 12px */
var(--text-sm)    /* 14px */
var(--text-base)  /* 16px */
var(--text-lg)    /* 20px */
var(--text-xl)    /* 24px */
var(--text-2xl)   /* 32px */
var(--text-3xl)   /* 48px */
var(--text-4xl)   /* 72px */
```

### Spacing

```css
var(--space-1)   /* 4px */
var(--space-4)   /* 16px */
var(--space-6)   /* 32px */
var(--space-8)   /* 64px */
var(--space-9)   /* 96px */
```

## Component Styles

Create component-scoped styles in `src/styles/components/`.

Import in Astro components:
```astro
import '../styles/components/my-component.css';
```

## Weight Mixing

Use weight mixing for typographic interest:
```html
<h1>
  <span style="font-weight: 700">Bold</span>
  <span style="font-weight: 400">Light</span>
</h1>
```

## Dark Mode

Theme is controlled by `data-theme` attribute on `<html>`:
- `data-theme="light"` - Light mode
- `data-theme="dark"` - Dark mode
- No attribute - Auto (follows system preference)
```

**Step 6: Commit documentation**

```bash
git add docs/design-system.md
git commit -m "docs: add design system documentation"
```

---

## Task 16: Production Build Test

**Files:**
- None (testing only)

**Step 1: Run production build**

Run: `npm run build`
Expected: Build completes without errors

**Step 2: Preview production build**

Run: `npm run preview`
Open: http://localhost:4321
Expected: Site works identically to dev mode

**Step 3: Check build output**

Run: `ls -lh dist`
Expected: Build artifacts present, reasonable file sizes

**Step 4: Final commit**

```bash
git add .
git commit -m "chore: complete design system overhaul implementation"
```

---

## Success Criteria Checklist

- [ ] Tailwind removed completely
- [ ] Design tokens working in light and dark mode
- [ ] Auto-hide header functions on scroll
- [ ] Plugin index uses asymmetric grid layout
- [ ] Weight mixing applied to headlines
- [ ] Theme toggle works (Light/Dark/Auto)
- [ ] Responsive design works on mobile/tablet/desktop
- [ ] Category filters function correctly
- [ ] All pages styled consistently
- [ ] Production build succeeds
- [ ] Performance maintained (no regression)

---

## Notes for Executor

- Each task is independent and can be completed in 2-5 minutes
- Test in browser after visual changes
- Commit frequently with descriptive messages
- If a step fails, fix the issue before proceeding
- The design is intentionally minimal - resist adding decoration
- Weight mixing should feel intentional, not random
- Whitespace is a feature, not empty space to fill

---

*Implementation plan complete. Ready for execution.*
