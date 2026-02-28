# Plugin Improvement Research

**Date:** 2026-02-27
**Status:** Living document
**Scope:** paid-search, meta-ads, and universal cross-plugin improvements

---

## Meta Ads MCP — Build vs. Bundle

**Best existing option:** `brijr/meta-mcp` — MIT licensed, TypeScript, 25 tools, full CRUD + audience management. Leader (pipeboard, 536 stars) has BUSL license.

**Gaps in every existing server:** Conversions API/CAPI, Product Catalog/feed management, Lead Forms API, Advantage+ unified campaign API, Pixel management.

**Recommendation:** Fork `brijr/meta-mcp` as starting point for `@channel47/meta-ads-mcp`. Add CAPI + gaps above. Auth complexity (token lifecycle) is the main UX pain point — brijr handles automatic token refresh.

---

## New Skills for paid-search

| Priority | Skill | Tier | Why |
|----------|-------|------|-----|
| 1 | `bid-strategy-advisor` | 1 | Highest-leverage decision. Decision tree + GAQL data. |
| 2 | `conversion-audit` | 1 | Root cause fixer — 71% of accounts have bad tracking. |
| 3 | `rsa-grader` | 1 | Asset-level data now in GAQL. Low effort, high signal. |
| 4 | `budget-pacer` | 1 | Extends morning-brief. Cross-campaign reallocation. |
| 5 | `change-investigator` | 1 | "Why did CPA spike?" drill-down. `change_event` in GAQL. |
| 6 | `account-structure-audit` | 1 | Brand/non-brand separation, duplicate keywords, theme coherence. |
| 7 | `ngram-miner` | 2 | Extends search-term-verdict. Needs helper script. |

**Quick wins on existing skills:**
- `waste-detector`: Add industry benchmark comparison
- `morning-brief`: Add RSA health flag, conversion tracking health flag
- Reference data: Expand `benchmarks.md` with 2025-2026 industry benchmarks by vertical

---

## Universal Cross-Plugin Skills (potential `ad-toolkit` plugin)

| Priority | Skill | Impact | Feasibility |
|----------|-------|--------|-------------|
| 1 | `cross-platform-brief` | HIGH | MEDIUM |
| 2 | `ad-copy-generator` | HIGH | VERY HIGH |
| 3 | `budget-allocator` | VERY HIGH | MEDIUM |
| 4 | `utm-enforcer` | MEDIUM | VERY HIGH |
| 5 | `budget-pacer` (cross-platform) | MEDIUM-HIGH | HIGH |
| 6 | `ab-test-designer` | MEDIUM-HIGH | HIGH |
| 7 | `incrementality-advisor` | HIGH | HIGH |
| 8 | `ad-policy-checker` | MEDIUM | HIGH |

---

## MCP Server Improvements

| Priority | Improvement | Pattern Source |
|----------|-------------|----------------|
| 1 | Exponential backoff with jitter | brijr/meta-mcp |
| 2 | Tiered response caching (structure=1hr, metrics=5min, metadata=24hr) | 41x faster warm |
| 3 | Health check command | brijr pattern |
| 4 | `ENABLED_TOOLS` env var | xing5/mcp-google-sheets |
| 5 | CSV/JSON export tools | brijr pattern |
| 6 | Progress notifications for long reports | MCP spec |
| 7 | Debug mode via env var | Standard pattern |

---

## Complementary MCP Servers

| Server | Why | Best Option |
|--------|-----|-------------|
| Google Sheets | Export reports | `xing5/mcp-google-sheets` (19 tools) |
| Google Analytics | Conversion correlation | Official `googleanalytics/google-analytics-mcp` |
| Slack/Discord | Budget/anomaly alerting | `notifyme_mcp` (webhook-based) |
| Charts | Visual reports | `antvis/mcp-server-chart` (26+ types) |
| DataForSEO | Competitive intelligence | Already in `mcps/` |

---

## Competitive Landscape

- **AgriciDaniel/claude-ads**: 186 audit checks, weighted "Ads Health Score" — audit-focused, complementary
- **Adspirer (ads-mcp)**: 100+ tools across 4 platforms, single remote endpoint, `STRATEGY.md` persistence
- **OpenClaudia**: 56+ marketing skills — broad but shallow
- **Anthropic knowledge-work-plugins**: `performance-analytics` SKILL.md is gold-standard template

---

## Suggested Roadmap

**Phase 1:** Add 2-3 new paid-search skills (bid-strategy-advisor, conversion-audit, rsa-grader). Expand benchmarks.md.
**Phase 2:** Fork brijr/meta-mcp → @channel47/meta-ads-mcp. Add CAPI. Wire meta-ads skills.
**Phase 3:** Create ad-toolkit universal plugin (cross-platform-brief, ad-copy-generator, utm-enforcer).
**Phase 4:** MCP server hardening — backoff, caching, health checks, tool filtering.

---

## Sources

### Meta Ads MCP
- [pipeboard-co/meta-ads-mcp](https://github.com/pipeboard-co/meta-ads-mcp) — 536 stars, BUSL license, 29 tools
- [brijr/meta-mcp](https://github.com/brijr/meta-mcp) — 86 stars, MIT, TypeScript, 25 tools
- [gomarble-ai/facebook-ads-mcp-server](https://github.com/gomarble-ai/facebook-ads-mcp-server) — 238 stars, MIT, read-only
- [talknerdytome-labs/facebook-ads-library-mcp](https://github.com/talknerdytome-labs/facebook-ads-library-mcp) — competitor intel

### Paid Search
- [WordStream 2025 Benchmarks](https://www.wordstream.com/blog/2025-google-ads-benchmarks)
- [Adalysis N-Gram Analysis](https://adalysis.com/blog/n-gram-analysis-the-secret-to-scalable-search-term-management-in-google-ads/)
- [Google Ads Script Library](https://developers.google.com/google-ads/scripts/docs/solutions)
- [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) — 186 audit checks

### Universal Skills
- [Measured.com — Diminishing Returns / MMM](https://www.measured.com/faq/media-mix-modeling-diminishing-return-curves-mmm-budget-decision/)
- [Improvado — UTM Conventions](https://improvado.io/blog/utm-naming-conventions)
- [AdCreative.ai — Compliance Checker](https://www.adcreative.ai/post/introducing-compliance-checker-ai)

### MCP Patterns
- [philschmid.de MCP Best Practices](https://www.philschmid.de/mcp-best-practices)
- [MCP Spec — Pagination](https://modelcontextprotocol.io/specification/2025-03-26/server/utilities/pagination)
- [xing5/mcp-google-sheets](https://github.com/xing5/mcp-google-sheets) — tool filtering pattern
- [Adspirer ads-mcp](https://github.com/amekala/ads-mcp) — 100+ tools, STRATEGY.md pattern
