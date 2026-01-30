# Component Patterns

Detailed implementation patterns for premium landing page components.

## Navigation

### Sticky Header with Theme Switch

```jsx
function Header() {
  const [scrolled, setScrolled] = useState(false)

  useEffect(() => {
    const handleScroll = () => setScrolled(window.scrollY > 100)
    window.addEventListener('scroll', handleScroll)
    return () => window.removeEventListener('scroll', handleScroll)
  }, [])

  return (
    <header
      className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 ${
        scrolled 
          ? 'bg-black text-white py-3' 
          : 'bg-transparent text-black py-6'
      }`}
    >
      <nav className="max-w-7xl mx-auto px-6 flex items-center justify-between">
        <Logo className={scrolled ? 'text-white' : 'text-black'} />
        
        <div className="hidden md:flex items-center gap-8">
          {navLinks.map(link => (
            <a 
              key={link.href}
              href={link.href}
              className="text-sm font-medium uppercase tracking-wider opacity-80 hover:opacity-100 transition-opacity"
            >
              {link.label}
            </a>
          ))}
        </div>

        <button 
          className={`px-4 py-2 text-sm font-medium border transition-colors ${
            scrolled
              ? 'border-white hover:bg-white hover:text-black'
              : 'border-black hover:bg-black hover:text-white'
          }`}
        >
          SIGN IN
        </button>
      </nav>
    </header>
  )
}
```

## Hero Section

### Full Hero with Gradient Rays

```jsx
function HeroSection() {
  return (
    <section className="relative min-h-screen overflow-hidden bg-[#FAF9F7]">
      {/* Gradient background layer */}
      <div className="absolute inset-0 pointer-events-none">
        {/* Base radial gradient */}
        <div 
          className="absolute inset-0"
          style={{
            background: `radial-gradient(ellipse 100% 70% at 50% 100%, 
              rgba(139, 92, 246, 0.25) 0%, 
              rgba(139, 92, 246, 0.08) 40%,
              transparent 70%
            )`,
          }}
        />
        
        {/* Ray panels */}
        <div className="absolute bottom-0 left-1/2 -translate-x-1/2 w-[200vw] h-[120%]">
          {[...Array(16)].map((_, i) => (
            <div
              key={i}
              className="absolute bottom-0 left-1/2 h-full origin-bottom"
              style={{
                width: '6%',
                transform: `translateX(-50%) rotate(${(i - 8) * 6}deg)`,
                background: `linear-gradient(to top, 
                  rgba(139, 92, 246, ${0.18 - Math.abs(i - 8) * 0.015}) 0%,
                  rgba(139, 92, 246, ${0.08 - Math.abs(i - 8) * 0.008}) 50%,
                  transparent 85%
                )`,
              }}
            />
          ))}
        </div>
      </div>

      {/* Content */}
      <div className="relative z-10 max-w-6xl mx-auto px-6 pt-32 pb-24 min-h-screen flex flex-col justify-center">
        <div className="max-w-3xl">
          {/* Decorative line */}
          <div className="w-16 h-0.5 bg-gray-300 mb-8" />
          
          {/* Main headline with mixed typography */}
          <h1 className="text-5xl md:text-6xl lg:text-7xl tracking-tight leading-[1.1] mb-6">
            <span className="font-serif">Skills that </span>
            <em className="font-serif italic">evolve</em>
            <span className="font-serif"> with</span>
            <br />
            <span className="font-serif">your </span>
            <span className="font-sans font-semibold">Agents</span>
          </h1>

          {/* Subheadline */}
          <p className="text-lg md:text-xl text-gray-600 max-w-xl mb-10">
            More than just integrations, <strong className="text-gray-900 font-semibold">10,000+ tools</strong> that 
            can adapt — turning automation into intuition.
          </p>

          {/* CTAs */}
          <div className="flex flex-wrap gap-4">
            <button className="px-6 py-3 bg-black text-white text-sm font-medium uppercase tracking-wider hover:bg-gray-800 transition-colors">
              Get Started for Free
            </button>
            <button className="px-6 py-3 border border-gray-300 text-sm font-medium uppercase tracking-wider hover:border-black transition-colors flex items-center gap-2">
              <ArrowRightIcon className="w-4 h-4" />
              Explore Docs
            </button>
          </div>
        </div>
      </div>
    </section>
  )
}
```

## Statistics Display

### Floating Stats with Gradient Background

```jsx
function StatsSection() {
  return (
    <section className="py-24 bg-[#FAF9F7]">
      <div className="max-w-6xl mx-auto px-6">
        <div className="grid md:grid-cols-2 gap-16 items-center">
          {/* Text content */}
          <div>
            <h2 className="text-4xl md:text-5xl font-serif tracking-tight mb-6">
              Muscle Memory<br />
              for <em className="italic">Intelligence</em>
            </h2>
            <p className="text-gray-600 text-lg mb-8 max-w-md">
              In a world with <strong className="text-black">countries of geniuses in datacenters</strong>, 
              we believe the most important thing is for them to be able to take complex actions 
              and learn from them in realtime.
            </p>
            <button className="px-6 py-3 bg-black text-white text-sm font-medium uppercase tracking-wider flex items-center gap-2">
              <ArrowRightIcon className="w-4 h-4" />
              The Results
            </button>
          </div>

          {/* Gradient visual with floating stats */}
          <div className="relative">
            {/* Layered gradient blocks */}
            <div className="relative w-full aspect-square">
              {[...Array(5)].map((_, i) => (
                <div
                  key={i}
                  className="absolute rounded-lg"
                  style={{
                    top: `${i * 8}%`,
                    left: `${i * 5}%`,
                    right: `${(4 - i) * 5}%`,
                    bottom: `${(4 - i) * 8}%`,
                    background: `linear-gradient(135deg, 
                      rgba(251, 191, 36, ${0.9 - i * 0.15}) 0%,
                      rgba(249, 115, 22, ${0.8 - i * 0.15}) 50%,
                      rgba(234, 88, 12, ${0.7 - i * 0.15}) 100%
                    )`,
                  }}
                />
              ))}

              {/* Floating stat badges */}
              <AnimatedStat 
                label="Stars on GitHub" 
                value={25000} 
                className="absolute -top-4 right-0"
              />
              <AnimatedStat 
                label="Successful Calls" 
                value={7000000} 
                className="absolute top-1/3 -right-4"
              />
              <AnimatedStat 
                label="Developers" 
                value={100000} 
                className="absolute top-2/3 right-8"
              />
              <AnimatedStat 
                label="Customers" 
                value={200} 
                className="absolute bottom-0 right-1/4"
              />
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}

function AnimatedStat({ label, value, suffix = '+', className }) {
  const [count, setCount] = useState(0)
  const [isVisible, setIsVisible] = useState(false)
  const ref = useRef(null)

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting && !isVisible) {
          setIsVisible(true)
        }
      },
      { threshold: 0.5 }
    )
    if (ref.current) observer.observe(ref.current)
    return () => observer.disconnect()
  }, [isVisible])

  useEffect(() => {
    if (!isVisible) return
    
    let start = 0
    const duration = 2000
    const startTime = Date.now()

    const animate = () => {
      const elapsed = Date.now() - startTime
      const progress = Math.min(elapsed / duration, 1)
      const eased = 1 - Math.pow(1 - progress, 3)
      setCount(Math.floor(eased * value))
      
      if (progress < 1) {
        requestAnimationFrame(animate)
      }
    }

    requestAnimationFrame(animate)
  }, [isVisible, value])

  return (
    <div 
      ref={ref}
      className={`inline-flex items-center gap-3 px-4 py-2.5 bg-white rounded-full border border-gray-200 shadow-md ${className}`}
    >
      <span className="text-sm text-gray-600 whitespace-nowrap">{label}</span>
      <span className="font-mono font-semibold text-black tracking-tight">
        {count.toLocaleString()}{suffix}
      </span>
    </div>
  )
}
```

## Feature Cards

### Card with Gradient Icon

```jsx
function FeatureCard({ icon: Icon, title, description, role, gradient = 'orange-pink' }) {
  const gradients = {
    'orange-pink': 'from-amber-400 via-orange-400 to-pink-400',
    'purple-blue': 'from-violet-400 via-purple-500 to-blue-500',
    'green-cyan': 'from-emerald-400 via-teal-400 to-cyan-400',
  }

  return (
    <div className="group p-6 bg-white rounded-2xl border border-gray-100 shadow-sm hover:shadow-lg transition-shadow duration-300">
      <div className="flex items-start gap-4">
        {/* Gradient icon */}
        <div className={`flex-shrink-0 w-14 h-14 rounded-xl bg-gradient-to-br ${gradients[gradient]} p-0.5`}>
          <div className="w-full h-full rounded-[10px] bg-gradient-to-br from-white/30 to-white/10 flex items-center justify-center">
            <Icon className="w-6 h-6 text-white" />
          </div>
        </div>

        {/* Content */}
        <div className="flex-1 min-w-0">
          <p className="text-gray-900 leading-relaxed">
            {title}
            {description && (
              <span className="text-gray-500"> {description}</span>
            )}
          </p>
          {role && (
            <span className="inline-block mt-3 text-sm text-gray-400">{role}</span>
          )}
        </div>
      </div>
    </div>
  )
}

{/* Pill badge component for inline use */}
function PillBadge({ children }) {
  return (
    <span className="inline-flex items-center px-2.5 py-1 mx-1 bg-gray-100 rounded-full text-sm font-medium text-gray-700 align-middle">
      {children}
    </span>
  )
}

{/* Usage example */}
<FeatureCard 
  icon={SparklesIcon}
  title={
    <>
      Use an <PillBadge>AI Agent</PillBadge> to detect bugs in Slack, auto-log them to GitHub and Notion
    </>
  }
  role="Product Manager"
  gradient="orange-pink"
/>
```

## Pink Gradient Section

### Solution Section with Curved Rays

```jsx
function PinkGradientSection({ title }) {
  return (
    <section className="relative py-32 overflow-hidden">
      {/* Background with curved panels */}
      <div className="absolute inset-0">
        {/* Base gradient */}
        <div 
          className="absolute inset-0"
          style={{
            background: `linear-gradient(to bottom, 
              #FAF9F7 0%,
              #FDF2F8 15%,
              #FCE7F3 40%,
              #FBCFE8 70%,
              #F9A8D4 100%
            )`,
          }}
        />
        
        {/* Curved ray panels */}
        {[...Array(10)].map((_, i) => (
          <div
            key={i}
            className="absolute bottom-0 h-full"
            style={{
              left: `${i * 12 - 10}%`,
              width: '18%',
              background: `linear-gradient(to top,
                rgba(244, 114, 182, ${0.4 - i * 0.03}) 0%,
                rgba(251, 207, 232, ${0.2 - i * 0.015}) 60%,
                transparent 90%
              )`,
              borderRadius: '40% 40% 0 0 / 15% 15% 0 0',
            }}
          />
        ))}
      </div>

      {/* Content */}
      <div className="relative z-10 max-w-4xl mx-auto px-6 text-center">
        <h2 className="text-4xl md:text-5xl lg:text-6xl font-serif tracking-tight text-gray-800">
          {title}
        </h2>
      </div>
    </section>
  )
}

{/* Usage */}
<PinkGradientSection 
  title={
    <>
      Composio <em className="italic">erases</em> that drag in <strong className="font-semibold">one call</strong>
    </>
  }
/>
```

## Code Showcase

### Annotated Code Block with Visual Transition

```jsx
function CodeShowcase() {
  const [showSimplified, setShowSimplified] = useState(false)

  return (
    <section className="py-24 bg-[#FAF9F7]">
      <div className="max-w-6xl mx-auto px-6">
        <div className="relative">
          {/* Complex code (before) */}
          <div 
            className={`transition-all duration-700 ${
              showSimplified ? 'opacity-0 scale-95 blur-sm' : 'opacity-100 scale-100'
            }`}
          >
            <CodeBlock 
              title="Without Composio"
              subtitle="22+ hours of setup"
              code={complexCode}
              annotations={[
                { label: 'AI Agent', side: 'left', y: '15%' },
                { label: 'Tools', side: 'right', y: '70%' },
              ]}
            />
          </div>

          {/* Simplified diagram (after) */}
          <div 
            className={`absolute inset-0 transition-all duration-700 ${
              showSimplified ? 'opacity-100 scale-100' : 'opacity-0 scale-105 pointer-events-none'
            }`}
          >
            <SimplifiedDiagram />
            <div className="text-center mt-8">
              <span className="text-4xl font-mono font-bold text-green-500">5</span>
              <span className="text-xl text-green-500 ml-1">mins</span>
              <p className="text-gray-500 mt-2">with Composio</p>
            </div>
          </div>

          {/* Toggle trigger - activate on scroll */}
          <ScrollTrigger onEnter={() => setShowSimplified(true)} />
        </div>
      </div>
    </section>
  )
}

function CodeBlock({ title, subtitle, code, annotations }) {
  return (
    <div className="relative">
      {/* Title header */}
      <div className="text-center mb-6">
        <span className="text-4xl font-mono font-bold text-red-500">{subtitle.split(' ')[0]}</span>
        <span className="text-red-500 ml-2">{subtitle.split(' ').slice(1).join(' ')}</span>
        <p className="text-gray-500 mt-1">{title}</p>
      </div>

      {/* Code panel */}
      <div className="bg-white rounded-xl border border-gray-200 shadow-xl overflow-hidden">
        {/* Window chrome */}
        <div className="flex items-center gap-2 px-4 py-3 bg-gray-50 border-b border-gray-200">
          <div className="w-3 h-3 rounded-full bg-red-400" />
          <div className="w-3 h-3 rounded-full bg-yellow-400" />
          <div className="w-3 h-3 rounded-full bg-green-400" />
          <span className="ml-4 text-xs text-gray-500">integration.py</span>
        </div>
        
        {/* Code content */}
        <div className="p-6 overflow-x-auto">
          <pre className="text-sm text-gray-800 font-mono leading-relaxed">
            {code}
          </pre>
        </div>
      </div>

      {/* Connected annotation badges */}
      {annotations.map((ann, i) => (
        <div
          key={i}
          className="absolute flex items-center gap-2"
          style={{
            top: ann.y,
            [ann.side]: '-160px',
          }}
        >
          {ann.side === 'left' && (
            <>
              <span className="px-4 py-2 bg-white border border-gray-200 rounded-full text-sm font-medium shadow-sm">
                {ann.label}
              </span>
              <svg width="80" height="2" className="text-gray-200">
                <path d="M0,1 Q40,1 70,20" fill="none" stroke="currentColor" strokeWidth="1" />
              </svg>
            </>
          )}
          {ann.side === 'right' && (
            <>
              <svg width="80" height="2" className="text-gray-200">
                <path d="M80,1 Q40,1 10,20" fill="none" stroke="currentColor" strokeWidth="1" />
              </svg>
              <span className="px-4 py-2 bg-white border border-gray-200 rounded-full text-sm font-medium shadow-sm">
                {ann.label}
              </span>
            </>
          )}
        </div>
      ))}
    </div>
  )
}
```

## CTA Section

### Confident Close

```jsx
function CTASection() {
  return (
    <section className="py-32 bg-black text-white">
      <div className="max-w-4xl mx-auto px-6 text-center">
        <p className="text-sm uppercase tracking-[0.2em] text-gray-400 mb-6">
          Ready to build?
        </p>
        <h2 className="text-4xl md:text-5xl lg:text-6xl font-serif tracking-tight mb-10">
          Start shipping <em className="italic">faster</em>
        </h2>
        <div className="flex flex-wrap justify-center gap-4">
          <button className="px-8 py-4 bg-white text-black text-sm font-medium uppercase tracking-wider hover:bg-gray-100 transition-colors">
            Get Started Free
          </button>
          <button className="px-8 py-4 border border-white/30 text-sm font-medium uppercase tracking-wider hover:bg-white/10 transition-colors">
            Schedule a Demo
          </button>
        </div>
      </div>
    </section>
  )
}
```

## Footer

### Minimal Premium Footer

```jsx
function Footer() {
  return (
    <footer className="py-16 bg-[#FAF9F7] border-t border-gray-200">
      <div className="max-w-6xl mx-auto px-6">
        <div className="grid md:grid-cols-5 gap-12">
          {/* Logo and tagline */}
          <div className="md:col-span-2">
            <Logo className="h-8 w-auto" />
            <p className="mt-4 text-sm text-gray-500 max-w-xs">
              Building the infrastructure for intelligent automation.
            </p>
          </div>

          {/* Link columns */}
          {footerLinks.map((column) => (
            <div key={column.title}>
              <h4 className="text-xs uppercase tracking-wider text-gray-400 mb-4">
                {column.title}
              </h4>
              <ul className="space-y-3">
                {column.links.map((link) => (
                  <li key={link.href}>
                    <a 
                      href={link.href}
                      className="text-sm text-gray-600 hover:text-black transition-colors"
                    >
                      {link.label}
                    </a>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>

        {/* Bottom bar */}
        <div className="mt-16 pt-8 border-t border-gray-200 flex flex-wrap justify-between items-center gap-4">
          <p className="text-xs text-gray-400">
            © 2024 Company, Inc. All rights reserved.
          </p>
          <div className="flex gap-6">
            <a href="#" className="text-gray-400 hover:text-black transition-colors">
              <TwitterIcon className="w-5 h-5" />
            </a>
            <a href="#" className="text-gray-400 hover:text-black transition-colors">
              <GitHubIcon className="w-5 h-5" />
            </a>
            <a href="#" className="text-gray-400 hover:text-black transition-colors">
              <LinkedInIcon className="w-5 h-5" />
            </a>
          </div>
        </div>
      </div>
    </footer>
  )
}
```
