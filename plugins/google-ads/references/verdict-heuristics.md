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
  shared negative keyword list via Google Ads UI:
  `Google Ads > Tools & Settings > Shared Library > Negative keyword lists`

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

Before finalizing any NEGATE verdict, apply these checks to avoid blocking
queries that are actually valuable. False negatives (missing a bad term) cost
money gradually; false positives (blocking a good term) kill revenue immediately.

### 1. Positive keyword collision check

Compare every proposed negative against the account's actively converting keywords:

- Extract all keywords with conversions > 0 in the analysis window.
- For each proposed PHRASE negative, check if any converting keyword contains
  that phrase as a substring. Example: negating `"blue shoes"` would block the
  converting keyword `blue shoes for women`.
- For each proposed EXACT negative, check for exact overlap with converting keywords.
- If a collision is found: change verdict to INVESTIGATE and note the conflicting
  keyword, its CPA, and conversion count. Let the user decide.

### 2. Close variant and plural/singular awareness

Google's close variant matching means negatives can block more than the literal text:

- Before recommending `"running shoe"` as a negative, verify that `"running shoes"`
  (plural) is not a high-performing keyword. Google may treat the negative as blocking
  both forms.
- Check for common close variants: singular/plural, verb tenses (run/running),
  spelling variants (color/colour), abbreviations (apt/apartment).
- When in doubt about close variant reach, recommend EXACT match negatives rather
  than PHRASE to limit blast radius.

### 3. Branded term handling

Branded terms require special care — never auto-NEGATE:

- **Own brand terms:** Always KEEP or INVESTIGATE. Even if a branded term has zero
  conversions in the analysis window, it may serve a navigation or brand protection
  function. Flag for user review with context.
- **Competitor brand terms:** Default to INVESTIGATE, not NEGATE. Some accounts
  intentionally bid on competitor terms (conquest strategy). Check if the campaign
  or ad group name suggests competitive targeting intent. If so, classify as KEEP
  unless performance is clearly poor (>3x CPA with meaningful spend).
- **Partner/reseller brand terms:** INVESTIGATE. Terms containing partner or reseller
  names may be valuable for co-marketing or channel partnerships. Flag with context.
- **Misspelled brand terms:** If a term is a misspelling of the advertiser's own brand
  (e.g., "nikee" for "Nike"), keep it — Google's close variants should handle the match,
  and these queries have strong brand intent.

### 4. Statistical significance guard

Do not NEGATE terms that lack sufficient data for a confident verdict:

- **Minimum data threshold:** 5+ clicks AND $10+ spend. Below this, default to KEEP
  unless semantic mismatch is unambiguous (e.g., "jobs hiring near me" on a product
  purchase campaign).
- **CPA-based threshold:** Use the campaign's average CPA as the spend floor. A term
  must have spent at least 1x campaign CPA with zero conversions before NEGATE is
  appropriate. A term at 0.3x CPA has not had enough opportunity to convert.
- **Impression-only terms:** Terms with impressions but zero clicks are not waste —
  they don't cost money. Do not NEGATE based on impressions alone.

### 5. Conversion lag awareness

Google Ads conversions can take days to attribute, especially with longer
conversion windows (7-day click, 30-day click):

- **Recent click buffer:** If a search term's most recent click was within the last
  3 days, do NOT assign NEGATE even if current conversions = 0. Assign INVESTIGATE
  with note: "Recent clicks may not yet have attributed conversions. Re-evaluate
  in 3-5 days."
- **Long conversion windows:** For accounts using 30-day or 90-day click attribution
  windows, extend the buffer. Terms with clicks in the last 7 days should be
  INVESTIGATE, not NEGATE.
- **View-through conversions:** If the account tracks view-through conversions, note
  that some terms may contribute to conversions that aren't attributed to the click.
  This is context for INVESTIGATE verdicts, not a reason to override NEGATE.

### 6. Cross-campaign cannibalization check

A search term may appear in multiple campaigns with different performance:

- **Converting elsewhere:** If a term has zero conversions in Campaign A but converts
  in Campaign B, it's a cannibalization issue, not a negative keyword issue. Assign
  INVESTIGATE with note: "This term converts in [Campaign B] at $X CPA. Consider
  adding as exact match negative in [Campaign A] to force traffic to [Campaign B]."
- **Different match types:** If broad match in Campaign A triggers a term that exact
  match in Campaign B already handles, this is a sculpting opportunity. Recommend
  adding the exact match term as a negative in the broad campaign.
- **Budget competition:** Multiple campaigns bidding on the same term inflates CPC
  through internal competition. Flag this in INVESTIGATE notes.

### 7. Seasonal and temporal awareness

Performance varies by time of year — a term that looks wasteful now may convert seasonally:

- **Seasonal products:** For accounts selling seasonal goods (holiday gifts, summer
  outdoor gear, tax software), check if the analysis window overlaps with off-season.
  Terms like "christmas gifts" in January should be INVESTIGATE with note:
  "Seasonal term — re-evaluate during peak season."
- **Day-of-week patterns:** Some B2B terms only convert on weekdays. If the analysis
  window is skewed (e.g., includes a holiday week), note this context.
- **New campaigns:** Campaigns running for less than 14 days don't have enough data
  for confident NEGATE verdicts on most terms. Extend the analysis window or assign
  INVESTIGATE with a review date.

### 8. Over-broad negative risks

Single-word negatives and very short phrase negatives are dangerous:

- **Never recommend single-word PHRASE negatives** unless the word is unambiguously
  irrelevant across all conceivable search contexts for this account. Examples where
  single-word PHRASE negatives are safe: "jobs", "salary", "porn". Examples where
  they are NOT safe: "cheap" (might block "cheap flights" for a budget airline),
  "reviews" (might block "product reviews" for a review site).
- **Two-word negatives:** Acceptable for clear intent mismatches. But verify no
  converting queries contain the phrase as a substring.
- **Prefer EXACT over PHRASE** when the mismatch is query-specific rather than
  theme-wide. EXACT negatives have zero collateral damage risk.

### 9. Match type drift classification

When broad match expands far beyond the seed keyword:

- **0-word overlap:** The search term shares zero words with the triggering keyword.
  This is maximum drift. If the term also has zero conversions, it's a strong NEGATE
  candidate. But check if the intent is related even without word overlap (e.g.,
  keyword "plumber" triggering "fix leaky faucet" — related intent, just different words).
- **Partial overlap with intent preservation:** The term shares some words and the
  intent is aligned. This is expected broad match behavior. Only NEGATE if performance
  is poor AND intent is mismatched.
- **Close variant drift:** Google's close variant matching triggers exact/phrase
  keywords for terms that are conceptually related but literally different. If the
  close variant is relevant, KEEP. If it's a stretch, INVESTIGATE.

## N-gram assist

When search term volume is high:

1. Build 2-gram and 3-gram frequency tables.
2. Rank grams by total spend and zero-conversion spend.
3. Use high-cost recurring grams to accelerate negative mining candidates.
4. Cross-reference top n-grams against the false-positive protections above —
   especially the positive keyword collision check and over-broad negative risks.

N-gram output should inform suggestions, not replace row-level judgment.

### N-gram interpretation guidelines

- **High-frequency, high-waste n-grams** (e.g., "near me" with $500+ zero-conv spend
  across 50 terms): Strong signal for a PHRASE negative at campaign or shared list level.
  But verify that no converting queries contain the n-gram.
- **High-frequency, mixed-performance n-grams** (e.g., "best" appears in both converting
  and non-converting terms): Do NOT use as a negative. The n-gram itself is neutral —
  the waste comes from specific combinations. Negate at the term level, not the n-gram level.
- **Low-frequency, high-spend n-grams** (e.g., one term with a specific 3-gram spent $200):
  This is a single-term issue, not an n-gram pattern. Handle at the row level.
