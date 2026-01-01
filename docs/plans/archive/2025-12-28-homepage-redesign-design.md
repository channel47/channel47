# Channel 47 Homepage Redesign - Design Document

**Date**: 2025-12-28
**Status**: Design Complete, Ready for Implementation
**Design Inspiration**: Menerals.com

## Overview

Complete redesign of the Channel 47 homepage to employ clean, full-screen, progressive disclosure layout principles modeled after Menerals.com. The redesign maintains Channel 47's terminal DNA through subtle accents while embracing modern, sophisticated design patterns that work seamlessly across all devices.

## Brand Direction

### Core Narrative
**The Power User Enabler**: "Claude Code is powerful but incomplete. Here's what I built to unlock it."

### Visual Philosophy
- Clean, full-screen progressive disclosure
- Menerals-inspired copy rhythm (short lines, 5-6 max before visual break)
- Terminal DNA preserved through subtle accents (monospace fonts, scanlines, ASCII art)
- Seamless text-image integration with no clear separation
- Minimal UI chrome - let content breathe

### Channel 47 Identity
Channel 47 is a personal brand embodiment bridging:
- Who Jackson is (craftsman, contrarian builder, curator)
- Curated high-signal value for Claude/MCP ecosystem power users
- Builder AND curator positioning

### Content Roles
- **Site**: Showcases Jackson's creations (plugins, tools)
- **Newsletter**: Curates the broader ecosystem (plugins from others, MCP servers, discoveries, workflow improvements)

## Page Structure

The homepage follows a 4-section narrative arc with full-screen progressive disclosure:

### Section 1: Hero - "Claude Code is powerful but incomplete"

**Purpose**: Hook visitors with the core problem statement

**Layout**:
- Full-screen (`100vh`)
- Looping background video: Retro humanoid robot picking up power tools
- Semi-transparent overlay: `rgba(10, 14, 20, 0.45)` using `--color-terminal-black`
- Centered, vertically aligned content

**Copy**:
```
Claude Code is powerful.

But it's incomplete.

[subtle scroll indicator]
```

**Typography**:
- "Claude Code" in JetBrains Mono (maintains terminal DNA)
- Rest in Inter
- Large fluid sizing: `clamp(2.5rem, 4vw, 4.5rem)`
- Sequential fade-in (200-300ms stagger between lines)

**Terminal DNA Accents**:
- Very subtle scanline overlay (opacity: 0.03 - barely visible, atmospheric)
- Video color-graded to complement terminal palette

**Technical**:
- `<section>` with `height: 100vh`, `position: relative`
- `<video autoplay loop muted playsinline>` as background
- Overlay div with semi-transparent gradient
- Centered copy container with staggered fade-in animations
- Scroll indicator appears after copy sequence completes

---

### Section 2: The Gap - Contrast Presentation

**Purpose**: Show what's missing vs. what's possible (problem → solution)

**Layout**:
- Full-screen section (`100vh`)
- Vertical split (desktop: 50/50, mobile: stacked)
- Thin glowing border separator in `--color-accent-primary`

**Left Side - "Out of the box"**:
- Background: Slightly darker than `--color-terminal-black`
- Nano Banana generated image: Minimalist toolbox, mostly empty, few basic tools (transparent background matching darker shade)
- Copy:
  ```
  Out of the box, Claude Code is focused.

  Powerful.

  But minimal.
  ```

**Right Side - "What's possible"**:
- Background: Standard `--color-terminal-black`
- Nano Banana generated image: Same toolbox, overflowing with precision instruments, power tools, specialized equipment (transparent background)
- Copy:
  ```
  What if you had specialized tools?

  Built for power users.

  By a power user.
  ```

**Micro-interactions**:
- Border "draws" from top to bottom on scroll (stroke-dasharray animation)
- Images fade in with slight scale (0.95 → 1.0)
- Copy staggered fade-in

**Responsive**:
- Desktop: 50/50 split, vertical border
- Mobile: Stack vertically, horizontal border between sections

---

### Section 3: Plugin Showcase - Progressive Reveal Cascade

**Purpose**: Showcase the tools built to fill the gaps

**Layout**:
- Extended section (150-200vh height)
- Continuous scroll with plugins appearing/stacking progressively
- Staggered left/right positioning

**Opening Copy** (centered):
```
Here's what I built.

Tools for the gaps.
```

**Plugin Cascade** (appears sequentially as you scroll):

1. **ASCII ART** (scrolls in from right)
   - Large ASCII block letters: "ASCII ART" (same style as WELCOME in current hero)
   - Color: `--color-accent-primary` with subtle glow
   - Copy below: `Turn text into terminal art.`
   - Links to `/plugins/ascii-art`

2. **PROMPT** (scrolls in from left, vertically offset)
   - ASCII block letters: "PROMPT"
   - Color: `--color-accent-secondary`
   - Copy: `Craft better prompts. Anthropic's playbook.`
   - Links to `/plugins/prompt-enhancer`

3. **CREATIVE** (scrolls in from right)
   - ASCII block letters: "CREATIVE"
   - Color: `--color-highlight-gold`
   - Copy: `Editorial polish. Without pretense.`
   - Links to `/plugins/creative-writing`

4. **GOOGLE ADS** (scrolls in from left)
   - ASCII block letters: "GOOGLE ADS" (stack as "GOOGLE" / "ADS" if needed)
   - Color: `--color-accent-primary`
   - Copy: `GAQL queries. No docs needed.`
   - Links to `/plugins/google-ads`

**Micro-interactions** (per plugin):
- ASCII text fade-in with slight scale (0.98 → 1)
- Letter-by-letter staggered animation (left to right reveal)
- Scanline effect passes over ASCII on initial reveal
- Hover: ASCII glows brighter, increased box-shadow, slight lift (translateY -4px)
- Connecting dotted lines in `--color-muted-gray` between plugins

**Responsive**:
- Desktop: Staggered left/right, large ASCII
- Tablet: Smaller ASCII, maintained stagger
- Mobile: Center-aligned, appropriately scaled

**Result**: By end of scroll, all 4 plugins visible together, creating complete toolkit view

---

### Section 4: Newsletter CTA - The Invitation

**Purpose**: Transition from "my tools" to "broader ecosystem curation"

**Layout**:
- Full-screen (`100vh`)
- Vertically centered content
- Minimal, generous breathing room

**Copy Sequence** (appears line by line):
```
I'm not the only one building.

The Claude ecosystem is exploding.

New plugins. MCP servers. Workflow breakthroughs.

Most of it's noise.

I curate the signal.
```

**Visual Element**:
- Small ASCII art icon representing signal vs noise (radar/antenna design)
- Or: ASCII visualization showing "noise" characters fading into clean "signal" text
- Color: `--color-accent-primary` with subtle pulse glow
- Positioned above or beside copy

**Email Capture Form** (appears last):
- Minimal input field with terminal styling
- Border: `1px solid var(--color-muted-gray)`
- Focus state: Border glows `--color-accent-primary`
- Placeholder: `your@email.com` in `--font-mono`
- Submit button: `.terminal-button` style with "Subscribe" text
- Input focus: Scanline animation passes over once

**Success State**:
- Brief "SUBSCRIBED ✓" message in `--color-accent-primary`
- Form fades out, replaced with: `Welcome to the signal.`

**Supporting Copy** (small, muted):
```
Weekly curation. Claude plugins. MCP servers. Tools worth your time.
Unsubscribe anytime.
```

**Responsive**: Centered approach across all devices, slightly tighter spacing on mobile

---

## Technical Architecture

### File Structure
```
src/
├── pages/
│   └── index.astro (redesigned homepage)
├── components/
│   ├── home/
│   │   ├── HeroSection.astro (video hero)
│   │   ├── GapSection.astro (contrast presentation)
│   │   ├── PluginShowcase.astro (ASCII cascade)
│   │   └── NewsletterSection.astro (email capture)
│   └── shared/
│       └── ScrollReveal.astro (reusable animation wrapper)
├── styles/
│   ├── components/
│   │   └── home-redesign.css (homepage-specific styles)
│   └── utilities/
│       └── scroll-animations.css (reusable animation utilities)
└── ascii-assets/
    └── plugins/ (new directory)
        ├── ascii-art.txt
        ├── prompt.txt
        ├── creative.txt
        └── google-ads.txt
```

### Core Technologies
- **Scroll animations**: Intersection Observer API (no external libraries)
- **CSS animations**: CSS custom properties + keyframes (Menerals approach)
- **Fluid typography**: `clamp()` functions for responsive scaling
- **Video**: Native `<video>` element with `autoplay loop muted playsinline`
- **Form**: Progressive enhancement - works without JavaScript

### Key Implementation Patterns

**1. Full-screen sections**:
```css
section {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}
```

**2. Progressive disclosure**:
- Intersection Observer triggers `.in-view` classes
- CSS animations activated via class changes
- Example:
```css
.scroll-section {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.8s ease-out, transform 0.8s ease-out;
}

.scroll-section.in-view {
  opacity: 1;
  transform: translateY(0);
}
```

**3. Menerals-style spacing**:
- Generous padding using `clamp()`: `padding: clamp(3rem, 8vh, 6rem)`
- Consistent use of existing design tokens from `global.css`

**4. ASCII text loading**:
- Server-side read from `.txt` files
- Injected as `<pre>` with proper HTML escaping
- Styled with existing terminal color palette

**5. Color-matched images**:
- Nano Banana generated with `--color-terminal-black` background
- Transparent or color-matched to create seamless integration

### Animation Strategy

Scroll-reveal pattern (NOT scroll-jacking):
- Sections/elements start with `opacity: 0` and slight `translateY`
- Intersection Observer detects viewport entry
- Adds `.in-view` class
- CSS transitions handle actual animation
- Respects `prefers-reduced-motion`

### Responsive Breakpoints
- **Mobile**: < 768px (stacked, centered layout)
- **Tablet**: 768px - 1024px (adjusted spacing, maintained structure)
- **Desktop**: > 1024px (full staggered layout)

### Performance Considerations
- **Video**: Preload metadata only, lazy load actual video content
- **Images**: `loading="lazy"` attribute
- **Animations**: Respect `prefers-reduced-motion` media query
- **ASCII**: Inline in HTML (no additional requests)
- **Intersection Observer**: Single observer instance, reused across elements

### Newsletter Integration
- Form posts to existing newsletter endpoint
- Client-side email validation
- Success/error states with terminal-style messaging
- Honeypot field for spam prevention
- Progressive enhancement: works without JavaScript

---

## Design Principles from Menerals

### Copy Rhythm
- Short lines (rarely more than 5-6 words)
- Frequent visual breaks
- One concept per line/group
- Let copy breathe with generous spacing

### Visual Integration
- Text and images flow seamlessly
- No clear separation/boxes around content
- Transparent or color-matched backgrounds
- Content feels like one cohesive piece

### Minimal UI Chrome
- Remove unnecessary borders, boxes, containers
- Let content speak for itself
- Interface elements only when absolutely needed
- Trust whitespace and typography

### Progressive Disclosure
- One idea at a time
- Scroll reveals next concept naturally
- No information overload
- Guide user through narrative journey

### Micro-interactions
- Subtle, purposeful animations
- Never gratuitous or distracting
- Enhance understanding and delight
- Respect user preferences (reduced motion)

---

## Implementation Notes

### Playwright Analysis
During implementation, use Playwright to:
- Navigate to https://menerals.com
- Capture screenshots of key sections
- Inspect actual CSS for spacing/animation values
- Analyze scroll behavior and timing
- Extract exact layout patterns and breakpoints

### ASCII Art Generation
Need to create ASCII block letter files for plugins:
- Use consistent style (same as WELCOME/LATEST)
- Save to `src/ascii-assets/plugins/`
- Filenames: `ascii-art.txt`, `prompt.txt`, `creative.txt`, `google-ads.txt`

### Nano Banana Image Prompts
**Left toolbox (minimal)**:
```
Isometric view of a minimalist metal toolbox, mostly empty, containing only 2-3 basic hand tools like a hammer and screwdriver, clean workshop background, transparent background, flat design, tech illustration style
```

**Right toolbox (complete)**:
```
Isometric view of an overflowing professional toolbox filled with precision instruments, power tools, specialized equipment, wrenches, measuring devices, technical tools arranged dynamically, clean workshop background, transparent background, flat design, tech illustration style
```

**Signal icon for newsletter**:
```
Simple ASCII art style radar or antenna icon, clean lines, technical diagram aesthetic, representing signal detection, monochrome, minimalist
```

### Video Asset
- Robot picking up power tools video to be generated externally
- Specs: MP4 format, 1920x1080 minimum, optimized for web
- Loop-friendly (seamless start/end)
- Color grading to complement terminal palette

### Existing Design System Usage
Leverage existing CSS variables:
- Colors: Use terminal palette (`--color-terminal-black`, `--color-accent-primary`, etc.)
- Typography: Existing font stacks (`--font-heading`, `--font-body`, `--font-mono`)
- Spacing: Existing spacing tokens (`--space-xl`, `--section-gap`, etc.)
- Effects: Existing glows (`--glow-primary`, `--glow-secondary`)

### Testing Checklist
- [ ] All sections full-screen on desktop
- [ ] Smooth scroll reveal animations
- [ ] Responsive stacking on mobile works
- [ ] ASCII art displays correctly across devices
- [ ] Video loops seamlessly
- [ ] Newsletter form validates and submits
- [ ] Reduced motion preference respected
- [ ] Links to plugin pages work
- [ ] Performance: LCP < 2.5s, CLS < 0.1
- [ ] Accessibility: Keyboard navigation, screen reader friendly

---

## Success Criteria

### User Experience
- Effortless scroll with clear narrative progression
- Immediate understanding of Channel 47's value proposition
- Visual delight without overwhelming
- Clear path to plugins and newsletter signup

### Brand Perception
- Professional, sophisticated, modern
- Terminal/tech heritage maintained through accents
- Craftsman quality evident in design execution
- Differentiated from generic AI tool sites

### Technical Quality
- Fast load times (LCP < 2.5s)
- Smooth 60fps animations
- Responsive across all devices
- Accessible (WCAG 2.1 AA minimum)

### Conversion Goals
- Increased plugin page visits
- Newsletter signups increase
- Longer average time on site
- Lower bounce rate on homepage

---

## Future Considerations

### Content Expansion
As Channel 47 grows, this design pattern can extend to:
- Individual plugin pages (each tells its own story)
- Blog post template (narrative-driven, not documentation-style)
- Additional landing pages for specific use cases

### Newsletter Content Evolution
As newsletter grows, consider:
- Featured section on homepage showing latest curated finds
- Subscriber count as social proof
- Archive of past curations

### Video Assets
Consider creating additional videos for:
- Section 2 backgrounds (subtle tool animations)
- Plugin showcase backgrounds (relevant metaphors)
- Tutorial/demo content

---

## Appendix: Reference Links

- **Design Inspiration**: https://menerals.com
- **Existing Site**: https://channel47.com (current state)
- **Brand Philosophy**: Personal brand embodiment + high-signal curator for Claude/MCP ecosystem
