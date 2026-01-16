# Google Ads Plugin Redesign - Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Transform the plugin from 9 skills (~7,883 tokens) to 1 agent + 1 skill (~450 tokens) achieving 94% token reduction.

**Architecture:** Subagent-based design where `google-ads-analyst` handles all query operations in isolated context, mutations stay in main context with simplified hook, and minimal troubleshooting skill covers plugin-specific errors only.

**Tech Stack:** Claude Code plugins (markdown agents/skills), Python hooks, JSON config

---

## Task 1: Delete Atomic Skills

**Files:**
- Delete: `plugins/google-ads-specialist/skills/atomic-campaign-performance/`
- Delete: `plugins/google-ads-specialist/skills/atomic-search-terms-report/`
- Delete: `plugins/google-ads-specialist/skills/atomic-wasted-spend-analysis/`
- Delete: `plugins/google-ads-specialist/skills/atomic-quality-score-audit/`
- Delete: `plugins/google-ads-specialist/skills/atomic-budget-pacing/`
- Delete: `plugins/google-ads-specialist/skills/atomic-add-negative-keywords/`
- Delete: `plugins/google-ads-specialist/skills/atomic-adjust-bids/`

**Step 1: Delete all atomic skill directories**

```bash
rm -rf plugins/google-ads-specialist/skills/atomic-campaign-performance
rm -rf plugins/google-ads-specialist/skills/atomic-search-terms-report
rm -rf plugins/google-ads-specialist/skills/atomic-wasted-spend-analysis
rm -rf plugins/google-ads-specialist/skills/atomic-quality-score-audit
rm -rf plugins/google-ads-specialist/skills/atomic-budget-pacing
rm -rf plugins/google-ads-specialist/skills/atomic-add-negative-keywords
rm -rf plugins/google-ads-specialist/skills/atomic-adjust-bids
```

**Step 2: Verify deletion**

```bash
ls plugins/google-ads-specialist/skills/
```

Expected: Only `playbook-account-health-audit/` and `troubleshooting-gaql-errors/` remain

**Step 3: Commit**

```bash
git add -A plugins/google-ads-specialist/skills/
git commit -m "refactor(google-ads): remove atomic skills

Claude can write GAQL autonomously. Removes 7 skills (~954 lines).
Part of subagent-based architecture redesign."
```

---

## Task 2: Delete Playbook Skill

**Files:**
- Delete: `plugins/google-ads-specialist/skills/playbook-account-health-audit/`

**Step 1: Delete playbook directory**

```bash
rm -rf plugins/google-ads-specialist/skills/playbook-account-health-audit
```

**Step 2: Verify deletion**

```bash
ls plugins/google-ads-specialist/skills/
```

Expected: Only `troubleshooting-gaql-errors/` remains

**Step 3: Commit**

```bash
git add -A plugins/google-ads-specialist/skills/
git commit -m "refactor(google-ads): remove playbook skill

Starting fresh - will develop playbooks as agents if needed.
Removes 836 lines of mostly duplicated content."
```

---

## Task 3: Delete Old Troubleshooting Skill

**Files:**
- Delete: `plugins/google-ads-specialist/skills/troubleshooting-gaql-errors/`

**Step 1: Delete old troubleshooting directory**

```bash
rm -rf plugins/google-ads-specialist/skills/troubleshooting-gaql-errors
```

**Step 2: Verify skills directory is empty**

```bash
ls plugins/google-ads-specialist/skills/
```

Expected: Empty directory (or directory doesn't exist)

**Step 3: Commit**

```bash
git add -A plugins/google-ads-specialist/skills/
git commit -m "refactor(google-ads): remove verbose troubleshooting skill

Will be replaced with minimal plugin-specific version.
Removes 347 lines (80% was generic GAQL docs)."
```

---

## Task 4: Create Google Ads Analyst Subagent

**Files:**
- Create: `plugins/google-ads-specialist/agents/google-ads-analyst.md`

**Step 1: Create agents directory**

```bash
mkdir -p plugins/google-ads-specialist/agents
```

**Step 2: Create the subagent file**

Create `plugins/google-ads-specialist/agents/google-ads-analyst.md`:

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

**Step 3: Verify file creation**

```bash
cat plugins/google-ads-specialist/agents/google-ads-analyst.md
```

Expected: File contents match above

**Step 4: Commit**

```bash
git add plugins/google-ads-specialist/agents/
git commit -m "feat(google-ads): add analyst subagent for query isolation

Subagent handles all GAQL queries in isolated context:
- Small results (<20 rows) returned inline
- Large results summarized + written to file
- Uses Sonnet model for cost efficiency"
```

---

## Task 5: Create Minimal Troubleshooting Skill

**Files:**
- Create: `plugins/google-ads-specialist/skills/troubleshooting/SKILL.md`

**Step 1: Create troubleshooting directory**

```bash
mkdir -p plugins/google-ads-specialist/skills/troubleshooting
```

**Step 2: Create the skill file**

Create `plugins/google-ads-specialist/skills/troubleshooting/SKILL.md`:

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

**Step 3: Verify file creation**

```bash
cat plugins/google-ads-specialist/skills/troubleshooting/SKILL.md
```

Expected: File contents match above

**Step 4: Commit**

```bash
git add plugins/google-ads-specialist/skills/troubleshooting/
git commit -m "feat(google-ads): add minimal troubleshooting skill

Plugin-specific errors only (~50 lines vs 347 before):
- Customer ID format
- Auth errors
- Mutation failures
- Rate limits
Links to Google docs for GAQL syntax."
```

---

## Task 6: Replace Hook with Mutation-Only Version

**Files:**
- Delete: `plugins/google-ads-specialist/.claude/hooks/validate-google-ads.py`
- Create: `plugins/google-ads-specialist/.claude/hooks/validate-mutations.py`

**Step 1: Delete old hook**

```bash
rm plugins/google-ads-specialist/.claude/hooks/validate-google-ads.py
```

**Step 2: Create new mutation-only hook**

Create `plugins/google-ads-specialist/.claude/hooks/validate-mutations.py`:

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

**Step 3: Make executable**

```bash
chmod +x plugins/google-ads-specialist/.claude/hooks/validate-mutations.py
```

**Step 4: Verify file creation**

```bash
cat plugins/google-ads-specialist/.claude/hooks/validate-mutations.py
```

Expected: File contents match above

**Step 5: Commit**

```bash
git add plugins/google-ads-specialist/.claude/hooks/
git commit -m "refactor(google-ads): simplify hook to mutations only

Queries now flow freely (Claude writes GAQL autonomously).
Hook only gates mutations:
- Dry runs pass silently
- Live mutations get warning message"
```

---

## Task 7: Update Hook Settings

**Files:**
- Modify: `plugins/google-ads-specialist/.claude/settings.json`

**Step 1: Update settings.json**

Replace contents of `plugins/google-ads-specialist/.claude/settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "mcp__google-ads__mutate",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/validate-mutations.py",
            "timeout": 5
          }
        ]
      }
    ]
  }
}
```

**Step 2: Verify file update**

```bash
cat plugins/google-ads-specialist/.claude/settings.json
```

Expected: Matcher is now `mcp__google-ads__mutate` (not `query|mutate`)

**Step 3: Commit**

```bash
git add plugins/google-ads-specialist/.claude/settings.json
git commit -m "refactor(google-ads): update hook to match mutate only

Removes query from matcher - queries handled by subagent now."
```

---

## Task 8: Update Plugin Manifest

**Files:**
- Modify: `plugins/google-ads-specialist/.claude-plugin/plugin.json`

**Step 1: Update plugin.json**

Replace contents of `plugins/google-ads-specialist/.claude-plugin/plugin.json`:

```json
{
  "name": "google-ads-specialist",
  "version": "4.0.0",
  "description": "Google Ads management with subagent-based architecture. Query isolation via analyst subagent, autonomous GAQL generation, mutation oversight via hooks.",
  "author": {
    "name": "Jackson",
    "url": "https://channel47.dev"
  },
  "homepage": "https://channel47.dev/plugins/google-ads-specialist",
  "repository": "https://github.com/channel47/channel47",
  "keywords": ["google-ads", "advertising", "gaql", "ppc", "marketing", "analytics", "subagent"],
  "license": "MIT",
  "mcpServers": "./.mcp.json"
}
```

**Step 2: Verify file update**

```bash
cat plugins/google-ads-specialist/.claude-plugin/plugin.json
```

Expected: Version is `4.0.0`, description mentions subagent architecture

**Step 3: Commit**

```bash
git add plugins/google-ads-specialist/.claude-plugin/plugin.json
git commit -m "chore(google-ads): bump version to 4.0.0

Major version bump for architectural change:
- Skill-based -> Subagent-based
- 94% token reduction"
```

---

## Task 9: Update CHANGELOG

**Files:**
- Modify: `plugins/google-ads-specialist/CHANGELOG.md`

**Step 1: Read current changelog**

```bash
head -20 plugins/google-ads-specialist/CHANGELOG.md
```

**Step 2: Prepend new version entry**

Add to top of `plugins/google-ads-specialist/CHANGELOG.md` (after title):

```markdown
## [4.0.0] - 2026-01-09

### Breaking Changes
- Removed all atomic skills (7 skills)
- Removed playbook skill
- Removed skill-reference requirement for queries

### Added
- `google-ads-analyst` subagent for query isolation
- Adaptive result sizing (inline vs file output)
- Minimal troubleshooting skill (plugin-specific only)

### Changed
- Hook now gates mutations only (queries flow freely)
- 94% token reduction (7,883 -> ~450 tokens)

### Migration
- No action needed for queries - they work autonomously now
- Mutations still require dry_run handling (unchanged behavior)
- For GAQL syntax help, see Google docs (no longer bundled)

```

**Step 3: Verify changelog update**

```bash
head -30 plugins/google-ads-specialist/CHANGELOG.md
```

Expected: New 4.0.0 entry at top

**Step 4: Commit**

```bash
git add plugins/google-ads-specialist/CHANGELOG.md
git commit -m "docs(google-ads): add 4.0.0 changelog entry"
```

---

## Task 10: Update README

**Files:**
- Modify: `plugins/google-ads-specialist/README.md`

**Step 1: Read current README structure**

```bash
head -50 plugins/google-ads-specialist/README.md
```

**Step 2: Update README to reflect new architecture**

Key sections to update:
- Overview: Mention subagent-based architecture
- Features: Update to reflect new capabilities
- How it works: Describe subagent flow
- Remove references to atomic skills

Create updated README reflecting the new architecture. Keep setup instructions, update architecture section.

**Step 3: Verify README update**

```bash
head -50 plugins/google-ads-specialist/README.md
```

**Step 4: Commit**

```bash
git add plugins/google-ads-specialist/README.md
git commit -m "docs(google-ads): update README for v4.0.0 architecture

Reflects subagent-based design:
- Query isolation via analyst subagent
- Autonomous GAQL generation
- Mutation oversight via hooks"
```

---

## Task 11: Final Verification

**Step 1: Verify directory structure**

```bash
find plugins/google-ads-specialist -type f \( -name "*.md" -o -name "*.py" -o -name "*.json" \) | grep -v node_modules | sort
```

Expected structure:
```
plugins/google-ads-specialist/.claude/hooks/validate-mutations.py
plugins/google-ads-specialist/.claude/settings.json
plugins/google-ads-specialist/.claude-plugin/plugin.json
plugins/google-ads-specialist/.mcp.json
plugins/google-ads-specialist/agents/google-ads-analyst.md
plugins/google-ads-specialist/CHANGELOG.md
plugins/google-ads-specialist/commands/setup.md
plugins/google-ads-specialist/docs/plans/...
plugins/google-ads-specialist/GETTING_STARTED.md
plugins/google-ads-specialist/MIGRATION_3.1.md
plugins/google-ads-specialist/package.json
plugins/google-ads-specialist/README.md
plugins/google-ads-specialist/skills/troubleshooting/SKILL.md
```

**Step 2: Count lines in new files**

```bash
wc -l plugins/google-ads-specialist/agents/google-ads-analyst.md \
      plugins/google-ads-specialist/skills/troubleshooting/SKILL.md \
      plugins/google-ads-specialist/.claude/hooks/validate-mutations.py
```

Expected: ~120 total lines

**Step 3: Verify git status is clean**

```bash
git status
```

Expected: `nothing to commit, working tree clean`

---

## Summary

| Task | Description | Commits |
|------|-------------|---------|
| 1 | Delete atomic skills | 1 |
| 2 | Delete playbook skill | 1 |
| 3 | Delete old troubleshooting | 1 |
| 4 | Create analyst subagent | 1 |
| 5 | Create minimal troubleshooting | 1 |
| 6 | Replace hook | 1 |
| 7 | Update hook settings | 1 |
| 8 | Update plugin manifest | 1 |
| 9 | Update CHANGELOG | 1 |
| 10 | Update README | 1 |
| 11 | Final verification | 0 |

**Total: 10 commits, ~120 lines added, ~2,137 lines removed**
