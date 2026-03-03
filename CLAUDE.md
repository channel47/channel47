# Channel 47 Ecosystem

AI skills registry for Claude Code, Claude Cowork, and Codex. Houses skills (SKILL.md open standard), MCP servers, CLI tools, subagents, and full plugins.

## Structure

```
.claude-plugin/marketplace.json   # Plugin registry (channel47 marketplace)
plugins/
  paid-search/                    # Google Ads + Bing Ads paid search toolkit (v7.0.0)
  meta-ads/                       # Meta Ads (Facebook + Instagram) toolkit — skeleton (v0.1.0)
```

## Vision

Marketing-focused plugin registry (paid-search v7.0.0 live, meta-ads v0.1.0 skeleton). Growing toward browsable marketplace — 21st.dev model.

## Commands

**Plugin install** (from any Claude Code session):
```
/plugin marketplace add channel47/plugins
/plugin install paid-search@channel47
```

## Plugin Development

Plugins live in `plugins/`. Each plugin has a `.claude-plugin/plugin.json` manifest. The marketplace registry at `.claude-plugin/marketplace.json` indexes all available plugins. To develop a plugin, work inside its directory (e.g., `plugins/paid-search/`). Each plugin has its own CLAUDE.md with specific commands. Use `/plugin-dev:plugin-validator` to validate structure before committing.

Future contributions aren't limited to full plugins — individual skills (SKILL.md), MCP server configs, CLI tools, and subagents are all first-class registry items.

## Gotchas

- **MCP servers moved** — MCP servers now live in their own repo: [channel47/mcps](https://github.com/channel47/mcps)
- **Strategy docs moved** — positioning brief and product marketing context now live in `../site/.claude/`, not here.
- **No `docs/` directory** — despite older references, strategy docs are consolidated in the site repo.
