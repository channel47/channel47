---
featured: true
draft: false
---

## What it does

Ask questions about your Google Ads data in plain English. Get answers instantly. No GAQL syntax to memorize. No clicking through dashboards.

Setup takes 10 minutes. You'll configure OAuth and API credentials. After that, you can investigate performance issues, find optimization opportunities, and answer stakeholder questions in seconds instead of hours.

## Key Features

- **Natural language queries**: "Find wasted spend in the last 30 days" instead of writing GAQL
- **Negative keyword discovery**: Automated analysis of search terms for optimization opportunities
- **Ad-hoc investigation**: Quick answers to performance questions without exporting data
- **Full GAQL access**: Drop into raw queries when you need precise control
- **Interactive setup wizard**: `/setup` guides you through OAuth and API configuration
- **MCC account support**: Query across multiple accounts from one place

## Real-world use cases

I use this for:

- Finding search terms with spend but no conversions (negative keyword candidates)
- Investigating performance drops: "Why did campaign X cost more this week?"
- Quick stakeholder answers: "What's our CTR for brand campaigns this month?"
- Analyzing wasted spend on broad match keywords
- Comparing performance across campaigns without building reports
- Ad-hoc checks: "Show me all paused ads with high historical CTR"

The LLM understands context. You can ask follow-up questions naturally:

- "Show me those same metrics for last quarter"
- "Which of these campaigns have the lowest conversion rates?"
- "Add those search terms as negative keywords"

## What makes it different

You don't need to:

- Learn GAQL syntax and field names
- Click through Google Ads UI tabs and filters
- Export to spreadsheets for basic analysis
- Build custom reports for one-off questions

You just ask. The LLM translates your intent into GAQL queries. It interprets results. You can drill down conversationally.

## Setup

**Time investment:** ~10 minutes for initial OAuth configuration. After that, instant access forever.

1. Install: `/plugin install google-ads@channel47`
2. Run the setup wizard: `/setup`
3. Follow prompts to configure:
   - Google Cloud project + OAuth credentials
   - Developer token from Google Ads API Center
   - Refresh token generation

The wizard walks through each step with direct links and copy-paste instructions. Credentials persist across sessions after setup.

**Quick troubleshooting:**

- If queries fail with "invalid_grant": Refresh token expired (common if OAuth app in Testing mode). Re-run `/setup` and skip to Phase 5.
- If MCP server won't connect: Verify all 5 environment variables in settings.json, then restart Claude Code.

See the [Getting Started Guide](https://github.com/ctrlswing/channel47-marketplace/blob/main/plugins/google-ads/GETTING_STARTED.md) for detailed setup steps and troubleshooting.

## Example workflows

**Find negative keyword opportunities:**

```
"Analyze search terms for account 1234567890 in the last 30 days"
"Show me terms with spend but zero conversions"
"Which of these would make good negative keywords?"
```

**Investigate performance drops:**

```
"Compare campaign metrics week over week for account 1234567890"
"Why did cost increase for Brand Campaign?"
"Show me the search terms driving the cost increase"
```

**Quick stakeholder questions:**

```
"What's our overall CTR this month?"
"List top 5 campaigns by conversion rate"
"How much did we spend on Shopping campaigns yesterday?"
```

**Advanced GAQL queries:**

```
"Run this GAQL query for account 1234567890:
SELECT campaign.name, metrics.cost_micros, metrics.conversions
FROM campaign
WHERE segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC"
```

## Available commands & skills

**Setup:**

- `/setup` - Interactive wizard for OAuth and API configuration

**Skills:**

- `/gaql-query-guide` - Reference for constructing GAQL queries and understanding available fields

**Agents:**
The negative keyword hunter agent triggers automatically when you mention negative keywords, wasted spend, or search term analysis. It analyzes search term performance and identifies optimization opportunities.

**Natural language queries:**
Just ask questions directly:

- "List my Google Ads accounts"
- "Find search terms with zero conversions for account X"
- "Show me campaign performance for last week"

The MCP server provides two tools accessible via natural language:

- Account listing (shows all accounts under your MCC)
- GAQL query execution (runs any valid Google Ads Query Language query)

See the [Getting Started Guide](https://github.com/ctrlswing/channel47-marketplace/blob/main/plugins/google-ads/GETTING_STARTED.md) for complete usage examples and troubleshooting.
