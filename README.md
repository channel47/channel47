# Channel 47

Open-source AI tools for media buyers and marketers.

## Plugins

| Plugin | Description | Install |
|--------|-------------|---------|
| [Google Ads Specialist](./plugins/google-ads-specialist) | GAQL queries and campaign management | `npx -y @channel47/google-ads-specialist` |
| [Designer](./plugins/designer) | AI image generation with Gemini | `uvx channel47-designer` |
| [Copywriter](./plugins/copywriter) | Master copywriting frameworks | Claude Code only |
| [Prompt Engineer](./plugins/prompt-engineer) | Optimize prompts for Claude | Claude Code only |

## Installation

### Claude Code

```bash
/plugin marketplace add github:channel47/channel47
/plugin install google-ads-specialist@channel47
```

### Claude Desktop

See individual plugin READMEs for `claude_desktop_config.json` snippets.

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
