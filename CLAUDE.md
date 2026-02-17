# Channel 47 Ecosystem

Plugin marketplace and brand skills for Claude Code.

## Structure

```
.claude-plugin/marketplace.json   # Plugin registry (channel47 marketplace)
plugins/
  media-buyer/                    # Google Ads + Bing Ads paid-search toolkit (v6.0.0)
skills/                           # Brand .skill files
```

## Commands

**Plugin install** (from any Claude Code session):
```
/plugin marketplace add channel47/channel47
/plugin install media-buyer@channel47
```

## Plugin Development

Plugins live in `plugins/`. Each plugin has a `.claude-plugin/plugin.json` manifest. The marketplace registry at `.claude-plugin/marketplace.json` indexes all available plugins.

## Gotchas

- **MCP servers moved** — MCP servers now live in their own repo: [channel47/mcps](https://github.com/channel47/mcps)
- **Strategy docs moved** — positioning brief and product marketing context now live in `../site/.claude/`, not here.
- **No `docs/` directory** — despite older references, strategy docs are consolidated in the site repo.
