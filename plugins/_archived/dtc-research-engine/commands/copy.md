---
description: Write platform-specific DTC ad copy (Meta, Google, TikTok, email, landing pages)
argument-hint: [product name] [platform: meta|google|tiktok|email|landing|all] (optional)
allowed-tools: Read, Write, Edit, Grep, Glob
---

Run the copy-writer skill.

Locate research, personas, and angles files in the workspace. If $ARGUMENTS includes a product name, match against it. If a platform is specified, write copy for that platform. Default to Meta + Google Search if unspecified.

For each top angle:
- Write 3-5 primary text variations (short, medium, long for Meta)
- Write 5-10 headline variations per platform
- Write descriptions, captions, or subject lines as appropriate
- Respect all character limits for each platform
- Use customer language from research data naturally

Save as [product-slug]-copy.md in the workspace.
