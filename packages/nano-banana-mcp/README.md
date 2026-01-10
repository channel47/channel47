# nano-banana-mcp

MCP server for AI-powered image generation using Google's Gemini models.

## Features

- **Dual Model Support**: Flash (2-3s, 1024px) and Pro (4K quality)
- **Smart Model Selection**: Auto-selects based on prompt keywords
- **Aspect Ratio Control**: 1:1, 16:9, 9:16, 21:9, 4:3, 3:4, 2:1
- **Google Search Grounding**: Factually accurate images (Pro only)
- **File Management**: Upload, list, and delete files via Gemini Files API
- **Reproducible Generation**: Seed support for consistent results

## Installation

### Via uvx (Recommended)

No installation needed - runs directly:

```bash
uvx nano-banana-mcp
```

### Via pip

```bash
pip install nano-banana-mcp
```

### Via pipx

```bash
pipx install nano-banana-mcp
```

## Configuration

### Environment Variable

Get your free API key from [Google AI Studio](https://aistudio.google.com/apikey).

```bash
export GEMINI_API_KEY="your-api-key-here"
```

### Claude Code Integration

Add to your `.mcp.json`:

```json
{
  "mcpServers": {
    "nano-banana": {
      "command": "uvx",
      "args": ["nano-banana-mcp"]
    }
  }
}
```

Or configure in `~/.claude/settings.json`:

```json
{
  "env": {
    "GEMINI_API_KEY": "your-api-key-here"
  }
}
```

## Tools

### generate_image

Generate images with automatic model selection.

```
mcp__nano-banana__generate_image
```

Parameters:
- `prompt` (required): Image description
- `model_tier`: "flash", "pro", or "auto" (default: auto)
- `aspect_ratio`: "1:1", "16:9", "9:16", etc. (default: 1:1)
- `thinking_level`: "LOW" or "HIGH" (Pro only)
- `use_grounding`: Enable Google Search grounding (Pro only)
- `safety_level`: "STRICT", "MODERATE", "PERMISSIVE", "OFF"
- `seed`: Integer for reproducible results
- `output_path`: File path to save image

### list_files

List uploaded files.

```
mcp__nano-banana__list_files
```

### upload_file

Upload a file for use as reference.

```
mcp__nano-banana__upload_file
```

### delete_file

Delete an uploaded file.

```
mcp__nano-banana__delete_file
```

## Model Selection

**Pro model** auto-selects for prompts containing:
- professional, 4k, high quality, detailed, photorealistic
- ultra, premium, studio, commercial, product photo

**Flash model** auto-selects for prompts containing:
- quick, fast, sketch, draft, concept, rough
- preview, test, iterate, simple, basic

## Development

```bash
# Clone and setup
cd packages/nano-banana-mcp
uv venv && source .venv/bin/activate
uv pip install -e ".[dev]"

# Run tests
pytest tests/ -v

# Format code
ruff format src/ tests/
ruff check src/ tests/
```

## License

MIT
