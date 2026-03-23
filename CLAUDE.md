# channel47 Plugins

Open-source Claude plugins for DTC media buyers.

## Structure

```
plugins/
  _archived/                        # All archived plugins
    dtc-google-ads-playbook/        # Google Ads playbook for DTC brands
    dtc-research-engine/            # Customer research → ad creative pipeline
    google-ads/                     # Old MCP-connected Google Ads plugin
    microsoft-ads/                  # Old MCP-connected Microsoft Ads plugin
    meta-ads/                       # Old MCP-connected Meta Ads plugin
    paid-search/                    # Deprecated combined Google + Bing plugin
    frontend-craft/                 # Design/UI plugin, not part of DTC suite
docs/                               # Planning and research docs (historical)
```

No active plugins at this time.

## Design Philosophy

1. **DTC-specific depth over horizontal breadth.** Every skill, command, and agent is built for DTC media buyers running Google Ads.
2. **No external dependencies.** No MCP servers, no API keys, no environment variables. Install and use immediately.
3. **Built from real accounts.** Frameworks come from a $6M+ Google Ads account, not theory.
4. **Structured pipelines.** The research engine is a 5-stage pipeline: research → personas → angles → scripts → copy. Each stage feeds the next.

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
- **No MCP servers needed** — The new plugins don't connect to ad platform APIs. The research engine uses WebSearch/WebFetch (built into Claude). The playbook is pure knowledge.
- **Plugin author is channel47** — Use "channel47" as the brand across both plugins. Individual plugin.json files may reference "Leadcap Digital" or "Four AM Media" as the author org — update these to "channel47" for consistency.
