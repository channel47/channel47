---
featured: true
draft: false
---

## What it does

Query your Google Ads data directly from Claude Code using GaQL (Google Ads Query Language). Perfect for automating PPC analysis, generating reports, and monitoring campaign performance.

## Key Features

- **List all accounts**: Quickly see all accessible Google Ads accounts
- **GaQL queries**: Run any GaQL query directly from Claude
- **OAuth authentication**: Secure, token-based auth with automatic refresh

## Real-world use cases

I use this daily for:
- Analyzing campaign performance across multiple accounts
- Generating weekly PPC reports
- Debugging campaign issues with ad-hoc queries
- Monitoring budget pacing

## Setup

The setup involves getting OAuth credentials from Google Cloud and generating a refresh token. Full walkthrough:

1. Install: `/plugin install google-ads@channel47`
2. Follow [Getting Started Guide](https://github.com/ctrlswing/channel47-marketplace/blob/main/plugins/google-ads/GETTING_STARTED.md)
3. Configure your credentials in Claude Code settings

## Example queries

Ask Claude:
- "Show me all my Google Ads accounts"
- "Query campaign performance for last 30 days"
- "What's my average CPC across all campaigns?"
