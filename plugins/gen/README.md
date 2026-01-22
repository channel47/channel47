# Image Generation Plugin

AI image generation via Nano Banana MCP server (Gemini).

## Setup

1. Get your API key from [Google AI Studio](https://aistudio.google.com/apikey)
2. Add to `~/.claude/settings.json`:

```json
{
  "env": {
    "GEMINI_API_KEY": "your-api-key"
  }
}
```

3. Restart Claude Code

## MCP Tools

- `mcp__nano-banana__generate_image` - Generate images from text prompts
- `mcp__nano-banana__list_files` - List uploaded files
- `mcp__nano-banana__upload_file` - Upload reference images

## Usage

```
"Generate an image of a sunset over mountains"
```

## License

MIT
