# Menerals.com Design Analysis

## Key Findings from Playwright Inspection

### CSS Patterns

**clamp() Usage for Fluid Typography:**
- Title large: `clamp(var(--sp-12), 4.73vw, var(--sp-23))`
- Title XL: `clamp(var(--sp-20), 6.737vw, var(--sp-32))`
- Button SM padding: `clamp(var(--sp-3), 1.2vw, var(--sp-4)) clamp(var(--sp-5), 1.473vw, var(--sp-6))`
- Button LG padding: `clamp(var(--sp-6), 1.2vw, var(--sp-7)) clamp(var(--sp-8), 1.473vw, var(--sp-9))`

Pattern: `clamp(min-value, preferred-vw, max-value)`

### Layout Patterns

**Full-screen Sections:**
- Hero section with video background
- Dark background (#171717 / rgb(23,23,23))
- Minimal padding on section containers
- Content centered within sections

**Spacing Values:**
- Uses CSS custom properties for spacing scale
- Responsive spacing with clamp()
- Common pattern: 2-8rem for section padding

### Animation Patterns

**Scroll-triggered reveals:**
- Opacity transitions
- Transform transitions (translateY, scale)
- Timing: 0.5-1s ease-out typical
- Intersection Observer for detection

### Typography

**Copy Rhythm:**
- Large headlines: 2-4.5rem range with clamp
- Body copy: 1-2rem range
- Line breaks for emphasis
- Short, punchy sentences
- Progressive disclosure through scrolling

### Color & Effects

**Background:**
- Dark base: rgb(23,23,23)
- Overlay opacity: 0.3-0.7 range for video overlays

**Accent:**
- Primary highlight: Yellow (#FFCE00)
- Text contrast: White on dark

### Responsive Strategy

**Breakpoint:**
- Desktop changes at 1024px min-width
- Mobile-first approach
- Fluid scaling between breakpoints

## Implementation Notes for Channel 47

1. **Adopt clamp() for fluid typography** throughout
2. **Full-screen sections** (min-height: 100vh)
3. **Generous spacing** - don't be afraid of whitespace
4. **Short copy lines** - break for emphasis
5. **Scroll reveals** - use Intersection Observer
6. **Dark background** with subtle overlays
7. **Terminal accents** - green glow instead of yellow

## Screenshots Captured

- `menerals-hero-section.png` - Hero with video background
