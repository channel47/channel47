# Media Buyer - Claude Code Plugin

Operational toolkit for paid-search execution.

The plugin connects to live ad platforms and helps media buyers do daily account
work: search term review, anomaly triage, waste detection, and Performance Max
analysis. Strategy and planning are intentionally out of scope.

---

## Install

```bash
/plugin marketplace add channel47/channel47
/plugin install media-buyer@channel47
```

### Dependencies

```bash
pip install google-ads bingads pandas
```

---

## Version

Current plugin version: `5.0.0`

---

## What's Inside

```text
media-buyer/
├── .claude-plugin/
│   └── plugin.json
├── hooks/
│   ├── hooks.json
│   └── validate-mutations.py
├── skills/
│   ├── ad-platform-connection/
│   │   ├── SKILL.md
│   │   ├── scripts/google/{auth,report,mutate}.py
│   │   ├── scripts/bing/{auth,report}.py
│   │   └── references/{shared,google,bing}/*.md
│   ├── search-term-verdict/
│   │   ├── SKILL.md
│   │   └── references/{gaql-queries,verdict-heuristics}.md
│   ├── morning-brief/
│   │   ├── SKILL.md
│   │   └── references/{gaql-queries,anomaly-formulas}.md
│   ├── waste-detector/
│   │   ├── SKILL.md
│   │   └── references/{gaql-queries,thresholds,benchmarks}.md
│   └── pmax-decoder/
│       ├── SKILL.md
│       └── references/gaql-queries.md
├── docs/
├── tests/
├── README.md
└── LICENSE
```

---

## Skill Inventory

### 1) `ad-platform-connection` (foundation)

Shared auth, reporting, and mutation layer for Google Ads and Bing Ads.

- Google: OAuth, GAQL reporting, campaign/ad/keyword mutations.
- Bing: OAuth, reporting helpers, service patterns.
- Safety defaults: read before write, `dry_run=True` by default.

### 2) `search-term-verdict`

Classifies search terms as `NEGATE`, `PROMOTE`, `INVESTIGATE`, or `KEEP` and
builds ready-to-apply negative keyword lists and promotion candidates.

### 3) `morning-brief`

Generates a daily account-health narrative with prioritized anomalies, budget
pacing risk, disapprovals, and recent change summaries.

### 4) `waste-detector`

Finds eight common spend leaks, quantifies estimated monthly waste, and outputs
concrete remediation actions.

### 5) `pmax-decoder`

Analyzes Performance Max campaign transparency gaps: search categories, channel
distribution, asset labels, brand cannibalization risk, and placements.

---

## Dependency Flow

```text
ad-platform-connection
├── search-term-verdict
├── morning-brief
├── waste-detector
└── pmax-decoder
```

The four execution skills use existing scripts in
`skills/ad-platform-connection/scripts/google/` and do not duplicate SDK code.

---

## Safety Model

All write operations follow the same protocol:

1. Query and analyze first.
2. Preview write operations with `dry_run=True`.
3. Request explicit user approval.
4. Execute live mutation only after approval.
5. Keep changes scoped and auditable.

The mutation hook in `hooks/validate-mutations.py` flags live write attempts
through both MCP tool calls and direct Python script execution.

---

## Typical Prompts

- "Review my search terms and draft negatives."
- "Give me this morning's account brief."
- "Find where I am wasting budget this month."
- "Decode what my PMax campaign is actually doing."
- "Connect to Google Ads and pull campaign performance."

---

## Built by Channel 47

[channel47.dev](https://channel47.dev)
