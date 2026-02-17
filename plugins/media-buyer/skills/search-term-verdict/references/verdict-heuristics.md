# Verdict Heuristics

Use these heuristics when classifying search terms into `NEGATE`, `PROMOTE`,
`INVESTIGATE`, or `KEEP`.

## Priority order

1. Conversion and CPA signal.
2. Semantic relevance to campaign intent.
3. Match type drift severity.
4. Term status (`EXCLUDED` means already handled).
5. Volume and spend significance.

## Decision guidance

## `NEGATE`

Typical signals:

- Spend above threshold with zero conversions. Default: use the campaign's average
  CPA as the NEGATE spend floor (e.g., if avg CPA is $40, any term spending $40+ with
  zero conversions qualifies). When no CPA is available, fall back to $25-$50.
- Clear intent mismatch: jobs, free, DIY, used, tutorial, reviews, competitor-only,
  or informational queries when campaign objective is transactional.
- Location mismatch when campaign targets a different geography.

Preferred negative level:

- Ad group level when mismatch is tightly scoped.
- Campaign level when mismatch applies broadly.
- For universal exclusions (e.g., "jobs", "free"), recommend the user add terms to a
  shared negative keyword list via Google Ads UI. `add_negative_keywords()` supports
  campaign and ad group levels only.

## `PROMOTE`

Typical signals:

- Strong conversion volume/value but term is not a managed keyword theme.
- High commercial intent with repeat conversions.
- Term appears across multiple ad groups and should be centralized.

Recommend exact/phrase variants and target ad group placement.

## `INVESTIGATE`

Use when signal conflicts:

- Moderate spend, low volume, no conversions yet.
- Ambiguous intent that may represent top-of-funnel discovery.
- Branded or partner terms with unclear strategic value.

Provide a short question for user resolution.

## `KEEP`

Use when relevance and efficiency are acceptable relative to account goals.

## False-positive protections

Before finalizing negatives:

- Compare proposed negatives with top converting keywords to avoid blocking winners.
- Check plural/singular and close-variant collisions.
- Avoid over-broad single-word negatives unless account-level policy supports them.

## N-gram assist

When search term volume is high:

1. Build 2-gram and 3-gram frequency tables.
2. Rank grams by total spend and zero-conversion spend.
3. Use high-cost recurring grams to accelerate negative mining candidates.

N-gram output should inform suggestions, not replace row-level judgment.
