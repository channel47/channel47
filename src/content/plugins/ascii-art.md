---
featured: false
draft: false
---

## What it does

Generate ASCII art logos, banners, diagrams, and decorative text for CLI tools and documentation. Inspired by CLI agents like Claude Code and Gemini CLI that use ASCII art to create memorable brand experiences.

## Key Features

- **Logo generation**: Create large ASCII text logos in various font styles (block, slant, banner, small)
- **Decorative banners**: Build customizable banners with multiple border styles
- **ASCII boxes**: Wrap content in boxes with optional titles
- **Diagrams**: Generate flowcharts, trees, tables, and architecture diagrams
- **Freeform art**: Create ASCII art from text descriptions
- **Text effects**: Apply shadow, 3D, outline, gradient, rainbow, neon, and glitch effects
- **ANSI colors**: Full color support with gradients like sunset, ocean, and matrix

## Real-world use cases

I use this for:

- Creating splash screens for CLI tools that leave a lasting impression
- Adding visual structure to documentation with boxes and banners
- Making README headers stand out with ASCII logos
- Visualizing architecture and data flows in plain text
- Adding personality to terminal output

## What makes it different

Most ASCII generators are web tools or standalone scripts. This plugin works directly in Claude Code, so you can generate and iterate on designs without leaving your workflow. Each skill is focused on a specific use case with sensible defaults and extensive customization options.

## Setup

1. Install: `/plugin install ascii-art@channel47`
2. Try it immediately with `/generate-logo "YOUR TEXT"`

## Example workflows

**Create a startup logo:**

```
/generate-logo "ACME" --style block
```

```
 █████╗  ██████╗███╗   ███╗███████╗
██╔══██╗██╔════╝████╗ ████║██╔════╝
███████║██║     ██╔████╔██║█████╗
██╔══██║██║     ██║╚██╔╝██║██╔══╝
██║  ██║╚██████╗██║ ╚═╝ ██║███████╗
╚═╝  ╚═╝ ╚═════╝╚═╝     ╚═╝╚══════╝
```

**Add a welcome banner:**

```
/generate-banner "Welcome to My CLI" --style rounded
```

```
╭─────────────────────────────────╮
│      Welcome to My CLI          │
╰─────────────────────────────────╯
```

**Visualize a flow:**

```
/generate-diagram "User clicks -> API validates -> Database saves" --type flowchart
```

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│    User     │────▶│     API     │────▶│  Database   │
│   clicks    │     │  validates  │     │    saves    │
└─────────────┘     └─────────────┘     └─────────────┘
```

## Available skills

- `/generate-logo` - Create large ASCII text logos in various font styles
- `/generate-banner` - Create decorative banners with customizable borders
- `/generate-box` - Wrap content in ASCII boxes with optional titles
- `/generate-diagram` - Create flowcharts, trees, tables, and architecture diagrams
- `/generate-art` - Generate freeform ASCII art from descriptions
- `/text-effects` - Apply shadow, 3D, outline, and other effects to text

See the [Getting Started Guide](https://github.com/ctrlswing/channel47-marketplace/blob/main/plugins/ascii-art/GETTING_STARTED.md) for detailed usage and customization options.
