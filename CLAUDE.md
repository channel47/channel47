# channel47 Plugins

Open-source Claude plugins for paid media. One plugin per ad platform. Read-only by design — the plugins read account data and produce prioritized, dollar-quantified action plans. They cannot modify accounts.

## Structure

```
.claude-plugin/marketplace.json   # Plugin registry (derived — run sync.sh to regenerate)
validate.sh                       # Structural validator (7 check categories)
sync.sh                           # Regenerate marketplace.json from plugin.json files
commands/                         # Repo-level slash commands (/validate, /sync, /check-versions)
product-marketing-context.md      # Product positioning, audience, competitive landscape
CREDITS.md                        # Suite-level open source attribution
.github/workflows/validate.yml    # CI: validate + sync-check on push/PR
plugins/
  google-ads/                     # Google Ads (v1.0.0) — 9 skills, read-only
  microsoft-ads/                  # Microsoft Advertising (v1.0.0) — 8 skills, read-only
  meta-ads/                       # Meta Ads (v1.0.0) — 9 skills, 2 agents, read-only
  paid-search/                    # [DEPRECATED] Google + Bing combined (v7.0.0) — frozen
  frontend-craft/                 # Design/UI plugin — not part of paid media suite
docs/
  plans/plugin-suite-design.md    # Plugin suite architecture map (8 platforms, MCP selections)
```

## Plugin Overview

| Plugin | Platform | Skills | MCP Server | Status |
|--------|----------|-------:|-----------|--------|
| google-ads | Google Ads | 9 | @channel47/google-ads-mcp (READ_ONLY=true) | Active |
| microsoft-ads | Microsoft Advertising | 8 | @channel47/bing-ads-mcp | Active |
| meta-ads | Facebook + Instagram | 9 | meta-ads-mcp (brijr/meta-mcp) | Active |
| paid-search | Google + Bing | 6 | Both MCPs | Deprecated — use google-ads + microsoft-ads |

## Design Philosophy

1. **Curate, don't rebuild.** Bundle the best existing open-source MCP servers. Build only the workflow intelligence layer (skills).
2. **Read-only by design.** No mutations. Skills produce action plans with dollar impact, UI paths, and copy-paste artifacts.
3. **One plugin per platform.** Google, Bing, and Meta are separate. Each plugin stands alone.
4. **Specificity over automation.** Compensate for no write access with extreme output specificity — dollar tables, exact UI navigation paths, copy-paste negative keyword lists.

## Plugin Development

Plugins live in `plugins/`. Each plugin has a `.claude-plugin/plugin.json` manifest. The marketplace registry at `.claude-plugin/marketplace.json` indexes all available plugins.

Every plugin follows this structure:
```
[platform]-ads/
├── .claude-plugin/plugin.json     # Manifest
├── .mcp.json                      # Curated MCP server(s), pinned versions
├── CREDITS.md                     # Open source attribution
├── commands/                      # Orchestrator entry point (/google-ads, etc.)
├── skills/                        # SKILL.md workflow files
├── agents/                        # Subagents for parallel execution
├── hooks/                         # inject-profile.sh, preserve-profile.sh, update-profile.py
└── references/                    # Query templates, thresholds, benchmarks, ui-paths
```

Plugin component counts:
- google-ads: 9 skills, 2 agents (waste-scanner, search-term-classifier)
- microsoft-ads: 8 skills, 2 agents (import-checker, placement-scanner)
- meta-ads: 9 skills, 2 agents (creative-analyst, competitor-scout)

Use `/plugin-dev:plugin-validator` to validate structure before committing.

## Validation & Maintenance

Three tools keep the plugin suite consistent:

| Tool | Command | Purpose |
|------|---------|---------|
| **Validate** | `bash validate.sh` or `/validate` | Structural consistency, cross-file references, spec compliance |
| **Sync** | `bash sync.sh` or `/sync` | Regenerate marketplace.json from plugin.json (source of truth) |
| **Check Versions** | `/check-versions` | Compare pinned MCP versions against npm latest |

CI runs both validate + sync-check on every push/PR that touches plugin files (`.github/workflows/validate.yml`).

### What validate checks (7 categories)

1. Marketplace registry sync (entries, versions, directories)
2. Required files per plugin (plugin.json, .mcp.json, hooks.json, README, LICENSE)
3. Skill frontmatter (name matches dir, description 60-80 words, allowed-tools, no mutations)
4. Agent frontmatter (`tools:` not `allowed-tools:`, Output Schema + Fallback sections)
5. Hook validity (valid events, referenced scripts exist)
6. Cross-file references (skills/agents -> references/ files exist)
7. Cross-plugin consistency (shared skills everywhere, hook structure uniform)

### Source of truth

- `plugin.json` is authoritative for `name`, `version`, `description`.
- `marketplace.json` is authoritative for `category`, `tags`, `replacedBy` (fields not in plugin.json).
- Run `bash sync.sh` to pull plugin.json fields into marketplace.json while preserving marketplace-only fields.

## Key Files

- `product-marketing-context.md` — Product positioning, target audience, competitive landscape, brand voice. Read before writing any copy or making strategic decisions.
- `docs/plans/plugin-suite-design.md` — Full architecture map: 8 platform plugins, MCP selections, workflow→tool mapping, build order, resolved decisions.
- `CREDITS.md` — Suite-level open source attribution covering all evaluated MCPs, companion tools, and design influences.

## Skill Description Guidelines

- Descriptions should be ~60-80 words. Over 85 is too long (metadata is always in context, ~2% budget).
- Use third-person: "This skill should be used when the user asks..."
- End with "or mentions [category terms]..." catch-all clause for broad matching.
- Avoid near-synonym trigger phrases ("find waste", "find wasted spend", "find the waste" — pick one).
- Include casual, question, abbreviation, and pain-point trigger phrases for diversity.

## Frontmatter Field Names

- **Skills** (`SKILL.md`): use `allowed-tools:` for tool access
- **Agents** (`agents/*.md`): use `tools:` for tool access — NOT `allowed-tools:`

## Gotchas

- **References are plugin-level, not per-skill** — Consolidated reference files live in `[plugin]/references/`. Don't create per-skill `references/` directories (except `platform-setup/references/` which has setup-specific files). Skills cross-reference the shared pool.
- **Porting skills across platforms** — When splitting paid-search skills into platform-specific plugins: remove the other platform's tool calls from `allowed-tools`, remove platform detection logic, replace mutation flows with action plans (dollar tables + UI paths + copy-paste artifacts).
- **Bing data quirks** — Spend is in dollars (no micros conversion). CTR comes as percentage string (parse before math). No change event history, no impression share in standard reports, no ad disapproval data via API.
- **Meta MCP (brijr/meta-mcp)** — 44 tools, single env var (`META_ACCESS_TOKEN`), local stdio via `npx meta-ads-mcp@^1.7.0`.
- **MCP servers are separate** — MCP servers live in their own repo: [channel47/mcps](https://github.com/channel47/mcps). Plugins reference MCPs via `.mcp.json`. Meta uses a third-party MCP (brijr/meta-mcp).
- **Read-only is a hard constraint** — No mutations in any plugin. Don't add `mutate` tools to `allowed-tools`. Skills produce action plans, not API calls that change accounts.
- **No PreToolUse mutation hooks** — Since plugins are read-only, there are no mutation validation hooks. Hooks: SessionStart (inject profile), PreCompact (preserve profile), Stop (update profile).
- **PreCompact hook is valid** — Confirmed as one of 21 official Claude Code hook events. Fires before manual `/compact` or automatic compaction. All 3 paid media plugins use it to preserve account profile context through compaction.
- **paid-search is deprecated** — Still functional but frozen. Use `google-ads` and `microsoft-ads` instead. See `paid-search/DEPRECATED.md` for migration guide.
- **frontend-craft is not part of the paid media suite** — It exists in the registry but is not marketed on channel47.dev.
- **PMC lives here** — `product-marketing-context.md` is at this repo root. The site-level PMC covers the Ch47 brand broadly; this one covers the plugin suite specifically.
- **Shared Google Ads developer token** — google-ads plugin and PaidBrief share the same developer token (Basic Access, 15K ops/day). Monitor combined usage.
