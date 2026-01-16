# Navigation Patterns

Top navigation, sidebar navigation, and link patterns.

---

## Top Navigation

```tsx
function Navigation({ items, currentPath }: { items: NavItem[]; currentPath: string }) {
  return (
    <nav className="nav" aria-label="Main navigation">
      <a href="/" className="nav-logo">
        {/* Logo component */}
      </a>
      <ul className="nav-items">
        {items.map(item => (
          <li key={item.href}>
            <a
              href={item.href}
              className="nav-link"
              aria-current={currentPath === item.href ? 'page' : undefined}
            >
              {item.label}
            </a>
          </li>
        ))}
      </ul>
    </nav>
  );
}
```

```css
.nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem 2rem;
  background: var(--color-bg);
  border-bottom: 1px solid var(--color-border);
}

.nav-items {
  display: flex;
  gap: 2rem;
  list-style: none;
  margin: 0;
  padding: 0;
}

.nav-link {
  color: var(--color-text-secondary);
  text-decoration: none;
  font-size: 0.875rem;
  font-weight: 500;
  transition: color 150ms var(--ease-out);
}

.nav-link:hover,
.nav-link[aria-current="page"] {
  color: var(--color-text-primary);
}

.nav-link[aria-current="page"] {
  position: relative;
}

.nav-link[aria-current="page"]::after {
  content: '';
  position: absolute;
  bottom: -0.5rem;
  left: 0;
  right: 0;
  height: 2px;
  background: var(--color-accent);
}
```

## Sidebar Navigation

```css
.sidebar {
  width: 250px;
  padding: 1.5rem;
  background: var(--color-surface);
  border-right: 1px solid var(--color-border);
  height: 100vh;
  overflow-y: auto;
}

.sidebar-section {
  margin-bottom: 2rem;
}

.sidebar-heading {
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--color-text-tertiary);
  margin-bottom: 0.75rem;
}

.sidebar-link {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.5rem 0.75rem;
  margin: 0 -0.75rem;
  color: var(--color-text-secondary);
  text-decoration: none;
  font-size: 0.875rem;
  border-radius: 4px;
  transition: background 150ms var(--ease-out), color 150ms var(--ease-out);
}

.sidebar-link:hover {
  background: var(--color-surface-elevated);
  color: var(--color-text-primary);
}

.sidebar-link[aria-current="page"] {
  background: var(--color-accent-subtle);
  color: var(--color-accent);
}
```
