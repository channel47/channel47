---
name: creative-analyzer
description: >-
  This skill should be used when the user asks to "analyze my Meta creatives",
  "review ad performance", "which ads are working", "creative fatigue check",
  "ad creative audit", "best performing ads", "worst performing ads",
  "creative testing results", "hook rate analysis", or mentions creative
  performance, ad fatigue, thumb-stop ratio, or video ad metrics.
allowed-tools: mcp__meta-ads__query, mcp__meta-ads__list_accounts
---

# Creative Analyzer

Evaluate Meta Ads creative performance at the ad level — identify winners, flag fatigue, and surface replacement priorities.

## Status

Skeleton — requires `@channel47/meta-ads-mcp` to be built and published before this skill is functional.

## Account Context

Read `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md` at the start of every run.
If it exists:
- Use known account IDs — skip `list_accounts` discovery.
- Apply KPI targets as anomaly detection thresholds (e.g., flag CPA > target CPA, CPM > ceiling).
- Use frequency cap from profile to calibrate fatigue alerts on creatives.
- Note active creative tests when interpreting performance — don't flag test variants as underperformers.
- Check watch list for follow-up items from prior sessions.
If it doesn't exist, fall back to `list_accounts` and suggest running `platform-setup`.

## Key Creative Metrics

| Metric | What It Measures | Good Benchmark |
|--------|-----------------|----------------|
| Hook Rate | % of viewers past 3 seconds (video) | >25% |
| Hold Rate | % of hook viewers to 50% completion | >30% |
| ThruPlay Rate | % to completion or 15s | >15% |
| Thumb-Stop Ratio | 3s views / impressions | >20% |
| CTR | Click-through rate | >1.0% (feed) |
| Outbound CTR | Clicks to external URL / impressions | >0.8% |
| Frequency | Avg times shown per person | <3.0 per 7d |
| CPA | Cost per conversion | Varies by vertical |

## Workflow

### Phase 1: Pull creative performance data

For each active campaign, pull ad-level data:
- Performance metrics (impressions, clicks, CTR, CPA, ROAS)
- Video metrics (hook rate, hold rate, ThruPlay rate)
- Creative asset details (format, copy, thumbnail)
- Frequency and delivery status

### Phase 2: Classify creatives

Assign each ad a status:
- **Winner**: CPA below target, CTR above benchmark, sufficient volume
- **Fatigued**: Was performing well, now declining (frequency > 3, CTR dropped >20% from peak)
- **Underperformer**: Never hit benchmarks with sufficient spend
- **Testing**: Insufficient data to classify (<1,000 impressions or <$50 spend)
- **New**: Less than 3 days old

### Phase 3: Generate recommendations

- Replacement priorities for fatigued and underperforming creatives
- Winning creative patterns (what format, hook style, copy angle works)
- Budget reallocation suggestions (shift spend to winners)

## Output format

```markdown
## Creative Analysis - [Date]
### Campaign: [Name]

### Winners
| Ad | Format | CTR | CPA | ROAS | Hook Rate | Notes |

### Fatigued (Replace Soon)
| Ad | Format | Frequency | CTR Decline | Days Active | Priority |

### Underperformers (Consider Pausing)
| Ad | Format | Spend | CPA | vs Target | Recommendation |

### Testing (Insufficient Data)
| Ad | Format | Spend | Impressions | Status |

### Creative Patterns
- Top-performing format: [image/video/carousel]
- Best hook style: [question/stat/pain point]
- Winning copy angle: [benefit/social proof/urgency]
```

## Guardrails

- Do not recommend pausing creatives without noting the learning-loss tradeoff
- Minimum data thresholds before classifying (1,000 impressions or $50 spend)
- Note that Meta's ad-level metrics can lag 24-48 hours
- Creative performance is heavily audience-dependent — note this context

## References

- `references/` — to be populated when MCP server is built
