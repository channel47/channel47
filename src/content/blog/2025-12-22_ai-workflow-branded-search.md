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

I used to dread setting up branded search campaigns. Not because the work is particularly hard, but because it's tedious in a way that makes you question your life choices. You're copying and pasting ad copy variations, double-checking that you didn't mix up product names, making sure the X-All Dishwasher campaign doesn't accidentally show ads for the X-All Washing Machine. It's the kind of work where one small mistake at 11pm means you're serving the wrong landing page to thousands of dollars in ad spend.

Last week I needed to launch branded search campaigns for five products across two Google Ads accounts. I decided to treat it like a software deployment problem instead of a marketing task.

The setup was straightforward. I gave Claude a list of six product names and two requirements. First, verify each Google Ads account could handle new campaigns. Second, create campaign documentation files I could use to build everything in the Google Ads web editor. No CSV exports, just markdown files with the campaign specs.

What happened next felt less like delegating to AI and more like pair programming with someone who actually reads your documentation. Claude started by mapping each product to its correct Google Ads account by reading the meta.yaml files in my product directories. Denta Blast and Best Breath went to the 4am account. The four X-All products went to the X-All account. Then it queried each account through the Google Ads API to confirm they were active and check for existing campaigns.

This is where it got interesting. The X-All Mold Gel account already had a branded search campaign from December 18th. Instead of blindly creating a duplicate, Claude flagged it and skipped that product entirely. It also noticed that multiple X-All products share the same brand term, which creates overlap risk. The dishwasher campaign documentation includes negative keywords for washing machine terms, and vice versa. I didn't ask for that. The system inferred it from the pattern.

Each campaign file follows the same structure because Claude used the existing X-All Mold Gel campaign as a reference template. Three ad groups per campaign. Brand Core for people searching the exact product name. Brand + Product for variations that include category terms. Brand + Intent for searches that signal purchase intent. Every file includes responsive search ad copy with 15 headlines and 4 descriptions, sitelink extensions, callout extensions, and competitor negative keywords.

The trade-off is that I still need to verify the sales page URLs. Claude pulled the confirmed URL for DentaBlast from existing campaign data, but the other four products got placeholder URLs that need checking. Fair enough. I'd rather verify four URLs than build five complete campaign structures from scratch.

The whole process took maybe 20 minutes, most of which was Claude reading files and querying APIs. What I got was five campaign-ready markdown files sitting in the correct product directory structure, each one following the exact documentation pattern I've been using for months. No copying and pasting between products. No forgetting to update the CID or target ROAS. No accidentally mixing up ad copy between Best Breath and DentaBlast.

Here's what made this work. I didn't ask Claude to "write some ads" or "help with marketing." I gave it a structured request with clear output requirements, then let it figure out how to gather the information it needed. It read config files. It queried APIs. It referenced existing documentation patterns. It handled the systematic parts so I could focus on the verification and approval steps that actually need human judgment.

The files are just markdown, nothing fancy. But they're consistent, complete, and organized in a way that my future self will understand when I need to update them in six months. That consistency matters more than any individual piece of ad copy.
