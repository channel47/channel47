// scripts/sync-marketplace.ts
import * as fs from 'fs/promises';
import * as path from 'path';
import matter from 'gray-matter';
import type { MarketplaceData, PluginMerged } from './types/marketplace';

const MARKETPLACE_PATH = path.join(process.cwd(), 'marketplace');
const PLUGINS_CONTENT_PATH = path.join(process.cwd(), 'src/content/plugins');
const BLOG_CONTENT_PATH = path.join(process.cwd(), 'src/content/blog');
const OUTPUT_PATH = path.join(process.cwd(), 'src/data/merged-plugins.json');

async function loadMarketplaceData(): Promise<MarketplaceData | null> {
  const jsonPath = path.join(MARKETPLACE_PATH, '.claude-plugin/marketplace.json');
  try {
    const content = await fs.readFile(jsonPath, 'utf-8');
    return JSON.parse(content);
  } catch {
    // Marketplace not initialized - return null (pivoting to hosted MCP)
    return null;
  }
}

async function loadPluginMarkdown(slug: string): Promise<string | undefined> {
  const mdPath = path.join(PLUGINS_CONTENT_PATH, `${slug}.md`);
  try {
    return await fs.readFile(mdPath, 'utf-8');
  } catch {
    return undefined;
  }
}

async function discoverRelatedPosts(pluginSlug: string) {
  try {
    const files = await fs.readdir(BLOG_CONTENT_PATH);
    const blogPosts = [];

    for (const file of files) {
      if (!file.endsWith('.md')) continue;

      const filePath = path.join(BLOG_CONTENT_PATH, file);
      const content = await fs.readFile(filePath, 'utf-8');
      const { data } = matter(content);

      // Skip draft posts
      if (data.draft === true) continue;

      // Check if this post uses the plugin
      const toolsUsed = data.toolsUsed as Array<{ slug: string; source: string }> | undefined;
      if (toolsUsed?.some(tool => tool.slug === pluginSlug && tool.source === 'channel47')) {
        const slug = file.replace(/\.md$/, '');
        blogPosts.push({
          title: data.title as string,
          slug,
          date: new Date(data.date).toISOString(),
        });
      }
    }

    // Sort by date descending (newest first)
    return blogPosts.sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime());
  } catch (error) {
    // If blog directory doesn't exist or other error, return empty array
    return [];
  }
}

async function syncMarketplace(): Promise<void> {
  console.log('Syncing marketplace data...');

  const marketplaceData = await loadMarketplaceData();

  // If no marketplace data, write empty array and exit gracefully
  if (!marketplaceData) {
    console.log('⚠ Marketplace not found - writing empty plugins array');
    await fs.mkdir(path.dirname(OUTPUT_PATH), { recursive: true });
    await fs.writeFile(OUTPUT_PATH, JSON.stringify([], null, 2));
    return;
  }

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

syncMarketplace().catch(console.error);
