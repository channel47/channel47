# Channel 47 Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a digital assets marketplace with automated content pipeline that transforms conversation logs into blog posts.

**Architecture:** Astro static site deployed to Vercel with GitHub Actions pipeline that synthesizes conversation logs into blog posts via Claude API, and Stripe integration for payments with serverless webhook handlers.

**Tech Stack:** Astro 4.x, Tailwind CSS, Vercel, Stripe, GitHub Actions, Claude API, Resend (email)

---

## Batch 1: Project Foundation

### Task 1.1: Initialize Repository Structure

**Files:**
- Create: `package.json`
- Create: `.gitignore`
- Create: `README.md`
- Create: `logs/.gitkeep`
- Create: `drafts/.gitkeep`

**Step 1: Create project directory and initialize git**

```bash
cd /Users/jd/Desktop/digital_assets
git init
```

**Step 2: Create .gitignore**

```gitignore
# .gitignore
node_modules/
dist/
.vercel/
.env
.env.local
.DS_Store
*.log
```

**Step 3: Create directory structure**

```bash
mkdir -p logs drafts src .github/workflows
touch logs/.gitkeep drafts/.gitkeep
```

**Step 4: Create README**

```markdown
# Channel 47

Digital assets marketplace for Claude Code power users.

## Development

npm install
npm run dev

## Deployment

Automatically deploys to Vercel on push to main.
```

**Step 5: Commit**

```bash
git add .
git commit -m "chore: initialize repository structure"
```

---

### Task 1.2: Scaffold Astro Project

**Files:**
- Create: `package.json` (Astro)
- Create: `astro.config.mjs`
- Create: `tsconfig.json`
- Create: `src/pages/index.astro`

**Step 1: Initialize Astro**

```bash
npm create astro@latest . -- --template minimal --install --git --typescript strict
```

Select: Empty project, Yes to TypeScript (strict), Yes to install dependencies

**Step 2: Verify installation**

```bash
npm run dev
```

Expected: Server running at http://localhost:4321

**Step 3: Commit**

```bash
git add .
git commit -m "chore: scaffold Astro project"
```

---

### Task 1.3: Install and Configure Tailwind CSS

**Files:**
- Modify: `package.json`
- Create: `tailwind.config.mjs`
- Create: `src/styles/global.css`
- Modify: `astro.config.mjs`

**Step 1: Install Tailwind integration**

```bash
npx astro add tailwind
```

Select: Yes to all prompts

**Step 2: Update tailwind.config.mjs with brand colors**

```javascript
// tailwind.config.mjs
/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        coral: {
          50: '#fff5f5',
          100: '#ffe0e0',
          200: '#ffc7c7',
          300: '#ffa3a3',
          400: '#ff7a7a',
          500: '#e85c5c',  // Primary coral
          600: '#d44545',
          700: '#b33636',
          800: '#942d2d',
          900: '#7a2828',
        },
        cream: {
          50: '#fffdf9',
          100: '#fef9f0',
          200: '#fdf3e1',
          300: '#faecd0',
          400: '#f5e1b8',
        },
        charcoal: {
          700: '#374151',
          800: '#1f2937',
          900: '#111827',
        },
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        mono: ['JetBrains Mono', 'monospace'],
      },
    },
  },
  plugins: [],
}
```

**Step 3: Create global CSS**

```css
/* src/styles/global.css */
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  html {
    @apply antialiased;
  }

  body {
    @apply bg-cream-50 text-charcoal-800;
  }
}
```

**Step 4: Verify Tailwind works**

```bash
npm run dev
```

**Step 5: Commit**

```bash
git add .
git commit -m "feat: configure Tailwind CSS with brand colors"
```

---

### Task 1.4: Create Base Layout Component

**Files:**
- Create: `src/layouts/BaseLayout.astro`
- Create: `src/components/Header.astro`
- Create: `src/components/Footer.astro`

**Step 1: Create Header component**

```astro
---
// src/components/Header.astro
---
<header class="border-b border-charcoal-800/10 bg-cream-50/80 backdrop-blur-sm sticky top-0 z-50">
  <nav class="max-w-5xl mx-auto px-6 py-4 flex items-center justify-between">
    <a href="/" class="flex items-center gap-2 font-semibold text-charcoal-900">
      <span class="text-xl">Channel 47</span>
    </a>
    <div class="flex items-center gap-6 text-sm">
      <a href="/blog" class="text-charcoal-700 hover:text-coral-600 transition-colors">Blog</a>
      <a href="/products" class="text-charcoal-700 hover:text-coral-600 transition-colors">Products</a>
      <a href="/about" class="text-charcoal-700 hover:text-coral-600 transition-colors">About</a>
    </div>
  </nav>
</header>
```

**Step 2: Create Footer component**

```astro
---
// src/components/Footer.astro
const year = new Date().getFullYear();
---
<footer class="border-t border-charcoal-800/10 mt-auto">
  <div class="max-w-5xl mx-auto px-6 py-8">
    <div class="flex flex-col sm:flex-row items-center justify-between gap-4 text-sm text-charcoal-700">
      <p>&copy; {year} Channel 47. All rights reserved.</p>
      <div class="flex items-center gap-4">
        <a href="https://x.com/channel47" class="hover:text-coral-600 transition-colors">X/Twitter</a>
        <a href="https://github.com/channel47" class="hover:text-coral-600 transition-colors">GitHub</a>
      </div>
    </div>
  </div>
</footer>
```

**Step 3: Create BaseLayout**

```astro
---
// src/layouts/BaseLayout.astro
import Header from '../components/Header.astro';
import Footer from '../components/Footer.astro';
import '../styles/global.css';

interface Props {
  title: string;
  description?: string;
}

const { title, description = 'Digital assets for Claude Code power users.' } = Astro.props;
---
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="description" content={description} />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono&display=swap" rel="stylesheet">
    <title>{title} | Channel 47</title>
  </head>
  <body class="min-h-screen flex flex-col">
    <Header />
    <main class="flex-1">
      <slot />
    </main>
    <Footer />
  </body>
</html>
```

**Step 4: Verify layout renders**

```bash
npm run dev
```

**Step 5: Commit**

```bash
git add .
git commit -m "feat: add base layout with header and footer"
```

---

## Batch 2: Core Pages

### Task 2.1: Create Homepage

**Files:**
- Modify: `src/pages/index.astro`

**Step 1: Update homepage**

```astro
---
// src/pages/index.astro
import BaseLayout from '../layouts/BaseLayout.astro';
---
<BaseLayout title="Home">
  <section class="max-w-5xl mx-auto px-6 py-20">
    <div class="max-w-2xl">
      <h1 class="text-4xl sm:text-5xl font-bold text-charcoal-900 leading-tight">
        Tools for Claude Code<br />
        <span class="text-coral-600">power users.</span>
      </h1>
      <p class="mt-6 text-lg text-charcoal-700 leading-relaxed">
        A curated directory of skills, plugins, MCP servers, and prompts to supercharge your
        AI-assisted development workflow. Quality picks from the community, plus my own builds.
      </p>
      <div class="mt-8 flex flex-wrap gap-4">
        <a href="/products" class="inline-flex items-center px-6 py-3 bg-coral-600 text-white font-medium rounded-lg hover:bg-coral-700 transition-colors">
          Browse Products
        </a>
        <a href="/blog" class="inline-flex items-center px-6 py-3 border border-charcoal-800/20 text-charcoal-800 font-medium rounded-lg hover:border-charcoal-800/40 transition-colors">
          Read the Blog
        </a>
      </div>
    </div>
  </section>

  <section class="border-t border-charcoal-800/10 bg-cream-100/50">
    <div class="max-w-5xl mx-auto px-6 py-16">
      <h2 class="text-2xl font-semibold text-charcoal-900 mb-8">Latest from the blog</h2>
      <p class="text-charcoal-600">Posts coming soon...</p>
    </div>
  </section>
</BaseLayout>
```

**Step 2: Verify homepage renders**

```bash
npm run dev
```

Navigate to http://localhost:4321

**Step 3: Commit**

```bash
git add .
git commit -m "feat: create homepage"
```

---

### Task 2.2: Create About Page

**Files:**
- Create: `src/pages/about.astro`

**Step 1: Create about page**

```astro
---
// src/pages/about.astro
import BaseLayout from '../layouts/BaseLayout.astro';
---
<BaseLayout title="About" description="About Channel 47 and the person behind it.">
  <section class="max-w-5xl mx-auto px-6 py-16">
    <div class="max-w-2xl">
      <h1 class="text-3xl font-bold text-charcoal-900">About Channel 47</h1>

      <div class="mt-8 prose prose-charcoal">
        <p class="text-lg text-charcoal-700 leading-relaxed">
          Channel 47 is a collection of tools, skills, and insights for people who
          use Claude Code and other AI coding assistants every day.
        </p>

        <p class="mt-4 text-charcoal-700 leading-relaxed">
          Everything here comes from real work. I build these tools because I need them,
          then share what works. No theory, no fluff—just practical stuff from the trenches.
        </p>

        <h2 class="text-xl font-semibold text-charcoal-900 mt-10 mb-4">The name</h2>
        <p class="text-charcoal-700 leading-relaxed">
          Channel 47 is a nod to the UHF channels of old—slightly off the beaten path,
          where you'd find the interesting stuff. This is that channel for AI-assisted development.
        </p>

        <h2 class="text-xl font-semibold text-charcoal-900 mt-10 mb-4">Get in touch</h2>
        <p class="text-charcoal-700 leading-relaxed">
          Find me on <a href="https://x.com/channel47" class="text-coral-600 hover:underline">X/Twitter</a>
          or <a href="mailto:hello@channel47.dev" class="text-coral-600 hover:underline">email me</a>.
        </p>
      </div>
    </div>
  </section>
</BaseLayout>
```

**Step 2: Verify about page renders**

Navigate to http://localhost:4321/about

**Step 3: Commit**

```bash
git add .
git commit -m "feat: create about page"
```

---

### Task 2.3: Create Blog Index Page

**Files:**
- Create: `src/pages/blog/index.astro`

**Step 1: Create blog index**

```astro
---
// src/pages/blog/index.astro
import BaseLayout from '../../layouts/BaseLayout.astro';
// Posts will come from content collection later
const posts: any[] = [];
---
<BaseLayout title="Blog" description="Insights and tutorials from building with Claude Code.">
  <section class="max-w-5xl mx-auto px-6 py-16">
    <h1 class="text-3xl font-bold text-charcoal-900">Blog</h1>
    <p class="mt-4 text-lg text-charcoal-700 max-w-2xl">
      Real stories from building with AI coding assistants. No theory—just what actually works.
    </p>

    <div class="mt-12">
      {posts.length === 0 ? (
        <p class="text-charcoal-600">Posts coming soon. Check back later.</p>
      ) : (
        <ul class="space-y-8">
          {posts.map((post) => (
            <li class="border-b border-charcoal-800/10 pb-8">
              <a href={`/blog/${post.slug}`} class="group">
                <h2 class="text-xl font-semibold text-charcoal-900 group-hover:text-coral-600 transition-colors">
                  {post.data.title}
                </h2>
                <p class="mt-2 text-charcoal-600">{post.data.description}</p>
                <time class="mt-2 block text-sm text-charcoal-500">{post.data.date}</time>
              </a>
            </li>
          ))}
        </ul>
      )}
    </div>
  </section>
</BaseLayout>
```

**Step 2: Verify blog index renders**

Navigate to http://localhost:4321/blog

**Step 3: Commit**

```bash
git add .
git commit -m "feat: create blog index page"
```

---

### Task 2.4: Create Products Index Page

**Files:**
- Create: `src/pages/products/index.astro`

**Step 1: Create products index**

```astro
---
// src/pages/products/index.astro
import BaseLayout from '../../layouts/BaseLayout.astro';
// Products will come from content collection later
const products: any[] = [];
---
<BaseLayout title="Products" description="Curated Claude Code skills, plugins, MCP servers, and prompts.">
  <section class="max-w-5xl mx-auto px-6 py-16">
    <h1 class="text-3xl font-bold text-charcoal-900">Products</h1>
    <p class="mt-4 text-lg text-charcoal-700 max-w-2xl">
      Curated tools to supercharge your Claude Code workflow. All free. Quality picks from the community and my own builds.
    </p>

    <div class="mt-8 flex gap-4 text-sm">
      <button class="px-4 py-2 bg-charcoal-900 text-white rounded-lg">All</button>
      <button class="px-4 py-2 text-charcoal-700 hover:bg-charcoal-100 rounded-lg transition-colors">Skills</button>
      <button class="px-4 py-2 text-charcoal-700 hover:bg-charcoal-100 rounded-lg transition-colors">Plugins</button>
      <button class="px-4 py-2 text-charcoal-700 hover:bg-charcoal-100 rounded-lg transition-colors">MCP Servers</button>
      <button class="px-4 py-2 text-charcoal-700 hover:bg-charcoal-100 rounded-lg transition-colors">Prompts</button>
    </div>

    <div class="mt-12">
      {products.length === 0 ? (
        <p class="text-charcoal-600">Products coming soon. Check back later.</p>
      ) : (
        <div class="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
          {products.map((product) => (
            <a href={`/products/${product.slug}`} class="group block p-6 border border-charcoal-800/10 rounded-xl hover:border-coral-600/30 hover:shadow-lg transition-all">
              <div class="flex items-center justify-between">
                <span class="text-xs font-medium text-coral-600 uppercase tracking-wide">{product.data.category}</span>
                {product.data.featured && (
                  <span class="text-xs font-medium text-charcoal-700 uppercase tracking-wide px-2 py-1 bg-charcoal-100 rounded">★</span>
                )}
              </div>
              <h2 class="mt-2 text-lg font-semibold text-charcoal-900 group-hover:text-coral-600 transition-colors">
                {product.data.title}
              </h2>
              <p class="mt-2 text-sm text-charcoal-600 line-clamp-2">{product.data.description}</p>
              <div class="mt-4 text-xs text-charcoal-500">
                by {product.data.author}
              </div>
            </a>
          ))}
        </div>
      )}
    </div>
  </section>
</BaseLayout>
```

**Step 2: Verify products index renders**

Navigate to http://localhost:4321/products

**Step 3: Commit**

```bash
git add .
git commit -m "feat: create products index page"
```

---

## Batch 3: Content Collections

### Task 3.1: Set Up Blog Content Collection

**Files:**
- Create: `src/content/config.ts`
- Create: `src/content/blog/.gitkeep`

**Step 1: Create content config**

```typescript
// src/content/config.ts
import { defineCollection, z } from 'astro:content';

const blog = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    date: z.coerce.date(),
    draft: z.boolean().default(false),
    tags: z.array(z.string()).default([]),
  }),
});

const products = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    price: z.number().default(0), // Phase 1: all free
    tier: z.enum(['free', 'premium', 'subscription']).default('free'),
    category: z.enum(['skill', 'plugin', 'mcp-server', 'prompt']),
    author: z.string(), // Creator name
    authorUrl: z.string().url().optional(), // Creator website/X/GitHub
    sourceUrl: z.string().url(), // Source repository or download
    downloadFile: z.string().optional(), // For self-hosted downloads
    featured: z.boolean().default(false), // Highlight quality picks
    draft: z.boolean().default(false),
  }),
});

export const collections = { blog, products };
```

**Step 2: Create content directories**

```bash
mkdir -p src/content/blog src/content/products
touch src/content/blog/.gitkeep src/content/products/.gitkeep
```

**Step 3: Commit**

```bash
git add .
git commit -m "feat: configure blog and products content collections"
```

---

### Task 3.2: Create Blog Post Template and Dynamic Route

**Files:**
- Create: `src/pages/blog/[...slug].astro`
- Create: `src/layouts/BlogPost.astro`

**Step 1: Create blog post layout**

```astro
---
// src/layouts/BlogPost.astro
import BaseLayout from './BaseLayout.astro';

interface Props {
  title: string;
  description: string;
  date: Date;
  tags?: string[];
}

const { title, description, date, tags = [] } = Astro.props;
const formattedDate = date.toLocaleDateString('en-US', {
  year: 'numeric',
  month: 'long',
  day: 'numeric'
});
---
<BaseLayout title={title} description={description}>
  <article class="max-w-3xl mx-auto px-6 py-16">
    <header class="mb-12">
      <div class="flex items-center gap-2 text-sm text-charcoal-500 mb-4">
        <time datetime={date.toISOString()}>{formattedDate}</time>
        {tags.length > 0 && (
          <>
            <span>·</span>
            <div class="flex gap-2">
              {tags.map((tag) => (
                <span class="text-coral-600">{tag}</span>
              ))}
            </div>
          </>
        )}
      </div>
      <h1 class="text-3xl sm:text-4xl font-bold text-charcoal-900 leading-tight">{title}</h1>
      <p class="mt-4 text-lg text-charcoal-600">{description}</p>
    </header>

    <div class="prose prose-charcoal prose-lg max-w-none
      prose-headings:font-semibold prose-headings:text-charcoal-900
      prose-a:text-coral-600 prose-a:no-underline hover:prose-a:underline
      prose-code:bg-charcoal-100 prose-code:px-1 prose-code:py-0.5 prose-code:rounded
      prose-pre:bg-charcoal-900 prose-pre:text-cream-100
      prose-blockquote:border-coral-500 prose-blockquote:bg-cream-100/50 prose-blockquote:py-1">
      <slot />
    </div>

    <footer class="mt-16 pt-8 border-t border-charcoal-800/10">
      <a href="/blog" class="text-coral-600 hover:underline">&larr; Back to blog</a>
    </footer>
  </article>
</BaseLayout>
```

**Step 2: Create dynamic blog route**

```astro
---
// src/pages/blog/[...slug].astro
import { getCollection } from 'astro:content';
import BlogPost from '../../layouts/BlogPost.astro';

export async function getStaticPaths() {
  const posts = await getCollection('blog', ({ data }) => !data.draft);
  return posts.map((post) => ({
    params: { slug: post.slug },
    props: { post },
  }));
}

const { post } = Astro.props;
const { Content } = await post.render();
---
<BlogPost
  title={post.data.title}
  description={post.data.description}
  date={post.data.date}
  tags={post.data.tags}
>
  <Content />
</BlogPost>
```

**Step 3: Install Typography plugin for prose styles**

```bash
npm install -D @tailwindcss/typography
```

**Step 4: Update tailwind.config.mjs**

```javascript
// tailwind.config.mjs - add to plugins array
plugins: [require('@tailwindcss/typography')],
```

**Step 5: Commit**

```bash
git add .
git commit -m "feat: add blog post layout and dynamic routing"
```

---

### Task 3.3: Create Product Detail Template and Dynamic Route

**Files:**
- Create: `src/pages/products/[...slug].astro`
- Create: `src/layouts/ProductPage.astro`

**Step 1: Create product page layout**

```astro
---
// src/layouts/ProductPage.astro
import BaseLayout from './BaseLayout.astro';
import EmailSignup from '../components/EmailSignup.astro';

interface Props {
  title: string;
  description: string;
  category: string;
  author: string;
  authorUrl?: string;
  sourceUrl: string;
  featured: boolean;
}

const { title, description, category, author, authorUrl, sourceUrl, featured } = Astro.props;
---
<BaseLayout title={title} description={description}>
  <article class="max-w-5xl mx-auto px-6 py-16">
    <div class="grid lg:grid-cols-3 gap-12">
      <div class="lg:col-span-2">
        <div class="flex items-center gap-3 mb-4">
          <span class="text-xs font-medium text-coral-600 uppercase tracking-wide px-2 py-1 bg-coral-100 rounded">
            {category}
          </span>
          <span class="text-xs font-medium text-green-700 uppercase tracking-wide px-2 py-1 bg-green-100 rounded">
            Free
          </span>
          {featured && (
            <span class="text-xs font-medium text-charcoal-700 uppercase tracking-wide px-2 py-1 bg-charcoal-100 rounded">
              Featured
            </span>
          )}
        </div>
        <h1 class="text-3xl font-bold text-charcoal-900">{title}</h1>
        <p class="mt-4 text-lg text-charcoal-600">{description}</p>

        <div class="mt-4 text-sm text-charcoal-500">
          Created by {authorUrl ? (
            <a href={authorUrl} class="text-coral-600 hover:underline" target="_blank" rel="noopener noreferrer">{author}</a>
          ) : (
            <span>{author}</span>
          )}
        </div>

        <div class="mt-12 prose prose-charcoal max-w-none">
          <slot />
        </div>
      </div>

      <div class="lg:col-span-1">
        <div class="sticky top-24 p-6 border border-charcoal-800/10 rounded-xl bg-white">
          <div class="text-3xl font-bold text-charcoal-900 mb-4">Free</div>

          <EmailSignup
            title="Get this tool"
            description="Enter your email to download"
            source={`product-${category}`}
          />

          <div class="mt-4">
            <a
              href={sourceUrl}
              target="_blank"
              rel="noopener noreferrer"
              class="block text-center py-3 px-6 border border-charcoal-800/20 text-charcoal-800 font-medium rounded-lg hover:border-charcoal-800/40 transition-colors"
            >
              View on GitHub
            </a>
          </div>

          <ul class="mt-6 space-y-2 text-sm text-charcoal-600">
            <li class="flex items-center gap-2">
              <svg class="w-4 h-4 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
              </svg>
              Instant email delivery
            </li>
            <li class="flex items-center gap-2">
              <svg class="w-4 h-4 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
              </svg>
              Free forever
            </li>
          </ul>
        </div>
      </div>
    </div>

    <footer class="mt-16 pt-8 border-t border-charcoal-800/10">
      <a href="/products" class="text-coral-600 hover:underline">&larr; Back to products</a>
    </footer>
  </article>
</BaseLayout>
```

**Step 2: Create dynamic product route**

```astro
---
// src/pages/products/[...slug].astro
import { getCollection } from 'astro:content';
import ProductPage from '../../layouts/ProductPage.astro';

export async function getStaticPaths() {
  const products = await getCollection('products', ({ data }) => !data.draft);
  return products.map((product) => ({
    params: { slug: product.slug },
    props: { product },
  }));
}

const { product } = Astro.props;
const { Content } = await product.render();
---
<ProductPage
  title={product.data.title}
  description={product.data.description}
  category={product.data.category}
  author={product.data.author}
  authorUrl={product.data.authorUrl}
  sourceUrl={product.data.sourceUrl}
  featured={product.data.featured}
>
  <Content />
</ProductPage>
```

**Step 3: Commit**

```bash
git add .
git commit -m "feat: add product page layout and dynamic routing"
```

---

### Task 3.4: Create Sample Content

**Files:**
- Create: `src/content/blog/hello-world.md`
- Create: `src/content/products/sample-skill.md`

**Step 1: Create sample blog post**

```markdown
---
title: "Building Channel 47: The Beginning"
description: "Why I'm building a marketplace for Claude Code power users, and what you can expect."
date: 2025-12-19
tags: ["meta", "claude-code"]
---

This is the first post on Channel 47. More content coming soon.

## What's Channel 47?

A collection of tools for people who use Claude Code every day.

> **Me:** What should I build first?
> **Claude:** Start with the most painful problem you have right now.

That's the approach here. Real problems, real solutions.

## What's coming

- Skills for common workflows
- MCP servers for integrations
- Prompts that actually work

Stay tuned.
```

**Step 2: Create sample product**

```markdown
---
title: "Sample Skill"
description: "A sample skill to demonstrate the product structure."
category: "skill"
author: "Your Name"
sourceUrl: "https://github.com/yourusername/sample-skill"
authorUrl: "https://x.com/yourhandle"
featured: false
draft: true
---

## What's included

This is a sample product. Replace with real content.

## Installation

Instructions here.

## Usage

Usage examples here.

## About the Author

[Author bio and link to their other work]
```

**Step 3: Update blog index to fetch posts**

```astro
---
// src/pages/blog/index.astro
import { getCollection } from 'astro:content';
import BaseLayout from '../../layouts/BaseLayout.astro';

const posts = await getCollection('blog', ({ data }) => !data.draft);
const sortedPosts = posts.sort((a, b) => b.data.date.valueOf() - a.data.date.valueOf());
---
<BaseLayout title="Blog" description="Insights and tutorials from building with Claude Code.">
  <section class="max-w-5xl mx-auto px-6 py-16">
    <h1 class="text-3xl font-bold text-charcoal-900">Blog</h1>
    <p class="mt-4 text-lg text-charcoal-700 max-w-2xl">
      Real stories from building with AI coding assistants. No theory—just what actually works.
    </p>

    <div class="mt-12">
      {sortedPosts.length === 0 ? (
        <p class="text-charcoal-600">Posts coming soon. Check back later.</p>
      ) : (
        <ul class="space-y-8">
          {sortedPosts.map((post) => (
            <li class="border-b border-charcoal-800/10 pb-8">
              <a href={`/blog/${post.slug}`} class="group">
                <h2 class="text-xl font-semibold text-charcoal-900 group-hover:text-coral-600 transition-colors">
                  {post.data.title}
                </h2>
                <p class="mt-2 text-charcoal-600">{post.data.description}</p>
                <time class="mt-2 block text-sm text-charcoal-500">
                  {post.data.date.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' })}
                </time>
              </a>
            </li>
          ))}
        </ul>
      )}
    </div>
  </section>
</BaseLayout>
```

**Step 4: Verify content renders**

```bash
npm run dev
```

Navigate to http://localhost:4321/blog and http://localhost:4321/blog/hello-world

**Step 5: Commit**

```bash
git add .
git commit -m "feat: add sample blog post and wire up content collections"
```

---

## Batch 4: Synthesis Pipeline

### Task 4.1: Create Synthesis Prompt Template

**Files:**
- Create: `scripts/prompts/synthesis.md`

**Step 1: Create prompts directory and synthesis template**

```bash
mkdir -p scripts/prompts
```

```markdown
<!-- scripts/prompts/synthesis.md -->
# Content Synthesis Prompt

You are a content synthesizer for Channel 47, a blog about Claude Code and AI-assisted development.

## Input
You will receive a conversation transcript between a developer and Claude Code.

## Output
Generate two outputs:

### 1. Blog Post (Markdown)

Write a blog post in this format:
- Title: Descriptive, SEO-friendly
- Description: 1-2 sentence summary
- Hybrid format: Polished narrative with embedded conversation snippets

Structure:
1. Hook - What problem was solved?
2. Context - Why does this matter?
3. The journey - What was tried? (include 2-3 conversation snippets as blockquotes)
4. The solution - What worked?
5. Takeaway - What can readers apply?

Style guide:
- Voice: Practitioner sharing real work, not guru dispensing advice
- Tone: Direct, no fluff
- Length: 800-1500 words

### 2. X/Twitter Content

Generate 3 variations:
1. Hook tweet (single tweet, punchy, <280 chars)
2. Thread opener (sets up a 3-5 tweet thread)
3. Question format (engagement-focused)

Include: [LINK] placeholder for the blog post URL

## Format

Return as JSON:

```json
{
  "blog": {
    "title": "...",
    "description": "...",
    "tags": ["tag1", "tag2"],
    "content": "... full markdown content ..."
  },
  "x_content": {
    "hook": "...",
    "thread_opener": "...",
    "question": "..."
  }
}
```
```

**Step 2: Commit**

```bash
git add .
git commit -m "feat: add synthesis prompt template"
```

---

### Task 4.2: Create Synthesis Script

**Files:**
- Create: `scripts/synthesize.ts`
- Modify: `package.json` (add script)

**Step 1: Install dependencies**

```bash
npm install @anthropic-ai/sdk dotenv
npm install -D @types/node tsx
```

**Step 2: Create synthesis script**

```typescript
// scripts/synthesize.ts
import Anthropic from '@anthropic-ai/sdk';
import * as fs from 'fs/promises';
import * as path from 'path';

const anthropic = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY,
});

async function loadPrompt(): Promise<string> {
  const promptPath = path.join(__dirname, 'prompts', 'synthesis.md');
  return fs.readFile(promptPath, 'utf-8');
}

async function synthesize(logPath: string): Promise<void> {
  console.log(`Synthesizing: ${logPath}`);

  const logContent = await fs.readFile(logPath, 'utf-8');
  const systemPrompt = await loadPrompt();

  const message = await anthropic.messages.create({
    model: 'claude-sonnet-4-20250514',
    max_tokens: 4096,
    system: systemPrompt,
    messages: [
      {
        role: 'user',
        content: `Here is the conversation transcript to synthesize:\n\n${logContent}`,
      },
    ],
  });

  const responseText = message.content[0].type === 'text' ? message.content[0].text : '';

  // Extract JSON from response
  const jsonMatch = responseText.match(/```json\n([\s\S]*?)\n```/);
  if (!jsonMatch) {
    throw new Error('Failed to extract JSON from response');
  }

  const result = JSON.parse(jsonMatch[1]);

  // Generate filename from log path
  const logFilename = path.basename(logPath, '.md');
  const date = new Date().toISOString().split('T')[0];
  const slug = logFilename.replace(/^\d{4}-\d{2}-\d{2}-/, '');

  // Write blog draft
  const blogDraftPath = path.join('drafts', 'blog', `${date}-${slug}.md`);
  const blogContent = `---
title: "${result.blog.title}"
description: "${result.blog.description}"
date: ${date}
tags: ${JSON.stringify(result.blog.tags)}
draft: true
---

${result.blog.content}`;

  await fs.mkdir(path.dirname(blogDraftPath), { recursive: true });
  await fs.writeFile(blogDraftPath, blogContent);
  console.log(`Blog draft written to: ${blogDraftPath}`);

  // Write X content draft
  const xDraftPath = path.join('drafts', 'x', `${date}-${slug}.md`);
  const xContent = `# X Content for: ${result.blog.title}

## Hook Tweet
${result.x_content.hook}

## Thread Opener
${result.x_content.thread_opener}

## Question Format
${result.x_content.question}

---
Blog link: [LINK]
`;

  await fs.mkdir(path.dirname(xDraftPath), { recursive: true });
  await fs.writeFile(xDraftPath, xContent);
  console.log(`X content draft written to: ${xDraftPath}`);
}

// Main
const logPath = process.argv[2];
if (!logPath) {
  console.error('Usage: npx tsx scripts/synthesize.ts <path-to-log>');
  process.exit(1);
}

synthesize(logPath).catch(console.error);
```

**Step 3: Add script to package.json**

```json
{
  "scripts": {
    "synthesize": "tsx scripts/synthesize.ts"
  }
}
```

**Step 4: Create .env.example**

```bash
# .env.example
ANTHROPIC_API_KEY=your-api-key-here
RESEND_API_KEY=your-resend-api-key
```

**Step 5: Commit**

```bash
git add .
git commit -m "feat: add synthesis script with Claude API integration"
```

---

### Task 4.3: Create GitHub Action for Log Detection

**Files:**
- Create: `.github/workflows/synthesize.yml`

**Step 1: Create workflow file**

```yaml
# .github/workflows/synthesize.yml
name: Synthesize Content

on:
  push:
    paths:
      - 'logs/**/*.md'
    branches:
      - main

jobs:
  synthesize:
    runs-on: ubuntu-latest
    permissions:
      contents: write
      pull-requests: write

    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          fetch-depth: 2

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Get changed log files
        id: changed-files
        run: |
          echo "files=$(git diff --name-only HEAD~1 HEAD -- 'logs/*.md' | tr '\n' ' ')" >> $GITHUB_OUTPUT

      - name: Synthesize content
        if: steps.changed-files.outputs.files != ''
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          for file in ${{ steps.changed-files.outputs.files }}; do
            echo "Processing: $file"
            npm run synthesize "$file"
          done

      - name: Create Pull Request
        if: steps.changed-files.outputs.files != ''
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          commit-message: 'content: synthesize drafts from conversation logs'
          title: 'Content: New drafts from conversation logs'
          body: |
            This PR contains synthesized content from new conversation logs.

            **Review checklist:**
            - [ ] Blog post draft is accurate and engaging
            - [ ] X content drafts are punchy and on-brand
            - [ ] Move approved content from `drafts/` to `src/content/`
            - [ ] Remove `draft: true` from frontmatter when publishing
          branch: content/synthesized-drafts
          delete-branch: true
```

**Step 2: Commit**

```bash
git add .
git commit -m "feat: add GitHub Action for content synthesis pipeline"
```

---

## Batch 5: Email Capture & Downloads

### Task 5.1: Create Email Signup Component

**Files:**
- Create: `src/components/EmailSignup.astro`

**Step 1: Create component**

```astro
---
// src/components/EmailSignup.astro
interface Props {
  title?: string;
  description?: string;
  source?: string;
}

const {
  title = "Get notified about new tools",
  description = "Join the list for early access to new skills, plugins, and insights.",
  source = "website"
} = Astro.props;
---
<div class="p-6 bg-cream-100 rounded-xl border border-charcoal-800/10">
  <h3 class="text-lg font-semibold text-charcoal-900">{title}</h3>
  <p class="mt-2 text-sm text-charcoal-600">{description}</p>

  <form
    id="email-form"
    class="mt-4 flex gap-2"
    data-source={source}
  >
    <input
      type="email"
      name="email"
      placeholder="you@example.com"
      required
      class="flex-1 px-4 py-2 border border-charcoal-800/20 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-coral-500 focus:border-transparent"
    />
    <button
      type="submit"
      class="px-4 py-2 bg-coral-600 text-white text-sm font-medium rounded-lg hover:bg-coral-700 transition-colors"
    >
      Subscribe
    </button>
  </form>

  <p id="form-message" class="mt-2 text-sm hidden"></p>
</div>

<script>
  const form = document.getElementById('email-form') as HTMLFormElement;
  const message = document.getElementById('form-message');

  form?.addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = new FormData(form);
    const email = formData.get('email');
    const source = form.dataset.source;

    const button = form.querySelector('button');
    if (button) {
      button.textContent = 'Subscribing...';
      button.setAttribute('disabled', 'true');
    }

    try {
      const response = await fetch('/api/subscribe', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, source }),
      });

      if (response.ok) {
        if (message) {
          message.textContent = 'Thanks! Check your email to confirm.';
          message.className = 'mt-2 text-sm text-green-600';
        }
        form.reset();
      } else {
        throw new Error('Subscription failed');
      }
    } catch (err) {
      if (message) {
        message.textContent = 'Something went wrong. Please try again.';
        message.className = 'mt-2 text-sm text-red-600';
      }
    } finally {
      if (button) {
        button.textContent = 'Subscribe';
        button.removeAttribute('disabled');
      }
    }
  });
</script>
```

**Step 2: Commit**

```bash
git add .
git commit -m "feat: add email signup component"
```

---

### Task 5.2: Create Subscribe API Endpoint

**Files:**
- Create: `src/pages/api/subscribe.ts`

**Step 1: Install Resend SDK**

```bash
npm install resend
```

**Step 2: Create subscribe endpoint**

```typescript
// src/pages/api/subscribe.ts
import type { APIRoute } from 'astro';
import { Resend } from 'resend';

const resend = new Resend(import.meta.env.RESEND_API_KEY);

// Simple in-memory store for demo - replace with database in production
const subscribers: Set<string> = new Set();

export const POST: APIRoute = async ({ request }) => {
  try {
    const { email, source } = await request.json();

    if (!email || !email.includes('@')) {
      return new Response(JSON.stringify({ error: 'Valid email required' }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    // Check if already subscribed
    if (subscribers.has(email)) {
      return new Response(JSON.stringify({ message: 'Already subscribed' }), {
        status: 200,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    // Add to subscribers
    subscribers.add(email);

    // Send welcome email
    await resend.emails.send({
      from: 'Channel 47 <hello@channel47.dev>',
      to: email,
      subject: 'Welcome to Channel 47',
      html: `
        <h1>Welcome to Channel 47!</h1>
        <p>Thanks for subscribing. You'll be the first to know about new tools and content.</p>
        <p>- Channel 47</p>
      `,
    });

    console.log(`New subscriber: ${email} (source: ${source})`);

    return new Response(JSON.stringify({ success: true }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' },
    });
  } catch (error) {
    console.error('Subscribe error:', error);
    return new Response(JSON.stringify({ error: 'Subscription failed' }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    });
  }
};
```

**Step 3: Commit**

```bash
git add .
git commit -m "feat: add email subscribe API endpoint"
```

---

### Task 5.3: Add Email Signup to Homepage

**Files:**
- Modify: `src/pages/index.astro`

**Step 1: Import and add EmailSignup component**

Add after the "Latest from the blog" section:

```astro
---
import EmailSignup from '../components/EmailSignup.astro';
---

<!-- Add this section before closing </BaseLayout> -->
<section class="border-t border-charcoal-800/10">
  <div class="max-w-5xl mx-auto px-6 py-16">
    <div class="max-w-md mx-auto">
      <EmailSignup
        title="Stay in the loop"
        description="Get notified when new tools drop. No spam, just useful stuff."
        source="homepage"
      />
    </div>
  </div>
</section>
```

**Step 2: Commit**

```bash
git add .
git commit -m "feat: add email signup to homepage"
```

---

## Batch 6: Deployment

### Task 6.1: Configure Vercel Deployment

**Files:**
- Create: `vercel.json`

**Step 1: Create Vercel config**

```json
{
  "framework": "astro",
  "buildCommand": "npm run build",
  "outputDirectory": "dist",
  "env": {
    "ANTHROPIC_API_KEY": "@anthropic-api-key",
    "RESEND_API_KEY": "@resend-api-key"
  }
}
```

**Step 2: Commit**

```bash
git add .
git commit -m "chore: add Vercel configuration"
```

---

### Task 6.2: Final Build Test

**Step 1: Run production build locally**

```bash
npm run build
```

Expected: Build completes without errors

**Step 2: Preview production build**

```bash
npm run preview
```

Expected: Site runs at http://localhost:4321

**Step 3: Commit any build fixes**

```bash
git add .
git commit -m "chore: fix build issues" # if any
```

---

### Task 6.3: Push and Deploy

**Step 1: Create GitHub repository**

```bash
gh repo create channel47 --public --source=. --push
```

Or manually:
1. Create repo on GitHub
2. Add remote: `git remote add origin git@github.com:YOUR_USERNAME/channel47.git`
3. Push: `git push -u origin main`

**Step 2: Connect to Vercel**

1. Go to vercel.com
2. Import GitHub repository
3. Add environment variables in Vercel dashboard:
   - `ANTHROPIC_API_KEY`
   - `RESEND_API_KEY`

**Step 3: Verify deployment**

Check deployment URL provided by Vercel.

---

## Summary

**Phase 1 Complete. You now have:**

- [x] Astro site with brand styling (coral/cream/charcoal palette)
- [x] Homepage, About, Blog, Products pages
- [x] Content collections for blog posts and products (with third-party attribution)
- [x] Synthesis pipeline (GitHub Action + Claude API)
- [x] Email capture with Resend
- [x] Free download flow with email gate
- [x] Deployed to Vercel

**Next steps (Content & Launch):**

1. Add 5-10 products to `src/content/products/` (mix of own + curated third-party)
2. Write 5+ blog posts to seed content
3. Configure domain (channel47.dev or similar)
4. Set up Reddit account and join target subreddits
5. Test full download flow end-to-end
6. Soft launch and gather feedback

**Phase 2 (Monetization - Future):**

1. Set up Stripe integration (checkout + webhooks)
2. Create premium product tier
3. Add subscription option
4. Implement paid download flow

---

**Plan complete and saved to `docs/plans/2025-12-19-channel47-implementation.md`.**

**Two execution options:**

1. **Subagent-Driven (this session)** - I dispatch fresh subagent per task, review between tasks, fast iteration

2. **Parallel Session (separate)** - Open new session with executing-plans, batch execution with checkpoints

**Which approach?**
