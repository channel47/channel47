---
name: competitor-research
description: >-
  This skill should be used when the user asks about "competitor ads",
  "what are competitors running", "Meta Ad Library", "Facebook Ad Library",
  "competitor creative research", "spy on competitor ads", "competitive
  analysis", "competitor benchmarks", "how do I compare to competitors",
  "competitor Facebook ads", "Ad Library lookup",
  "what ads are my competitors running",
  "I have no idea what competitors are doing",
  or mentions competitive intelligence, ad library research,
  competitor creative analysis, or competitive benchmarking for Meta Ads.
allowed-tools: mcp__meta-ads__get_ad_accounts, mcp__meta-ads__get_meta_api_reference
---

# Competitor Research

Light competitive intelligence combining own-account performance benchmarking with Meta Ad Library research guidance. Phase 1: manual Ad Library guidance + own account vs. industry benchmarks. References trypeggy/facebook-ads-library-mcp as a companion MCP for deeper automated competitor research.

## Account Context

Read `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md` at the start of every run.
If it exists:
- Use known account IDs for own-account benchmarking.
- Apply KPI targets as baseline for competitive comparison.
- Check preferences for known competitors or industry vertical.
If it doesn't exist, suggest running `platform-setup` first.

## Phase 1 Capabilities (Current)

### Own Account vs. Industry Benchmarks

Compare the user's account metrics against 2026 Meta benchmarks from `references/benchmarks.md`:
- CPM by objective (Traffic, Conversions, Lead Gen, etc.).
- CTR by placement (Feed, Stories, Reels, etc.).
- Video metrics (Hook Rate, ThruPlay Rate) by vertical.
- Frequency benchmarks by campaign type.
- CPA ranges by vertical and objective.

### Meta Ad Library Guidance

Guide the user through manual competitive research:

1. **Access the Ad Library:**
   - URL: https://www.facebook.com/ads/library
   - No login required — publicly accessible.

2. **Search for competitors:**
   - Search by page name, keyword, or advertiser name.
   - Filter by: Country, Platform (Facebook/Instagram), Media Type (Image/Video/Carousel), Active Status.

3. **What to look for:**
   - **Ad count:** How many active ads? (More ads = more testing, likely more sophisticated).
   - **Format mix:** What % video vs. image vs. carousel?
   - **Creative themes:** What concepts dominate (UGC, testimonial, demo, lifestyle)?
   - **Hook patterns:** For video ads, what are the first 3 seconds showing?
   - **Copy patterns:** What angles, CTAs, offers appear most frequently?
   - **Landing page patterns:** Where are ads driving? (Product page, lead form, quiz, etc.)
   - **Ad longevity:** How long have their ads been running? (Long-running = likely performing well.)
   - **Seasonal patterns:** Are they ramping up/down creative for seasons?

4. **Competitive creative categorization:**
   Use the same Format x Concept x Angle framework from `creative-audit`:
   - **Format:** Image, Video (Short/Long), Carousel, Collection, DPA.
   - **Concept:** Testimonial, UGC, Product Demo, Lifestyle, Pain Point, Social Proof, Offer, Educational.
   - **Angle:** Benefit-led, Pain-led, Social proof, Urgency, Curiosity, Authority.

## Workflow

### Phase 1: Own account benchmarking

1. Ask the user for their industry vertical (if not in profile).
2. Pull account-level metrics using `mcp__meta-ads__get_ad_accounts`.
3. Use `mcp__meta-ads__get_meta_api_reference` for API documentation if needed.
4. Compare against benchmarks from `references/benchmarks.md`.

### Phase 2: Competitor identification

Ask the user:
- Who are your top 3-5 competitors on Meta?
- What are their Facebook page names? (Needed for Ad Library search.)
- Any specific competitors you want to analyze?

### Phase 3: Ad Library research guidance

Provide step-by-step guidance for researching each competitor in the Ad Library. For each competitor:
1. Search URL: `https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=[competitor_name]`
2. Walk through the analysis framework (format, concept, angle, longevity).
3. Ask the user to report findings back for synthesis.

### Phase 4: Synthesis

Combine own-account benchmarking with competitor findings to produce:
- Performance gaps (where user is below benchmarks AND competitors are doing something different).
- Creative inspiration (competitor creative concepts not yet tested by user).
- Differentiation opportunities (formats/concepts competitors are NOT using).
- Testing priorities based on competitive gaps.

## Output Format

```markdown
## Competitor Research - [Date]

### Account: [Name] (act_XXXXXXXXX)

### Own Account vs. Industry Benchmarks
| Metric | Your Account | Industry Avg | Percentile | Assessment |
|--------|------------:|------------:|:-----------|:-----------|
| CPM | $ | $ | | |
| CTR | % | % | | |
| CPA | $ | $ | | |
| ROAS | | | | |
| Frequency (7d) | | | | |
| Video Hook Rate | % | % | | |

### Competitor Overview
| Competitor | Active Ads | Top Format | Top Concept | Longest Running Ad | Notes |
|-----------|----------:|:----------|:-----------|:-------------------|:------|
| | | | | | |

### Competitor Creative Matrix
| | [Competitor A] | [Competitor B] | [Competitor C] | Your Account |
|---|---:|---:|---:|---:|
| Static Image | | | | |
| Video (Short) | | | | |
| Video (Long) | | | | |
| Carousel | | | | |

### Competitive Gaps
| Gap | Competitors Doing | You're Not | Impact | Priority |
|-----|:-----------------|:-----------|:-------|:---------|
| | Video testimonials | No video testimonials | Missing high-trust format | HIGH |
| | UGC-style content | Polished creative only | Missing authenticity angle | MEDIUM |

### Testing Recommendations (Inspired by Competitors)
| Priority | Test | Inspired By | Format | Concept | Effort |
|:---------|------|:-----------|:-------|:--------|:-------|
| 1 | | [Competitor]'s long-running ad | | | |
| 2 | | Industry trend across competitors | | | |

### Ad Library Research URLs
| Competitor | Ad Library URL |
|-----------|:--------------|
| [Name] | https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=[name] |
```

## Companion MCP for Deeper Research

For automated Ad Library queries (scraping competitor ads at scale), consider adding the
[trypeggy/facebook-ads-library-mcp](https://github.com/trypeggy/facebook-ads-library-mcp) as a companion MCP.
This is NOT bundled with the meta-ads plugin but can be added to your `.mcp.json` for deeper competitor research.

The `competitor-scout` subagent (see `agents/competitor-scout.md`) is designed to orchestrate
multi-competitor analysis when this companion MCP is available.

## Guardrails

- **Read-only:** This skill produces analysis and research guidance only.
- **Benchmark accuracy:** Industry benchmarks are directional, not definitive. Account-specific history always takes precedence.
- **Ad Library limitations:** The Meta Ad Library shows active and recently inactive ads. Historical ad data beyond ~90 days may not be available. Ad spend/performance data is NOT available in the Ad Library.
- **Privacy:** Do not attempt to reverse-engineer competitor targeting, budgets, or performance. Focus on publicly visible creative.
- **Competitor identification:** If the user is unsure who their competitors are on Meta, suggest searching industry keywords in the Ad Library.

## Profile Maintenance

After completing analysis, if `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md` exists:
1. Note key competitive findings in Watch List.
2. If user commits to competitive tests, add to Active Tests.
3. Update "Last updated" date.
Present proposed profile changes to the user before writing.

## References

- `references/benchmarks.md` — 2026 Meta benchmarks by objective and vertical
- `references/ui-paths.md` — Meta Ads Manager UI paths
