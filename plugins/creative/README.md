# Creative Plugin

Open-source AI plugin that replaces **Graphic Designer** roles.

## Overview

The Creative plugin provides AI-powered visual content creation. Generate professional images, illustrations, and graphics without traditional design software or skills.

## Included Tools

| Tool | Function | MCP Server | Status |
|------|----------|------------|--------|
| **Gen** | AI image generation with Gemini (Nano Banana) | `nano-banana` | Available |
| **Photo Editor** | AI-powered photo editing and manipulation | — | Coming Soon |

## Installation

### Claude Code

```bash
/plugin install creative@channel47
```

Or install from the marketplace:

1. Open Claude Code
2. Run `/plugin marketplace add github:channel47/channel47`
3. Run `/plugin install creative`

### Claude Desktop

Add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "nano-banana": {
      "command": "uvx",
      "args": ["gemini-image-mcp"]
    }
  }
}
```

## Requirements

- Python 3.10+
- Google AI API key (for Gemini access)

## Quick Start

### Product Photography

```
Generate a product photo of wireless earbuds,
floating on gradient background, studio lighting,
professional e-commerce style
```

### Illustration

```
Create an illustration of a cozy coffee shop interior,
warm lighting, watercolor style, inviting atmosphere
```

### Social Media Graphics

```
Generate an Instagram post graphic for a fitness brand,
bold typography, energetic colors, motivational theme
```

## Style Frameworks

The Gen tool includes professional style frameworks:

- **Photography**: Studio, lifestyle, product, editorial
- **Illustration**: Flat, isometric, hand-drawn, vector
- **3D Render**: Product visualization, abstract, architectural
- **Painting**: Digital painting, watercolor, oil
- **Sketch**: Pencil, ink, technical drawing

## Workflows

### Brand Asset Creation

1. Define brand colors, style, and tone
2. Generate logo concepts and variations
3. Create social media templates
4. Produce marketing collateral

### Content Pipeline

1. Brief the visual requirements
2. Generate initial concepts with Gen
3. Iterate on feedback
4. Export final assets

## Tool Documentation

- [Gen - AI Image Generation](../tools/gen/README.md)

## Commands

| Command | Description |
|---------|-------------|
| `/gen:setup` | Configure Gemini API key |

## Project Configuration

For design projects, configure Claude Code at the **project level**:

```bash
cd your-design-project
/plugin install creative@channel47
```

This keeps creative context separate from other work.

## Shared Resources

The **Gen** tool is shared with the Marketing plugin. If you have both installed, Claude deduplicates the `nano-banana` MCP server automatically.

## Roadmap

- [ ] Photo Editor tool for AI-powered editing
- [ ] Vector graphics generation
- [ ] Brand kit management
- [ ] Asset organization and export

## Version

- Plugin: 1.0.0
- Gen Tool: 2.4.1

## License

MIT
