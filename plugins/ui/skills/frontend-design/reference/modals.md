# Modal & Dialog Patterns

Modal dialogs using native `<dialog>` element.

---

## Native Dialog Element

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

## Modal Anti-Patterns

- **Don't use modals for confirmations** — Use inline confirmation or toast
- **Don't nest modals** — Redesign the flow
- **Don't auto-open modals** — Users hate unexpected interruptions
- **Don't trap focus incorrectly** — Use native `<dialog>` or proper focus management
