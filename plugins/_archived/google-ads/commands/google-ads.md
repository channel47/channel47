---
description: Google Ads intelligence toolkit — daily briefs, waste detection, search term analysis, PMax transparency, account scoring, ad copy review, competitive intel
argument-hint: "brief" | "waste" | "search terms" | "pmax" | "scorecard" | "ad copy" | "competitors" | "setup"
---

# Google Ads

Orchestrator for the Google Ads plugin. Routes to the right skill based on your request.

## Quick Reference

| Command | Skill | What it does |
|---------|-------|-------------|
| `/google-ads brief` | morning-brief | Daily health check with anomaly detection and budget pacing |
| `/google-ads waste` | waste-detector | Find 8 categories of spend leaks with dollar impact |
| `/google-ads search terms` | search-term-verdict | Classify search queries into NEGATE/PROMOTE/INVESTIGATE verdicts |
| `/google-ads pmax` | pmax-decoder | Performance Max transparency — search terms, channels, assets, placements |
| `/google-ads scorecard` | account-scorecard | 5-dimension health grade (A-F) with improvement priorities |
| `/google-ads ad copy` | ad-copy-analyzer | RSA quality gaps, asset performance, messaging diversity |
| `/google-ads competitors` | competitor-intel | Auction insights analysis — threats, trends, coverage gaps |
| `/google-ads setup` | platform-setup | Connect credentials and verify Google Ads API access |

## Routing

If `$ARGUMENTS` is provided, match to the appropriate skill:

- **"brief"**, **"morning"**, **"daily"**, **"health"**, **"overnight"** → Run `/google-ads:morning-brief`
- **"waste"**, **"audit"**, **"leaks"**, **"wasted"**, **"optimization"** → Run `/google-ads:waste-detector`
- **"search terms"**, **"SQR"**, **"queries"**, **"negatives"**, **"n-gram"** → Run `/google-ads:search-term-verdict`
- **"pmax"**, **"performance max"**, **"PMax"** → Run `/google-ads:pmax-decoder`
- **"scorecard"**, **"grade"**, **"score"**, **"health check"** → Run `/google-ads:account-scorecard`
- **"ad copy"**, **"RSA"**, **"ads"**, **"headlines"**, **"copy"** → Run `/google-ads:ad-copy-analyzer`
- **"competitors"**, **"auction"**, **"competitive"**, **"SOV"** → Run `/google-ads:competitor-intel`
- **"setup"**, **"connect"**, **"configure"**, **"credentials"** → Run `/google-ads:platform-setup`
- **"profile"**, **"review profile"**, **"cleanup"** → Run `/google-ads:profile-review`

If no argument is provided:

1. Check if `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md` exists.
2. If yes → Run `/google-ads:morning-brief` (default daily workflow).
3. If no → Run `/google-ads:platform-setup` (first-time onboarding).

## Example Prompts

- "Give me a morning brief for my Google Ads account"
- "Where am I wasting money in Google Ads?"
- "Pull my search term report and find negatives"
- "What is PMax actually doing?"
- "Grade my Google Ads account"
- "Review my ad copy quality"
- "Who am I competing with in auctions?"
