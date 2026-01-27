# Design Recipes

Detailed patterns for common UI challenges. Reference when building specific component types.

## Landing Page Recipe

### Structure That Breaks Expectation

Instead of the template flow (hero → features → testimonials → CTA), create rhythm:

```jsx
export default function LandingPage() {
  return (
    <main>
      {/* 1. Statement — not a "hero", a declaration */}
      <section className="min-h-[80vh] flex items-end pb-24 px-6">
        <h1 className="font-serif text-[clamp(3rem,10vw,8rem)] leading-[0.9] tracking-tighter max-w-4xl">
          Design tools for people who care about details
        </h1>
      </section>

      {/* 2. Proof — immediately, before features */}
      <section className="bg-black text-white py-2 overflow-hidden">
        <div className="flex gap-8 animate-marquee">
          {logos.map((logo) => (
            <img key={logo} src={logo} className="h-6 opacity-60" />
          ))}
        </div>
      </section>

      {/* 3. Show, don't tell — demo/visual, not feature list */}
      <section className="py-24">
        <div className="max-w-6xl mx-auto px-6">
          <InteractiveDemo />
        </div>
      </section>

      {/* 4. Sparse features — 2-3 max, with real depth */}
      <section className="grid md:grid-cols-2 border-t border-black">
        <FeatureDeep />
        <FeatureDeep />
      </section>

      {/* 5. Social proof woven in, not isolated */}
      <section className="max-w-2xl mx-auto px-6 py-24">
        <blockquote className="font-serif text-2xl">
          "Quote that sounds human, not marketing."
        </blockquote>
        <cite className="block mt-4 text-sm text-gray-500">— Name, Role</cite>
      </section>

      {/* 6. Close with confidence, not desperation */}
      <section className="border-t border-black py-24 text-center">
        <p className="text-sm uppercase tracking-widest text-gray-500 mb-4">
          Ready?
        </p>
        <a
          href="/start"
          className="text-2xl underline underline-offset-4 hover:no-underline"
        >
          Get started
        </a>
      </section>
    </main>
  );
}
```

### Key Principles

- Lead with the boldest statement, not explanations
- Proof before promises
- Depth over breadth in features
- Quotes should sound like humans, not press releases
- CTAs show confidence (underline link) not anxiety (giant gradient button)

## Editorial/Blog Recipe

### Typography-First Layout

```jsx
export default function Article({ title, date, content }) {
  return (
    <article>
      {/* Masthead with tension */}
      <header className="pt-24 pb-16 px-6">
        <div className="max-w-2xl mx-auto">
          <time className="font-mono text-xs uppercase tracking-widest text-gray-400">
            {date}
          </time>
          <h1 className="font-serif text-5xl md:text-6xl tracking-tight mt-4 leading-[1.1]">
            {title}
          </h1>
        </div>
      </header>

      {/* Full-bleed image breaks the container */}
      <figure className="w-full aspect-[21/9] bg-gray-100">
        <img src="/hero.jpg" className="w-full h-full object-cover" />
      </figure>

      {/* Body with optimal reading width */}
      <div className="max-w-2xl mx-auto px-6 py-16">
        <div className="prose prose-lg prose-gray">
          {/* 
            Prose styles:
            - Body: 18-20px, 1.7 line-height
            - Paragraphs: 1.5em margin between
            - Links: underline, no color change
            - Code: subtle background, monospace
            - Blockquotes: left border, italic, indented
          */}
          {content}
        </div>
      </div>

      {/* End mark */}
      <div className="text-center py-16">
        <span className="text-2xl">◆</span>
      </div>
    </article>
  );
}
```

### Pull Quote Pattern

```jsx
{
  /* Break reading rhythm with a pull quote */
}
<aside className="my-16 -mx-6 md:-mx-24 px-6 md:px-24 py-12 bg-black text-white">
  <p className="font-serif text-3xl md:text-4xl leading-snug max-w-3xl">
    "The key insight goes here — something worth pausing for."
  </p>
</aside>;
```

## Directory/List Recipe

### Dense but Scannable

```jsx
export default function Directory({ items }) {
  return (
    <div className="divide-y divide-gray-200">
      {items.map((item) => (
        <a
          key={item.id}
          href={item.url}
          className="group flex items-baseline justify-between py-4 px-6 hover:bg-gray-50 transition-colors duration-100"
        >
          <div className="flex items-baseline gap-4">
            <span className="font-mono text-xs text-gray-400 w-8">
              {item.index.toString().padStart(2, "0")}
            </span>
            <span className="font-medium group-hover:underline">
              {item.title}
            </span>
            {item.tag && (
              <span className="text-xs uppercase tracking-wider text-gray-400">
                {item.tag}
              </span>
            )}
          </div>
          <span className="text-sm text-gray-400">{item.meta}</span>
        </a>
      ))}
    </div>
  );
}
```

### Card Grid (When Cards Are Actually Right)

Cards work for: distinct items with images, comparable options, portfolio pieces.

```jsx
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-px bg-gray-200">
  {items.map((item) => (
    <article key={item.id} className="bg-white p-6 group">
      {/* Image with consistent aspect ratio */}
      <div className="aspect-[4/3] bg-gray-100 mb-4 overflow-hidden">
        <img
          src={item.image}
          className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
        />
      </div>

      {/* Minimal text */}
      <h3 className="font-medium">{item.title}</h3>
      <p className="text-sm text-gray-500 mt-1">{item.description}</p>
    </article>
  ))}
</div>
```

Note: `gap-px bg-gray-200` creates 1px borders between cards without actual borders.

## Button Hierarchy

```jsx
{
  /* Primary — one per view */
}
<button className="bg-black text-white px-6 py-3 text-sm font-medium hover:bg-gray-800 transition-colors">
  Primary Action
</button>;

{
  /* Secondary — supporting actions */
}
<button className="border border-black px-6 py-3 text-sm font-medium hover:bg-black hover:text-white transition-colors">
  Secondary Action
</button>;

{
  /* Tertiary — navigation, less important */
}
<button className="text-sm font-medium underline underline-offset-4 hover:no-underline">
  Tertiary Action
</button>;

{
  /* Ghost — icon buttons, close buttons */
}
<button className="p-2 hover:bg-gray-100 rounded transition-colors">
  <Icon />
</button>;
```

## Form Patterns

### Text Input

```jsx
<div>
  <label className="block text-sm font-medium mb-2">Email</label>
  <input
    type="email"
    className="w-full px-4 py-3 border border-gray-300 focus:border-black focus:outline-none transition-colors"
    placeholder="you@example.com"
  />
  <p className="text-xs text-gray-500 mt-2">We'll never share your email.</p>
</div>
```

### Checkbox

```jsx
<label className="flex items-start gap-3 cursor-pointer">
  <input
    type="checkbox"
    className="mt-1 w-4 h-4 border-gray-300 rounded-none focus:ring-0 focus:ring-offset-0 checked:bg-black"
  />
  <span className="text-sm">
    I agree to the{" "}
    <a href="/terms" className="underline">
      terms
    </a>
  </span>
</label>
```

## Animation Snippets

### Staggered Entrance

```jsx
{
  items.map((item, i) => (
    <div
      key={item.id}
      className="animate-in fade-in slide-in-from-bottom-4"
      style={{ animationDelay: `${i * 100}ms`, animationFillMode: "backwards" }}
    >
      {item.content}
    </div>
  ));
}
```

### Hover Reveal

```jsx
<div className="group relative overflow-hidden">
  <img
    src={image}
    className="transition-transform duration-500 group-hover:scale-105"
  />
  <div className="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center">
    <span className="text-white">View Project</span>
  </div>
</div>
```

### Smooth Expand

```jsx
const [open, setOpen] = useState(false)

<div>
  <button onClick={() => setOpen(!open)}>Toggle</button>
  <div
    className="grid transition-all duration-300 ease-out"
    style={{ gridTemplateRows: open ? '1fr' : '0fr' }}
  >
    <div className="overflow-hidden">
      <div className="py-4">{content}</div>
    </div>
  </div>
</div>
```

## Dark Mode Done Right

Don't just invert. Reduce contrast and add depth:

```jsx
// Light: white bg, black text, gray accents
// Dark: NOT black bg — use dark gray for depth

<div
  className="
  bg-white text-black
  dark:bg-[#1a1a1a] dark:text-[#e5e5e5]
"
>
  {/* Surfaces in dark mode should layer */}
  <div
    className="
    bg-gray-50
    dark:bg-[#252525]
  "
  >
    {/* Borders get subtler */}
    <div
      className="
      border border-gray-200
      dark:border-[#333]
    "
    >
      Content
    </div>
  </div>
</div>
```

## Responsive Breakpoints

Don't just stack — redesign:

```jsx
{
  /* Mobile: single column, touch-friendly */
}
{
  /* Desktop: denser, hover states */
}

<nav
  className="
  {/* Mobile: bottom bar */}
  fixed bottom-0 left-0 right-0 border-t bg-white p-4
  flex justify-around
  
  {/* Desktop: sidebar */}
  md:static md:border-t-0 md:border-r md:h-screen md:w-64
  md:flex-col md:justify-start md:p-6 md:gap-2
"
>
  <NavItems />
</nav>;
```
