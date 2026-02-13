# Media Buyer — Claude Code Plugin

Two skills. Zero fluff. Built for media buyers who run paid ads.

**Search Campaign Builder** — Give it a landing page URL, get back a complete Google Search campaign: keywords by intent, 15-headline RSAs, negative keyword defense, extensions, bidding strategy. Ready to upload to Google Ads Editor.

**Creative Variant Generator** — Give it a winning ad image, get back variations at three divergence levels (subtle, moderate, dramatic). Self-contained Python CLI that calls OpenAI or Google Gemini directly. No extra servers needed.

---

## Install

### 1. Clone or download this plugin

```bash
# Option A: Clone
git clone https://github.com/channel47/media-buyer.git

# Option B: Download and unzip
# Download from https://channel47.dev/plugins/media-buyer
```

### 2. Add to your Claude Code project

Copy the plugin folder into your project's `.claude/plugins/` directory:

```bash
mkdir -p .claude/plugins
cp -r media-buyer .claude/plugins/media-buyer
```

Or create a symlink if you cloned it elsewhere:

```bash
mkdir -p .claude/plugins
ln -s /path/to/media-buyer .claude/plugins/media-buyer
```

### 3. Install dependencies (for Creative Variants only)

The creative variant generator uses a Python script. Install its dependencies:

```bash
pip install openai google-genai Pillow
```

### 4. Set API keys (for Creative Variants only)

```bash
# For Google Gemini (default, recommended)
export GEMINI_API_KEY='your-key-here'

# OR for OpenAI
export OPENAI_API_KEY='your-key-here'
```

### 5. Use it

**Search Campaign:**
> "Build me a Google Search campaign for this landing page: https://example.com"

**Creative Variants:**
> Upload a winning ad image, then: "Generate 4 moderate variations of this ad"

That's it. Both skills work immediately with no additional setup beyond the above.

---

## What's Inside

```
media-buyer/
├── .claude-plugin/
│   └── plugin.json
├── skills/
│   ├── search-campaign/
│   │   ├── SKILL.md                    # The search campaign builder
│   │   └── references/
│   │       ├── ad-copy-formulas.md     # Headline & description patterns
│   │       ├── negative-keywords.md    # Industry negative keyword lists
│   │       └── worked-example.md       # Full Notion campaign walkthrough
│   └── creative-variants/
│       ├── SKILL.md                    # The creative variant generator
│       ├── scripts/
│       │   └── ad_variant_gen.py       # Self-contained image generation CLI
│       └── references/
│           ├── cli.md                  # CLI flags and recipes
│           ├── variation-strategies.md # Divergence framework deep dive
│           ├── prompt-patterns.md      # Prompt engineering for ad variants
│           └── platform-specs.md       # Ad sizes & safe zones by platform
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

Supports:
- Google Gemini (default — just needs a `GEMINI_API_KEY`)
- OpenAI gpt-image-1.5 (best for face/logo preservation)
- Google Imagen 4 (via Vertex AI)
- Platform-aware sizing (Facebook, Instagram, Google Display, TikTok, LinkedIn, Pinterest)
- Dry run mode to preview prompts before spending tokens

---

## Requirements

| Skill | Requires |
|-------|----------|
| Search Campaign | Nothing — works out of the box |
| Creative Variants | Python 3.9+, `openai` or `google-genai` package, API key |

---

## Built by Channel 47

[channel47.dev](https://channel47.dev) — AI skills for marketers who ship.

Questions? [jackson@channel47.dev](mailto:jackson@channel47.dev)
