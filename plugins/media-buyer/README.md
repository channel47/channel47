# Media Buyer — Claude Code Plugin

Connect and manage paid ad accounts across Google Ads and Bing Ads. Auth, reporting, campaign management, and bulk operations via self-contained Python scripts.

No MCP servers required. No external dependencies beyond the platform SDKs.

---

## Install

```
/plugin marketplace add channel47/channel47
/plugin install media-buyer@channel47
```

### Dependencies

```bash
pip install google-ads bingads pandas
```

---

## What's Inside

```
media-buyer/
├── .claude-plugin/
│   └── plugin.json
├── hooks/
│   ├── hooks.json                     # Mutation safety gate
│   └── validate-mutations.py          # Flags live mutations before execution
├── skills/
│   └── ad-platform-connection/
│       ├── SKILL.md                   # Routing hub — detects platform, loads references + scripts
│       ├── scripts/
│       │   ├── google/
│       │   │   ├── auth.py            # OAuth2 setup, account listing, token rotation
│       │   │   ├── report.py          # GAQL queries → pandas DataFrames
│       │   │   └── mutate.py          # Campaign/ad group/keyword/ad CRUD with dry-run default
│       │   └── bing/
│       │       ├── auth.py            # OAuth2 setup, account switching
│       │       └── report.py          # Reporting API → pandas DataFrames
│       └── references/
│           ├── shared/
│           │   └── config-patterns.md
│           ├── google/
│           │   ├── campaign-management.md
│           │   ├── shopping-campaigns.md
│           │   └── reporting.md
│           └── bing/
│               ├── campaign-management.md
│               ├── shopping-campaigns.md
│               ├── content-api.md
│               ├── bulk-operations.md
│               └── reporting.md
├── README.md
├── LICENSE
└── .gitignore
```

---

## How It Works

Say "connect to Google Ads," "pull campaign performance," "set up a shopping campaign," or any ad platform phrase. The skill detects the platform from context and routes to the right scripts and references.

### Platform Detection

- **Google** — Google Ads, GAQL, Performance Max, RSA, Google Shopping
- **Bing** — Bing, Microsoft Advertising, MSAN, Microsoft Merchant Center
- **Ambiguous** — asks which platform; defaults to Google for generic paid-search phrasing

### Config Files

| Platform | Config Path |
|----------|-------------|
| Google Ads | `~/.google_ads_config.json` |
| Bing Ads | `~/.msads_config.json` |

See `references/shared/config-patterns.md` for setup details.

---

## Capabilities

### Google Ads

| What | Script |
|------|--------|
| Auth and account setup | `scripts/google/auth.py` |
| Campaign/ad group/keyword/ad CRUD | `scripts/google/mutate.py` |
| Shopping campaigns | `scripts/google/mutate.py` |
| Reporting (GAQL → DataFrames) | `scripts/google/report.py` |

### Bing Ads

| What | Script / Method |
|------|-----------------|
| Auth and account setup | `scripts/bing/auth.py` |
| Campaign/ad group/keyword/ad CRUD | Bing SDK service calls |
| Shopping campaigns | Bing SDK service calls |
| Merchant Center catalog management | Content API REST |
| Reporting | `scripts/bing/report.py` |
| Bulk changes (50+) | `BulkServiceManager` |

---

## Safety

All write operations follow the same protocol:

1. Read before write
2. Dry run first (`dry_run=True` is the default in Google mutate helpers)
3. Confirm planned changes with the user before live execution
4. Small batches first, then scale
5. No deletes unless explicitly confirmed

The mutation validation hook intercepts Google Ads write operations. Dry runs pass silently. Live mutations get flagged with a warning before execution. Read operations always flow freely.

---

## Built by Channel 47

[channel47.dev](https://channel47.dev)
