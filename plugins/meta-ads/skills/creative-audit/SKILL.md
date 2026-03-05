---
name: creative-audit
description: >-
  This skill should be used when the user asks to "audit my creatives",
  "creative mix analysis", "what ad formats am I missing", "creative gaps",
  "creative diversity check", "ad format breakdown", "creative matrix",
  "creative testing roadmap", "what types of ads should I test",
  "am I running enough video", "I keep running the same ads",
  "what creative concepts work", "creative strategy review",
  "what ads should I make next",
  or mentions creative categorization, format analysis, concept mapping,
  creative gap identification, or creative mix optimization for Meta Ads.
allowed-tools: mcp__meta-ads__list_ads, mcp__meta-ads__list_creatives, mcp__meta-ads__get_creative_performance, mcp__meta-ads__analyze_account_creatives, mcp__meta-ads__preview_ad
---

# Creative Audit

Categorize all active ads by format, concept, and angle. Cross-reference with performance data to identify creative gaps and build a testing roadmap. Complements `creative-fatigue` (which focuses on lifecycle) by focusing on creative diversity and mix.

## Account Context

Read `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md` at the start of every run.
If it exists:
- Use known account IDs.
- Apply KPI targets for performance benchmarking.
- Note active creative tests — highlight them in the matrix.
- Check watch list for creative-related items from prior sessions.
If it doesn't exist, fall back to discovery and suggest running `platform-setup`.

## Classification Dimensions

### Format
| Format | Description | Key Metric |
|--------|-------------|-----------|
| Static Image | Single image ad | CTR, CPA |
| Video (Short) | <15 seconds | Hook Rate, ThruPlay Rate |
| Video (Long) | 15-60 seconds | Hold Rate, ThruPlay Rate |
| Carousel | Multi-card swipeable | Card CTR, CPA |
| Collection | Instant Experience catalog | Browse time, CPA |
| Dynamic Product Ad (DPA) | Auto-generated from catalog | ROAS, CPA |
| Instant Experience | Full-screen mobile | Browse time, CTR |

### Concept
| Concept | Description |
|---------|-------------|
| Testimonial | Customer quote, review, or case study |
| UGC (User-Generated Content) | Authentic, non-polished content |
| Product Demo | Feature walkthrough or how-to |
| Lifestyle | Product in context, aspirational |
| Pain Point | Problem-focused, agitation |
| Social Proof | Numbers, awards, press mentions |
| Offer/Promo | Discount, free trial, limited time |
| Educational | Teaching, tips, industry knowledge |
| Behind-the-Scenes | Company culture, process |
| Comparison | vs. competitor or alternative |

### Angle
| Angle | Description |
|-------|-------------|
| Benefit-led | "You'll get X" |
| Pain-led | "Tired of X?" |
| Social proof | "10,000 customers..." |
| Urgency | "Limited time", "Last chance" |
| Curiosity | "The secret to...", "Why X works" |
| Authority | "Experts recommend...", "Award-winning" |

## Workflow

### Phase 1: Pull creative data

1. Use `mcp__meta-ads__list_ads` to get all active ads across campaigns.
2. Use `mcp__meta-ads__list_creatives` to get creative asset details.
3. Use `mcp__meta-ads__preview_ad` for ads where format/concept is ambiguous.
4. Use `mcp__meta-ads__get_creative_performance` for performance metrics.
5. Use `mcp__meta-ads__analyze_account_creatives` for account-level creative health.

**Parallelization:** If the account has more than 5 active ad sets, consider spawning the `creative-analyst` subagent (see `agents/creative-analyst.md`) for parallel analysis.

### Phase 2: Categorize each ad

For each active ad:
1. Identify **Format** from ad metadata (image, video, carousel, etc.).
2. Classify **Concept** from creative content (may require `preview_ad` for context).
3. Classify **Angle** from primary text and headline.
4. Record performance metrics alongside classification.

### Phase 3: Build creative matrix

Create a Format x Concept matrix showing:
- Count of active ads in each cell.
- Average performance (CTR, CPA) per cell.
- Highlight empty cells as gaps.
- Highlight high-performing cells as winning combinations.

### Phase 4: Gap analysis

Identify missing creative combinations:
- Formats never tested (e.g., no video, no carousel).
- Concepts never tested (e.g., no UGC, no testimonial).
- Angles never tested (e.g., no pain-led, no curiosity).
- Winning format + losing concept combinations (format works, need new concepts).

### Phase 5: Testing roadmap

Prioritize gaps by:
1. **Format gaps** with strong cross-industry benchmarks (e.g., video typically 20-30% lower CPA than static).
2. **Concept gaps** where competitors are active (if competitor-research data available).
3. **Angle variety** — low-risk tests to diversify messaging.

## Output Format

```markdown
## Creative Audit - [Date]

### Account: [Name] (act_XXXXXXXXX)

### Active Creative Summary
| Metric | Count |
|--------|------:|
| Total Active Ads | |
| Unique Formats | |
| Unique Concepts | |
| Avg Ads per Ad Set | |

### Creative Matrix: Format x Concept
| | Testimonial | UGC | Product Demo | Lifestyle | Pain Point | Social Proof | Offer | Educational |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Static Image | | | | | | | | |
| Video (Short) | | | | | | | | |
| Video (Long) | | | | | | | | |
| Carousel | | | | | | | | |
| DPA | | | | | | | | |

*Cell = count of active ads. Green = above-avg CPA. Red = below-avg CPA. Empty = gap.*

### Performance Heatmap: Avg CPA by Format x Concept
| | Testimonial | UGC | Product Demo | Lifestyle | Pain Point | Social Proof | Offer |
|---|---:|---:|---:|---:|---:|---:|---:|
| Static Image | $ | $ | $ | $ | $ | $ | $ |
| Video (Short) | $ | $ | $ | $ | $ | $ | $ |
| Carousel | $ | $ | $ | $ | $ | $ | $ |

### Top Performing Combinations
| Rank | Format | Concept | Angle | Avg CPA | Avg CTR | Active Ads | 30d Spend |
|:-----|--------|---------|-------|--------:|--------:|-----------:|----------:|
| 1 | | | | | | | |

### Creative Gaps (Missing or Undertested)
| Gap | Type | Why Test | Priority | Benchmark CPA |
|-----|------|----------|:---------|:--------------|
| No video ads | Format | Video typically 20-30% lower CPA | HIGH | |
| No UGC | Concept | Fastest-growing format on Meta | HIGH | |
| No testimonials | Concept | Highest trust signal | MEDIUM | |
| Single angle across all ads | Angle | Message fatigue risk | MEDIUM | |

### Testing Roadmap
| Priority | Test | Format | Concept | Angle | Budget | Duration | Success Metric |
|:---------|------|--------|---------|-------|-------:|----------|:---------------|
| 1 | | | | | $ | 7-14d | CPA < $X |
| 2 | | | | | $ | 7-14d | CPA < $X |
| 3 | | | | | $ | 7-14d | CTR > X% |

### Implementation
For each test:
- Meta Ads Manager > Campaign "[Name]" > Ad Set "[Name]" > Ads > Create Ad
- Use existing ad set targeting — isolate creative as the variable.
- Run for minimum 7 days or 50 conversions before evaluating.
```

## Guardrails

- **Read-only:** This skill produces analysis only. Testing roadmap actions include UI paths.
- **Classification limits:** AI classification of concept/angle from ad preview is approximate. Flag confidence level when ambiguous.
- **Minimum data:** Require 7+ days and $50+ spend per ad for performance comparisons. Newer ads go into "Insufficient Data" bucket.
- **Cross-platform context:** If user runs ads on Google/Bing too, note that creative learnings may transfer (video hooks, messaging angles) but format performance is platform-specific.

## Profile Maintenance

After completing analysis, if `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md` exists:
1. Note any creative gaps identified in Watch List.
2. If user commits to testing roadmap items, add to Active Tests.
3. Update "Last updated" date.
Present proposed profile changes to the user before writing.

## References

- `references/benchmarks.md` — 2026 Meta benchmarks by format and objective
- `references/ui-paths.md` — Meta Ads Manager UI paths for creating ads
