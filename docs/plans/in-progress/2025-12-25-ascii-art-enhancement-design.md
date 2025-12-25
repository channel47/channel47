# ASCII Art Enhancement Design

**Date:** 2025-12-25
**Status:** Design Phase
**Goal:** Systematically enhance Channel 47 site with bold ASCII art elements while maintaining minimal aesthetic with lots of white space

## Vision

Transform Channel 47 into a visually distinctive site where ASCII art becomes a defining characteristic. The enhancement follows a hybrid approach: bold ASCII block text for main landmark headers, complemented by minimalist zen-inspired organic ASCII art pieces (birds, trees, nature elements) that add human warmth to the technical aesthetic.

## Design Principles

- **Bold but minimal**: ASCII art has strong presence but doesn't overwhelm content
- **Zen aesthetic**: Organic elements rendered in clean, minimalist ASCII with emphasis on negative space
- **Systematic integration**: Cohesive visual identity across all pages
- **Accessibility-first**: ASCII enhancements remain decorative; semantic HTML and screen reader support unchanged
- **Performance**: Pre-generated assets committed to repo for fast loading

## Architecture & Component Strategy

### Core Components

**1. `<AsciiHeader>` (new)**
- Renders pre-generated block-style ASCII text for main section headers
- Props: `text` (which header), `align` (left/center/right)
- Handles responsive sizing
- Wraps in semantic `<h1>` or `<h2>` with proper ARIA labels

**2. `<AsciiArt>` (new)**
- Displays decorative zen/organic ASCII pieces
- Props: `name` (which piece), `position` (hero/divider/sidebar), `opacity` (default 0.6)
- Wraps in `<figure>` with `aria-hidden="true"` (decorative only)

**3. `<AsciiLogo>` (existing)**
- Keep as-is, works well for navigation

**4. `<AsciiIcon>` (existing)**
- Keep subtle watermarks on plugin cards at current opacity

### Asset Organization

```
src/
  ascii-assets/
    headers/
      tools.txt
      blog.txt
      latest.txt
      subscribe.txt
    art/
      hero-bird.txt
      tree-silhouette.txt
      plugin-background.txt
      blog-bird.txt
      blog-leaf.txt
      blog-mountain.txt
      email-icon.txt
      about-scene.txt
```

Each `.txt` file contains pre-generated ASCII art. Components import and render these at build time. This keeps them maintainable and easy to swap out.

## Site-Wide Placement Strategy

### Homepage (`src/pages/index.astro`)

**Hero Section:**
- Add zen ASCII art piece (bird in flight) positioned to right or left of hero text
- Medium-large size (~10-12 lines tall), 60% opacity
- Creates immediate visual impact while text remains primary focus

**Blog Section Divider:**
- Replace "Latest from the blog" text header with `<AsciiHeader text="LATEST" />`
- Add small decorative art (tree silhouette, ~6-8 lines) as subtle accent below header

**Email Signup Section:**
- Replace section title with `<AsciiHeader text="SUBSCRIBE" />`
- Add tiny email/paper plane icon (~4 lines, 50-70% opacity) as playful accent

### Plugin Index (`src/pages/plugins/index.astro`)

**Main Header:**
- Convert "Tools that work" to bold ASCII block text using `<AsciiHeader text="TOOLS" />` paired with light-weight "that work" in regular typography
- This becomes a primary landmark moment

**Background Element:**
- Add large zen ASCII piece (minimalist terminal window with plant/sprout growing from it, ~20-30 lines tall)
- Very subtle watermark behind plugin grid (15-20% opacity)
- Lower opacity since it's behind interactive elements
- Hide on mobile to prevent visual clutter

**Existing Elements:**
- Keep plugin cards with their subtle `<AsciiIcon>` watermarks at current opacity
- Good contrast between bold header and subtle cards

### Blog Pages

**Blog Index:**
- ASCII block text header: `<AsciiHeader text="BLOG" />`

**Individual Posts:**
- Small zen art piece at top of each post (bird, leaf, or mountain - ~4-6 lines tall)
- Rotate through options or categorize by post topic
- 40-60% opacity for noticeable but harmonious presence

### About Page

- Decorative ASCII art piece that feels personal and contemplative (~10-15 lines)
- Meditation stone or minimal landscape scene
- 40-60% opacity

## ASCII Art Content Specification

### Block Text Headers (using 'block' style)

Generate with ascii-art skill using `style: "block"`:

1. **"TOOLS"** - Plugin index first word
2. **"BLOG"** - Blog index header
3. **"LATEST"** - Homepage blog section
4. **"SUBSCRIBE"** - Email signup section

### Zen/Organic Art Pieces (using 'minimal' style)

Generate with ascii-art skill using `style: "minimal"` with nature/organic prompts:

1. **Homepage hero companion** (`hero-bird.txt`)
   - Minimalist bird in flight or perched on branch
   - Clean lines, ~8-12 lines tall
   - Conveys freedom, exploration

2. **Homepage blog divider** (`tree-silhouette.txt`)
   - Simple tree silhouette or zen garden pattern
   - ~6-8 lines tall
   - Calming transition element

3. **Plugin page background** (`plugin-background.txt`)
   - Large (20-30 lines) minimalist scene: terminal window with small plant/sprout growing from it
   - Symbolizes growth + tech
   - Very subtle as background watermark

4. **Blog post headers** (rotating set)
   - `blog-bird.txt` - Bird (~5 lines)
   - `blog-leaf.txt` - Leaf (~4 lines)
   - `blog-mountain.txt` - Mountain peak (~6 lines)
   - Each post gets one (random selection or by category)

5. **About page feature** (`about-scene.txt`)
   - Contemplative element like meditation stone or minimal landscape
   - ~10-15 lines

6. **Email signup accent** (`email-icon.txt`)
   - Tiny envelope or paper plane (~4 lines)
   - Playful but minimal

**Design Notes:**
- All pieces use clean ASCII characters
- Avoid heavy blocks except for text headers
- Emphasis on negative space within the art itself to maintain zen aesthetic
- Characters should work in monospace font (JetBrains Mono)

## Styling & Visual Treatment

### Typography & Sizing

**Block Text Headers:**
- Font: `JetBrains Mono` (existing monospace)
- Responsive sizing:
  - Mobile: `clamp(1.5rem, 4vw, 2.5rem)` - readable but not overwhelming
  - Desktop: `clamp(2.5rem, 5vw, 4rem)` - bold landmark presence

**Decorative Art Pieces:**
- Fixed `font-size: 1rem` for ASCII characters
- Scale container for responsive sizing (keeps ASCII proportions intact)

### Color & Opacity Strategy

**Block Text Headers:**
- Color: `var(--color-text)` at 100% opacity
- Functional headers need full readability
- Consider subtle gradient effect on dark mode

**Large Decorative Pieces** (homepage hero, plugin background):
- Color: `var(--color-text)` at 15-25% opacity
- Present but not competing with content

**Medium Decorative Pieces** (blog post headers, dividers):
- Color: `var(--color-text)` at 40-60% opacity
- Noticeable but harmonious

**Small Accents** (email signup icon):
- Color: `var(--color-text)` at 50-70% opacity
- Clear but playful

### Responsive Behavior

**Mobile:**
- Hide large background pieces (plugin page watermark)
- Keep headers and medium/small pieces
- Prevents visual clutter on small screens

**Tablet/Desktop:**
- Show all pieces
- Larger pieces get more breathing room with increased margins

### Animation

**Scroll-Triggered Fade-In:**
- Similar to existing plugin card animation
- Gentle fade-in on scroll (200-300ms duration)
- Apply to both headers and decorative pieces
- Stagger timing:
  - Headers appear first
  - Decorative pieces follow (50-100ms delays)
- Maintains zen vibe - no bouncing or sliding

## Implementation Workflow

### Step 1: Generate ASCII Assets

Use `ascii-art` skill to generate all pieces upfront:

```bash
# Block text headers (style: "block")
- Generate "TOOLS"
- Generate "BLOG"
- Generate "LATEST"
- Generate "SUBSCRIBE"

# Zen art pieces (style: "minimal")
- Generate bird for homepage hero
- Generate tree silhouette for blog divider
- Generate terminal+plant for plugin background
- Generate small bird, leaf, mountain for blog posts
- Generate meditation scene for about page
- Generate email icon for signup
```

Save to appropriate directories:
- Headers → `src/ascii-assets/headers/*.txt`
- Art → `src/ascii-assets/art/*.txt`

Commit all assets to repo.

### Step 2: Build Components

**Create `src/components/AsciiHeader.astro`:**
- Read from `headers/*.txt` files at build time (static imports)
- Accept props: `text`, `align`, `level` (h1/h2)
- Wrap in semantic heading with aria-label containing actual text
- Apply responsive CSS classes

**Create `src/components/AsciiArt.astro`:**
- Read from `art/*.txt` files at build time (static imports)
- Accept props: `name`, `position`, `opacity`
- Wrap in `<figure>` with `aria-hidden="true"`
- Apply responsive CSS classes

**Create corresponding CSS:**
- `src/styles/components/ascii-header.css`
- `src/styles/components/ascii-art.css`
- `src/styles/components/ascii-animations.css`

### Step 3: Update Pages

Systematically integrate into each page:

1. **Homepage** (`src/pages/index.astro`)
   - Import components
   - Add hero bird
   - Replace "Latest from the blog" with `<AsciiHeader>`
   - Add tree divider
   - Replace email section title with `<AsciiHeader>`
   - Add email icon accent

2. **Plugin Index** (`src/pages/plugins/index.astro`)
   - Replace "Tools that work" with `<AsciiHeader text="TOOLS" />` + light "that work"
   - Add plugin background watermark

3. **Blog Index** (`src/pages/blog/index.astro`)
   - Add `<AsciiHeader text="BLOG" />`

4. **Blog Posts** (`src/pages/blog/[...slug].astro`)
   - Add rotating `<AsciiArt>` at top (bird/leaf/mountain)

5. **About Page** (`src/pages/about.astro`)
   - Add contemplative scene `<AsciiArt>`

Adjust spacing/margins to accommodate new visual elements.

### Step 4: Add Animations

**Create `src/styles/components/ascii-animations.css`:**
- Define `.ascii-animate` and `.ascii-visible` classes
- Intersection Observer setup (similar to existing plugin card animation)
- Stagger timing configuration

**Update page scripts:**
- Apply animation classes to ASCII elements
- Set up observers with appropriate thresholds

### Step 5: Dark Mode & Accessibility Testing

**Dark Mode:**
- Test all opacity levels in both light and dark modes
- May need 5-10% higher opacity in dark mode for same visual weight
- Verify `var(--color-text)` adapts correctly

**Accessibility:**
- Verify screen readers read header text (not ASCII characters)
- Confirm decorative pieces are `aria-hidden="true"`
- Maintain color contrast ratios for functional text
- Test keyboard navigation not affected

## Testing Checklist

- [ ] All ASCII assets generated and committed
- [ ] Components built and tested in isolation
- [ ] Homepage integration complete
- [ ] Plugin index integration complete
- [ ] Blog pages integration complete
- [ ] About page integration complete
- [ ] Animations working smoothly
- [ ] Mobile responsive behavior correct (large pieces hidden)
- [ ] Dark mode appearance acceptable
- [ ] Screen reader testing passed
- [ ] Performance impact minimal (pre-generated assets)
- [ ] Visual balance maintained (minimal aesthetic preserved)

## Success Criteria

- ASCII art is bold and present without overwhelming content
- Site maintains minimal aesthetic with lots of white space
- Zen/organic elements add human warmth to technical theme
- All accessibility standards maintained
- No performance degradation
- Cohesive visual identity across all pages
- Users perceive Channel 47 as visually distinctive and sophisticated
