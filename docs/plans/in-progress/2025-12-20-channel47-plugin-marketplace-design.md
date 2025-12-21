# Channel 47 Plugin Marketplace Design

**Date:** 2025-12-20
**Status:** Design Complete
**Author:** Jackson

## Vision

Build a publisher-focused plugin marketplace for Claude Code that creates a cyclical engine:

```
Daily workflows → Build tools → Write essays → Share tools → Inspire ideas → Repeat
```

### Core Principles

1. **Publisher, not aggregator**: Feature only tools built and maintained by Channel 47
2. **Quality over quantity**: Every plugin is battle-tested in daily use
3. **Open source first**: Build for long-term impact and community, not monetization
4. **Natural discovery**: Blog naturally aggregates other tools through authentic mentions
5. **Sustainable**: Only maintain what is actively used

### Long-term Goal

Look back in 5-20 years and say: "I built something meaningful that connected people, sparked ideas, and created opportunities through open source contribution."

## Architecture Overview

### Two-Repository Structure

**Repository 1: `channel47`** (Astro site)
- **Purpose**: Blog, essays, plugin showcase
- **URL**: `channel47.dev` (or similar)
- **GitHub**: `yourusername/channel47`
- **Deployment**: Vercel (auto-deploy on push)
- **Content**:
  - `/blog` - Essays about workflows and daily Claude Code usage
  - `/plugins` - Channel 47 marketplace plugins showcase
  - `/about` - About the project and author

**Repository 2: `channel47-marketplace`** (Plugin registry)
- **Purpose**: Plugin distribution registry
- **GitHub**: `yourusername/channel47-marketplace`
- **Installation**: `/plugin marketplace add yourusername/channel47-marketplace`
- **Contains**: Only plugins built/maintained by Channel 47

### Relationship

- Marketplace is independent and can be used standalone
- Astro site features marketplace plugins prominently
- Site can mention other community tools in blog posts (no formal directory)
- No tight coupling - either repo can update independently
- Site auto-rebuilds when marketplace updates (Vercel webhook)

## Marketplace Repository Structure

### Directory Layout

```
channel47-marketplace/
├── .claude-plugin/
│   └── marketplace.json          # Registry catalog (source of truth)
├── plugins/
│   ├── google-ads/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json       # Plugin manifest
│   │   ├── .mcp.json            # MCP server config
│   │   ├── src/
│   │   │   └── google_ads_mcp.py
│   │   ├── scripts/
│   │   │   ├── generate_refresh_token.py
│   │   │   └── test_auth.py
│   │   ├── config/
│   │   │   └── .env.example
│   │   ├── requirements.txt
│   │   ├── README.md
│   │   ├── GETTING_STARTED.md
│   │   ├── QUICK_START.md
│   │   └── CHANGELOG.md
│   └── (future-plugins)/
├── shared/                       # Optional: shared utilities
│   └── lib/
└── README.md                     # Marketplace overview
```

### marketplace.json

Source of truth for all plugin metadata:

```json
{
  "name": "channel47",
  "owner": {
    "name": "Jackson",
    "url": "https://channel47.dev"
  },
  "description": "Battle-tested Claude Code plugins from daily workflows",
  "metadata": {
    "pluginRoot": "./plugins"
  },
  "plugins": [
    {
      "name": "google-ads",
      "source": "google-ads",
      "description": "Query Google Ads data using GaQL with OAuth authentication",
      "version": "1.0.0",
      "author": "Jackson",
      "category": "marketing",
      "tags": ["google-ads", "marketing", "analytics", "mcp"]
    }
  ]
}
```

### Individual Plugin Structure

**Example: Google Ads MCP Plugin**

```
plugins/google-ads/
├── .claude-plugin/
│   └── plugin.json              # Plugin manifest
├── .mcp.json                    # MCP server configuration
├── src/
│   └── google_ads_mcp.py       # Python MCP server (single file)
├── scripts/
│   ├── generate_refresh_token.py  # One-time OAuth setup
│   ├── test_auth.py              # Auth verification
│   └── client_secrets.example.json
├── config/
│   └── .env.example            # Environment variables template
├── requirements.txt             # Python dependencies
├── README.md                    # User-facing documentation
├── GETTING_STARTED.md          # Setup walkthrough
├── QUICK_START.md              # Fast path instructions
└── CHANGELOG.md                 # Version history
```

**plugin.json:**

```json
{
  "name": "google-ads",
  "version": "1.0.0",
  "description": "Query Google Ads data using GaQL with OAuth authentication",
  "author": {
    "name": "Jackson",
    "url": "https://channel47.dev"
  },
  "homepage": "https://channel47.dev/plugins/google-ads",
  "repository": "https://github.com/yourusername/channel47-marketplace",
  "mcp": {
    "configFile": ".mcp.json"
  },
  "requirements": {
    "python": ">=3.10"
  }
}
```

**.mcp.json:**

```json
{
  "mcpServers": {
    "google-ads": {
      "command": "python",
      "args": ["${CLAUDE_PLUGIN_ROOT}/src/google_ads_mcp.py"],
      "env": {
        "GOOGLE_ADS_DEVELOPER_TOKEN": "",
        "GOOGLE_ADS_LOGIN_CUSTOMER_ID": "",
        "GOOGLE_ADS_CLIENT_ID": "",
        "GOOGLE_ADS_CLIENT_SECRET": "",
        "GOOGLE_ADS_REFRESH_TOKEN": ""
      }
    }
  }
}
```

**User setup flow:**
1. Install plugin: `/plugin install google-ads@channel47`
2. Run one-time OAuth setup: `python ${CLAUDE_PLUGIN_ROOT}/scripts/generate_refresh_token.py`
3. Copy refresh token to Claude settings or `.env`
4. Server uses refresh token for all future API requests

## Astro Site Integration

### Hybrid Sync Strategy

**Data ownership split:**

**Technical metadata** (from `marketplace.json`):
- Plugin name, version, description
- Install commands
- Category, tags
- Repository URL

**Editorial content** (from Astro markdown):
- Rich usage guides
- Screenshots and examples
- Real-world workflow stories
- Related blog posts
- Setup walkthroughs

### Content Structure

```
channel47/src/content/
├── blog/
│   └── 2024-12-20-automating-google-ads.md
└── plugins/
    └── google-ads.md
```

**plugins/google-ads.md:**

```markdown
---
slug: "google-ads"
featured: true
# Technical data comes from marketplace.json
# relatedPosts auto-discovered from blog frontmatter
---

## What it does

Full editorial content explaining the plugin, your experience using it,
detailed examples, screenshots, etc.

## Real-world usage

Here's how I use this daily for managing PPC campaigns...

## Setup walkthrough

Step-by-step guide with screenshots...
```

### Build-Time Merge Process

```typescript
// scripts/sync-marketplace.ts
// Runs at build time (Astro integration)

1. Fetch marketplace.json from channel47-marketplace repo (git submodule or API)
2. Read all markdown files from src/content/plugins/
3. Merge:
   - Technical metadata from marketplace.json (version, install command, tags)
   - Editorial content from markdown files
   - Auto-discover related blog posts (scan blog frontmatter for toolsUsed)
4. Generate unified data structure for templates
5. Render plugin pages
```

### Plugin Page Layout

```
/plugins/google-ads

┌─────────────────────────────────────────────┐
│ Google Ads MCP                              │
│ Query Google Ads data using GaQL            │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ Install                                 │ │
│ │                                         │ │
│ │ Already added marketplace?              │ │
│ │ Skip to install →                       │ │
│ │                                         │ │
│ │ Step 1: Add Channel 47 marketplace      │ │ <- Collapsible
│ │ /plugin marketplace add username/...    │ │    after first use
│ │ [Copy]                                  │ │
│ │                                         │ │
│ │ Step 2: Install plugin                  │ │
│ │ /plugin install google-ads@channel47    │ │
│ │ [Copy]                                  │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ v1.2.0 | Marketing | MCP Server             │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ See it in action:                       │ │
│ │                                         │ │
│ │ • Building a Google Ads MCP Server      │ │ <- Auto-discovered
│ │   Nov 12, 2024                          │ │    from blog posts
│ │                                         │ │
│ │ • Automating PPC with Claude            │ │
│ │   Dec 20, 2024                          │ │
│ └─────────────────────────────────────────┘ │
└─────────────────────────────────────────────┘

[Rich editorial content: What it does, setup, usage examples]
```

**Progressive disclosure install CTA:**
- First-time visitors see full two-step process
- Returning users see collapsed first step with "Skip to install"
- Copy buttons for easy command execution
- Clear visual hierarchy prioritizing installation

### /plugins Index Page

```
/plugins

Filter bar:
[All] [Marketing] [Development] [Writing] [Automation]

Plugin grid:
┌──────────────────────┐ ┌──────────────────────┐
│ ⭐ Google Ads MCP    │ │ Future Plugin        │
│ v1.2.0               │ │ v0.1.0               │
│ Marketing            │ │ Development          │
│                      │ │                      │
│ Query Google Ads...  │ │ Description...       │
└──────────────────────┘ └──────────────────────┘
```

## Blog ↔ Tools Bidirectional Linking

### Blog Post → Tools

**Blog post frontmatter:**

```markdown
---
title: "Automating Google Ads with Claude Code"
date: 2024-12-20
toolsUsed:
  - slug: google-ads
    source: channel47         # Your plugin
  - slug: superpowers
    source: external          # External plugin
    installCommand: /plugin marketplace add superpowers-marketplace/superpowers
---

Today I automated my entire PPC workflow...
```

**Display on blog post:**

```
┌────────────────────────────────────┐
│ Tools mentioned in this post:      │
│                                    │
│ ⚡ Google Ads MCP                  │ <- Links to /plugins/google-ads
│    /plugin install google-ads...   │    Prominent if it's yours
│                                    │
│ 🔗 Superpowers                     │ <- External link with icon
│    /plugin marketplace add...      │    Shows how to get it
└────────────────────────────────────┘
```

### Plugin Page → Blog Posts

**Auto-discovery process:**

```typescript
// Build time: scan all blog posts
for (const post of blogPosts) {
  for (const tool of post.frontmatter.toolsUsed) {
    if (tool.slug === 'google-ads' && tool.source === 'channel47') {
      addRelatedPost(post, 'google-ads-plugin')
    }
  }
}
```

**Display on plugin page:**

```
┌────────────────────────────────────┐
│ See it in action:                  │
│                                    │
│ • Building a Google Ads MCP Server │
│   Nov 12, 2024                     │
│                                    │
│ • Automating PPC with Claude       │
│   Dec 20, 2024                     │
└────────────────────────────────────┘
```

**Benefits:**
- No manual maintenance of related posts
- Blog posts automatically appear on plugin pages
- Natural discovery path: tool → usage examples
- Creates the cyclical engine: tools ↔ content

## Workflow & Operations

### Adding a New Plugin

```
Daily work → "This needs a tool" → Build it → Share it

1. Build plugin locally in channel47-marketplace/plugins/new-plugin/
   - Create plugin structure
   - Implement MCP server or skills
   - Test locally with Claude Code

2. Add entry to marketplace.json:
   {
     "name": "new-plugin",
     "version": "0.1.0",
     "description": "...",
     "category": "...",
     "tags": [...]
   }

3. Create plugin documentation in marketplace repo:
   - README.md (user-facing)
   - GETTING_STARTED.md (setup)
   - CHANGELOG.md (version history)

4. Create plugin page in channel47 repo:
   src/content/plugins/new-plugin.md
   ---
   slug: "new-plugin"
   featured: false
   ---
   ## What it does...
   [Rich editorial content]

5. Commit both repos
   - channel47-marketplace → users can install
   - channel47 → site auto-deploys with new plugin page

6. Optional: Write blog post about the workflow that inspired the tool
   - Add toolsUsed: [new-plugin] to frontmatter
   - Auto-links to plugin page
```

### Updating an Existing Plugin

**Semantic versioning:**
- `1.0.0` → `1.0.1` - Bug fix (patch)
- `1.0.1` → `1.1.0` - New feature/tool (minor)
- `1.1.0` → `2.0.0` - Breaking change (major)

**Update workflow:**

```
1. Make changes in channel47-marketplace/plugins/google-ads/
   - Update code
   - Test changes

2. Update version in marketplace.json:
   "version": "1.0.0" → "1.1.0"

3. Update CHANGELOG.md in plugin directory:
   ## [1.1.0] - 2024-12-20
   ### Added
   - New shopping campaign analysis tool
   ### Fixed
   - OAuth token refresh edge case

4. Optional: Update plugin page content if needed
   - Update examples, screenshots, setup guide
   - channel47/src/content/plugins/google-ads.md

5. Commit and push both repos
   - Marketplace: users see update notification in Claude Code
   - Astro site: auto-rebuilds, shows new version on plugin page

6. Users update via:
   /plugin marketplace update channel47
```

**CHANGELOG pattern (per plugin):**

```markdown
# Changelog - Google Ads MCP

All notable changes to this plugin will be documented in this file.

## [1.1.0] - 2024-12-20
### Added
- New shopping campaign analysis tool
- Support for Performance Max campaigns

### Fixed
- OAuth token refresh edge case

## [1.0.0] - 2024-11-10
### Added
- Initial release
- List accounts tool
- GaQL query tool
```

### Update Distribution

**For users:**
- Third-party marketplaces have auto-update disabled by default
- Users manually update when ready: `/plugin marketplace update channel47`
- Claude Code shows notification when updates available
- Plugin page displays "v1.1.0 available" if user on older version
- Clear changelog visible on plugin page

**For the site:**
- Vercel webhook triggers rebuild on marketplace repo push
- Site always displays latest version from marketplace.json
- No manual deployment needed

## Implementation Phases

### Phase 1: Marketplace Foundation
- [ ] Create `channel47-marketplace` repository
- [ ] Set up marketplace.json structure
- [ ] Migrate Google Ads MCP into plugin structure
- [ ] Test installation flow
- [ ] Write marketplace README

### Phase 2: Site Integration
- [ ] Rename `/products` to `/plugins` in Astro site
- [ ] Create hybrid sync build script
- [ ] Implement plugin page template with install CTA
- [ ] Create `/plugins` index page with filtering
- [ ] Set up Vercel webhook for auto-rebuild

### Phase 3: Bidirectional Linking
- [ ] Add `toolsUsed` support to blog post frontmatter
- [ ] Implement auto-discovery for related posts
- [ ] Create "Tools mentioned" component for blog posts
- [ ] Create "See it in action" component for plugin pages
- [ ] Test linking flow both directions

### Phase 4: Polish & Launch
- [ ] Write launch blog post about the marketplace
- [ ] Create example blog posts using Google Ads plugin
- [ ] Add screenshots and examples to plugin page
- [ ] Test complete user journey (discover → install → use)
- [ ] Announce Channel 47 marketplace

## Success Metrics

**Qualitative:**
- Pride in the work built (5-20 year perspective)
- Quality of connections and opportunities created
- Community feedback and contributions
- Personal workflow improvements

**Quantitative (secondary):**
- Plugin installations
- Blog post engagement
- Related post click-through
- GitHub stars/forks
- Community PRs to marketplace

## Future Considerations

**Community contributions:**
- Accept PRs to Channel 47 marketplace for new plugins
- Quality bar: must be battle-tested, well-documented
- Maintains publisher focus while enabling community growth
- Like Homebrew "core" vs "cask" model

**Plugin ideas from workflows:**
- Each daily Claude Code session is potential plugin material
- Blog posts document the problem → solution journey
- Plugins extract reusable solutions from one-off workflows
- Natural pipeline: work → writing → tools → sharing

**Ecosystem evolution:**
- As Claude Code plugin ecosystem matures, Channel 47 becomes known for quality
- "Channel 47 standard" emerges from consistent patterns
- Others may fork/adapt approaches
- Focus stays on personal use cases, not feature requests

## Appendix: Key Decisions

### Why Publisher vs Aggregator?
- **Sustainability**: Only maintain what you use daily
- **Quality**: Personal use guarantees quality and relevance
- **Defensibility**: Unique workflows can't be copied
- **Time economics**: Marginal cost near zero vs aggregator burden
- **Brand**: "Jackson's battle-tested tools" vs "Yet another directory"
- **Long-term value**: Portfolio of built work vs curated links

### Why Separate Repos?
- **Independence**: Marketplace can be used without the site
- **Deployment**: Site and marketplace update independently
- **Clarity**: Clear separation of concerns
- **Growth**: Site can evolve beyond just plugins

### Why Hybrid Sync?
- **Single source of truth**: marketplace.json for technical data
- **Rich content**: Editorial content where it belongs (site)
- **Auto-sync**: Always current without manual duplication
- **Flexibility**: Can deploy site without updating marketplace

### Why Auto-Discovery for Related Posts?
- **No maintenance**: Blog posts automatically link to plugins
- **Freshness**: New posts appear on plugin pages automatically
- **Accuracy**: Source of truth is blog post frontmatter
- **Scalability**: Works as content and plugins grow

---

**Next Steps:** Proceed to implementation planning, starting with Phase 1.
