# Channel 47 Terminal Redesign - Implementation Prompt

```xml
<role>
You are a senior frontend developer and designer specializing in unique web experiences with expertise in:
- Modern web technologies (HTML, CSS, JavaScript/TypeScript, Astro framework)
- Terminal UI/UX patterns and aesthetics
- Performance-optimized animations and interactions
- Accessible design that maintains visual distinctiveness
- Progressive enhancement and mobile-responsive implementation

Your task is to transform channel47.dev from a conventional developer portfolio into an unforgettable "delightful terminal experience" - the most beautiful command-line interface users have ever seen rendered in a browser.
</role>

<context>
Channel 47 is a website showcasing Claude Code plugins, skills, and MCP servers. The current design is clean but conventional - it looks like many developer portfolio sites. The redesign should embody the same philosophy as the tools it showcases: bringing unexpected personality and joy to minimalist foundations.

Current stack: Astro framework, existing components in src/components/, styles likely in CSS/SCSS
Current pages: Homepage (/), Tools/Plugins (/plugins), Blog (/blog), About (/about), Individual plugin pages
</context>

<instructions>
Implement the terminal-inspired redesign systematically, following the prioritized phases below. Before making any changes, thoroughly explore the current codebase structure using available tools to understand the architecture, component patterns, and styling approach.

For each implementation phase, think through your approach in <thinking> tags before executing, then provide implementation details.
</instructions>

<design_specifications>

<visual_identity>

<color_palette>
/**
 * Terminal-Inspired Color System
 * Based on modern terminal themes with neon accents
 */
--color-terminal-black: #0a0e14;     /* Deep terminal background (slightly blue-tinted) */
--color-terminal-white: #e6edf3;     /* Soft phosphor glow text */
--color-accent-primary: #00ff9f;     /* Terminal green/cyan - success, links, primary actions */
--color-accent-secondary: #ff6b9d;   /* Neon pink/magenta - errors, warnings, CTAs */
--color-muted-gray: #6e7681;         /* Comment gray - secondary text, metadata */
--color-highlight-gold: #ffd700;     /* Gold - special moments, featured items */

/* Semantic color assignments */
--color-bg-primary: var(--color-terminal-black);
--color-bg-hover: rgba(0, 255, 159, 0.1);        /* Subtle green glow */
--color-text-primary: var(--color-terminal-white);
--color-text-secondary: var(--color-muted-gray);
--color-interactive: var(--color-accent-primary);
--color-cta: var(--color-accent-secondary);
--color-success: var(--color-accent-primary);
--color-special: var(--color-highlight-gold);
</color_palette>

<typography>
/* Headings: Monospace for terminal authenticity */
--font-heading: 'JetBrains Mono', 'IBM Plex Mono', 'Courier New', monospace;

/* Body: Clean sans-serif for readability */
--font-body: 'Inter Variable', 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;

/* Code/Terminal elements */
--font-mono: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace;

/* Type scale with generous vertical rhythm */
--font-size-xs: 0.75rem;    /* 12px */
--font-size-sm: 0.875rem;   /* 14px */
--font-size-base: 1rem;     /* 16px */
--font-size-lg: 1.25rem;    /* 20px */
--font-size-xl: 1.5rem;     /* 24px */
--font-size-2xl: 2rem;      /* 32px */
--font-size-3xl: 2.5rem;    /* 40px */
--font-size-4xl: 3rem;      /* 48px */

--line-height-tight: 1.2;
--line-height-normal: 1.5;
--line-height-relaxed: 1.75;
</typography>

<spacing>
/* Generous vertical rhythm based on terminal line spacing */
--space-unit: 2rem;
--space-xs: calc(var(--space-unit) * 0.25);  /* 0.5rem / 8px */
--space-sm: calc(var(--space-unit) * 0.5);   /* 1rem / 16px */
--space-md: var(--space-unit);               /* 2rem / 32px */
--space-lg: calc(var(--space-unit) * 1.5);   /* 3rem / 48px */
--space-xl: calc(var(--space-unit) * 2);     /* 4rem / 64px */
--space-2xl: calc(var(--space-unit) * 3);    /* 6rem / 96px */
</spacing>

<visual_style>
/* Terminal Brutalism Design System */
--border-radius: 0px;                /* Sharp corners (terminal windows are rectangular) */
--border-radius-beveled: 4px;        /* Occasional beveled edges for special interactive elements */
--border-width: 1px;
--border-style: solid;
--border-color: var(--color-muted-gray);

/* Box-drawing characters for UI borders */
/* Use these Unicode characters: ─ │ ┌ ┐ └ ┘ ├ ┤ ┬ ┴ ┼ */

/* Transitions */
--transition-fast: 150ms ease-out;
--transition-normal: 250ms ease-out;
--transition-slow: 400ms ease-out;

/* Shadows - subtle glow effects */
--glow-primary: 0 0 20px rgba(0, 255, 159, 0.3);
--glow-secondary: 0 0 20px rgba(255, 107, 157, 0.3);
--glow-gold: 0 0 20px rgba(255, 215, 0, 0.3);
</visual_style>

</visual_identity>

<key_features>

<feature id="1" priority="high">
<name>Floating Terminal Prompt Navigation</name>
<description>
Replace traditional header navigation with a floating, semi-transparent bar at the top that resembles a terminal prompt. By default shows "[channel47.dev]$ _" with blinking cursor. On interaction (hover/click), expands to reveal navigation as terminal commands.
</description>
<implementation_notes>
- Position: fixed, top of viewport, slight transparency (rgba)
- Default state: Compact prompt with blinking cursor animation
- Expanded state: Shows command list with syntax highlighting
- Commands format:
  > tools     # Browse all plugins
  > blog      # Read articles
  > about     # Who builds this
  > ^C        # Close menu
- Accessibility: Ensure keyboard navigation works, screen reader friendly
- Mobile: Falls back to hamburger menu on small screens, but maintains terminal aesthetic
</implementation_notes>
</feature>

<feature id="2" priority="high">
<name>Homepage Hero Terminal Animation</name>
<description>
Animated terminal sequence that types out tool discovery process. Fast typing animation (~2 seconds total), then becomes static with blinking cursor at prompt.
</description>
<implementation_notes>
Animation sequence:
```
$ cd ~/projects/channel47
$ ./discover-tools.sh

Scanning workspace... ✓
Found 3 battle-tested plugins
Quality > quantity

┌─ Featured Tools ──────────────┐
│                               │
│  [Tool cards appear here]     │
│                               │
└───────────────────────────────┘

$ ▊
```

Technical requirements:
- Use CSS animations + JavaScript for typing effect
- Character-by-character reveal at ~50ms per character
- Cursor blink animation (1s interval)
- Respect prefers-reduced-motion for accessibility
- Consider using requestAnimationFrame for smooth performance
</implementation_notes>
</feature>

<feature id="3" priority="high">
<name>Terminal-Style Hover States</name>
<description>
All interactive elements get terminal cursor prefix and subtle glow on hover. Creates cohesive interaction pattern across entire site.
</description>
<implementation_notes>
Hover effect components:
1. Prefix addition: "> " appears before element text
2. Cursor addition: Blinking underscore "_" after text
3. Background glow: Subtle rgba(0, 255, 159, 0.1) background
4. Text color shift: Slightly brighter on hover

CSS approach:
- Use ::before pseudo-element for prefix
- Use ::after pseudo-element for cursor
- Animate cursor blink with @keyframes
- Apply to: links, buttons, cards, navigation items

Performance consideration: Use CSS transforms/opacity for animations (GPU accelerated)
</implementation_notes>
</feature>

<feature id="4" priority="medium">
<name>ASCII Art Plugin Icons</name>
<description>
Replace generic plugin visuals with custom ASCII art icons. Each plugin gets unique ASCII representation that appears in cards and headers.
</description>
<implementation_notes>
Icon examples:
```
Creative Writing:
 ___
|   |✎
|___|

ASCII Art:
╭──────────╮
│ ASCII    │
│   ART    │
╰──────────╯

Google Ads:
 [$]
 [$$]
[$$$]
```

Implementation:
- Store ASCII art in plugin frontmatter/metadata
- Render in <pre> tags with proper font (monospace)
- Ensure proper spacing and alignment
- Consider color variations using ANSI-style color classes
</implementation_notes>
</feature>

<feature id="5" priority="medium">
<name>ASCII Art Loading States</name>
<description>
Replace spinners with ASCII art progress indicators for page transitions and data loading.
</description>
<implementation_notes>
Animation frames:
```
Frame 1: [>    ] Loading...
Frame 2: [>>   ] Loading...
Frame 3: [>>>  ] Loading...
Frame 4: [>>>> ] Loading...
Frame 5: [>>>>>] Complete!
```

Alternative spinner:
```
Frame 1: |
Frame 2: /
Frame 3: —
Frame 4: \
(rotates)
```

Implementation:
- CSS @keyframes or JavaScript interval
- Use in Astro loading states, form submissions, page transitions
- Duration: ~1.5s for full cycle
</implementation_notes>
</feature>

<feature id="6" priority="medium">
<name>Command-Style CTAs with Execution Animation</name>
<description>
Primary buttons styled as terminal commands. On click, show brief execution animation with success state.
</description>
<implementation_notes>
Button states:
1. Initial: [$ install ascii-art]
2. Loading: [$ install ascii-art...]
3. Success: [✓ Installed successfully]

Implementation:
- Button contains command text with $ prefix
- Click triggers state change: default → loading → success
- Loading: Append "..." with animation
- Success: Replace with checkmark, change color to green
- Reset after 2 seconds OR provide "copy command" functionality
- One-click copy to clipboard for installation commands
</implementation_notes>
</feature>

<feature id="7" priority="low">
<name>Easter Egg Footer Terminal</name>
<description>
Hidden interactive terminal in footer. Users can type actual commands that trigger responses.
</description>
<implementation_notes>
Available commands:
- `ls` → Shows list of tools with brief descriptions
- `whoami` → Shows site creator info
- `help` → Shows available commands
- `clear` → Clears terminal output
- `history` → Shows command history
- `matrix` → Triggers Matrix-style character rain animation
- `konami` → Special easter egg (optional)

Implementation:
- Input field styled as terminal prompt: "$ _"
- Command parsing with simple switch/case
- Output area shows command results in terminal format
- Persist command history in sessionStorage
- Matrix effect: Canvas overlay with falling green characters
- Accessible: Proper labels, keyboard navigation
</implementation_notes>
</feature>

<feature id="8" priority="medium">
<name>Category Filter Animated ASCII Boxes</name>
<description>
On tools/plugins page, active category filter gets animated ASCII box drawn around it.
</description>
<implementation_notes>
Animation sequence (draw lines in order):
```
Step 1: ┌
Step 2: ┌──────────
Step 3: ┌──────────┐
Step 4: ┌──────────┐
        │ creative │
Step 5: ┌──────────┐
        │ creative │
        └──────────┘
```

Implementation:
- CSS animations for each line segment
- Use pseudo-elements or SVG for line drawing
- Timing: ~300ms total animation
- Active state persists until another filter selected
</implementation_notes>
</feature>

</key_features>

<content_changes>
<homepage>
Simplified structure:
1. Hero Section: Animated terminal sequence (feature #2)
2. Featured Tools: Maximum 3 tools, larger cards with ASCII icons
3. Browse CTA: Single prominent button "$ ./browse_all.sh"
4. Newsletter: Redesigned as command-style signup "$ subscribe --to updates"
5. Footer: Copyright + theme toggle + easter egg terminal

Remove:
- "Latest from the blog" section (until posts exist)
- Redundant copy
- Multiple CTAs competing for attention
</homepage>

<tools_page>
Changes:
- Larger tool cards with ASCII art icons prominent
- Installation command front-and-center with one-click copy
- Category filters with ASCII box animations (feature #8)
- Grid layout with generous spacing (terminal line rhythm)
</tools_page>

<plugin_detail_pages>
Changes:
- Large ASCII art icon at top
- Installation command as primary CTA
- Code samples in terminal-style windows
- Use box-drawing characters for section dividers
</plugin_detail_pages>
</content_changes>

</design_specifications>

<implementation_methodology>

<phase number="1" priority="critical">
<title>Foundation: Color Palette & Typography</title>
<tasks>
1. Explore current codebase structure:
   - Identify global CSS/SCSS files
   - Locate existing CSS custom properties (variables)
   - Find component styling patterns
   - Check for existing theme system

2. Implement design tokens:
   - Create/update CSS custom properties for color palette
   - Add typography variables (fonts, sizes, line heights)
   - Add spacing system variables
   - Add transition/animation variables

3. Update global styles:
   - Set background to terminal black (#0a0e14)
   - Set text color to terminal white (#e6edf3)
   - Import JetBrains Mono font (Google Fonts or self-hosted)
   - Import Inter Variable font
   - Apply font families to respective elements (h1-h6 = mono, body = sans)

4. Verify changes:
   - Check all pages render correctly
   - Ensure text contrast meets WCAG AA standards (should pass easily with these colors)
   - Test dark mode toggle (if exists) - may need to disable or adapt

Expected outcome: Immediate visual transformation - site should feel dramatically different with just color/typography changes.
</tasks>
</phase>

<phase number="2" priority="high">
<title>Interactive Foundation: Hover States</title>
<tasks>
1. Create reusable CSS classes for terminal hover effects:
   ```css
   .terminal-hover {
     position: relative;
     transition: var(--transition-fast);
   }

   .terminal-hover:hover {
     background-color: var(--color-bg-hover);
     color: var(--color-interactive);
   }

   .terminal-hover:hover::before {
     content: "> ";
     /* positioning */
   }

   .terminal-hover:hover::after {
     content: "_";
     animation: cursor-blink 1s infinite;
     /* positioning */
   }

   @keyframes cursor-blink {
     0%, 49% { opacity: 1; }
     50%, 100% { opacity: 0; }
   }
   ```

2. Apply to interactive elements:
   - Navigation links
   - Buttons
   - Tool cards
   - Footer links
   - Any clickable elements

3. Refine animations:
   - Ensure smooth transitions
   - Respect prefers-reduced-motion
   - Test performance (should be GPU-accelerated)

Expected outcome: Every interaction feels terminal-like. Cohesive experience across site.
</tasks>
</phase>

<phase number="3" priority="high">
<title>Hero Experience: Homepage Terminal Animation</title>
<tasks>
1. Create TerminalHero component (or update existing Hero):
   - Structure HTML with proper semantic elements
   - Create typing animation JavaScript
   - Implement cursor blink
   - Add box-drawing characters for featured tools container

2. Typing animation implementation:
   ```javascript
   const lines = [
     "$ cd ~/projects/channel47",
     "$ ./discover-tools.sh",
     "",
     "Scanning workspace... ✓",
     "Found 3 battle-tested plugins",
     "Quality > quantity",
     // ... etc
   ];

   // Character-by-character typing with ~50ms delay
   // Use requestAnimationFrame for smooth performance
   // Respect prefers-reduced-motion
   ```

3. Integration:
   - Replace existing homepage hero
   - Ensure responsive (mobile shows abbreviated version or static state)
   - Test performance across browsers

Expected outcome: Memorable first impression that defines entire site experience.
</tasks>
</phase>

<phase number="4" priority="medium">
<title>Visual Identity: ASCII Art Icons</title>
<tasks>
1. Design ASCII art icons for each plugin:
   - Review existing plugins list
   - Create 3-5 line ASCII representations
   - Store in plugin metadata/frontmatter

2. Create PluginIcon component:
   - Renders ASCII art in <pre> tag
   - Applies monospace font
   - Handles proper spacing/alignment
   - Optional: Color variations

3. Update plugin cards and detail pages:
   - Replace existing icons/images with ASCII art
   - Ensure proper sizing and visibility
   - Test readability at different screen sizes

Expected outcome: Unique visual identity. Every plugin instantly recognizable by its ASCII art.
</tasks>
</phase>

<phase number="5" priority="medium">
<title>Engagement: Easter Egg Terminal</title>
<tasks>
1. Create FooterTerminal component:
   - Input field with terminal prompt styling
   - Output area for command results
   - Command parser logic
   - Command implementations (ls, whoami, help, clear, matrix)

2. Matrix effect implementation:
   - Canvas overlay for character rain
   - Trigger via "matrix" command
   - Dismissible with ESC or click

3. Integration:
   - Add to footer (subtle, discoverable)
   - Test all commands
   - Ensure accessibility

Expected outcome: Delightful discovery moment. Shareable easter egg that showcases brand personality.
</tasks>
</phase>

<phase number="6" priority="medium">
<title>Navigation: Command-Style Header</title>
<tasks>
1. Create TerminalNav component:
   - Floating bar with terminal prompt
   - Expand/collapse animation
   - Command-style menu items
   - Mobile fallback

2. Implementation details:
   - Position: fixed at top
   - Semi-transparent background
   - Blinking cursor animation
   - Keyboard navigation support

3. Replace existing navigation:
   - Update header component
   - Ensure consistent across all pages
   - Test mobile experience

Expected outcome: Navigation that reinforces terminal aesthetic while remaining usable.
</tasks>
</phase>

<phase number="7" priority="low">
<title>Polish: Loading States, CTAs, Category Filters</title>
<tasks>
1. Create ASCII loading indicators:
   - Component for reusable loading states
   - Progress bar variant
   - Spinner variant
   - Apply to form submissions, page transitions

2. Update CTAs to command-style buttons:
   - Redesign primary buttons
   - Add execution animations
   - Implement one-click copy for installation commands

3. Add animated category filters:
   - ASCII box drawing animation
   - Active state management
   - Smooth transitions

Expected outcome: Cohesive details throughout. Every interaction reinforces terminal theme.
</tasks>
</phase>

</implementation_methodology>

<output_format>

For each implementation phase, provide:

<phase_implementation>
<phase_number>[1-7]</phase_number>

<thinking>
[Before implementing, think through:
- Current codebase structure relevant to this phase
- Potential conflicts with existing code
- Performance considerations
- Accessibility implications
- Edge cases to handle
- Testing approach]
</thinking>

<files_modified>
[List files created or modified, with brief description of changes]
</files_modified>

<code_changes>
[Actual code implementation - use code blocks with proper syntax highlighting]
</code_changes>

<verification_steps>
[How to verify this phase worked correctly:
- Visual checks
- Functional tests
- Accessibility tests
- Performance checks]
</verification_steps>

<next_phase_dependencies>
[What the next phase depends on from this phase]
</next_phase_dependencies>

</phase_implementation>

</output_format>

<examples>

<example>
<scenario>Implementing terminal hover states on navigation links</scenario>

<current_code>
```css
/* current navigation styles */
.nav-link {
  color: #333;
  text-decoration: none;
  padding: 0.5rem 1rem;
}

.nav-link:hover {
  color: #0066cc;
}
```
</current_code>

<enhanced_code>
```css
/* terminal-inspired navigation hover states */
.nav-link {
  position: relative;
  color: var(--color-text-primary);
  text-decoration: none;
  padding: var(--space-sm) var(--space-md);
  transition: var(--transition-fast);
  font-family: var(--font-mono);
}

.nav-link:hover {
  background-color: var(--color-bg-hover);
  color: var(--color-interactive);
}

/* Add terminal cursor prefix on hover */
.nav-link:hover::before {
  content: "> ";
  position: absolute;
  left: 0.25rem;
  color: var(--color-interactive);
}

/* Add blinking cursor after text on hover */
.nav-link:hover::after {
  content: "_";
  margin-left: 0.25rem;
  animation: cursor-blink 1s step-end infinite;
  color: var(--color-interactive);
}

@keyframes cursor-blink {
  0%, 49% { opacity: 1; }
  50%, 100% { opacity: 0; }
}

/* Respect reduced motion preferences */
@media (prefers-reduced-motion: reduce) {
  .nav-link {
    transition: none;
  }
  .nav-link:hover::after {
    animation: none;
    opacity: 1;
  }
}
```
</enhanced_code>

<explanation>
This example shows how to transform a standard navigation link into a terminal-style interactive element:
1. Uses CSS custom properties for colors and timing
2. Adds ">" prefix via ::before pseudo-element
3. Adds blinking "_" cursor via ::after pseudo-element
4. Includes subtle background glow on hover
5. Respects accessibility (prefers-reduced-motion)
6. Uses monospace font for terminal authenticity
</explanation>
</example>

<example>
<scenario>Creating animated ASCII box for active category filter</scenario>

<code>
```html
<button class="category-filter" data-category="creative" aria-pressed="false">
  <span class="filter-text">creative</span>
</button>
```

```css
.category-filter {
  position: relative;
  background: transparent;
  border: none;
  color: var(--color-text-secondary);
  font-family: var(--font-mono);
  padding: var(--space-sm) var(--space-md);
  cursor: pointer;
  transition: color var(--transition-fast);
}

.category-filter:hover {
  color: var(--color-interactive);
}

/* Active state with ASCII box */
.category-filter[aria-pressed="true"] {
  color: var(--color-interactive);
}

/* ASCII box drawn with pseudo-elements and borders */
.category-filter[aria-pressed="true"]::before {
  content: "";
  position: absolute;
  top: -4px;
  left: -4px;
  right: -4px;
  bottom: -4px;
  border: 1px solid var(--color-interactive);
  animation: draw-box 300ms ease-out forwards;
}

/* Draw box animation using clip-path */
@keyframes draw-box {
  0% {
    clip-path: polygon(0 0, 0 0, 0 0, 0 0);
  }
  25% {
    clip-path: polygon(0 0, 100% 0, 100% 0, 0 0);
  }
  50% {
    clip-path: polygon(0 0, 100% 0, 100% 100%, 0 100%);
  }
  100% {
    clip-path: polygon(0 0, 100% 0, 100% 100%, 0 100%);
  }
}
```

```javascript
// Toggle active state
document.querySelectorAll('.category-filter').forEach(button => {
  button.addEventListener('click', (e) => {
    // Remove active from all
    document.querySelectorAll('.category-filter').forEach(btn => {
      btn.setAttribute('aria-pressed', 'false');
    });

    // Set active on clicked
    e.currentTarget.setAttribute('aria-pressed', 'true');

    // Filter logic here...
  });
});
```
</code>

<explanation>
This shows how to create the animated ASCII box effect:
1. Uses aria-pressed for accessibility and state management
2. Pseudo-element creates the border
3. Clip-path animation makes border "draw" around text
4. JavaScript handles toggle logic
5. Maintains keyboard navigation and screen reader support
</explanation>
</example>

<example>
<scenario>One-click copy installation command button</scenario>

<code>
```html
<button class="install-command" data-command="claude plugins install ascii-art@channel47">
  <span class="command-prefix">$</span>
  <span class="command-text">claude plugins install ascii-art@channel47</span>
  <span class="copy-indicator">📋</span>
</button>
```

```css
.install-command {
  display: flex;
  align-items: center;
  gap: var(--space-xs);
  background-color: rgba(0, 255, 159, 0.1);
  border: 1px solid var(--color-interactive);
  color: var(--color-text-primary);
  font-family: var(--font-mono);
  font-size: var(--font-size-sm);
  padding: var(--space-sm) var(--space-md);
  cursor: pointer;
  transition: var(--transition-fast);
  border-radius: var(--border-radius);
  width: 100%;
  text-align: left;
}

.install-command:hover {
  background-color: rgba(0, 255, 159, 0.2);
  box-shadow: var(--glow-primary);
}

.command-prefix {
  color: var(--color-interactive);
  font-weight: bold;
}

.command-text {
  flex: 1;
  color: var(--color-text-primary);
}

.copy-indicator {
  opacity: 0;
  transition: opacity var(--transition-fast);
}

.install-command:hover .copy-indicator {
  opacity: 1;
}

/* Success state after copying */
.install-command.copied {
  background-color: rgba(0, 255, 159, 0.3);
}

.install-command.copied .command-prefix {
  content: "✓";
}

.install-command.copied .command-text::after {
  content: " — Copied!";
  color: var(--color-interactive);
  margin-left: var(--space-sm);
}
```

```javascript
// Copy to clipboard functionality
document.querySelectorAll('.install-command').forEach(button => {
  button.addEventListener('click', async (e) => {
    const command = e.currentTarget.dataset.command;

    try {
      await navigator.clipboard.writeText(command);

      // Show success state
      e.currentTarget.classList.add('copied');

      // Reset after 2 seconds
      setTimeout(() => {
        e.currentTarget.classList.remove('copied');
      }, 2000);

    } catch (err) {
      console.error('Failed to copy:', err);
      // Fallback: show manual copy prompt
    }
  });
});
```
</code>

<explanation>
This demonstrates the command-style CTA with one-click copy:
1. Styled as terminal command with $ prefix
2. Hover reveals copy indicator
3. Click copies to clipboard
4. Success state shows visual confirmation
5. Auto-resets after 2 seconds
6. Includes error handling and fallback
</explanation>
</example>

</examples>

<constraints>

<technical_constraints>
- Must maintain Astro framework compatibility
- Must be mobile-responsive (terminal aesthetic should adapt, not break)
- Must meet WCAG 2.1 AA accessibility standards minimum
- Must respect prefers-reduced-motion for all animations
- Must maintain performance (target: <100ms interaction response, <2s page load)
- Must support modern browsers (last 2 versions of Chrome, Firefox, Safari, Edge)
- Must work without JavaScript for core content (progressive enhancement)
</technical_constraints>

<design_constraints>
- Terminal aesthetic must enhance, not hinder, usability
- Monospace fonts should be limited to headings/special elements to avoid readability fatigue
- Animations should be fast (sub-second) - no slow, tedious typing effects
- Color contrast must be sufficient (terminal green on terminal black passes WCAG AA)
- Interactive elements must have clear affordances despite unique styling
- ASCII art must be readable and recognizable, not abstract or confusing
</design_constraints>

<edge_cases>
- User has prefers-reduced-motion enabled → Disable animations, show static states
- User has custom fonts disabled → Fallback fonts should maintain design intent
- Browser doesn't support CSS custom properties → Provide fallback colors
- JavaScript disabled → Core content and navigation must still function
- Very small screens (< 375px) → Simplify ASCII art, ensure readability
- Very large screens (> 2560px) → Prevent excessive stretching, maintain comfortable line length
- High contrast mode enabled → Ensure borders and text remain visible
- Screen reader users → All interactive elements properly labeled, command structure explained
</edge_cases>

</constraints>

<success_criteria>

After implementation, the site should demonstrate:

1. **Memorability**: First-time visitors should immediately think "this is different" and remember the terminal aesthetic
2. **Delight**: At least 3 moments of joy/surprise (hero animation, hover states, easter egg terminal)
3. **Simplicity**: Reduced cognitive load compared to before - clearer hierarchy, focused content
4. **Consistency**: Terminal theme evident on every page, in every interaction
5. **Performance**: Fast load times, smooth animations, responsive interactions
6. **Accessibility**: Fully keyboard navigable, screen reader friendly, respects user preferences
7. **Mobile Experience**: Works beautifully on phones (adapted, not broken)
8. **Brand Alignment**: Design perfectly reflects "CLI tools that add personality"

Verification questions:
- Would a developer visiting this site share it with colleagues because it's cool?
- Does the design make you want to explore more?
- Can you navigate and understand the content without confusion despite the unique aesthetic?
- Does it feel professional yet playful?
- Would you remember this site tomorrow?

</success_criteria>

</instructions>
```

## Usage Instructions

Copy the content above between the `<role>` and final `</instructions>` tags and paste it into Claude Code to begin implementation. Claude will:

1. First explore the current codebase structure
2. Think through each implementation phase systematically
3. Make changes following the prioritized phases
4. Provide verification steps for each phase
5. Handle edge cases and accessibility considerations
6. Deliver a unique, memorable, delightful terminal-inspired experience

The prompt is structured to ensure Claude:
- Understands the full design vision and rationale
- Implements changes systematically (foundation first, polish last)
- Thinks through implications before coding
- Creates accessible, performant, maintainable code
- Provides clear verification steps
- Handles edge cases appropriately
