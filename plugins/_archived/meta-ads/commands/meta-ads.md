---
description: Meta Ads intelligence toolkit — daily briefs, waste detection, creative fatigue analysis, creative audits, audience analysis, competitive research, account scoring
argument-hint: "brief" | "waste" | "creative fatigue" | "creative audit" | "audience" | "competitors" | "scorecard" | "setup"
---

# Meta Ads

Orchestrator for the Meta Ads plugin. Routes to the right skill based on your request.

## Quick Reference

| Command | Skill | What it does |
|---------|-------|-------------|
| `/meta-ads brief` | morning-brief | Daily health check for Facebook + Instagram campaigns |
| `/meta-ads waste` | waste-detector | Find 8 categories of Meta spend leaks with dollar impact |
| `/meta-ads creative fatigue` | creative-fatigue | Lifecycle staging (Testing/Rising/Peak/Fatiguing/Dead) with days-remaining estimates |
| `/meta-ads creative audit` | creative-audit | Creative mix analysis — format, concept, angle gaps with testing roadmap |
| `/meta-ads audience` | audience-analyzer | Audience performance, saturation, overlap detection, refresh recommendations |
| `/meta-ads competitors` | competitor-research | Ad Library research + own-account competitive benchmarking |
| `/meta-ads scorecard` | account-scorecard | 5-dimension health grade (A-F) with improvement priorities |
| `/meta-ads setup` | platform-setup | Connect Meta API credentials and verify account access |

## Routing

If `$ARGUMENTS` is provided, match to the appropriate skill:

- **"brief"**, **"morning"**, **"daily"**, **"health"**, **"overnight"** → Run `/meta-ads:morning-brief`
- **"waste"**, **"audit"**, **"leaks"**, **"wasted"**, **"optimization"** → Run `/meta-ads:waste-detector`
- **"creative fatigue"**, **"fatigue"**, **"dying ads"**, **"days remaining"**, **"ad lifecycle"** → Run `/meta-ads:creative-fatigue`
- **"creative audit"**, **"creative mix"**, **"format gaps"**, **"creative matrix"** → Run `/meta-ads:creative-audit`
- **"audience"**, **"audiences"**, **"targeting"**, **"lookalike"**, **"overlap"** → Run `/meta-ads:audience-analyzer`
- **"competitors"**, **"competitive"**, **"ad library"**, **"spy"** → Run `/meta-ads:competitor-research`
- **"scorecard"**, **"grade"**, **"score"**, **"health check"** → Run `/meta-ads:account-scorecard`
- **"setup"**, **"connect"**, **"configure"**, **"credentials"** → Run `/meta-ads:platform-setup`
- **"profile"**, **"review profile"**, **"cleanup"** → Run `/meta-ads:profile-review`

If no argument is provided:

1. Check if `${CLAUDE_PLUGIN_ROOT}/profile/account-profile.md` exists.
2. If yes → Run `/meta-ads:morning-brief` (default daily workflow).
3. If no → Run `/meta-ads:platform-setup` (first-time onboarding).

## Example Prompts

- "Give me a morning brief for my Meta campaigns"
- "Where am I wasting money on Facebook Ads?"
- "Which creatives are dying?"
- "Audit my creative mix and find gaps"
- "How are my audiences performing?"
- "What are my competitors running?"
- "Grade my Meta Ads account"
