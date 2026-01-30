# Animation Patterns

Advanced animation recipes for creating cinematic landing page experiences.

## Scroll-Triggered Animations

### Intersection Observer Hook

```jsx
function useInView(options = {}) {
  const [isInView, setIsInView] = useState(false)
  const [hasAnimated, setHasAnimated] = useState(false)
  const ref = useRef(null)

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting && !hasAnimated) {
          setIsInView(true)
          setHasAnimated(true)
          if (options.once) {
            observer.disconnect()
          }
        } else if (!options.once) {
          setIsInView(entry.isIntersecting)
        }
      },
      {
        threshold: options.threshold || 0.1,
        rootMargin: options.rootMargin || '-50px',
      }
    )

    if (ref.current) {
      observer.observe(ref.current)
    }

    return () => observer.disconnect()
  }, [options.once, options.threshold, options.rootMargin, hasAnimated])

  return [ref, isInView]
}
```

### Fade In From Direction

```jsx
function FadeIn({ 
  children, 
  direction = 'up', 
  delay = 0, 
  duration = 700,
  distance = 30,
  className = '' 
}) {
  const [ref, isInView] = useInView({ once: true, threshold: 0.1 })

  const transforms = {
    up: `translateY(${distance}px)`,
    down: `translateY(-${distance}px)`,
    left: `translateX(${distance}px)`,
    right: `translateX(-${distance}px)`,
  }

  return (
    <div
      ref={ref}
      className={className}
      style={{
        opacity: isInView ? 1 : 0,
        transform: isInView ? 'translate(0)' : transforms[direction],
        transition: `opacity ${duration}ms ease-out ${delay}ms, transform ${duration}ms ease-out ${delay}ms`,
      }}
    >
      {children}
    </div>
  )
}

{/* Usage */}
<FadeIn direction="up" delay={0}>
  <h1>Main Headline</h1>
</FadeIn>
<FadeIn direction="up" delay={150}>
  <p>Supporting text</p>
</FadeIn>
<FadeIn direction="up" delay={300}>
  <button>CTA</button>
</FadeIn>
```

### Staggered Children Animation

```jsx
function StaggeredContainer({ children, staggerDelay = 100 }) {
  const [ref, isInView] = useInView({ once: true, threshold: 0.1 })

  return (
    <div ref={ref}>
      {React.Children.map(children, (child, i) => (
        <div
          style={{
            opacity: isInView ? 1 : 0,
            transform: isInView ? 'translateY(0)' : 'translateY(20px)',
            transition: `opacity 500ms ease-out ${i * staggerDelay}ms, transform 500ms ease-out ${i * staggerDelay}ms`,
          }}
        >
          {child}
        </div>
      ))}
    </div>
  )
}

{/* Usage */}
<StaggeredContainer staggerDelay={100}>
  <FeatureCard />
  <FeatureCard />
  <FeatureCard />
</StaggeredContainer>
```

## Number Counting Animation

### Animated Counter

```jsx
function AnimatedNumber({ 
  value, 
  duration = 2000, 
  formatFn = (n) => n.toLocaleString(),
  suffix = '' 
}) {
  const [displayValue, setDisplayValue] = useState(0)
  const [ref, isInView] = useInView({ once: true, threshold: 0.5 })

  useEffect(() => {
    if (!isInView) return

    let startTime
    const animate = (currentTime) => {
      if (!startTime) startTime = currentTime
      const elapsed = currentTime - startTime
      const progress = Math.min(elapsed / duration, 1)
      
      // Ease out cubic
      const eased = 1 - Math.pow(1 - progress, 3)
      setDisplayValue(Math.floor(eased * value))

      if (progress < 1) {
        requestAnimationFrame(animate)
      }
    }

    requestAnimationFrame(animate)
  }, [isInView, value, duration])

  return (
    <span ref={ref} className="font-mono tabular-nums">
      {formatFn(displayValue)}{suffix}
    </span>
  )
}

{/* Usage */}
<AnimatedNumber value={25000} suffix="+" />
<AnimatedNumber value={7000000} suffix="+" />
<AnimatedNumber value={99.9} suffix="%" formatFn={(n) => n.toFixed(1)} />
```

### Counting with Easing Options

```jsx
const easings = {
  linear: (t) => t,
  easeOut: (t) => 1 - Math.pow(1 - t, 3),
  easeIn: (t) => Math.pow(t, 3),
  easeInOut: (t) => t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2,
  bounce: (t) => {
    const n1 = 7.5625
    const d1 = 2.75
    if (t < 1 / d1) return n1 * t * t
    if (t < 2 / d1) return n1 * (t -= 1.5 / d1) * t + 0.75
    if (t < 2.5 / d1) return n1 * (t -= 2.25 / d1) * t + 0.9375
    return n1 * (t -= 2.625 / d1) * t + 0.984375
  },
}

function CountUp({ value, duration = 2000, easing = 'easeOut' }) {
  const [count, setCount] = useState(0)
  const [ref, isInView] = useInView({ once: true })

  useEffect(() => {
    if (!isInView) return
    
    const startTime = Date.now()
    const easeFn = easings[easing]

    const tick = () => {
      const elapsed = Date.now() - startTime
      const progress = Math.min(elapsed / duration, 1)
      const easedProgress = easeFn(progress)
      
      setCount(Math.round(easedProgress * value))

      if (progress < 1) {
        requestAnimationFrame(tick)
      }
    }

    requestAnimationFrame(tick)
  }, [isInView, value, duration, easing])

  return <span ref={ref}>{count.toLocaleString()}</span>
}
```

## Scroll-Based Parallax

### Parallax Text Elements

```jsx
function ParallaxText({ children, speed = 0.5, className = '' }) {
  const [offset, setOffset] = useState(0)
  const ref = useRef(null)

  useEffect(() => {
    const handleScroll = () => {
      if (!ref.current) return
      const rect = ref.current.getBoundingClientRect()
      const viewportCenter = window.innerHeight / 2
      const elementCenter = rect.top + rect.height / 2
      const distance = viewportCenter - elementCenter
      setOffset(distance * speed)
    }

    window.addEventListener('scroll', handleScroll, { passive: true })
    handleScroll() // Initial call
    return () => window.removeEventListener('scroll', handleScroll)
  }, [speed])

  return (
    <div
      ref={ref}
      className={className}
      style={{ transform: `translateY(${offset}px)` }}
    >
      {children}
    </div>
  )
}

{/* Usage - scattered text that moves at different speeds */}
<section className="relative min-h-screen">
  <h2 className="text-center text-4xl">Building agents is hard</h2>
  
  <ParallaxText speed={0.3} className="absolute left-[10%] top-[30%]">
    <span className="text-gray-400 font-mono text-sm">building integrations</span>
  </ParallaxText>
  
  <ParallaxText speed={0.5} className="absolute right-[15%] top-[40%]">
    <span className="text-gray-400 font-mono text-sm">managing auth</span>
  </ParallaxText>
  
  <ParallaxText speed={0.2} className="absolute left-[20%] bottom-[35%]">
    <span className="text-gray-400 font-mono text-sm">scaling execution</span>
  </ParallaxText>
</section>
```

### Section Background Parallax

```jsx
function ParallaxBackground({ children, imageUrl }) {
  const [offset, setOffset] = useState(0)
  const ref = useRef(null)

  useEffect(() => {
    const handleScroll = () => {
      if (!ref.current) return
      const rect = ref.current.getBoundingClientRect()
      const scrollProgress = -rect.top / (window.innerHeight + rect.height)
      setOffset(scrollProgress * 100) // 100px of movement
    }

    window.addEventListener('scroll', handleScroll, { passive: true })
    return () => window.removeEventListener('scroll', handleScroll)
  }, [])

  return (
    <section ref={ref} className="relative overflow-hidden">
      <div 
        className="absolute inset-0 bg-cover bg-center"
        style={{
          backgroundImage: `url(${imageUrl})`,
          transform: `translateY(${offset}px) scale(1.1)`,
        }}
      />
      <div className="relative z-10">{children}</div>
    </section>
  )
}
```

## Scroll-Triggered Morphing

### Code to Diagram Transition

```jsx
function MorphingShowcase() {
  const [morphed, setMorphed] = useState(false)
  const ref = useRef(null)

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting && entry.intersectionRatio > 0.5) {
          // Delay before morphing
          setTimeout(() => setMorphed(true), 500)
        }
      },
      { threshold: 0.5 }
    )

    if (ref.current) observer.observe(ref.current)
    return () => observer.disconnect()
  }, [])

  return (
    <div ref={ref} className="relative h-[600px]">
      {/* Complex state (code) */}
      <div
        className={`absolute inset-0 transition-all duration-1000 ${
          morphed ? 'opacity-0 scale-95 blur-md' : 'opacity-100 scale-100'
        }`}
      >
        <CodePanel />
        <TimeLabel label="22+ hrs" variant="complex" />
      </div>

      {/* Simple state (diagram) */}
      <div
        className={`absolute inset-0 transition-all duration-1000 delay-300 ${
          morphed ? 'opacity-100 scale-100' : 'opacity-0 scale-105'
        }`}
      >
        <SimpleDiagram />
        <TimeLabel label="5 mins" variant="simple" />
      </div>
    </div>
  )
}

function TimeLabel({ label, variant }) {
  const styles = {
    complex: 'text-red-500',
    simple: 'text-green-500',
  }

  return (
    <div className="text-center mt-8">
      <span className={`text-5xl font-mono font-bold ${styles[variant]}`}>
        {label.split(' ')[0]}
      </span>
      <span className={`text-xl ${styles[variant]} ml-2`}>
        {label.split(' ')[1]}
      </span>
    </div>
  )
}
```

## Logo Marquee Animation

### Infinite Scroll Carousel

```jsx
function LogoMarquee({ logos, speed = 30 }) {
  return (
    <div className="relative overflow-hidden">
      {/* Fade edges */}
      <div className="absolute left-0 top-0 bottom-0 w-24 bg-gradient-to-r from-[#FAF9F7] to-transparent z-10" />
      <div className="absolute right-0 top-0 bottom-0 w-24 bg-gradient-to-l from-[#FAF9F7] to-transparent z-10" />

      {/* Scrolling track */}
      <div 
        className="flex"
        style={{
          animation: `marquee ${speed}s linear infinite`,
        }}
      >
        {/* Double the logos for seamless loop */}
        {[...logos, ...logos].map((logo, i) => (
          <div 
            key={i}
            className="flex-shrink-0 w-40 h-16 flex items-center justify-center px-8"
          >
            <img 
              src={logo.src} 
              alt={logo.name}
              className="h-6 w-auto opacity-50 grayscale hover:opacity-100 hover:grayscale-0 transition-all duration-300"
            />
          </div>
        ))}
      </div>

      <style jsx>{`
        @keyframes marquee {
          from { transform: translateX(0); }
          to { transform: translateX(-50%); }
        }
      `}</style>
    </div>
  )
}
```

### Pause on Hover

```jsx
function LogoMarqueeWithPause({ logos }) {
  const [isPaused, setIsPaused] = useState(false)

  return (
    <div 
      className="overflow-hidden"
      onMouseEnter={() => setIsPaused(true)}
      onMouseLeave={() => setIsPaused(false)}
    >
      <div 
        className="flex"
        style={{
          animation: 'marquee 30s linear infinite',
          animationPlayState: isPaused ? 'paused' : 'running',
        }}
      >
        {[...logos, ...logos].map((logo, i) => (
          <LogoItem key={i} logo={logo} />
        ))}
      </div>
    </div>
  )
}
```

## Gradient Ray Animation

### Animated Background Rays

```jsx
function AnimatedRays() {
  return (
    <div className="absolute inset-0 overflow-hidden">
      {[...Array(12)].map((_, i) => (
        <div
          key={i}
          className="absolute bottom-0 left-1/2 h-full w-[8%] origin-bottom"
          style={{
            transform: `translateX(-50%) rotate(${(i - 6) * 8}deg)`,
            animation: `rayPulse ${3 + i * 0.2}s ease-in-out infinite`,
            animationDelay: `${i * 0.1}s`,
          }}
        >
          <div 
            className="absolute inset-0"
            style={{
              background: `linear-gradient(to top, 
                rgba(139, 92, 246, 0.15) 0%,
                rgba(139, 92, 246, 0.05) 50%,
                transparent 80%
              )`,
            }}
          />
        </div>
      ))}

      <style jsx>{`
        @keyframes rayPulse {
          0%, 100% { opacity: 1; }
          50% { opacity: 0.7; }
        }
      `}</style>
    </div>
  )
}
```

## Glowing Effects

### Logo with Animated Glow

```jsx
function GlowingLogo({ children }) {
  return (
    <div className="relative">
      {/* Animated glow layers */}
      <div 
        className="absolute inset-0 rounded-full blur-xl"
        style={{
          background: 'rgba(59, 130, 246, 0.3)',
          animation: 'glow 3s ease-in-out infinite',
        }}
      />
      <div 
        className="absolute inset-0 rounded-full blur-lg"
        style={{
          background: 'rgba(16, 185, 129, 0.2)',
          animation: 'glow 3s ease-in-out infinite 0.5s',
        }}
      />
      
      {/* Logo container */}
      <div className="relative bg-white rounded-2xl p-4 shadow-lg">
        {children}
      </div>

      <style jsx>{`
        @keyframes glow {
          0%, 100% { 
            transform: scale(1); 
            opacity: 0.8; 
          }
          50% { 
            transform: scale(1.2); 
            opacity: 1; 
          }
        }
      `}</style>
    </div>
  )
}
```

## Page Load Animation

### Hero Entrance Sequence

```jsx
function HeroEntrance() {
  const [stage, setStage] = useState(0)

  useEffect(() => {
    // Stagger the entrance
    const timers = [
      setTimeout(() => setStage(1), 100),   // Background rays
      setTimeout(() => setStage(2), 400),   // Headline
      setTimeout(() => setStage(3), 700),   // Subheadline
      setTimeout(() => setStage(4), 1000),  // CTAs
    ]
    return () => timers.forEach(clearTimeout)
  }, [])

  return (
    <section className="relative min-h-screen">
      {/* Background */}
      <div className={`absolute inset-0 transition-opacity duration-1000 ${stage >= 1 ? 'opacity-100' : 'opacity-0'}`}>
        <GradientRays />
      </div>

      <div className="relative z-10 max-w-4xl mx-auto px-6 pt-32">
        {/* Headline */}
        <h1 
          className={`text-6xl font-serif transition-all duration-700 ${
            stage >= 2 ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-8'
          }`}
        >
          Build something amazing
        </h1>

        {/* Subheadline */}
        <p 
          className={`text-xl text-gray-600 mt-6 transition-all duration-700 ${
            stage >= 3 ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-8'
          }`}
        >
          The platform for modern development
        </p>

        {/* CTAs */}
        <div 
          className={`flex gap-4 mt-10 transition-all duration-700 ${
            stage >= 4 ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-8'
          }`}
        >
          <button className="px-6 py-3 bg-black text-white">Get Started</button>
          <button className="px-6 py-3 border border-black">Learn More</button>
        </div>
      </div>
    </section>
  )
}
```

## Performance Tips

### GPU-Accelerated Properties

```jsx
// ✅ Prefer these (GPU-accelerated)
transform: translateX(), translateY(), scale(), rotate()
opacity

// ❌ Avoid animating these (trigger layout/paint)
width, height, top, left, right, bottom
margin, padding
border-radius (on large elements)
box-shadow (especially with blur)
```

### Reducing Layout Thrashing

```jsx
// ❌ Bad - causes multiple reflows
elements.forEach(el => {
  const height = el.offsetHeight // Read
  el.style.height = height + 10 + 'px' // Write
})

// ✅ Good - batch reads and writes
const heights = elements.map(el => el.offsetHeight) // All reads
elements.forEach((el, i) => {
  el.style.height = heights[i] + 10 + 'px' // All writes
})
```

### Use will-change Sparingly

```jsx
// Only add will-change when animation is about to start
function AnimatedElement() {
  const [isAnimating, setIsAnimating] = useState(false)
  
  return (
    <div 
      style={{ willChange: isAnimating ? 'transform, opacity' : 'auto' }}
      onMouseEnter={() => setIsAnimating(true)}
      onAnimationEnd={() => setIsAnimating(false)}
    />
  )
}
```
