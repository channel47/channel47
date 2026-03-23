---
description: Orchestrated frontend design and build workflow — from design system to polished, reviewed UI
argument-hint: Optional description of what to build (e.g., "pricing page", "settings dashboard", "hero section")
---

# Frontend Craft

A structured workflow for designing and building beautiful web UIs. Follows a deliberate sequence: understand → design system → plan → build → polish → review.

## Phase 1: Discovery

Understand what we're building before writing code.

1. If the user provided a description (argument), clarify:
   - What type of page/component is this? (landing, dashboard, settings, component, etc.)
   - What's the primary user action on this page?
   - Any brand/visual references or inspiration?
   - Is this a new project or extending an existing one?

2. If no description provided, ask:
   - "What are we building today?"

Keep discovery to 2-3 targeted questions. Don't interrogate.

## Phase 2: Codebase Exploration

Launch the **pattern-scout** agent to analyze the existing codebase:

```
Agent: pattern-scout
Task: "Analyze this project's existing design patterns — colors, typography, spacing, components, layout conventions. Report what exists so we can build consistently."
```

Review the scout's findings. Understand what patterns exist before adding to them.

## Phase 3: Design System Check

Check if a `.design-system.json` exists in the project root.

**If it exists:** Read it. Confirm with the user that we should follow it.

**If it doesn't exist:** Ask the user:
> "This project doesn't have a formal design system. Would you like to create one now, or should I work with the patterns the pattern-scout found?"

If creating one, invoke the `design-system` skill to generate `.design-system.json`.

If working with existing patterns, extract the implicit system from the scout report and use it as the reference.

## Phase 4: Layout Planning

For page-level work (not individual components), plan the layout before building:

1. **Identify the page type** — landing, dashboard, editorial, directory, settings, app page
2. **Map the density rhythm** — sketch HIGH/MEDIUM/LOW zones with ASCII:

```
SECTION 1 [HIGH]   ████████████████  Hero / main content
SECTION 2 [LOW]    ████████          Breathing space
SECTION 3 [MEDIUM] ██████████████    Features / content
SECTION 4 [LOW]    ████████          Testimonial / quote
SECTION 5 [HIGH]   ████████████████  CTA
```

3. **Place the rupture** — one moment that breaks the pattern
4. **Choose container widths** for each section
5. **Define responsive behavior** — what happens on mobile?

Present the plan to the user. Get approval before building.

## Phase 5: Implementation

Build the UI. Follow this order:

### For Pages:
1. **Page shell** — Layout structure, navigation, containers
2. **Sections** — Top to bottom, one section at a time
3. **Components within sections** — Build or reuse as needed
4. **Responsive** — Mobile adjustments at each step (don't leave for later)
5. **Dark mode** — If applicable, implement alongside (not as a separate pass)

### For Components:
1. **Semantic HTML** — Choose the right base element
2. **Variants** — Define with cva or equivalent
3. **States** — Default, hover, focus-visible, disabled, active
4. **Accessibility** — Labels, ARIA, keyboard behavior
5. **Transitions** — Smooth state changes with design system motion tokens

### Rules During Implementation:
- Every color, spacing, radius, and shadow value comes from the design system
- `forwardRef` on all React components wrapping native elements
- `className` prop accepted and merged via `cn()`
- Mobile-first: base styles = mobile, add breakpoints upward
- No hardcoded values. If a value isn't in the design system, flag it.

## Phase 6: Polish Pass

After the core build is complete, run through the polish checklist:

1. **Interactive states** — Verify every clickable element has hover, focus, active, disabled
2. **Transitions** — All state changes animate smoothly (150-300ms)
3. **Loading states** — Skeleton screens for async content
4. **Empty states** — Designed empty states for lists and data areas
5. **Error states** — Helpful error messages with recovery actions
6. **Edge cases** — Long text, missing images, single items in grids
7. **Micro-interactions** — 1-2 moments of delight per page (copy feedback, count animation, success state)

If significant polish is needed, invoke the `polish` skill for detailed guidance.

## Phase 7: Review

Launch two parallel review agents:

**Design Critic:**
```
Agent: design-critic
Task: "Review [files] for visual quality, spacing consistency, color usage, typography hierarchy, and interactive states. Report findings at 70+ confidence only."
```

**Accessibility Quick-Check:**
Read the key files and check for:
- Heading hierarchy (one h1, no skipped levels)
- All images have alt text
- All inputs have labels
- Focus indicators visible
- Color not used as sole indicator

For a deep accessibility audit, suggest the user run the `accessibility` skill separately.

## Phase 8: Summary

After review findings are addressed, summarize:

```markdown
## Built

### What was created
- [List of files created/modified with brief descriptions]

### Design system
- [Tokens used, any new tokens added]

### Key decisions
- [Layout choices, component patterns, notable trade-offs]

### Review results
- [Findings addressed, any deferred items]

### Next steps
- [Polish items remaining, accessibility deep-dive, responsive testing]
```

---

## Workflow Shortcuts

Not every task needs all 8 phases. Adapt based on scope:

| Task | Phases |
|------|--------|
| New page from scratch | All 8 |
| New component | 1, 2, 3, 5, 6, 8 (skip layout planning and full review) |
| Polish existing page | 6, 7, 8 (go straight to polish and review) |
| Design system setup | 1, 2, 3, 8 (discovery, scout, generate system, summarize) |
| Visual audit only | 2, 7 (scout existing patterns, run design critic) |
| Quick component fix | 5 only (just build it) |

Match the process to the task. Don't run 8 phases for a button variant.
