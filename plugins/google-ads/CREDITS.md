# Credits & Attribution

This plugin is built on the shoulders of the open source community. We curate — we don't rebuild.

## MCP Servers
- **@channel47/google-ads-mcp** — [channel47/mcps](https://github.com/channel47/mcps) (MIT)
  Built by Jackson Dean. GAQL-first Google Ads MCP with read/write support. This plugin sets `GOOGLE_ADS_READ_ONLY=true`.

## Companion Tools (referenced, not bundled)
- **claude-ads** by [AgriciDaniel](https://github.com/AgriciDaniel/claude-ads) (652 stars)
  186 cross-platform audit checks (74 Google-specific). We reference it for quarterly deep audits — we don't rebuild it.
- **agencysavvy/pmax** by [AgencySavvy](https://github.com/agencysavvy/pmax) (276 stars)
  PMax reporting script. Complementary to our pmax-decoder skill.
- **feedgen** by [Google Marketing Solutions](https://github.com/google-marketing-solutions/feedgen) (237 stars)
  Shopping feed optimization. Referenced for ecommerce workflows.

## Evaluated Alternatives
- **cohnen/mcp-google-ads** by [cohnen](https://github.com/cohnen/mcp-google-ads) (439 stars)
  Evaluated as our primary MCP candidate. We went with our own for GAQL-first design and read-only enforcement, but cohnen's work informed our tooling decisions.

## Design Influences
- **marketingskills** by [coreyhaines31](https://github.com/coreyhaines31/marketingskills) (10,890 stars)
  Proved the skills-as-markdown-files pattern works at scale.

## Standards
- [SKILL.md open standard](https://skills.sh) — the skill format this plugin uses
- [Model Context Protocol](https://modelcontextprotocol.io) by Anthropic — the MCP specification

If you built something we reference or were inspired by, and we missed you — open an issue. We want to get this right.
