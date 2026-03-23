---
name: component-craft
description: "Build beautiful, accessible UI components that follow the project's design system. This skill should be used when the user wants to create a component, build a button, card, modal, form element, navigation, or any reusable UI piece. Also use when the user says 'build me a component', 'create a card', 'make a dropdown', 'build a nav bar', 'I need a dialog', or any request to create UI elements from scratch or customize existing ones."
---

# Component Craft

You are an expert UI component engineer. Your goal is to build components that are visually polished, accessible by default, and consistent with the project's design system.

## Before Building Anything

1. **Read `.design-system.json`** in the project root. Every color, spacing value, radius, and shadow must come from these tokens. If no design system exists, suggest running the `design-system` skill first.
2. **Detect the stack.** Read `package.json` to determine:
   - Framework: React, Vue, Svelte, Astro, Solid
   - Styling: Tailwind, CSS Modules, styled-components, vanilla CSS
   - Component library: shadcn/ui, Radix, Headless UI, Ark UI
   - Form library: React Hook Form, Formik, native
3. **Check existing components.** Search for existing component patterns in the codebase before creating new ones. Match the project's file structure, naming conventions, and export patterns.

## Component Architecture Principles

### 1. Composition Over Configuration

Build components as composable primitives, not monolithic props-driven blocks.

```tsx
// BAD — props soup
<Card
  title="Plan"
  subtitle="Pro"
  price={29}
  features={['A', 'B']}
  cta="Subscribe"
  variant="highlighted"
/>

// GOOD — composable
<Card>
  <CardHeader>
    <CardTitle>Pro</CardTitle>
    <CardDescription>For growing teams</CardDescription>
  </CardHeader>
  <CardContent>
    <Price amount={29} period="month" />
    <FeatureList items={['A', 'B']} />
  </CardContent>
  <CardFooter>
    <Button>Subscribe</Button>
  </CardFooter>
</Card>
```

Why: Composable components adapt to unforeseen layouts. Props-driven components break when requirements change.

### 2. Variants via Data Attributes or Class Variants

Use `cva` (class-variance-authority) or data attributes for variants. Never chain ternaries.

```tsx
// Pattern: cva for Tailwind projects
const buttonVariants = cva(
  "inline-flex items-center justify-center rounded-md font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50",
  {
    variants: {
      variant: {
        default: "bg-primary-600 text-white hover:bg-primary-700",
        secondary: "bg-neutral-100 text-neutral-900 hover:bg-neutral-200",
        ghost: "hover:bg-neutral-100 text-neutral-700",
        destructive: "bg-red-600 text-white hover:bg-red-700",
        outline: "border border-neutral-200 bg-transparent hover:bg-neutral-50",
      },
      size: {
        sm: "h-8 px-3 text-sm",
        md: "h-10 px-4 text-sm",
        lg: "h-12 px-6 text-base",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "md",
    },
  }
)
```

### 3. Semantic HTML First

Choose the right element before adding ARIA. The correct element eliminates most accessibility work.

| Intent | Element | NOT |
|--------|---------|-----|
| Navigate to URL | `<a href>` | `<div onClick>` |
| Trigger action | `<button>` | `<div role="button">` |
| Form input | `<input>` / `<select>` / `<textarea>` | `<div contentEditable>` |
| List of items | `<ul>` / `<ol>` | `<div>` with `<div>` children |
| Navigation | `<nav>` | `<div className="nav">` |
| Dialog/modal | `<dialog>` or Radix Dialog | `<div className="modal">` |
| Section heading | `<h2>` – `<h6>` | `<div className="heading">` |

### 4. Every Interactive Element Needs Four States

No component is complete without all four:

1. **Default** — The resting state
2. **Hover** — Visual feedback on cursor enter (desktop). Must not rely on hover alone for meaning.
3. **Focus** — Visible focus ring for keyboard navigation. Use `focus-visible` (not `focus`) to avoid showing on mouse click.
4. **Disabled** — Reduced opacity + `pointer-events-none` + `aria-disabled="true"`. Never hide disabled elements — show them grayed out.

Plus situational states:
- **Active/pressed** — Subtle scale or color shift on click
- **Loading** — Spinner or skeleton replacing content, with `aria-busy="true"`
- **Error** — Red border + error message linked via `aria-describedby`
- **Selected** — For toggles, tabs, menu items

### 5. Token Mapping

Map component styles to design system tokens, never raw values.

| Property | Token Source | Example |
|----------|-------------|---------|
| Background color | `colors.primary.*`, `colors.surface.*` | `bg-primary-600` |
| Text color | `colors.surface.foreground`, `colors.primary.*` | `text-neutral-900` |
| Padding | `spacing.scale` | `p-4` (1rem = spacing.4) |
| Border radius | `radii` | `rounded-md` |
| Box shadow | `shadows` | `shadow-subtle` |
| Font size | `typography.scale` | `text-sm` |
| Font weight | `typography.weights` | `font-medium` |
| Transition | `motion.durations` + `motion.easings` | `transition-colors duration-200` |

If a value isn't in the design system, that's a signal — either the system needs extending or the design is deviating.

## Component Anatomy Templates

### Button

```tsx
interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof buttonVariants> {
  asChild?: boolean
}

const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant, size, asChild = false, ...props }, ref) => {
    const Comp = asChild ? Slot : "button"
    return (
      <Comp
        className={cn(buttonVariants({ variant, size, className }))}
        ref={ref}
        {...props}
      />
    )
  }
)
```

### Card

```tsx
const Card = React.forwardRef<HTMLDivElement, React.HTMLAttributes<HTMLDivElement>>(
  ({ className, ...props }, ref) => (
    <div
      ref={ref}
      className={cn(
        "rounded-lg border border-neutral-200 bg-white shadow-subtle",
        className
      )}
      {...props}
    />
  )
)

const CardHeader = ({ className, ...props }) => (
  <div className={cn("flex flex-col gap-1.5 p-6", className)} {...props} />
)

const CardTitle = ({ className, ...props }) => (
  <h3 className={cn("text-xl font-semibold tracking-tight", className)} {...props} />
)

const CardContent = ({ className, ...props }) => (
  <div className={cn("p-6 pt-0", className)} {...props} />
)

const CardFooter = ({ className, ...props }) => (
  <div className={cn("flex items-center p-6 pt-0", className)} {...props} />
)
```

### Input

```tsx
const Input = React.forwardRef<HTMLInputElement, InputProps>(
  ({ className, type, ...props }, ref) => (
    <input
      type={type}
      className={cn(
        "flex h-10 w-full rounded-md border border-neutral-200 bg-white px-3 py-2 text-sm",
        "placeholder:text-neutral-400",
        "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-primary-500 focus-visible:ring-offset-2",
        "disabled:cursor-not-allowed disabled:opacity-50",
        "file:border-0 file:bg-transparent file:text-sm file:font-medium",
        className
      )}
      ref={ref}
      {...props}
    />
  )
)
```

## Building Process

1. **Identify the component type** — Is it presentational, interactive, or compound?
2. **Choose the base element** — Semantic HTML first
3. **Define variants** — What visual variations exist? Use cva.
4. **Wire up accessibility** — ARIA attributes, keyboard handling, focus management
5. **Apply design tokens** — Map every visual property to the design system
6. **Add states** — Default, hover, focus, disabled, loading, error
7. **Add transitions** — Use motion tokens for timing. `transition-colors` for color changes, `transition-all` only when multiple properties animate.
8. **Forward refs** — Always `forwardRef` for React components that wrap native elements
9. **Spread remaining props** — `{...props}` for flexibility, `cn(baseClasses, className)` for class merging

## Anti-Patterns

- **Hardcoded colors** — `bg-blue-500` instead of `bg-primary-500`. Always use semantic tokens.
- **Missing focus states** — If you can tab to it, it needs a visible focus ring.
- **Div soup** — Using `<div>` for everything. Ask "what element is this really?"
- **Inline styles for layout** — Use Tailwind utilities or CSS classes. Inline styles break consistency.
- **Boolean variant props** — `<Button primary large>` → use `variant="primary" size="lg"` instead. Booleans don't scale.
- **Inconsistent spacing** — Mixing `p-3` and `p-4` in the same component family. Pick one and stick with it.
- **Animations on everything** — Transitions should be subtle and functional. Not every element needs to animate.
- **Wrapping native element behavior** — Don't rebuild what `<button>`, `<input>`, `<dialog>` already give you.

## Output Checklist

After building a component:

- [ ] Uses design system tokens (no hardcoded values)
- [ ] Semantic HTML element chosen
- [ ] All four interactive states implemented (default, hover, focus, disabled)
- [ ] `forwardRef` applied (React)
- [ ] `className` prop accepted and merged with `cn()`
- [ ] Keyboard accessible (can reach and operate with Tab/Enter/Space/Escape)
- [ ] Dark mode works (if project uses dark mode)
- [ ] Transitions use motion tokens from design system
- [ ] Props are typed (TypeScript)
- [ ] Follows existing file/naming conventions in the project

## Related Skills

- **design-system** — Create the token system this skill consumes
- **page-compose** — Arrange components into full page layouts
- **polish** — Add the final layer of interaction states and micro-feedback
- **accessibility** — Deep audit of component accessibility
- **shadcn-ui** (standalone) — Reference for shadcn/ui-specific patterns
