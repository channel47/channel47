# Media Buyer - Claude Code Plugin

Operational toolkit for paid-search execution with MCP-native Google Ads access.

The plugin supports daily media-buyer workflows: setup verification, morning health checks, waste detection, search-term verdicting, and Performance Max decoding.

---

## Install

```bash
/plugin marketplace add channel47/channel47
/plugin install media-buyer@channel47
```

---

## Version

Current plugin version: `6.0.0`

---

## Configuration

This plugin bundles Google Ads MCP via `.mcp.json`:

```json
{
  "google-ads": {
    "command": "npx",
    "args": ["-y", "@channel47/google-ads-mcp@latest"],
    "env": {
      "GOOGLE_ADS_DEVELOPER_TOKEN": "${GOOGLE_ADS_DEVELOPER_TOKEN}",
      "GOOGLE_ADS_CLIENT_ID": "${GOOGLE_ADS_CLIENT_ID}",
      "GOOGLE_ADS_CLIENT_SECRET": "${GOOGLE_ADS_CLIENT_SECRET}",
      "GOOGLE_ADS_REFRESH_TOKEN": "${GOOGLE_ADS_REFRESH_TOKEN}",
      "GOOGLE_ADS_LOGIN_CUSTOMER_ID": "${GOOGLE_ADS_LOGIN_CUSTOMER_ID}"
    }
  }
}
```

Set required environment variables in your shell profile before using the plugin.

---

## What's Inside

```text
media-buyer/
├── .claude-plugin/
│   └── plugin.json
├── .mcp.json
├── hooks/
│   ├── hooks.json
│   └── validate-mutations.py
├── skills/
│   ├── platform-setup/
│   ├── morning-brief/
│   ├── waste-detector/
│   ├── search-term-verdict/
│   └── pmax-decoder/
├── tests/
├── README.md
└── LICENSE
```

---

## Skill Inventory

### 1) `platform-setup`

Setup and verification guidance for Google Ads and Bing credentials. Uses `mcp__google-ads__list_accounts` for Google access validation.

### 2) `morning-brief`

Builds a daily account-health summary from GAQL queries via `mcp__google-ads__query`.

### 3) `waste-detector`

Finds high-impact spend leaks and prepares remediation actions using `mcp__google-ads__query` and `mcp__google-ads__mutate` (dry-run first).

### 4) `search-term-verdict`

Classifies search terms and prepares negative keyword packages with `mcp__google-ads__query` plus approval-gated `mcp__google-ads__mutate`.

### 5) `pmax-decoder`

Analyzes Performance Max campaign transparency data and proposes actions via `mcp__google-ads__query` and optional dry-run mutations.

---

## Safety Model

All write operations follow the same protocol:

1. Query and analyze first.
2. Preview mutations with `dry_run: true`.
3. Request explicit user approval.
4. Execute with `dry_run: false` only after approval.

`hooks/validate-mutations.py` is bound to `mcp__google-ads__mutate` in `hooks/hooks.json`.

---

## Typical Prompts

- "Set up and verify my Google Ads access."
- "Give me this morning's account brief."
- "Find where I am wasting budget this month."
- "Review search terms and draft negatives."
- "Decode what my PMax campaign is actually doing."

---

## Built by Channel 47

[channel47.dev](https://channel47.dev)
