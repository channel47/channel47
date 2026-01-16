# Component Patterns

Distinctive approaches to common UI components.

---

## Buttons

### The Problem with Default Buttons

AI-generated buttons tend toward:
- Blue primary + gray secondary
- Rounded corners + shadow + border (all three)
- Generic hover (darken 10%)
- Identical sizing ratios

### Distinctive Button Approaches

#### Brutalist

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

#### Minimal/Swiss

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

#### Technical/Dev

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

### Button State Guidelines

| State | Purpose | Implementation |
|-------|---------|----------------|
| **Default** | Primary appearance | Base styles |
| **Hover** | Affordance, interactivity | ONE change (not multiple) |
| **Active/Pressed** | Feedback during click | Quick, subtle (translate, darken) |
| **Focus** | Keyboard navigation | Visible outline, high contrast |
| **Disabled** | Unavailable action | Reduced opacity, cursor change |
| **Loading** | Async operation in progress | Spinner or skeleton, disabled interaction |

### Variant Philosophy

Don't create 6 variants. Create 2-3 with clear purposes:

- **Primary** — The ONE action you want users to take
- **Secondary** — Supporting actions, de-emphasized
- **Destructive** (if needed) — Dangerous actions, red tint

Skip: ghost, outline, link, tertiary, quaternary. Less is more.

---

## Forms

### Form Field Architecture

```tsx
interface FormFieldProps {
  label: string;
  name: string;
  type?: 'text' | 'email' | 'password' | 'textarea';
  error?: string;
  hint?: string;
}

function FormField({ label, name, type = 'text', error, hint }: FormFieldProps) {
  return (
    <div className="form-field" data-error={!!error}>
      <label htmlFor={name} className="form-label">
        {label}
      </label>
      <input
        id={name}
        name={name}
        type={type}
        className="form-input"
        aria-describedby={error ? `${name}-error` : hint ? `${name}-hint` : undefined}
        aria-invalid={!!error}
      />
      {hint && !error && (
        <span id={`${name}-hint`} className="form-hint">{hint}</span>
      )}
      {error && (
        <span id={`${name}-error`} className="form-error" role="alert">{error}</span>
      )}
    </div>
  );
}
```

### Form Styling Patterns

```css
.form-field {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.form-label {
  font-size: 0.875rem;
  font-weight: 500;
  color: var(--color-text-secondary);
}

.form-input {
  padding: 0.75rem 1rem;
  font-size: 1rem;
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: 4px;
  transition: border-color 150ms var(--ease-out), box-shadow 150ms var(--ease-out);
}

.form-input:focus {
  outline: none;
  border-color: var(--color-accent);
  box-shadow: 0 0 0 3px var(--color-accent-subtle);
}

.form-field[data-error="true"] .form-input {
  border-color: var(--color-error);
}

.form-hint {
  font-size: 0.75rem;
  color: var(--color-text-tertiary);
}

.form-error {
  font-size: 0.75rem;
  color: var(--color-error);
}
```

### Form Anti-Patterns to Avoid

- **Placeholder as label** — Always use real `<label>` elements
- **Inline validation on every keystroke** — Validate on blur or submit
- **Error messages that don't explain the fix** — "Invalid email" → "Enter a valid email address"
- **Required asterisks everywhere** — Mark optional fields instead if most are required

---

## Cards

### Card Architecture

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

### Interactive Cards

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

---

## Navigation

### Top Navigation

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

### Sidebar Navigation

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

---

## Modals & Dialogs

### Native Dialog Element

```tsx
function Modal({ open, onClose, title, children }: ModalProps) {
  const dialogRef = useRef<HTMLDialogElement>(null);

  useEffect(() => {
    const dialog = dialogRef.current;
    if (!dialog) return;

    if (open) {
      dialog.showModal();
    } else {
      dialog.close();
    }
  }, [open]);

  return (
    <dialog ref={dialogRef} className="modal" onClose={onClose}>
      <header className="modal-header">
        <h2 className="modal-title">{title}</h2>
        <button className="modal-close" onClick={onClose} aria-label="Close">
          <CloseIcon />
        </button>
      </header>
      <div className="modal-content">{children}</div>
    </dialog>
  );
}
```

```css
.modal {
  max-width: 500px;
  width: 90vw;
  padding: 0;
  border: none;
  border-radius: 8px;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
}

.modal::backdrop {
  background: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(4px);
}

.modal-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1.25rem 1.5rem;
  border-bottom: 1px solid var(--color-border);
}

.modal-title {
  font-size: 1.125rem;
  font-weight: 600;
  margin: 0;
}

.modal-close {
  padding: 0.5rem;
  background: transparent;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  color: var(--color-text-tertiary);
  transition: color 150ms var(--ease-out), background 150ms var(--ease-out);
}

.modal-close:hover {
  background: var(--color-surface);
  color: var(--color-text-primary);
}

.modal-content {
  padding: 1.5rem;
}
```

### Modal Anti-Patterns

- **Don't use modals for confirmations** — Use inline confirmation or toast
- **Don't nest modals** — Redesign the flow
- **Don't auto-open modals** — Users hate unexpected interruptions
- **Don't trap focus incorrectly** — Use native `<dialog>` or proper focus management
