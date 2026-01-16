# Theming

Dark mode, theme switching, and color scheme management.

---

## System Preference Detection

```css
@media (prefers-color-scheme: dark) {
  :root {
    --color-bg: #0a0a0a;
    --color-surface: #171717;
    --color-surface-elevated: #262626;

    --color-text-primary: #fafafa;
    --color-text-secondary: #a3a3a3;
    --color-text-tertiary: #525252;

    --color-border: #262626;
    --color-border-strong: #404040;

    /* Accent may need adjustment for contrast */
    --color-accent-subtle: #431407;
  }
}
```

## Manual Toggle Support

```css
/* Light mode explicit */
[data-theme="light"] {
  --color-bg: #fafafa;
  /* ... light colors */
}

/* Dark mode explicit */
[data-theme="dark"] {
  --color-bg: #0a0a0a;
  /* ... dark colors */
}

/* System default (no data-theme attribute) */
@media (prefers-color-scheme: dark) {
  :root:not([data-theme]) {
    --color-bg: #0a0a0a;
    /* ... dark colors */
  }
}
```

## Toggle Implementation

```typescript
function ThemeToggle() {
  const [theme, setTheme] = useState<'light' | 'dark' | 'system'>('system');

  useEffect(() => {
    const root = document.documentElement;
    if (theme === 'system') {
      root.removeAttribute('data-theme');
    } else {
      root.setAttribute('data-theme', theme);
    }
    localStorage.setItem('theme', theme);
  }, [theme]);

  useEffect(() => {
    const saved = localStorage.getItem('theme') as typeof theme;
    if (saved) setTheme(saved);
  }, []);

  return (
    <select value={theme} onChange={e => setTheme(e.target.value as typeof theme)}>
      <option value="system">System</option>
      <option value="light">Light</option>
      <option value="dark">Dark</option>
    </select>
  );
}
```

## Dark Mode Design Principles

1. **Not inversion** — Dark mode is a separate, intentional palette
2. **Elevation = lightness** — In dark mode, elevated surfaces are LIGHTER
3. **Reduce contrast slightly** — Pure white (#fff) on dark is harsh; use #fafafa or #e5e5e5
4. **Accent colors may need adjustment** — Some colors look different on dark backgrounds
5. **Shadows become less visible** — Consider borders or lighter surfaces instead
