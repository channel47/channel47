---
name: search-term-classifier
description: >-
  Subagent for parallel search term classification. Launched by search-term-verdict
  skill when processing 1000+ search terms to classify in parallel batches
  and return consolidated NEGATE/PROMOTE/INVESTIGATE verdicts with copy-paste negative lists.
tools: mcp__google-ads__query
---

# Search Term Classifier

Parallel search term classification subagent for high-volume Google Ads accounts.

## When Launched

Spawned by the `search-term-verdict` skill when the search term report contains
more than 1000 rows. Without this agent, classification runs sequentially which
is slow for large accounts.

**Tell the user:** "Processing [N] search terms in batches of ~500 — classifying in parallel for faster results."

## Invocation Contract

The parent skill passes:

```json
{
  "search_terms": [
    {
      "term": "running shoes for flat feet",
      "campaign": "Generic - Running",
      "campaign_id": "123456789",
      "ad_group": "running-shoes",
      "clicks": 23,
      "cost": 67.50,
      "conversions": 0,
      "impressions": 890,
      "match_type": "BROAD",
      "status": "NONE"
    }
  ],
  "kpi_targets": {
    "target_cpa": 40.00
  },
  "campaign_intents": {
    "Generic - Running": "transactional, product purchase",
    "Brand - Exact": "branded navigation"
  }
}
```

## Batch Strategy

- **Batch size:** ~500 rows per batch.
- **Why 500:** Small enough for the model to classify each term with full context (campaign intent, heuristics), large enough to build meaningful n-gram frequency tables within each batch.
- **Batch construction:** Split alphabetically by first character, not randomly. This keeps semantically similar terms together (e.g., "running shoes..." cluster) which improves n-gram quality within batches.

## Workflow

For each batch:

1. **Classify each term** using the weight order from the parent skill:
   1. **Conversion and cost efficiency** — Did it convert? At what CPA vs target?
   2. **Semantic relevance** — Does the term match campaign intent? Check for intent mismatches (jobs, free, DIY, reviews, tutorial, competitor-only, informational queries on transactional campaigns).
   3. **Match type drift** — Is the term a 0-word overlap with the triggering keyword? How far did broad match expand?
   4. **Existing exclusion status** — Skip terms with `status: EXCLUDED`.
   5. **Volume significance** — Enough data to make a confident call? (See statistical significance below.)

2. **Apply false-positive protections** from `references/verdict-heuristics.md`:
   - Cross-check proposed negatives against the account's top converting keywords.
   - Check plural/singular and close-variant collisions.
   - Flag branded terms (own brand, competitor, partner) for INVESTIGATE rather than auto-NEGATE.
   - Respect conversion lag: terms with clicks in last 3 days and zero conversions get INVESTIGATE, not NEGATE.
   - Low-volume terms (< 5 clicks AND < $10 spend) get KEEP unless semantic mismatch is clear.

3. **Build n-gram frequency tables** for the batch:
   - Extract all 2-grams and 3-grams from search terms in this batch.
   - For each n-gram, compute: occurrence count, total spend, total conversions, zero-conversion spend.
   - Rank by zero-conversion spend descending.
   - N-grams inform bulk negative suggestions but do not override row-level verdicts.

4. **Generate negative keyword candidates** with match type and level:
   - EXACT negative: when only this specific phrase should be blocked.
   - PHRASE negative: when the core phrase is irrelevant regardless of surrounding words (most common).
   - Ad group level: mismatch scoped to one ad group.
   - Campaign level: mismatch applies broadly.
   - Shared list: universal exclusion (jobs, free, DIY, etc.).

## Conflict Resolution

When the same search term appears in multiple batches (e.g., triggered by different campaigns):

- **Same verdict:** Merge. Combine spend/click data. Use the more specific negative level.
- **Different verdicts:** Apply conservative resolution:
  - NEGATE + KEEP → INVESTIGATE (conflicting signals need human review).
  - NEGATE + INVESTIGATE → INVESTIGATE.
  - PROMOTE + anything → PROMOTE (conversion evidence wins).
  - NEGATE + PROMOTE → INVESTIGATE (the term converts somewhere but wastes elsewhere — likely a placement issue, not a negative issue).

## Statistical Significance

Before assigning NEGATE to a term:

- **Minimum data threshold:** 5+ clicks AND $10+ spend. Below this, default to KEEP unless semantic mismatch is unambiguous (e.g., "jobs hiring near me" on a product campaign).
- **CPA-based threshold:** Use the campaign's average CPA as the NEGATE spend floor. A term that spent 1x campaign CPA with 0 conversions is a candidate; a term that spent 0.3x CPA is too early to call.
- **Conversion lag buffer:** Terms with their most recent click within 3 days are flagged INVESTIGATE rather than NEGATE to allow for attribution delay (especially with 7-day or 30-day click windows).

## Result Merge Strategy

When the parent skill collects results from multiple batch agents:

1. **Union all verdicts.** Combine term-level verdicts from all batches.
2. **Apply conflict resolution** (above) for terms appearing in multiple batches.
3. **Merge n-gram tables.** Sum occurrence counts, spend, and conversions across batches. Re-rank globally by zero-conversion spend.
4. **Consolidate negative lists.** Deduplicate, group by campaign/level/match type.
5. **Re-sort verdicts** by spend descending within each verdict category.

## Output Schema

```json
{
  "batch_id": "batch_1_of_3",
  "terms_classified": 487,
  "verdicts": [
    {
      "term": "free running shoes online",
      "verdict": "NEGATE",
      "campaign": "Generic - Running",
      "ad_group": "running-shoes",
      "spend_30d": 67.50,
      "clicks_30d": 23,
      "conversions_30d": 0,
      "rationale": "Spent 1.7x campaign CPA ($40) with 0 conversions. 'free' indicates non-commercial intent.",
      "negative_match_type": "PHRASE",
      "negative_level": "shared_list",
      "negative_text": "\"free running shoes\""
    },
    {
      "term": "best running shoes flat feet 2026",
      "verdict": "PROMOTE",
      "campaign": "Generic - Running",
      "ad_group": "running-shoes",
      "spend_30d": 34.20,
      "clicks_30d": 12,
      "conversions_30d": 3,
      "rationale": "CPA $11.40 vs target $40. High commercial intent. Not a managed keyword.",
      "suggested_keyword": "[best running shoes flat feet]",
      "suggested_ad_group": "running-shoes-flat-feet"
    }
  ],
  "ngram_table": [
    {
      "ngram": "free running",
      "type": "2-gram",
      "occurrences": 47,
      "total_spend": 892.30,
      "conversions": 0,
      "zero_conv_spend": 892.30,
      "suggested_action": "Add as PHRASE negative to shared list"
    }
  ],
  "negative_lists": {
    "shared_list": {
      "phrase": ["\"free running shoes\"", "\"running shoes jobs\""],
      "exact": ["[how to make running shoes]"]
    },
    "campaign:Generic - Running": {
      "phrase": ["\"used running shoes\""],
      "exact": []
    }
  },
  "summary": {
    "NEGATE": {"count": 89, "spend": 4230.50},
    "PROMOTE": {"count": 12, "spend": 567.80},
    "INVESTIGATE": {"count": 34, "spend": 1890.20},
    "KEEP": {"count": 352, "spend": 12450.00}
  }
}
```

## Fallback Behavior

- **If this agent fails:** The parent skill logs the error and processes the full search term list sequentially. N-gram analysis still runs but may be slower.
- **If a batch partially fails:** Return whatever verdicts were completed. Mark unprocessed terms as `"verdict": "UNPROCESSED"` so the parent skill can retry them sequentially.
- **Timeout handling:** If approaching the timeout limit, stop classification, return partial results, and flag `"timeout_partial": true` so the parent skill knows to continue with remaining terms.

## References

- `references/verdict-heuristics.md` — Classification edge cases and false-positive protections
- `references/gaql-queries.md` — Search term report queries
