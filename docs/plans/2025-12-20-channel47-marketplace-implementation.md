# Channel 47 Plugin Marketplace Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a publisher-focused plugin marketplace that creates a cyclical engine between daily workflows, tool building, essay writing, and sharing.

**Architecture:** Two-repository structure with marketplace registry (channel47-marketplace) and Astro site (channel47). Hybrid sync merges technical metadata from marketplace.json with editorial content from markdown at build time. Bidirectional linking auto-discovers relationships between blog posts and plugins.

**Tech Stack:** Astro 4.x, TypeScript, Tailwind CSS, Git submodules, Vercel webhooks

---

## Phase 1: Marketplace Foundation

### Task 1: Create marketplace repository structure

**Files:**
- Create: `../channel47-marketplace/.claude-plugin/marketplace.json`
- Create: `../channel47-marketplace/README.md`
- Create: `../channel47-marketplace/.gitignore`

**Step 1: Initialize repository**

```bash
cd ..
mkdir channel47-marketplace
cd channel47-marketplace
git init
```

**Step 2: Create .gitignore**

```
# Dependencies
node_modules/
*.pyc
__pycache__/

# Environment
.env
.env.local
*.log

# OS
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/
*.swp

# Testing
.pytest_cache/
coverage/
```

**Step 3: Create marketplace.json**

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
  "plugins": []
}
```

**Step 4: Create README.md**

```markdown
# Channel 47 Marketplace

Battle-tested Claude Code plugins from daily workflows.

## Installation

Add this marketplace to Claude Code:

\`\`\`bash
/plugin marketplace add yourusername/channel47-marketplace
\`\`\`

## Available Plugins

Coming soon.

## Philosophy

- **Publisher, not aggregator**: Only tools built and maintained by Channel 47
- **Quality over quantity**: Every plugin is battle-tested in daily use
- **Open source first**: Building for long-term impact and community

## Learn More

Visit [channel47.dev](https://channel47.dev) for usage guides, examples, and blog posts.
```

**Step 5: Commit initial structure**

```bash
git add .
git commit -m "feat: initialize marketplace repository structure"
```

### Task 2: Migrate Google Ads MCP plugin structure

**Files:**
- Create: `../channel47-marketplace/plugins/google-ads/.claude-plugin/plugin.json`
- Create: `../channel47-marketplace/plugins/google-ads/.mcp.json`
- Create: `../channel47-marketplace/plugins/google-ads/README.md`
- Create: `../channel47-marketplace/plugins/google-ads/GETTING_STARTED.md`
- Create: `../channel47-marketplace/plugins/google-ads/CHANGELOG.md`

**Step 1: Create plugin directory structure**

```bash
cd ../channel47-marketplace
mkdir -p plugins/google-ads/.claude-plugin
mkdir -p plugins/google-ads/src
mkdir -p plugins/google-ads/scripts
mkdir -p plugins/google-ads/config
```

**Step 2: Create plugin.json**

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

**Step 3: Create .mcp.json**

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

**Step 4: Create README.md**

```markdown
# Google Ads MCP Plugin

Query Google Ads data using GaQL with OAuth authentication.

## Quick Start

1. Install the plugin:
   \`\`\`bash
   /plugin install google-ads@channel47
   \`\`\`

2. Set up OAuth credentials (see [GETTING_STARTED.md](GETTING_STARTED.md))

3. Configure environment variables in Claude Code settings

## Tools Available

- List Google Ads accounts
- Execute GaQL queries
- Analyze campaign performance

## Documentation

- [Getting Started Guide](GETTING_STARTED.md) - Detailed setup walkthrough
- [Changelog](CHANGELOG.md) - Version history

## Support

Visit [channel47.dev/plugins/google-ads](https://channel47.dev/plugins/google-ads) for examples and guides.
```

**Step 5: Create GETTING_STARTED.md**

```markdown
# Getting Started with Google Ads MCP

## Prerequisites

- Python 3.10 or higher
- Google Ads account with API access
- Google Cloud project with Ads API enabled

## Step 1: Google Cloud Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing
3. Enable Google Ads API
4. Create OAuth 2.0 credentials (Desktop app)
5. Download client secrets JSON

## Step 2: Generate Refresh Token

1. Run the OAuth setup script:
   \`\`\`bash
   python ${CLAUDE_PLUGIN_ROOT}/scripts/generate_refresh_token.py
   \`\`\`

2. Follow browser prompts to authorize

3. Copy the refresh token from terminal output

## Step 3: Configure Claude Code

Add to Claude Code settings or .env:

\`\`\`
GOOGLE_ADS_DEVELOPER_TOKEN=your-developer-token
GOOGLE_ADS_LOGIN_CUSTOMER_ID=your-customer-id
GOOGLE_ADS_CLIENT_ID=your-client-id
GOOGLE_ADS_CLIENT_SECRET=your-client-secret
GOOGLE_ADS_REFRESH_TOKEN=your-refresh-token
\`\`\`

## Step 4: Verify Installation

Test the connection:
\`\`\`bash
python ${CLAUDE_PLUGIN_ROOT}/scripts/test_auth.py
\`\`\`

## Troubleshooting

Common issues and solutions will be documented here as they arise.
```

**Step 6: Create CHANGELOG.md**

```markdown
# Changelog - Google Ads MCP

All notable changes to this plugin will be documented in this file.

## [1.0.0] - 2025-12-20

### Added
- Initial release
- List accounts tool
- GaQL query tool
- OAuth authentication support
```

**Step 7: Update marketplace.json**

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

**Step 8: Commit plugin structure**

```bash
git add plugins/google-ads .claude-plugin/marketplace.json
git commit -m "feat: add Google Ads MCP plugin structure"
```

### Task 3: Create GitHub repository and link

**Files:**
- Modify: `../channel47-marketplace/.git/config`

**Step 1: Create GitHub repository**

Use GitHub CLI or web interface:
```bash
gh repo create channel47-marketplace --public --description "Battle-tested Claude Code plugins from daily workflows"
```

**Step 2: Add remote and push**

```bash
git remote add origin git@github.com:yourusername/channel47-marketplace.git
git branch -M main
git push -u origin main
```

**Step 3: Verify repository**

```bash
gh repo view
```

Expected: Repository details displayed

**Step 4: Commit tracking**

```bash
# No commit needed - remote setup complete
```

---

## Phase 2: Site Integration

### Task 4: Rename products to plugins

**Files:**
- Modify: `src/content/config.ts`
- Rename: `src/content/products/` → `src/content/plugins/`
- Rename: `src/pages/products/` → `src/pages/plugins/`

**Step 1: Update content collection schema**

In `src/content/config.ts`, replace `products` collection:

```typescript
const plugins = defineCollection({
  type: 'content',
  schema: z.object({
    slug: z.string(),
    featured: z.boolean().default(false),
    draft: z.boolean().default(false),
  }),
});
```

**Step 2: Update exports**

```typescript
export const collections = { blog, plugins };
```

**Step 3: Rename directories**

```bash
cd /Users/jackson/Documents/Access/1/a_projects/channel47
mv src/content/products src/content/plugins
mv src/pages/products src/pages/plugins
```

**Step 4: Update page imports**

In `src/pages/plugins/index.astro`:
```astro
---
import { getCollection } from 'astro:content';
const plugins = await getCollection('plugins', ({ data }) => !data.draft);
---
```

**Step 5: Commit rename**

```bash
git add -A
git commit -m "refactor: rename products to plugins"
```

### Task 5: Add Git submodule for marketplace

**Files:**
- Create: `.gitmodules`
- Create: `marketplace/` (submodule)

**Step 1: Add submodule**

```bash
cd /Users/jackson/Documents/Access/1/a_projects/channel47
git submodule add git@github.com:yourusername/channel47-marketplace.git marketplace
```

**Step 2: Initialize submodule**

```bash
git submodule update --init --recursive
```

**Step 3: Verify submodule**

```bash
ls -la marketplace/.claude-plugin/
```

Expected: marketplace.json exists

**Step 4: Commit submodule**

```bash
git add .gitmodules marketplace
git commit -m "feat: add marketplace as git submodule"
```

### Task 6: Create marketplace sync script

**Files:**
- Create: `scripts/sync-marketplace.ts`
- Modify: `astro.config.mjs`

**Step 1: Create TypeScript types**

```typescript
// scripts/types/marketplace.ts
export interface MarketplacePlugin {
  name: string;
  source: string;
  description: string;
  version: string;
  author: string;
  category: string;
  tags: string[];
}

export interface MarketplaceData {
  name: string;
  owner: {
    name: string;
    url: string;
  };
  description: string;
  metadata: {
    pluginRoot: string;
  };
  plugins: MarketplacePlugin[];
}

export interface PluginMerged extends MarketplacePlugin {
  editorialContent?: string;
  relatedPosts?: Array<{
    title: string;
    slug: string;
    date: Date;
  }>;
}
```

**Step 2: Create sync script**

```typescript
// scripts/sync-marketplace.ts
import * as fs from 'fs/promises';
import * as path from 'path';
import type { MarketplaceData, PluginMerged } from './types/marketplace';

const MARKETPLACE_PATH = path.join(process.cwd(), 'marketplace');
const PLUGINS_CONTENT_PATH = path.join(process.cwd(), 'src/content/plugins');
const OUTPUT_PATH = path.join(process.cwd(), 'src/data/merged-plugins.json');

async function loadMarketplaceData(): Promise<MarketplaceData> {
  const jsonPath = path.join(MARKETPLACE_PATH, '.claude-plugin/marketplace.json');
  const content = await fs.readFile(jsonPath, 'utf-8');
  return JSON.parse(content);
}

async function loadPluginMarkdown(slug: string): Promise<string | undefined> {
  const mdPath = path.join(PLUGINS_CONTENT_PATH, `${slug}.md`);
  try {
    return await fs.readFile(mdPath, 'utf-8');
  } catch {
    return undefined;
  }
}

async function syncMarketplace(): Promise<void> {
  console.log('Syncing marketplace data...');

  const marketplaceData = await loadMarketplaceData();
  const merged: PluginMerged[] = [];

  for (const plugin of marketplaceData.plugins) {
    const editorialContent = await loadPluginMarkdown(plugin.name);

    merged.push({
      ...plugin,
      editorialContent,
      relatedPosts: [], // Will be populated by blog discovery
    });
  }

  await fs.mkdir(path.dirname(OUTPUT_PATH), { recursive: true });
  await fs.writeFile(OUTPUT_PATH, JSON.stringify(merged, null, 2));

  console.log(`✓ Synced ${merged.length} plugins to ${OUTPUT_PATH}`);
}

syncMarketplace().catch(console.error);
```

**Step 3: Update package.json scripts**

```json
{
  "scripts": {
    "sync-marketplace": "tsx scripts/sync-marketplace.ts",
    "prebuild": "npm run sync-marketplace",
    "dev": "npm run sync-marketplace && astro dev"
  }
}
```

**Step 4: Test sync**

```bash
npm run sync-marketplace
```

Expected: `src/data/merged-plugins.json` created

**Step 5: Commit sync script**

```bash
git add scripts/sync-marketplace.ts scripts/types/marketplace.ts package.json
git commit -m "feat: add marketplace sync script for build-time integration"
```

### Task 7: Create plugin page template

**Files:**
- Modify: `src/pages/plugins/[...slug].astro`

**Step 1: Update plugin page template**

```astro
---
// src/pages/plugins/[...slug].astro
import { getCollection } from 'astro:content';
import BaseLayout from '../../layouts/BaseLayout.astro';
import mergedPlugins from '../../data/merged-plugins.json';

export async function getStaticPaths() {
  const plugins = await getCollection('plugins');

  return plugins.map(plugin => {
    const marketplaceData = mergedPlugins.find(p => p.name === plugin.slug);

    return {
      params: { slug: plugin.slug },
      props: {
        plugin,
        marketplaceData,
      },
    };
  });
}

const { plugin, marketplaceData } = Astro.props;
const { Content } = await plugin.render();
---

<BaseLayout title={marketplaceData?.name || plugin.slug} description={marketplaceData?.description || ''}>
  <article class="max-w-4xl mx-auto px-6 py-16">
    {/* Header */}
    <header class="mb-8">
      <h1 class="text-4xl font-bold text-charcoal-900">{marketplaceData?.name || plugin.slug}</h1>
      <p class="mt-4 text-xl text-charcoal-700">{marketplaceData?.description}</p>
    </header>

    {/* Install CTA */}
    <div class="my-12 p-8 bg-cream-100 border border-charcoal-800/10 rounded-xl">
      <h2 class="text-lg font-semibold text-charcoal-900 mb-4">Install</h2>

      <details class="mb-4 group">
        <summary class="cursor-pointer text-sm text-coral-600 hover:text-coral-700 mb-2">
          First time? Add Channel 47 marketplace first
        </summary>
        <div class="mt-2 p-4 bg-white rounded-lg border border-charcoal-800/10">
          <p class="text-sm text-charcoal-700 mb-2">Step 1: Add marketplace</p>
          <code class="block p-3 bg-charcoal-900 text-cream-100 rounded text-sm font-mono">
            /plugin marketplace add yourusername/channel47-marketplace
          </code>
        </div>
      </details>

      <div class="p-4 bg-white rounded-lg border border-charcoal-800/10">
        <p class="text-sm text-charcoal-700 mb-2">Install plugin:</p>
        <code class="block p-3 bg-charcoal-900 text-cream-100 rounded text-sm font-mono">
          /plugin install {marketplaceData?.name}@channel47
        </code>
      </div>

      <div class="mt-4 flex gap-4 text-sm text-charcoal-600">
        <span>v{marketplaceData?.version}</span>
        <span>•</span>
        <span class="capitalize">{marketplaceData?.category}</span>
      </div>
    </div>

    {/* Editorial Content */}
    <div class="prose prose-lg max-w-none">
      <Content />
    </div>

    {/* Related Posts - placeholder */}
    {marketplaceData?.relatedPosts && marketplaceData.relatedPosts.length > 0 && (
      <div class="mt-12 p-6 bg-cream-100 rounded-xl">
        <h3 class="text-lg font-semibold text-charcoal-900 mb-4">See it in action:</h3>
        <ul class="space-y-3">
          {marketplaceData.relatedPosts.map(post => (
            <li>
              <a href={`/blog/${post.slug}`} class="text-coral-600 hover:text-coral-700">
                {post.title}
              </a>
              <span class="text-sm text-charcoal-600 ml-2">
                {new Date(post.date).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })}
              </span>
            </li>
          ))}
        </ul>
      </div>
    )}
  </article>
</BaseLayout>
```

**Step 2: Test plugin page**

```bash
npm run dev
```

Open: http://localhost:4321/plugins/google-ads

**Step 3: Commit template**

```bash
git add src/pages/plugins/\[...slug\].astro
git commit -m "feat: create plugin page template with install CTA"
```

### Task 8: Create plugins index page

**Files:**
- Modify: `src/pages/plugins/index.astro`

**Step 1: Update index page**

```astro
---
// src/pages/plugins/index.astro
import { getCollection } from 'astro:content';
import BaseLayout from '../../layouts/BaseLayout.astro';
import mergedPlugins from '../../data/merged-plugins.json';

const plugins = await getCollection('plugins', ({ data }) => !data.draft);

// Merge with marketplace data
const enrichedPlugins = plugins.map(plugin => {
  const marketplaceData = mergedPlugins.find(p => p.name === plugin.slug);
  return { ...plugin, marketplaceData };
});

// Get unique categories
const categories = ['all', ...new Set(mergedPlugins.map(p => p.category))];
---

<BaseLayout title="Plugins" description="Battle-tested Claude Code plugins from daily workflows.">
  <section class="max-w-5xl mx-auto px-6 py-16">
    <h1 class="text-4xl font-bold text-charcoal-900">Plugins</h1>
    <p class="mt-4 text-lg text-charcoal-700 max-w-2xl">
      Battle-tested Claude Code plugins from daily workflows. All free. Quality over quantity.
    </p>

    {/* Filter Bar - Static for now */}
    <div class="mt-8 flex gap-4 text-sm flex-wrap">
      {categories.map(cat => (
        <button
          class={`px-4 py-2 rounded-lg transition-colors capitalize ${
            cat === 'all'
              ? 'bg-charcoal-900 text-white'
              : 'text-charcoal-700 hover:bg-charcoal-100'
          }`}
        >
          {cat}
        </button>
      ))}
    </div>

    {/* Plugin Grid */}
    <div class="mt-12">
      {enrichedPlugins.length === 0 ? (
        <p class="text-charcoal-600">Plugins coming soon. Check back later.</p>
      ) : (
        <div class="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
          {enrichedPlugins.map(({ slug, data, marketplaceData }) => (
            <a
              href={`/plugins/${slug}`}
              class="group block p-6 border border-charcoal-800/10 rounded-xl hover:border-coral-600/30 hover:shadow-lg transition-all"
            >
              <div class="flex items-center justify-between">
                <span class="text-xs font-medium text-coral-600 uppercase tracking-wide">
                  {marketplaceData?.category || 'plugin'}
                </span>
                {data.featured && (
                  <span class="text-xs font-medium text-charcoal-700 uppercase tracking-wide px-2 py-1 bg-charcoal-100 rounded">
                    ★
                  </span>
                )}
              </div>
              <h2 class="mt-2 text-lg font-semibold text-charcoal-900 group-hover:text-coral-600 transition-colors">
                {marketplaceData?.name || slug}
              </h2>
              <p class="mt-2 text-sm text-charcoal-600 line-clamp-2">
                {marketplaceData?.description || ''}
              </p>
              <div class="mt-4 flex items-center justify-between text-xs text-charcoal-500">
                <span>by {marketplaceData?.author || 'Unknown'}</span>
                <span>v{marketplaceData?.version}</span>
              </div>
            </a>
          ))}
        </div>
      )}
    </div>
  </section>
</BaseLayout>
```

**Step 2: Test index page**

```bash
npm run dev
```

Open: http://localhost:4321/plugins

**Step 3: Commit index page**

```bash
git add src/pages/plugins/index.astro
git commit -m "feat: create plugins index page with category filter"
```

---

## Phase 3: Bidirectional Linking

### Task 9: Add toolsUsed to blog schema

**Files:**
- Modify: `src/content/config.ts`

**Step 1: Update blog collection schema**

```typescript
const blog = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    date: z.coerce.date(),
    draft: z.boolean().default(false),
    tags: z.array(z.string()).default([]),
    toolsUsed: z.array(z.object({
      slug: z.string(),
      source: z.enum(['channel47', 'external']),
      installCommand: z.string().optional(),
    })).optional(),
  }),
});
```

**Step 2: Run type generation**

```bash
npm run astro check
```

Expected: No errors, types regenerated

**Step 3: Commit schema update**

```bash
git add src/content/config.ts .astro/
git commit -m "feat: add toolsUsed field to blog schema"
```

### Task 10: Create blog-plugin discovery script

**Files:**
- Modify: `scripts/sync-marketplace.ts`

**Step 1: Add blog discovery logic**

```typescript
// Add to scripts/sync-marketplace.ts

import { getCollection } from 'astro:content';

async function discoverRelatedPosts(pluginSlug: string) {
  const blogPosts = await getCollection('blog', ({ data }) => !data.draft);

  const relatedPosts = blogPosts
    .filter(post =>
      post.data.toolsUsed?.some(
        tool => tool.slug === pluginSlug && tool.source === 'channel47'
      )
    )
    .map(post => ({
      title: post.data.title,
      slug: post.slug,
      date: post.data.date,
    }))
    .sort((a, b) => b.date.getTime() - a.date.getTime());

  return relatedPosts;
}

async function syncMarketplace(): Promise<void> {
  console.log('Syncing marketplace data...');

  const marketplaceData = await loadMarketplaceData();
  const merged: PluginMerged[] = [];

  for (const plugin of marketplaceData.plugins) {
    const editorialContent = await loadPluginMarkdown(plugin.name);
    const relatedPosts = await discoverRelatedPosts(plugin.name);

    merged.push({
      ...plugin,
      editorialContent,
      relatedPosts,
    });
  }

  await fs.mkdir(path.dirname(OUTPUT_PATH), { recursive: true });
  await fs.writeFile(OUTPUT_PATH, JSON.stringify(merged, null, 2));

  console.log(`✓ Synced ${merged.length} plugins`);
  console.log(`✓ Discovered related posts for ${merged.filter(p => p.relatedPosts && p.relatedPosts.length > 0).length} plugins`);
}
```

**Step 2: Test discovery**

```bash
npm run sync-marketplace
```

Expected: "Discovered related posts for X plugins"

**Step 3: Commit discovery**

```bash
git add scripts/sync-marketplace.ts
git commit -m "feat: add blog-plugin auto-discovery"
```

### Task 11: Create ToolsMentioned component

**Files:**
- Create: `src/components/ToolsMentioned.astro`

**Step 1: Create component**

```astro
---
// src/components/ToolsMentioned.astro
import mergedPlugins from '../data/merged-plugins.json';

interface Props {
  tools: Array<{
    slug: string;
    source: 'channel47' | 'external';
    installCommand?: string;
  }>;
}

const { tools } = Astro.props;

const enrichedTools = tools.map(tool => {
  if (tool.source === 'channel47') {
    const pluginData = mergedPlugins.find(p => p.name === tool.slug);
    return {
      ...tool,
      name: pluginData?.name || tool.slug,
      description: pluginData?.description,
      url: `/plugins/${tool.slug}`,
      installCmd: `/plugin install ${tool.slug}@channel47`,
    };
  }
  return {
    ...tool,
    name: tool.slug,
    url: null,
    installCmd: tool.installCommand,
  };
});
---

{enrichedTools.length > 0 && (
  <aside class="my-8 p-6 bg-cream-100 border border-charcoal-800/10 rounded-xl">
    <h3 class="text-lg font-semibold text-charcoal-900 mb-4">Tools mentioned in this post:</h3>
    <div class="space-y-4">
      {enrichedTools.map(tool => (
        <div class="p-4 bg-white rounded-lg">
          {tool.url ? (
            <a href={tool.url} class="text-coral-600 hover:text-coral-700 font-medium flex items-center gap-2">
              ⚡ {tool.name}
            </a>
          ) : (
            <p class="text-charcoal-900 font-medium flex items-center gap-2">
              🔗 {tool.name}
            </p>
          )}
          {tool.description && (
            <p class="mt-1 text-sm text-charcoal-600">{tool.description}</p>
          )}
          {tool.installCmd && (
            <code class="mt-2 block p-2 bg-charcoal-900 text-cream-100 rounded text-xs font-mono">
              {tool.installCmd}
            </code>
          )}
        </div>
      ))}
    </div>
  </aside>
)}
```

**Step 2: Add to blog post template**

In `src/pages/blog/[...slug].astro`:

```astro
---
import ToolsMentioned from '../../components/ToolsMentioned.astro';
// ... existing imports
---

<BaseLayout>
  <article>
    <header>...</header>

    {post.data.toolsUsed && <ToolsMentioned tools={post.data.toolsUsed} />}

    <Content />
  </article>
</BaseLayout>
```

**Step 3: Commit component**

```bash
git add src/components/ToolsMentioned.astro src/pages/blog/\[...slug\].astro
git commit -m "feat: add ToolsMentioned component to blog posts"
```

### Task 12: Test bidirectional linking flow

**Files:**
- Create: `src/content/blog/test-google-ads.md`
- Create: `src/content/plugins/google-ads.md`

**Step 1: Create test blog post**

```markdown
---
title: "Testing Google Ads Plugin"
description: "A test post to verify bidirectional linking"
date: 2025-12-20
draft: true
tags: ["test"]
toolsUsed:
  - slug: google-ads
    source: channel47
---

This is a test post mentioning the Google Ads plugin.
```

**Step 2: Create plugin editorial content**

```markdown
---
slug: "google-ads"
featured: true
draft: false
---

## What it does

The Google Ads MCP plugin allows you to query your Google Ads data directly from Claude Code using GaQL.

## Setup

Follow the [Getting Started guide](https://github.com/yourusername/channel47-marketplace/blob/main/plugins/google-ads/GETTING_STARTED.md) for detailed setup instructions.
```

**Step 3: Run sync and build**

```bash
npm run sync-marketplace
npm run build
```

Expected: Build succeeds, related posts discovered

**Step 4: Verify in dev server**

```bash
npm run dev
```

Check:
- `/blog/test-google-ads` shows ToolsMentioned component
- `/plugins/google-ads` shows "See it in action" section with test post

**Step 5: Commit test content**

```bash
git add src/content/
git commit -m "test: add test content for bidirectional linking"
```

---

## Phase 4: Polish & Deploy

### Task 13: Set up Vercel webhook for auto-rebuild

**Files:**
- Create: `.github/workflows/trigger-vercel.yml` (in marketplace repo)

**Step 1: Create GitHub Actions workflow in marketplace**

```yaml
# .github/workflows/trigger-vercel.yml
name: Trigger Vercel Deploy

on:
  push:
    branches:
      - main
    paths:
      - '.claude-plugin/marketplace.json'
      - 'plugins/**'

jobs:
  trigger-deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Trigger Vercel Deploy Hook
        run: |
          curl -X POST "${{ secrets.VERCEL_DEPLOY_HOOK }}"
```

**Step 2: Add secret to marketplace repo**

1. Deploy channel47 to Vercel first
2. Get deploy hook URL from Vercel dashboard
3. Add as `VERCEL_DEPLOY_HOOK` secret in marketplace repo settings

**Step 3: Test webhook**

```bash
cd ../channel47-marketplace
git add .github/workflows/trigger-vercel.yml
git commit -m "feat: add Vercel auto-deploy trigger"
git push
```

Expected: Vercel deploy triggered

**Step 4: No commit needed in main repo**

This is marketplace-only configuration.

### Task 14: Update navigation to use /plugins

**Files:**
- Modify: `src/layouts/BaseLayout.astro` (or nav component)

**Step 1: Find navigation component**

```bash
grep -r "products" src/layouts/ src/components/
```

**Step 2: Update all /products links to /plugins**

Example in BaseLayout.astro:

```astro
<nav>
  <a href="/blog">Blog</a>
  <a href="/plugins">Plugins</a>
  <a href="/about">About</a>
</nav>
```

**Step 3: Search for any remaining references**

```bash
grep -r "/products" src/
```

Expected: No matches

**Step 4: Commit navigation update**

```bash
git add src/layouts/ src/components/
git commit -m "refactor: update navigation to use /plugins"
```

### Task 15: Clean up test content and finalize

**Files:**
- Delete: `src/content/blog/test-google-ads.md`
- Modify: `src/content/plugins/google-ads.md` (remove draft flag)

**Step 1: Remove test blog post**

```bash
rm src/content/blog/test-google-ads.md
```

**Step 2: Finalize Google Ads plugin page**

Update `src/content/plugins/google-ads.md` with real editorial content:

```markdown
---
slug: "google-ads"
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
2. Follow [Getting Started Guide](https://github.com/yourusername/channel47-marketplace/blob/main/plugins/google-ads/GETTING_STARTED.md)
3. Configure your credentials in Claude Code settings

## Example queries

Ask Claude:
- "Show me all my Google Ads accounts"
- "Query campaign performance for last 30 days"
- "What's my average CPC across all campaigns?"
```

**Step 3: Run final sync and build**

```bash
npm run sync-marketplace
npm run build
```

Expected: Clean build, no errors

**Step 4: Test production preview**

```bash
npm run preview
```

Verify all pages work correctly.

**Step 5: Commit final content**

```bash
git add src/content/
git commit -m "docs: finalize Google Ads plugin editorial content"
```

### Task 16: Deploy to production

**Files:**
- None (deployment only)

**Step 1: Push to main**

```bash
git push origin main
```

**Step 2: Verify Vercel deployment**

```bash
vercel --prod
```

Or wait for auto-deploy from GitHub integration.

**Step 3: Test production site**

Visit https://channel47.dev/plugins

Verify:
- Plugin index page works
- Google Ads plugin page displays correctly
- Install instructions are clear
- Navigation works

**Step 4: Update marketplace README with live URL**

In `../channel47-marketplace/README.md`:

```markdown
## Installation

Add this marketplace to Claude Code:

\`\`\`bash
/plugin marketplace add yourusername/channel47-marketplace
\`\`\`

## Available Plugins

- [Google Ads MCP](https://channel47.dev/plugins/google-ads) - Query Google Ads data using GaQL
```

**Step 5: Push marketplace update**

```bash
cd ../channel47-marketplace
git add README.md
git commit -m "docs: add live plugin URLs"
git push
```

Expected: Site auto-rebuilds via webhook

---

## Verification Checklist

After completing all tasks, verify:

**Marketplace Repository:**
- [ ] Repository exists at `yourusername/channel47-marketplace`
- [ ] marketplace.json has correct structure
- [ ] Google Ads plugin has complete structure
- [ ] README has clear installation instructions
- [ ] Vercel webhook triggers on push

**Site Integration:**
- [ ] /plugins page displays correctly
- [ ] /plugins/google-ads page shows merged data
- [ ] Install CTA has progressive disclosure
- [ ] Git submodule updates on build
- [ ] sync-marketplace runs before build

**Bidirectional Linking:**
- [ ] Blog posts can specify toolsUsed
- [ ] ToolsMentioned component displays on blog posts
- [ ] Related posts auto-discovered on plugin pages
- [ ] Links work in both directions

**Production:**
- [ ] Site deployed to Vercel
- [ ] All navigation links work
- [ ] Plugin installation flow is clear
- [ ] Marketplace webhook triggers rebuilds
- [ ] No broken links or 404s

---

## Post-Implementation: Adding New Plugins

To add a new plugin after this implementation:

1. **In marketplace repo:**
   - Create plugin directory structure
   - Add plugin to marketplace.json
   - Write documentation (README, GETTING_STARTED, CHANGELOG)
   - Commit and push

2. **In site repo:**
   - Create `src/content/plugins/{slug}.md` with editorial content
   - Optionally write blog post with `toolsUsed` frontmatter
   - Commit and push (or let webhook auto-rebuild)

3. **Users install:**
   - First time: `/plugin marketplace add yourusername/channel47-marketplace`
   - Then: `/plugin install {plugin-name}@channel47`

---

## Notes

- DRY: marketplace.json is single source of truth for technical metadata
- YAGNI: No client-side filtering yet - add when multiple plugins exist
- TDD: N/A for this integration work (mostly configuration and templates)
- Frequent commits: Each task has explicit commit step

## Future Enhancements

Consider later:
- Client-side category filtering with Alpine.js or vanilla JS
- Plugin version update notifications
- Download statistics tracking
- Community plugin submission process
- Automated testing for marketplace.json schema
