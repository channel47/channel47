# Monorepo Marketplace Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Consolidate channel47-marketplace and channel47 site into a unified monorepo with open-source distribution.

**Architecture:** Single repo with `plugins/` directory containing all Claude Code plugins and `site/` directory containing the Astro website. Site pulls content directly from plugin READMEs via Astro content collections. MCP servers distributed via npm (Google Ads) and PyPI (Creative Designer).

**Tech Stack:** Astro 4.x, TypeScript, npm workspaces, Python (FastMCP), Beehiiv

---

## Phase 1: Monorepo Consolidation

### Task 1.1: Create Monorepo Structure

**Files:**
- Create: `plugins/` (directory)
- Create: `.claude-plugin/marketplace.json`
- Create: `package.json` (root workspace)

**Step 1: Create the new directory structure**

```bash
cd /Users/jackson/Documents/Access/1/a_projects/channel47
mkdir -p plugins
mkdir -p .claude-plugin
```

**Step 2: Verify directories created**

Run: `ls -la /Users/jackson/Documents/Access/1/a_projects/channel47/`
Expected: See `plugins/` and `.claude-plugin/` directories

**Step 3: Commit empty structure**

```bash
cd /Users/jackson/Documents/Access/1/a_projects/channel47
git add .
git commit -m "chore: add monorepo directory structure"
```

---

### Task 1.2: Copy Plugins from Marketplace

**Files:**
- Copy: `channel47-marketplace/plugins/*` → `channel47/plugins/`

**Step 1: Copy all plugins**

```bash
cp -r /Users/jackson/Documents/Access/1/a_projects/channel47-marketplace/plugins/* /Users/jackson/Documents/Access/1/a_projects/channel47/plugins/
```

**Step 2: Verify plugins copied**

Run: `ls -la /Users/jackson/Documents/Access/1/a_projects/channel47/plugins/`
Expected: See `google-ads-specialist/`, `creative-designer/`, `copywriting-expert/`, `prompt-enhancer/`

**Step 3: Commit plugins**

```bash
cd /Users/jackson/Documents/Access/1/a_projects/channel47
git add plugins/
git commit -m "feat: add plugins from marketplace"
```

---

### Task 1.3: Create Marketplace Configuration

**Files:**
- Create: `.claude-plugin/marketplace.json`

**Step 1: Write marketplace.json**

Create file at `/Users/jackson/Documents/Access/1/a_projects/channel47/.claude-plugin/marketplace.json`:

```json
{
  "name": "channel47",
  "owner": {
    "name": "Jackson",
    "url": "https://channel47.dev"
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
      "version": "3.1.0",
      "category": "marketing",
      "tags": ["google-ads", "gaql", "marketing", "analytics", "ppc"]
    },
    {
      "name": "creative-designer",
      "source": "creative-designer",
      "description": "AI image generation with Gemini",
      "version": "1.2.0",
      "category": "creative",
      "tags": ["image-generation", "ai-art", "gemini", "mcp"]
    },
    {
      "name": "copywriting-expert",
      "source": "copywriting-expert",
      "description": "Master copywriting frameworks",
      "version": "1.0.0",
      "category": "writing",
      "tags": ["copywriting", "sales-copy", "direct-response"]
    },
    {
      "name": "prompt-enhancer",
      "source": "prompt-enhancer",
      "description": "Optimize prompts for Claude",
      "version": "1.0.0",
      "category": "development",
      "tags": ["prompts", "optimization", "prompt-engineering"]
    }
  ]
}
```

**Step 2: Verify JSON is valid**

Run: `cat /Users/jackson/Documents/Access/1/a_projects/channel47/.claude-plugin/marketplace.json | python3 -m json.tool`
Expected: Pretty-printed JSON with no errors

**Step 3: Commit marketplace config**

```bash
cd /Users/jackson/Documents/Access/1/a_projects/channel47
git add .claude-plugin/
git commit -m "feat: add marketplace configuration"
```

---

### Task 1.4: Move Site into Subdirectory

**Files:**
- Move: `src/`, `public/`, `astro.config.mjs`, `tsconfig.json`, `package.json`, `package-lock.json` → `site/`

**Step 1: Create site directory and move files**

```bash
cd /Users/jackson/Documents/Access/1/a_projects/channel47
mkdir -p site
mv src site/
mv public site/
mv astro.config.mjs site/
mv tsconfig.json site/
mv package.json site/
mv package-lock.json site/
mv node_modules site/
mv .astro site/
mv dist site/
```

**Step 2: Verify site structure**

Run: `ls -la /Users/jackson/Documents/Access/1/a_projects/channel47/site/`
Expected: See `src/`, `public/`, `astro.config.mjs`, `package.json`, etc.

**Step 3: Test site still builds**

```bash
cd /Users/jackson/Documents/Access/1/a_projects/channel47/site
npm run build
```
Expected: Build succeeds

**Step 4: Commit site relocation**

```bash
cd /Users/jackson/Documents/Access/1/a_projects/channel47
git add .
git commit -m "refactor: move site into subdirectory"
```

---

### Task 1.5: Create Root Workspace Package.json

**Files:**
- Create: `package.json` (root)

**Step 1: Write root package.json**

Create file at `/Users/jackson/Documents/Access/1/a_projects/channel47/package.json`:

```json
{
  "name": "channel47-monorepo",
  "private": true,
  "workspaces": [
    "site"
  ],
  "scripts": {
    "dev": "npm run dev --workspace=site",
    "build": "npm run build --workspace=site",
    "preview": "npm run preview --workspace=site"
  }
}
```

**Step 2: Install workspace dependencies**

```bash
cd /Users/jackson/Documents/Access/1/a_projects/channel47
npm install
```

**Step 3: Verify workspace works**

Run: `npm run build`
Expected: Site builds successfully

**Step 4: Commit workspace setup**

```bash
git add package.json package-lock.json
git commit -m "feat: add npm workspace configuration"
```

---

### Task 1.6: Add Root Documentation

**Files:**
- Create: `README.md` (root)
- Create: `CONTRIBUTING.md`
- Create: `LICENSE`

**Step 1: Write root README.md**

Create file at `/Users/jackson/Documents/Access/1/a_projects/channel47/README.md`:

```markdown
# Channel 47

Open-source AI tools for media buyers and marketers.

## Plugins

| Plugin | Description | Install |
|--------|-------------|---------|
| [Google Ads Specialist](./plugins/google-ads-specialist) | GAQL queries and campaign management | `npx -y @channel47/google-ads-mcp` |
| [Creative Designer](./plugins/creative-designer) | AI image generation with Gemini | `uvx channel47-creative-designer` |
| [Copywriting Expert](./plugins/copywriting-expert) | Master copywriting frameworks | Claude Code only |
| [Prompt Enhancer](./plugins/prompt-enhancer) | Optimize prompts for Claude | Claude Code only |

## Installation

### Claude Code

```bash
/plugin marketplace add github:channel47/channel47
/plugin install google-ads-specialist@channel47
```

### Claude Desktop

See individual plugin READMEs for `claude_desktop_config.json` snippets.

## Development

```bash
# Install dependencies
npm install

# Run site locally
npm run dev

# Build site
npm run build
```

## License

MIT
```

**Step 2: Write CONTRIBUTING.md**

Create file at `/Users/jackson/Documents/Access/1/a_projects/channel47/CONTRIBUTING.md`:

```markdown
# Contributing to Channel 47

Thanks for your interest in contributing!

## Ways to Contribute

- **Report bugs** - Open an issue with reproduction steps
- **Suggest features** - Open an issue describing the use case
- **Improve docs** - PRs for typos, clarifications, examples
- **Add skills** - Contribute new skills to existing plugins

## Development Setup

1. Clone the repo: `git clone https://github.com/channel47/channel47.git`
2. Install dependencies: `npm install`
3. Run the site: `npm run dev`

## Plugin Development

Each plugin follows Claude Code plugin structure:

```
plugins/plugin-name/
├── .claude-plugin/plugin.json
├── skills/
├── commands/
├── agents/
└── README.md
```

## Code of Conduct

Be kind. Be helpful. Assume good intent.
```

**Step 3: Write LICENSE**

Create file at `/Users/jackson/Documents/Access/1/a_projects/channel47/LICENSE`:

```
MIT License

Copyright (c) 2026 Channel 47

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

**Step 4: Commit documentation**

```bash
cd /Users/jackson/Documents/Access/1/a_projects/channel47
git add README.md CONTRIBUTING.md LICENSE
git commit -m "docs: add root documentation and license"
```

---

### Task 1.7: Validate Marketplace Structure

**Step 1: Run marketplace validation**

```bash
cd /Users/jackson/Documents/Access/1/a_projects/channel47
claude /plugin validate .
```
Expected: Validation passes with no errors

**Step 2: Test plugin installation locally**

```bash
claude /plugin marketplace add /Users/jackson/Documents/Access/1/a_projects/channel47
claude /plugin list
```
Expected: See channel47 marketplace and available plugins

---

## Phase 2: Site Restructure

### Task 2.1: Update Astro Config for Sitemap

**Files:**
- Modify: `site/astro.config.mjs`

**Step 1: Install sitemap integration**

```bash
cd /Users/jackson/Documents/Access/1/a_projects/channel47/site
npm install @astrojs/sitemap
```

**Step 2: Update astro.config.mjs**

Replace contents of `/Users/jackson/Documents/Access/1/a_projects/channel47/site/astro.config.mjs`:

```javascript
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://channel47.dev',
  integrations: [sitemap()],
  redirects: {
    '/setup': '/tools/google-ads'
  }
});
```

**Step 3: Verify config is valid**

Run: `cd /Users/jackson/Documents/Access/1/a_projects/channel47/site && npm run build`
Expected: Build succeeds, sitemap generated

**Step 4: Commit**

```bash
cd /Users/jackson/Documents/Access/1/a_projects/channel47
git add site/
git commit -m "feat: add sitemap integration"
```

---

### Task 2.2: Create robots.txt

**Files:**
- Create: `site/public/robots.txt`

**Step 1: Write robots.txt**

Create file at `/Users/jackson/Documents/Access/1/a_projects/channel47/site/public/robots.txt`:

```
User-agent: *
Allow: /

Sitemap: https://channel47.dev/sitemap-index.xml
```

**Step 2: Commit**

```bash
cd /Users/jackson/Documents/Access/1/a_projects/channel47
git add site/public/robots.txt
git commit -m "feat: add robots.txt"
```

---

### Task 2.3: Create SEO Schema Components

**Files:**
- Create: `site/src/components/SEO/ToolSchema.astro`
- Create: `site/src/components/SEO/ArticleSchema.astro`

**Step 1: Create SEO directory**

```bash
mkdir -p /Users/jackson/Documents/Access/1/a_projects/channel47/site/src/components/SEO
```

**Step 2: Write ToolSchema.astro**

Create file at `/Users/jackson/Documents/Access/1/a_projects/channel47/site/src/components/SEO/ToolSchema.astro`:

```astro
---
interface Props {
  name: string;
  description: string;
  url: string;
  version: string;
}
const { name, description, url, version } = Astro.props;

const schema = {
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
};
---

<script type="application/ld+json" set:html={JSON.stringify(schema)} />
```

**Step 3: Write ArticleSchema.astro**

Create file at `/Users/jackson/Documents/Access/1/a_projects/channel47/site/src/components/SEO/ArticleSchema.astro`:

```astro
---
interface Props {
  title: string;
  description: string;
  datePublished: Date;
  dateModified?: Date;
  url: string;
}
const { title, description, datePublished, dateModified, url } = Astro.props;

const schema = {
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": title,
  "description": description,
  "datePublished": datePublished.toISOString(),
  "dateModified": (dateModified || datePublished).toISOString(),
  "url": url,
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
};
---

<script type="application/ld+json" set:html={JSON.stringify(schema)} />
```

**Step 4: Commit**

```bash
cd /Users/jackson/Documents/Access/1/a_projects/channel47
git add site/src/components/SEO/
git commit -m "feat: add JSON-LD schema components"
```

---

### Task 2.4: Create InstallTabs Component

**Files:**
- Create: `site/src/components/InstallTabs.astro`

**Step 1: Write InstallTabs.astro**

Create file at `/Users/jackson/Documents/Access/1/a_projects/channel47/site/src/components/InstallTabs.astro`:

```astro
---
interface Props {
  plugin: 'google-ads' | 'creative-designer' | 'copywriting' | 'prompt-enhancer';
}

const { plugin } = Astro.props;

const configs: Record<string, { claudeDesktop: string | null; claudeCode: string }> = {
  'google-ads': {
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
    claudeCode: `/plugin marketplace add github:channel47/channel47
/plugin install google-ads-specialist@channel47`
  },
  'creative-designer': {
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
    claudeCode: `/plugin marketplace add github:channel47/channel47
/plugin install creative-designer@channel47`
  },
  'copywriting': {
    claudeDesktop: null,
    claudeCode: `/plugin marketplace add github:channel47/channel47
/plugin install copywriting-expert@channel47`
  },
  'prompt-enhancer': {
    claudeDesktop: null,
    claudeCode: `/plugin marketplace add github:channel47/channel47
/plugin install prompt-enhancer@channel47`
  }
};

const config = configs[plugin];
const hasMcp = config.claudeDesktop !== null;
---

<div class="install-tabs">
  <div class="tab-buttons">
    {hasMcp && <button data-tab="claude-desktop" class="active">Claude Desktop</button>}
    <button data-tab="claude-code" class:list={[{ active: !hasMcp }]}>Claude Code</button>
  </div>

  {hasMcp && (
    <div class="tab-content" data-content="claude-desktop">
      <p>Add to your <code>claude_desktop_config.json</code>:</p>
      <div class="code-block">
        <pre><code>{config.claudeDesktop}</code></pre>
        <button class="copy-btn" data-copy={config.claudeDesktop}>Copy</button>
      </div>
      <p class="config-path">
        <strong>Config location:</strong><br />
        macOS: <code>~/Library/Application Support/Claude/claude_desktop_config.json</code><br />
        Windows: <code>%APPDATA%\Claude\claude_desktop_config.json</code>
      </p>
    </div>
  )}

  <div class="tab-content" data-content="claude-code" hidden={hasMcp}>
    <div class="code-block">
      <pre><code>{config.claudeCode}</code></pre>
      <button class="copy-btn" data-copy={config.claudeCode}>Copy</button>
    </div>
  </div>
</div>

<style>
  .install-tabs {
    margin: var(--space-6) 0;
  }

  .tab-buttons {
    display: flex;
    gap: var(--space-2);
    margin-bottom: var(--space-4);
  }

  .tab-buttons button {
    padding: var(--space-2) var(--space-4);
    background: var(--color-bg-elevated);
    border: 1px solid var(--color-border);
    border-radius: var(--radius-md);
    color: var(--color-text-secondary);
    cursor: pointer;
    font-family: var(--font-sans);
    font-size: var(--text-sm);
    transition: all var(--duration-fast) var(--ease-out);
  }

  .tab-buttons button.active {
    background: var(--color-accent);
    border-color: var(--color-accent);
    color: var(--color-bg);
  }

  .tab-content[hidden] {
    display: none;
  }

  .code-block {
    position: relative;
    background: var(--color-bg-elevated);
    border: 1px solid var(--color-border);
    border-radius: var(--radius-md);
    overflow: hidden;
  }

  .code-block pre {
    margin: 0;
    padding: var(--space-4);
    overflow-x: auto;
  }

  .code-block code {
    font-family: var(--font-mono);
    font-size: var(--text-sm);
  }

  .copy-btn {
    position: absolute;
    top: var(--space-2);
    right: var(--space-2);
    padding: var(--space-1) var(--space-2);
    background: var(--color-bg);
    border: 1px solid var(--color-border);
    border-radius: var(--radius-sm);
    color: var(--color-text-secondary);
    cursor: pointer;
    font-family: var(--font-sans);
    font-size: var(--text-xs);
  }

  .copy-btn:hover {
    background: var(--color-accent);
    border-color: var(--color-accent);
    color: var(--color-bg);
  }

  .config-path {
    margin-top: var(--space-4);
    padding: var(--space-3);
    background: var(--color-bg-elevated);
    border-radius: var(--radius-md);
    font-size: var(--text-sm);
    color: var(--color-text-secondary);
  }

  .config-path code {
    font-size: var(--text-xs);
  }
</style>

<script>
  document.querySelectorAll('.install-tabs').forEach(tabs => {
    const buttons = tabs.querySelectorAll('.tab-buttons button');
    const contents = tabs.querySelectorAll('.tab-content');

    buttons.forEach(btn => {
      btn.addEventListener('click', () => {
        const tab = btn.dataset.tab;
        buttons.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        contents.forEach(c => {
          c.hidden = c.dataset.content !== tab;
        });
      });
    });
  });

  document.querySelectorAll('.copy-btn').forEach(btn => {
    btn.addEventListener('click', async () => {
      const text = btn.dataset.copy;
      if (text) {
        await navigator.clipboard.writeText(text);
        const original = btn.textContent;
        btn.textContent = 'Copied!';
        setTimeout(() => btn.textContent = original, 2000);
      }
    });
  });
</script>
```

**Step 2: Commit**

```bash
cd /Users/jackson/Documents/Access/1/a_projects/channel47
git add site/src/components/InstallTabs.astro
git commit -m "feat: add InstallTabs component for Claude Desktop/Code"
```

---

### Task 2.5: Update EmailSignup with Tags

**Files:**
- Modify: `site/src/components/EmailSignup.astro`

**Step 1: Read current EmailSignup**

Review existing component at `site/src/components/EmailSignup.astro`

**Step 2: Update EmailSignup.astro**

Ensure the component accepts `tag` and `context` props. Update to match:

```astro
---
interface Props {
  title?: string;
  description?: string;
  buttonText?: string;
  variant?: 'inline' | 'card';
  tag?: string;
  context?: 'tool' | 'blog' | 'homepage';
  class?: string;
}

const {
  tag = 'general',
  context = 'homepage',
  variant = 'card',
  class: className = ''
} = Astro.props;

const defaultCopy = {
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

const defaults = defaultCopy[context] || defaultCopy.homepage;
const title = Astro.props.title || defaults.title;
const description = Astro.props.description || defaults.description;
const buttonText = Astro.props.buttonText || defaults.button;

const BEEHIIV_FORM_URL = import.meta.env.BEEHIIV_FORM_URL || '#';
---

<form
  action={BEEHIIV_FORM_URL}
  method="POST"
  class:list={['email-signup', `email-signup--${variant}`, className]}
>
  <input type="hidden" name="tag" value={tag} />

  <div class="signup-content">
    <h3>{title}</h3>
    <p>{description}</p>
  </div>

  <div class="signup-form">
    <input
      type="email"
      name="email"
      placeholder="you@example.com"
      required
    />
    <button type="submit">{buttonText}</button>
  </div>

  <p class="privacy-note">No spam. Unsubscribe anytime.</p>
</form>
```

**Step 3: Commit**

```bash
cd /Users/jackson/Documents/Access/1/a_projects/channel47
git add site/src/components/EmailSignup.astro
git commit -m "feat: add tag and context props to EmailSignup"
```

---

## Phase 3: Claude Desktop Distribution

### Task 3.1: Create PyPI Package for Creative Designer

**Files:**
- Create: `plugins/creative-designer/pyproject.toml`

**Step 1: Write pyproject.toml**

Create file at `/Users/jackson/Documents/Access/1/a_projects/channel47/plugins/creative-designer/pyproject.toml`:

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "channel47-creative-designer"
version = "1.2.0"
description = "AI-powered image generation MCP server using Google Gemini"
readme = "README.md"
license = "MIT"
authors = [
    { name = "Jackson", email = "jackson@channel47.dev" }
]
keywords = ["mcp", "gemini", "image-generation", "ai", "claude"]
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
]
requires-python = ">=3.10"
dependencies = [
    "mcp>=1.23.0,<2.0.0",
    "fastmcp>=2.14.0,<3.0.0",
    "httpx>=0.27.1,<1.0.0",
    "pydantic>=2.11.0,<3.0.0",
    "python-dotenv>=1.1.0",
]

[project.urls]
Homepage = "https://channel47.dev"
Repository = "https://github.com/channel47/channel47"

[project.scripts]
channel47-creative-designer = "nanobanana_mcp:main"

[tool.hatch.build.targets.wheel]
packages = ["src"]
```

**Step 2: Update MCP server entry point**

The `src/nanobanana_mcp.py` needs a `main()` function as entry point. Check if it exists, if not add:

```python
def main():
    mcp.run()

if __name__ == "__main__":
    main()
```

**Step 3: Commit**

```bash
cd /Users/jackson/Documents/Access/1/a_projects/channel47
git add plugins/creative-designer/pyproject.toml
git commit -m "feat: add pyproject.toml for PyPI distribution"
```

---

### Task 3.2: Test Local PyPI Package

**Step 1: Build package locally**

```bash
cd /Users/jackson/Documents/Access/1/a_projects/channel47/plugins/creative-designer
pip install build
python -m build
```
Expected: Creates `dist/` directory with `.whl` and `.tar.gz` files

**Step 2: Test local install**

```bash
pip install dist/channel47_creative_designer-1.2.0-py3-none-any.whl
channel47-creative-designer --help
```
Expected: Shows help or runs MCP server

**Step 3: Uninstall test**

```bash
pip uninstall channel47-creative-designer -y
```

---

## Phase 4: Content Updates

### Task 4.1: Update Tool Pages with InstallTabs

**Files:**
- Modify: `site/src/pages/tools/google-ads.astro`

**Step 1: Add InstallTabs import and usage**

At the top of the file, add:
```astro
import InstallTabs from '../../components/InstallTabs.astro';
```

In the appropriate section, add:
```astro
<InstallTabs plugin="google-ads" />
```

**Step 2: Commit**

```bash
cd /Users/jackson/Documents/Access/1/a_projects/channel47
git add site/src/pages/tools/
git commit -m "feat: add InstallTabs to tool pages"
```

---

### Task 4.2: Add SEO Schemas to Pages

**Files:**
- Modify: `site/src/pages/tools/google-ads.astro`
- Modify: `site/src/layouts/ProseLayout.astro`

**Step 1: Add ToolSchema to tool page**

Import and add to head section:
```astro
import ToolSchema from '../../components/SEO/ToolSchema.astro';

<!-- In head or near top of body -->
<ToolSchema
  name="Google Ads MCP Server"
  description="Query Google Ads data using GAQL with OAuth authentication"
  url="https://channel47.dev/tools/google-ads"
  version="3.1.0"
/>
```

**Step 2: Add ArticleSchema to ProseLayout**

Import and add:
```astro
import ArticleSchema from '../components/SEO/ArticleSchema.astro';

<!-- In layout, pass frontmatter data -->
<ArticleSchema
  title={frontmatter.title}
  description={frontmatter.description}
  datePublished={frontmatter.date}
  url={Astro.url.href}
/>
```

**Step 3: Commit**

```bash
cd /Users/jackson/Documents/Access/1/a_projects/channel47
git add site/src/
git commit -m "feat: add JSON-LD schemas to pages"
```

---

### Task 4.3: Update Homepage for Open Source Messaging

**Files:**
- Modify: `site/src/pages/index.astro`

**Step 1: Update hero copy**

Change value proposition to emphasize free/open source:

```astro
<h1>Open-source AI tools for media buyers</h1>
<p>Claude Code plugins and MCP servers. Free forever.</p>
```

**Step 2: Update CTAs**

```astro
<div class="hero-ctas">
  <Button href="/tools" variant="primary">Browse Tools</Button>
  <Button href="https://github.com/channel47/channel47" variant="outline">Star on GitHub</Button>
</div>
```

**Step 3: Remove pricing references**

Remove any `$199` or paid product references from homepage.

**Step 4: Commit**

```bash
cd /Users/jackson/Documents/Access/1/a_projects/channel47
git add site/src/pages/index.astro
git commit -m "refactor: update homepage for open source positioning"
```

---

## Phase 5: Final Validation

### Task 5.1: Full Build Test

**Step 1: Clean and rebuild**

```bash
cd /Users/jackson/Documents/Access/1/a_projects/channel47
rm -rf site/dist site/.astro
npm run build
```
Expected: Build succeeds with no errors

**Step 2: Preview locally**

```bash
npm run preview
```
Expected: Site loads at localhost, all pages render correctly

---

### Task 5.2: Marketplace Validation

**Step 1: Validate marketplace**

```bash
cd /Users/jackson/Documents/Access/1/a_projects/channel47
claude /plugin validate .
```
Expected: All plugins valid

---

### Task 5.3: Final Commit and Tag

**Step 1: Review all changes**

```bash
git status
git log --oneline -10
```

**Step 2: Create release tag**

```bash
git tag -a v1.0.0 -m "Monorepo consolidation complete"
git push origin main --tags
```

---

## Summary Checklist

### Phase 1: Monorepo Consolidation
- [ ] Task 1.1: Create monorepo structure
- [ ] Task 1.2: Copy plugins from marketplace
- [ ] Task 1.3: Create marketplace configuration
- [ ] Task 1.4: Move site into subdirectory
- [ ] Task 1.5: Create root workspace package.json
- [ ] Task 1.6: Add root documentation
- [ ] Task 1.7: Validate marketplace structure

### Phase 2: Site Restructure
- [ ] Task 2.1: Update Astro config for sitemap
- [ ] Task 2.2: Create robots.txt
- [ ] Task 2.3: Create SEO schema components
- [ ] Task 2.4: Create InstallTabs component
- [ ] Task 2.5: Update EmailSignup with tags

### Phase 3: Claude Desktop Distribution
- [ ] Task 3.1: Create PyPI package for Creative Designer
- [ ] Task 3.2: Test local PyPI package

### Phase 4: Content Updates
- [ ] Task 4.1: Update tool pages with InstallTabs
- [ ] Task 4.2: Add SEO schemas to pages
- [ ] Task 4.3: Update homepage for open source messaging

### Phase 5: Final Validation
- [ ] Task 5.1: Full build test
- [ ] Task 5.2: Marketplace validation
- [ ] Task 5.3: Final commit and tag

---

## Post-Implementation

After completing this plan:

1. **Archive old marketplace repo** - Mark `channel47-marketplace` as deprecated, point to new repo
2. **Update GitHub settings** - Enable issues, update description, add topics
3. **Publish Creative Designer to PyPI** - `python -m twine upload dist/*`
4. **Configure Beehiiv** - Add form URL to `.env`
5. **Write first 5 blog posts** - Per SEO content priority list

---

*Total estimated tasks: 17 | Estimated time: 2-3 hours*
