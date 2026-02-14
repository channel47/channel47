# Media Buyer — Claude Code Plugin

Three skills. Zero fluff. Built for media buyers who run paid ads.

**Search Campaign Builder** — Give it a landing page URL, get back a complete Google Search campaign: keywords by intent, 15-headline RSAs, negative keyword defense, extensions, bidding strategy. Ready to upload to Google Ads Editor.

**Creative Variant Generator** — Give it a winning ad image, get back variations at three divergence levels (subtle, moderate, dramatic). Self-contained Python CLI that calls OpenAI or Google Gemini directly. No extra servers needed.

**Account Audit** — Point it at a Google Ads account, get back a full health check: wasted spend analysis, keyword quality scores, search term mining, ad copy assessment, and prioritized recommendations with industry benchmarks.

---

## Install

```
/plugin marketplace add channel47/channel47
/plugin install media-buyer@channel47
```

### Dependencies (optional, by skill)

**Creative Variants** requires Python 3.9+ and an image generation API key:

```bash
pip install openai google-genai Pillow

# Google Gemini (default, recommended)
export GEMINI_API_KEY='your-key-here'

# OR OpenAI
export OPENAI_API_KEY='your-key-here'
```

**Account Audit** requires the Google Ads MCP server to be configured.

---

## What's Inside

```
media-buyer/
├── .claude-plugin/
│   └── plugin.json
├── hooks/
│   ├── hooks.json                     # Mutation safety gate
│   └── validate-mutations.py          # Flags live mutations before execution
├── skills/
│   ├── search-campaign/
│   │   ├── SKILL.md                   # The search campaign builder
│   │   └── references/
│   │       ├── ad-copy-formulas.md    # Headline & description patterns
│   │       ├── negative-keywords.md   # Industry negative keyword lists
│   │       └── worked-example.md      # Full campaign walkthrough
│   ├── creative-variants/
│   │   ├── SKILL.md                   # The creative variant generator
│   │   ├── scripts/
│   │   │   └── ad_variant_gen.py      # Self-contained image generation CLI
│   │   └── references/
│   │       ├── cli.md                 # CLI flags and recipes
│   │       ├── variation-strategies.md # Divergence framework deep dive
│   │       ├── prompt-patterns.md     # Prompt engineering for ad variants
│   │       └── platform-specs.md      # Ad sizes & safe zones by platform
│   └── audit/
│       ├── SKILL.md                   # Account health check
│       └── references/
│           └── performance-benchmarks.md # Industry averages by vertical
├── README.md
├── LICENSE
└── .gitignore
```

---

## Skill Details

### Search Campaign Builder

**Input:** A landing page URL + optional budget/geo/keywords.

**Output:** A complete, implementation-ready Google Search campaign including:
- Landing page analysis (value prop, proof points, audience signals)
- Keyword strategy organized by search intent
- Tightly themed ad groups (5-15 keywords each)
- RSA ad copy: 15 headlines + 4 descriptions per ad group
- Match type strategy (exact/phrase/broad)
- Negative keyword defense
- Extensions (sitelinks, callouts, structured snippets)
- Bidding and budget recommendations

No MCP servers required. No API keys. Just paste a URL and go.

### Creative Variant Generator

**Input:** A winning ad image + divergence level.

**Output:** Multiple ad creative variations preserving what works while testing new angles.

Three divergence levels:
- **Subtle** — Same ad, different skin. Background shifts, texture changes, shadow tweaks. Fights frequency fatigue.
- **Moderate** — Same formula, new clothes. Layout rearrangement, color palette shifts, copy angle rewording. Tests which elements actually drive performance.
- **Dramatic** — Same offer, fresh concept. Complete visual overhaul. Discovers new winning angles.

Supports Google Gemini, OpenAI gpt-image-1.5, Google Imagen 4, and platform-aware sizing for Facebook, Instagram, Google Display, TikTok, LinkedIn, and Pinterest.

### Account Audit

**Input:** A Google Ads Customer ID + industry vertical.

**Output:** An 8-phase account health check covering:
- Account-level KPIs vs industry benchmarks (CTR, CVR, CPA, ROAS)
- Campaign budget efficiency and impression share analysis
- Keyword quality scores and wasted spend identification
- Search terms mining (new keywords + negative recommendations)
- Ad copy strength and performance review
- Audience utilization assessment
- Prioritized recommendations report with estimated savings

Requires Google Ads MCP server. Read-only — never makes changes to the account.

---

## Safety

The mutation validation hook intercepts all Google Ads write operations. Dry runs pass silently. Live mutations get flagged with a warning before execution. Queries (read operations) always flow freely.

---

## Requirements

| Skill | Requires |
|-------|----------|
| Search Campaign | Nothing — works out of the box |
| Creative Variants | Python 3.9+, `openai` or `google-genai` package, API key |
| Account Audit | Google Ads MCP server configured |

---

## Built by Channel 47

[channel47.dev](https://channel47.dev) — AI skills for marketers who ship.
