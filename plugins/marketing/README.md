# Marketing Plugin

Open-source AI plugin that replaces **Media Buyer** and **Copywriter** roles.

## Overview

The Marketing plugin bundles all tools needed for modern digital marketing: campaign management, creative generation, and persuasive copywriting. Install once to get a complete AI marketing department.

## Included Tools

| Tool | Function | MCP Server |
|------|----------|------------|
| **Ads** | Google Ads campaign management and GAQL queries | `google-ads` |
| **Gen** | AI image generation with Gemini (Nano Banana) | `nano-banana` |
| **Copy** | Copywriting frameworks (Schwartz, Hemingway, Halbert) | — |

## Installation

### Claude Code

```bash
/plugin install marketing@channel47
```

Or install from the marketplace:

1. Open Claude Code
2. Run `/plugin marketplace add github:channel47/channel47`
3. Run `/plugin install marketing`

### Claude Desktop

Add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "google-ads": {
      "command": "npx",
      "args": ["-y", "@channel47/google-ads-mcp@latest"]
    },
    "nano-banana": {
      "command": "uvx",
      "args": ["gemini-image-mcp"]
    }
  }
}
```

## Requirements

- **Ads**: Node.js 18+, Google Ads API credentials ([setup guide](../tools/ads/GETTING_STARTED.md))
- **Gen**: Python 3.10+, Google AI API key
- **Copy**: No external dependencies

## Quick Start

### Campaign Analysis

```
Analyze my Google Ads campaigns from the last 30 days
and identify top performers and wasted spend
```

### Creative Generation

```
Generate a product photo for a premium coffee brand,
professional studio lighting, white background
```

### Sales Copy

```
Write a landing page headline for a SaaS product
that helps teams collaborate asynchronously
```

## Workflows

### Full-Funnel Campaign Creation

1. **Research**: Analyze competitor ads and identify winning angles
2. **Copy**: Generate headlines, ad copy, and landing page content
3. **Creative**: Create ad images and social media visuals
4. **Deploy**: Set up Google Ads campaigns with negative keywords
5. **Optimize**: Monitor performance and iterate

### A/B Testing Creative

1. Generate multiple image variations with Gen
2. Create corresponding ad copy with Copy
3. Launch as experiments in Google Ads
4. Analyze results and scale winners

## Tool Documentation

- [Ads - Google Ads Management](../tools/ads/README.md)
- [Gen - AI Image Generation](../tools/gen/README.md)
- [Copy - Copywriting Frameworks](../tools/copy/README.md)

## Commands

| Command | Description |
|---------|-------------|
| `/ads:setup` | Configure Google Ads API credentials |
| `/gen:setup` | Configure Gemini API key |
| `/copy:email` | Generate email sequences |
| `/copy:headline` | Generate headlines |
| `/copy:landing-page` | Generate landing page copy |

## Project Configuration

For best results, configure Claude Code at the **project level**:

```bash
cd your-marketing-project
/plugin install marketing@channel47
```

This keeps marketing context separate from other work and manages token usage naturally.

## Shared Resources

The **Gen** tool (AI image generation) is shared with the Creative plugin. If you have both installed, Claude deduplicates the `nano-banana` MCP server automatically—you won't consume extra tokens.

## Version

- Plugin: 1.0.0
- Ads Tool: 4.1.2
- Gen Tool: 2.4.1
- Copy Tool: 2.1.1

## License

MIT
