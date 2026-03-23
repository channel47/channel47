# Campaign Naming Convention Guide

## The Naming System

Every campaign name should be parseable into its key attributes at a glance.

### Format
```
{platform}-{offer/price}-{audience}-{sequence}-{modifier}
```

### Platform Prefix
| Prefix | Meaning |
|--------|---------|
| `gpm` | Google Performance Max |
| `gdg` | Google Demand Gen |
| `gs` | Google Search |
| `gd` | Google Display (rare) |

### Offer/Price Segment
| Pattern | Meaning |
|---------|---------|
| `$149` | $149 price point offer |
| `$179` | $179 price point offer |
| (brand name) | Brand-specific campaign (e.g., `directmeds`) |
| (omitted) | Legacy or general campaign |

### Audience Segment
| Pattern | Meaning |
|---------|---------|
| `women` | Women audience |
| `senior` or `seniors` | Senior audience (55+) |
| `mom` | Mom/parent audience |
| `men` | Men audience |
| `feb`, `jan` | Month-based launch (seasonal) |
| `newyearreset` | Event/promotion name |
| `bb` | Black Friday / big sale events |
| `California`, `Texas` | State-level geographic targeting |

### Sequence Number
Increment with each iteration/duplication:
- `women-1` → first women campaign
- `women-2` → second iteration (usually duplicated from -1)
- `women-4` → fourth iteration (the one that scaled)

### Modifiers
| Modifier | Meaning |
|----------|---------|
| `-phone-excl` | Mobile phone traffic excluded |
| `-pe` | Short for phone exclusion |
| `-tab` or `-tablet` | Tablet-only targeting |
| `-ce` | Custom exclusion (could be content or audience) |
| `-upt-comp` | Updated/competitor targeting variant |
| `-bb` | Black Friday / big deal variant |

## Real Examples Decoded

```
gpm-$149-women-4
├── gpm         = Performance Max
├── $149        = $149 offer
├── women       = Women audience
└── 4           = 4th iteration (scaled winner)

gpm-$149-senior-1-phone-excl
├── gpm         = Performance Max
├── $149        = $149 offer
├── senior      = Senior audience
├── 1           = 1st iteration
└── phone-excl  = Mobile phones excluded

gdg-youtube-seniors-8
├── gdg         = Demand Gen
├── youtube     = YouTube placement
├── seniors     = Senior audience
└── 8           = 8th iteration

gpm-1-feb-upt-comp
├── gpm         = Performance Max
├── 1           = Sequence 1
├── feb         = February launch
└── upt-comp    = Updated competitor targeting

directmeds-seniors-3
├── directmeds  = DirectMeds brand
├── seniors     = Senior audience
└── 3           = 3rd iteration
```

## Budget Naming Convention

Use matching budget names that auto-link to campaigns:
- Budget name: `gpm-$149-women-4` (matches campaign)
- Use non-round numbers (e.g., `$8,888.88`, `$2,588.88`) to differentiate team-managed budgets from Google suggestions

## Landing Page Mapping

Each campaign name maps to a landing page via the `sub1` parameter:
```
URL: ...&sub1=gpm-$149-women-4
```

This creates a 1:1 mapping between campaign name and landing page tracking, making attribution analysis straightforward.

## Quick-Reference Naming Template

For a new DTC brand launching campaigns:

```
# Core campaigns
gpm-{price}-women-1
gpm-{price}-women-2-phone-excl
gpm-{price}-senior-1
gpm-{price}-senior-1-phone-excl
gpm-{price}-mom-1
gpm-{price}-{month}-1

# Demand Gen
gdg-youtube-women-1
gdg-youtube-seniors-1
gdg-{price}-senior-pe-1

# Geographic tests
gpm-{price}-{State}-1

# Event/seasonal
gpm-{price}-{event}-1
gpm-{price}-bb-1
```
