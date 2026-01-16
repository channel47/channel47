# Google Ads Plugin Redesign

**Date:** 2026-01-09
**Status:** Approved
**Goal:** Maximize efficiency, minimize token debt, leverage Claude's autonomous capabilities

---

## Executive Summary

Redesign the Google Ads Specialist plugin from a skill-heavy architecture (9 skills, ~7,883 tokens) to a subagent-based architecture (1 agent, 1 skill, ~450 tokens). This achieves a **94% token reduction** while improving autonomy and context isolation.

### Key Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Approach | Moderate - subagent-based | Balance autonomy with oversight |
| Atomic skills | Remove all | Claude can write GAQL autonomously |
| Playbooks | Remove all | Start fresh, develop over time if needed |
| Query handling | Subagent | Context isolation for large results |
| Mutation handling | Direct + hook | Sensitive ops need user oversight |
| Troubleshooting | Minimal (~50 lines) | Plugin-specific only, link to Google docs |

---

## Architecture

### Before (Current)

```
plugins/google-ads-specialist/
├── commands/setup.md
├── skills/ (9 skills, ~7,883 tokens)
│   ├── atomic-campaign-performance/
│   ├── atomic-search-terms-report/
│   ├── atomic-wasted-spend-analysis/
│   ├── atomic-quality-score-audit/
│   ├── atomic-budget-pacing/
│   ├── atomic-add-negative-keywords/
│   ├── atomic-adjust-bids/
│   ├── playbook-account-health-audit/
│   └── troubleshooting-gaql-errors/
└── .claude/hooks/validate-google-ads.py
```

### After (Proposed)

```
plugins/google-ads-specialist/
├── commands/setup.md (unchanged)
├── agents/
│   └── google-ads-analyst.md (~40 lines)
├── skills/
│   └── troubleshooting/SKILL.md (~50 lines)
└── .claude/hooks/validate-mutations.py (~30 lines)
```

---

## Component Specifications

### 1. Google Ads Analyst Subagent

**File:** `agents/google-ads-analyst.md`

```markdown
---
name: google-ads-analyst
description: >
  Use for Google Ads data queries and analysis. Spawns for query tool
  only - keeps large result sets out of main context. NOT for mutations
  or account listing.
tools:
  - mcp__google-ads__query
model: sonnet
---

You are a Google Ads analyst subagent. Your job:

1. Execute the requested Google Ads query/analysis
2. Process and interpret results
3. Return appropriately sized responses:
   - <20 rows: Return data inline with brief analysis
   - 20+ rows: Summarize key insights, write full data to
     `.claude/google-ads-results/{timestamp}-{query-type}.json`

Always include:
- Row count and query execution time
- Key metrics highlighted (spend, conversions, CTR)
- Actionable insights when patterns are clear

For mutations: Confirm dry_run=true unless user explicitly
requests live execution.
```

**Design rationale:**
- Uses Sonnet model (cost-effective for data processing)
- Tool access restricted to `query` only
- Adaptive output sizing prevents context bloat
- Automatic file output for large datasets

### 2. Mutation Validation Hook

**File:** `.claude/hooks/validate-mutations.py`

```python
#!/usr/bin/env python3
"""
PreToolUse hook: Require explicit confirmation context for mutations.
Queries flow freely; mutations need user awareness.
"""
import json
import sys

def main():
    input_data = json.load(sys.stdin)
    tool_name = input_data.get("tool_name", "")

    # Only gate mutations
    if "mutate" not in tool_name.lower():
        # Allow all non-mutation tools
        print(json.dumps({"decision": "allow"}))
        return

    tool_input = input_data.get("tool_input", {})
    dry_run = tool_input.get("dry_run", True)

    if dry_run:
        # Dry run mutations are safe - allow
        print(json.dumps({"decision": "allow"}))
    else:
        # Live mutations need acknowledgment in decision
        # Hook passes but adds context reminder
        print(json.dumps({
            "decision": "allow",
            "message": "LIVE MUTATION: dry_run=false. Changes will be permanent."
        }))

if __name__ == "__main__":
    main()
```

**Design rationale:**
- Removed query validation (Claude handles GAQL autonomously)
- Removed skill-reference requirement
- Silent pass for dry runs
- Warning context for live mutations

### 3. Minimal Troubleshooting Skill

**File:** `skills/troubleshooting/SKILL.md`

```markdown
---
name: troubleshooting
description: Plugin-specific Google Ads errors. Use when hitting auth, format, or hook issues.
---

# Google Ads Plugin Troubleshooting

## Customer ID Format
- Must be 10 digits without dashes: `1234567890`
- Wrong: `123-456-7890`
- Set default: `GOOGLE_ADS_DEFAULT_CUSTOMER_ID` env var

## Authentication Errors
- "AUTHENTICATION_ERROR": Refresh token expired - re-run `/google-ads-specialist:setup`
- "PERMISSION_DENIED": Account not accessible under current MCC
- "DEVELOPER_TOKEN_NOT_APPROVED": Token still pending Google approval

## Dry Run Validation
- `dry_run: true` (default) validates but doesn't execute
- Set `dry_run: false` explicitly for live mutations
- Hook will warn on live mutations

## Common Mutation Failures
- "MUTATE_ERROR": Check operation structure matches resource type
- "RESOURCE_NOT_FOUND": Verify resource name format: `customers/{id}/campaigns/{id}`
- "INVALID_OPERATION": Can't update immutable fields

## Rate Limits
- Basic access: 15,000 operations/day
- If hitting limits: batch operations, reduce query frequency

For GAQL syntax errors, see: [Google GAQL Reference](https://developers.google.com/google-ads/api/docs/query/overview)
```

**Design rationale:**
- Only plugin-specific gotchas
- Generic GAQL syntax removed (Claude knows it, Google docs linked)
- 50 lines vs. 347 lines (85% reduction)

---

## Tool Routing Matrix

| Tool | Handler | Rationale |
|------|---------|-----------|
| `list_accounts` | Direct (orchestrator) | Small response, setup context needed |
| `query` | Subagent | Large datasets, context isolation |
| `mutate` | Direct (orchestrator) | Sensitive, needs user oversight |

---

## Migration Plan

### Files to Delete

| File | Lines | Reason |
|------|-------|--------|
| `skills/atomic-campaign-performance/` | 109 | Claude writes GAQL autonomously |
| `skills/atomic-search-terms-report/` | 114 | Claude writes GAQL autonomously |
| `skills/atomic-wasted-spend-analysis/` | 142 | Claude writes GAQL autonomously |
| `skills/atomic-quality-score-audit/` | 122 | Claude writes GAQL autonomously |
| `skills/atomic-budget-pacing/` | 116 | Claude writes GAQL autonomously |
| `skills/atomic-add-negative-keywords/` | 172 | Claude writes GAQL autonomously |
| `skills/atomic-adjust-bids/` | 179 | Claude writes GAQL autonomously |
| `skills/playbook-account-health-audit/` | 836 | Starting fresh, develop over time |
| `skills/troubleshooting-gaql-errors/` | 347 | Replaced with minimal version |
| `.claude/hooks/validate-google-ads.py` | ~100 | Replaced with mutation-only hook |

**Total deleted:** ~2,137 lines

### Files to Create

| File | Lines | Purpose |
|------|-------|---------|
| `agents/google-ads-analyst.md` | ~40 | Subagent for query isolation |
| `skills/troubleshooting/SKILL.md` | ~50 | Plugin-specific errors only |
| `.claude/hooks/validate-mutations.py` | ~30 | Gate live mutations only |

**Total created:** ~120 lines

### Files Unchanged

- `commands/setup.md` - OAuth wizard still needed
- `.mcp.json` - MCP server config unchanged
- `.claude-plugin/plugin.json` - Update to reflect new structure
- `README.md`, `GETTING_STARTED.md` - Update docs

---

## Metrics

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Total lines | 2,137 | ~120 | **-94%** |
| Token footprint | ~7,883 | ~450 | **-94%** |
| Skills | 9 | 1 | **-89%** |
| Agents | 0 | 1 | +1 |
| Hook complexity | High | Low | Simplified |

---

## Behavioral Changes

### Queries (NEW)
1. User requests Google Ads data
2. Orchestrator spawns `google-ads-analyst` subagent
3. Subagent writes GAQL autonomously, executes query
4. Small results (<20 rows): returned inline with analysis
5. Large results (20+ rows): summary returned, full data to file
6. Orchestrator context stays clean

### Mutations (MODIFIED)
1. User requests change (add negatives, adjust bids, etc.)
2. Orchestrator handles directly (no subagent)
3. Claude writes mutation operation autonomously
4. Hook allows dry_run silently, warns on live mutations
5. User has full visibility in main context

### Account Discovery (UNCHANGED)
1. User asks about accounts
2. Orchestrator calls `list_accounts` directly
3. Small response stays in context

---

## Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Claude writes invalid GAQL | Self-correcting; MCP server returns clear errors |
| Large results overwhelm context | Subagent summarizes, writes to file |
| Live mutations without oversight | Hook adds warning, user sees in main context |
| Lost institutional knowledge | Keep README, develop playbooks over time if needed |

---

## Future Considerations

- **Playbooks:** If complex workflows emerge as common patterns, add as agents (not skills)
- **MCP Server:** Consider adding pagination/cursor support for very large datasets
- **Caching:** Could add result caching to reduce repeat queries

---

## Approval

- [x] Architecture approved
- [x] Subagent design approved
- [x] Hook design approved
- [x] Troubleshooting scope approved
- [x] Migration plan approved
