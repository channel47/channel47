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
