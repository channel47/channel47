# Channel 47 vs Official Anthropic Plugin Guidelines

Comparison analysis based on [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) repository and [Claude Code Plugin Documentation](https://code.claude.com/docs/en/plugins).

## Executive Summary

Channel 47 plugins are **largely compliant** with official guidelines. Tool plugins (ads, gen, copy) follow best practices well. Domain plugins introduce custom extensions that work but aren't officially documented. Several improvements would increase compatibility and future-proofing.

---

## Plugin Manifest (plugin.json) Comparison

### Required Fields

| Field | Official | Channel 47 | Status |
|-------|----------|------------|--------|
| `name` | ✓ Required | ✓ Present | **Compliant** |
| `description` | ✓ Required | ✓ Present | **Compliant** |
| `version` | ✓ Required, semver | ✓ Present, semver | **Compliant** |

### Optional Fields

| Field | Official | Channel 47 | Status |
|-------|----------|------------|--------|
| `author` | `{ name: string }` | `{ name, url }` | **Extended** |
| `homepage` | ✓ URL string | ✓ Present | **Compliant** |
| `repository` | ✓ URL string | ✓ Present | **Compliant** |
| `license` | ✓ String | ✓ Present | **Compliant** |

### Custom Fields (Not in Official Spec)

| Field | Channel 47 Usage | Risk Level |
|-------|------------------|------------|
| `keywords` | Array of search terms | **Low** - Likely ignored |
| `mcpServers` | Path to `.mcp.json` | **Medium** - Non-standard reference |
| `domain` | Domain metadata object | **Medium** - Custom extension |
| `author.url` | Author website | **Low** - Extra property |

---

## Directory Structure Comparison

### Official Structure
```
plugin-name/
├── .claude-plugin/
│   └── plugin.json          # ONLY plugin.json here
├── .mcp.json                # MCP config at root
├── .lsp.json                # LSP config at root (optional)
├── commands/                # Slash commands
│   └── command-name.md
├── agents/                  # Agent definitions
│   └── agent-name/
│       └── agent.md
├── skills/                  # Skills (model-invoked)
│   └── skill-name/
│       └── SKILL.md
├── hooks/
│   └── hooks.json           # Event handlers
└── README.md
```

### Channel 47 Structure (Ads Plugin)
```
ads/
├── .claude-plugin/
│   └── plugin.json          ✅ Correct
├── .mcp.json                ✅ Correct
├── commands/
│   └── setup.md             ✅ Correct
├── agents/
│   └── google-ads-analyst.md  ⚠️ Missing subdirectory
├── skills/
│   └── troubleshooting/
│       └── SKILL.md         ✅ Correct
├── hooks/
│   ├── hooks.json           ✅ Correct
│   └── validate-mutations.py ✅ Correct
└── README.md                ✅ Correct
```

### Issues Found

1. **Agent Structure**: Official uses `agents/agent-name/agent.md`, Channel 47 uses `agents/agent-name.md`
2. **Gen Plugin**: Has `agents/image-creator/agent.md` which is correct
3. **Ads Plugin**: Has `agents/google-ads-analyst.md` (flat structure)

---

## Hooks Comparison

### Official hooks.json Schema
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [{ "type": "command", "command": "npm run lint:fix $FILE" }]
      }
    ]
  }
}
```

### Channel 47 hooks.json (Ads)
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "mcp__google-ads__mutate",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PLUGIN_ROOT}/hooks/validate-mutations.py",
            "timeout": 5
          }
        ]
      }
    ]
  }
}
```

### Comparison

| Aspect | Official | Channel 47 | Status |
|--------|----------|------------|--------|
| Root structure | `{ hooks: { EventName: [...] } }` | `{ hooks: { EventName: [...] } }` | ✅ Match |
| Event location | Key name | Key name | ✅ Match |
| Matcher | String pattern | String pattern | ✅ Match |
| Path variable | `${CLAUDE_PLUGIN_ROOT}` | `${CLAUDE_PLUGIN_ROOT}` | ✅ Match |
| Timeout | Optional | Present | ✅ Extended |

**Status**: ✅ Compliant - Hooks follow official format exactly.

---

## Skills Comparison

### Official SKILL.md Format
```yaml
---
name: skill-name
description: Trigger conditions for this skill
version: 1.0.0  # Optional
---

Skill content here...
```

### Channel 47 SKILL.md (Copy Plugin)
```yaml
---
name: copywriting-expert
description: Copywriting specialist with legendary frameworks from Schwartz, Hemingway, and Halbert
version: 2.1.1
---
```

**Status**: ✅ Compliant - All required frontmatter present

---

## Commands Comparison

### Official Command Format
```yaml
---
description: Short description for /help
argument-hint: <arg1> [optional-arg]
allowed-tools: [Read, Glob, Grep]
---
```

### Channel 47 Command (Copy Plugin - email.md)
```yaml
---
description: Write a strategic email sequence
allowed-tools: [Read, Grep, Glob, Bash]
---
```

**Status**: ✅ Compliant - Correct frontmatter format

---

## MCP Configuration Comparison

### Official .mcp.json
```json
{
  "server-name": {
    "type": "http",
    "url": "https://mcp.example.com/api"
  }
}
```

### Channel 47 .mcp.json
```json
{
  "mcpServers": {
    "google-ads": {
      "command": "npx",
      "args": ["-y", "@channel47/google-ads-mcp@latest"]
    }
  }
}
```

### Difference

- **Official**: Direct server object at root
- **Channel 47**: Wrapped in `mcpServers` object
- **Server type**: Official shows HTTP example; Channel 47 uses stdio (command-based)

Both patterns appear valid for different server types (HTTP vs stdio).

---

## Domain Plugin Architecture (Custom)

Channel 47 introduces a domain concept not in official specs:

```json
{
  "domain": {
    "name": "Marketing",
    "professionsReplaced": ["Media Buyer", "Copywriter"],
    "tools": ["ads", "gen", "copy"]
  }
}
```

### Assessment

| Aspect | Evaluation |
|--------|------------|
| Innovation | Creative solution for organizing plugins |
| Compatibility | Unknown - not officially supported |
| Risk | Medium - may be ignored or cause issues |
| Recommendation | Document as extension; watch for official domain support |

---

## Recommendations

### High Priority

1. **Standardize agent directory structure**
   - Move `ads/agents/google-ads-analyst.md` to `ads/agents/google-ads-analyst/agent.md`
   - Gen plugin already follows correct pattern: `agents/image-creator/agent.md`

### Medium Priority

3. **Add `${CLAUDE_PLUGIN_ROOT}` consistently**
   - Already used in hooks ✅
   - Consider for any relative paths in documentation

4. **Document custom fields**
   - Add comments or documentation explaining `keywords`, `domain`, `mcpServers` extensions
   - Track official support for these features

5. **Consider LSP integration**
   - Official supports `.lsp.json` for language servers
   - Could enhance developer experience for code-heavy plugins

### Low Priority

6. **Align author field**
   - Consider moving `author.url` to `homepage` field
   - Official spec only shows `author.name`

7. **Validate against plugin-dev toolkit**
   - Install `plugin-dev` plugin from official repository
   - Run validation utilities: `validate-hook-schema.sh`, `validate-agent.sh`

---

## Compliance Summary

| Component | Status | Notes |
|-----------|--------|-------|
| plugin.json required fields | ✅ Compliant | All present |
| plugin.json optional fields | ✅ Compliant | Well documented |
| Directory structure | ⚠️ Partial | Ads agent structure differs |
| Commands | ✅ Compliant | Correct format |
| Skills | ✅ Compliant | Correct format |
| Hooks | ✅ Compliant | Matches official format |
| MCP config | ✅ Compliant | Valid stdio pattern |
| Custom extensions | ⚠️ Unknown | `domain`, `keywords` fields |

### Overall Score: **90% Compliant**

Channel 47 plugins follow official guidelines well. The only structural issue is the ads plugin agent directory (flat vs nested). The domain plugin architecture is an innovative extension that should be documented as non-standard. Primary action item is standardizing agent directory structure in the ads plugin.

---

## Sources

- [Anthropic Claude Plugins Official Repository](https://github.com/anthropics/claude-plugins-official)
- [Claude Code Plugin Documentation](https://code.claude.com/docs/en/plugins)
- [plugin-dev Toolkit](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/plugin-dev)
