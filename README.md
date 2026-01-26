# Channel 47

Claude Code plugin marketplace for Google Ads.

## Plugins

| Plugin | Description | Install |
|--------|-------------|---------|
| [ads](./plugins/ads) | Google Ads campaign creation and optimization with PMax, Search, Audit, and Assets skills plus research agents | `/plugin install ads@channel47` |

## Installation

### Claude Code

```bash
# Add the marketplace
/plugin marketplace add github:channel47/channel47

# Install the ads plugin
/plugin install ads@channel47
```

### Claude Desktop (MCP servers only)

For the `ads` plugin MCP servers:
```json
{
  "mcpServers": {
    "google-ads": {
      "command": "npx",
      "args": ["-y", "@channel47/google-ads-mcp"]
    },
    "dataforseo": {
      "command": "npx",
      "args": ["-y", "@channel47/dataforseo-mcp-server"]
    }
  }
}
```

See the [ads plugin README](./plugins/ads/README.md) for environment variable configuration and full MCP server list.

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
