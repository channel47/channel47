# Source Strategies — Platform Access & Workarounds

## Platform Access Tiers

### Tier 1: Direct Access Works
These sources return customer content when fetched directly:

- **Trustpilot** — `trustpilot.com/review/[company-domain.com]` — Star ratings, review counts, exact customer quotes. Single most reliable source of verbatim customer language.
- **ConsumerAffairs** — `consumeraffairs.com/[product-or-company]` — Detailed complaint narratives. Skews negative, which is valuable for objections and fears.
- **SiteJabber** — `sitejabber.com/reviews/[domain]` — Similar to Trustpilot, sometimes different brands listed.
- **BBB** — `bbb.org/us/[state]/[city]/profile/[category]/[company]` — Formal complaints with resolution details.
- **Niche forums** — Older forum software (vBulletin, phpBB) often renders server-side. Test each one — if it returns content, extract everything. If it returns JavaScript/empty, skip immediately.
- **Review aggregation articles** — Wirecutter, BuzzFeed, Tom's Guide, Dogster, etc. These often quote Reddit and Amazon reviews verbatim. They're your backdoor to blocked platforms.

### Tier 2: Blocked — Requires Browser Automation or Search
These platforms actively block scrapers and bots:

- **Reddit** — Both `reddit.com` and `old.reddit.com` block automated access (429 errors). Two approaches:
  - **Browser automation** (Playwright, Browserbase) — renders the page in a real browser, bypasses bot detection. Best for getting full thread content.
  - **Google search** with `site:reddit.com` — surfaces relevant threads and often includes the most upvoted quotes in snippets.
- **Amazon** — Returns 404 or CAPTCHA on automated access. Same two approaches:
  - **Browser automation** — can access review pages directly.
  - **Google search** with `site:amazon.com` + emotional language queries to surface review snippets.
- **Quora** — Returns 403 on direct fetch. Browser automation or `site:quora.com` Google searches.
- **Walmart** — Returns CAPTCHA. Browser automation or search snippets.

### Tier 3: Indirect Access Only
- **YouTube comments** — Load dynamically, hard to extract even with browser tools. Search for review articles that reference YouTube content instead.
- **Facebook groups** — Completely inaccessible. Search for articles/blogs that quote group discussions.

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

If a source fails, note it and move on. Don't spend more than a minute retrying a blocked source.
