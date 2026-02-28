# Plugin Restructure: Platform-Specific Plugins

**Date:** 2026-02-27
**Status:** Approved
**Approach:** A — Platform-Native, Self-Contained Plugins

## Summary

Restructure the monolithic `media-buyer` plugin into granular, platform-specific plugins. Each plugin is fully self-contained with its own MCP servers, hooks, and skills. No cross-plugin dependencies.

## Plugins

| Plugin | Platforms | MCP Servers | Status |
|--------|-----------|-------------|--------|
| `paid-search` | Google Ads, Bing Ads | `@channel47/google-ads-mcp`, `@channel47/bing-ads-mcp` | Refactor from media-buyer |
| `meta-ads` | Facebook, Instagram | `@channel47/meta-ads-mcp` (future) | Skeleton only |

## Plugin Boundaries

- **paid-search**: Keyword-intent advertising. Search campaigns, Shopping, PMax. Everything where the user has search intent.
- **meta-ads**: Demand generation. Creative-driven, audience-driven, algorithmic optimization.

## Skill Design

### Universal Skills (present in both plugins, platform-specific implementations)

| Skill | Shared Pattern | Output Contract |
|-------|---------------|-----------------|
| `platform-setup` | Credential verification → account listing → summary | Same flow, platform-specific auth |
| `morning-brief` | Prioritized narrative: Urgent / Watch / Healthy with $ impact | Same severity model, platform-specific metrics |
| `waste-detector` | Severity-tagged waste items (HIGH/MED/LOW/INFO) with remediation | Same severity scale, platform-specific waste types |

### paid-search Skills

| Skill | Status | Notes |
|-------|--------|-------|
| `platform-setup` | Existing — metadata update only | Google + Bing credential setup |
| `morning-brief` | Existing — metadata update only | Search-specific metrics and anomaly formulas |
| `waste-detector` | Existing — metadata update only | QS, match types, Display expansion waste |
| `search-term-verdict` | Existing — metadata update only | Search-only skill |
| `pmax-decoder` | Existing — metadata update only | Google-only, search-adjacent |

### meta-ads Skills

| Skill | Status | Notes |
|-------|--------|-------|
| `platform-setup` | Skeleton | Meta Business Manager, pixel, CAPI |
| `morning-brief` | Skeleton | CPM, frequency, relevance score, creative fatigue |
| `waste-detector` | Skeleton | Audience overlap, creative fatigue, placement bleed, frequency |
| `creative-analyzer` | Skeleton | No search equivalent. Hook rate, hold rate, thumb-stop ratio |
| `audience-builder` | Skeleton | No search equivalent. Lookalikes, custom audiences, exclusions |

## Hooks & Safety

Same mutation guard pattern across both plugins:

1. Query & analyze (no side effects)
2. Preview mutations (dry_run: true)
3. PreToolUse hook fires on live mutation, alerts user
4. User approves → execute

Each plugin has its own `hooks/hooks.json` + `validate-mutations.py` matching its platform's MCP mutate tool.

## Directory Structure

```
plugins/plugins/
├── paid-search/
│   ├── .claude-plugin/plugin.json
│   ├── .mcp.json                    ← google-ads + bing-ads
│   ├── hooks/hooks.json + validate-mutations.py
│   ├── skills/
│   │   ├── platform-setup/
│   │   ├── morning-brief/
│   │   ├── waste-detector/
│   │   ├── search-term-verdict/
│   │   └── pmax-decoder/
│   ├── README.md
│   └── LICENSE
│
└── meta-ads/
    ├── .claude-plugin/plugin.json
    ├── .mcp.json                    ← meta-ads MCP (placeholder)
    ├── hooks/hooks.json + validate-mutations.py
    ├── skills/
    │   ├── platform-setup/
    │   ├── morning-brief/
    │   ├── waste-detector/
    │   ├── creative-analyzer/
    │   └── audience-builder/
    ├── README.md
    └── LICENSE
```

## Build Sequence

### Phase 1: Refactor paid-search
1. Rename `media-buyer/` → `paid-search/`
2. Update plugin.json (name, description, keywords)
3. Update all SKILL.md descriptions to say "paid search" not "media buyer"
4. Update README
5. Remove `image-gen/` stub
6. Clean up tests

### Phase 2: Scaffold meta-ads
1. Create directory structure matching paid-search pattern
2. Write plugin.json manifest
3. Stub `.mcp.json` with placeholder for `@channel47/meta-ads-mcp`
4. Write SKILL.md frontmatter + skeleton instructions for all 5 skills
5. Copy and adapt hooks from paid-search (match `mcp__meta-ads__mutate`)
6. Write README
7. Add LICENSE

### Future (not this pass)
- Build Meta Ads MCP server (in `ch47/mcps/` repo)
- Wire meta-ads skills to live MCP tools
- Add tiktok-ads, linkedin-ads plugins following same pattern
- Add shopping-specific and bid-strategy skills to paid-search
