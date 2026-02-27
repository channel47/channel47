# Channel 47 Ecosystem

AI skills registry for Claude Code, Claude Cowork, and Codex. Houses skills (SKILL.md open standard), MCP servers, CLI tools, subagents, and full plugins.

## Structure

```
.claude-plugin/marketplace.json   # Plugin registry (channel47 marketplace)
plugins/
  media-buyer/                    # Google Ads + Bing Ads paid-search toolkit (v6.1.2)
```

## Vision

**Current state:** One profession plugin (media-buyer v6.1.2). Marketing/media buying tools focus.

**Direction:** Browsable, categorized registry. Community contributions. General-purpose AI skills marketplace eventually.

**Model:** 21st.dev — community content is the SEO/discovery magnet. Commercial products (starting with Paid Briefs) generate revenue.

## Commands

**Plugin install** (from any Claude Code session):
```
/plugin marketplace add channel47/plugins
/plugin install media-buyer@channel47
```

## Plugin Development

Plugins live in `plugins/`. Each plugin has a `.claude-plugin/plugin.json` manifest. The marketplace registry at `.claude-plugin/marketplace.json` indexes all available plugins.

Future contributions aren't limited to full plugins — individual skills (SKILL.md), MCP server configs, CLI tools, and subagents are all first-class registry items.

## Gotchas

- **MCP servers moved** — MCP servers now live in their own repo: [channel47/mcps](https://github.com/channel47/mcps)
- **Strategy docs moved** — positioning brief and product marketing context now live in `../site/.claude/`, not here.
- **No `docs/` directory** — despite older references, strategy docs are consolidated in the site repo.
