---
name: stunning-landing-pages
description: Create visually stunning, premium landing pages inspired by modern SaaS sites like composio.dev, linear.app, and vercel.com. Specializes in dramatic gradient backgrounds, scroll-triggered animations, mixed typography, floating UI elements, and cinematic visual effects. Use when the user wants a "wow factor" landing page that feels premium, modern, and memorable.
---

# Stunning Landing Pages

Create landing pages that make visitors stop scrolling. Premium SaaS aesthetic with cinematic visual design.

## Design DNA

This skill captures the aesthetic of modern premium SaaS landing pages characterized by:

- **Dramatic gradient backgrounds** — Radiating rays, layered panels, color transitions on scroll
- **Cinematic typography** — Serif/sans-serif mixing, extreme size contrasts, italic emphasis
- **Scroll-triggered magic** — Elements that reveal, transform, and animate as users scroll
- **Floating UI elements** — Connected diagrams, animated badges, glowing effects
- **Warm neutral foundations** — Cream/off-white backgrounds instead of pure white

## The Composio.dev Signature Elements

### 1. Radiating Gradient Backgrounds

The hero and section backgrounds use CSS gradients that create a "ray" or "sunburst" effect:

```jsx
{/* Purple/violet radiating gradient */}
<section className="relative min-h-screen overflow-hidden bg-[#FAF9F7]">
  <div 
    className="absolute inset-0"
    style={{
      background: `
        radial-gradient(ellipse 80% 50% at 50% 100%, 
          rgba(139, 92, 246, 0.3) 0%, 
          rgba(139, 92, 246, 0.1) 30%,
          transparent 70%
        )
      `,
    }}
  />
  {/* Layered ray panels - multiple semi-transparent divs rotated */}
  <div className="absolute bottom-0 left-1/2 -translate-x-1/2 w-[200%] h-[150%]">
    {[...Array(12)].map((_, i) => (
      <div
        key={i}
        className="absolute bottom-0 left-1/2 h-full w-[8%] origin-bottom"
        style={{
          transform: `translateX(-50%) rotate(${(i - 6) * 8}deg)`,
          background: `linear-gradient(to top, rgba(139, 92, 246, ${0.15 - i * 0.01}), transparent 80%)`,
        }}
      />
    ))}
  </div>
  <div className="relative z-10">{/* Content */}</div>
</section>

{/* Pink/magenta version for variety */}
<section className="relative overflow-hidden">
  <div 
    className="absolute inset-0"
    style={{
      background: `
        radial-gradient(ellipse 80% 50% at 50% 100%, 
          rgba(236, 72, 153, 0.4) 0%, 
          rgba(236, 72, 153, 0.15) 40%,
          transparent 70%
        )
      `,
    }}
  />
  {/* Curved panels instead of straight rays */}
  <div className="absolute inset-0 overflow-hidden">
    {[...Array(8)].map((_, i) => (
      <div
        key={i}
        className="absolute bottom-0 h-full"
        style={{
          left: `${i * 14}%`,
          width: '20%',
          background: `linear-gradient(to top, rgba(236, 72, 153, ${0.25 - i * 0.02}), transparent 85%)`,
          borderRadius: '50% 50% 0 0 / 20% 20% 0 0',
        }}
      />
    ))}
  </div>
</section>
```

### 2. Mixed Typography System

Headlines use serif fonts with italic emphasis, body uses clean sans-serif:

```jsx
{/* Import premium fonts */}
// In your HTML head or layout:
// <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">

{/* Design system tokens */}
const typography = {
  // Display headlines - Instrument Serif or similar elegant serif
  display: 'font-["Instrument_Serif",serif]',
  // Body text - Inter or system sans-serif  
  body: 'font-["Inter",system-ui,sans-serif]',
  // Stats/badges - JetBrains Mono or similar
  mono: 'font-["JetBrains_Mono",monospace]',
}

{/* Headline with mixed styles */}
<h1 className="text-4xl md:text-6xl lg:text-7xl tracking-tight">
  <span className="font-['Instrument_Serif',serif]">Skills that </span>
  <span className="font-['Instrument_Serif',serif] italic">evolve</span>
  <span className="font-['Instrument_Serif',serif]"> with</span>
  <br />
  <span className="font-['Instrument_Serif',serif]">your </span>
  <span className="font-sans font-semibold">Agents</span>
</h1>

{/* Supporting text with different weight */}
<p className="text-lg text-gray-600 font-['Inter',sans-serif]">
  More than just integrations, <span className="font-semibold text-black">10,000+ tools</span> that 
  can adapt — turning automation into intuition.
</p>
```

### 3. Floating Statistics Badges

Animated counters in pill-shaped badges with monospace fonts:

```jsx
function StatBadge({ label, value, suffix = '+' }) {
  const [displayValue, setDisplayValue] = useState(0)
  
  useEffect(() => {
    // Animate from 0 to value
    const duration = 2000
    const start = Date.now()
    const animate = () => {
      const elapsed = Date.now() - start
      const progress = Math.min(elapsed / duration, 1)
      // Easing function
      const eased = 1 - Math.pow(1 - progress, 3)
      setDisplayValue(Math.floor(eased * value))
      if (progress < 1) requestAnimationFrame(animate)
    }
    animate()
  }, [value])

  return (
    <div className="inline-flex items-center gap-2 px-4 py-2 bg-white rounded-full border border-gray-200 shadow-sm">
      <span className="text-sm text-gray-600">{label}</span>
      <span className="font-mono font-medium text-black">
        {displayValue.toLocaleString()}{suffix}
      </span>
    </div>
  )
}

{/* Usage with floating positioning */}
<div className="relative">
  <StatBadge label="Stars on GitHub" value={25000} className="absolute top-0 right-0" />
  <StatBadge label="Successful Calls" value={7000000} className="absolute top-20 right-10" />
  <StatBadge label="Developers" value={100000} className="absolute top-40 right-5" />
</div>
```

### 4. Scroll-Triggered Text Animation

Text elements that appear from different positions as user scrolls:

```jsx
function ScrollRevealText({ children, from = 'bottom', delay = 0 }) {
  const ref = useRef(null)
  const [isVisible, setIsVisible] = useState(false)

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => setIsVisible(entry.isIntersecting),
      { threshold: 0.1, rootMargin: '-50px' }
    )
    if (ref.current) observer.observe(ref.current)
    return () => observer.disconnect()
  }, [])

  const transforms = {
    bottom: 'translate-y-8',
    left: '-translate-x-8',
    right: 'translate-x-8',
    top: '-translate-y-8',
  }

  return (
    <div
      ref={ref}
      className={`transition-all duration-700 ease-out ${
        isVisible ? 'opacity-100 translate-x-0 translate-y-0' : `opacity-0 ${transforms[from]}`
      }`}
      style={{ transitionDelay: `${delay}ms` }}
    >
      {children}
    </div>
  )
}

{/* Scattered text that reveals on scroll */}
<section className="relative min-h-screen flex items-center justify-center">
  <h2 className="text-4xl font-serif text-center">
    Building agents that take action <em>is hard</em>
  </h2>
  
  {/* Floating context phrases */}
  <ScrollRevealText from="left" delay={200} className="absolute left-[15%] top-[30%]">
    <span className="font-mono text-sm text-gray-400">building integrations</span>
  </ScrollRevealText>
  
  <ScrollRevealText from="right" delay={400} className="absolute right-[15%] top-[35%]">
    <span className="font-mono text-sm text-gray-400">optimising JSON schema for agents</span>
  </ScrollRevealText>
  
  <ScrollRevealText from="left" delay={600} className="absolute left-[10%] bottom-[35%]">
    <span className="font-mono text-sm text-gray-400">managing auth and permissions</span>
  </ScrollRevealText>
  
  <ScrollRevealText from="right" delay={800} className="absolute right-[12%] bottom-[30%]">
    <span className="font-mono text-sm text-gray-400">scaling to millions of executions</span>
  </ScrollRevealText>
</section>
```

### 5. Connected Diagram Elements

Floating labels connected by curved SVG paths:

```jsx
function ConnectedDiagram() {
  return (
    <div className="relative w-full max-w-4xl mx-auto h-[400px]">
      {/* Center logo with glow effect */}
      <div className="absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2">
        <div className="relative">
          {/* Glow */}
          <div className="absolute inset-0 bg-blue-400/30 blur-xl rounded-full scale-150" />
          <div className="absolute inset-0 bg-green-400/20 blur-lg rounded-full scale-125" />
          {/* Logo */}
          <div className="relative w-16 h-16 bg-white rounded-2xl shadow-lg flex items-center justify-center">
            <Logo className="w-8 h-8" />
          </div>
        </div>
      </div>

      {/* SVG connection lines */}
      <svg className="absolute inset-0 w-full h-full" style={{ overflow: 'visible' }}>
        {/* Curved path from AI Agent badge to center */}
        <path
          d="M 150,180 Q 250,200 320,200"
          fill="none"
          stroke="#e5e5e5"
          strokeWidth="1"
        />
        {/* Curved path from center to Tools badge */}
        <path
          d="M 380,200 Q 450,220 550,280"
          fill="none"
          stroke="#e5e5e5"
          strokeWidth="1"
        />
      </svg>

      {/* Floating badges */}
      <div className="absolute left-[10%] top-[40%]">
        <Badge>AI Agent</Badge>
      </div>
      
      <div className="absolute right-[10%] bottom-[30%]">
        <Badge>Tools</Badge>
      </div>
    </div>
  )
}

function Badge({ children }) {
  return (
    <span className="inline-flex items-center px-4 py-2 bg-white border border-gray-200 rounded-full text-sm font-medium shadow-sm">
      {children}
    </span>
  )
}
```

### 6. Gradient Icon Blocks

App-icon style containers with warm gradients:

```jsx
function GradientIcon({ gradient = 'orange-pink', children }) {
  const gradients = {
    'orange-pink': 'from-amber-400 via-orange-400 to-pink-400',
    'blue-purple': 'from-blue-400 via-violet-400 to-purple-500',
    'green-teal': 'from-emerald-400 via-teal-400 to-cyan-400',
  }

  return (
    <div className={`w-16 h-16 rounded-2xl bg-gradient-to-br ${gradients[gradient]} p-0.5 shadow-lg`}>
      <div className="w-full h-full rounded-[14px] bg-gradient-to-br from-white/20 to-transparent flex items-center justify-center">
        {children}
      </div>
    </div>
  )
}

{/* Feature card with gradient icon */}
<div className="flex items-start gap-4 p-6 bg-white rounded-2xl border border-gray-100">
  <GradientIcon gradient="orange-pink">
    <SparklesIcon className="w-8 h-8 text-white" />
  </GradientIcon>
  <div>
    <p className="text-gray-900">
      Use an <Badge>AI Agent</Badge> to detect bugs in Slack, auto-log them to GitHub and Notion
    </p>
    <span className="text-sm text-gray-500 mt-2 block">Product Manager</span>
  </div>
</div>
```

### 7. Logo Carousel with Grid Lines

Social proof section with animated marquee:

```jsx
function LogoCarousel({ logos }) {
  return (
    <section className="py-12 border-y border-gray-200">
      <p className="text-center text-sm text-gray-500 mb-8">Used by Agents from</p>
      
      {/* Grid container with visible lines */}
      <div className="relative overflow-hidden">
        {/* Vertical grid lines */}
        <div className="absolute inset-0 flex justify-around pointer-events-none">
          {[...Array(7)].map((_, i) => (
            <div key={i} className="w-px h-full bg-gray-200" />
          ))}
        </div>
        
        {/* Horizontal lines top and bottom */}
        <div className="absolute top-0 left-0 right-0 h-px bg-gray-200" />
        <div className="absolute bottom-0 left-0 right-0 h-px bg-gray-200" />
        
        {/* Logo marquee */}
        <div className="flex animate-marquee">
          {[...logos, ...logos].map((logo, i) => (
            <div key={i} className="flex-shrink-0 w-40 h-20 flex items-center justify-center px-8">
              <img src={logo.src} alt={logo.name} className="h-6 w-auto opacity-60 grayscale" />
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}

{/* Add to your CSS */}
<style>{`
  @keyframes marquee {
    from { transform: translateX(0); }
    to { transform: translateX(-50%); }
  }
  .animate-marquee {
    animation: marquee 30s linear infinite;
  }
`}</style>
```

### 8. Code Block with Annotations

Showcase code with floating connected labels:

```jsx
function AnnotatedCode({ code, annotations }) {
  return (
    <div className="relative">
      {/* Code panel */}
      <div className="bg-white rounded-lg border border-gray-200 p-6 font-mono text-sm overflow-x-auto shadow-lg">
        <div className="flex items-center gap-2 mb-4 pb-4 border-b border-gray-100">
          <div className="w-3 h-3 rounded-full bg-red-400" />
          <div className="w-3 h-3 rounded-full bg-yellow-400" />
          <div className="w-3 h-3 rounded-full bg-green-400" />
          <span className="ml-4 text-gray-500 text-xs">api-integration.py</span>
        </div>
        <pre className="text-gray-800">{code}</pre>
      </div>

      {/* Connected annotations */}
      {annotations.map((annotation, i) => (
        <div 
          key={i}
          className="absolute"
          style={{ top: annotation.y, left: annotation.side === 'left' ? '-180px' : 'calc(100% + 20px)' }}
        >
          <div className="flex items-center gap-2">
            {annotation.side === 'right' && (
              <svg width="60" height="40" className="flex-shrink-0">
                <path d="M 0,20 Q 30,20 50,30" fill="none" stroke="#e5e5e5" strokeWidth="1" />
              </svg>
            )}
            <Badge>{annotation.label}</Badge>
            {annotation.side === 'left' && (
              <svg width="60" height="40" className="flex-shrink-0">
                <path d="M 60,20 Q 30,20 10,30" fill="none" stroke="#e5e5e5" strokeWidth="1" />
              </svg>
            )}
          </div>
        </div>
      ))}
    </div>
  )
}
```

## Color System

### Warm Neutrals Foundation

```jsx
const colors = {
  // Background - warm off-white, NOT pure white
  background: {
    primary: '#FAF9F7',    // Cream
    secondary: '#F5F4F1',  // Slightly darker cream
    tertiary: '#EEEDEA',   // Even darker for cards
  },
  
  // Text - warm blacks and grays
  text: {
    primary: '#1A1A1A',    // Near-black
    secondary: '#666666',  // Medium gray
    tertiary: '#999999',   // Light gray
    muted: '#CCCCCC',      // Very light
  },
  
  // Accent gradients
  gradients: {
    purple: 'linear-gradient(to bottom, #8B5CF6, #6D28D9)',
    pink: 'linear-gradient(to bottom, #EC4899, #DB2777)',
    orange: 'linear-gradient(to bottom, #F59E0B, #EA580C)',
    blue: 'linear-gradient(to bottom, #3B82F6, #2563EB)',
  },
}
```

## Complete Landing Page Template

```jsx
export default function StunningLandingPage() {
  return (
    <main className="bg-[#FAF9F7]">
      {/* Sticky Header */}
      <Header />

      {/* Hero with Gradient Rays */}
      <HeroSection />

      {/* Logo Carousel */}
      <LogoCarousel />

      {/* Stats Section with Gradient Blocks */}
      <StatsSection />

      {/* Scroll-Triggered Problem Statement */}
      <ProblemSection />

      {/* Solution with Pink Gradient Background */}
      <SolutionSection />

      {/* Interactive Demo/Diagram */}
      <DiagramSection />

      {/* Code Showcase */}
      <CodeSection />

      {/* Final CTA */}
      <CTASection />

      {/* Footer */}
      <Footer />
    </main>
  )
}
```

## Animation Guidelines

### Scroll-Based Reveals

```jsx
// Use Intersection Observer for scroll-triggered animations
// Avoid animating everything - pick 3-4 key moments

// Good: Central headline, floating badges, diagram connections
// Bad: Every paragraph, every image, every button
```

### Timing Functions

```jsx
const timing = {
  // Quick feedback (buttons, hovers)
  snappy: 'duration-150 ease-out',
  
  // Smooth transitions (color changes, opacity)
  smooth: 'duration-300 ease-out',
  
  // Cinematic reveals (scroll animations, page loads)
  cinematic: 'duration-700 ease-out',
  
  // Dramatic entrances (hero elements)
  dramatic: 'duration-1000 ease-[cubic-bezier(0.16,1,0.3,1)]',
}
```

### Number Animations

```jsx
// Animate statistics counting up when they enter view
// Duration: 1.5-2.5 seconds
// Easing: ease-out cubic for natural deceleration
// Start: when element is 20% visible
```

## Implementation Checklist

Before shipping, verify:

- [ ] Warm cream background, not pure white (#FAF9F7 or similar)
- [ ] Mixed typography with at least one serif/italic element
- [ ] At least one dramatic gradient section
- [ ] Scroll-triggered animation on key content
- [ ] Floating elements with subtle shadows
- [ ] Monospace font for statistics/badges
- [ ] Connected diagram or visual metaphor
- [ ] Generous whitespace between sections
- [ ] Sticky header with scroll behavior
- [ ] Smooth page feel - no jarring transitions

## Reference

For detailed component patterns, see [references/components.md](references/components.md).
For animation recipes, see [references/animations.md](references/animations.md).
