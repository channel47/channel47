# Monorepo Marketplace Design

This document outlines the strategy for consolidating the Channel 47 marketplace and website into a unified monorepo, enabling open-source distribution, audience growth, and frictionless installation for Claude Desktop users.

---

## Implementation Status

| Phase | Status | Completed |
|-------|--------|-----------|
| Phase 1: Monorepo Consolidation | Pending | - |
| Phase 2: Site Restructure | Pending | - |
| Phase 3: Claude Desktop Distribution | Pending | - |
| Phase 4: SEO Foundation | Pending | - |
| Phase 5: Newsletter Setup | Pending | - |
| Phase 6: Open Source Transition | Pending | - |

---

## Strategic Context

### Goals
1. **Audience growth first** - Maximize newsletter signups and SEO traffic
2. **Open source everything** - All plugins and skills become free
3. **Claude Desktop focus** - Primary distribution for non-Claude Code users
4. **Hybrid SEO strategy** - Ecosystem content + tool-specific content

### Newsletter Strategy
Combination of four content angles:
- Tool updates and changelogs
- Curated AI tooling digest
- Media buying + AI intersection
- Behind-the-build process sharing

---

## Current State

### Marketplace (`channel47-marketplace`)
- 4 plugins: Google Ads Specialist, Creative Designer, Copywriting Expert, Prompt Enhancer
- 2 MCP servers:
  - Google Ads: npm-distributed (`@channel47/google-ads-mcp`)
  - Creative Designer: Local Python (FastMCP)
- Well-structured with skills, commands, agents, hooks
- 78 markdown documentation files

### Website (`channel47`)
- Astro static site with custom CSS design system
- Skills (products) + Tools (free MCP) pages
- Blog with 3 posts
- Beehiiv integration ready but unconfigured
- Missing: sitemap, robots.txt, JSON-LD, analytics

---

## Phase 1: Monorepo Consolidation

**Priority:** Critical
**Dependency:** None

### Target Structure

```
channel47/
├── .claude-plugin/
│   └── marketplace.json           # Marketplace catalog
├── plugins/
│   ├── google-ads-specialist/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   ├── .mcp.json
│   │   ├── skills/
│   │   ├── README.md
│   │   └── CHANGELOG.md
│   ├── creative-designer/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   ├── .mcp.json
│   │   ├── pyproject.toml         # NEW: PyPI publishing
│   │   ├── src/nanobanana_mcp.py
│   │   └── skills/
│   ├── copywriting-expert/
│   └── prompt-enhancer/
├── site/
│   ├── src/
│   ├── astro.config.mjs
│   └── package.json
├── .github/
│   └── workflows/
│       └── deploy.yml
├── package.json                   # Workspace root
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

### Marketplace Configuration

**File:** `.claude-plugin/marketplace.json`

```json
{
  "name": "channel47",
  "owner": {
    "name": "Jackson",
    "email": "..."
  },
  "metadata": {
    "pluginRoot": "./plugins",
    "description": "Open-source AI tools for media buyers and marketers"
  },
  "plugins": [
    {
      "name": "google-ads-specialist",
      "source": "google-ads-specialist",
      "description": "Google Ads campaign management with GAQL",
      "version": "3.1.0"
    },
    {
      "name": "creative-designer",
      "source": "creative-designer",
      "description": "AI image generation with Gemini",
      "version": "1.2.0"
    },
    {
      "name": "copywriting-expert",
      "source": "copywriting-expert",
      "description": "Master copywriting frameworks",
      "version": "1.0.0"
    },
    {
      "name": "prompt-enhancer",
      "source": "prompt-enhancer",
      "description": "Optimize prompts for Claude",
      "version": "1.0.0"
    }
  ]
}
```

Users install with: `/plugin marketplace add github:channel47/channel47`

### Tasks

- [ ] Create new unified repo (or restructure existing)
- [ ] Move `channel47-marketplace/plugins/` into `channel47/plugins/`
- [ ] Move current site code into `channel47/site/`
- [ ] Create root `marketplace.json` with `pluginRoot: "./plugins"`
- [ ] Set up npm workspaces in root `package.json`
- [ ] Validate marketplace structure: `/plugin validate .`
- [ ] Update GitHub repo settings and description

### Technical Notes

From Claude Code marketplace documentation:
- `pluginRoot` metadata field sets base directory for relative plugin paths
- Paths cannot contain `..` to traverse outside marketplace directory
- Each plugin must be self-contained (current structure already satisfies this)
- Symlinks are honored during plugin copying if shared resources needed

---

## Phase 2: Site Restructure

**Priority:** High
**Dependency:** Phase 1

### Simplified URL Structure

```
channel47.dev/
├── /                              # Homepage
├── /tools/                        # Tool directory (all plugins)
│   ├── /tools/google-ads/         # Combined: plugin + MCP + skills
│   ├── /tools/creative-designer/
│   ├── /tools/copywriting/
│   └── /tools/prompt-enhancer/
├── /blog/                         # All content (posts + guides)
│   ├── /blog/what-is-mcp/
│   ├── /blog/gaql-queries-reference/
│   └── /blog/mcp-servers-for-marketers/
└── /changelog/                    # Optional, could be blog posts
```

**Key Changes:**
- Remove `/plugins/` and `/skills/` routes - everything is a "tool"
- Merge `/guides/` into `/blog/` with tags
- Each tool page has sections: MCP install, Claude Code install, skills reference

### Content Collections Configuration

**File:** `site/src/content/config.ts`

```typescript
import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

// Pull plugin READMEs for tool pages
const plugins = defineCollection({
  loader: glob({
    pattern: "*/README.md",
    base: "../plugins",
    generateId: ({ entry }) => entry.split('/')[0]
  }),
  schema: z.object({
    name: z.string(),
    version: z.string(),
    description: z.string(),
    category: z.enum(['marketing', 'creative', 'writing', 'development']),
  })
});

// Pull changelogs
const changelogs = defineCollection({
  loader: glob({
    pattern: "*/CHANGELOG.md",
    base: "../plugins"
  }),
});

// Blog posts in site directory
const posts = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/posts" }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    date: z.coerce.date(),
    updated: z.coerce.date().optional(),
    tags: z.array(z.string()),
    category: z.enum(['ecosystem', 'tool-specific', 'industry']),
    ogImage: z.string().optional(),
  })
});

export const collections = { plugins, changelogs, posts };
```

### Dynamic Tool Pages

**File:** `site/src/pages/tools/[slug].astro`

```astro
---
import { getCollection } from 'astro:content';
import BaseLayout from '../../layouts/BaseLayout.astro';
import InstallTabs from '../../components/InstallTabs.astro';

export async function getStaticPaths() {
  const plugins = await getCollection('plugins');
  return plugins.map(plugin => ({
    params: { slug: plugin.id },
    props: { plugin }
  }));
}

const { plugin } = Astro.props;
const { Content } = await plugin.render();
---

<BaseLayout title={plugin.data.name}>
  <Content />
  <InstallTabs plugin={plugin.id} />
</BaseLayout>
```

### Tasks

- [ ] Update Astro content config to pull from `../plugins/`
- [ ] Create `InstallTabs.astro` component with Claude Desktop / Claude Code tabs
- [ ] Create unified tool page template
- [ ] Remove `/plugins/` and `/skills/` routes
- [ ] Merge guides into blog with appropriate tags
- [ ] Update internal links throughout site

---

## Phase 3: Claude Desktop Distribution

**Priority:** High
**Dependency:** Phase 1

### Distribution Models

**Model 1: npm-distributed (Google Ads)** - Already complete

```json
{
  "mcpServers": {
    "google-ads": {
      "command": "npx",
      "args": ["-y", "@channel47/google-ads-mcp@latest"],
      "env": {
        "GOOGLE_ADS_DEVELOPER_TOKEN": "your-token",
        "GOOGLE_ADS_CLIENT_ID": "your-client-id",
        "GOOGLE_ADS_CLIENT_SECRET": "your-client-secret",
        "GOOGLE_ADS_REFRESH_TOKEN": "your-refresh-token"
      }
    }
  }
}
```

**Model 2: Python/PyPI (Creative Designer)** - Needs work

Target state (after PyPI publish):
```json
{
  "mcpServers": {
    "creative-designer": {
      "command": "uvx",
      "args": ["channel47-creative-designer"],
      "env": {
        "GEMINI_API_KEY": "your-gemini-key"
      }
    }
  }
}
```

### Config File Locations

From Claude Help Center documentation:
- **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

### InstallTabs Component

**File:** `site/src/components/InstallTabs.astro`

```astro
---
interface Props {
  plugin: 'google-ads' | 'creative-designer';
}

const { plugin } = Astro.props;

const configs = {
  'google-ads': {
    npm: true,
    claudeDesktop: `{
  "mcpServers": {
    "google-ads": {
      "command": "npx",
      "args": ["-y", "@channel47/google-ads-mcp@latest"],
      "env": {
        "GOOGLE_ADS_DEVELOPER_TOKEN": "your-token",
        "GOOGLE_ADS_CLIENT_ID": "your-client-id",
        "GOOGLE_ADS_CLIENT_SECRET": "your-client-secret",
        "GOOGLE_ADS_REFRESH_TOKEN": "your-refresh-token"
      }
    }
  }
}`,
    claudeCode: '/plugin marketplace add github:channel47/channel47\n/plugin install google-ads-specialist@channel47'
  },
  'creative-designer': {
    npm: false,
    claudeDesktop: `{
  "mcpServers": {
    "creative-designer": {
      "command": "uvx",
      "args": ["channel47-creative-designer"],
      "env": {
        "GEMINI_API_KEY": "your-gemini-key"
      }
    }
  }
}`,
    claudeCode: '/plugin marketplace add github:channel47/channel47\n/plugin install creative-designer@channel47'
  }
};

const config = configs[plugin];
---

<div class="install-tabs">
  <div class="tab-buttons">
    <button data-tab="claude-desktop" class="active">Claude Desktop</button>
    <button data-tab="claude-code">Claude Code</button>
  </div>

  <div class="tab-content" data-content="claude-desktop">
    <p>Add to your <code>claude_desktop_config.json</code>:</p>
    <pre><code>{config.claudeDesktop}</code></pre>
    <button class="copy-btn" data-copy={config.claudeDesktop}>Copy</button>
  </div>

  <div class="tab-content" data-content="claude-code" hidden>
    <pre><code>{config.claudeCode}</code></pre>
    <button class="copy-btn" data-copy={config.claudeCode}>Copy</button>
  </div>
</div>

<script>
  // Tab switching logic
  document.querySelectorAll('.tab-buttons button').forEach(btn => {
    btn.addEventListener('click', () => {
      const tab = btn.dataset.tab;
      document.querySelectorAll('.tab-buttons button').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      document.querySelectorAll('.tab-content').forEach(c => c.hidden = c.dataset.content !== tab);
    });
  });

  // Copy functionality
  document.querySelectorAll('.copy-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      navigator.clipboard.writeText(btn.dataset.copy);
      btn.textContent = 'Copied!';
      setTimeout(() => btn.textContent = 'Copy', 2000);
    });
  });
</script>
```

### Tasks

- [ ] Create `InstallTabs.astro` component
- [ ] Add `pyproject.toml` to `plugins/creative-designer/`
- [ ] Publish Creative Designer to PyPI as `channel47-creative-designer`
- [ ] Test uvx installation: `uvx channel47-creative-designer`
- [ ] Document env var setup for each tool
- [ ] Add copy-to-clipboard for config JSON

---

## Phase 4: SEO Foundation

**Priority:** Medium
**Dependency:** Phase 2

### Technical SEO

**robots.txt** (`site/public/robots.txt`):
```
User-agent: *
Allow: /

Sitemap: https://channel47.dev/sitemap-index.xml
```

**Astro Sitemap Integration:**
```bash
npx astro add sitemap
```

```javascript
// site/astro.config.mjs
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://channel47.dev',
  integrations: [sitemap()],
});
```

### JSON-LD Schemas

**Tool Schema** (`site/src/components/SEO/ToolSchema.astro`):
```astro
---
interface Props {
  name: string;
  description: string;
  url: string;
  version: string;
}
const { name, description, url, version } = Astro.props;
---

<script type="application/ld+json" set:html={JSON.stringify({
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": name,
  "description": description,
  "url": url,
  "applicationCategory": "DeveloperApplication",
  "operatingSystem": "Cross-platform",
  "version": version,
  "author": {
    "@type": "Organization",
    "name": "Channel 47"
  },
  "offers": {
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "USD"
  }
})} />
```

**Article Schema** (`site/src/components/SEO/ArticleSchema.astro`):
```astro
---
interface Props {
  title: string;
  description: string;
  datePublished: Date;
  dateModified?: Date;
  url: string;
}
const props = Astro.props;
---

<script type="application/ld+json" set:html={JSON.stringify({
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": props.title,
  "description": props.description,
  "datePublished": props.datePublished.toISOString(),
  "dateModified": (props.dateModified || props.datePublished).toISOString(),
  "url": props.url,
  "author": {
    "@type": "Person",
    "name": "Jackson",
    "url": "https://channel47.dev"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Channel 47",
    "url": "https://channel47.dev"
  }
})} />
```

### Content Priority

| Priority | Title | Type | Target Keywords |
|----------|-------|------|-----------------|
| 1 | What is MCP? Model Context Protocol Explained | Ecosystem | "what is mcp", "model context protocol" |
| 2 | MCP Servers for Claude Desktop: Setup Guide | Ecosystem | "claude desktop mcp", "mcp server setup" |
| 3 | GAQL Query Reference: 50+ Google Ads Queries | Tool-specific | "gaql queries", "google ads query language" |
| 4 | Automating Google Ads Audits with AI | Tool-specific | "google ads audit automation" |
| 5 | Claude Code Plugins: Complete Guide | Ecosystem | "claude code plugins" |

### Tasks

- [ ] Create `robots.txt` in `site/public/`
- [ ] Install and configure `@astrojs/sitemap`
- [ ] Create `ToolSchema.astro` component
- [ ] Create `ArticleSchema.astro` component
- [ ] Add schemas to all tool and blog pages
- [ ] Create Open Graph image template
- [ ] Add canonical URLs to all pages

---

## Phase 5: Newsletter Setup

**Priority:** Medium
**Dependency:** None (can run in parallel)

### Subscriber Segmentation

| Tag | Entry Point | Content Focus |
|-----|-------------|---------------|
| `general` | Homepage | All content |
| `tools-user` | Any /tools/ page | Tool updates |
| `google-ads` | Google Ads tool page | Google Ads specific |
| `creative` | Creative Designer page | Image gen tips |
| `blog-reader` | Blog posts | Curated digest |

### EmailSignup Component

**File:** `site/src/components/EmailSignup.astro`

```astro
---
interface Props {
  tag?: string;
  context?: 'tool' | 'blog' | 'homepage';
}

const { tag = 'general', context = 'homepage' } = Astro.props;

const copy = {
  homepage: {
    title: "Get the newsletter",
    description: "Open-source AI tools, workflow tips, and what I'm building. No spam.",
    button: "Subscribe"
  },
  tool: {
    title: "Get notified of updates",
    description: "New features, fixes, and tips for this tool.",
    button: "Subscribe"
  },
  blog: {
    title: "More like this",
    description: "Weekly AI tooling insights for marketers and builders.",
    button: "Subscribe"
  }
};

const { title, description, button } = copy[context];
const BEEHIIV_FORM_URL = import.meta.env.BEEHIIV_FORM_URL;
---

<form action={BEEHIIV_FORM_URL} method="POST" class="email-signup">
  <input type="hidden" name="tag" value={tag} />

  <div class="signup-content">
    <h3>{title}</h3>
    <p>{description}</p>
  </div>

  <div class="signup-form">
    <input type="email" name="email" placeholder="you@example.com" required />
    <button type="submit">{button}</button>
  </div>
</form>
```

### Beehiiv Configuration

1. Create publication in Beehiiv
2. Get form action URL from Settings > Embeds > Custom Form
3. Configure custom field for `tag` parameter
4. Set up welcome email sequences per tag

**Environment variable:** `site/.env`
```
BEEHIIV_FORM_URL=https://api.beehiiv.com/v2/publications/YOUR_PUB_ID/subscriptions
```

### Content Cadence

| Frequency | Content Type |
|-----------|--------------|
| Per release | Tool updates (changelog, new features) |
| Biweekly | Curated AI tooling digest |
| Monthly | Behind-the-build (process, lessons) |
| As relevant | Media buying + AI intersection |

### Tasks

- [ ] Create Beehiiv publication
- [ ] Configure custom field for tag parameter
- [ ] Get form action URL and add to `.env`
- [ ] Update `EmailSignup.astro` with tag support
- [ ] Apply tags per location (homepage, tools, blog)
- [ ] Set up welcome email sequences
- [ ] Create first newsletter issue

---

## Phase 6: Open Source Transition

**Priority:** Low
**Dependency:** Phases 1-5

### Tasks

- [ ] Remove Stripe integration from site
- [ ] Update skill pages: remove pricing, add "Free & Open Source" badge
- [ ] Verify MIT license on all plugins
- [ ] Create `CONTRIBUTING.md` in repo root
- [ ] Add "Star on GitHub" CTA to tool pages
- [ ] Update homepage value prop (free tools, community-driven)
- [ ] Update README with contribution guidelines
- [ ] Set up GitHub issue templates

### CONTRIBUTING.md Template

```markdown
# Contributing to Channel 47

Thanks for your interest in contributing!

## Ways to Contribute

- **Report bugs** - Open an issue with reproduction steps
- **Suggest features** - Open an issue describing the use case
- **Improve docs** - PRs for typos, clarifications, examples
- **Add skills** - Contribute new skills to existing plugins

## Development Setup

1. Clone the repo
2. Install dependencies: `npm install`
3. Run the site: `cd site && npm run dev`

## Plugin Development

See [Claude Code Plugin Docs](https://docs.anthropic.com/...) for plugin structure.

## Code of Conduct

Be kind. Be helpful. Assume good intent.
```

---

## Implementation Order

| Order | Phase | Effort | Impact | Dependencies |
|-------|-------|--------|--------|--------------|
| 1 | Monorepo Consolidation | Medium | Foundation | None |
| 2 | Claude Desktop Distribution | Low | Unblocks users | Phase 1 |
| 3 | Site Restructure | Medium | UX + maintenance | Phase 1 |
| 4 | SEO Foundation | Low | Traffic prerequisites | Phase 3 |
| 5 | Newsletter Setup | Low | Audience capture | None |
| 6 | Open Source Transition | Low | Removes friction | Phases 1-5 |

---

## Final State Checklist

### Repository
- [ ] Single monorepo with plugins + site
- [ ] Valid `marketplace.json` at root
- [ ] All plugins self-contained in `plugins/`
- [ ] Site in `site/` with content collections pulling from plugins
- [ ] GitHub Actions for site deployment
- [ ] MIT license
- [ ] CONTRIBUTING.md

### Site
- [ ] Simplified URL structure (`/tools/`, `/blog/`)
- [ ] Dynamic tool pages from plugin data
- [ ] Install tabs (Claude Desktop / Claude Code)
- [ ] Sitemap and robots.txt
- [ ] JSON-LD on all pages
- [ ] Newsletter capture with segmentation

### Distribution
- [ ] Google Ads MCP on npm (done)
- [ ] Creative Designer on PyPI
- [ ] All plugins installable via Claude Code marketplace
- [ ] Clear install docs for Claude Desktop users

### Content
- [ ] 5+ ecosystem blog posts
- [ ] 5+ tool-specific blog posts
- [ ] Newsletter operational with welcome sequence

---

## Sources

- [Claude Code Plugin Marketplaces](https://code.claude.com/docs/en/plugin-marketplaces.md)
- [Claude Code Plugins Reference](https://code.claude.com/docs/en/plugins-reference.md)
- [Astro Content Collections](https://docs.astro.build/en/guides/content-collections/)
- [Claude Desktop MCP Setup](https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)

---

*This design document consolidates the Channel 47 marketplace and website into a unified structure optimized for open-source distribution and audience growth.*
