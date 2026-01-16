# Form Patterns

Form elements, labels, inputs, and validation patterns.

---

## Form Field Architecture

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

## Form Styling Patterns

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

## Form Anti-Patterns to Avoid

- **Placeholder as label** — Always use real `<label>` elements
- **Inline validation on every keystroke** — Validate on blur or submit
- **Error messages that don't explain the fix** — "Invalid email" -> "Enter a valid email address"
- **Required asterisks everywhere** — Mark optional fields instead if most are required
