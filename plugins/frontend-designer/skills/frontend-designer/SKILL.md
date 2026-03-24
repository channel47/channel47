---
name: frontend-designer
description: "Orchestrated frontend design and build workflow — from design system to polished, reviewed UI. This skill should be used when the user wants to build a complete page or component through a structured design process, or says 'design and build', 'frontend workflow', 'build a page from scratch', 'full design process', or wants the complete discover-scout-design-build-polish-review pipeline. For individual tasks (just polish, just a component, just a review), use the specific skill instead."
---

# Frontend Designer — Structured Design & Build Workflow

A deliberate workflow for designing and building web UIs. Follows the sequence: understand, scout, design system, plan, build, polish, review.

Not every task needs every phase. Match the process to the scope.

## Workflow Shortcuts

| Task | Phases |
|------|--------|
| New page from scratch | All phases |
| New component | Discovery, Scout, Design System, Build, Polish, Summary |
| Polish existing page | Polish, Review, Summary |
| Design system setup | Discovery, Scout, Design System, Summary |
| Visual audit only | Scout, Review |
| Quick component fix | Build only |

## Phase 1: Discovery

Understand what we're building before writing code.

If the user provided a description, clarify:
- What type of page/component is this? (landing, dashboard, settings, component, etc.)
- What's the primary user action?
- Any brand/visual references or inspiration?
- Is this a new project or extending an existing one?

If no description provided, ask: "What are we building today?"

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

**If it exists:** Read it. Confirm with the user that it should be followed.

**If it doesn't exist:** Ask:
> "This project doesn't have a formal design system. Would you like to create one now, or should I work with the patterns the pattern-scout found?"

If creating one, invoke the `design-system` skill. If working with existing patterns, extract the implicit system from the scout report.

## Phase 4: Layout Planning

For page-level work (not individual components), plan the layout before building:

1. **Identify the page type** — landing, dashboard, editorial, directory, settings, app page
2. **Map the density rhythm** — sketch HIGH/MEDIUM/LOW zones:

```
SECTION 1 [HIGH]   Hero / main content
SECTION 2 [LOW]    Breathing space
SECTION 3 [MEDIUM] Features / content
SECTION 4 [LOW]    Testimonial / quote
SECTION 5 [HIGH]   CTA
```

3. **Place the rupture** — one moment that breaks the pattern
4. **Choose container widths** for each section
5. **Define responsive behavior** — what happens on mobile?

Present the plan to the user. Get approval before building.

## Phase 5: Implementation

### For Pages:
1. **Page shell** — layout structure, navigation, containers
2. **Sections** — top to bottom, one at a time
3. **Components within sections** — build or reuse as needed
4. **Responsive** — mobile adjustments at each step (don't leave for later)
5. **Dark mode** — if applicable, implement alongside (not as a separate pass)

### For Components:
1. **Semantic HTML** — choose the right base element
2. **Variants** — define with cva or equivalent
3. **States** — default, hover, focus-visible, disabled, active
4. **Accessibility** — labels, ARIA, keyboard behavior
5. **Transitions** — smooth state changes with design system motion tokens

### Rules During Implementation:
- Every color, spacing, radius, and shadow value comes from the design system
- `forwardRef` on all React components wrapping native elements
- `className` prop accepted and merged via `cn()`
- Mobile-first: base styles = mobile, add breakpoints upward
- No hardcoded values. If a value isn't in the design system, flag it.

## Phase 6: Polish Pass

After the core build is complete, run through:

1. **Interactive states** — every clickable element has hover, focus, active, disabled
2. **Transitions** — all state changes animate smoothly (150-300ms)
3. **Loading states** — skeleton screens for async content
4. **Empty states** — designed empty states for lists and data areas
5. **Error states** — helpful error messages with recovery actions
6. **Edge cases** — long text, missing images, single items in grids
7. **Micro-interactions** — 1-2 moments of delight per page

If significant polish is needed, invoke the `polish` skill for detailed guidance.

## Phase 7: Review

Launch two parallel reviews:

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

After review findings are addressed, present:

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
