# Responsive Design

Breakpoints, fluid typography, fluid spacing, and container queries.

---

## Breakpoint Strategy

```css
/* Mobile-first approach */
:root {
  --breakpoint-sm: 640px;
  --breakpoint-md: 768px;
  --breakpoint-lg: 1024px;
  --breakpoint-xl: 1280px;
  --breakpoint-2xl: 1536px;
}

/* Base styles = mobile */
.component { }

/* Progressively enhance */
@media (min-width: 768px) {
  .component { }
}

@media (min-width: 1024px) {
  .component { }
}
```

## Fluid Typography

```css
/* Don't use fixed sizes */
h1 {
  font-size: clamp(2rem, 5vw + 1rem, 4rem);
}

/* Scale */
--font-size-display: clamp(2.5rem, 8vw, 6rem);
--font-size-heading: clamp(1.5rem, 4vw, 2.5rem);
--font-size-body: clamp(1rem, 2vw, 1.125rem);
```

## Fluid Spacing

```css
.section {
  padding-block: clamp(var(--space-12), 8vw, var(--space-24));
  padding-inline: clamp(var(--space-4), 4vw, var(--space-12));
}
```

## Container Queries

```css
/* Define container */
.card-wrapper {
  container-type: inline-size;
  container-name: card;
}

/* Query container, not viewport */
@container card (min-width: 400px) {
  .card {
    flex-direction: row;
  }
}
```
