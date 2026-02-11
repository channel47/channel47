---
name: frontend-design
description: "This skill should be used when building web components, pages, artifacts, posters, dashboards, React components, HTML/CSS layouts, or styling any web UI for channel47. Covers the full design system including motion, animation, scroll effects, micro-interactions, and choreography. Triggers on: build a page, website, landing page, dashboard, component, style, beautify, frontend, UI, web design, artifact, animation, motion, scroll effect, hover effect, micro-interaction, entrance animation, ch47, channel47."
---

# Frontend Design. ch47.

Every interface from here should feel built by someone with opinions. Not "designed" in the portfolio sense. Built. Tight joints, honest materials, at least one moment that makes someone stop scrolling.

The aesthetic lives in tension. Bones are industrial (monospace, dark surfaces, hard edges). Spirit is human (warm accents, considered rhythm, type that breathes). Most AI design fails because it hedges. Everything medium-warm, medium-spaced, medium-safe. ch47 builds with contrast. Dense next to sparse. Loud next to silent. Dark next to a single hot accent. The contrast IS the design.

The metaphor: a broadcast station, not a bookshop.

## Materials

### Surface (Dark First)

Default is dark. Warm near-black with depth.

```
Void       #0C0A09    Deep background. Almost black, warm undertone.
Soot       #1C1917    Primary surface. Cards, containers.
Smoke      #292524    Elevated surface. Hover states, active areas.
Ash        #44403C    Borders, dividers. Barely visible structure.
Stone      #78716C    Secondary text, metadata.
Dust       #A8A29E    Tertiary text. Timestamps, placeholders.
Bone       #E7E5E4    Primary text on dark.
Chalk      #F5F0EB    High-emphasis text. Headlines, key data.

Light mode:
Canvas     #FAF7F2    Light background. Warm cream.
Paper      #F0EBE3    Alt sections. Recessed.
Ink        #1C1917    Primary text on light.
```

No pure white (#FFFFFF). No pure black (#000000). No cool grays. No blue tints. Tailwind `gray-*` banned. Use `stone-*` or hex directly.

### Accent (One Color, One Purpose)

One hot accent. Active, important, interactive. Not decoration.

```
Signal     #F59E0B    Primary accent everywhere. Links, active states, the pulse.
Signal-dim #B45309    Muted borders, subtle emphasis on dark surfaces only.
Signal-wash #451A03   Dark tinted background. Selection, highlight on dark.
```

Signal (#F59E0B) is the accent on both dark AND light surfaces. Do not swap to Signal-dim on light. The warmth of #F59E0B reads well against cream (#FAF7F2) at the sizes used (small labels, thin bars, underlines). Consistency across surfaces is more important than dimming for contrast.

Signal in 2-4 places per view. If everywhere, it's noise. If nowhere, page is dead.

**Flare (#FB923C) is removed.** One accent color. No secondary warm tone. Flare created confusion between "important" and "really important." Signal handles both.

### Type (Two Voices + One Guest)

Monospace leads. That's the identity.

**The Terminal** (Primary)
`'JetBrains Mono', 'SF Mono', 'Cascadia Code', monospace`
Default voice. Body text in short-form, all labels, metadata, navigation, UI. 14-15px body, 11-12px uppercase tracked wide for labels. This font IS the brand.

**The Broadcast** (Display)
`'Space Grotesk', 'Inter', system-ui, sans-serif`
Headlines, hero text, display moments. Geometric, slightly technical. Tight tracking on large sizes (-0.03em to -0.05em). Appears when it matters.

**The Guest** (Accent)
`'Source Serif 4', Georgia, serif`
Reserved for pull quotes in editorial long-form only. Maybe once per page, and only when the context is explicitly editorial (essays, deep dives). Its rarity gives it weight. Never use in landing pages, dashboards, or product UI.

```html
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&display=swap" rel="stylesheet">
```

### Motion

Motion is covered in detail in [references/motion.md](references/motion.md). Core principles here for quick reference:

Quick and decisive. Things arrive. They don't drift. No bounce. No elastic. No spring physics.

```
Instant    100ms    Hover, micro-interactions.
Quick      200ms    Reveals, state changes. Default.
Measured   400ms    Section transitions, key entrances.
Cinematic  700ms    Hero reveals, page loads. Rare.

Easing     cubic-bezier(0.16, 1, 0.3, 1)    Fast start, smooth land. Default.
Sharp      cubic-bezier(0.33, 1, 0.68, 1)    Snappier. Interactive elements.
```

### Hover Philosophy

Hover states are **compound, not singular**. A single property change reads as functional. Two or three properties changing in staggered cascade reads as crafted. The viewer perceives choreography.

Every hover should transition at least two properties with slightly different durations:
- Border arrives first (100ms, `ease-sharp`)
- Background/color follows (150ms, `ease-out`)
- Shadow/transform lands last (200ms, `ease-out`)

The stagger is the difference between "this changes on hover" and "this responds to me." Cards get lift (`translateY(-2px)`) + border + background tint. Buttons get background morph + shadow. Text links get underline draw or color shift + arrow slide. Stats get glow. Each element type has one compound hover recipe — consistency across the site, variety between element types.

For animation patterns, hover effects, scroll reveals, and the glitch hover, see [references/motion.md](references/motion.md).

### Geometry

```
Border radius    0, 2px. That's it. (Exception: full-round for indicators/pills)
Shadows          Rare on dark. 0 1px 3px rgba(0,0,0,0.2) sm | 0 4px 12px rgba(0,0,0,0.25) md
Borders          1px Ash (#44403C) on dark. 1px #D6D3CD on light. 2px Signal-dim (#B45309) accent (rare).
```

## Signature Moves

### 1. The Index

Monospace counters. Small, uppercase, tracked wide. On almost everything that can be numbered. Sometimes non-sequential: `047` not `01`. `003.1` not `3`. Feels like a fragment of a larger catalog.

### 2. The Accent Bar

Thin accent line (2-3px) marking important sections. Horizontal or vertical. Always Signal color (#F59E0B). The broadcast indicator. "This is live." Appears 3-5 times per page max.

```jsx
<div style={{ width: 40, height: 2, backgroundColor: "#F59E0B", marginBottom: 20 }} />
```

### 3. The Rupture

One moment per page that breaks the pattern. Non-negotiable.

Options: **Scale** (display type, aggressive tracking). **Inversion** (dark-first page goes LIGHT for one section). **Bleed** (breaks container, edge-to-edge). **Overlap** (elements sharing grid space). **The Glitch** (CSS steps() displacement on hover). **Data** (raw numbers/code interrupting narrative). **The Void** (nearly empty, one precise element).

**Rupture coherence rule.** The rupture breaks the *rhythm*, not the *brand*. Every element in the rupture still uses the ch47 palette, type system, and accent color. A light inversion section uses Canvas (#FAF7F2) background with Ink (#1C1917) text and Signal (#F59E0B) accent. It does NOT introduce new colors, fonts, or styles. The rupture earns its impact from the contrast in surface and density, not from looking like a different site.

Rupture goes 50-70% down the page. Where expectations are set and ready to break.

### 4. The Broadcast Label

Monospace, uppercase, tracked wide, 11px. Operational, not editorial. Status indicators, not chapter titles.

Common texts: `Live`, `Build log`, `Transmitting`, `ch47`, `Notes`, `Archive`, `Status`, `Process`.

### 5. The Pipe

Vertical dividers between metadata. 1px wide, 12px tall, Ash color.

### 6. The Confident CTA

Never begs. Either a mono text link with Signal underline, or a minimal button (Signal fill, mono uppercase). Signal-fill button used at most once per page.

---

## Compositional Narrative

Materials give you the palette. Signature moves give you the vocabulary. This section is about *composing pages*. How the viewer's eye and attention moves through space over time.

### The Density Map

Every page has density zones. Not "sections." Zones of visual weight. The transitions between them are where the design happens.

**Three zones, always present:**

**HIGH** (Dense). Many elements, small type, tight spacing, grid structures, data. Stats strips, directory lists, dashboards, metadata clusters. The viewer's eye moves fast, scanning.

**MEDIUM** (Narrative). Headline and body, reasonable whitespace, one or two accent elements. Feature sections, manifesto blocks, content previews. The viewer reads.

**LOW** (Void). Extreme negative space, one precise element. A single headline. A lone CTA. An accent bar and a label. The viewer stops.

The rule: every page passes through all three densities. A page that's all medium is boring. A page that's all high is exhausting. A page that's all low is empty. The *sequence* of density zones is the page's rhythm.

**Default density sequence for a landing page:**
LOW (hero, sparse, commanding) → HIGH (proof strip, dense, credibility) → MEDIUM (features, narrative) → LOW or HIGH (rupture, density contrast with whatever came before) → MEDIUM (manifesto/story) → LOW (closing CTA, void)

**The density transition.** The moment the viewer crosses from one zone to the next should be felt, not announced. Tools: border-top (subtle), background color shift (strong), spacing change (powerful). The strongest transition is a surface flip (dark to light or light to dark) combined with a density shift. That's the rupture.

**The critical insight:** The rupture works not because it changes color. It works because it changes density AND color simultaneously. An inversion section that's the same density as the section above it doesn't feel like a rupture. It feels like a mistake.

### Hierarchy by Withdrawal

Most emphasis is additive. Bigger, bolder, brighter. ch47 also uses the opposite: emphasis by removing everything around it.

**The Void as emphasis.** A single line of 11px mono label in a field of 200px vertical padding is louder than a 5rem headline in a crowded section. The emptiness forces attention. The restraint reads as confidence.

**When to use withdrawal over addition:**
- The most important CTA on the page. Don't make it bigger. Give it more space.
- The closing statement. After a dense page, the final section should feel nearly empty.
- The single most important number in a dashboard. Don't add a border and a background and a Signal accent. Remove the other numbers. Show only the one.
- A pull quote or key observation. Don't increase font size. Give it a section alone.

**The formula:** If something is important and already in the viewer's attention path, withdraw. If it's important and the viewer might miss it, add.

### Typographic Pacing

The type scale exists. This section is about *sequencing* type sizes so they create rhythm, not just hierarchy.

**The Setup Rule.** A display headline (3rem+) earns its size through the type that precedes it. A display headline immediately following another display headline feels competitive, not hierarchical. A display headline after 20+ lines of 14px mono body text feels like a release of tension.

Before any display-scale type, ensure at least one of:
- 12+ lines of body mono text
- A broadcast label (11px, uppercase) acting as a "reset"
- A density transition (border, background shift, spacing change)

**The Descent.** Within a section, type sizes should generally descend: headline → subhead → body → metadata. Ascending within a section (body text followed by larger text) creates confusion unless it's a deliberate pull quote or rupture moment.

**The Silence.** A section with no display type at all. Just body text and labels. This section reads as intimate, workmanlike. Use it for process notes, confessions, the manifesto. It gives the surrounding display type more impact by contrast.

**Mono as equalizer.** When everything is in JetBrains Mono at the same size (14px body), hierarchy comes entirely from color and spacing. This is powerful for data-heavy sections where the content should feel flat and scannable (directories, archives, dashboards). Resist the urge to add Space Grotesk headlines in these contexts. Let mono carry it.

### Spatial Rhythm

Spacing isn't decoration. It's tempo.

**Vertical rhythm rule.** Every page should have at least two distinct vertical rhythms. Tight (16-24px between elements, used in dense zones) and open (48-80px between elements, used in narrative and void zones). Alternating between them creates the pulse.

**Asymmetric padding.** Never use the same padding top and bottom on a section unless you have a reason. Default: more padding top than bottom. This creates a feeling of "arrival" (space before) and "momentum" (less space after, pushing into the next section). Exception: the rupture, which gets equal or more padding bottom to let the viewer sit in the contrast.

**Horizontal asymmetry.** Left-aligned content with right-side negative space reads as confident and intentional. Center-aligned content reads as safe. ch47 default is left-aligned for body content, left-aligned or asymmetric for features. Center only for the closing CTA section (the void).

### Anti-Recipes

Layouts that follow every rule but feel dead, and why.

**The Polite Grid.** Three equal-width cards, equal padding, equal text length, no accent bars, same background. Follows the palette. Uses the right fonts. But nothing leads. Nothing is surprising. The eye has no entry point and no path. **Fix:** Make one card wider than the others. Or give one a Signal left-border. Or make the first card's index number 2x larger. One inequality breaks the politeness.

**The Even Page.** Every section has 80px padding top and bottom, a headline, a paragraph, and a broadcast label. Same rhythm six times. It's a drumbeat with no melody. **Fix:** Break the rhythm. Make one section 200px padding (void). Make another section borderless with no headline (just body text flowing). Let the rupture be a genuine shock, not a mild palette change.

**The Decoration Trap.** Signal accent bars on every section. Pipe dividers everywhere. Index counters on things that aren't a sequence. The signature moves become wallpaper. **Fix:** Count your accent bars. Count your pipes. If you have more than 4-5 accent elements per viewport, remove half. The ones that remain become visible again.

**The Flat Rupture.** A light inversion section that has the same padding, same layout grid, and same text density as the dark section above it. The color changed but nothing else did. It reads as a theme toggle, not a moment. **Fix:** Change density when you change surface. If the section above was a 3-column grid, the rupture should be a single wide column. If above was medium density, the rupture should be high (data, terminal mock, code) or low (single quote, one statistic).

## Process

1. **Map density first.** Before touching code, sketch the density sequence. Label each section: HIGH, MEDIUM, LOW. Check that all three appear. Check that transitions are intentional.
2. **Start dark.** Set the palette as CSS custom properties.
3. **Mono first.** Everything in JetBrains Mono. Switch to Space Grotesk only for headlines that earn their size. Serif only for editorial deep dives, never landing pages.
4. **Build with rhythm.** Alternate density, width, volume. Dense then sparse. Wide then narrow. Loud then silent. Check vertical rhythm, two tempos minimum.
5. **Place the Rupture.** Decide what it is before starting. Everything else sets it up. Keep it in-brand. Ensure it shifts density AND surface, not just color.
6. **Apply hierarchy by withdrawal.** Find the most important element. Try removing everything around it before making it bigger.
7. **Accent last.** Build in neutrals. Add Signal precisely. One link, one bar, one data point per viewport. Count the Signal placements. If more than 4, cut.
8. **Animate sparingly.** See [references/motion.md](references/motion.md) for patterns and choreography. Default: 2-4 animated elements per page, with clear lead/support roles.
9. **Anti-recipe check.** Compare against the four anti-recipes. If the page matches any of them, iterate.

## Type Scale

```
Label        11px     JetBrains Mono    uppercase, tracking: 0.15em
Body-mono    14px     JetBrains Mono    normal case, tracking: 0.02em
Body-serif   18px     Source Serif 4    line-height: 1.7 (essays only)
Section      1.75-2.5rem  Space Grotesk   tracking: -0.02em
Display      clamp(3rem+) Space Grotesk   tracking: -0.03em to -0.05em
```

## Dark / Light

Dark is default. Light is override.

```
Dark                          Light
#0C0A09 void (bg)       →    #FAF7F2 canvas
#1C1917 soot (surface)   →    #FFFFFF white card
#292524 smoke (elevated)  →    #F0EBE3 paper
#44403C ash (border)      →    #D6D3CD warm border
#78716C stone (muted)     →    #78716C stone (same)
#E7E5E4 bone (text)       →    #1C1917 ink
#F59E0B signal            →    #F59E0B signal (SAME on light)
```

Signal stays #F59E0B on both surfaces. This is a deliberate choice. The yellow reads as warm and intentional on cream. Dimming it to brown (#B45309) on light created visual incoherence between sections.

## Anti-Patterns

Kill: gradients (purple-blue-teal), rounded card grids, sans-serif-only (Inter/Roboto), predictable hero-features-testimonials-CTA flow, hover zoo (everything reacts), bounce/spring physics, cold surfaces (blue-gray), even pages (same padding everywhere), safe centered symmetric layouts, pulsing/glowing orbs, scanline overlays, particle effects, any motion that says "sci-fi UI" more than "someone built this."

**Exception: atmospheric effects.** Breathing glow (subtle brightness oscillation on accent bars), noise drift (texture translation over 8-10s), and status dot pulse are not "infinite animations" in the anti-pattern sense. They function as texture, not motion. They should be imperceptible as animation. If someone notices the breathing glow, it's too strong. See [references/motion.md](references/motion.md) for implementation.

## Responsive

Mobile simplifies, doesn't soften. Mono at 14px is legible on mobile. Touch targets 44px min. Rupture adapts, never disappears. Display type via `clamp()`. Broadcast Labels stay the same. No hover dependency.

## Recipes

For full component patterns (landing pages, directories, dashboards, forms, buttons, dark/light mode), see [references/recipes.md](references/recipes.md).

For animation patterns (entrances, scroll effects, micro-interactions, choreography sequences), see [references/motion.md](references/motion.md).

## References

Study for intent, not imitation: **Vercel** (dark-first, mono, technical confidence), **Linear** (dark UI that feels alive, micro-interactions), **Stripe** (typographic craft in technical brand), **Nothing** (dot-matrix aesthetic, constraint as identity), **Bloomberg Terminal** (max info density with hierarchy), **Teenage Engineering** (edge through restraint, weird made intentional).

## Final Test

*Does this look like it was made by a person with opinions, or by a system with defaults?*

If defaults, iterate.

*Can you trace the density map? Can you name the rupture type? Can you point to one moment of hierarchy by withdrawal?*

If you can't answer all three, the composition isn't finished.
