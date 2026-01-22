# Channel 47

Claude Code plugin marketplace for Google Ads and AI image generation.

## Plugins

| Plugin | Description | Install |
|--------|-------------|---------|
| [ads](./plugins/ads) | Google Ads MCP server with setup wizard and mutation hooks | `/plugin install ads@channel47` |
| [gen](./plugins/gen) | AI image generation via Nano Banana MCP server | `/plugin install gen@channel47` |

## Installation

### Claude Code

```bash
# Add the marketplace
/plugin marketplace add github:channel47/channel47

# Install individual plugins
/plugin install ads@channel47
/plugin install gen@channel47
```

### Claude Desktop (MCP servers only)

For the `ads` plugin MCP server:
```json
{
  "mcpServers": {
    "google-ads": {
      "command": "npx",
      "args": ["-y", "@channel47/google-ads-mcp"]
    }
  }
}
```

For the `gen` plugin MCP server:
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

See individual plugin READMEs for environment variable configuration.

## Development

```bash
# Install dependencies
npm install

# Run site locally
npm run dev

# Build site
npm run build
```

## License

MIT
