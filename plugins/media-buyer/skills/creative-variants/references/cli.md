# CLI Reference — ad_variant_gen.py

## Quick Start

```bash
# 4 moderate variants via Google Gemini (default)
python3 skills/creative-variants/scripts/ad_variant_gen.py --reference ad.png --divergence moderate --variants 4

# 6 subtle variants via OpenAI
python3 skills/creative-variants/scripts/ad_variant_gen.py --reference ad.png --provider openai --divergence subtle --variants 6
```

## Flags

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--reference` | path | *required* | Path to the winning ad image (PNG, JPG, WebP) |
| `--divergence` | choice | `moderate` | `subtle`, `moderate`, or `dramatic` |
| `--variants` | int | `4` | Number of variants to generate |
| `--provider` | choice | `google` | `openai` or `google` |
| `--google-backend` | choice | `gemini` | `gemini` (Nano Banana, simple) or `imagen` (Imagen 4 gen + Imagen 3 edit) |
| `--model` | string | auto | Model override (see defaults below) |
| `--platform` | string | none | Target platform for auto-sizing (see table below) |
| `--size` | string | `1024x1024` | OpenAI size. **Only supports:** `1024x1024`, `1536x1024`, `1024x1536`, `auto` |
| `--aspect-ratio` | string | `1:1` | Google aspect ratio. **Only supports:** `1:1`, `4:3`, `3:4`, `16:9`, `9:16` |
| `--quality` | choice | `high` | `low` (fast/cheap), `medium`, `high`, `auto` |
| `--input-fidelity` | choice | `high` | OpenAI only. `high` preserves faces/logos/brand elements; uses more tokens |
| `--output-format` | choice | `png` | `png`, `jpeg` (faster for OpenAI), `webp` |
| `--prompt` | string | auto | Override the generated prompt entirely |
| `--strategy` | string | none | 1-line description of what this batch tests |
| `--preserve` | string | none | Comma-separated elements to keep from original |
| `--change` | string | none | Comma-separated elements to modify |
| `--out-dir` | path | `output/ad-variants/` | Output directory |
| `--out` | path | none | Single-file output path (for 1 variant only) |
| `--dry-run` | flag | off | Print prompts without calling the API |
| `--verbose` | flag | off | Extra debug output |

## Default Models

| Provider + Backend | Model | Notes |
|--------------------|-------|-------|
| OpenAI | `gpt-image-1.5` | Latest (Dec 2025). Best instruction following, face/logo preservation |
| Google Gemini | `gemini-3-pro-image-preview` | Nano Banana Pro. Reasoning-enhanced, better text rendering, no Vertex AI needed |
| Google Imagen (generate) | `imagen-4.0-generate-001` | Also: `imagen-4.0-ultra-generate-001`, `imagen-4.0-fast-generate-001` |
| Google Imagen (edit) | `imagen-3.0-capability-001` | Imagen 4 does NOT support editing. Requires Vertex AI |

## Platform Shortcuts

Maps `--platform` to the closest supported size/ratio per provider.

| `--platform` value | OpenAI size | Google ratio | Use case |
|--------------------|-------------|--------------|----------|
| `facebook-feed` | 1024×1024 | 1:1 | Feed ads |
| `facebook-story` | 1024×1536 | 9:16 | Story ads |
| `instagram-feed` | 1024×1024 | 1:1 | Feed |
| `instagram-story` | 1024×1536 | 9:16 | Stories |
| `google-display` | 1536×1024 | 16:9 | Display Network |
| `google-square` | 1024×1024 | 1:1 | Display square |
| `tiktok` | 1024×1536 | 9:16 | In-feed ads |
| `linkedin-feed` | 1536×1024 | 16:9 | Sponsored content |
| `linkedin-square` | 1024×1024 | 1:1 | Square format |
| `twitter` | 1536×1024 | 16:9 | Promoted posts |
| `pinterest` | 1024×1536 | 3:4 | Promoted pins |

**Note:** OpenAI's GPT Image models only support 3 fixed sizes + `auto`. Arbitrary pixel dimensions like `1080x1080` are **not supported** — the CLI maps platforms to the closest valid size.

## Recipes

### Scale a winner across platforms

```bash
for platform in facebook-feed instagram-story google-display linkedin-feed; do
  python3 skills/creative-variants/scripts/ad_variant_gen.py \
    --reference winner.png \
    --divergence subtle \
    --variants 2 \
    --platform $platform \
    --out-dir output/ad-variants/$platform/
done
```

### Divergence ladder — test all three levels

```bash
for level in subtle moderate dramatic; do
  python3 skills/creative-variants/scripts/ad_variant_gen.py \
    --reference winner.png \
    --divergence $level \
    --variants 3 \
    --out-dir output/ad-variants/$level/
done
```

### Fast/cheap batch with low quality

```bash
python3 skills/creative-variants/scripts/ad_variant_gen.py \
  --reference winner.png \
  --divergence moderate \
  --variants 6 \
  --quality low \
  --output-format jpeg
```

### OpenAI for high-fidelity edits

```bash
python3 skills/creative-variants/scripts/ad_variant_gen.py \
  --reference winner.png \
  --provider openai \
  --divergence moderate \
  --variants 4
```

### Dry run to preview prompts before spending tokens

```bash
python3 skills/creative-variants/scripts/ad_variant_gen.py \
  --reference winner.png \
  --divergence moderate \
  --variants 4 \
  --dry-run
```

### Custom prompt with specific changes

```bash
python3 skills/creative-variants/scripts/ad_variant_gen.py \
  --reference winner.png \
  --divergence moderate \
  --variants 3 \
  --preserve "product shot, logo, CTA text" \
  --change "background from white to warm gradient, add subtle shadow" \
  --strategy "Test warm vs cool backgrounds"
```

## Output

Each run produces:
- `reference.{ext}` — Copy of the original for comparison
- `variant-01-{divergence}.{ext}` through `variant-N-{divergence}.{ext}`
- `manifest.json` — Machine-readable log of all generation parameters
- `manifest.md` — Human-readable summary

## Environment

| Variable | When needed |
|----------|-------------|
| `OPENAI_API_KEY` | `--provider openai` |
| `GEMINI_API_KEY` | `--provider google` (default, either backend) |
| `GOOGLE_API_KEY` | Also works for Google (takes precedence over GEMINI_API_KEY) |
| `GOOGLE_GENAI_USE_VERTEXAI=true` | Required for Imagen editing (`--google-backend imagen` + subtle/moderate) |
| `GOOGLE_CLOUD_PROJECT` | Required with Vertex AI |
| `GOOGLE_CLOUD_LOCATION` | Required with Vertex AI (e.g., `us-central1`) |

Set before running:
```bash
# OpenAI
export OPENAI_API_KEY='sk-...'

# Google (Gemini Developer API — simplest)
export GEMINI_API_KEY='...'

# Google (Vertex AI — needed for Imagen editing)
export GOOGLE_GENAI_USE_VERTEXAI=true
export GOOGLE_CLOUD_PROJECT='your-project'
export GOOGLE_CLOUD_LOCATION='us-central1'
```

## Mode Logic

The CLI automatically selects the API mode based on divergence level:

| Divergence | API Mode | Why |
|------------|----------|-----|
| `subtle` | `edit` | Preserves the reference image structure; makes surface changes |
| `moderate` | `edit` | Uses reference as anchor but allows structural changes |
| `dramatic` | `generate` | Creates from a prompt inspired by the reference; no pixel-level anchoring |

## Provider Considerations

### Google Gemini (`gemini-3-pro-image-preview`) — Default
- **Default provider.** Simplest path — works with just a `GEMINI_API_KEY`, no Vertex AI needed.
- Both generation and editing via `generate_content()` — pass the reference image as input alongside the prompt.
- **Critical:** Must pass `response_modalities=["IMAGE"]` in the config or the model may return text instead of an image.
- **Critical:** `part.inline_data.data` in the Python SDK is already raw bytes (SDK decodes base64 internally). Do NOT `base64.b64decode()` it — that double-decodes and produces ~620 bytes of corrupt garbage that looks like a successful write but isn't a valid image.
- Use `part.as_image().save()` or write `part.inline_data.data` directly.
- Supports `image_config` with `aspect_ratio` for controlling output dimensions.

### OpenAI `gpt-image-1.5`
- Edit mode with `input_fidelity=high` is purpose-built for preserving faces, logos, and brand elements while making targeted changes.
- Supports up to 16 input images per edit (first 5 get highest fidelity on gpt-image-1.5).
- `jpeg` output format is faster than `png` if you don't need transparency.
- Size `auto` lets the model pick the best dimensions based on the prompt.

### Google Imagen (`imagen-4.0-generate-001` + `imagen-3.0-capability-001`)
- Imagen 4 for generation is excellent quality but **does not support editing**.
- Editing falls back to `imagen-3.0-capability-001` which **requires Vertex AI**.
- More complex auth setup. Best for users already on Google Cloud.
- If Vertex AI isn't configured and you request subtle/moderate, the CLI auto-falls back to the Gemini backend.
