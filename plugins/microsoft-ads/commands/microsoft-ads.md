---
description: Microsoft Ads intelligence toolkit — daily briefs, waste detection, search term analysis, import auditing, placement cleanup, account scoring
argument-hint: "brief" | "waste" | "search terms" | "import audit" | "placements" | "scorecard" | "setup"
---

# Microsoft Ads

Orchestrator for the Microsoft Ads plugin. Routes to the right skill based on your request.

## Quick Reference

| Command | Skill | What it does |
|---------|-------|-------------|
| `/microsoft-ads brief` | morning-brief | Daily health check with anomaly detection, bot monitoring, import drift |
| `/microsoft-ads waste` | waste-detector | Find 7 Bing-specific spend leaks with dollar impact |
| `/microsoft-ads search terms` | search-term-verdict | Classify Bing search queries into NEGATE/PROMOTE/INVESTIGATE verdicts |
| `/microsoft-ads import audit` | import-auditor | Post-Google-import cleanup — catch misconfigured settings |
| `/microsoft-ads placements` | placement-cleaner | MSAN and search partner publisher URL quality analysis |
| `/microsoft-ads scorecard` | account-scorecard | 5-dimension health grade (A-F) with improvement priorities |
| `/microsoft-ads setup` | platform-setup | Connect credentials and verify Microsoft Advertising API access |

## Routing

If `$ARGUMENTS` is provided, match to the appropriate skill:

- **"brief"**, **"morning"**, **"daily"**, **"health"**, **"overnight"** → Run `/microsoft-ads:morning-brief`
- **"waste"**, **"audit"**, **"leaks"**, **"wasted"**, **"optimization"** → Run `/microsoft-ads:waste-detector`
- **"search terms"**, **"SQR"**, **"queries"**, **"negatives"**, **"n-gram"** → Run `/microsoft-ads:search-term-verdict`
- **"import"**, **"import audit"**, **"auto-import"**, **"Google import"** → Run `/microsoft-ads:import-auditor`
- **"placements"**, **"MSAN"**, **"publisher"**, **"exclusions"** → Run `/microsoft-ads:placement-cleaner`
- **"scorecard"**, **"grade"**, **"score"**, **"health check"** → Run `/microsoft-ads:account-scorecard`
- **"setup"**, **"connect"**, **"configure"**, **"credentials"** → Run `/microsoft-ads:platform-setup`
- **"profile"**, **"review profile"**, **"cleanup"** → Run `/microsoft-ads:profile-review`

If no argument is provided:

1. Check if `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md` exists.
2. If yes → Run `/microsoft-ads:morning-brief` (default daily workflow).
3. If no → Run `/microsoft-ads:platform-setup` (first-time onboarding).

## Example Prompts

- "Give me a morning brief for my Bing account"
- "Where am I wasting money on Microsoft Ads?"
- "Pull my Bing search term report"
- "Audit my Google import settings"
- "Clean up my MSAN placements"
- "Grade my Microsoft Ads account"
