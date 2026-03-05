---
name: profile-review
description: >-
  This skill should be used when the user asks to "review profile",
  "clean up profile", "profile maintenance", "stale watch items",
  "profile audit", "check my profile", "tidy up the account profile",
  "my Bing profile is messy", "old watch items", "clean up decision log",
  "profile hygiene", "outdated targets",
  or mentions profile cleanup, stale watch items, decision log maintenance,
  or account profile audit for Microsoft Ads.
version: 0.1.0
---

# Profile Review — Microsoft Ads

Periodic cleanup of the account profile to keep it lean and actionable.
Run after a few weeks of automated profile updates, or whenever the
watch list or decision log feels cluttered.

## Workflow

### 1. Load Profile

Read `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md`.

If the file does not exist, inform the user and suggest running
`platform-setup` to generate an initial profile. Stop here.

### 2. Audit Watch List

Scan all entries under `## Watch List`. Each entry follows the format
`- [YYYY-MM-DD] description`.

- **Stale items:** Flag any entry older than 14 days from today.
- For each stale item, ask whether to:
  - **Resolve** -- remove it (issue addressed)
  - **Promote** -- move it to Active Tests (needs formal investigation)
  - **Keep** -- reset the date to today (still relevant)

Present stale items in a table:

| Date | Item | Suggested Action |
|------|------|-----------------|
| ... | ... | Resolve / Promote / Keep |

### 3. Audit Active Tests

Scan all entries under `## Active Tests`.

- **Stale tests:** Flag tests with a start date older than 30 days
  that have no end date or results noted.
- For each stale test, ask whether to:
  - **Complete** -- record results and move to Decision Log
  - **Extend** -- reset start date (still running)
  - **Abandon** -- remove (no longer relevant)

### 4. Audit Decision Log

Scan all entries under `## Decision Log`.

- **Bloated log:** If there are more than 20 entries, suggest archiving
  older entries to `${CLAUDE_PLUGIN_ROOT}/profile/decision-archive.md`.
- Archive proposal: move all entries older than 30 days to the archive
  file, keeping the 10 most recent in the active log.
- Create the archive file if it doesn't exist. Prepend a header:
  `# Decision Archive — Microsoft Ads`

### 5. Audit Import Config

Check the `## Import Config` section.

- If auto-import is enabled, verify the last import date is recent (within 7 days).
- If import schedule is set, verify it matches the user's intended cadence.
- Flag if auto-import is enabled but no manual review has been noted in the Decision Log recently -- auto-imports can silently overwrite manual Bing optimizations.

### 6. Validate Accounts

Check the `## Accounts` section.

- If there is a "Last verified" or "Last updated" date older than
  30 days, suggest re-running `platform-setup` to refresh account
  discovery and verify active accounts.

### 7. Validate Targets

Check the `## Targets` section.

- Ask whether KPI targets (CPA, ROAS, budget) are still current.
- If any target has a note or date older than 30 days, flag it for review.

### 8. Apply Changes

Present all proposed changes as a summary before writing:

- Items to remove from Watch List
- Tests to complete/archive/remove
- Decision Log entries to archive
- Import Config updates
- Target updates

**Apply only after explicit user approval.** Write the updated profile
back to `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md`. Update the
"Last updated" date.
