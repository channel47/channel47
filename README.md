# Channel 47 Plugin Marketplace

Claude Code plugin marketplace for Google Ads workflows.

## Structure

```
.claude-plugin/marketplace.json   # Plugin registry
plugins/
  ads-legacy/                     # Full ads suite (PMax, Search, Audit, Research)
  media-buyer/                    # Streamlined media buyer skills
```

## Plugin Version Sync

When modifying plugins, update version in all three:
1. `plugins/{plugin}/.claude-plugin/plugin.json`
2. `plugins/{plugin}/package.json`
3. `.claude-plugin/marketplace.json`
