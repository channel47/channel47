# Channel 47

Open-source plugins that replace professions.

## Domain Plugins

Install by professional domain. Each plugin bundles everything needed to replace specific roles.

| Domain | Replaces | Tools | Status |
|--------|----------|-------|--------|
| [Marketing](./plugins/marketing) | Media Buyer, Copywriter | Ads, Gen, Copy | Available |
| [Creative](./plugins/creative) | Graphic Designer | Gen | Available |
| [Operations](./plugins/operations) | Financial Analyst | — | Coming Soon |
| [Research](./plugins/research) | Research Analyst | — | Coming Soon |
| [Content](./plugins/content) | Writer, Editor | — | Coming Soon |

## Quick Start

### Claude Code

```bash
# Add the marketplace
/plugin marketplace add github:channel47/channel47

# Install a domain plugin
/plugin install marketing
```

### Claude Desktop

See individual domain READMEs for `claude_desktop_config.json` configuration.

## Tools

Individual tools are bundled within domain plugins. For direct tool access:

| Tool | Function | Domain(s) |
|------|----------|-----------|
| [Ads](./plugins/tools/ads) | Google Ads management | Marketing |
| [Gen](./plugins/tools/gen) | AI image generation | Marketing, Creative |
| [Copy](./plugins/tools/copy) | Copywriting frameworks | Marketing |

## Project-Level Installation

For best results, install plugins at the **project level**:

```bash
cd my-project
/plugin install marketing@channel47
```

This keeps context focused and manages token usage naturally. Different projects can have different plugins installed.

## Shared Resources

Some tools exist across multiple domains. The Gen tool (AI image generation) serves both Marketing and Creative. When you install both domains, Claude automatically deduplicates—the MCP server loads once, not twice.

## Architecture

See [docs/ARCHITECTURE.md](./docs/ARCHITECTURE.md) for technical details on:

- Domain plugin structure
- Shared resource handling
- Token management
- Versioning strategy

## Development

```bash
# Install dependencies
npm install

# Run site locally
npm run dev

# Build site
npm run build
```

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

## License

MIT
