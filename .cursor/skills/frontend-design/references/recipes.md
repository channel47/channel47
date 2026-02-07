# Recipes. ch47.

Full component patterns. Every recipe uses the ch47 materials and signature moves. Understand why each decision was made before changing it.

## Landing Page

A landing page is a sequence, not a template. Each section shifts the reader's experience. Density changes, width changes, volume changes. Never predictable.

```jsx
export default function LandingPage() {
  return (
    <main style={{ backgroundColor: "#0C0A09", color: "#E7E5E4", fontFamily: "'JetBrains Mono', monospace" }}>

      {/* ---- ACT 1: THE OPENING ----
          Dark. Asymmetric. Type commands the space.
          The headline uses Space Grotesk at display scale.
          Left-aligned. Never centered for hero text. */}
      <section style={{
        minHeight: "90vh", display: "flex", flexDirection: "column",
        justifyContent: "flex-end",
        padding: "0 clamp(24px, 5vw, 64px) clamp(60px, 10vh, 100px)",
        position: "relative",
      }}>
        {/* Accent bar: the broadcast indicator */}
        <div style={{ width: 40, height: 2, backgroundColor: "#F59E0B", marginBottom: 24 }} />

        <p style={{
          fontSize: 11, textTransform: "uppercase",
          letterSpacing: "0.15em", color: "#78716C", marginBottom: 20,
        }}>
          ch47 / Build log
        </p>

        <h1 style={{
          fontFamily: "'Space Grotesk', system-ui, sans-serif",
          fontSize: "clamp(2.75rem, 10vw, 7rem)",
          lineHeight: 0.9, letterSpacing: "-0.04em",
          fontWeight: 600, maxWidth: 900,
        }}>
          Ship things that
          <br />
          <span style={{ color: "#F59E0B" }}>matter.</span>
        </h1>

        <p style={{
          fontSize: 14, lineHeight: 1.7,
          color: "#A8A29E", maxWidth: 420, marginTop: 32,
          letterSpacing: "0.02em",
        }}>
          One sentence. What this does. Who it's for. No buzzwords.
          Written in mono because this is a transmission, not a brochure.
        </p>
      </section>

      {/* ---- ACT 2: PROOF BAR ----
          Understated. Numbers or names at low opacity.
          Thin borders above and below. Dense, quiet. */}
      <section style={{
        borderTop: "1px solid #44403C", borderBottom: "1px solid #44403C",
        padding: "20px clamp(24px, 5vw, 64px)",
        display: "flex", justifyContent: "center", flexWrap: "wrap",
        gap: "clamp(24px, 5vw, 56px)",
      }}>
        {["4,200+ readers", "52% open rate", "87 issues shipped"].map(s => (
          <span key={s} style={{
            fontSize: 11, textTransform: "uppercase",
            letterSpacing: "0.15em", color: "#44403C",
          }}>
            {s}
          </span>
        ))}
      </section>

      {/* ---- ACT 3: ASYMMETRIC FEATURES ----
          Two panels. Unequal widths. 1px gap creates border.
          One panel is elevated (Smoke), one is Soot. */}
      <section>
        <div style={{
          display: "grid",
          gridTemplateColumns: "repeat(auto-fit, minmax(min(100%, 340px), 1fr))",
          gap: 1, backgroundColor: "#44403C",
        }}>
          <div style={{
            backgroundColor: "#1C1917",
            padding: "clamp(32px, 5vh, 56px) clamp(24px, 4vw, 48px)",
            minHeight: 360,
          }}>
            <div style={{ width: 32, height: 2, backgroundColor: "#F59E0B", marginBottom: 24 }} />
            <span style={{ fontSize: 11, textTransform: "uppercase", letterSpacing: "0.15em", color: "#78716C" }}>
              047.1
            </span>
            <h3 style={{
              fontFamily: "'Space Grotesk', system-ui", fontWeight: 500,
              fontSize: "clamp(1.5rem, 3vw, 2rem)",
              letterSpacing: "-0.02em", lineHeight: 1.15, marginTop: 12,
              color: "#F5F0EB",
            }}>
              The primary thing
            </h3>
            <p style={{
              fontSize: 14, lineHeight: 1.7, color: "#A8A29E",
              marginTop: 16, maxWidth: 400, letterSpacing: "0.02em",
            }}>
              Real depth. What this does and why it exists.
              Three sentences minimum. Written like you're explaining it
              to someone sharp, not someone slow.
            </p>
          </div>

          <div style={{
            backgroundColor: "#292524",
            padding: "clamp(32px, 5vh, 56px) clamp(24px, 4vw, 48px)",
            minHeight: 360,
          }}>
            <span style={{ fontSize: 11, textTransform: "uppercase", letterSpacing: "0.15em", color: "#78716C" }}>
              047.2
            </span>
            <h3 style={{
              fontFamily: "'Space Grotesk', system-ui", fontWeight: 500,
              fontSize: "clamp(1.5rem, 3vw, 2rem)",
              letterSpacing: "-0.02em", lineHeight: 1.15, marginTop: 12,
              color: "#F5F0EB",
            }}>
              The supporting thing
            </h3>
            <p style={{
              fontSize: 14, lineHeight: 1.7, color: "#A8A29E",
              marginTop: 16, letterSpacing: "0.02em",
            }}>
              Shorter. The asymmetry is intentional.
            </p>
          </div>
        </div>
      </section>

      {/* ---- ACT 4: THE RUPTURE ----
          Light inversion on a dark-first page.
          Cream section. Space Grotesk headline, mono body.
          Same Signal accent (#F59E0B), same type family.
          The rupture breaks RHYTHM, not BRAND.
          Everything still looks like ch47, just on a light surface. */}
      <section style={{
        backgroundColor: "#FAF7F2", color: "#1C1917",
        padding: "clamp(80px, 14vh, 140px) clamp(24px, 5vw, 64px)",
        position: "relative",
      }}>
        {/* Vertical accent bar */}
        <div style={{
          position: "absolute",
          left: "clamp(24px, 5vw, 64px)", top: "clamp(80px, 14vh, 140px)",
          width: 2, height: 40, backgroundColor: "#F59E0B",
        }} />

        <div style={{ maxWidth: 600, marginLeft: "clamp(0px, 8%, 120px)" }}>
          <span style={{
            fontFamily: "'JetBrains Mono', monospace",
            fontSize: 11, textTransform: "uppercase",
            letterSpacing: "0.15em", color: "#78716C",
            display: "block", marginBottom: 24,
          }}>
            047 / Transmission
          </span>

          <h2 style={{
            fontFamily: "'Space Grotesk', system-ui, sans-serif",
            fontSize: "clamp(1.75rem, 4vw, 2.75rem)",
            fontWeight: 600, letterSpacing: "-0.03em",
            lineHeight: 1.1, margin: 0, color: "#1C1917",
          }}>
            A statement or pull quote that earns this space.
          </h2>

          <p style={{
            fontFamily: "'JetBrains Mono', monospace",
            fontSize: 14, lineHeight: 1.7, color: "#78716C",
            marginTop: 20, letterSpacing: "0.02em",
          }}>
            Context or attribution. Same mono, same voice.
            The light surface is the contrast. Not the typography.
          </p>

          <div style={{ display: "flex", alignItems: "center", gap: 10, marginTop: 24 }}>
            <div style={{
              width: 32, height: 32, borderRadius: "50%",
              backgroundColor: "#F0EBE3", border: "1px solid #D6D3CD",
              display: "flex", alignItems: "center", justifyContent: "center",
              fontFamily: "'JetBrains Mono', monospace",
              fontSize: 11, color: "#78716C", fontWeight: 600,
            }}>47</div>
            <div>
              <span style={{
                fontFamily: "'JetBrains Mono', monospace",
                fontSize: 13, color: "#1C1917", display: "block",
              }}>Full Name</span>
              <span style={{
                fontFamily: "'JetBrains Mono', monospace",
                fontSize: 11, textTransform: "uppercase",
                letterSpacing: "0.15em", color: "#78716C",
              }}>What they actually do</span>
            </div>
          </div>
        </div>
      </section>

      {/* ---- ACT 5: THE CLOSE ----
          Back to dark. Minimal. CTA doesn't beg. */}
      <section style={{
        padding: "clamp(80px, 14vh, 140px) clamp(24px, 5vw, 64px)",
        textAlign: "center",
      }}>
        <p style={{
          fontSize: 11, textTransform: "uppercase",
          letterSpacing: "0.15em", color: "#78716C", marginBottom: 24,
        }}>
          Transmitting
        </p>
        <a href="/start" style={{
          fontFamily: "'Space Grotesk', system-ui",
          fontSize: "clamp(1.5rem, 4vw, 2.5rem)",
          fontWeight: 500, color: "#F5F0EB",
          textDecoration: "underline",
          textUnderlineOffset: 10,
          textDecorationColor: "#F59E0B",
          textDecorationThickness: 2,
          cursor: "pointer",
        }}>
          Get started
        </a>
      </section>
    </main>
  );
}
```

**The five acts:** Accent bar + display headline (the statement). Proof bar (quiet credibility). Asymmetric features (the substance). Light rupture (the pattern break, in-brand). Confident close (the ask). Each act shifts density, width, or color. The reader never knows what's next.

**Rupture coherence.** The light section uses Space Grotesk for the headline and JetBrains Mono for body/labels. Same type family as the rest of the page. Signal stays #F59E0B. The contrast comes from the surface flip (dark to cream), not from introducing new fonts or colors.

**What's missing on purpose:** No three-column icon grid. No "How it works" steps. No testimonials carousel. No scanline overlay. No pulsing indicators. Those earn their way in per-project, they're not default sections.

## Directory / Archive

Dense data, dark surface. The mono-first aesthetic thrives in lists.

```jsx
export default function Directory({ items, title }) {
  return (
    <section style={{ backgroundColor: "#0C0A09", color: "#E7E5E4", fontFamily: "'JetBrains Mono', monospace" }}>
      <header style={{ padding: "80px clamp(24px, 5vw, 64px) 40px" }}>
        <div style={{ width: 32, height: 2, backgroundColor: "#F59E0B", marginBottom: 20 }} />
        <span style={{ fontSize: 11, textTransform: "uppercase", letterSpacing: "0.15em", color: "#78716C" }}>
          Archive
        </span>
        <h1 style={{
          fontFamily: "'Space Grotesk', system-ui",
          fontSize: "clamp(2rem, 5vw, 3rem)",
          letterSpacing: "-0.03em", lineHeight: 1, fontWeight: 600,
          marginTop: 12, color: "#F5F0EB",
        }}>
          {title || "All transmissions"}
        </h1>
      </header>

      <div style={{ padding: "0 clamp(24px, 5vw, 64px) 80px" }}>
        {(items || []).map((item, i) => (
          <a
            key={i} href={item.url || "#"}
            style={{
              display: "flex", alignItems: "center", justifyContent: "space-between",
              padding: "18px 0", borderBottom: "1px solid #44403C",
              textDecoration: "none", color: "#E7E5E4",
            }}
          >
            <div style={{ display: "flex", alignItems: "baseline", gap: 16, minWidth: 0 }}>
              <span style={{ fontSize: 11, color: "#44403C", letterSpacing: "0.1em", flexShrink: 0 }}>
                {String(i + 1).padStart(3, "0")}
              </span>
              <span style={{
                fontSize: "clamp(1rem, 2vw, 1.25rem)",
                fontWeight: 500, overflow: "hidden",
                textOverflow: "ellipsis", whiteSpace: "nowrap",
              }}>
                {item.title}
              </span>
            </div>
            <div style={{ display: "flex", alignItems: "baseline", gap: 10, flexShrink: 0, marginLeft: 16 }}>
              <span style={{ fontSize: 11, color: "#78716C", textTransform: "uppercase", letterSpacing: "0.1em" }}>
                {item.date}
              </span>
              <span style={{ color: "#44403C", transition: "color 100ms" }}>→</span>
            </div>
          </a>
        ))}
      </div>
    </section>
  );
}
```

The arrow shifts to Signal on hover (implement via onMouseEnter on the arrow span). The three-digit index (001, 002...) gives the list a catalog feel.

## Dashboard

Information-dense. Monospace carries almost everything. Signal marks the metrics that matter.

```jsx
export default function Dashboard() {
  return (
    <div style={{ minHeight: "100vh", backgroundColor: "#0C0A09", color: "#E7E5E4", fontFamily: "'JetBrains Mono', monospace" }}>
      {/* Top bar */}
      <header style={{
        borderBottom: "1px solid #44403C",
        padding: "12px clamp(24px, 5vw, 64px)",
        display: "flex", alignItems: "center", justifyContent: "space-between",
        fontSize: 13,
      }}>
        <span style={{ fontWeight: 500 }}>ch47</span>
        <span style={{ fontSize: 11, color: "#78716C", textTransform: "uppercase", letterSpacing: "0.1em" }}>
          Status
        </span>
      </header>

      <div style={{ padding: "32px clamp(24px, 5vw, 64px)", maxWidth: 1200 }}>
        {/* Stat cards */}
        <div style={{
          display: "grid",
          gridTemplateColumns: "repeat(auto-fit, minmax(180px, 1fr))",
          gap: 1, backgroundColor: "#44403C",
          border: "1px solid #44403C",
        }}>
          {[
            { label: "Subscribers", value: "4,201", change: "+14%", up: true },
            { label: "Open rate", value: "52%", change: "+3%", up: true },
            { label: "Click rate", value: "8.4%", change: "-0.2%", up: false },
            { label: "Revenue", value: "$2,340", change: "+22%", up: true },
          ].map(stat => (
            <div key={stat.label} style={{ backgroundColor: "#1C1917", padding: "20px 24px" }}>
              <span style={{
                fontSize: 11, textTransform: "uppercase",
                letterSpacing: "0.15em", color: "#78716C",
              }}>{stat.label}</span>
              <p style={{
                fontFamily: "'Space Grotesk', system-ui",
                fontSize: "clamp(1.5rem, 3vw, 2rem)",
                fontWeight: 600, letterSpacing: "-0.02em",
                marginTop: 8, color: "#F5F0EB",
              }}>{stat.value}</p>
              <span style={{
                fontSize: 11, marginTop: 4, display: "inline-block",
                color: stat.up ? "#22C55E" : "#F59E0B",
              }}>{stat.change}</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
```

Green (#22C55E) is the only non-palette color allowed, and only for positive metrics. Negative metrics use Signal (amber). This creates an instant visual hierarchy: green = good, amber = attention.

## Forms

Mono labels. Underline inputs. Signal focus state. No rounded corners. No box shadows.

```jsx
<form style={{ maxWidth: 400 }}>
  <div style={{ marginBottom: 32 }}>
    <label style={{
      display: "block", fontFamily: "'JetBrains Mono', monospace",
      fontSize: 11, textTransform: "uppercase",
      letterSpacing: "0.15em", color: "#78716C", marginBottom: 12,
    }}>
      Email
    </label>
    <input
      type="email"
      placeholder="you@example.com"
      style={{
        width: "100%", padding: "12px 0",
        backgroundColor: "transparent", color: "#E7E5E4",
        border: "none", borderBottom: "1px solid #44403C",
        fontFamily: "'JetBrains Mono', monospace",
        fontSize: 14, outline: "none",
        transition: "border-color 100ms",
      }}
      onFocus={e => e.target.style.borderBottomColor = "#F59E0B"}
      onBlur={e => e.target.style.borderBottomColor = "#44403C"}
    />
  </div>

  <button style={{
    fontFamily: "'JetBrains Mono', monospace",
    fontSize: 11, textTransform: "uppercase",
    letterSpacing: "0.1em",
    padding: "12px 24px",
    backgroundColor: "#F59E0B", color: "#0C0A09",
    border: "none", borderRadius: 2,
    cursor: "pointer", fontWeight: 500,
  }}>
    Subscribe
  </button>
</form>
```

The Signal-colored submit button is the one hot element in the form. Everything else is muted. The focus state on inputs shifts the bottom border to Signal. Minimal, functional, specific.

## Button Hierarchy

```jsx
{/* Primary: Signal fill. One per view max. */}
<button style={{
  fontFamily: "'JetBrains Mono', monospace", fontSize: 11,
  textTransform: "uppercase", letterSpacing: "0.1em",
  padding: "10px 20px", backgroundColor: "#F59E0B",
  color: "#0C0A09", border: "none", borderRadius: 2,
}}>Primary</button>

{/* Secondary: border, inverts on hover */}
<button style={{
  fontFamily: "'JetBrains Mono', monospace", fontSize: 11,
  textTransform: "uppercase", letterSpacing: "0.1em",
  padding: "10px 20px", backgroundColor: "transparent",
  color: "#E7E5E4", border: "1px solid #44403C", borderRadius: 2,
}}>Secondary</button>

{/* Tertiary: text link with Signal color */}
<button style={{
  fontFamily: "'JetBrains Mono', monospace", fontSize: 13,
  color: "#F59E0B", background: "none", border: "none",
  textDecoration: "underline", textUnderlineOffset: 4,
  textDecorationColor: "rgba(245,158,11,0.4)",
}}>Tertiary</button>
```

## Light Mode Override

Apply to any recipe. The structure stays identical. Only materials swap.

```css
[data-theme="light"] {
  --bg:         #FAF7F2;
  --bg-alt:     #F0EBE3;
  --surface:    #FFFFFF;
  --text:       #1C1917;
  --text-muted: #78716C;
  --border:     #D6D3CD;
  --signal:     #F59E0B;
  --signal-wash:#FEF3C7;
}
```

Signal stays #F59E0B on light. Everything else warms. No cool tones. Ever.
