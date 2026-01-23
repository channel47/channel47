# Color Reference

## Why Most AI Palettes Fail

AI-generated color palettes converge on the same safe choices:
- Purple/violet gradients on white backgrounds
- Teal (#008275) paired with beige/cream
- Soft pastels with no dominant color
- "Friendly" palettes that say nothing

These feel generic because they **lack conviction**. Great color has a point of view.

---

## Building Palettes That Work

### Principle 1: Pick ONE Dominant

Every palette needs a hero. The rest are supporting cast.

**Not this**:
```
Blue 20%, Green 20%, Orange 20%, Purple 20%, Gray 20%
```

**This**:
```
Near-black 70%, White 25%, Single accent 5%
```

### Principle 0: Add Warmth to Your Neutrals

**The cold/sterile problem**: Pure black (#000000) and pure white (#ffffff) create a clinical, impersonal feel. Pure grays (equal RGB values) lack character.

**The fix**: Add a subtle warm hue (10-20 on the HSL hue scale) to all neutrals:

```css
/* Instead of cold neutrals */
--gray-900: #171717;  /* True neutral */

/* Use warm neutrals */
--gray-900: hsl(20, 10%, 9%);  /* Warm charcoal */
```

This single change makes the entire palette feel more human and considered.

### Principle 2: Neutrals Are the Foundation

Most of your interface is neutrals. Get these right first.

**The Neutral Spectrum**:
```css
/* Warm neutrals (editorial, luxury) */
--gray-50: #faf9f7;
--gray-100: #f0eeeb;
--gray-200: #e4e1dc;
--gray-400: #a8a29e;
--gray-600: #57534e;
--gray-800: #292524;
--gray-900: #1c1917;

/* Cool neutrals (technical, modern) */
--gray-50: #f8fafc;
--gray-100: #f1f5f9;
--gray-200: #e2e8f0;
--gray-400: #94a3b8;
--gray-600: #475569;
--gray-800: #1e293b;
--gray-900: #0f172a;

/* True neutrals (minimal, stark) */
--gray-50: #fafafa;
--gray-100: #f5f5f5;
--gray-200: #e5e5e5;
--gray-400: #a3a3a3;
--gray-600: #525252;
--gray-800: #262626;
--gray-900: #171717;
```

### Principle 3: Accent Colors Earn Their Place

An accent color should appear in **less than 10%** of the design.

Where accents work:
- Primary CTAs
- Active/selected states
- Key data highlights
- Brand moments (logo, etc.)

Where accents don't work:
- Section backgrounds
- Headers
- Most borders

---

## Palette Templates

### The Dark Editorial

Best for: Technical products, developer tools, media sites

```css
:root {
  /* Surfaces */
  --surface-primary: #0a0a0a;
  --surface-secondary: #141414;
  --surface-elevated: #1a1a1a;
  
  /* Text */
  --text-primary: #fafafa;
  --text-secondary: #a3a3a3;
  --text-muted: #525252;
  
  /* Accent: pick ONE */
  --accent: #3b82f6;  /* Blue */
  /* OR */
  --accent: #22c55e;  /* Green */
  /* OR */
  --accent: #f97316;  /* Orange */
  
  /* Borders */
  --border-subtle: #262626;
  --border-default: #404040;
}
```

**Examples**: Linear, Vercel, Raycast

### The Light Minimal

Best for: Portfolios, agencies, luxury brands

```css
:root {
  /* Surfaces */
  --surface-primary: #ffffff;
  --surface-secondary: #fafafa;
  --surface-elevated: #ffffff;
  
  /* Text */
  --text-primary: #0a0a0a;
  --text-secondary: #525252;
  --text-muted: #a3a3a3;
  
  /* Accent: often black or very dark */
  --accent: #0a0a0a;
  
  /* Borders */
  --border-subtle: #f5f5f5;
  --border-default: #e5e5e5;
}
```

**Examples**: Apple, Nothing, Stripe (some pages)

### The Warm Editorial

Best for: Content platforms, media, editorial brands

```css
:root {
  /* Surfaces - warm undertones */
  --surface-primary: #faf9f7;
  --surface-secondary: #f5f3f0;
  --surface-elevated: #ffffff;
  
  /* Text */
  --text-primary: #1c1917;
  --text-secondary: #57534e;
  --text-muted: #a8a29e;
  
  /* Accent: earthy or muted */
  --accent: #b45309;  /* Warm amber */
  /* OR */
  --accent: #166534;  /* Forest green */
  
  /* Borders */
  --border-subtle: #e7e5e4;
  --border-default: #d6d3d1;
}
```

**Examples**: Substack, Medium, some Gumroad pages

### The Bold Accent

Best for: Product launches, campaigns, brands with strong color identity

```css
:root {
  /* Surfaces - mostly neutral */
  --surface-primary: #ffffff;
  --surface-secondary: #f5f5f5;
  --surface-accent: #4f46e5;  /* Used sparingly */
  
  /* Text */
  --text-primary: #111827;
  --text-secondary: #6b7280;
  --text-inverse: #ffffff;
  
  /* Accent: bold and confident */
  --accent: #4f46e5;  /* Indigo */
  --accent-hover: #4338ca;
  
  /* The accent ONLY appears in: */
  /* - Primary buttons */
  /* - Links */
  /* - Selected states */
}
```

---

## Color in Practice

### Buttons

```css
/* Primary - uses accent */
.btn-primary {
  background: var(--accent);
  color: var(--text-inverse);
}

/* Secondary - neutral */
.btn-secondary {
  background: var(--surface-secondary);
  color: var(--text-primary);
  border: 1px solid var(--border-default);
}

/* Ghost - minimal */
.btn-ghost {
  background: transparent;
  color: var(--text-primary);
}
```

### Cards

```css
.card {
  background: var(--surface-elevated);
  border: 1px solid var(--border-subtle);
  /* Avoid colored cards unless part of brand system */
}

/* If you need visual distinction, use border or shadow */
.card-featured {
  border-color: var(--accent);
  /* OR */
  box-shadow: 0 0 0 1px var(--accent);
}
```

### Section Backgrounds

Alternate between `surface-primary` and `surface-secondary` for rhythm:

```astro
<section class="bg-primary">...</section>
<section class="bg-secondary">...</section>
<section class="bg-primary">...</section>
```

**Avoid**: Using your accent color as a section background. It's almost never necessary.

---

## Dark Mode Considerations

### Token-Based Switching

```css
:root {
  --surface-primary: #ffffff;
  --text-primary: #0a0a0a;
}

:root.dark {
  --surface-primary: #0a0a0a;
  --text-primary: #fafafa;
}
```

### What Stays Constant

Some colors shouldn't invert:
- Brand accent colors
- Status colors (error, success, warning)
- Image treatments

### Contrast Requirements

- **Body text**: Minimum 4.5:1 contrast ratio
- **Large text (18px+)**: Minimum 3:1
- **UI components**: Minimum 3:1

Check with: https://webaim.org/resources/contrastchecker/

---

## Gradients (Use Sparingly)

### When Gradients Work

- Background atmosphere (subtle)
- Highlighting premium features
- As part of established brand identity

### When Gradients Fail

- Primary UI elements
- Replacing solid accent colors
- "Looking modern" without purpose

### If You Must Gradient

```css
/* Subtle background gradient */
.gradient-bg {
  background: linear-gradient(
    180deg,
    var(--surface-primary) 0%,
    var(--surface-secondary) 100%
  );
}

/* NOT this AI slop */
.gradient-bad {
  background: linear-gradient(
    135deg,
    #667eea 0%,
    #764ba2 100%
  );
}
```

---

## Color Anti-Patterns

### The Purple Gradient

This is the default AI slop color scheme. Avoid at all costs:
```css
/* DON'T */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

### The Teal + Beige

Another AI default that screams "generated":
```css
/* DON'T */
--accent: #008275;
--background: #faf5f0;
```

### Too Many Colors

If you have more than 3 distinct hues, you probably have too many:
```css
/* DON'T */
--blue: ...;
--green: ...;
--orange: ...;
--purple: ...;
--pink: ...;
/* This is chaos, not a palette */
```

### Safe, Timid Pastels

Soft colors that don't commit:
```css
/* DON'T */
--accent: #a5b4fc;  /* Washed out indigo */
--secondary: #fbcfe8;  /* Washed out pink */
/* Neither is confident enough to be the hero */
```

---

## Quick Palette Generator

**Step 1**: Choose your neutrals (warm, cool, or true)

**Step 2**: Choose ONE accent color

**Step 3**: Verify contrast ratios

**Step 4**: Define where accent appears (should be <10% of UI)

**Step 5**: Resist adding more colors

That's it. Most great editorial sites use fewer than 5 distinct colors.
