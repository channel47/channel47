# Contributing to Channel 47

Thanks for your interest in contributing!

## Ways to Contribute

- **Report bugs** - Open an issue with reproduction steps
- **Suggest features** - Open an issue describing the use case
- **Improve docs** - PRs for typos, clarifications, examples
- **Add skills** - Contribute new skills to existing plugins

## Development Setup

1. Clone the repo: `git clone https://github.com/channel47/channel47.git`
2. Install dependencies: `npm install`
3. Run the site: `npm run dev`

## Plugin Development

Each plugin follows Claude Code plugin structure:

```
plugins/plugin-name/
├── .claude-plugin/plugin.json
├── skills/
├── commands/
├── agents/
└── README.md
```

## Code of Conduct

Be kind. Be helpful. Assume good intent.
