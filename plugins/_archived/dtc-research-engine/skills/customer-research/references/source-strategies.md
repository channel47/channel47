# Source-Specific Fetching Strategies — TESTED & VERIFIED

This document contains URL patterns and strategies that have been verified to work with WebFetch. Pay close attention to which sources work directly vs. which require indirect approaches.

## Source Reliability Tier List

### Tier 1: Direct Fetch Works Reliably
These sources return actual customer content when fetched directly:

- **Trustpilot** — `trustpilot.com/review/[company-domain.com]` — Returns review text, star ratings, customer quotes directly. This is your single most reliable source of real customer language.
- **Niche forums** (non-JS-heavy) — e.g., QuiltingBoard, HomesteadingToday, CleaningTalk, breed-specific pet forums. Many smaller forums render server-side and return full post content.
- **Some review aggregators** — ConsumerAffairs, BBB complaint pages, SiteJabber

### Tier 2: WebSearch Is Your Primary Tool
These sources block direct WebFetch but are deeply indexed by search engines:

- **Reddit** — Both `old.reddit.com` and `www.reddit.com` are blocked by WebFetch. Use WebSearch with queries like `reddit [product] review` or `[product] worth it reddit`. Search snippets often contain the most valuable quotes. Also look for third-party sites that aggregate Reddit discussions (e.g., articles titled "Reddit's Best [Product] Recommendations").
- **Amazon** — Direct Amazon review page fetches are blocked (returns 404 or CAPTCHA). Use WebSearch with queries like `amazon reviews [product] "game changer" OR "waste of money"`. The search results often include review snippets with exact customer language.
- **Quora** — Returns 403 on direct fetch. Use WebSearch to find Quora threads — search snippets contain answer previews.

### Tier 3: Indirect Access Only
These sources require creative approaches:

- **YouTube comments** — Comments load dynamically, but video pages sometimes return descriptions. Better to search for "[product] review youtube" and fetch the review articles/blogs that reference YouTube content.
- **Facebook groups** — Completely inaccessible. Search for articles/blogs that quote Facebook group discussions.
- **Walmart reviews** — Returns CAPTCHA. Use WebSearch for Walmart review snippets.

---

## Detailed Platform Strategies

### Trustpilot (HIGHEST PRIORITY — always try first)

**URL Pattern:** `https://www.trustpilot.com/review/[company-domain.com]`

Examples:
- `trustpilot.com/review/barxbuddy.com`
- `trustpilot.com/review/blueland.com`
- `trustpilot.com/review/audien.com`

**What You Get:** Star ratings, review counts, exact customer quotes, complaint categories, and praise language. Reviews often include detailed stories about customer service experiences, product failures, and emotional reactions.

**Strategy:**
1. Identify the top 2-4 competitor/brand domains in the product category
2. Fetch each Trustpilot page directly
3. Extract: exact quotes, star distribution, common complaint themes, praise patterns

**Finding the right domain:** If you don't know the exact domain, use WebSearch: `trustpilot [brand name]` or `trustpilot [product category]`

### Reddit (via WebSearch — cannot fetch directly)

**Reddit is blocked by WebFetch.** Do not waste time trying `old.reddit.com` or `www.reddit.com` URLs.

**WebSearch Strategies That Work:**

Search queries that surface Reddit content with customer quotes in the snippets:
- `reddit [product category] recommendation`
- `reddit [product] "worth it" OR "don't buy" OR "game changer"`
- `reddit [product category] "I finally" OR "I've tried everything"`
- `reddit best [product category] 2024 OR 2025 OR 2026`
- `[product] review reddit complaints`

**Also search for Reddit aggregation articles:**
- `"reddit recommends" [product category]`
- `"according to reddit" [product]`
- `"redditors say" [product category]`
These articles from publications like BuzzFeed, Wirecutter, and niche blogs often quote Reddit posts verbatim — and those articles ARE fetchable.

**What to extract from search results:**
- Quoted text in search snippets (often the most upvoted/emotional quotes)
- Thread titles (reveal the most common questions and frustrations)
- Subreddit names (reveal which communities care about this topic)

### Amazon (via WebSearch — cannot fetch directly)

**Amazon review pages return 404 or blocked responses.** Do not attempt direct Amazon fetches.

**WebSearch Strategies That Work:**

Use search queries that include emotional customer language to surface the richest review snippets:
- `amazon reviews [product name] "I bought" OR "doesn't work" OR "waste of money"`
- `amazon reviews [product category] "game changer" OR "finally found" OR "changed my life"`
- `amazon [product] review "I've tried everything" OR "last resort"`
- `"amazon verified purchase" [product] review`
- `amazon [product] one star review complaints`

**Also try:**
- `[product name] amazon review site:wirecutter.com OR site:nytimes.com` — These sites often quote Amazon reviews in their articles and are fetchable.
- `best [product category] amazon 2025 OR 2026` — Roundup articles often include Amazon review excerpts

### Forums (Direct Fetch — test each one)

Forums are hit-or-miss. Some render content server-side (fetchable), others use JavaScript frameworks (blocked).

**Forums That Tend to Work:**
- QuiltingBoard.com (HomesteadingToday.com) — Older forum software, renders fully
- CleaningTalk.com — Sometimes returns JS, sometimes content. Try and see.
- HearingTracker.com — Review/discussion site for hearing devices, good data
- Breed-specific pet forums — Many use older forum software (vBulletin, phpBB)

**Forums That Usually Don't Work:**
- Most Reddit-style platforms (Lemmy, etc.)
- Facebook Groups (completely blocked)
- Modern forums using React/Vue (return empty content)

**Strategy:** WebSearch for `[product category] forum discussion` → try fetching the top 3-4 results → keep what works, skip what doesn't. Budget 60 seconds max per forum attempt.

### Chewy.com (Pet Products)

**Rate-limited but sometimes works.** URL pattern: `chewy.com/[product-name]/product-reviews/[id]`

If it returns 429, move on. Don't retry.

### ConsumerAffairs / BBB / SiteJabber

**Often fetchable** and contain detailed complaint narratives:
- `consumeraffairs.com/[product-or-company]`
- `bbb.org/us/[state]/[city]/profile/[category]/[company]`
- `sitejabber.com/reviews/[domain]`

These skew heavily negative (people come here to complain), which is actually valuable for finding objections, fears, and pain points.

---

## Critical WebSearch Tips

WebSearch is your most versatile tool. Use it aggressively:

1. **Use emotional language in queries** — Searching for `"I was skeptical" [product]` surfaces more genuine customer language than `[product] review`
2. **Use OR operators** — `"game changer" OR "changed my life" OR "finally found"` in one query surfaces multiple quote styles
3. **Target specific platforms via query text** — `reddit [query]` or `amazon review [query]` reliably surfaces those platforms in results even though you can't fetch them directly
4. **Do multiple searches per product** — Don't rely on a single search query. Run 4-6 different queries targeting different angles: pain-focused, praise-focused, comparison-focused, objection-focused
5. **Fetch articles that reference reviews** — Publications like Wirecutter, BuzzFeed, Tom's Guide, Dogster, etc. quote real customer reviews and are fetchable

---

## Source Coverage Checklist

For every research project, aim to hit data from at least 4 of these 6 source types:

1. [ ] **Trustpilot** (direct fetch) — brand-specific reviews
2. [ ] **Reddit** (via WebSearch) — unfiltered discussion
3. [ ] **Amazon** (via WebSearch) — high-volume review data
4. [ ] **Forums** (direct fetch where possible) — detailed stories
5. [ ] **Review articles** (fetch) — curated customer quotes from multiple sources
6. [ ] **Complaint sites** (direct fetch) — ConsumerAffairs, BBB, SiteJabber

If you can only access 2-3 source types despite trying, note which sources were inaccessible in the research output.
