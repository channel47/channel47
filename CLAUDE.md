# channel47 Plugins

Open-source role-based Claude Code plugins.

## Structure

```
plugins/
  media-buyer/                      # Paid ads management across Google, Bing, Meta
  frontend-designer/                # Design, build, review, and polish web UIs
  creative-strategist/              # Customer research → personas → angles
  _archived/                        # All archived plugins
    dtc-google-ads-playbook/        # Google Ads playbook for DTC brands
    dtc-research-engine/            # Customer research → ad creative pipeline
    google-ads/                     # Old MCP-connected Google Ads plugin
    microsoft-ads/                  # Old MCP-connected Microsoft Ads plugin
    meta-ads/                       # Old MCP-connected Meta Ads plugin
    paid-search/                    # Deprecated combined Google + Bing plugin
    frontend-craft/                 # Predecessor to frontend-designer
docs/                               # Planning and research docs (historical)
```

## Design Philosophy

1. **Role-based architecture.** Each plugin maps to a professional role (media-buyer, frontend-designer, etc.) rather than a specific tool or workflow.
2. **Built from real work.** Frameworks come from production accounts and projects, not theory.
3. **Plugin author is channel47** — Use "channel47" as the brand across all plugins.

## Plugin Development

Each plugin follows this structure:
```
[plugin-name]/
├── .claude-plugin/plugin.json     # Manifest (name, version, description, author, keywords)
├── skills/                        # SKILL.md files — auto-activate on relevant conversations
│   └── [skill-name]/
│       ├── SKILL.md               # Skill definition with frontmatter
│       └── references/            # Supporting reference material
├── commands/                      # Slash commands — user-invoked
├── agents/                        # Subagents for complex tasks
└── README.md                      # User-facing documentation
```

## Key Files

- `../.claude/product-marketing-context.md` — CH47 brand positioning (if it exists). Read before writing any copy.

## Skill Description Guidelines

- Descriptions should be ~60-80 words.
- Use third-person: "This skill should be used when the user asks..."
- End with "or mentions [category terms]..." catch-all clause.
- Include casual, question, and pain-point trigger phrases.

## Frontmatter Field Names

- **Skills** (`SKILL.md`): use `allowed-tools:` for tool access (if needed)
- **Agents** (`agents/*.md`): use `tools:` for tool access
- **Commands** (`commands/*.md`): use `allowed-tools:` for tool access

## Gotchas

- **References are per-skill** — Each skill can have a `references/` subdirectory with supporting material.
- **Some plugins use MCP servers** — media-buyer connects to ad platform MCP servers (google-ads, bing-ads, meta-ads). frontend-designer is pure knowledge, no external dependencies.
- **Plugin author is channel47** — Use "channel47" as the brand across all plugins.
