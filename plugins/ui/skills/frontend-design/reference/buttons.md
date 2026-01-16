# Button Patterns

Distinctive approaches to button styling and states.

---

## The Problem with Default Buttons

AI-generated buttons tend toward:
- Blue primary + gray secondary
- Rounded corners + shadow + border (all three)
- Generic hover (darken 10%)
- Identical sizing ratios

## Distinctive Button Approaches

### Brutalist

```css
.button {
  background: var(--color-text-primary);
  color: var(--color-bg);
  border: 3px solid var(--color-text-primary);
  padding: 1rem 2rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  transition: transform 100ms var(--ease-out);
}

.button:hover {
  transform: translate(-4px, -4px);
  box-shadow: 4px 4px 0 var(--color-text-primary);
}

.button:active {
  transform: translate(0, 0);
  box-shadow: none;
}
```

### Minimal/Swiss

```css
.button {
  background: transparent;
  color: var(--color-text-primary);
  border: 1px solid currentColor;
  padding: 0.75rem 1.5rem;
  font-weight: 500;
  letter-spacing: 0.02em;
  transition: background 150ms var(--ease-out), color 150ms var(--ease-out);
}

.button:hover {
  background: var(--color-text-primary);
  color: var(--color-bg);
}
```

### Technical/Dev

```css
.button {
  background: var(--color-surface);
  color: var(--color-text-primary);
  border: 1px solid var(--color-border);
  padding: 0.5rem 1rem;
  font-family: var(--font-mono);
  font-size: 0.875rem;
  border-radius: 4px;
  transition: border-color 150ms var(--ease-out);
}

.button:hover {
  border-color: var(--color-accent);
}

.button::before {
  content: '>';
  margin-right: 0.5rem;
  opacity: 0;
  transition: opacity 150ms var(--ease-out);
}

.button:hover::before {
  opacity: 1;
}
```

## Button State Guidelines

| State | Purpose | Implementation |
|-------|---------|----------------|
| **Default** | Primary appearance | Base styles |
| **Hover** | Affordance, interactivity | ONE change (not multiple) |
| **Active/Pressed** | Feedback during click | Quick, subtle (translate, darken) |
| **Focus** | Keyboard navigation | Visible outline, high contrast |
| **Disabled** | Unavailable action | Reduced opacity, cursor change |
| **Loading** | Async operation in progress | Spinner or skeleton, disabled interaction |

## Variant Philosophy

Don't create 6 variants. Create 2-3 with clear purposes:

- **Primary** — The ONE action you want users to take
- **Secondary** — Supporting actions, de-emphasized
- **Destructive** (if needed) — Dangerous actions, red tint

Skip: ghost, outline, link, tertiary, quaternary. Less is more.
