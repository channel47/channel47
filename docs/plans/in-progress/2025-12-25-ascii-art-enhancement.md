# ASCII Art Enhancement Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Systematically enhance Channel 47 site with bold ASCII art elements—block text headers for landmarks, zen-inspired organic art pieces—while maintaining minimal aesthetic with lots of white space.

**Architecture:** Pre-generate ASCII art assets as .txt files, build two new Astro components (AsciiHeader for functional headers, AsciiArt for decorative pieces), integrate systematically across all pages with scroll-triggered fade-in animations.

**Tech Stack:** Astro, CSS, ascii-art skill (for generation), Intersection Observer (for animations)

---

## Task 1: Create ASCII Assets Directory Structure

**Files:**
- Create: `src/ascii-assets/headers/` (directory)
- Create: `src/ascii-assets/art/` (directory)

**Step 1: Create headers directory**

Run:
```bash
mkdir -p src/ascii-assets/headers
```

Expected: Directory created at `src/ascii-assets/headers/`

**Step 2: Create art directory**

Run:
```bash
mkdir -p src/ascii-assets/art
```

Expected: Directory created at `src/ascii-assets/art/`

**Step 3: Commit directory structure**

```bash
touch src/ascii-assets/headers/.gitkeep src/ascii-assets/art/.gitkeep
git add src/ascii-assets/
git commit -m "feat: add ASCII assets directory structure"
```

---

## Task 2: Generate Block Text Header - TOOLS

**Files:**
- Create: `src/ascii-assets/headers/tools.txt`

**Step 1: Generate ASCII art using ascii-art skill**

Use the ascii-art skill to generate "TOOLS" in block style.

Prompt: Generate the word "TOOLS" in block/banner style ASCII art

**Step 2: Save to file**

Copy the generated ASCII art and save it to `src/ascii-assets/headers/tools.txt`

**Step 3: Verify file contents**

Run:
```bash
cat src/ascii-assets/headers/tools.txt
```

Expected: File contains block-style ASCII art for "TOOLS"

**Step 4: Commit**

```bash
git add src/ascii-assets/headers/tools.txt
git commit -m "feat: add TOOLS block header ASCII art"
```

---

## Task 3: Generate Block Text Header - BLOG

**Files:**
- Create: `src/ascii-assets/headers/blog.txt`

**Step 1: Generate ASCII art**

Use ascii-art skill to generate "BLOG" in block style.

Prompt: Generate the word "BLOG" in block/banner style ASCII art

**Step 2: Save to file**

Save generated art to `src/ascii-assets/headers/blog.txt`

**Step 3: Verify file contents**

Run:
```bash
cat src/ascii-assets/headers/blog.txt
```

Expected: File contains block-style ASCII art for "BLOG"

**Step 4: Commit**

```bash
git add src/ascii-assets/headers/blog.txt
git commit -m "feat: add BLOG block header ASCII art"
```

---

## Task 4: Generate Block Text Header - LATEST

**Files:**
- Create: `src/ascii-assets/headers/latest.txt`

**Step 1: Generate ASCII art**

Use ascii-art skill to generate "LATEST" in block style.

Prompt: Generate the word "LATEST" in block/banner style ASCII art

**Step 2: Save to file**

Save generated art to `src/ascii-assets/headers/latest.txt`

**Step 3: Verify file contents**

Run:
```bash
cat src/ascii-assets/headers/latest.txt
```

Expected: File contains block-style ASCII art for "LATEST"

**Step 4: Commit**

```bash
git add src/ascii-assets/headers/latest.txt
git commit -m "feat: add LATEST block header ASCII art"
```

---

## Task 5: Generate Block Text Header - SUBSCRIBE

**Files:**
- Create: `src/ascii-assets/headers/subscribe.txt`

**Step 1: Generate ASCII art**

Use ascii-art skill to generate "SUBSCRIBE" in block style.

Prompt: Generate the word "SUBSCRIBE" in block/banner style ASCII art

**Step 2: Save to file**

Save generated art to `src/ascii-assets/headers/subscribe.txt`

**Step 3: Verify file contents**

Run:
```bash
cat src/ascii-assets/headers/subscribe.txt
```

Expected: File contains block-style ASCII art for "SUBSCRIBE"

**Step 4: Commit**

```bash
git add src/ascii-assets/headers/subscribe.txt
git commit -m "feat: add SUBSCRIBE block header ASCII art"
```

---

## Task 6: Generate Zen Art - Hero Bird

**Files:**
- Create: `src/ascii-assets/art/hero-bird.txt`

**Step 1: Generate ASCII art**

Use ascii-art skill to generate minimalist bird in flight (8-12 lines tall).

Prompt: Generate a minimalist zen-style bird in flight, clean lines, 8-12 lines tall, ASCII art using minimal style

**Step 2: Save to file**

Save generated art to `src/ascii-assets/art/hero-bird.txt`

**Step 3: Verify file contents**

Run:
```bash
cat src/ascii-assets/art/hero-bird.txt
```

Expected: File contains minimalist bird ASCII art, ~8-12 lines

**Step 4: Commit**

```bash
git add src/ascii-assets/art/hero-bird.txt
git commit -m "feat: add hero bird zen ASCII art"
```

---

## Task 7: Generate Zen Art - Tree Silhouette

**Files:**
- Create: `src/ascii-assets/art/tree-silhouette.txt`

**Step 1: Generate ASCII art**

Use ascii-art skill to generate simple tree silhouette (6-8 lines tall).

Prompt: Generate a minimalist zen-style tree silhouette, simple and clean, 6-8 lines tall, ASCII art using minimal style

**Step 2: Save to file**

Save generated art to `src/ascii-assets/art/tree-silhouette.txt`

**Step 3: Verify file contents**

Run:
```bash
cat src/ascii-assets/art/tree-silhouette.txt
```

Expected: File contains tree silhouette ASCII art, ~6-8 lines

**Step 4: Commit**

```bash
git add src/ascii-assets/art/tree-silhouette.txt
git commit -m "feat: add tree silhouette zen ASCII art"
```

---

## Task 8: Generate Zen Art - Plugin Background (Terminal + Plant)

**Files:**
- Create: `src/ascii-assets/art/plugin-background.txt`

**Step 1: Generate ASCII art**

Use ascii-art skill to generate terminal window with plant/sprout growing from it (20-30 lines).

Prompt: Generate a minimalist zen-style terminal window with a small plant or sprout growing out of it, symbolizing growth and technology, 20-30 lines tall, ASCII art using minimal style

**Step 2: Save to file**

Save generated art to `src/ascii-assets/art/plugin-background.txt`

**Step 3: Verify file contents**

Run:
```bash
cat src/ascii-assets/art/plugin-background.txt
```

Expected: File contains terminal+plant ASCII art, ~20-30 lines

**Step 4: Commit**

```bash
git add src/ascii-assets/art/plugin-background.txt
git commit -m "feat: add plugin background terminal+plant zen ASCII art"
```

---

## Task 9: Generate Zen Art - Blog Bird

**Files:**
- Create: `src/ascii-assets/art/blog-bird.txt`

**Step 1: Generate ASCII art**

Use ascii-art skill to generate small bird (5 lines tall).

Prompt: Generate a minimalist zen-style small bird, clean and simple, 5 lines tall, ASCII art using minimal style

**Step 2: Save to file**

Save generated art to `src/ascii-assets/art/blog-bird.txt`

**Step 3: Verify file contents**

Run:
```bash
cat src/ascii-assets/art/blog-bird.txt
```

Expected: File contains small bird ASCII art, ~5 lines

**Step 4: Commit**

```bash
git add src/ascii-assets/art/blog-bird.txt
git commit -m "feat: add blog bird zen ASCII art"
```

---

## Task 10: Generate Zen Art - Blog Leaf

**Files:**
- Create: `src/ascii-assets/art/blog-leaf.txt`

**Step 1: Generate ASCII art**

Use ascii-art skill to generate leaf (4 lines tall).

Prompt: Generate a minimalist zen-style leaf, simple and clean, 4 lines tall, ASCII art using minimal style

**Step 2: Save to file**

Save generated art to `src/ascii-assets/art/blog-leaf.txt`

**Step 3: Verify file contents**

Run:
```bash
cat src/ascii-assets/art/blog-leaf.txt
```

Expected: File contains leaf ASCII art, ~4 lines

**Step 4: Commit**

```bash
git add src/ascii-assets/art/blog-leaf.txt
git commit -m "feat: add blog leaf zen ASCII art"
```

---

## Task 11: Generate Zen Art - Blog Mountain

**Files:**
- Create: `src/ascii-assets/art/blog-mountain.txt`

**Step 1: Generate ASCII art**

Use ascii-art skill to generate mountain peak (6 lines tall).

Prompt: Generate a minimalist zen-style mountain peak, clean lines, 6 lines tall, ASCII art using minimal style

**Step 2: Save to file**

Save generated art to `src/ascii-assets/art/blog-mountain.txt`

**Step 3: Verify file contents**

Run:
```bash
cat src/ascii-assets/art/blog-mountain.txt
```

Expected: File contains mountain ASCII art, ~6 lines

**Step 4: Commit**

```bash
git add src/ascii-assets/art/blog-mountain.txt
git commit -m "feat: add blog mountain zen ASCII art"
```

---

## Task 12: Generate Zen Art - Email Icon

**Files:**
- Create: `src/ascii-assets/art/email-icon.txt`

**Step 1: Generate ASCII art**

Use ascii-art skill to generate envelope or paper plane (4 lines tall).

Prompt: Generate a minimalist zen-style envelope or paper plane, playful but simple, 4 lines tall, ASCII art using minimal style

**Step 2: Save to file**

Save generated art to `src/ascii-assets/art/email-icon.txt`

**Step 3: Verify file contents**

Run:
```bash
cat src/ascii-assets/art/email-icon.txt
```

Expected: File contains email icon ASCII art, ~4 lines

**Step 4: Commit**

```bash
git add src/ascii-assets/art/email-icon.txt
git commit -m "feat: add email icon zen ASCII art"
```

---

## Task 13: Generate Zen Art - About Scene

**Files:**
- Create: `src/ascii-assets/art/about-scene.txt`

**Step 1: Generate ASCII art**

Use ascii-art skill to generate contemplative scene (meditation stone or minimal landscape, 10-15 lines).

Prompt: Generate a minimalist zen-style contemplative scene like a meditation stone or minimal landscape, peaceful and personal, 10-15 lines tall, ASCII art using minimal style

**Step 2: Save to file**

Save generated art to `src/ascii-assets/art/about-scene.txt`

**Step 3: Verify file contents**

Run:
```bash
cat src/ascii-assets/art/about-scene.txt
```

Expected: File contains about scene ASCII art, ~10-15 lines

**Step 4: Commit**

```bash
git add src/ascii-assets/art/about-scene.txt
git commit -m "feat: add about scene zen ASCII art"
```

---

## Task 14: Create AsciiHeader Component Styles

**Files:**
- Create: `src/styles/components/ascii-header.css`

**Step 1: Create stylesheet**

Create file with the following content:

```css
/* ASCII Header Component Styles */

.ascii-header {
  font-family: 'JetBrains Mono', monospace;
  color: var(--color-text);
  line-height: 1;
  white-space: pre;
  margin: 0;
  padding: 0;
}

.ascii-header--left {
  text-align: left;
}

.ascii-header--center {
  text-align: center;
}

.ascii-header--right {
  text-align: right;
}

/* Responsive sizing */
.ascii-header {
  font-size: clamp(1.5rem, 4vw, 2.5rem);
}

@media (min-width: 768px) {
  .ascii-header {
    font-size: clamp(2.5rem, 5vw, 4rem);
  }
}

/* Subtle gradient in dark mode (optional enhancement) */
@media (prefers-color-scheme: dark) {
  .ascii-header {
    background: linear-gradient(180deg, var(--color-text) 0%, var(--color-text-muted) 100%);
    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }
}
```

**Step 2: Verify file exists**

Run:
```bash
ls -la src/styles/components/ascii-header.css
```

Expected: File exists

**Step 3: Commit**

```bash
git add src/styles/components/ascii-header.css
git commit -m "feat: add AsciiHeader component styles"
```

---

## Task 15: Create AsciiHeader Component

**Files:**
- Create: `src/components/AsciiHeader.astro`

**Step 1: Create component file**

Create file with the following content:

```astro
---
// src/components/AsciiHeader.astro
// Renders pre-generated block-style ASCII text for main section headers
interface Props {
  text: 'TOOLS' | 'BLOG' | 'LATEST' | 'SUBSCRIBE';
  align?: 'left' | 'center' | 'right';
  level?: 'h1' | 'h2';
  ariaLabel?: string;
}

const { text, align = 'left', level = 'h2', ariaLabel } = Astro.props;

// Import ASCII art files
import toolsArt from '../ascii-assets/headers/tools.txt?raw';
import blogArt from '../ascii-assets/headers/blog.txt?raw';
import latestArt from '../ascii-assets/headers/latest.txt?raw';
import subscribeArt from '../ascii-assets/headers/subscribe.txt?raw';

const artMap: Record<string, string> = {
  TOOLS: toolsArt,
  BLOG: blogArt,
  LATEST: latestArt,
  SUBSCRIBE: subscribeArt,
};

const asciiArt = artMap[text];
const HeadingTag = level;
const label = ariaLabel || text;

import '../styles/components/ascii-header.css';
---

<HeadingTag
  class={`ascii-header ascii-header--${align}`}
  aria-label={label}
>
  {asciiArt}
</HeadingTag>
```

**Step 2: Verify file exists**

Run:
```bash
ls -la src/components/AsciiHeader.astro
```

Expected: File exists

**Step 3: Test component builds**

Run:
```bash
npm run build
```

Expected: Build succeeds without errors

**Step 4: Commit**

```bash
git add src/components/AsciiHeader.astro
git commit -m "feat: add AsciiHeader component"
```

---

## Task 16: Create AsciiArt Component Styles

**Files:**
- Create: `src/styles/components/ascii-art.css`

**Step 1: Create stylesheet**

Create file with the following content:

```css
/* ASCII Art Component Styles */

.ascii-art {
  font-family: 'JetBrains Mono', monospace;
  color: var(--color-text);
  line-height: 1;
  white-space: pre;
  margin: 0;
  padding: 0;
  user-select: none;
  pointer-events: none;
}

/* Position variants */
.ascii-art--hero {
  font-size: 1rem;
  opacity: 0.6;
}

.ascii-art--divider {
  font-size: 1rem;
  opacity: 0.5;
  text-align: center;
}

.ascii-art--sidebar {
  font-size: 1rem;
  opacity: 0.4;
}

.ascii-art--background {
  font-size: 1rem;
  opacity: 0.18;
  position: absolute;
  z-index: 0;
}

/* Responsive: hide background pieces on mobile */
@media (max-width: 767px) {
  .ascii-art--background {
    display: none;
  }
}

/* Custom opacity override */
.ascii-art[style*="--opacity"] {
  opacity: var(--opacity);
}
```

**Step 2: Verify file exists**

Run:
```bash
ls -la src/styles/components/ascii-art.css
```

Expected: File exists

**Step 3: Commit**

```bash
git add src/styles/components/ascii-art.css
git commit -m "feat: add AsciiArt component styles"
```

---

## Task 17: Create AsciiArt Component

**Files:**
- Create: `src/components/AsciiArt.astro`

**Step 1: Create component file**

Create file with the following content:

```astro
---
// src/components/AsciiArt.astro
// Displays decorative zen/organic ASCII pieces
interface Props {
  name: 'hero-bird' | 'tree-silhouette' | 'plugin-background' | 'blog-bird' | 'blog-leaf' | 'blog-mountain' | 'email-icon' | 'about-scene';
  position?: 'hero' | 'divider' | 'sidebar' | 'background';
  opacity?: number;
}

const { name, position = 'hero', opacity } = Astro.props;

// Import ASCII art files
import heroBird from '../ascii-assets/art/hero-bird.txt?raw';
import treeSilhouette from '../ascii-assets/art/tree-silhouette.txt?raw';
import pluginBackground from '../ascii-assets/art/plugin-background.txt?raw';
import blogBird from '../ascii-assets/art/blog-bird.txt?raw';
import blogLeaf from '../ascii-assets/art/blog-leaf.txt?raw';
import blogMountain from '../ascii-assets/art/blog-mountain.txt?raw';
import emailIcon from '../ascii-assets/art/email-icon.txt?raw';
import aboutScene from '../ascii-assets/art/about-scene.txt?raw';

const artMap: Record<string, string> = {
  'hero-bird': heroBird,
  'tree-silhouette': treeSilhouette,
  'plugin-background': pluginBackground,
  'blog-bird': blogBird,
  'blog-leaf': blogLeaf,
  'blog-mountain': blogMountain,
  'email-icon': emailIcon,
  'about-scene': aboutScene,
};

const asciiArt = artMap[name];
const style = opacity ? `--opacity: ${opacity}` : undefined;

import '../styles/components/ascii-art.css';
---

<figure
  class={`ascii-art ascii-art--${position}`}
  aria-hidden="true"
  style={style}
>
  {asciiArt}
</figure>
```

**Step 2: Verify file exists**

Run:
```bash
ls -la src/components/AsciiArt.astro
```

Expected: File exists

**Step 3: Test component builds**

Run:
```bash
npm run build
```

Expected: Build succeeds without errors

**Step 4: Commit**

```bash
git add src/components/AsciiArt.astro
git commit -m "feat: add AsciiArt component"
```

---

## Task 18: Create ASCII Animations Stylesheet

**Files:**
- Create: `src/styles/components/ascii-animations.css`

**Step 1: Create stylesheet**

Create file with the following content:

```css
/* ASCII Animations - Scroll-triggered fade-in */

.ascii-animate {
  opacity: 0;
  transform: translateY(10px);
  transition: opacity 250ms ease-out, transform 250ms ease-out;
}

.ascii-visible {
  opacity: 1 !important; /* Override component opacity after animation */
  transform: translateY(0);
}

/* Preserve component-specific opacity after animation */
.ascii-art--hero.ascii-visible {
  opacity: 0.6 !important;
}

.ascii-art--divider.ascii-visible {
  opacity: 0.5 !important;
}

.ascii-art--sidebar.ascii-visible {
  opacity: 0.4 !important;
}

.ascii-art--background.ascii-visible {
  opacity: 0.18 !important;
}

.ascii-header.ascii-visible {
  opacity: 1 !important;
}

/* Custom opacity values */
.ascii-art[style*="--opacity"].ascii-visible {
  opacity: var(--opacity) !important;
}
```

**Step 2: Verify file exists**

Run:
```bash
ls -la src/styles/components/ascii-animations.css
```

Expected: File exists

**Step 3: Commit**

```bash
git add src/styles/components/ascii-animations.css
git commit -m "feat: add ASCII animations stylesheet"
```

---

## Task 19: Integrate ASCII Elements into Homepage - Imports and Hero

**Files:**
- Modify: `src/pages/index.astro`

**Step 1: Read current homepage**

Run:
```bash
cat src/pages/index.astro
```

Note the current structure.

**Step 2: Add imports at top of frontmatter**

Add these imports after the existing imports:

```astro
import AsciiHeader from '../components/AsciiHeader.astro';
import AsciiArt from '../components/AsciiArt.astro';
import '../styles/components/ascii-animations.css';
```

**Step 3: Add hero bird to hero section**

Add the bird art inside the `home-hero` div, after the actions:

```astro
<div class="home-hero">
  <!-- existing h1, p, actions -->
  <div style="position: absolute; top: 2rem; right: 2rem;">
    <AsciiArt name="hero-bird" position="hero" />
  </div>
</div>
```

**Step 4: Verify changes**

Run:
```bash
npm run dev
```

Open browser, verify hero bird appears on homepage.

**Step 5: Commit**

```bash
git add src/pages/index.astro
git commit -m "feat: add hero bird to homepage"
```

---

## Task 20: Integrate ASCII Elements into Homepage - Blog Section

**Files:**
- Modify: `src/pages/index.astro:27-32`

**Step 1: Replace blog section header**

Replace the existing `<h2 class="section-title">Latest from the blog</h2>` with:

```astro
<AsciiHeader text="LATEST" align="center" level="h2" ariaLabel="Latest from the blog" />
<div style="margin-top: 2rem; text-align: center;">
  <AsciiArt name="tree-silhouette" position="divider" />
</div>
```

**Step 2: Verify changes**

Run:
```bash
npm run dev
```

Open browser, verify ASCII header and tree appear in blog section.

**Step 3: Commit**

```bash
git add src/pages/index.astro
git commit -m "feat: add ASCII header and tree to blog section"
```

---

## Task 21: Integrate ASCII Elements into Homepage - Email Signup

**Files:**
- Modify: `src/pages/index.astro:34-44`
- Modify: `src/components/EmailSignup.astro`

**Step 1: Read EmailSignup component**

Run:
```bash
cat src/components/EmailSignup.astro
```

Note the structure.

**Step 2: Update EmailSignup to optionally hide title**

Modify `src/components/EmailSignup.astro` to add a `hideTitle` prop:

```astro
interface Props {
  title: string;
  description: string;
  source: string;
  hideTitle?: boolean;
}

const { title, description, source, hideTitle = false } = Astro.props;
```

Then conditionally render the title:

```astro
{!hideTitle && <h2 class="email-signup__title">{title}</h2>}
```

**Step 3: Update homepage to use AsciiHeader instead**

In `src/pages/index.astro`, replace the email signup section:

```astro
<section class="section-divider">
  <div class="home-section">
    <div style="max-width: 32rem; margin: 0 auto;">
      <div style="text-align: center; margin-bottom: 1.5rem;">
        <AsciiHeader text="SUBSCRIBE" align="center" level="h2" ariaLabel="Get notified when I add new tools" />
        <div style="margin-top: 1rem;">
          <AsciiArt name="email-icon" position="divider" opacity={0.6} />
        </div>
      </div>
      <EmailSignup
        title="Get notified when I add new tools"
        description="Usually once or twice a month. I only send updates when there's something genuinely useful."
        source="homepage"
        hideTitle={true}
      />
    </div>
  </div>
</section>
```

**Step 4: Verify changes**

Run:
```bash
npm run dev
```

Open browser, verify email section has ASCII header and icon.

**Step 5: Commit**

```bash
git add src/pages/index.astro src/components/EmailSignup.astro
git commit -m "feat: add ASCII header and icon to email signup section"
```

---

## Task 22: Add Animation Script to Homepage

**Files:**
- Modify: `src/pages/index.astro`

**Step 1: Add animation script at end of file**

Add this script tag at the very end of `src/pages/index.astro`, after the closing `</BaseLayout>`:

```astro
<script>
  // Scroll-triggered fade-in for ASCII elements
  const asciiElements = document.querySelectorAll('.ascii-header, .ascii-art');

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry, index) => {
        if (entry.isIntersecting) {
          // Stagger: headers first, then art pieces
          const isHeader = entry.target.classList.contains('ascii-header');
          const delay = isHeader ? index * 50 : index * 50 + 100;

          setTimeout(() => {
            entry.target.classList.add('ascii-visible');
            entry.target.classList.remove('ascii-animate');
          }, delay);
        }
      });
    },
    { threshold: 0.1 }
  );

  asciiElements.forEach((el) => {
    el.classList.add('ascii-animate');
    observer.observe(el);
  });
</script>
```

**Step 2: Verify animations work**

Run:
```bash
npm run dev
```

Open browser, scroll homepage, verify ASCII elements fade in smoothly.

**Step 3: Commit**

```bash
git add src/pages/index.astro
git commit -m "feat: add scroll-triggered animations to homepage ASCII elements"
```

---

## Task 23: Integrate ASCII Elements into Plugin Index - Header

**Files:**
- Modify: `src/pages/plugins/index.astro:70-79`

**Step 1: Add imports**

Add these imports to the frontmatter:

```astro
import AsciiHeader from '../../components/AsciiHeader.astro';
import AsciiArt from '../../components/AsciiArt.astro';
import '../../styles/components/ascii-animations.css';
```

**Step 2: Replace header**

Replace the existing header section with:

```astro
<header class="plugin-index__hero">
  <h1 class="plugin-index__title">
    <AsciiHeader text="TOOLS" align="left" level="h1" ariaLabel="Tools that work" />
    <span style="font-weight: 300; display: block; margin-top: 0.5rem;">that work</span>
  </h1>
  <p class="plugin-index__subtitle">
    Battle-tested Claude Code plugins from daily workflows. All free. Quality over quantity.
  </p>
</header>
```

**Step 3: Verify changes**

Run:
```bash
npm run dev
```

Navigate to `/plugins`, verify ASCII "TOOLS" header appears.

**Step 4: Commit**

```bash
git add src/pages/plugins/index.astro
git commit -m "feat: add ASCII TOOLS header to plugin index"
```

---

## Task 24: Integrate ASCII Elements into Plugin Index - Background

**Files:**
- Modify: `src/pages/plugins/index.astro:92-144`

**Step 1: Add background art before plugin spreads**

Add the background art wrapper around the plugin spreads grid:

```astro
<div style="position: relative;">
  <div style="position: absolute; top: 10%; left: 50%; transform: translateX(-50%); z-index: 0;">
    <AsciiArt name="plugin-background" position="background" />
  </div>

  <div class="plugin-spreads" style="position: relative; z-index: 1;">
    <!-- existing plugin spread loop -->
  </div>
</div>
```

**Step 2: Verify changes**

Run:
```bash
npm run dev
```

Navigate to `/plugins`, verify subtle background art appears behind grid (desktop only).

**Step 3: Commit**

```bash
git add src/pages/plugins/index.astro
git commit -m "feat: add background zen art to plugin index"
```

---

## Task 25: Add Animation Script to Plugin Index

**Files:**
- Modify: `src/pages/plugins/index.astro`

**Step 1: Add animation setup to existing script**

Find the existing `<script>` tag (around line 148) and add this code before the category filter code:

```javascript
// Scroll-triggered fade-in for ASCII elements
const asciiElements = document.querySelectorAll('.ascii-header, .ascii-art');

const asciiObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry, index) => {
      if (entry.isIntersecting) {
        const isHeader = entry.target.classList.contains('ascii-header');
        const delay = isHeader ? index * 50 : index * 50 + 100;

        setTimeout(() => {
          entry.target.classList.add('ascii-visible');
          entry.target.classList.remove('ascii-animate');
        }, delay);
      }
    });
  },
  { threshold: 0.1 }
);

asciiElements.forEach((el) => {
  el.classList.add('ascii-animate');
  asciiObserver.observe(el);
});

// Category filter functionality (existing code below)
```

**Step 2: Verify animations work**

Run:
```bash
npm run dev
```

Navigate to `/plugins`, verify ASCII elements animate in.

**Step 3: Commit**

```bash
git add src/pages/plugins/index.astro
git commit -m "feat: add animations to plugin index ASCII elements"
```

---

## Task 26: Integrate ASCII Elements into Blog Index

**Files:**
- Modify: `src/pages/blog/index.astro`

**Step 1: Read current blog index**

Run:
```bash
cat src/pages/blog/index.astro
```

**Step 2: Add imports**

Add imports to frontmatter:

```astro
import AsciiHeader from '../../components/AsciiHeader.astro';
import '../../styles/components/ascii-animations.css';
```

**Step 3: Replace blog header**

Replace the main blog header (likely an `<h1>`) with:

```astro
<AsciiHeader text="BLOG" align="center" level="h1" ariaLabel="Blog" />
```

**Step 4: Add animation script**

Add script at end of file:

```astro
<script>
  const asciiElements = document.querySelectorAll('.ascii-header');

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('ascii-visible');
          entry.target.classList.remove('ascii-animate');
        }
      });
    },
    { threshold: 0.1 }
  );

  asciiElements.forEach((el) => {
    el.classList.add('ascii-animate');
    observer.observe(el);
  });
</script>
```

**Step 5: Verify changes**

Run:
```bash
npm run dev
```

Navigate to `/blog`, verify ASCII "BLOG" header appears.

**Step 6: Commit**

```bash
git add src/pages/blog/index.astro
git commit -m "feat: add ASCII BLOG header to blog index"
```

---

## Task 27: Integrate ASCII Elements into Blog Posts

**Files:**
- Modify: `src/pages/blog/[...slug].astro`

**Step 1: Read current blog post template**

Run:
```bash
cat src/pages/blog/[...slug].astro
```

**Step 2: Add imports**

Add imports to frontmatter:

```astro
import AsciiArt from '../../components/AsciiArt.astro';
import '../../styles/components/ascii-animations.css';
```

**Step 3: Add rotating zen art at top of post**

Add art piece near the top of the post content (after title/meta, before body):

```astro
{/* Rotating zen art - use different piece based on simple rotation */}
<div style="text-align: center; margin: 2rem 0;">
  <AsciiArt
    name={['blog-bird', 'blog-leaf', 'blog-mountain'][Math.floor(Math.random() * 3)] as any}
    position="divider"
    opacity={0.5}
  />
</div>
```

**Step 4: Add animation script**

Add script at end of file:

```astro
<script>
  const asciiElements = document.querySelectorAll('.ascii-art');

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('ascii-visible');
          entry.target.classList.remove('ascii-animate');
        }
      });
    },
    { threshold: 0.1 }
  );

  asciiElements.forEach((el) => {
    el.classList.add('ascii-animate');
    observer.observe(el);
  });
</script>
```

**Step 5: Verify changes**

Run:
```bash
npm run dev
```

Navigate to a blog post, verify zen art appears.

**Step 6: Commit**

```bash
git add src/pages/blog/[...slug].astro
git commit -m "feat: add rotating zen art to blog posts"
```

---

## Task 28: Integrate ASCII Elements into About Page

**Files:**
- Modify: `src/pages/about.astro`

**Step 1: Read current about page**

Run:
```bash
cat src/pages/about.astro
```

**Step 2: Add imports**

Add imports to frontmatter:

```astro
import AsciiArt from '../components/AsciiArt.astro';
import '../styles/components/ascii-animations.css';
```

**Step 3: Add contemplative scene**

Add art piece in a prominent location (perhaps after intro paragraph):

```astro
<div style="text-align: center; margin: 3rem 0;">
  <AsciiArt name="about-scene" position="hero" opacity={0.5} />
</div>
```

**Step 4: Add animation script**

Add script at end of file:

```astro
<script>
  const asciiElements = document.querySelectorAll('.ascii-art');

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('ascii-visible');
          entry.target.classList.remove('ascii-animate');
        }
      });
    },
    { threshold: 0.1 }
  );

  asciiElements.forEach((el) => {
    el.classList.add('ascii-animate');
    observer.observe(el);
  });
</script>
```

**Step 5: Verify changes**

Run:
```bash
npm run dev
```

Navigate to `/about`, verify zen scene appears.

**Step 6: Commit**

```bash
git add src/pages/about.astro
git commit -m "feat: add contemplative zen scene to about page"
```

---

## Task 29: Test Responsive Behavior - Mobile

**Files:**
- Test: All integrated pages

**Step 1: Start dev server**

Run:
```bash
npm run dev
```

**Step 2: Open browser DevTools responsive mode**

Set viewport to mobile size (375px width).

**Step 3: Verify mobile behavior**

Check each page:
- Homepage: Hero bird visible, headers readable
- Plugins: Background art HIDDEN, headers readable
- Blog index: Header readable
- Blog posts: Art pieces visible
- About: Scene visible

Expected: Large background pieces hidden on mobile, everything else visible and readable.

**Step 4: Document findings**

If issues found, note them. Otherwise, proceed.

---

## Task 30: Test Responsive Behavior - Desktop

**Files:**
- Test: All integrated pages

**Step 1: Set viewport to desktop**

Set viewport to desktop size (1440px width).

**Step 2: Verify desktop behavior**

Check each page:
- Homepage: All art visible with proper spacing
- Plugins: Background art VISIBLE behind grid
- Blog: All elements visible
- About: Scene visible

Expected: All ASCII elements visible with good spacing.

**Step 3: Document findings**

Note any spacing/layout issues.

---

## Task 31: Test Dark Mode

**Files:**
- Test: All integrated pages in dark mode

**Step 1: Enable dark mode**

Toggle dark mode (system preference or site toggle).

**Step 2: Check opacity levels**

Verify all ASCII elements are visible with appropriate contrast:
- Headers should be clearly readable
- Art pieces should be subtle but visible
- Background pieces very subtle

**Step 3: Adjust opacity if needed**

If any elements are too faint or too bold in dark mode, adjust the opacity values in `src/styles/components/ascii-art.css` or component-specific styles.

Expected: All elements visible with good contrast in both light and dark modes.

**Step 4: Commit any adjustments**

```bash
git add src/styles/components/ascii-art.css
git commit -m "fix: adjust opacity for dark mode visibility"
```

---

## Task 32: Accessibility Testing - Screen Readers

**Files:**
- Test: All pages with screen reader

**Step 1: Enable screen reader**

Use VoiceOver (Mac), NVDA (Windows), or browser extensions.

**Step 2: Navigate each page**

Test:
- Homepage: Verify headers read as "Latest from the blog", "Get notified...", not ASCII characters
- Plugins: Verify reads as "Tools that work", not ASCII
- Blog: Verify reads as "Blog"
- Posts: Verify art pieces are ignored (aria-hidden)

Expected:
- Headers announce actual text via aria-label
- Decorative art is completely ignored
- No "random characters" announced

**Step 3: Document issues**

If screen reader announces ASCII characters, verify:
- Headers have proper `aria-label`
- Art pieces have `aria-hidden="true"`

**Step 4: Fix any issues and commit**

```bash
git add src/components/
git commit -m "fix: improve screen reader accessibility for ASCII elements"
```

---

## Task 33: Performance Testing

**Files:**
- Test: Build output and page load times

**Step 1: Run production build**

Run:
```bash
npm run build
```

Expected: Build succeeds without warnings.

**Step 2: Check bundle size**

Run:
```bash
du -sh dist/
```

Note the size. Compare to previous builds if available.

**Step 3: Test page load**

Run:
```bash
npm run preview
```

Open browser DevTools Network tab, test each page load time.

Expected: No significant performance impact (ASCII art is text-based, very lightweight).

**Step 4: Document findings**

Note any performance concerns.

---

## Task 34: Visual Balance Review

**Files:**
- Review: All pages for aesthetic quality

**Step 1: Review homepage**

Check:
- White space maintained
- ASCII elements add life without overwhelming
- Hierarchy clear

**Step 2: Review plugin index**

Check:
- Background subtle enough
- Header bold but not overpowering
- Plugin cards remain focus

**Step 3: Review blog pages**

Check:
- Headers clear
- Art pieces enhance without distraction

**Step 4: Review about page**

Check:
- Scene adds personality
- Text remains primary focus

**Step 5: Document findings**

Note any visual balance issues or areas that feel too crowded.

---

## Task 35: Final Build and Commit

**Files:**
- All modified files

**Step 1: Run final build**

Run:
```bash
npm run build
```

Expected: Build succeeds without errors or warnings.

**Step 2: Review git status**

Run:
```bash
git status
```

Verify all changes are committed.

**Step 3: Push to remote**

Run:
```bash
git push origin main
```

Expected: All commits pushed successfully.

**Step 4: Verify deployment**

If auto-deploy is configured, verify site deploys successfully to production.

---

## Success Criteria Checklist

After completing all tasks, verify:

- [ ] All ASCII assets generated and committed
- [ ] AsciiHeader component renders block text correctly
- [ ] AsciiArt component renders zen art correctly
- [ ] Homepage has hero bird, LATEST header, tree, SUBSCRIBE header, email icon
- [ ] Plugin index has TOOLS header and background zen art
- [ ] Blog index has BLOG header
- [ ] Blog posts have rotating zen art (bird/leaf/mountain)
- [ ] About page has contemplative scene
- [ ] Animations work smoothly on scroll
- [ ] Mobile hides large background pieces
- [ ] Dark mode opacity levels appropriate
- [ ] Screen readers announce proper text, ignore decorative art
- [ ] No performance degradation
- [ ] Visual balance maintained - bold ASCII without overwhelming content
- [ ] Site feels visually distinctive and sophisticated

---

**Implementation Notes:**

- Use @ascii-art skill for all ASCII generation
- DRY: Components handle all rendering logic
- YAGNI: No unnecessary features beyond spec
- Frequent commits: After each task completion
- Test as you go: Verify each integration before moving to next page
