# Import Checklist — Microsoft Ads

Master checklist for post-Google-Ads-import cleanup. Used by the import-auditor skill.

## Why imports break things

Google Ads import is the most common way Microsoft Advertising accounts get created. But the import process has blind spots:

- MSAN gets enabled by default (Google has no equivalent network)
- Search partner settings default to enabled
- "People in or searching for" is the default location targeting
- Google shared negative keyword lists are platform-specific and don't transfer
- Smart Bidding strategies may not map 1:1 to Bing equivalents
- Ad scheduling is lost (imports default to 24/7)
- Device bid modifiers may not carry over correctly

## Checklist

### Critical (fix immediately)

| # | Check | Default After Import | Correct Setting | Impact |
|---|-------|---------------------|-----------------|--------|
| C1 | MSAN disabled | Enabled (no Google equivalent) | Disabled on search campaigns | Budget leak to low-quality display placements |
| C2 | Search partners appropriate | Enabled | Disabled unless intentional | Lower intent, higher CPA traffic |
| C3 | Location targeting: "People in" only | "People in or searching for" | "People in your targeted locations" | 5-15% spend on out-of-area users |
| C4 | Conversion tracking verified | May break (different UET vs gtag) | At least 1 conversion in 7d | Flying blind on performance |

### Important (fix within 48h)

| # | Check | Default After Import | Correct Setting | Impact |
|---|-------|---------------------|-----------------|--------|
| I1 | Broad match keywords reviewed | Same match types as Google | Add negatives or switch to phrase/exact | Bing close variants are more aggressive |
| I2 | Negative keyword lists imported | Not transferred | Manually recreate Google shared lists | Unprotected broad match spend |
| I3 | Ad scheduling applied | 24/7 (no schedule) | Match Google schedule or optimize for Bing | Overnight budget burn |
| I4 | Device bid adjustments reviewed | May not map correctly | Set based on Bing device performance | Misallocated spend by device |

### Optimization (fix within 1 week)

| # | Check | Default After Import | Correct Setting | Impact |
|---|-------|---------------------|-----------------|--------|
| O1 | Bid strategy compatibility | May use unmapped Google strategy | Native Bing strategy | Suboptimal bidding |
| O2 | Ad extensions imported | Most transfer, some don't | All core extensions present | Missing extensions = lower CTR |
| O3 | Campaign naming consistent | Google naming carries over | Consistent convention with [Bing] prefix or similar | Operational clarity |

## Auto-import risks

If auto-import is enabled (Microsoft Advertising > Import > Google Ads > Schedule):

- Every sync can silently re-enable MSAN and search partners
- Budget changes from Google overwrite manual Bing adjustments
- New Google broad match keywords arrive without Bing-specific negatives
- Bid strategy changes in Google cascade to Bing

**Recommendation**: Disable auto-import. Use manual import with careful review, or keep auto-import but run import-auditor after each sync.

## Scoring

- **Pass**: Setting matches correct value
- **Fail**: Setting matches default/wrong value
- **N/A**: Check doesn't apply (e.g., no broad match keywords)

Score = Passed / (Total - N/A) as percentage.
