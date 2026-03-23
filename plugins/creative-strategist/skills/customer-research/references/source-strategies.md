# Source Strategies — Platform Access & Workarounds

## Platform Access Tiers

### Tier 1: Direct Access Works
These sources return customer content when fetched directly:

- **Trustpilot** — `trustpilot.com/review/[company-domain.com]` — Star ratings, review counts, exact customer quotes. Single most reliable source of verbatim customer language.
- **ConsumerAffairs** — `consumeraffairs.com/[product-or-company]` — Detailed complaint narratives. Skews negative, which is valuable for objections and fears.
- **SiteJabber** — `sitejabber.com/reviews/[domain]` — Similar to Trustpilot, sometimes different brands listed.
- **BBB** — `bbb.org/us/[state]/[city]/profile/[category]/[company]` — Formal complaints with resolution details.
- **Niche forums** — Older forum software (vBulletin, phpBB) often renders server-side. Test each one — if it returns content, extract everything. If it returns JavaScript/empty, escalate to browser tools.
- **Review aggregation articles** — Wirecutter, BuzzFeed, Tom's Guide, Dogster, etc. These often quote Reddit and Amazon reviews verbatim. They're your backdoor to blocked platforms.

### Tier 2: Blocked — Requires Browser Automation or Search
These platforms actively block scrapers and bots:

- **Reddit** — Both `reddit.com` and `old.reddit.com` block automated access (429 errors).
- **Amazon** — Returns 404 or CAPTCHA on automated access.
- **Quora** — Returns 403 on direct fetch.
- **Walmart** — Returns CAPTCHA.

### Tier 3: Indirect Access Only
- **YouTube comments** — Load dynamically, hard to extract even with browser tools. Search for review articles that reference YouTube content instead.
- **Facebook groups** — Completely inaccessible. Search for articles/blogs that quote group discussions.

## Fallback Chains — Never Give Up After One Failure

Every source has a fallback chain. Work through the chain in order. Only move on to the next source after the ENTIRE chain is exhausted.

### Trustpilot / ConsumerAffairs / SiteJabber / BBB
```
1. WebFetch (direct URL)
2. If 403/blocked → Browser automation (Playwright navigate + extract)
3. If no Playwright → Claude in Chrome (navigate to URL, read page)
4. If browser tools unavailable → WebSearch: site:trustpilot.com "[product]"
5. If search returns snippets → extract quotes from snippets
6. If nothing → WebSearch: "[product] trustpilot reviews" (articles quoting the platform)
```

### Reddit
```
1. WebFetch old.reddit.com thread URL (sometimes works, usually 429)
2. If blocked → Browser automation (Playwright navigate to thread)
3. If no Playwright → Claude in Chrome (navigate to Reddit thread, read page)
4. If browser tools unavailable → WebSearch: site:reddit.com "[product] [emotional phrase]"
5. Extract quotes from search snippets
6. WebSearch: "reddit recommends [product]" OR "according to reddit [product]" (articles quoting Reddit)
7. WebFetch those articles and extract quoted Reddit content
```

### Amazon
```
1. WebFetch Amazon review page (usually blocked)
2. If blocked → Browser automation (Playwright navigate to review page)
3. If no Playwright → Claude in Chrome (navigate to Amazon reviews, read page)
4. If browser tools unavailable → WebSearch: site:amazon.com "[product]" review "[emotional phrase]"
5. Extract quotes from search snippets
6. WebSearch: "[product] amazon review" site:wirecutter.com OR site:tomsguide.com (articles quoting Amazon reviews)
7. WebFetch those articles and extract quoted Amazon content
```

### Quora / Walmart / Other Blocked
```
1. WebFetch (direct URL — will likely fail)
2. If blocked → Browser automation (Playwright)
3. If no Playwright → Claude in Chrome
4. If browser tools unavailable → WebSearch: site:[platform] "[product]"
5. Extract from search snippets
```

### Niche Forums
```
1. WebFetch (direct URL — works for many older forums)
2. If empty/JS-only → Browser automation (Playwright)
3. If no Playwright → Claude in Chrome
4. If browser tools unavailable → WebSearch: site:[forum-url] "[product]"
```

### Key Rules
- **A 403 or CAPTCHA is not a dead end** — it means "try the next tool in the chain"
- **Browser automation tools (Playwright, Claude in Chrome) should be the second attempt on ANY blocked source**, not a last resort
- **Search snippets are always available** as a fallback, even if less context-rich
- **Review articles that quote blocked platforms** are a reliable final fallback — they often reproduce the best quotes verbatim
- **Log which step in the chain succeeded** so the source coverage log in the output reflects actual access method

## Search Query Patterns

When using Google search to discover content on blocked platforms, emotional language in queries surfaces the richest results:

**Pain-focused:** `site:reddit.com [product] "doesn't work" OR "waste of money" OR "I've tried everything"`
**Praise-focused:** `site:reddit.com [product] "game changer" OR "finally found" OR "changed my life"`
**Comparison:** `site:reddit.com best [product category] recommendation OR "vs"`
**Objection:** `site:reddit.com [product] "is it worth" OR "should I buy" OR "skeptical"`

Same patterns work for Amazon: `site:amazon.com [product] review "I bought" OR "doesn't work"`

**Aggregation article searches:**
- `"reddit recommends" [product category]`
- `"according to reddit" [product]`
- `[product] review site:wirecutter.com OR site:nytimes.com OR site:tomsguide.com`

## Source Coverage Checklist

For every research project, aim for data from at least 4 of these 6 source types:

1. **Review sites** (Trustpilot, ConsumerAffairs, SiteJabber) — direct access
2. **Reddit** — browser automation or search
3. **Amazon** — browser automation or search
4. **Niche forums** — direct access where possible
5. **Review articles** — direct access, often quote blocked platforms
6. **Complaint sites** (BBB, SiteJabber) — direct access

Never abandon a source after one failed tool — work through the full fallback chain above before moving on. The research is only as good as the variety and depth of sources that feed it.
