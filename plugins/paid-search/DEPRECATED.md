# Deprecated — Use google-ads and microsoft-ads Instead

The `paid-search` plugin (v7.0.0) combined Google Ads and Bing Ads into one plugin. It has been replaced by two standalone, platform-specific plugins with expanded skill sets.

## Migration Guide

### Google Ads Users

Install the `google-ads` plugin:

```bash
/plugin install google-ads@channel47
```

**What you get:**
- All 6 original skills (platform-setup, profile-review, morning-brief, waste-detector, search-term-verdict, pmax-decoder)
- 3 new skills: account-scorecard, ad-copy-analyzer, competitor-intel
- Read-only by design (no mutations — action plans with UI paths instead)
- `GOOGLE_ADS_READ_ONLY=true` enforced at MCP level

**Env vars:** Same Google Ads env vars. No changes needed.

### Microsoft Ads Users

Install the `microsoft-ads` plugin:

```bash
/plugin install microsoft-ads@channel47
```

**What you get:**
- 5 ported skills (platform-setup, profile-review, morning-brief, waste-detector, search-term-verdict)
- 3 new skills: account-scorecard, import-auditor, placement-cleaner
- Read-only by design

**Env vars:** Same Bing Ads env vars. No changes needed.

### Both Platforms

Install both plugins. They work independently — no cross-plugin dependencies.

### Account Profile

Your existing `profile/account-profile.md` is compatible with both new plugins. Copy it to the new plugin's `profile/` directory if you have one.

## What's Different

| Feature | paid-search v7 | google-ads + microsoft-ads v1 |
|---------|---------------|-------------------------------|
| Mutations | Supported (dry-run gated) | Removed — action plans only |
| Skills | 6 shared | 9 Google + 8 Microsoft |
| Safety hooks | PreToolUse mutation validator | No mutation hooks needed |
| Platform coupling | Shared skills detect platforms | Fully independent |
| New capabilities | — | Scorecard, ad copy, competitor intel, import auditor, placement cleaner |

## This Plugin

This plugin remains functional but frozen. No new features or bug fixes. Use the standalone plugins for active development.
