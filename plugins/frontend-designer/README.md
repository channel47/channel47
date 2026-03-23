# frontend-designer

Design, build, review, and polish beautiful web UIs — from design system to final animation. 7 skills, 2 agents, and a design token hook.

Part of [channel47](https://channel47.dev), open-source role-based plugins for Claude Code.

## What it does

A complete frontend design workflow covering design systems, component building, page composition, accessibility, responsive design, polish, and visual review.

## Install

```
claude plugin install frontend-designer@channel47
```

## Skills

| Skill | Auto-triggers on |
|-------|-----------------|
| design-system | creating design tokens, color palettes, typography scales |
| component-craft | building UI components, buttons, cards, modals |
| page-compose | building pages, layouts, dashboards |
| polish | adding hover effects, transitions, loading states |
| responsive | fixing mobile layout, testing breakpoints |
| accessibility | checking a11y, WCAG compliance, keyboard navigation |
| visual-review | reviewing UI for visual quality and design consistency |

## Command

| Command | What it does |
|---------|-------------|
| `/frontend-designer [description]` | Full orchestrated workflow: discover, scout, design system, plan, build, polish, review |

## Agents

- **design-critic** — reviews visual quality, spacing, color usage, typography hierarchy
- **pattern-scout** — analyzes existing codebase for design patterns and conventions

## Hook

**PostToolUse** on `Write|Edit` — checks frontend files for hardcoded colors, spacing values, and missing focus styles. Flags design system violations.

## License

MIT
