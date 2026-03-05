# Credits & Attribution — Channel 47 Plugin Suite

The channel47 paid media plugin suite is built on the shoulders of the open source community. We curate the best tools and build the workflow intelligence layer on top.

## MCP Servers (bundled)

| Plugin | MCP Server | Author | License |
|--------|-----------|--------|---------|
| google-ads | @channel47/google-ads-mcp | Jackson Dean | MIT |
| microsoft-ads | @channel47/bing-ads-mcp | Jackson Dean | MIT |
| meta-ads | meta-ads-mcp (brijr/meta-mcp) | brijr | MIT |

## MCP Servers (evaluated)

| MCP Server | Stars | Why we didn't use it | Notes |
|-----------|------:|---------------------|-------|
| cohnen/mcp-google-ads | 439 | We needed GAQL-first design + read-only enforcement | Excellent implementation, informed our decisions |
| pipeboard-co/meta-ads-mcp | 563 | Remote SSE architecture — we needed local stdio | Documented as alternative for remote setups |
| Duartemartins/microsoft-ads-mcp-server | — | Python/FastMCP — we went Node.js for consistency | Good reference implementation |

## Companion Tools (referenced, not bundled)

| Tool | Stars | What it does | How we use it |
|------|------:|-------------|---------------|
| claude-ads (AgriciDaniel) | 652 | 186 cross-platform audit checks | Quarterly deep audits — we reference, don't rebuild |
| agencysavvy/pmax | 276 | PMax reporting script | Complementary to pmax-decoder |
| feedgen (Google Marketing Solutions) | 237 | Shopping feed optimization | Referenced for ecommerce workflows |
| meta-ads-analyzer (mathiaschu) | 215 | Breakdown Effect analysis | Inspired placement bleed detection |
| facebook-ads-library-mcp (trypeggy) | — | Meta Ad Library access | Optional companion for competitor research |

## Design Influences

| Project | Stars | Influence |
|---------|------:|----------|
| marketingskills (coreyhaines31) | 10,890 | Proved skills-as-markdown works at scale |
| talknerdytome-labs/claude-agents | — | Multi-competitor benchmarking agent pattern |

## Standards

- [SKILL.md open standard](https://skills.sh) — the skill format all plugins use
- [Model Context Protocol](https://modelcontextprotocol.io) by Anthropic — the MCP specification
- [Claude Code Plugins](https://docs.anthropic.com/en/docs/claude-code/plugins) — the plugin architecture

## Philosophy

We curate — we don't rebuild. The paid media ecosystem has excellent open-source MCPs. Our value is the workflow intelligence layer: skills that turn API access into prioritized, dollar-quantified action plans with UI paths and copy-paste artifacts. Every MCP we bundle and every tool we reference deserves credit for making this possible.

If you built something we reference or were inspired by, and we missed you — open an issue. We want to get this right.
