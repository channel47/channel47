---
name: sync
description: Sync marketplace.json from plugin.json files (source of truth)
allowed-tools: Bash
---

# Plugin Suite Sync

Regenerate `marketplace.json` from individual `plugin.json` files. Plugin manifests are the source of truth — marketplace.json is a derived artifact.

## Steps

1. Run `bash sync.sh --dry-run` first to preview changes.
2. If changes look correct, run `bash sync.sh` to apply.
3. The script auto-fixes skill count mismatches in descriptions.
4. Review any description or version drift it reports.
