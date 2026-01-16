# Component Patterns

Distinctive approaches to common UI components.

For detailed patterns, see the specific component files:

| Component | Reference |
|-----------|-----------|
| Buttons | @buttons.md — Button styles, states, variants |
| Forms | @forms.md — Form fields, labels, inputs, validation |
| Cards | @cards.md — Card containers, interactive patterns |
| Navigation | @navigation.md — Top nav, sidebar, link patterns |
| Modals | @modals.md — Dialog patterns using native `<dialog>` |

## General Principles

- **Pick ONE visual treatment** — Don't combine shadow + border + radius on everything
- **State changes should be singular** — Hover does ONE thing, not three
- **Accessibility first** — Real labels, focus states, keyboard support
- **Consistency over novelty** — All components should share a design language
