---
featured: true
draft: false
asciiIcon: |
  ╔═══════════╗
  ║  NANO     ║
  ║  BANANA   ║
  ╚═══════════╝
iconColor: "var(--color-accent-secondary)"
---

## What it does

Generate professional-quality images using Google's latest Gemini image models. Supports both quick iterations with Flash (2-3 seconds) and production-ready 4K output with Pro.

Built for practical use cases: product mockups, visual concepts, social assets, and creative exploration.

## Key Features

- **Dual model support**: Pro tier for 4K quality, Flash tier for fast drafts
- **Smart model selection**: Automatically picks the right model based on your prompt
- **Aspect ratio control**: 16:9, 1:1, 9:16, and more for different use cases
- **Reproducible generation**: Use seed values for consistent results
- **Google Search grounding**: Generate factually accurate images
- **Safety controls**: Four-level filtering (strict to off)
- **Reference image support**: Upload images to guide generation

## Real-world use cases

I use this for:

- Generating product mockups during design discussions
- Creating social media visuals without leaving the terminal
- Quick concept art for creative projects
- Visual prototypes before committing to stock photos
- Iterating on image ideas with seed-based consistency

## What makes it different

Most image generation tools require browser context switching. This plugin works directly in Claude Code. Describe what you want, get an image. Change something, iterate quickly.

The dual-model approach means you don't waste time on slow generation during exploration. Use Flash for quick iterations, switch to Pro when you need the final asset.

## Setup

1. Get your API key from [Google AI Studio](https://aistudio.google.com/apikey)
2. Add to `~/.claude/settings.json`:
```json
{
  "env": {
    "GEMINI_API_KEY": "your-api-key-here"
  }
}
```
3. Install: `/plugin install nano-banana@channel47`
4. Restart Claude Code

## Example workflows

**Quick concept:**

```
"Quick sketch of a robot mascot for a tech startup"
```

Uses Flash model, returns in 2-3 seconds.

**Production asset:**

```
"4K professional product photo of a coffee mug on a wooden table, studio lighting"
```

Uses Pro model, returns high-resolution output.

**Consistent iterations:**

```
"Generate sunset over mountains with seed 42"
```

Then iterate:

```
"Same scene with seed 42 but add a cabin in the foreground"
```

**Specific format:**

```
"Generate a 9:16 mobile wallpaper of an abstract geometric pattern"
```

## Model selection

| Model | Speed | Best For |
|-------|-------|----------|
| Flash | 2-3s | Drafts, concepts, quick iterations |
| Pro | 5-10s | Final assets, product photos, 4K output |

**Auto-triggers Pro:** professional, 4k, high quality, detailed, photorealistic, studio, commercial

**Auto-triggers Flash:** quick, fast, sketch, draft, concept, rough, preview

## Available commands

- Direct prompts work immediately: "Generate an image of..."
- Supports aspect ratios: "16:9 landscape of..."
- Seed-based generation: "...with seed 42"
- Safety levels: "...with moderate safety filtering"
- Reference images: Upload first, then reference in generation

See the [README](https://github.com/ctrlswing/channel47-marketplace/blob/main/plugins/nano-banana/README.md) for full parameter documentation.
