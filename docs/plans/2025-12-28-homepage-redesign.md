# Homepage Redesign Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Redesign Channel 47 homepage with full-screen progressive disclosure layout inspired by Menerals.com, maintaining terminal DNA through subtle accents.

**Architecture:** Four full-screen sections (Hero, Gap, Plugin Showcase, Newsletter) using Intersection Observer for scroll-triggered animations. Native video, CSS animations, Astro components, progressive enhancement. No external animation libraries.

**Tech Stack:** Astro, TypeScript, CSS (clamp-based fluid typography), Intersection Observer API, Nano Banana (image generation)

**Reference:** See `docs/plans/2025-12-28-homepage-redesign-design.md` for complete design specification.

---

## Task 1: Analyze Menerals.com with Playwright

**Files:**
- None (exploration task)

**Step 1: Navigate to Menerals and capture screenshots**

Run Playwright to analyze reference site:
- Take full-page screenshot
- Capture hero section
- Capture scroll sections
- Note spacing, animations, transitions

Expected: Multiple screenshots saved to analyze layout patterns

**Step 2: Inspect CSS patterns**

Focus on:
- `clamp()` usage for fluid typography
- Section padding values
- Animation timing functions
- Scroll-trigger patterns
- Responsive breakpoints

Expected: Notes on exact CSS values and patterns to replicate

**Step 3: Document findings**

Create notes file with:
- Padding patterns: `clamp(min, preferred, max)` values
- Animation durations and easing
- Color overlay opacity values
- Breakpoint strategy

Expected: Clear reference for implementation

---

## Task 2: Create ASCII Art Assets

**Files:**
- Create: `src/ascii-assets/plugins/ascii-art.txt`
- Create: `src/ascii-assets/plugins/prompt.txt`
- Create: `src/ascii-assets/plugins/creative.txt`
- Create: `src/ascii-assets/plugins/google-ads.txt`

**Step 1: Create directory structure**

```bash
mkdir -p src/ascii-assets/plugins
```

Expected: Directory created

**Step 2: Generate ASCII ART block letters**

Use ASCII art generator or create manually in same style as WELCOME/LATEST.

Create `src/ascii-assets/plugins/ascii-art.txt`:
```
 █████╗ ███████╗ ██████╗██╗██╗     █████╗ ██████╗ ████████╗
██╔══██╗██╔════╝██╔════╝██║██║    ██╔══██╗██╔══██╗╚══██╔══╝
███████║███████╗██║     ██║██║    ███████║██████╔╝   ██║
██╔══██║╚════██║██║     ██║██║    ██╔══██║██╔══██╗   ██║
██║  ██║███████║╚██████╗██║██║    ██║  ██║██║  ██║   ██║
╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝╚═╝    ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝
```

**Step 3: Generate PROMPT block letters**

Create `src/ascii-assets/plugins/prompt.txt`:
```
██████╗ ██████╗  ██████╗ ███╗   ███╗██████╗ ████████╗
██╔══██╗██╔══██╗██╔═══██╗████╗ ████║██╔══██╗╚══██╔══╝
██████╔╝██████╔╝██║   ██║██╔████╔██║██████╔╝   ██║
██╔═══╝ ██╔══██╗██║   ██║██║╚██╔╝██║██╔═══╝    ██║
██║     ██║  ██║╚██████╔╝██║ ╚═╝ ██║██║        ██║
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝        ╚═╝
```

**Step 4: Generate CREATIVE block letters**

Create `src/ascii-assets/plugins/creative.txt`:
```
 ██████╗██████╗ ███████╗ █████╗ ████████╗██╗██╗   ██╗███████╗
██╔════╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██║██║   ██║██╔════╝
██║     ██████╔╝█████╗  ███████║   ██║   ██║██║   ██║█████╗
██║     ██╔══██╗██╔══╝  ██╔══██║   ██║   ██║╚██╗ ██╔╝██╔══╝
╚██████╗██║  ██║███████╗██║  ██║   ██║   ██║ ╚████╔╝ ███████╗
 ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═══╝  ╚══════╝
```

**Step 5: Generate GOOGLE ADS block letters (stacked)**

Create `src/ascii-assets/plugins/google-ads.txt`:
```
 ██████╗  ██████╗  ██████╗  ██████╗ ██╗     ███████╗
██╔════╝ ██╔═══██╗██╔═══██╗██╔════╝ ██║     ██╔════╝
██║  ███╗██║   ██║██║   ██║██║  ███╗██║     █████╗
██║   ██║██║   ██║██║   ██║██║   ██║██║     ██╔══╝
╚██████╔╝╚██████╔╝╚██████╔╝╚██████╔╝███████╗███████╗
 ╚═════╝  ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚══════╝

 █████╗ ██████╗ ███████╗
██╔══██╗██╔══██╗██╔════╝
███████║██║  ██║███████╗
██╔══██║██║  ██║╚════██║
██║  ██║██████╔╝███████║
╚═╝  ╚═╝╚═════╝ ╚══════╝
```

**Step 6: Verify all ASCII files**

```bash
ls -la src/ascii-assets/plugins/
cat src/ascii-assets/plugins/ascii-art.txt
```

Expected: All 4 files created, ASCII art displays correctly in terminal

**Step 7: Commit ASCII assets**

```bash
git add src/ascii-assets/plugins/
git commit -m "feat: add ASCII art block letters for plugin showcase"
```

---

## Task 3: Generate Nano Banana Images

**Files:**
- Output: `public/images/toolbox-minimal.png`
- Output: `public/images/toolbox-complete.png`
- Output: `public/images/signal-icon.png`

**Step 1: Create images directory**

```bash
mkdir -p public/images
```

Expected: Directory created

**Step 2: Generate minimal toolbox image**

Use Nano Banana MCP tool to generate:

Prompt: "Isometric view of a minimalist metal toolbox, mostly empty, containing only 2-3 basic hand tools like a hammer and screwdriver, clean workshop background, flat design, tech illustration style, dark background #0a0e14"

Model: pro
Aspect ratio: 1:1
Output path: `public/images/toolbox-minimal.png`

Expected: Image generated and saved

**Step 3: Generate complete toolbox image**

Prompt: "Isometric view of an overflowing professional toolbox filled with precision instruments, power tools, specialized equipment, wrenches, measuring devices, technical tools arranged dynamically, clean workshop background, flat design, tech illustration style, dark background #0a0e14"

Model: pro
Aspect ratio: 1:1
Output path: `public/images/toolbox-complete.png`

Expected: Image generated and saved

**Step 4: Generate signal icon**

Prompt: "Simple radar or antenna icon in ASCII art style, clean lines, technical diagram aesthetic, representing signal detection and curation, monochrome green #00ff9f on dark background #0a0e14, minimalist"

Model: flash
Aspect ratio: 1:1
Output path: `public/images/signal-icon.png`

Expected: Image generated and saved

**Step 5: Verify images**

```bash
ls -la public/images/
```

Expected: 3 PNG files created

**Step 6: Commit images**

```bash
git add public/images/
git commit -m "feat: add Nano Banana generated images for homepage sections"
```

---

## Task 4: Create Scroll Animation Utility CSS

**Files:**
- Create: `src/styles/utilities/scroll-animations.css`

**Step 1: Create utilities directory**

```bash
mkdir -p src/styles/utilities
```

**Step 2: Write scroll animation base styles**

Create `src/styles/utilities/scroll-animations.css`:

```css
/* Scroll-triggered reveal animations */

/* Base hidden state for scroll-triggered elements */
.scroll-reveal {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.8s ease-out, transform 0.8s ease-out;
}

/* Visible state when in viewport */
.scroll-reveal.in-view {
  opacity: 1;
  transform: translateY(0);
}

/* Slide from left variant */
.scroll-reveal-left {
  opacity: 0;
  transform: translateX(-40px);
  transition: opacity 0.8s ease-out, transform 0.8s ease-out;
}

.scroll-reveal-left.in-view {
  opacity: 1;
  transform: translateX(0);
}

/* Slide from right variant */
.scroll-reveal-right {
  opacity: 0;
  transform: translateX(40px);
  transition: opacity 0.8s ease-out, transform 0.8s ease-out;
}

.scroll-reveal-right.in-view {
  opacity: 1;
  transform: translateX(0);
}

/* Scale variant */
.scroll-reveal-scale {
  opacity: 0;
  transform: scale(0.95);
  transition: opacity 0.8s ease-out, transform 0.8s ease-out;
}

.scroll-reveal-scale.in-view {
  opacity: 1;
  transform: scale(1);
}

/* Stagger delays for sequential reveals */
.scroll-stagger-1 { transition-delay: 0ms; }
.scroll-stagger-2 { transition-delay: 150ms; }
.scroll-stagger-3 { transition-delay: 300ms; }
.scroll-stagger-4 { transition-delay: 450ms; }
.scroll-stagger-5 { transition-delay: 600ms; }

/* Respect reduced motion preference */
@media (prefers-reduced-motion: reduce) {
  .scroll-reveal,
  .scroll-reveal-left,
  .scroll-reveal-right,
  .scroll-reveal-scale {
    opacity: 1;
    transform: none;
    transition: none;
  }
}
```

**Step 3: Verify file created**

```bash
cat src/styles/utilities/scroll-animations.css
```

Expected: File contains all animation classes

**Step 4: Commit utility CSS**

```bash
git add src/styles/utilities/scroll-animations.css
git commit -m "feat: add scroll animation utility classes"
```

---

## Task 5: Create Home Section Components Directory and Shared ScrollReveal

**Files:**
- Create: `src/components/home/.gitkeep`
- Create: `src/components/shared/ScrollReveal.astro`

**Step 1: Create directories**

```bash
mkdir -p src/components/home
mkdir -p src/components/shared
touch src/components/home/.gitkeep
```

**Step 2: Create ScrollReveal wrapper component**

Create `src/components/shared/ScrollReveal.astro`:

```astro
---
interface Props {
  direction?: 'up' | 'left' | 'right' | 'scale';
  delay?: 1 | 2 | 3 | 4 | 5;
  class?: string;
}

const { direction = 'up', delay, class: className } = Astro.props;

const directionClass = direction === 'up' ? 'scroll-reveal' :
                       direction === 'left' ? 'scroll-reveal-left' :
                       direction === 'right' ? 'scroll-reveal-right' :
                       'scroll-reveal-scale';

const delayClass = delay ? `scroll-stagger-${delay}` : '';
const classes = [directionClass, delayClass, className].filter(Boolean).join(' ');
---

<div class={classes} data-scroll-reveal>
  <slot />
</div>

<script>
  // Intersection Observer for scroll-triggered animations
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -10% 0px'
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('in-view');
      }
    });
  }, observerOptions);

  // Observe all scroll-reveal elements
  document.querySelectorAll('[data-scroll-reveal]').forEach(el => {
    observer.observe(el);
  });
</script>
```

**Step 3: Verify component created**

```bash
cat src/components/shared/ScrollReveal.astro
```

Expected: Component code present

**Step 4: Commit ScrollReveal component**

```bash
git add src/components/home/.gitkeep src/components/shared/ScrollReveal.astro
git commit -m "feat: add ScrollReveal wrapper component for animations"
```

---

## Task 6: Build Hero Section Component

**Files:**
- Create: `src/components/home/HeroSection.astro`

**Step 1: Write Hero component structure**

Create `src/components/home/HeroSection.astro`:

```astro
---
// src/components/home/HeroSection.astro
import ScrollReveal from '../shared/ScrollReveal.astro';
---

<section class="hero-section">
  <!-- Video Background -->
  <video
    class="hero-section__video"
    autoplay
    loop
    muted
    playsinline
    poster="/images/hero-poster.jpg"
  >
    <source src="/videos/robot-tools.mp4" type="video/mp4" />
  </video>

  <!-- Overlay -->
  <div class="hero-section__overlay"></div>

  <!-- Scanline Effect (subtle) -->
  <div class="hero-section__scanline"></div>

  <!-- Content -->
  <div class="hero-section__content">
    <ScrollReveal direction="up" delay={1}>
      <h1 class="hero-section__line">
        <span class="hero-section__mono">Claude Code</span> is powerful.
      </h1>
    </ScrollReveal>

    <ScrollReveal direction="up" delay={2}>
      <h1 class="hero-section__line hero-section__line--secondary">
        But it's incomplete.
      </h1>
    </ScrollReveal>

    <ScrollReveal direction="up" delay={3}>
      <div class="hero-section__scroll-indicator">
        <span class="hero-section__scroll-text">Scroll to explore</span>
        <svg class="hero-section__scroll-arrow" width="24" height="24" viewBox="0 0 24 24" fill="none">
          <path d="M12 5v14M19 12l-7 7-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </div>
    </ScrollReveal>
  </div>
</section>

<style>
  .hero-section {
    position: relative;
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
  }

  .hero-section__video {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    z-index: 1;
  }

  .hero-section__overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(10, 14, 20, 0.45);
    z-index: 2;
  }

  .hero-section__scanline {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: repeating-linear-gradient(
      0deg,
      transparent,
      transparent 2px,
      rgba(0, 255, 159, 0.03) 2px,
      rgba(0, 255, 159, 0.03) 4px
    );
    pointer-events: none;
    z-index: 3;
  }

  .hero-section__content {
    position: relative;
    z-index: 4;
    text-align: center;
    padding: var(--space-md);
    max-width: 1200px;
  }

  .hero-section__line {
    font-size: clamp(2.5rem, 4vw, 4.5rem);
    font-weight: var(--weight-bold);
    line-height: var(--leading-tight);
    color: var(--color-terminal-white);
    margin-bottom: var(--space-md);
  }

  .hero-section__line--secondary {
    color: var(--color-accent-primary);
  }

  .hero-section__mono {
    font-family: var(--font-mono);
    color: var(--color-accent-primary);
  }

  .hero-section__scroll-indicator {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: var(--space-xs);
    margin-top: var(--space-xl);
    color: var(--color-muted-gray);
    font-size: var(--text-sm);
    font-family: var(--font-mono);
  }

  .hero-section__scroll-arrow {
    animation: bounce 2s infinite;
  }

  @keyframes bounce {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(10px); }
  }

  @media (prefers-reduced-motion: reduce) {
    .hero-section__scroll-arrow {
      animation: none;
    }
  }

  @media (max-width: 768px) {
    .hero-section__line {
      font-size: clamp(1.8rem, 6vw, 2.5rem);
    }
  }
</style>
```

**Step 2: Create placeholder video poster**

For now, create a note that video will be added:

```bash
mkdir -p public/videos
echo "TODO: Add robot-tools.mp4 video here" > public/videos/README.md
echo "TODO: Add hero-poster.jpg here" > public/images/README.md
```

**Step 3: Test component renders**

Create a test page or verify it compiles without errors:

```bash
npx astro check
```

Expected: No TypeScript errors

**Step 4: Commit Hero component**

```bash
git add src/components/home/HeroSection.astro public/videos/README.md public/images/README.md
git commit -m "feat: add Hero section component with video background"
```

---

## Task 7: Build Gap Section Component

**Files:**
- Create: `src/components/home/GapSection.astro`

**Step 1: Write Gap component structure**

Create `src/components/home/GapSection.astro`:

```astro
---
// src/components/home/GapSection.astro
import ScrollReveal from '../shared/ScrollReveal.astro';
---

<section class="gap-section">
  <div class="gap-section__split">
    <!-- Left Side: Minimal -->
    <div class="gap-section__side gap-section__side--minimal">
      <ScrollReveal direction="left">
        <img
          src="/images/toolbox-minimal.png"
          alt="Minimal toolbox with basic tools"
          class="gap-section__image"
          loading="lazy"
        />
      </ScrollReveal>

      <div class="gap-section__copy">
        <ScrollReveal direction="up" delay={1}>
          <p class="gap-section__line">Out of the box, Claude Code is focused.</p>
        </ScrollReveal>
        <ScrollReveal direction="up" delay={2}>
          <p class="gap-section__line">Powerful.</p>
        </ScrollReveal>
        <ScrollReveal direction="up" delay={3}>
          <p class="gap-section__line">But minimal.</p>
        </ScrollReveal>
      </div>
    </div>

    <!-- Divider with glow effect -->
    <div class="gap-section__divider"></div>

    <!-- Right Side: Complete -->
    <div class="gap-section__side gap-section__side--complete">
      <ScrollReveal direction="right">
        <img
          src="/images/toolbox-complete.png"
          alt="Complete toolbox overflowing with specialized tools"
          class="gap-section__image"
          loading="lazy"
        />
      </ScrollReveal>

      <div class="gap-section__copy">
        <ScrollReveal direction="up" delay={1}>
          <p class="gap-section__line">What if you had specialized tools?</p>
        </ScrollReveal>
        <ScrollReveal direction="up" delay={2}>
          <p class="gap-section__line">Built for power users.</p>
        </ScrollReveal>
        <ScrollReveal direction="up" delay={3}>
          <p class="gap-section__line">By a power user.</p>
        </ScrollReveal>
      </div>
    </div>
  </div>
</section>

<style>
  .gap-section {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background: var(--color-terminal-black);
  }

  .gap-section__split {
    display: grid;
    grid-template-columns: 1fr 2px 1fr;
    width: 100%;
    height: 100vh;
    gap: 0;
  }

  .gap-section__side {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: clamp(2rem, 6vw, 4rem);
    gap: var(--space-xl);
  }

  .gap-section__side--minimal {
    background: rgba(10, 14, 20, 0.7);
  }

  .gap-section__side--complete {
    background: var(--color-terminal-black);
  }

  .gap-section__divider {
    width: 2px;
    background: linear-gradient(
      to bottom,
      transparent,
      var(--color-accent-primary),
      transparent
    );
    box-shadow: var(--glow-primary);
    animation: divider-draw 1s ease-out;
    animation-fill-mode: both;
  }

  @keyframes divider-draw {
    from {
      transform: scaleY(0);
    }
    to {
      transform: scaleY(1);
    }
  }

  .gap-section__image {
    max-width: min(400px, 80%);
    height: auto;
    filter: drop-shadow(0 10px 30px rgba(0, 0, 0, 0.5));
  }

  .gap-section__copy {
    display: flex;
    flex-direction: column;
    gap: var(--space-md);
    text-align: center;
  }

  .gap-section__line {
    font-size: clamp(1.25rem, 2.5vw, 2rem);
    font-weight: var(--weight-medium);
    color: var(--color-terminal-white);
    line-height: var(--leading-tight);
  }

  /* Responsive: Stack vertically on mobile */
  @media (max-width: 768px) {
    .gap-section__split {
      grid-template-columns: 1fr;
      grid-template-rows: 1fr 2px 1fr;
      height: auto;
      min-height: 100vh;
    }

    .gap-section__divider {
      width: 100%;
      height: 2px;
      background: linear-gradient(
        to right,
        transparent,
        var(--color-accent-primary),
        transparent
      );
      animation: divider-draw-horizontal 1s ease-out;
    }

    @keyframes divider-draw-horizontal {
      from {
        transform: scaleX(0);
      }
      to {
        transform: scaleX(1);
      }
    }
  }

  @media (prefers-reduced-motion: reduce) {
    .gap-section__divider {
      animation: none;
    }
  }
</style>
```

**Step 2: Verify component compiles**

```bash
npx astro check
```

Expected: No errors

**Step 3: Commit Gap component**

```bash
git add src/components/home/GapSection.astro
git commit -m "feat: add Gap section with contrast presentation"
```

---

## Task 8: Build Plugin Showcase Component

**Files:**
- Create: `src/components/home/PluginShowcase.astro`

**Step 1: Read ASCII art files utility**

Create `src/components/home/PluginShowcase.astro`:

```astro
---
// src/components/home/PluginShowcase.astro
import ScrollReveal from '../shared/ScrollReveal.astro';
import { readFileSync } from 'fs';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

// Read ASCII art files
const asciiDir = join(process.cwd(), 'src/ascii-assets/plugins');
const asciiArt = readFileSync(join(asciiDir, 'ascii-art.txt'), 'utf-8');
const prompt = readFileSync(join(asciiDir, 'prompt.txt'), 'utf-8');
const creative = readFileSync(join(asciiDir, 'creative.txt'), 'utf-8');
const googleAds = readFileSync(join(asciiDir, 'google-ads.txt'), 'utf-8');

interface Plugin {
  ascii: string;
  name: string;
  description: string;
  url: string;
  color: string;
  direction: 'left' | 'right';
}

const plugins: Plugin[] = [
  {
    ascii: asciiArt,
    name: 'ASCII Art',
    description: 'Turn text into terminal art.',
    url: '/plugins/ascii-art',
    color: 'primary',
    direction: 'right'
  },
  {
    ascii: prompt,
    name: 'Prompt Enhancer',
    description: "Craft better prompts. Anthropic's playbook.",
    url: '/plugins/prompt-enhancer',
    color: 'secondary',
    direction: 'left'
  },
  {
    ascii: creative,
    name: 'Creative Writing',
    description: 'Editorial polish. Without pretense.',
    url: '/plugins/creative-writing',
    color: 'gold',
    direction: 'right'
  },
  {
    ascii: googleAds,
    name: 'Google Ads',
    description: 'GAQL queries. No docs needed.',
    url: '/plugins/google-ads',
    color: 'primary',
    direction: 'left'
  }
];
---

<section class="plugin-showcase">
  <!-- Opening Copy -->
  <div class="plugin-showcase__intro">
    <ScrollReveal direction="up">
      <h2 class="plugin-showcase__heading">Here's what I built.</h2>
    </ScrollReveal>
    <ScrollReveal direction="up" delay={2}>
      <p class="plugin-showcase__subheading">Tools for the gaps.</p>
    </ScrollReveal>
  </div>

  <!-- Plugin Cascade -->
  <div class="plugin-showcase__grid">
    {plugins.map((plugin, index) => (
      <ScrollReveal direction={plugin.direction} delay={index + 1}>
        <a
          href={plugin.url}
          class={`plugin-showcase__item plugin-showcase__item--${plugin.color}`}
        >
          <pre class="plugin-showcase__ascii" aria-label={plugin.name}>{plugin.ascii}</pre>
          <p class="plugin-showcase__description">{plugin.description}</p>
        </a>
      </ScrollReveal>
    ))}
  </div>
</section>

<style>
  .plugin-showcase {
    min-height: 200vh;
    padding: clamp(4rem, 10vh, 8rem) clamp(2rem, 6vw, 4rem);
    background: var(--color-terminal-black);
  }

  .plugin-showcase__intro {
    text-align: center;
    margin-bottom: clamp(4rem, 10vh, 8rem);
  }

  .plugin-showcase__heading {
    font-size: clamp(2rem, 4vw, 3.5rem);
    font-weight: var(--weight-bold);
    color: var(--color-terminal-white);
    margin-bottom: var(--space-md);
  }

  .plugin-showcase__subheading {
    font-size: clamp(1.25rem, 2.5vw, 2rem);
    font-weight: var(--weight-normal);
    color: var(--color-muted-gray);
  }

  .plugin-showcase__grid {
    display: flex;
    flex-direction: column;
    gap: clamp(6rem, 15vh, 12rem);
    max-width: 1400px;
    margin: 0 auto;
  }

  .plugin-showcase__item {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: var(--space-lg);
    padding: var(--space-xl);
    text-decoration: none;
    transition: transform var(--transition-normal), box-shadow var(--transition-normal);
    cursor: pointer;
  }

  .plugin-showcase__item:nth-child(odd) {
    align-self: flex-start;
    max-width: 70%;
  }

  .plugin-showcase__item:nth-child(even) {
    align-self: flex-end;
    max-width: 70%;
  }

  .plugin-showcase__ascii {
    font-family: var(--font-mono);
    font-size: clamp(0.5rem, 1vw, 0.8rem);
    line-height: 1;
    white-space: pre;
    overflow: visible;
    transition: filter var(--transition-normal), transform var(--transition-normal);
  }

  .plugin-showcase__item--primary .plugin-showcase__ascii {
    color: var(--color-accent-primary);
    text-shadow: 0 0 10px rgba(0, 255, 159, 0.3);
  }

  .plugin-showcase__item--secondary .plugin-showcase__ascii {
    color: var(--color-accent-secondary);
    text-shadow: 0 0 10px rgba(255, 107, 157, 0.3);
  }

  .plugin-showcase__item--gold .plugin-showcase__ascii {
    color: var(--color-highlight-gold);
    text-shadow: 0 0 10px rgba(255, 215, 0, 0.3);
  }

  .plugin-showcase__item:hover .plugin-showcase__ascii {
    filter: brightness(1.3);
    transform: scale(1.02);
  }

  .plugin-showcase__item--primary:hover {
    box-shadow: var(--glow-primary);
  }

  .plugin-showcase__item--secondary:hover {
    box-shadow: var(--glow-secondary);
  }

  .plugin-showcase__item--gold:hover {
    box-shadow: var(--glow-gold);
  }

  .plugin-showcase__description {
    font-size: clamp(1rem, 2vw, 1.5rem);
    font-weight: var(--weight-normal);
    color: var(--color-terminal-white);
    text-align: center;
    font-family: var(--font-body);
  }

  @media (max-width: 768px) {
    .plugin-showcase {
      min-height: auto;
    }

    .plugin-showcase__item:nth-child(odd),
    .plugin-showcase__item:nth-child(even) {
      align-self: center;
      max-width: 100%;
    }

    .plugin-showcase__ascii {
      font-size: clamp(0.35rem, 2vw, 0.5rem);
    }
  }
</style>
```

**Step 2: Verify component compiles**

```bash
npx astro check
```

Expected: No errors

**Step 3: Commit Plugin Showcase component**

```bash
git add src/components/home/PluginShowcase.astro
git commit -m "feat: add Plugin Showcase with ASCII cascade"
```

---

## Task 9: Build Newsletter Section Component

**Files:**
- Create: `src/components/home/NewsletterSection.astro`

**Step 1: Write Newsletter component**

Create `src/components/home/NewsletterSection.astro`:

```astro
---
// src/components/home/NewsletterSection.astro
import ScrollReveal from '../shared/ScrollReveal.astro';
---

<section class="newsletter-section">
  <div class="newsletter-section__content">
    <!-- Narrative Copy -->
    <ScrollReveal direction="up">
      <p class="newsletter-section__line newsletter-section__line--intro">
        I'm not the only one building.
      </p>
    </ScrollReveal>

    <ScrollReveal direction="up" delay={2}>
      <p class="newsletter-section__line">
        The Claude ecosystem is exploding.
      </p>
    </ScrollReveal>

    <ScrollReveal direction="up" delay={3}>
      <p class="newsletter-section__line">
        New plugins. MCP servers. Workflow breakthroughs.
      </p>
    </ScrollReveal>

    <ScrollReveal direction="up" delay={4}>
      <p class="newsletter-section__line newsletter-section__line--emphasis">
        Most of it's noise.
      </p>
    </ScrollReveal>

    <ScrollReveal direction="up" delay={5}>
      <p class="newsletter-section__line newsletter-section__line--cta">
        I curate the signal.
      </p>
    </ScrollReveal>

    <!-- Signal Icon -->
    <ScrollReveal direction="scale">
      <img
        src="/images/signal-icon.png"
        alt="Signal curation icon"
        class="newsletter-section__icon"
        loading="lazy"
      />
    </ScrollReveal>

    <!-- Email Form -->
    <ScrollReveal direction="up">
      <form class="newsletter-section__form" id="newsletter-form">
        <div class="newsletter-section__input-group">
          <input
            type="email"
            name="email"
            placeholder="your@email.com"
            class="newsletter-section__input"
            required
            aria-label="Email address"
          />
          <button type="submit" class="newsletter-section__button">
            Subscribe
          </button>
        </div>
        <p class="newsletter-section__fine-print">
          Weekly curation. Claude plugins. MCP servers. Tools worth your time.<br/>
          Unsubscribe anytime.
        </p>
      </form>
    </ScrollReveal>

    <!-- Success Message (hidden by default) -->
    <div class="newsletter-section__success" id="newsletter-success" hidden>
      <p class="newsletter-section__success-text">
        ✓ SUBSCRIBED
      </p>
      <p class="newsletter-section__success-message">
        Welcome to the signal.
      </p>
    </div>
  </div>
</section>

<style>
  .newsletter-section {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background: var(--color-terminal-black);
    padding: clamp(3rem, 8vh, 6rem) clamp(2rem, 6vw, 4rem);
  }

  .newsletter-section__content {
    max-width: 800px;
    text-align: center;
  }

  .newsletter-section__line {
    font-size: clamp(1.25rem, 2.5vw, 2rem);
    font-weight: var(--weight-normal);
    color: var(--color-terminal-white);
    margin-bottom: var(--space-lg);
    line-height: var(--leading-normal);
  }

  .newsletter-section__line--intro {
    color: var(--color-muted-gray);
    font-size: clamp(1rem, 2vw, 1.5rem);
  }

  .newsletter-section__line--emphasis {
    color: var(--color-accent-secondary);
    font-weight: var(--weight-medium);
  }

  .newsletter-section__line--cta {
    color: var(--color-accent-primary);
    font-weight: var(--weight-bold);
    margin-bottom: var(--space-xl);
  }

  .newsletter-section__icon {
    max-width: 120px;
    height: auto;
    margin: var(--space-xl) auto;
    filter: drop-shadow(0 0 20px rgba(0, 255, 159, 0.4));
    animation: pulse 3s ease-in-out infinite;
  }

  @keyframes pulse {
    0%, 100% { opacity: 0.8; }
    50% { opacity: 1; }
  }

  .newsletter-section__form {
    margin-top: var(--space-2xl);
  }

  .newsletter-section__input-group {
    display: flex;
    gap: var(--space-sm);
    margin-bottom: var(--space-md);
    flex-wrap: wrap;
    justify-content: center;
  }

  .newsletter-section__input {
    flex: 1;
    min-width: 250px;
    max-width: 400px;
    padding: var(--space-sm) var(--space-md);
    background: transparent;
    border: 1px solid var(--color-muted-gray);
    color: var(--color-terminal-white);
    font-family: var(--font-mono);
    font-size: var(--text-base);
    transition: border-color var(--transition-fast), box-shadow var(--transition-fast);
  }

  .newsletter-section__input:focus {
    outline: none;
    border-color: var(--color-accent-primary);
    box-shadow: 0 0 0 1px var(--color-accent-primary), var(--glow-primary);
  }

  .newsletter-section__input::placeholder {
    color: var(--color-muted-gray);
  }

  .newsletter-section__button {
    padding: var(--space-sm) var(--space-md);
    background: var(--color-bg-hover);
    border: 1px solid var(--color-accent-primary);
    color: var(--color-accent-primary);
    font-family: var(--font-mono);
    font-size: var(--text-sm);
    font-weight: var(--weight-medium);
    cursor: pointer;
    transition: all var(--transition-fast);
    white-space: nowrap;
  }

  .newsletter-section__button::before {
    content: "$ ";
  }

  .newsletter-section__button:hover {
    background: rgba(0, 255, 159, 0.2);
    box-shadow: var(--glow-primary);
    transform: translateY(-1px);
  }

  .newsletter-section__button:active {
    transform: translateY(0);
  }

  .newsletter-section__fine-print {
    font-size: var(--text-sm);
    color: var(--color-muted-gray);
    line-height: var(--leading-relaxed);
  }

  .newsletter-section__success {
    margin-top: var(--space-xl);
  }

  .newsletter-section__success-text {
    font-size: clamp(1.5rem, 3vw, 2.5rem);
    font-weight: var(--weight-bold);
    color: var(--color-accent-primary);
    font-family: var(--font-mono);
    margin-bottom: var(--space-md);
  }

  .newsletter-section__success-message {
    font-size: clamp(1rem, 2vw, 1.5rem);
    color: var(--color-terminal-white);
  }

  @media (max-width: 768px) {
    .newsletter-section__input-group {
      flex-direction: column;
      align-items: stretch;
    }

    .newsletter-section__input {
      min-width: auto;
    }
  }

  @media (prefers-reduced-motion: reduce) {
    .newsletter-section__icon {
      animation: none;
    }
  }
</style>

<script>
  const form = document.getElementById('newsletter-form') as HTMLFormElement;
  const successDiv = document.getElementById('newsletter-success') as HTMLDivElement;

  form?.addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = new FormData(form);
    const email = formData.get('email') as string;

    // TODO: Replace with actual newsletter API endpoint
    // For now, just show success
    try {
      // Simulate API call
      await new Promise(resolve => setTimeout(resolve, 500));

      // Hide form, show success
      form.style.display = 'none';
      successDiv.hidden = false;

      console.log('Newsletter signup:', email);
    } catch (error) {
      console.error('Newsletter signup failed:', error);
      alert('Subscription failed. Please try again.');
    }
  });
</script>
```

**Step 2: Verify component compiles**

```bash
npx astro check
```

Expected: No errors

**Step 3: Commit Newsletter component**

```bash
git add src/components/home/NewsletterSection.astro
git commit -m "feat: add Newsletter section with email capture"
```

---

## Task 10: Create Homepage Redesign CSS

**Files:**
- Create: `src/styles/components/home-redesign.css`

**Step 1: Write homepage-specific styles**

Create `src/styles/components/home-redesign.css`:

```css
/* Homepage Redesign Styles */

/* Smooth scroll behavior */
html {
  scroll-behavior: smooth;
}

/* Remove padding from main on homepage */
.homepage-layout main {
  padding-top: 0;
  padding-bottom: 0;
}

/* Full-screen section utilities */
.full-screen-section {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Menerals-inspired fluid spacing */
.section-padding {
  padding: clamp(3rem, 8vh, 6rem) clamp(2rem, 6vw, 4rem);
}

/* Typography rhythm - Menerals style */
.copy-line {
  margin-bottom: clamp(1rem, 3vh, 2rem);
}

.copy-line + .copy-line {
  margin-top: clamp(0.5rem, 2vh, 1rem);
}

/* Scanline effect utility */
.scanline-overlay {
  position: relative;
}

.scanline-overlay::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: repeating-linear-gradient(
    0deg,
    transparent,
    transparent 2px,
    rgba(0, 255, 159, 0.03) 2px,
    rgba(0, 255, 159, 0.03) 4px
  );
  pointer-events: none;
  z-index: 10;
}

/* Video background utilities */
.video-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* Gradient overlay utility */
.gradient-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    180deg,
    rgba(10, 14, 20, 0.3) 0%,
    rgba(10, 14, 20, 0.5) 100%
  );
}

/* Glow divider utility */
.glow-divider {
  width: 100%;
  height: 2px;
  background: linear-gradient(
    to right,
    transparent,
    var(--color-accent-primary),
    transparent
  );
  box-shadow: var(--glow-primary);
}

.glow-divider--vertical {
  width: 2px;
  height: 100%;
  background: linear-gradient(
    to bottom,
    transparent,
    var(--color-accent-primary),
    transparent
  );
}

/* Respect reduced motion */
@media (prefers-reduced-motion: reduce) {
  html {
    scroll-behavior: auto;
  }

  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

**Step 2: Verify file created**

```bash
cat src/styles/components/home-redesign.css
```

Expected: File contains utility styles

**Step 3: Commit homepage CSS**

```bash
git add src/styles/components/home-redesign.css
git commit -m "feat: add homepage redesign utility styles"
```

---

## Task 11: Update Homepage (index.astro) with New Components

**Files:**
- Modify: `src/pages/index.astro`

**Step 1: Back up current homepage**

```bash
cp src/pages/index.astro src/pages/index.astro.backup
```

**Step 2: Rewrite homepage with new sections**

Replace content of `src/pages/index.astro`:

```astro
---
// src/pages/index.astro
import BaseLayout from '../layouts/BaseLayout.astro';
import HeroSection from '../components/home/HeroSection.astro';
import GapSection from '../components/home/GapSection.astro';
import PluginShowcase from '../components/home/PluginShowcase.astro';
import NewsletterSection from '../components/home/NewsletterSection.astro';

import '../styles/utilities/scroll-animations.css';
import '../styles/components/home-redesign.css';
---

<BaseLayout
  title="Home"
  description="Claude Code is powerful but incomplete. Discover specialized tools built for power users by a power user."
>
  <div class="homepage-layout">
    <HeroSection />
    <GapSection />
    <PluginShowcase />
    <NewsletterSection />
  </div>
</BaseLayout>

<style>
  .homepage-layout :global(main) {
    padding: 0;
  }
</style>
```

**Step 3: Test homepage loads**

```bash
npm run dev
```

Expected: Dev server starts without errors

**Step 4: Open browser and verify**

Navigate to `http://localhost:4321`

Expected: New homepage renders with all 4 sections

**Step 5: Commit updated homepage**

```bash
git add src/pages/index.astro src/pages/index.astro.backup
git commit -m "feat: replace homepage with redesigned full-screen sections"
```

---

## Task 12: Test Responsive Behavior

**Files:**
- None (testing task)

**Step 1: Test desktop layout**

Open dev tools, viewport at 1440px width

Verify:
- All sections full-screen
- Gap section has side-by-side split
- Plugin showcase has staggered left/right layout
- Typography is large and readable

Expected: Desktop layout looks good

**Step 2: Test tablet layout**

Resize to 768px width

Verify:
- Sections still readable
- Gap section split maintained or starts to stack
- Plugin showcase stagger maintained
- Typography scales down appropriately

Expected: Tablet layout works

**Step 3: Test mobile layout**

Resize to 375px width

Verify:
- Gap section stacks vertically
- Plugin showcase centers
- Newsletter form stacks
- All text remains readable
- No horizontal scroll

Expected: Mobile layout works without issues

**Step 4: Test reduced motion**

Enable "Reduce motion" in OS accessibility settings

Verify:
- Animations don't play or are minimal
- Content still appears
- No jarring transitions
- Hero scroll indicator doesn't bounce

Expected: Reduced motion respected

**Step 5: Document any issues**

If issues found, create TODO list:
```bash
echo "Responsive issues to fix:" > responsive-todos.md
```

---

## Task 13: Optimize Performance

**Files:**
- Modify: Various component files as needed

**Step 1: Add lazy loading to all images**

Verify all `<img>` tags have `loading="lazy"`:
- GapSection images
- PluginShowcase (none, uses ASCII)
- Newsletter icon

Expected: All images lazy load

**Step 2: Add video poster and preload**

In HeroSection.astro, ensure:
- `poster` attribute is set
- `preload="metadata"` is set

Expected: Video doesn't auto-download full file

**Step 3: Test Lighthouse performance**

```bash
npm run build
npm run preview
```

Then run Lighthouse on `http://localhost:4321`

Target scores:
- Performance: > 90
- Accessibility: > 95
- Best Practices: > 95
- SEO: > 90

**Step 4: Check Core Web Vitals**

Verify:
- LCP (Largest Contentful Paint) < 2.5s
- FID (First Input Delay) < 100ms
- CLS (Cumulative Layout Shift) < 0.1

Expected: All metrics in green

**Step 5: Commit any performance optimizations**

```bash
git add .
git commit -m "perf: optimize images and video loading"
```

---

## Task 14: Accessibility Audit

**Files:**
- Modify: Component files as needed

**Step 1: Test keyboard navigation**

Using only keyboard:
- Tab through all sections
- Activate newsletter form
- Tab to plugin links
- Activate plugin links

Expected: All interactive elements reachable and activatable

**Step 2: Test with screen reader**

Enable VoiceOver (Mac) or NVDA (Windows)

Verify:
- All sections announced
- ASCII art has proper aria-labels
- Form inputs have labels
- Images have alt text
- Headings properly structured

Expected: Screen reader can navigate entire page

**Step 3: Check color contrast**

Use browser dev tools or WebAIM contrast checker

Verify all text meets WCAG AA:
- Normal text: 4.5:1 minimum
- Large text: 3:1 minimum

Expected: All text passes contrast requirements

**Step 4: Test focus indicators**

Tab through page and verify:
- All focusable elements show clear focus ring
- Focus ring uses `--color-accent-primary`
- Focus ring visible on all backgrounds

Expected: Focus always visible

**Step 5: Run axe DevTools**

Install axe browser extension, run scan

Fix any critical or serious issues found

Expected: No critical accessibility issues

**Step 6: Commit accessibility improvements**

```bash
git add .
git commit -m "a11y: improve keyboard navigation and screen reader support"
```

---

## Task 15: Final Polish and Testing

**Files:**
- Various

**Step 1: Cross-browser testing**

Test in:
- Chrome/Edge
- Firefox
- Safari

Verify all animations and layouts work

Expected: Consistent experience across browsers

**Step 2: Add missing video file placeholder**

Since video generation is external, add a proper placeholder:

Create `public/videos/robot-tools-placeholder.mp4` or add fallback logic

Expected: Page doesn't break without video

**Step 3: Verify all links work**

Click through:
- All plugin showcase links → plugin pages
- Newsletter form submission
- Scroll indicators

Expected: All links functional

**Step 4: Check console for errors**

Open browser console

Expected: No errors or warnings

**Step 5: Final build test**

```bash
npm run build
```

Expected: Build succeeds without errors

**Step 6: Create deployment checklist**

Add to README or create DEPLOY.md:
```markdown
## Pre-deployment Checklist

- [ ] Replace robot-tools.mp4 with actual video
- [ ] Connect newsletter form to real API
- [ ] Test on production domain
- [ ] Verify analytics tracking
- [ ] Check all plugin links
```

**Step 7: Final commit**

```bash
git add .
git commit -m "chore: final polish and pre-deployment prep"
```

---

## Task 16: Documentation and Handoff

**Files:**
- Create: `docs/homepage-redesign-notes.md`

**Step 1: Document implementation**

Create `docs/homepage-redesign-notes.md`:

```markdown
# Homepage Redesign - Implementation Notes

## Completed

- Full-screen progressive disclosure layout
- 4 sections: Hero, Gap, Plugin Showcase, Newsletter
- Menerals-inspired copy rhythm and spacing
- Terminal DNA maintained through ASCII art and subtle effects
- Responsive design (mobile, tablet, desktop)
- Accessibility (keyboard nav, screen reader, reduced motion)
- Performance optimized (lazy loading, minimal dependencies)

## Components Created

- `HeroSection.astro` - Video hero with overlay
- `GapSection.astro` - Contrast split-screen
- `PluginShowcase.astro` - ASCII art cascade
- `NewsletterSection.astro` - Email capture
- `ScrollReveal.astro` - Reusable animation wrapper

## Still Needed

1. **Video Asset**: Replace placeholder with actual robot-tools.mp4
2. **Newsletter API**: Connect form to real endpoint (currently console.log)
3. **Signal Icon**: Verify Nano Banana generated image looks good
4. **Testing**: Real-world user testing for UX validation

## Maintenance Notes

- ASCII art files in `src/ascii-assets/plugins/`
- Images in `public/images/`
- All animations respect `prefers-reduced-motion`
- Scroll animations use Intersection Observer (no external libs)

## Performance

Current Lighthouse scores (localhost):
- Performance: TBD (test after video added)
- Accessibility: TBD
- Best Practices: TBD
- SEO: TBD
```

**Step 2: Update main README**

Add to project README.md:

```markdown
## Homepage Redesign (Dec 2025)

New full-screen progressive disclosure homepage inspired by Menerals.com.

See `docs/plans/2025-12-28-homepage-redesign-design.md` for design spec.
See `docs/homepage-redesign-notes.md` for implementation notes.
```

**Step 3: Commit documentation**

```bash
git add docs/homepage-redesign-notes.md README.md
git commit -m "docs: add homepage redesign implementation notes"
```

**Step 4: Push to remote**

```bash
git push origin main
```

Expected: All commits pushed successfully

---

## Post-Implementation Tasks

### Video Generation (External)

Generate robot-tools.mp4 with:
- Retro humanoid robot picking up power tools
- Loop-friendly (seamless start/end)
- 1920x1080 minimum resolution
- Color graded to complement `--color-terminal-black`
- MP4 format, H.264 codec, optimized for web

### Newsletter API Integration

Replace console.log in NewsletterSection.astro with actual API call:

```typescript
const response = await fetch('/api/newsletter', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ email })
});
```

Create API endpoint at `src/pages/api/newsletter.ts`

### Analytics Tracking

Add event tracking for:
- Plugin link clicks
- Newsletter signups
- Scroll depth

### A/B Testing Ideas

Consider testing:
- Different hero copy variations
- Plugin showcase order
- Newsletter CTA placement

---

## Success Metrics

Track after deployment:
- Newsletter signup rate
- Plugin page visit rate from showcase
- Average time on homepage
- Scroll depth percentage
- Bounce rate change

Compare to pre-redesign metrics.

---

**Plan Complete!**
