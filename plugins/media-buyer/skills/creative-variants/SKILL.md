---
name: creative-variants
description: "Generate variations of winning ad creatives to extend campaign longevity and scale. Upload a reference image of a winning static ad (Facebook, Google, TikTok, LinkedIn, etc.) and get back multiple creative variations at configurable divergence levels (subtle, moderate, dramatic). Supports OpenAI gpt-image-1.5 and Google Gemini as generation backends. Self-contained — no MCP servers required. Triggers on: ad variations, creative variants, ad testing, split test creatives, ad fatigue, extend winning ad, scale ad creative, generate ad variants, creative refresh, ad iteration, winning ad variations, A/B test ads, ad creative generator, Facebook ad variants, Google ad variants, media buyer, performance creative."
---

# Ad Creative Variant Generator

Generate variations of winning ad creatives to fight fatigue, scale spend, and discover new winners.

Takes a reference image of a performing static ad → analyzes its winning elements → generates configurable variations that preserve what works while testing new angles.

---

## When to Use

- User uploads a winning ad image and wants variations
- User asks to "extend", "scale", "refresh", or "iterate" on an ad creative
- User wants to fight ad fatigue on a performing creative
- User needs split-test variants for Facebook, Google, TikTok, LinkedIn, or any paid channel
- User says "generate ad variants", "ad creative variations", or similar

---

## Core Workflow

```
1. RECEIVE   → User uploads reference ad image + context
2. ANALYZE   → Deconstruct the ad into its winning elements
3. PLAN      → Build variation specs at the requested divergence level
4. GENERATE  → Run the CLI to produce image variants
5. VALIDATE  → Inspect outputs, verify brand/structural integrity
6. ITERATE   → Refine any variant that missed the mark
7. DELIVER   → Output final variants + a manifest documenting each
```

Run the bundled CLI (`skills/creative-variants/scripts/ad_variant_gen.py`) with sensible defaults (see `references/cli.md`). For each variation, inspect the output and validate: brand consistency, layout integrity, copy legibility, CTA visibility, and adherence to the divergence level. Iterate with targeted prompt changes. Save final outputs and document the variation strategy used.

---

## Step 1: Receive & Classify

When the user provides a reference ad, gather the following. Ask ONLY if a critical detail is missing and blocks success; otherwise infer from context and proceed.

**Required:**
- Reference ad image (uploaded file)
- Divergence level: `subtle` | `moderate` | `dramatic` (default: `moderate`)

**Optional (infer when possible):**
- Ad platform (Facebook, Google, TikTok, LinkedIn, etc.)
- Product/service category
- Target audience
- Number of variants desired (default: 4)
- Specific elements to preserve or change
- Brand colors or guidelines
- Image generation provider: `openai` | `google` (default: `google` via Gemini)

---

## Step 2: Analyze the Reference Ad

Before generating anything, deconstruct the reference ad into a structured analysis. This is the foundation for all variations.

Build an **Ad Anatomy** by examining:

```
Ad Anatomy:
  Layout:        <grid structure, element placement, visual hierarchy>
  Hero element:  <primary visual — product shot, person, illustration, etc.>
  Copy:          <headline, subhead, body text — exact words if legible>
  CTA:           <call-to-action text, button style, placement>
  Color palette: <dominant, secondary, accent colors>
  Typography:    <style, weight, size relationships>
  Background:    <solid, gradient, photo, pattern, texture>
  Mood/tone:     <urgent, calm, playful, premium, etc.>
  Composition:   <rule of thirds, centered, asymmetric, etc.>
  Brand marks:   <logo placement, brand elements>
  Whitespace:    <density — airy, balanced, packed>
  Platform cues: <aspect ratio, safe zones, format hints>
```

State the analysis to the user before proceeding. This grounds the conversation and lets them correct any misreads.

---

## Step 3: Plan Variations

Map the divergence level to a variation strategy. Each level has a clear definition of what changes and what stays locked.

### Divergence Levels

**SUBTLE** — Same ad, different day. The viewer should feel familiarity.
- Locked: layout, copy, CTA, hero element, brand marks, composition
- Variable: background color/gradient shifts, lighting adjustments, minor texture changes, color temperature, shadow direction, subtle filter shifts
- Goal: Bypass frequency-based fatigue without losing the pattern that converts
- Typical changes: 1–2 elements, surface-level only

**MODERATE** — Recognizably related, clearly different. The winning formula with new clothes.
- Locked: hero element (or close variant), CTA intent, core message, brand marks
- Variable: background scene, color palette shifts, layout rearrangement, typography weight/style, copy angle rewording, image cropping/framing, mood shift
- Goal: Test which supporting elements actually drive performance vs. the core offer
- Typical changes: 3–5 elements, structural shifts allowed

**DRAMATIC** — Same product/offer, fresh creative concept. A new ad inspired by the winner.
- Locked: product/offer, brand identity, CTA purpose
- Variable: everything else — layout, visual style, color palette, composition, copy angle, background, mood, art direction
- Goal: Discover entirely new winning angles while keeping the proven offer
- Typical changes: near-total creative overhaul, only the strategic core survives

### Variation Spec

For each planned variant, write a structured spec:

```
Variant [N]:
  Divergence:     <subtle|moderate|dramatic>
  Strategy:       <1-line description of what this variant tests>
  Preserve:       <elements kept from original>
  Change:         <elements being modified + how>
  Rationale:      <why this variation might perform — ties to ad psychology>
  Prompt notes:   <specific prompt engineering considerations>
```

Present the plan to the user before generating. Let them approve, adjust, or redirect.

---

## Step 4: Generate Variants

### Provider Configuration

The CLI supports two providers with three backends. Use Google Gemini by default; switch to OpenAI if the user requests it or if the task requires capabilities Gemini lacks (e.g., high-fidelity face/logo preservation).

**Google Gemini (default) — `--provider google --google-backend gemini`:**
- Model: `gemini-3-pro-image-preview` (Nano Banana Pro — reasoning-enhanced, better text rendering, supports both generation and editing)
- Simpler API — works with a Gemini Developer API key, no Vertex AI required
- Both gen and edit use `client.models.generate_content()` with image input
- Requires: `GEMINI_API_KEY` or `GOOGLE_API_KEY` env var

**OpenAI — `--provider openai`:**
- Model: `gpt-image-1.5` (latest, Dec 2025 — better instruction following, logo/face preservation)
- Mode: `edit` with the reference image as input for subtle/moderate; `generate` for dramatic
- API: OpenAI Images API via Python SDK (`openai` package)
- Sizes: `1024x1024`, `1536x1024` (landscape), `1024x1536` (portrait), `auto`
- Key parameter: `input_fidelity=high` — preserves faces, logos, and brand elements in edits (default for this skill)
- Quality: `low` (fast/cheap), `medium`, `high` (default), `auto`
- Output formats: `png` (default), `jpeg` (faster), `webp`
- Requires: `OPENAI_API_KEY` env var

**Google Imagen — `--provider google --google-backend imagen`:**
- Generate model: `imagen-4.0-generate-001` (also `ultra` and `fast` variants)
- Edit model: `imagen-3.0-capability-001` (Imagen 4 does NOT support editing)
- **Important:** Imagen editing requires Vertex AI. If Vertex AI is not configured, the CLI auto-falls back to the Gemini backend for edits.
- Sizes: aspect ratios (`1:1`, `4:3`, `3:4`, `16:9`, `9:16`)
- Requires: `GEMINI_API_KEY` / `GOOGLE_API_KEY` for generation, or Vertex AI credentials for editing

### Prompt Engineering for Ad Variants

Reformat each variation spec into a production prompt. Follow these principles:

1. **Anchor to the reference.** Start every prompt with what's being preserved from the original.
2. **Be surgical about changes.** Name exactly what changes and how. Vague prompts produce unpredictable results.
3. **Include ad-specific constraints.** Always specify: no watermarks, no placeholder text, text must be legible, CTA must be prominent.
4. **Specify the output context.** "This is a paid social media ad for [platform]" grounds the model.
5. **Include negative constraints.** Explicitly state what to avoid — especially common AI image artifacts that kill ad performance (uncanny faces, garbled text, weird hands, logo distortion).

**Prompt template:**

```
[CONTEXT]
This is a static image ad for [platform]. The original ad is performing well and I need a variation.

[PRESERVE — do not change these elements]
<locked elements from variation spec>

[CHANGE — modify these elements as described]
<variable elements with specific instructions>

[CONSTRAINTS]
- Maintain professional advertising quality
- All text must be sharp and legible
- CTA must be clearly visible and prominent
- No watermarks, no stock photo indicators
- No AI artifacts (distorted text, uncanny faces, extra fingers)
- Output must work as a standalone ad — no borders, no mockup frames
- Aspect ratio: [platform-appropriate ratio]

[AVOID]
<negative constraints specific to this variant>
```

### CLI Execution

```bash
# Basic variant generation (Google Gemini default, moderate divergence)
python3 skills/creative-variants/scripts/ad_variant_gen.py \
  --reference path/to/winning-ad.png \
  --divergence moderate \
  --variants 4 \
  --out-dir output/ad-variants/

# OpenAI for high-fidelity face/logo preservation
python3 skills/creative-variants/scripts/ad_variant_gen.py \
  --reference path/to/winning-ad.png \
  --provider openai \
  --divergence subtle \
  --variants 6 \
  --out-dir output/ad-variants/

# Google Imagen 4 for dramatic variants (generation only)
python3 skills/creative-variants/scripts/ad_variant_gen.py \
  --reference path/to/winning-ad.png \
  --google-backend imagen \
  --divergence dramatic \
  --variants 3 \
  --out-dir output/ad-variants/

# Platform-aware sizing with faster jpeg output
python3 skills/creative-variants/scripts/ad_variant_gen.py \
  --reference path/to/winning-ad.png \
  --divergence moderate \
  --variants 3 \
  --platform facebook-feed \
  --output-format jpeg \
  --out-dir output/ad-variants/
```

See `references/cli.md` for all flags and recipes.

---

## Step 5: Validate & Iterate

After each generation, inspect the output image and check:

- [ ] **Brand integrity** — Logo, colors, and brand elements are correct and undistorted
- [ ] **Text legibility** — All copy is sharp, readable, and correctly spelled
- [ ] **CTA visibility** — Call-to-action is prominent and clickable-looking
- [ ] **Divergence fidelity** — The variant matches the requested divergence level (not too similar, not too different)
- [ ] **Platform compliance** — Aspect ratio, safe zones, text-to-image ratio (Facebook's ~20% text guideline)
- [ ] **No AI artifacts** — No garbled text, extra limbs, uncanny faces, melted objects
- [ ] **Ad effectiveness** — Would this stop a thumb? Does the visual hierarchy work?

If a variant fails any check, iterate with a single targeted change to the prompt. Do not overhaul — make one surgical fix and re-run. The iteration loop:

```
Generate → Inspect → Identify ONE issue → Adjust prompt → Re-generate → Re-inspect
```

Maximum 3 iterations per variant. If still failing after 3, flag it to the user and suggest an alternative approach.

---

## Step 6: Deliver

### Output Structure

```
output/ad-variants/
├── reference.png              # Copy of the original for comparison
├── variant-01-subtle.png      # Generated variants
├── variant-02-subtle.png
├── variant-03-moderate.png
├── variant-04-moderate.png
├── manifest.json              # Machine-readable manifest
└── manifest.md                # Human-readable summary
```

### Manifest

Generate both `manifest.json` and `manifest.md` documenting:
- Reference ad filename and analysis
- Each variant: filename, divergence level, strategy description, what was preserved, what was changed, prompt used, provider, model, generation parameters
- Platform targeting and sizing
- Timestamp

The manifest is critical — it lets the user (or their team) understand what was tested and reconstruct the logic later.

### Presenting Results

Show the user each variant alongside the reference. For each variant, briefly state:
1. What divergence level it used
2. The 1-line strategy (what it tests)
3. Any notable observations or recommendations

Do NOT over-explain. Let the visuals speak. The user is a media buyer — they know what works when they see it.

---

## Environment & Security

### API Keys

- `OPENAI_API_KEY` — Required for OpenAI provider. Must be set as environment variable.
- `GEMINI_API_KEY` or `GOOGLE_API_KEY` — Required for Google Gemini / Imagen generation. Either works; if both set, `GOOGLE_API_KEY` takes precedence.
- For Google Imagen **editing**: Requires Vertex AI credentials (`GOOGLE_GENAI_USE_VERTEXAI=true` + `GOOGLE_CLOUD_PROJECT` + `GOOGLE_CLOUD_LOCATION`). Without Vertex AI, the CLI auto-falls back to the Gemini backend for edits.
- **Never** ask the user to paste keys in chat. Ask them to set the env var and confirm.
- **Never** log, print, or embed API keys in output files.

### Dependencies

```
openai>=1.0.0          # OpenAI SDK (for OpenAI provider)
google-genai>=1.0.0    # Google GenAI SDK (for Google provider — both Gemini and Imagen)
Pillow>=10.0.0         # Image handling
```

Prefer `uv` for dependency management. If a package is missing, tell the user what to install.

### File Handling

- Use `tmp/ad-variants/` for intermediate files; clean up when done
- Write final outputs to `output/ad-variants/` (or user-specified `--out-dir`)
- Keep filenames stable and descriptive: `variant-01-subtle.png`, not `output_1.png`
- Preserve the reference image in the output directory for side-by-side comparison

---

## Reference Documents

```
references/cli.md                # CLI flags, commands, and recipes
references/variation-strategies.md  # Deep dive on divergence levels with examples
references/platform-specs.md     # Ad specs by platform (sizes, safe zones, guidelines)
references/prompt-patterns.md    # Prompt engineering patterns for ad variants
```

---

## Rules

1. **Always analyze before generating.** Never skip the ad anatomy step.
2. **Always plan before generating.** Present variation specs for user approval.
3. **Preserve what wins.** The whole point is to keep the winning formula intact (at the appropriate divergence level).
4. **One change per iteration.** When fixing a failed variant, change one thing.
5. **Never modify `skills/creative-variants/scripts/ad_variant_gen.py`.** If functionality is missing, flag it.
6. **Respect the divergence level.** Subtle means subtle. Dramatic means dramatic. Don't drift.
7. **Document everything.** Every variant gets a manifest entry. The user's future self will thank you.
8. **Prefer the bundled CLI** over writing one-off scripts.
9. **Don't invent brand elements.** Never add logos, brand names, or taglines the user didn't provide.
10. **When in doubt, ask.** But only if the missing detail truly blocks success. Otherwise, make a reasonable inference and proceed.
