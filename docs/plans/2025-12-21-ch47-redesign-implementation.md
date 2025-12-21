# CH47 Visual Redesign Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Transform Channel 47 into CH47 with street/culture magazine aesthetics while maintaining all existing functionality.

**Architecture:** Progressive enhancement approach starting with CSS foundation (variables, typography, spacing), then visual effects (grain, halftone), followed by component updates, and finally page-specific implementations with animations.

**Tech Stack:** Astro, Tailwind CSS, Vanilla JavaScript (theme toggle, scroll animations), Google Fonts (Bungee Inline, Staatliches, IBM Plex Sans)

---

## Task 1: Foundation - CSS Variables & Color System

**Files:**
- Modify: `src/styles/global.css`
- Test: Visual inspection in browser (light + dark mode)

**Step 1: Update CSS variables for new color system**

Replace existing Tailwind config colors with CSS variables:

```css
/* src/styles/global.css */
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  :root {
    /* Colors - Light Mode */
    --bg-base: #FAFAFA;
    --ink: #0A0A0A;
    --surface: #F0F0F0;
    --orange: #FF6600;
    --orange-tint: #FFF3ED;

    /* Spacing */
    --space-micro: 8px;
    --space-small: 16px;
    --space-medium: 32px;
    --space-large: 48px;
    --space-xl: 80px;
    --space-2xl: 120px;
    --space-3xl: 160px;

    /* Typography */
    --font-display: 'Bungee Inline', sans-serif;
    --font-header: 'Staatliches', sans-serif;
    --font-body: 'IBM Plex Sans', sans-serif;
    --font-mono: 'JetBrains Mono', monospace;

    --text-mega: clamp(2.5rem, 5vw, 4.5rem);
    --text-display: clamp(2rem, 3.5vw, 3rem);
    --text-headline: clamp(1.5rem, 2.5vw, 2rem);
    --text-body: 1.125rem;
    --text-caption: 0.875rem;

    /* Effects */
    --grain-opacity: 0.03;
    --shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
    --shadow-large: 0 8px 32px rgba(0, 0, 0, 0.15);

    /* Grid */
    --container-width: 1280px;
    --grid-columns: 12;
    --grid-gap: 24px;
  }

  [data-theme="dark"] {
    --bg-base: #0A0A0A;
    --ink: #FAFAFA;
    --surface: #1A1A1A;
    --orange: #FF7722;
    --orange-tint: #1A0F0A;
    --grain-opacity: 0.04;
    --shadow: 0 4px 16px rgba(255, 255, 255, 0.1);
    --shadow-large: 0 8px 32px rgba(255, 255, 255, 0.15);
  }

  html {
    @apply antialiased;
  }

  body {
    background-color: var(--bg-base);
    color: var(--ink);
    font-family: var(--font-body);
    font-size: var(--text-body);
  }
}
```

**Step 2: Test in browser**

Run: `npm run dev`
Expected: Site loads with new off-white background (#FAFAFA) and rich black text (#0A0A0A)

**Step 3: Commit**

```bash
git add src/styles/global.css
git commit -m "feat: add CSS variables for CH47 color system and spacing"
```

---

## Task 2: Typography System - Font Loading

**Files:**
- Modify: `src/layouts/BaseLayout.astro:21-23`

**Step 1: Update font imports**

Replace existing Google Fonts link with new typography:

```html
<!-- src/layouts/BaseLayout.astro -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bungee+Inline&family=Staatliches&family=IBM+Plex+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
```

**Step 2: Update page title**

Change "Channel 47" to "CH47":

```html
<title>{title} | CH47</title>
```

**Step 3: Test font loading**

Run: `npm run dev`
Open browser DevTools Network tab
Expected: See requests for Bungee Inline, Staatliches, IBM Plex Sans fonts

**Step 4: Commit**

```bash
git add src/layouts/BaseLayout.astro
git commit -m "feat: load CH47 typography fonts (Bungee Inline, Staatliches, IBM Plex Sans)"
```

---

## Task 3: Tailwind Config - Extend with CSS Variables

**Files:**
- Modify: `tailwind.config.mjs`

**Step 1: Update Tailwind config to use CSS variables**

```javascript
/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        'bg-base': 'var(--bg-base)',
        'ink': 'var(--ink)',
        'surface': 'var(--surface)',
        'orange': 'var(--orange)',
        'orange-tint': 'var(--orange-tint)',
      },
      fontFamily: {
        display: 'var(--font-display)',
        header: 'var(--font-header)',
        body: 'var(--font-body)',
        mono: 'var(--font-mono)',
      },
      fontSize: {
        mega: 'var(--text-mega)',
        display: 'var(--text-display)',
        headline: 'var(--text-headline)',
        body: 'var(--text-body)',
        caption: 'var(--text-caption)',
      },
      spacing: {
        'micro': 'var(--space-micro)',
        'small': 'var(--space-small)',
        'medium': 'var(--space-medium)',
        'large': 'var(--space-large)',
        'xl': 'var(--space-xl)',
        '2xl': 'var(--space-2xl)',
        '3xl': 'var(--space-3xl)',
      },
      boxShadow: {
        'ch47': 'var(--shadow)',
        'ch47-large': 'var(--shadow-large)',
      },
    },
  },
  plugins: [require('@tailwindcss/typography')],
}
```

**Step 2: Test Tailwind classes**

Run: `npm run dev`
Expected: Tailwind classes like `text-orange` and `font-display` work with CSS variables

**Step 3: Commit**

```bash
git add tailwind.config.mjs
git commit -m "feat: extend Tailwind config with CH47 design tokens"
```

---

## Task 4: Visual Effect - Grain Texture Overlay

**Files:**
- Modify: `src/layouts/BaseLayout.astro:15-16` (after head tags)
- Modify: `src/styles/global.css` (add grain styles)

**Step 1: Add grain SVG filter to BaseLayout**

Add before closing `</head>`:

```html
<!-- Grain texture filter -->
<svg style="position: absolute; width: 0; height: 0;" aria-hidden="true">
  <defs>
    <filter id="grain">
      <feTurbulence baseFrequency="0.8" numOctaves="4" type="fractalNoise"/>
      <feColorMatrix type="saturate" values="0"/>
    </filter>
  </defs>
</svg>
```

**Step 2: Add grain overlay styles**

Add to `src/styles/global.css`:

```css
@layer base {
  body::after {
    content: '';
    position: fixed;
    inset: 0;
    background: url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxmaWx0ZXIgaWQ9ImEiPjxmZVR1cmJ1bGVuY2UgYmFzZUZyZXF1ZW5jeT0iLjgiIG51bU9jdGF2ZXM9IjQiLz48L2ZpbHRlcj48cmVjdCB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiBmaWx0ZXI9InVybCgjYSkiLz48L3N2Zz4=');
    opacity: var(--grain-opacity);
    pointer-events: none;
    mix-blend-mode: overlay;
    z-index: 9999;
  }
}
```

**Step 3: Test grain texture**

Run: `npm run dev`
Expected: Subtle texture overlay visible on all backgrounds (3% opacity in light mode)

**Step 4: Commit**

```bash
git add src/layouts/BaseLayout.astro src/styles/global.css
git commit -m "feat: add grain texture overlay effect"
```

---

## Task 5: Theme Toggle Component

**Files:**
- Create: `src/components/ThemeToggle.astro`
- Create: `public/scripts/theme.js`

**Step 1: Create theme toggle component**

```astro
---
// src/components/ThemeToggle.astro
---
<button
  id="theme-toggle"
  aria-label="Toggle theme"
  class="p-2 rounded hover:bg-surface transition-colors"
>
  <svg class="sun-icon w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" />
  </svg>
  <svg class="moon-icon w-5 h-5 hidden" fill="none" viewBox="0 0 24 24" stroke="currentColor">
    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" />
  </svg>
</button>

<script>
  function initTheme() {
    const toggle = document.getElementById('theme-toggle');
    const html = document.documentElement;
    const sunIcon = toggle?.querySelector('.sun-icon');
    const moonIcon = toggle?.querySelector('.moon-icon');

    // Initialize theme
    const savedTheme = localStorage.getItem('theme') ||
      (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    html.setAttribute('data-theme', savedTheme);
    updateIcons(savedTheme);

    // Toggle handler
    toggle?.addEventListener('click', () => {
      const currentTheme = html.getAttribute('data-theme') || 'light';
      const newTheme = currentTheme === 'light' ? 'dark' : 'light';

      html.style.setProperty('transition', 'background-color 0.3s, color 0.3s');
      html.setAttribute('data-theme', newTheme);
      localStorage.setItem('theme', newTheme);
      updateIcons(newTheme);

      setTimeout(() => {
        html.style.removeProperty('transition');
      }, 300);
    });

    function updateIcons(theme: string) {
      if (theme === 'dark') {
        sunIcon?.classList.add('hidden');
        moonIcon?.classList.remove('hidden');
      } else {
        sunIcon?.classList.remove('hidden');
        moonIcon?.classList.add('hidden');
      }
    }
  }

  // Run on load and after navigation
  initTheme();
  document.addEventListener('astro:after-swap', initTheme);
</script>
```

**Step 2: Test theme toggle**

Run: `npm run dev`
Expected: Button appears but not integrated yet (next task)

**Step 3: Commit**

```bash
git add src/components/ThemeToggle.astro
git commit -m "feat: create theme toggle component with localStorage persistence"
```

---

## Task 6: Header Component Redesign

**Files:**
- Modify: `src/components/Header.astro`

**Step 1: Redesign header with CH47 branding**

```astro
---
// src/components/Header.astro
import ThemeToggle from './ThemeToggle.astro';
---
<header class="border-b-2 border-ink/10 bg-bg-base/80 backdrop-blur-sm sticky top-0 z-50 transition-all duration-300" id="main-header">
  <nav class="max-w-[1280px] mx-auto px-6 py-4 flex items-center justify-between">
    <a href="/" class="flex items-center gap-2">
      <span class="logo text-2xl font-display relative" data-text="CH47">CH47</span>
    </a>
    <div class="flex items-center gap-6 text-sm">
      <a href="/blog" class="nav-link font-header uppercase tracking-wide text-ink hover:text-orange transition-colors">Blog</a>
      <a href="/plugins" class="nav-link font-header uppercase tracking-wide text-ink hover:text-orange transition-colors">Tools</a>
      <a href="/about" class="nav-link font-header uppercase tracking-wide text-ink hover:text-orange transition-colors">About</a>
      <ThemeToggle />
    </div>
  </nav>
</header>

<style>
  .logo::before,
  .logo::after {
    content: attr(data-text);
    position: absolute;
    inset: 0;
  }
  .logo::before {
    color: cyan;
    transform: translate(-2px, -2px);
    opacity: 0.3;
  }
  .logo::after {
    color: red;
    transform: translate(2px, 2px);
    opacity: 0.3;
  }

  /* Active nav styling */
  .nav-link {
    position: relative;
  }
  .nav-link::before {
    content: '[';
    opacity: 0;
    transform: translateX(4px);
    transition: all 0.2s ease;
  }
  .nav-link::after {
    content: ']';
    opacity: 0;
    transform: translateX(-4px);
    transition: all 0.2s ease;
  }
  .nav-link:hover::before,
  .nav-link:hover::after {
    opacity: 1;
    transform: translateX(0);
  }

  /* Header compression on scroll */
  #main-header {
    height: 80px;
  }
  #main-header.compressed {
    height: 64px;
  }
</style>

<script>
  let lastScroll = 0;
  const header = document.getElementById('main-header');

  window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;
    if (currentScroll > 100) {
      header?.classList.add('compressed');
    } else {
      header?.classList.remove('compressed');
    }
    lastScroll = currentScroll;
  });
</script>
```

**Step 2: Test header**

Run: `npm run dev`
Expected:
- CH47 logo with chromatic offset visible
- Nav items show brackets on hover
- Header compresses when scrolling down
- Theme toggle works

**Step 3: Commit**

```bash
git add src/components/Header.astro
git commit -m "feat: redesign header with CH47 logo and chromatic offset"
```

---

## Task 7: Footer Component Redesign

**Files:**
- Modify: `src/components/Footer.astro`

**Step 1: Minimal footer redesign**

```astro
---
// src/components/Footer.astro
---
<footer class="border-t-2 border-ink/10 mt-auto">
  <div class="max-w-[1280px] mx-auto px-6 py-16">
    <div class="flex flex-col gap-4 relative">
      <span class="section-number" aria-hidden="true">05</span>
      <span class="logo text-xl font-display relative inline-block" data-text="CH47">CH47</span>
      <p class="text-ink/60 max-w-md">Digital tools for Claude Code power users</p>
      <p class="text-caption text-ink/40 mt-4">
        Built with <a href="https://claude.com/claude-code" class="text-orange hover:underline">Claude Code</a> • 2025
      </p>
    </div>
  </div>
</footer>

<style>
  .logo::before,
  .logo::after {
    content: attr(data-text);
    position: absolute;
    inset: 0;
  }
  .logo::before {
    color: cyan;
    transform: translate(-2px, -2px);
    opacity: 0.3;
  }
  .logo::after {
    color: red;
    transform: translate(2px, 2px);
    opacity: 0.3;
  }

  .section-number {
    font-family: var(--font-header);
    font-size: 120px;
    color: var(--orange);
    opacity: 0.15;
    position: absolute;
    right: -40px;
    top: -20px;
    line-height: 1;
    user-select: none;
    pointer-events: none;
  }

  @media (max-width: 768px) {
    .section-number {
      font-size: 80px;
      right: -20px;
      top: -10px;
    }
  }
</style>
```

**Step 2: Test footer**

Run: `npm run dev`
Expected: Minimal footer with CH47 logo, decorative "05" section number

**Step 3: Commit**

```bash
git add src/components/Footer.astro
git commit -m "feat: redesign footer with minimal layout and section number"
```

---

## Task 8: Utility CSS Classes - Effects

**Files:**
- Modify: `src/styles/global.css`

**Step 1: Add utility classes for visual effects**

Add to end of `global.css`:

```css
@layer components {
  /* Halftone effect */
  .halftone {
    position: relative;
  }
  .halftone::after {
    content: '';
    position: absolute;
    inset: 0;
    background-image: radial-gradient(circle, var(--ink) 1px, transparent 1px);
    background-size: 4px 4px;
    opacity: 0.15;
    mix-blend-mode: multiply;
    pointer-events: none;
  }
  [data-theme="dark"] .halftone::after {
    mix-blend-mode: screen;
    background-image: radial-gradient(circle, var(--bg-base) 1px, transparent 1px);
  }

  /* Orange highlighter */
  .highlight {
    position: relative;
    display: inline;
  }
  .highlight::after {
    content: '';
    position: absolute;
    bottom: 0.1em;
    left: -0.1em;
    right: -0.1em;
    height: 0.3em;
    background: var(--orange);
    opacity: 0.3;
    z-index: -1;
  }

  /* Section number utility */
  .section-number {
    font-family: var(--font-header);
    font-size: clamp(80px, 10vw, 120px);
    color: var(--orange);
    opacity: 0.15;
    line-height: 1;
    user-select: none;
    pointer-events: none;
  }

  /* Link animations */
  .link-underline {
    position: relative;
    text-decoration: none;
  }
  .link-underline::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    width: 0;
    height: 2px;
    background: var(--orange);
    transition: width 0.3s ease;
  }
  .link-underline:hover::after {
    width: 100%;
  }
  .link-underline:hover {
    letter-spacing: 0.02em;
    transition: letter-spacing 0.3s ease;
  }

  /* Brutalist form elements */
  .input-brutalist {
    border: 2px solid var(--ink);
    border-radius: 0;
    background: var(--bg-base);
    padding: 12px 16px;
    font-family: var(--font-body);
    color: var(--ink);
    transition: all 0.2s ease;
  }
  .input-brutalist:focus {
    outline: none;
    border-color: var(--orange);
    transform: translateY(-2px);
    box-shadow: var(--shadow);
  }

  /* Button base */
  .btn-brutalist {
    border: 2px solid var(--ink);
    border-radius: 0;
    background: var(--bg-base);
    padding: 12px 24px;
    font-family: var(--font-header);
    font-size: 14px;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: var(--ink);
    cursor: pointer;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
  }
  .btn-brutalist:hover {
    border-width: 4px;
    transform: translateY(-2px);
    box-shadow: var(--shadow-large);
  }

  /* Primary button */
  .btn-primary {
    background: var(--orange);
    border-color: var(--orange);
    color: var(--bg-base);
  }
  .btn-primary:hover {
    background: var(--ink);
    border-color: var(--ink);
  }
}

@layer utilities {
  /* Animation utilities */
  .animate-fade-in-up {
    animation: fadeInUp 0.6s cubic-bezier(0.34, 1.56, 0.64, 1) both;
  }

  @keyframes fadeInUp {
    from {
      opacity: 0;
      transform: translateY(30px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }

  /* Reduced motion */
  @media (prefers-reduced-motion: reduce) {
    *,
    *::before,
    *::after {
      animation-duration: 0.01ms !important;
      animation-iteration-count: 1 !important;
      transition-duration: 0.01ms !important;
      scroll-behavior: auto !important;
    }
  }
}
```

**Step 2: Test utility classes**

Run: `npm run dev`
Expected: Classes available for use in components

**Step 3: Commit**

```bash
git add src/styles/global.css
git commit -m "feat: add utility classes for halftone, highlights, and brutalist forms"
```

---

## Task 9: Homepage Hero Redesign

**Files:**
- Modify: `src/pages/index.astro`

**Step 1: Redesign hero section**

```astro
---
// src/pages/index.astro
import BaseLayout from '../layouts/BaseLayout.astro';
import EmailSignup from '../components/EmailSignup.astro';
---
<BaseLayout title="Home">
  <!-- Hero Section -->
  <section class="relative overflow-hidden bg-orange-tint halftone">
    <div class="max-w-[1280px] mx-auto px-6 py-2xl relative">
      <span class="section-number absolute right-0 top-0" aria-hidden="true">01</span>

      <!-- NEW label -->
      <div class="absolute top-8 right-8 transform rotate-3">
        <span class="bg-orange text-bg-base px-4 py-2 font-header text-sm uppercase tracking-wide">New</span>
      </div>

      <div class="max-w-2xl relative z-10">
        <h1 class="font-display text-mega text-ink leading-tight animate-fade-in-up" style="animation-delay: 0.2s">
          Tools for Claude Code
        </h1>
        <p class="font-display text-display text-orange animate-fade-in-up" style="animation-delay: 0.3s">
          <span class="highlight">power users</span>
        </p>

        <p class="mt-6 text-body text-ink/80 leading-relaxed animate-fade-in-up" style="animation-delay: 0.4s">
          A curated directory of skills, plugins, MCP servers, and prompts to supercharge your
          AI-assisted development workflow. Quality picks from the community, plus my own builds.
        </p>

        <div class="mt-8 flex flex-wrap gap-4 animate-fade-in-up" style="animation-delay: 0.5s">
          <a href="/plugins" class="btn-brutalist btn-primary">
            Browse Tools →
          </a>
          <a href="/blog" class="btn-brutalist">
            Read the Blog
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- Featured Tools Section -->
  <section class="border-t-2 border-ink/10 relative">
    <div class="max-w-[1280px] mx-auto px-6 py-xl">
      <span class="section-number absolute right-0 top-8" aria-hidden="true">02</span>
      <h2 class="font-header text-display text-ink mb-8 uppercase tracking-wide">Featured Tools</h2>
      <p class="text-ink/60">Coming soon...</p>
    </div>
  </section>

  <!-- Latest Blog Section -->
  <section class="border-t-2 border-ink/10 bg-surface/50 relative">
    <div class="max-w-[1280px] mx-auto px-6 py-xl">
      <span class="section-number absolute right-0 top-8" aria-hidden="true">03</span>
      <h2 class="font-header text-display text-ink mb-8 uppercase tracking-wide">Latest from the Blog</h2>
      <p class="text-ink/60">Posts coming soon...</p>
    </div>
  </section>

  <!-- Email Signup Section -->
  <section class="border-t-2 border-ink/10 relative">
    <div class="max-w-[1280px] mx-auto px-6 py-xl">
      <span class="section-number absolute right-0 top-8" aria-hidden="true">04</span>
      <div class="max-w-md mx-auto">
        <EmailSignup
          title="Stay in the loop"
          description="Get notified when new tools drop. No spam, just useful stuff."
          source="homepage"
        />
      </div>
    </div>
  </section>
</BaseLayout>
```

**Step 2: Test homepage**

Run: `npm run dev`
Visit: `http://localhost:4321`
Expected:
- Hero with orange tint background and halftone
- CH47 typography visible (Bungee Inline)
- "power users" has orange highlight
- Section numbers visible (01, 02, 03, 04)
- Staggered fade-in animations
- NEW label rotated in corner

**Step 3: Commit**

```bash
git add src/pages/index.astro
git commit -m "feat: redesign homepage hero with CH47 aesthetics"
```

---

## Task 10: EmailSignup Component Redesign

**Files:**
- Modify: `src/components/EmailSignup.astro`

**Step 1: Apply brutalist form styling**

```astro
---
// src/components/EmailSignup.astro
interface Props {
  title: string;
  description: string;
  source: string;
}

const { title, description, source } = Astro.props;
---

<div class="email-signup">
  <h3 class="font-header text-headline text-ink mb-4 uppercase tracking-wide">{title}</h3>
  <p class="text-ink/70 mb-6">{description}</p>

  <form action="/api/subscribe" method="POST" class="flex flex-col gap-4">
    <input type="hidden" name="source" value={source} />
    <input
      type="email"
      name="email"
      placeholder="your@email.com"
      required
      class="input-brutalist w-full"
    />
    <button type="submit" class="btn-brutalist btn-primary w-full">
      Subscribe →
    </button>
  </form>

  <div class="message mt-4 hidden"></div>
</div>

<script>
  document.querySelectorAll('.email-signup form').forEach(form => {
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const formElement = e.target as HTMLFormElement;
      const messageEl = formElement.parentElement?.querySelector('.message');

      try {
        const formData = new FormData(formElement);
        const response = await fetch(formElement.action, {
          method: 'POST',
          body: formData,
        });

        const data = await response.json();

        if (messageEl) {
          messageEl.classList.remove('hidden');
          messageEl.textContent = data.message;
          messageEl.className = response.ok
            ? 'message mt-4 text-orange font-header'
            : 'message mt-4 text-ink/60 font-header';
        }

        if (response.ok) {
          formElement.reset();
        }
      } catch (error) {
        if (messageEl) {
          messageEl.classList.remove('hidden');
          messageEl.textContent = 'Something went wrong. Please try again.';
          messageEl.className = 'message mt-4 text-ink/60 font-header';
        }
      }
    });
  });
</script>
```

**Step 2: Test form**

Run: `npm run dev`
Expected:
- Input has thick black border, no radius
- Focus state shows orange border
- Button uses brutalist styling
- Hover effects work

**Step 3: Commit**

```bash
git add src/components/EmailSignup.astro
git commit -m "feat: apply brutalist styling to email signup form"
```

---

## Task 11: Create ProductCard Component

**Files:**
- Create: `src/components/ProductCard.astro`

**Step 1: Create product card with hover effects**

```astro
---
// src/components/ProductCard.astro
interface Props {
  title: string;
  description: string;
  href: string;
  tags?: string[];
}

const { title, description, href, tags = [] } = Astro.props;
---

<a href={href} class="product-card group block">
  <div class="card-inner border-2 border-ink bg-surface p-medium transition-all duration-300 relative overflow-hidden">
    <!-- Orange accent bar (slides in on hover) -->
    <div class="accent-bar absolute left-0 top-0 bottom-0 w-1 bg-orange transform -translate-x-full group-hover:translate-x-0 transition-transform duration-300"></div>

    <div class="relative z-10">
      <h3 class="font-header text-headline text-ink mb-3 uppercase tracking-wide">{title}</h3>
      <p class="text-body text-ink/70 mb-4 leading-relaxed">{description}</p>

      {tags.length > 0 && (
        <div class="flex flex-wrap gap-2 mb-4">
          {tags.map(tag => (
            <span class="text-caption font-mono text-ink/50">#{tag}</span>
          ))}
        </div>
      )}

      <div class="arrow opacity-0 group-hover:opacity-100 transition-opacity text-orange">
        →
      </div>
    </div>
  </div>
</a>

<style>
  .product-card .card-inner {
    background: var(--surface);
  }

  .product-card:hover .card-inner {
    transform: translateY(-8px);
    box-shadow: var(--shadow-large);
  }

  /* Grain texture on card */
  .card-inner::before {
    content: '';
    position: absolute;
    inset: 0;
    background: url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxmaWx0ZXIgaWQ9ImEiPjxmZVR1cmJ1bGVuY2UgYmFzZUZyZXF1ZW5jeT0iLjgiIG51bU9jdGF2ZXM9IjQiLz48L2ZpbHRlcj48cmVjdCB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiBmaWx0ZXI9InVybCgjYSkiLz48L3N2Zz4=');
    opacity: 0.02;
    pointer-events: none;
  }
</style>
```

**Step 2: Test product card**

Create test page or add to homepage:
Expected:
- Card has thick border, no radius
- Hover: lifts 8px, orange bar slides in, shadow appears
- Arrow appears on hover

**Step 3: Commit**

```bash
git add src/components/ProductCard.astro
git commit -m "feat: create ProductCard component with brutalist styling"
```

---

## Task 12: Create BlogCard Component

**Files:**
- Create: `src/components/BlogCard.astro`

**Step 1: Create blog card component**

```astro
---
// src/components/BlogCard.astro
interface Props {
  title: string;
  excerpt: string;
  href: string;
  date: string;
  readTime?: string;
}

const { title, excerpt, href, date, readTime } = Astro.props;
---

<a href={href} class="blog-card group block">
  <article class="card-inner border-2 border-ink bg-surface p-medium transition-all duration-300 h-full">
    <h3 class="font-header text-headline text-ink mb-3 uppercase tracking-wide group-hover:text-orange transition-colors">
      {title}
    </h3>
    <p class="text-body text-ink/70 mb-4 leading-relaxed line-clamp-3">{excerpt}</p>

    <div class="flex items-center gap-4 text-caption text-ink/50 font-mono mt-auto">
      <time datetime={date}>{new Date(date).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })}</time>
      {readTime && <span>• {readTime}</span>}
    </div>
  </article>
</a>

<style>
  .blog-card:hover .card-inner {
    transform: translateY(-4px);
    box-shadow: var(--shadow);
  }

  .card-inner {
    display: flex;
    flex-direction: column;
  }
</style>
```

**Step 2: Test blog card**

Expected: Card with minimal design, hover lift effect

**Step 3: Commit**

```bash
git add src/components/BlogCard.astro
git commit -m "feat: create BlogCard component with hover effects"
```

---

## Task 13: Scroll Animation Observer

**Files:**
- Create: `public/scripts/scroll-animations.js`
- Modify: `src/layouts/BaseLayout.astro` (add script)

**Step 1: Create scroll animation script**

```javascript
// public/scripts/scroll-animations.js
(function() {
  function initScrollAnimations() {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry, index) => {
        if (entry.isIntersecting) {
          // Add stagger delay
          entry.target.style.animationDelay = `${index * 100}ms`;
          entry.target.classList.add('animate-fade-in-up');
          observer.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.1,
      rootMargin: '0px 0px -100px 0px'
    });

    // Observe all elements with .reveal class
    document.querySelectorAll('.reveal').forEach(el => {
      observer.observe(el);
    });
  }

  // Run on load
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initScrollAnimations);
  } else {
    initScrollAnimations();
  }

  // Re-run after Astro page transitions
  document.addEventListener('astro:after-swap', initScrollAnimations);
})();
```

**Step 2: Add script to BaseLayout**

```html
<!-- src/layouts/BaseLayout.astro -->
<!-- Add before closing </body> -->
<script src="/scripts/scroll-animations.js"></script>
```

**Step 3: Test scroll animations**

Run: `npm run dev`
Add `class="reveal"` to any element
Expected: Elements fade in when scrolling into view

**Step 4: Commit**

```bash
git add public/scripts/scroll-animations.js src/layouts/BaseLayout.astro
git commit -m "feat: add scroll-triggered reveal animations"
```

---

## Task 14: Custom Cursor (Desktop Only)

**Files:**
- Create: `public/scripts/custom-cursor.js`
- Modify: `src/layouts/BaseLayout.astro`

**Step 1: Create custom cursor script**

```javascript
// public/scripts/custom-cursor.js
(function() {
  // Only on desktop devices with mouse
  if (window.matchMedia('(hover: none)').matches) return;

  function initCustomCursor() {
    // Create cursor dot
    const cursor = document.createElement('div');
    cursor.className = 'cursor-dot';
    document.body.appendChild(cursor);

    let mouseX = 0;
    let mouseY = 0;
    let cursorX = 0;
    let cursorY = 0;

    // Track mouse position
    document.addEventListener('mousemove', (e) => {
      mouseX = e.clientX;
      mouseY = e.clientY;
    });

    // Smooth follow animation
    function animate() {
      const dx = mouseX - cursorX;
      const dy = mouseY - cursorY;

      cursorX += dx * 0.15;
      cursorY += dy * 0.15;

      cursor.style.left = cursorX + 'px';
      cursor.style.top = cursorY + 'px';

      requestAnimationFrame(animate);
    }
    animate();

    // Hover effect on interactive elements
    const interactiveElements = 'a, button, input, textarea, [role="button"]';

    document.addEventListener('mouseover', (e) => {
      if (e.target.closest(interactiveElements)) {
        cursor.classList.add('hover');
      }
    });

    document.addEventListener('mouseout', (e) => {
      if (e.target.closest(interactiveElements)) {
        cursor.classList.remove('hover');
      }
    });
  }

  // Run on load
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initCustomCursor);
  } else {
    initCustomCursor();
  }
})();
```

**Step 2: Add cursor styles to global.css**

```css
/* Add to src/styles/global.css */
@layer base {
  @media (hover: hover) {
    body {
      cursor: none;
    }
  }

  .cursor-dot {
    width: 12px;
    height: 12px;
    background: var(--orange);
    border-radius: 50%;
    position: fixed;
    pointer-events: none;
    z-index: 10000;
    transition: transform 0.15s ease-out;
    mix-blend-mode: difference;
  }

  .cursor-dot.hover {
    transform: scale(2);
  }

  @media (hover: none) {
    body {
      cursor: auto !important;
    }
    .cursor-dot {
      display: none;
    }
  }
}
```

**Step 3: Add script to BaseLayout**

```html
<script src="/scripts/custom-cursor.js"></script>
```

**Step 4: Test custom cursor**

Run: `npm run dev`
On desktop: Orange dot follows cursor, scales on hover
On mobile: Normal cursor

**Step 5: Commit**

```bash
git add public/scripts/custom-cursor.js src/styles/global.css src/layouts/BaseLayout.astro
git commit -m "feat: add custom cursor for desktop devices"
```

---

## Task 15: Plugins Index Page Redesign

**Files:**
- Modify: `src/pages/plugins/index.astro`

**Step 1: Redesign plugins index**

```astro
---
// src/pages/plugins/index.astro
import BaseLayout from '../../layouts/BaseLayout.astro';
import ProductCard from '../../components/ProductCard.astro';
import { getCollection } from 'astro:content';

const plugins = await getCollection('plugins');
---

<BaseLayout title="Tools" description="Curated plugins, skills, and MCP servers for Claude Code">
  <div class="relative">
    <!-- Vertical section label -->
    <div class="hidden lg:block fixed left-8 top-1/2 -translate-y-1/2 z-40">
      <span class="font-display text-4xl text-orange/20 writing-mode-vertical transform -rotate-180">
        TOOLS
      </span>
    </div>

    <section class="max-w-[1280px] mx-auto px-6 py-xl relative">
      <span class="section-number absolute right-0 top-0" aria-hidden="true">01</span>

      <div class="mb-xl">
        <h1 class="font-display text-mega text-ink mb-4">
          Tools Directory
        </h1>
        <p class="text-body text-ink/70 max-w-2xl">
          Curated collection of plugins, skills, and MCP servers to enhance your Claude Code workflow.
        </p>
      </div>

      {plugins.length > 0 ? (
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {plugins.map((plugin) => (
            <div class="reveal">
              <ProductCard
                title={plugin.data.title}
                description={plugin.data.description}
                href={`/plugins/${plugin.slug}`}
                tags={plugin.data.tags}
              />
            </div>
          ))}
        </div>
      ) : (
        <p class="text-ink/60 font-header text-xl">Coming soon...</p>
      )}
    </section>
  </div>
</BaseLayout>

<style>
  .writing-mode-vertical {
    writing-mode: vertical-rl;
  }
</style>
```

**Step 2: Test plugins page**

Run: `npm run dev`
Visit: `/plugins`
Expected:
- Vertical "TOOLS" label on left (desktop)
- Grid of product cards
- Cards reveal on scroll
- Section number "01"

**Step 3: Commit**

```bash
git add src/pages/plugins/index.astro
git commit -m "feat: redesign plugins index with editorial layout"
```

---

## Task 16: Blog Index Page Redesign

**Files:**
- Modify: `src/pages/blog/index.astro`

**Step 1: Redesign blog index**

```astro
---
// src/pages/blog/index.astro
import BaseLayout from '../../layouts/BaseLayout.astro';
import BlogCard from '../../components/BlogCard.astro';
import { getCollection } from 'astro:content';

const posts = (await getCollection('blog')).sort(
  (a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf()
);
---

<BaseLayout title="Blog" description="Thoughts on AI-assisted development and Claude Code">
  <section class="max-w-[1280px] mx-auto px-6 py-xl relative">
    <span class="section-number absolute right-0 top-0" aria-hidden="true">01</span>

    <div class="mb-xl">
      <h1 class="font-display text-mega text-ink mb-4">
        Blog
      </h1>
      <p class="text-body text-ink/70 max-w-2xl">
        Thoughts on AI-assisted development, plugin building, and making the most of Claude Code.
      </p>
    </div>

    {posts.length > 0 ? (
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {posts.map((post, index) => (
          <div class="reveal">
            <BlogCard
              title={post.data.title}
              excerpt={post.data.description}
              href={`/blog/${post.slug}`}
              date={post.data.pubDate.toISOString()}
              readTime={post.data.readTime}
            />
          </div>
        ))}
      </div>
    ) : (
      <p class="text-ink/60 font-header text-xl">Posts coming soon...</p>
    )}
  </section>
</BaseLayout>
```

**Step 2: Test blog index**

Run: `npm run dev`
Visit: `/blog`
Expected: Grid of blog cards with section number

**Step 3: Commit**

```bash
git add src/pages/blog/index.astro
git commit -m "feat: redesign blog index with editorial grid layout"
```

---

## Task 17: Blog Post Layout Redesign

**Files:**
- Modify: `src/layouts/BlogPost.astro`
- Create: `src/components/PullQuote.astro`

**Step 1: Create PullQuote component**

```astro
---
// src/components/PullQuote.astro
interface Props {
  quote: string;
  cite?: string;
}

const { quote, cite } = Astro.props;
---

<aside class="pull-quote my-xl -ml-16 max-w-md">
  <div class="relative transform -rotate-2 border-l-4 border-orange pl-6 py-4 bg-surface">
    <blockquote class="font-header text-headline text-ink leading-tight">
      "{quote}"
    </blockquote>
    {cite && (
      <cite class="block mt-4 text-caption text-ink/60 font-body not-italic">
        — {cite}
      </cite>
    )}
  </div>
</aside>

<style>
  @media (max-width: 768px) {
    .pull-quote {
      margin-left: 0;
      transform: none;
    }
  }
</style>
```

**Step 2: Redesign blog post layout**

```astro
---
// src/layouts/BlogPost.astro
import BaseLayout from './BaseLayout.astro';

interface Props {
  title: string;
  description: string;
  pubDate: Date;
  author?: string;
  readTime?: string;
}

const { title, description, pubDate, author, readTime } = Astro.props;
---

<BaseLayout title={title} description={description}>
  <article class="blog-post">
    <!-- Header -->
    <header class="border-b-2 border-ink/10 bg-orange-tint">
      <div class="max-w-[1280px] mx-auto px-6 py-xl">
        <div class="max-w-3xl">
          <h1 class="font-header text-mega text-ink mb-6 uppercase leading-tight">
            {title}
          </h1>
          <p class="text-display text-ink/70 mb-6 leading-relaxed">
            {description}
          </p>
          <div class="flex items-center gap-4 text-caption text-ink/50 font-mono">
            <time datetime={pubDate.toISOString()}>
              {pubDate.toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric' })}
            </time>
            {readTime && <span>• {readTime}</span>}
            {author && <span>• {author}</span>}
          </div>
        </div>
      </div>
    </header>

    <!-- Content -->
    <div class="max-w-[1280px] mx-auto px-6 py-xl">
      <div class="prose-ch47 max-w-3xl mx-auto">
        <slot />
      </div>
    </div>
  </article>
</BaseLayout>

<style is:global>
  .prose-ch47 {
    color: var(--ink);
    font-family: var(--font-body);
    font-size: var(--text-body);
    line-height: 1.7;
  }

  .prose-ch47 h2 {
    font-family: var(--font-header);
    font-size: var(--text-display);
    text-transform: uppercase;
    letter-spacing: 0.02em;
    margin-top: 3rem;
    margin-bottom: 1.5rem;
    color: var(--ink);
  }

  .prose-ch47 h3 {
    font-family: var(--font-header);
    font-size: var(--text-headline);
    text-transform: uppercase;
    letter-spacing: 0.02em;
    margin-top: 2rem;
    margin-bottom: 1rem;
    color: var(--ink);
  }

  .prose-ch47 p {
    margin-bottom: 1.5rem;
  }

  .prose-ch47 a {
    color: var(--ink);
    position: relative;
    text-decoration: none;
  }

  .prose-ch47 a::after {
    content: '';
    position: absolute;
    bottom: 0.1em;
    left: -0.1em;
    right: -0.1em;
    height: 0.3em;
    background: var(--orange);
    opacity: 0.3;
    z-index: -1;
    transition: opacity 0.2s ease;
  }

  .prose-ch47 a:hover::after {
    opacity: 0.5;
  }

  .prose-ch47 code {
    font-family: var(--font-mono);
    font-size: 0.9em;
    background: var(--surface);
    padding: 0.2em 0.4em;
    border: 1px solid var(--ink);
    border-radius: 0;
  }

  .prose-ch47 pre {
    font-family: var(--font-mono);
    background: var(--surface);
    border: 2px solid var(--ink);
    padding: 1.5rem;
    overflow-x: auto;
    margin: 2rem 0;
    position: relative;
  }

  .prose-ch47 pre code {
    background: none;
    border: none;
    padding: 0;
  }

  /* Grain texture on code blocks */
  .prose-ch47 pre::before {
    content: '';
    position: absolute;
    inset: 0;
    background: url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxmaWx0ZXIgaWQ9ImEiPjxmZVR1cmJ1bGVuY2UgYmFzZUZyZXF1ZW5jeT0iLjgiIG51bU9jdGF2ZXM9IjQiLz48L2ZpbHRlcj48cmVjdCB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiBmaWx0ZXI9InVybCgjYSkiLz48L3N2Zz4=');
    opacity: 0.02;
    pointer-events: none;
  }

  .prose-ch47 ul, .prose-ch47 ol {
    margin: 1.5rem 0;
    padding-left: 2rem;
  }

  .prose-ch47 li {
    margin-bottom: 0.5rem;
  }

  .prose-ch47 blockquote {
    border-left: 4px solid var(--orange);
    padding-left: 1.5rem;
    margin: 2rem 0;
    font-style: italic;
    color: var(--ink);
    opacity: 0.8;
  }

  .prose-ch47 img {
    width: 100%;
    margin: 2rem 0;
    border: 2px solid var(--ink);
  }
</style>
```

**Step 3: Test blog post layout**

Run: `npm run dev`
Create a test blog post
Expected:
- Hero with orange tint background
- Wide margins (max 720px content)
- Orange highlighter on links
- Code blocks with grain texture
- Typography hierarchy with Staatliches

**Step 4: Commit**

```bash
git add src/layouts/BlogPost.astro src/components/PullQuote.astro
git commit -m "feat: redesign blog post layout with editorial styling"
```

---

## Task 18: About Page Redesign

**Files:**
- Modify: `src/pages/about.astro`

**Step 1: Redesign about page**

```astro
---
// src/pages/about.astro
import BaseLayout from '../layouts/BaseLayout.astro';
---

<BaseLayout title="About" description="About CH47 and the creator">
  <section class="max-w-[1280px] mx-auto px-6 py-xl relative">
    <span class="section-number absolute right-0 top-0" aria-hidden="true">01</span>

    <div class="grid grid-cols-1 lg:grid-cols-2 gap-xl items-start">
      <!-- Left column - WHO -->
      <div class="reveal">
        <span class="font-header text-display text-orange opacity-50 uppercase tracking-widest">Who</span>
        <h1 class="font-display text-mega text-ink mt-4 mb-6">
          About CH47
        </h1>
        <div class="prose-ch47">
          <p>
            CH47 is a curated directory of tools for Claude Code power users. Built by developers,
            for developers who want to push the boundaries of AI-assisted development.
          </p>
          <p>
            We focus on quality over quantity—every plugin, skill, and MCP server is tested and
            vetted to ensure it actually makes your workflow better.
          </p>
        </div>
      </div>

      <!-- Right column - placeholder for image -->
      <div class="reveal" style="animation-delay: 0.2s">
        <div class="aspect-square bg-surface border-2 border-ink halftone"></div>
      </div>
    </div>
  </section>

  <section class="border-t-2 border-ink/10 bg-surface/50">
    <div class="max-w-[1280px] mx-auto px-6 py-xl relative">
      <span class="section-number absolute right-0 top-0" aria-hidden="true">02</span>

      <div class="max-w-3xl reveal">
        <span class="font-header text-display text-orange opacity-50 uppercase tracking-widest">What</span>
        <h2 class="font-display text-display text-ink mt-4 mb-6">
          What We Offer
        </h2>
        <div class="prose-ch47">
          <p>
            Our directory includes plugins, skills, MCP servers, and prompts. Each tool is
            documented with clear installation instructions, usage examples, and real-world
            use cases.
          </p>
          <p>
            We also publish tutorials and guides on building your own tools, helping you
            contribute to the growing Claude Code ecosystem.
          </p>
        </div>
      </div>
    </div>
  </section>

  <section class="border-t-2 border-ink/10">
    <div class="max-w-[1280px] mx-auto px-6 py-xl relative">
      <span class="section-number absolute right-0 top-0" aria-hidden="true">03</span>

      <div class="max-w-3xl reveal">
        <span class="font-header text-display text-orange opacity-50 uppercase tracking-widest">Why</span>
        <h2 class="font-display text-display text-ink mt-4 mb-6">
          Our Mission
        </h2>
        <div class="prose-ch47">
          <p>
            Claude Code is powerful, but it's even better with the right tools. We believe
            in making those tools easy to discover and adopt.
          </p>
          <p>
            By curating the best resources and building our own, we're helping developers
            work smarter, not harder.
          </p>
        </div>
      </div>
    </div>
  </section>
</BaseLayout>

<style>
  .prose-ch47 p {
    font-size: var(--text-body);
    line-height: 1.7;
    color: var(--ink);
    margin-bottom: 1.5rem;
  }

  .prose-ch47 p:last-child {
    margin-bottom: 0;
  }
</style>
```

**Step 2: Test about page**

Run: `npm run dev`
Visit: `/about`
Expected:
- Three sections with WHO/WHAT/WHY labels
- Section numbers 01, 02, 03
- Scroll reveals
- Placeholder for image with halftone

**Step 3: Commit**

```bash
git add src/pages/about.astro
git commit -m "feat: redesign about page with editorial sections"
```

---

## Task 19: Accessibility - Focus States

**Files:**
- Modify: `src/styles/global.css`

**Step 1: Add focus-visible styles**

```css
/* Add to @layer base in global.css */
*:focus-visible {
  outline: 2px solid var(--orange);
  outline-offset: 4px;
}

/* Skip link for accessibility */
.skip-link {
  position: absolute;
  top: -100px;
  left: 0;
  background: var(--orange);
  color: var(--bg-base);
  padding: 12px 24px;
  font-family: var(--font-header);
  text-transform: uppercase;
  z-index: 10000;
  transition: top 0.2s ease;
}

.skip-link:focus {
  top: 0;
}
```

**Step 2: Add skip link to BaseLayout**

```html
<!-- Add at start of body in BaseLayout.astro -->
<a href="#main-content" class="skip-link">Skip to main content</a>
```

**Step 3: Add id to main element**

```html
<main class="flex-1" id="main-content">
```

**Step 4: Test accessibility**

Run: `npm run dev`
Press Tab key
Expected:
- Focus states visible with orange outline
- Skip link appears on Tab
- Keyboard navigation works

**Step 5: Commit**

```bash
git add src/styles/global.css src/layouts/BaseLayout.astro
git commit -m "feat: add accessibility focus states and skip link"
```

---

## Task 20: Performance - Font Display Swap

**Files:**
- Modify: `src/styles/global.css`

**Step 1: Add font-display swap**

```css
/* Add to @layer base */
@font-face {
  font-family: 'Bungee Inline';
  font-display: swap;
}

@font-face {
  font-family: 'Staatliches';
  font-display: swap;
}

@font-face {
  font-family: 'IBM Plex Sans';
  font-display: swap;
}

@font-face {
  font-family: 'JetBrains Mono';
  font-display: swap;
}
```

**Step 2: Test font loading**

Run: `npm run dev`
Throttle network to Slow 3G in DevTools
Expected: System fonts shown first, then custom fonts swap in

**Step 3: Commit**

```bash
git add src/styles/global.css
git commit -m "perf: add font-display swap to prevent FOIT"
```

---

## Task 21: Testing - Visual Regression Check

**Files:**
- None (manual testing)

**Step 1: Test all pages in light mode**

Run: `npm run dev`
Visit each page:
- `/` - Homepage
- `/plugins` - Plugins index
- `/blog` - Blog index
- `/about` - About page

Check:
- Typography renders correctly (Bungee Inline, Staatliches, IBM Plex Sans)
- Colors match spec (#FAFAFA bg, #0A0A0A text, #FF6600 orange)
- Grain texture visible
- Section numbers visible
- Spacing looks correct
- Animations work

**Step 2: Test all pages in dark mode**

Click theme toggle
Check same pages:
- Background should be #0A0A0A
- Text should be #FAFAFA
- Orange should be #FF7722 (brighter)
- Grain opacity increased to 4%

**Step 3: Test responsive design**

Resize browser to mobile widths:
- 375px (mobile)
- 768px (tablet)
- 1280px (desktop)

Check:
- Typography scales responsively
- Grid collapses properly
- Section numbers scale down
- Navigation remains usable
- Custom cursor hidden on mobile

**Step 4: Test interactions**

- Header compresses on scroll
- Product cards lift on hover
- Orange accent bar slides in
- Theme toggle works
- Form inputs show focus state
- Links show orange highlight
- Custom cursor appears on desktop

**Step 5: Document any issues**

Create GitHub issues or note for fixes

---

## Task 22: Build & Production Test

**Files:**
- None (build testing)

**Step 1: Run production build**

```bash
npm run build
```

Expected: Build succeeds with no errors

**Step 2: Preview production build**

```bash
npm run preview
```

Expected: Site works identically to dev mode

**Step 3: Check Lighthouse scores**

Open DevTools > Lighthouse
Run audit for:
- Performance (target: 90+)
- Accessibility (target: 90+)
- Best Practices (target: 90+)
- SEO (target: 90+)

**Step 4: Fix any issues**

If scores are low, investigate and fix:
- Performance: optimize images, fonts, scripts
- Accessibility: check contrast, ARIA labels, keyboard nav
- Best Practices: HTTPS, console errors
- SEO: meta tags, semantic HTML

**Step 5: Commit any fixes**

```bash
git add .
git commit -m "fix: address Lighthouse performance/accessibility issues"
```

---

## Task 23: Documentation - Design System

**Files:**
- Create: `docs/design-system.md`

**Step 1: Create design system documentation**

```markdown
# CH47 Design System

Quick reference for developers working on CH47.

## Colors

### Light Mode
- Background: `var(--bg-base)` (#FAFAFA)
- Text: `var(--ink)` (#0A0A0A)
- Surface: `var(--surface)` (#F0F0F0)
- Accent: `var(--orange)` (#FF6600)
- Tint: `var(--orange-tint)` (#FFF3ED)

### Dark Mode
- Background: `var(--bg-base)` (#0A0A0A)
- Text: `var(--ink)` (#FAFAFA)
- Surface: `var(--surface)` (#1A1A1A)
- Accent: `var(--orange)` (#FF7722)
- Tint: `var(--orange-tint)` (#1A0F0A)

## Typography

### Fonts
- Display: Bungee Inline - `font-display`
- Headers: Staatliches - `font-header`
- Body: IBM Plex Sans - `font-body`
- Mono: JetBrains Mono - `font-mono`

### Sizes
- Mega: `text-mega` (72px / 4.5rem)
- Display: `text-display` (48px / 3rem)
- Headline: `text-headline` (32px / 2rem)
- Body: `text-body` (18px / 1.125rem)
- Caption: `text-caption` (14px / 0.875rem)

## Spacing

- Micro: 8px
- Small: 16px
- Medium: 32px
- Large: 48px
- XL: 80px
- 2XL: 120px
- 3XL: 160px

## Components

### ProductCard
```astro
<ProductCard
  title="Tool Name"
  description="Brief description..."
  href="/plugins/tool-slug"
  tags={['skill', 'plugin']}
/>
```

### BlogCard
```astro
<BlogCard
  title="Post Title"
  excerpt="Post excerpt..."
  href="/blog/post-slug"
  date="2025-12-20"
  readTime="5 min read"
/>
```

### EmailSignup
```astro
<EmailSignup
  title="Stay updated"
  description="Get notified..."
  source="homepage"
/>
```

### PullQuote
```astro
<PullQuote
  quote="Important quote text"
  cite="Source Name"
/>
```

## Effects

### Halftone
```html
<div class="halftone">...</div>
```

### Highlight
```html
<span class="highlight">highlighted text</span>
```

### Section Number
```html
<span class="section-number" aria-hidden="true">01</span>
```

### Scroll Reveal
```html
<div class="reveal">...</div>
```

## Buttons

### Primary
```html
<button class="btn-brutalist btn-primary">Click me</button>
```

### Secondary
```html
<button class="btn-brutalist">Click me</button>
```

## Forms

### Input
```html
<input type="text" class="input-brutalist" />
```

### Textarea
```html
<textarea class="input-brutalist"></textarea>
```

## Best Practices

1. **Use CSS variables** for colors and spacing
2. **Prefer Tailwind classes** when available
3. **Add `.reveal` class** for scroll animations
4. **Use semantic HTML** for accessibility
5. **Test both light and dark modes**
6. **Check mobile responsiveness**
7. **Respect `prefers-reduced-motion`**
```

**Step 2: Commit documentation**

```bash
git add docs/design-system.md
git commit -m "docs: add design system quick reference"
```

---

## Task 24: Final Polish - Animation Timing

**Files:**
- Modify: `src/styles/global.css`

**Step 1: Fine-tune animation timing**

Review all animations:
- Page load sequence should feel orchestrated
- Scroll reveals should be smooth
- Hover effects should be snappy (300ms)
- Theme toggle transition should be seamless (300ms)

Adjust if needed:

```css
/* Example adjustments */
.animate-fade-in-up {
  animation: fadeInUp 0.6s cubic-bezier(0.34, 1.56, 0.64, 1) both;
}

/* Ensure consistent transition timing */
.product-card .card-inner,
.blog-card .card-inner,
.btn-brutalist,
.input-brutalist {
  transition-duration: 0.3s;
  transition-timing-function: ease-out;
}
```

**Step 2: Test all animations**

Run through all interactions:
- Page load
- Scroll reveals
- Hover effects
- Theme toggle
- Form focus states

**Step 3: Commit final polish**

```bash
git add src/styles/global.css
git commit -m "polish: fine-tune animation timing for consistency"
```

---

## Task 25: Final Build & Deployment Check

**Files:**
- None (final checks)

**Step 1: Clean build**

```bash
rm -rf dist .astro
npm run build
```

Expected: Clean build with no warnings

**Step 2: Final preview**

```bash
npm run preview
```

Test every page one more time:
- Light/dark mode
- All interactions
- Mobile responsiveness
- Performance

**Step 3: Check bundle size**

```bash
ls -lh dist/_astro/
```

Expected: Reasonable bundle sizes (<100KB for CSS, reasonable JS)

**Step 4: Final commit**

```bash
git add .
git commit -m "chore: final build verification for CH47 redesign"
```

**Step 5: Tag release**

```bash
git tag -a v2.0.0 -m "CH47 visual redesign - street magazine aesthetics"
git push origin v2.0.0
```

---

## Success Criteria

After completing all tasks, verify:

- ✅ All pages use new CH47 typography (Bungee Inline, Staatliches, IBM Plex Sans)
- ✅ Color system uses CSS variables with light/dark mode support
- ✅ Grain texture overlay visible on all backgrounds
- ✅ Chromatic offset effect on CH47 logo
- ✅ Brutalist form styling applied
- ✅ Section numbers visible on all pages
- ✅ Scroll animations work smoothly
- ✅ Custom cursor on desktop (hidden on mobile)
- ✅ Theme toggle persists preference
- ✅ Header compresses on scroll
- ✅ All hover states work (orange accents, lifts, shadows)
- ✅ Focus states visible for keyboard navigation
- ✅ Mobile responsive at 375px, 768px, 1280px
- ✅ Lighthouse scores 90+ across all metrics
- ✅ Build succeeds with no errors
- ✅ Design system documented

## Maintenance Notes

**Adding new components:**
1. Use CSS variables for colors/spacing
2. Add `.reveal` class for scroll animations
3. Follow brutalist styling (thick borders, no radius)
4. Include hover states with orange accents
5. Test in both light and dark modes

**Modifying colors:**
- Update CSS variables in `global.css`
- Changes automatically apply to all components
- Test contrast ratios (WCAG AA minimum)

**Performance:**
- Keep fonts to 4 families max (already at limit)
- Optimize images before adding
- Use lazy loading for images
- Minimize JavaScript (prefer CSS)

---

**Plan Version:** 1.0
**Created:** 2025-12-20
**Status:** Ready for Implementation
