---
title: "Treating Campaign Setup Like a Software Deployment"
description: "How AI-assisted workflow automation turned a tedious five-campaign launch into a systematic documentation process that took 20 minutes instead of hours of copy-paste work."
date: 2025-12-22
tags:
  [
    "ai-workflows",
    "google-ads",
    "marketing-automation",
    "claude-code",
    "api-integration",
    "systematic-processes",
  ]
toolsUsed:
  - slug: "google-ads"
    source: "channel47"
heroImages:
  styleA: null
  styleD: null
  selected: null
visualMetaphor: "A traditional campaign planning desk cluttered with spreadsheets and sticky notes transforming into a clean command line interface executing systematic API calls."
visualMetaphorReasoning: "Captures the shift from manual tedious marketing work to treating campaign setup as a structured software deployment problem."
---

## The Problem

I used to dread setting up branded search campaigns. The work isn't hard. It's tedious in a way that makes you question your life choices.

You're copying and pasting ad copy variations. You're double-checking that you didn't mix up product names. You're making sure the X-All Dishwasher campaign doesn't accidentally show ads for the X-All Washing Machine. One small mistake at 11pm means you're serving the wrong landing page to thousands of dollars in ad spend.

## Treating It Like Code

Last week I needed to launch branded search campaigns for five products across two Google Ads accounts. I treated it like a software deployment problem instead of a marketing task.

The setup was straightforward. I gave Claude a list of six product names and two requirements. First, verify each Google Ads account could handle new campaigns. Second, create campaign documentation files I could use to build everything in the Google Ads web editor.

## What Happened

Claude started by mapping each product to its correct Google Ads account. It read the meta.yaml files in my product directories. Denta Blast and Best Breath went to the 4am account. The four X-All products went to the X-All account. Then it queried each account through the Google Ads API to confirm they were active and check for existing campaigns.

The X-All Mold Gel account already had a branded search campaign from December 18th. Claude flagged it and skipped that product entirely. It also noticed that multiple X-All products share the same brand term. This creates overlap risk.

The dishwasher campaign documentation includes negative keywords for washing machine terms, and vice versa. I didn't ask for that. The system inferred it from the pattern.

Claude used the existing X-All Mold Gel campaign as a reference template. Each campaign file follows the same structure. Three ad groups per campaign: Brand Core for people searching the exact product name, Brand + Product for variations that include category terms, Brand + Intent for searches that signal purchase intent.

Every file includes responsive search ad copy with 15 headlines and 4 descriptions, sitelink extensions, callout extensions, and competitor negative keywords.

## The Trade-offs

The trade-off is that I still need to verify the sales page URLs. Claude pulled the confirmed URL for DentaBlast from existing campaign data. The other four products got placeholder URLs that need checking. I'd rather verify four URLs than build five complete campaign structures from scratch.

## What I Got

The whole process took 20 minutes. Most of that was Claude reading files and querying APIs. I got five campaign-ready markdown files in the correct product directory structure. Each one follows the exact documentation pattern I've been using for months.

## Why It Worked

I didn't ask Claude to "write some ads" or "help with marketing." I gave it a structured request with clear output requirements. Then I let it figure out how to gather the information it needed. It read config files. It queried APIs. It referenced existing documentation patterns.

The files are just markdown. But they're consistent, complete, and organized in a way that my future self will understand when I need to update them in six months. That consistency matters more than any individual piece of ad copy.
