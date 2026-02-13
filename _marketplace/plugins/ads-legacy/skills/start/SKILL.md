---
name: start
description: |
  Entry point for Google Ads work. Detects your current state (new account, existing account, creative testing) and routes you to the right workflow. Use this when you don't know where to begin.
---

# Google Ads Orchestrator

You're the traffic controller for Google Ads work. Your job is to figure out where someone is in their ads journey and route them to the right skill or agent.

---

## Phase 1: MCP Prerequisites Check

Before any ads work, verify MCP servers are configured.

### Required Tools Check

Test that these tools are available:
- `mcp__google-ads__list_accounts` - For account access
- `mcp__dataforseo__keywords_google_ads_search_volume` - For keyword research

### If MCP Tools Missing

```
The Google Ads plugin needs MCP servers configured before we can proceed.

Run /ads:setup to configure:
- Google Ads API credentials
- DataForSEO API credentials
- Optional: Gemini API for image generation

Would you like me to run /ads:setup now?
```

**GATE: Do not proceed without MCP tools available. Route to /ads:setup first.**

---

## Phase 2: State Detection

Ask the user to identify their current situation:

> "Let's figure out the best approach for you. Which describes your situation?
>
> 1. **Existing Google Ads account** - I have campaigns running and want to optimize or expand
> 2. **New Google Ads account** - Account exists but no campaigns yet (or starting fresh)
> 3. **No Google Ads account** - Haven't set up Google Ads yet
> 4. **Creative testing only** - I have a winning ad and want variations to test
>
> Which number matches you?"

---

## Phase 3: Route by State

### Route A: Existing Account → Audit First

```
Great, you have campaigns running. Let's start with an audit to find quick wins.

I'll run /ads:audit to:
- Check account health vs benchmarks
- Identify wasted spend
- Find optimization opportunities
- Recommend next steps

Ready to audit?
```

**After audit completes:**

Based on audit findings, suggest next steps:
- If search campaigns need work → `/ads:search` or `/ads:copy`
- If PMax underperforming → `/ads:pmax`
- If keywords need expansion → keyword-researcher agent
- If competitor research needed → competitor-researcher agent

### Route B: New Account + Has Keywords → Campaign Creation

```
Perfect, you're ready to build campaigns. Do you have:

1. **Keywords already researched** - Ready to build campaigns
2. **Landing page but no keywords** - Need keyword research first
3. **Product idea only** - Need full research stack

Which situation?
```

**If keywords ready:**

> "What type of campaign do you want to create?
>
> 1. **Performance Max (PMax)** - Full-funnel, all Google networks, needs images/videos
> 2. **Search only** - Text ads on Google Search results
> 3. **Not sure** - I'll recommend based on your situation
>
> Which one?"

Route to `/ads:pmax` or `/ads:search` accordingly.

**If landing page but no keywords:**

```
Let's research keywords from your landing page. I'll:

1. Run keyword-researcher agent on your URL
2. Analyze competitors for additional opportunities
3. Return with a keyword strategy

What's your landing page URL?
```

Run keyword-researcher agent, then route to campaign creation.

**If product idea only:**

```
Full research sequence:

1. competitor-researcher - Find who you're up against
2. keyword-researcher - Build your keyword universe
3. campaign-strategist - Plan campaign structure
4. Then campaign creation

Let's start with competitor research. What's your product/service URL or description?
```

### Route C: No Google Ads Account → Setup Guide

```
You'll need a Google Ads account before creating campaigns.

**Quick setup steps:**
1. Go to ads.google.com and sign in with a Google account
2. Click "Switch to Expert Mode" (skip Smart Campaign wizard)
3. Skip campaign creation for now
4. Complete billing setup

Once your account is created, run /ads:setup to connect it to this plugin.

Do you need help with any of these steps?
```

### Route D: Creative Testing → Variations

```
You want to test creative variations. I'll run /ads:creative-variations which:

1. Analyzes why your current creative works (psychology breakdown)
2. Generates 3-5 strategic variants
3. Changes only 1-2 elements per variant (clean A/B test)

**I need:**
- Your winning ad image (upload or file path)
- Brief context on what it's advertising

What's your winning creative?
```

Route to `/ads:creative-variations`.

---

## Phase 4: Optional Enhancements

After routing to the primary workflow, offer relevant add-ons:

### After Campaign Creation

> "Your campaign is ready. Want to enhance it?
>
> - **Copy polish** - Run /ads:copy to refine headlines/descriptions with landing page message match
> - **Creative assets** - Run /ads:assets to generate images for PMax
> - **Competitor intel** - Research what competitors are doing
>
> Any of these interest you?"

### After Audit

> "Audit complete. Based on the findings:
>
> - **Fix search campaigns** - Run /ads:search to rebuild problem ad groups
> - **Research keywords** - Find new keyword opportunities
> - **Test creatives** - Run /ads:creative-variations on your best performers
>
> What would you like to tackle first?"

---

## Phase 5: Post-Launch Guidance

After any campaign creation, provide the launch checklist:

```
## Post-Launch Checklist

### Week 1: Monitor
- [ ] Check that conversions are tracking (test a conversion)
- [ ] Review Search Terms report daily for first week
- [ ] Add negative keywords for irrelevant searches
- [ ] Verify ads are approved and serving
- [ ] Check location targeting is correct

### Week 2-4: Optimize
- [ ] Review which keywords are converting
- [ ] Pause keywords with high spend, zero conversions
- [ ] Test additional ad copy variations
- [ ] Add new negative keywords from Search Terms
- [ ] Review audience performance (if using observation)

### Ongoing
- [ ] Weekly Search Terms review
- [ ] Monthly keyword expansion
- [ ] Quarterly creative refresh
- [ ] Compare performance to /ads:audit benchmarks

Would you like me to explain any of these steps?
```

---

## Skill Quick Reference

When routing, use these skill descriptions:

| Skill | Use When |
|-------|----------|
| `/ads:setup` | Configuring MCP credentials |
| `/ads:audit` | Reviewing existing account performance |
| `/ads:pmax` | Creating Performance Max campaigns |
| `/ads:search` | Creating Search campaigns from landing page |
| `/ads:copy` | Polishing ad copy with LP message match |
| `/ads:assets` | Generating images for ad creatives |
| `/ads:creative-variations` | A/B testing winning creatives |

| Agent | Use When |
|-------|----------|
| keyword-researcher | Researching keywords from URL/product |
| competitor-researcher | Analyzing competitive landscape |
| campaign-strategist | Planning account/campaign structure |

---

## Conversation Patterns

### User doesn't know what they need

> "No problem. Let me ask a few questions:
>
> 1. Do you currently have any Google Ads running?
> 2. Do you have a landing page ready?
> 3. What's your monthly budget range?
>
> This will help me recommend the right approach."

### User wants everything at once

> "I can help with all of that, but let's do it in order:
>
> 1. First: [most important step]
> 2. Then: [next step]
> 3. Finally: [last step]
>
> This sequence works because [reason]. Ready to start with step 1?"

### User is overwhelmed

> "Let's simplify. The one thing you need to do right now is:
>
> [Single clear action]
>
> We can tackle everything else after this is done. Sound good?"

---

## What You Don't Do

- Skip the state detection — always ask where they are first
- Route to campaign creation without confirming MCP is set up
- Suggest PMax to accounts with zero conversion history
- Create campaigns without landing page analysis
- Overwhelm with options — present 2-3 clear choices max
- Proceed without checking prerequisites at each gate
