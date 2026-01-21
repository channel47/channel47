# Channel 47 Architecture

This document describes the plugin architecture for Channel 47's domain-based plugin system.

## Overview

Channel 47 organizes AI plugins by **professional domain** rather than individual tools. Each domain plugin bundles related tools, skills, agents, and MCP servers that together can replace specific professional roles.

## Directory Structure

```
plugins/
├── tools/                    # Core tool implementations
│   ├── ads/                  # Google Ads management
│   ├── gen/                  # AI image generation
│   └── copy/                 # Copywriting frameworks
│
├── marketing/                # Domain: Marketing
├── creative/                 # Domain: Creative
├── operations/               # Domain: Operations (coming soon)
├── research/                 # Domain: Research (coming soon)
└── content/                  # Domain: Content (coming soon)
```

## Design Principles

### 1. Domain-First Organization

Users install **domain plugins**, not individual tools. A marketer installs `marketing`, not `ads + gen + copy` separately. This:

- Simplifies discovery and installation
- Provides complete capability sets
- Enables domain-specific workflows and documentation

### 2. Single-Sourced Tools

All tools live in `plugins/tools/`. Domain plugins reference these shared tools. Benefits:

- One source of truth for tool implementations
- Consistent versioning across domains
- Easier maintenance and updates

### 3. Composition Over Duplication

Domain plugins compose tools via:

- **MCP Configuration**: Each domain has its own `.mcp.json` that lists the MCP servers it needs
- **Documentation References**: Domain READMEs link to tool documentation
- **Skills Aggregation**: Domain plugins can reference tool-level skills

### 4. MCP Deduplication

When a user installs multiple domains that share tools (e.g., Marketing and Creative both use Gen), Claude automatically deduplicates MCP servers with the same name. The `nano-banana` server loads once, not twice.

## Domain Plugin Structure

Each domain plugin contains:

```
plugins/{domain}/
├── .claude-plugin/
│   └── plugin.json          # Domain metadata
├── .mcp.json                # Combined MCP servers for this domain
├── README.md                # Domain documentation
└── CHANGELOG.md             # Version history
```

### plugin.json Schema

```json
{
  "name": "marketing",
  "version": "1.0.0",
  "description": "...",
  "domain": {
    "name": "Marketing",
    "professionsReplaced": ["Media Buyer", "Copywriter"],
    "tools": ["ads", "gen", "copy"]
  },
  "mcpServers": "./.mcp.json"
}
```

## Tool Structure

Each tool in `plugins/tools/` follows the existing plugin structure:

```
plugins/tools/{tool}/
├── .claude-plugin/
│   └── plugin.json          # Tool metadata
├── .mcp.json                # MCP server definition (if applicable)
├── agents/                  # Subagent definitions
├── skills/                  # Skill implementations
├── hooks/                   # PreToolUse/PostToolUse hooks
├── commands/                # User-facing commands
├── README.md                # Tool documentation
└── CHANGELOG.md             # Version history
```

## Shared Resources

### MCP Servers

| Server | Package | Used By |
|--------|---------|---------|
| `google-ads` | `@channel47/google-ads-mcp` | Marketing |
| `nano-banana` | `gemini-image-mcp` | Marketing, Creative |

### Deduplication Behavior

When multiple domains use the same MCP server:

1. Each domain's `.mcp.json` lists the server independently
2. Both use the same server name (e.g., `nano-banana`)
3. Claude loads the server once when either domain is installed
4. If both domains are installed, the server is still loaded only once

This is the **recommended approach** per Claude Code best practices—no special handling required.

## Token Management

### Project-Level Installation

Users should install plugins at the **project level**, not globally:

```bash
cd my-marketing-project
/plugin install marketing@channel47
```

This:

- Segments context by use case
- Prevents token bloat from unused tools
- Matches Claude's project-based workflow

### Token Footprint

Each tool has been optimized for minimal token consumption:

| Tool | Token Footprint |
|------|-----------------|
| Ads | ~450 tokens |
| Gen | ~300 tokens |
| Copy | ~200 tokens |

Domain plugins don't add significant overhead—they primarily aggregate existing tools.

## Versioning Strategy

### Independent Versioning

- **Tools** have independent versions (e.g., `ads@4.1.2`)
- **Domains** have independent versions (e.g., `marketing@1.0.0`)
- Domain versions increment when:
  - New tools are added
  - Domain-level documentation changes
  - Domain-specific features are added

### Version Sync

When a shared tool updates (e.g., `gen@2.5.0`), the domain versions don't automatically increment. Users get the latest tool version when they update the domain plugin.

### Update Requirements (per CLAUDE.md)

When modifying tools, update versions in:

1. `plugins/tools/{tool}/.claude-plugin/plugin.json`
2. `plugins/tools/{tool}/package.json` (if applicable)
3. `.claude-plugin/marketplace.json`
4. `plugins/tools/{tool}/CHANGELOG.md`

## Migration Path

### Existing Users

Users with individual tool plugins (e.g., `ads`, `gen`, `copy`) can:

1. **Keep current setup**: Individual tools still work
2. **Migrate to domains**: Uninstall individual tools, install domain plugin

### Recommended Migration

```bash
# Remove individual plugins
/plugin uninstall ads
/plugin uninstall gen
/plugin uninstall copy

# Install domain plugin
/plugin install marketing@channel47
```

## Future Considerations

### Cross-Domain Dependencies

If a tool legitimately belongs to multiple domains:

1. Tool lives in `plugins/tools/`
2. Each relevant domain lists it in `plugin.json`
3. MCP deduplication handles the rest

### Domain Expansion

New domains (Operations, Research, Content) will follow the same pattern:

1. Create domain plugin structure
2. Implement or integrate tools in `plugins/tools/`
3. Update `marketplace.json`

### Tool Extraction

If a shared tool becomes complex enough to warrant its own package:

1. Keep tool in `plugins/tools/` for source
2. Publish MCP server separately (like `@channel47/google-ads-mcp`)
3. Domain plugins reference the published package
