# Card Patterns

Card containers, variants, and interactive patterns.

---

## Card Architecture

Cards are containers. They should NOT be:
- Decorated with shadow + border + radius simultaneously
- Identical to every other card on the page
- Click targets without visual affordance

```css
/* Option A: Elevated (shadow, no border) */
.card-elevated {
  background: var(--color-surface-elevated);
  border-radius: 8px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1), 0 1px 2px rgba(0, 0, 0, 0.06);
  padding: 1.5rem;
}

/* Option B: Bordered (border, no shadow) */
.card-bordered {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: 8px;
  padding: 1.5rem;
}

/* Option C: Subtle (minimal distinction) */
.card-subtle {
  background: var(--color-surface);
  padding: 1.5rem;
}
```

## Interactive Cards

```css
.card-interactive {
  /* Pick ONE of the base styles above */
  cursor: pointer;
  transition: transform 200ms var(--ease-out), box-shadow 200ms var(--ease-out);
}

.card-interactive:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.card-interactive:active {
  transform: translateY(0);
}

/* Keyboard focus */
.card-interactive:focus-visible {
  outline: 2px solid var(--color-accent);
  outline-offset: 2px;
}
```
