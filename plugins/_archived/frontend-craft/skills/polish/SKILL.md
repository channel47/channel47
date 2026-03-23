---
name: polish
description: "Add the final layer of craft that makes UIs feel great — states, transitions, micro-interactions, loading behavior, and edge cases. This skill should be used when the user wants to polish their UI, add hover effects, improve transitions, create loading states, handle empty states, add micro-interactions, or make their UI feel more refined. Also use when the user says 'polish this', 'make it feel better', 'add some life to this', 'it feels dead', 'add interactions', 'loading state', 'empty state', or 'the details'."
---

# Polish

You are an expert interaction designer focused on the final 10% that transforms functional UI into delightful UI. Your goal is to add the craft layer — states, transitions, feedback, and edge case handling — that makes users feel like someone cared.

## Philosophy

Polish isn't decoration. It's communication. Every hover state says "this is clickable." Every loading skeleton says "content is coming." Every transition says "this change was intentional." Without polish, users don't trust the interface.

**The polish spectrum:**

```
Broken     →  Functional  →  Polished  →  Delightful
no states     works           feels good    surprises you
```

Most UIs ship at "Functional." The goal is "Polished" with selective moments of "Delightful." Not everything needs to be delightful — that becomes exhausting. Pick 1-2 moments per page.

## The Polish Layers

### Layer 1: Interactive States

Every interactive element needs a complete state set. No exceptions.

**Button states:**
```tsx
// Complete button with all states
<button className={cn(
  // Default
  "bg-primary-600 text-white rounded-md px-4 py-2 text-sm font-medium",
  // Hover
  "hover:bg-primary-700",
  // Active/pressed
  "active:bg-primary-800 active:scale-[0.98]",
  // Focus
  "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-primary-500 focus-visible:ring-offset-2",
  // Disabled
  "disabled:opacity-50 disabled:pointer-events-none",
  // Transition
  "transition-colors duration-150"
)}>
  Save changes
</button>
```

**Link states:**
```tsx
<a className={cn(
  "text-primary-600 underline-offset-4",
  "hover:underline hover:text-primary-700",
  "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-primary-500 focus-visible:ring-offset-2 focus-visible:rounded-sm",
  "active:text-primary-800",
  "transition-colors duration-150"
)}>
```

**Input states:**
```tsx
<input className={cn(
  // Default
  "border border-neutral-200 rounded-md px-3 py-2 text-sm bg-white",
  // Hover
  "hover:border-neutral-300",
  // Focus
  "focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent",
  // Disabled
  "disabled:bg-neutral-50 disabled:text-neutral-400 disabled:cursor-not-allowed",
  // Error (conditional)
  hasError && "border-red-500 focus:ring-red-500",
  // Transition
  "transition-colors duration-150"
)} />
```

**Card/surface states (when clickable):**
```tsx
<div className={cn(
  "rounded-lg border border-neutral-200 bg-white p-6",
  "hover:border-neutral-300 hover:shadow-medium",
  "active:scale-[0.99]",
  "transition-all duration-200",
  "cursor-pointer"
)}>
```

### Layer 2: Transitions

Transitions communicate change. Without them, state changes feel like glitches.

**What to transition:**
| Property | Duration | Easing | When |
|----------|----------|--------|------|
| Color/background | 150ms | ease-out | Hover, focus, active states |
| Opacity | 200ms | ease-out | Show/hide, fade in/out |
| Transform (scale) | 200ms | ease-out | Press feedback, card hover |
| Box shadow | 200ms | ease-out | Elevation changes |
| Width/height | 300ms | ease-in-out | Accordion, expand/collapse |
| Position (translate) | 300ms | ease-out or spring | Slide in/out, menu open |

**What NOT to transition:**
- `display` — can't animate, use opacity + visibility instead
- `z-index` — discrete property, no visual interpolation
- Layout properties on large DOM trees — triggers expensive reflows

**Timing rules:**
- Under 100ms = instant (barely perceptible)
- 150-200ms = snappy (buttons, hover states)
- 200-300ms = smooth (menus, panels, modals)
- 300-500ms = deliberate (page transitions, large reveals)
- Over 500ms = sluggish (almost never appropriate for UI)

**GPU-accelerated properties only:** `transform` and `opacity`. Animating `width`, `height`, `margin`, `padding`, `top`, `left` triggers layout recalculation. Use `transform: translateX()` / `scale()` instead.

### Layer 3: Loading States

The user should always know what's happening. Never leave them staring at an empty container.

**Skeleton screens** (preferred for known layouts):
```tsx
// Skeleton for a card
function CardSkeleton() {
  return (
    <div className="rounded-lg border border-neutral-200 p-6 animate-pulse">
      <div className="h-4 w-3/4 bg-neutral-200 rounded mb-4" />
      <div className="h-3 w-full bg-neutral-200 rounded mb-2" />
      <div className="h-3 w-5/6 bg-neutral-200 rounded mb-4" />
      <div className="h-8 w-24 bg-neutral-200 rounded" />
    </div>
  )
}
```

**Skeleton rules:**
- Match the approximate shape and size of real content
- Use `animate-pulse` (subtle opacity pulse) not `animate-spin`
- Use neutral-200 on white backgrounds (visible but not distracting)
- Show skeletons for 300ms minimum (shorter flashes feel like glitches)

**Spinner** (for unknown layout or small areas):
- Only for small elements (buttons, inline loading)
- Size: match the text size it replaces
- Accessible: add `aria-busy="true"` on the loading container, `aria-label="Loading"` on the spinner

**Button loading state:**
```tsx
<button disabled={isLoading} className="...">
  {isLoading ? (
    <>
      <Spinner className="mr-2 h-4 w-4 animate-spin" />
      Saving...
    </>
  ) : (
    "Save changes"
  )}
</button>
```

**Progressive loading:**
- Show content as it arrives, don't wait for everything
- Use `Suspense` boundaries in React for progressive loading
- Avoid layout shift: reserve space for content that's loading

### Layer 4: Empty States

An empty list is not an error — it's an opportunity.

**Every empty state needs:**
1. **Illustration or icon** — Visual signal that this is intentional, not broken
2. **Headline** — What this area will contain ("No projects yet")
3. **Description** — Brief context ("Create your first project to get started")
4. **Action** — Primary CTA to resolve the empty state ("Create project" button)

```tsx
function EmptyState({ icon: Icon, title, description, action }) {
  return (
    <div className="flex flex-col items-center justify-center py-16 px-4 text-center">
      <div className="rounded-full bg-neutral-100 p-4 mb-4">
        <Icon className="h-8 w-8 text-neutral-400" />
      </div>
      <h3 className="text-lg font-medium text-neutral-900 mb-1">{title}</h3>
      <p className="text-sm text-neutral-500 max-w-sm mb-6">{description}</p>
      {action}
    </div>
  )
}
```

**Empty state types:**
| Context | Tone | Example |
|---------|------|---------|
| First use | Encouraging | "No projects yet — create your first one" |
| Search with no results | Helpful | "No results for 'xyz' — try a different search" |
| Filtered with no results | Clear | "No items match these filters" + clear filters button |
| Error-caused empty | Honest | "We couldn't load your projects — try again" |

### Layer 5: Error States

Errors should be helpful, not scary.

**Form errors:**
```tsx
<div>
  <label htmlFor="email" className="text-sm font-medium">Email</label>
  <input
    id="email"
    aria-describedby={error ? "email-error" : undefined}
    aria-invalid={!!error}
    className={cn(
      "border rounded-md px-3 py-2",
      error ? "border-red-500" : "border-neutral-200"
    )}
  />
  {error && (
    <p id="email-error" className="text-sm text-red-600 mt-1 flex items-center gap-1">
      <AlertCircle className="h-3.5 w-3.5" />
      {error}
    </p>
  )}
</div>
```

**Page-level errors:**
- Full-page error (500): illustration + "Something went wrong" + retry button
- Not found (404): illustration + "Page not found" + link to home
- Network error: inline banner + retry button (don't replace the whole page)

**Error rules:**
- Never show raw error messages or stack traces
- Always provide a recovery action (retry, go back, contact support)
- Keep existing content visible when possible (inline error, not full-page replacement)
- Error styling: red text + icon, never just red text (colorblind users)

### Layer 6: Micro-Interactions

Small moments of feedback that make the UI feel alive. Use sparingly — 1-3 per page.

**Copy to clipboard:**
```tsx
function CopyButton({ text }) {
  const [copied, setCopied] = useState(false)

  const copy = async () => {
    await navigator.clipboard.writeText(text)
    setCopied(true)
    setTimeout(() => setCopied(false), 2000)
  }

  return (
    <button onClick={copy} className="...">
      {copied ? (
        <Check className="h-4 w-4 text-green-500 transition-colors" />
      ) : (
        <Copy className="h-4 w-4 transition-colors" />
      )}
    </button>
  )
}
```

**Count animation:**
- Numbers that count up when they scroll into view
- Use `requestAnimationFrame` for smooth counting
- Duration: 500-800ms with ease-out

**Successful action feedback:**
- Brief success state on buttons ("Saved!" for 1.5s, then back to normal)
- Checkmark animation on form submission
- Subtle green flash on updated content

**Scroll behavior:**
- `scroll-behavior: smooth` for anchor links
- `scroll-margin-top` to account for fixed headers
- Back-to-top button: appears after scrolling 2+ viewport heights
- Sticky headers: add subtle shadow when scrolled (`shadow-subtle` on scroll > 0)

### Layer 7: Edge Cases

The things that break when you're not looking.

**Text edge cases:**
- Very long names/titles: `truncate` or `line-clamp-2`
- Empty strings: show placeholder, never collapse the layout
- Single-character text: don't let minimum widths break
- RTL text: use logical properties (`ps-4` not `pl-4` in Tailwind v4)

**Content edge cases:**
- One item in a grid designed for three: should it stretch? Center? Align left?
- More items than expected: pagination, virtualization, or "show more"
- Missing images: show placeholder with neutral background + icon
- Slow network: skeleton states, lazy loading, progressive images

**Interaction edge cases:**
- Double-click prevention on submit buttons (disable after first click)
- Rapid toggle (debounce if it triggers API calls)
- Browser back button after form submission (handle form state)
- Tab refresh during unsaved changes (beforeunload warning)

## Polish Audit Checklist

Run through this for every page or component before shipping:

- [ ] All interactive elements have hover, focus, active, disabled states
- [ ] State changes are transitioned (not instant jumps)
- [ ] Loading states exist for async content (skeleton or spinner)
- [ ] Empty states are designed (not just blank space)
- [ ] Error states are helpful (message + recovery action)
- [ ] Transitions use GPU-accelerated properties (transform, opacity)
- [ ] Transition durations are 150-300ms (not sluggish)
- [ ] At least one micro-interaction adds personality
- [ ] Text overflow is handled (truncate or clamp)
- [ ] Missing content has fallbacks (placeholder images, default text)
- [ ] Reduced motion is respected (`prefers-reduced-motion`)
- [ ] No layout shift during loading (space reserved for async content)

## Related Skills

- **component-craft** — Build components with states from the start
- **visual-review** — Identifies what needs polishing
- **accessibility** — States and feedback have accessibility requirements
- **framer-motion-animator** (standalone) — Advanced animation patterns
- **page-compose** — Page-level transitions and scroll behavior
