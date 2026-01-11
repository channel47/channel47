/**
 * Plugin Sync Script
 *
 * Reads plugin.json files from ../plugins and generates
 * a tools.generated.json file for the site to consume.
 *
 * Run with: npx tsx scripts/sync-plugins.ts
 */

import { readdir, readFile, writeFile, mkdir } from 'fs/promises';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const PLUGINS_DIR = join(__dirname, '../../plugins');
const OUTPUT_FILE = join(__dirname, '../src/data/tools.generated.json');

// Types for plugin manifest
interface PluginSiteData {
  displayName: string;
  tagline: string;
  label: string;
  features: string[];
}

interface PluginManifest {
  name: string;
  version: string;
  description: string;
  repository?: string;
  mcpServers?: string;
}

// Types for generated output
interface GeneratedTool {
  id: string;
  version: string;
  displayName: string;
  tagline: string;
  label: string;
  features: string[];
  href: string;
  github: string;
  hasMcp: boolean;
}

interface GeneratedOutput {
  generatedAt: string;
  tools: GeneratedTool[];
}

/**
 * Maps plugin names to URL slugs for the site.
 */
function getToolSlug(name: string): string {
  const slugMap: Record<string, string> = {
    'google-ads-specialist': 'google-ads',
    'creative-designer': 'creative-designer',
    'copywriting-expert': 'copywriting',
    'prompt-enhancer': 'prompt-enhancer',
  };
  return slugMap[name] || name;
}

/**
 * Main sync function.
 * Reads all plugin manifests and generates the tools.generated.json file.
 */
async function syncPlugins(): Promise<void> {
  console.log('Syncing plugins to site data...\n');

  // Read all plugin directories
  const pluginDirs = await readdir(PLUGINS_DIR);
  const tools: GeneratedTool[] = [];
  let skipped = 0;

  for (const pluginDir of pluginDirs) {
    // Skip hidden files and non-directories
    if (pluginDir.startsWith('.')) {
      continue;
    }

    const manifestPath = join(PLUGINS_DIR, pluginDir, '.claude-plugin/plugin.json');
    const sitePath = join(PLUGINS_DIR, pluginDir, '.claude-plugin/site.json');

    try {
      const manifestContent = await readFile(manifestPath, 'utf-8');
      const manifest: PluginManifest = JSON.parse(manifestContent);

      // Read site metadata from separate file
      let siteData: PluginSiteData;
      try {
        const siteContent = await readFile(sitePath, 'utf-8');
        siteData = JSON.parse(siteContent);
      } catch {
        console.warn(`  [SKIP] ${pluginDir}: No site.json found`);
        skipped++;
        continue;
      }

      const tool: GeneratedTool = {
        id: manifest.name,
        version: manifest.version,
        displayName: siteData.displayName,
        tagline: siteData.tagline,
        label: siteData.label,
        features: siteData.features,
        href: `/tools/${getToolSlug(manifest.name)}`,
        github: manifest.repository
          ? `${manifest.repository}/tree/main/plugins/${pluginDir}`
          : `https://github.com/channel47/channel47/tree/main/plugins/${pluginDir}`,
        hasMcp: !!manifest.mcpServers,
      };

      tools.push(tool);
      console.log(`  [OK] ${manifest.name} v${manifest.version}`);
    } catch (err) {
      if ((err as NodeJS.ErrnoException).code === 'ENOENT') {
        console.warn(`  [SKIP] ${pluginDir}: No plugin.json found`);
      } else {
        console.error(`  [ERROR] ${pluginDir}:`, err);
      }
      skipped++;
    }
  }

  // Ensure output directory exists
  await mkdir(dirname(OUTPUT_FILE), { recursive: true });

  // Generate output
  const output: GeneratedOutput = {
    generatedAt: new Date().toISOString(),
    tools,
  };

  await writeFile(OUTPUT_FILE, JSON.stringify(output, null, 2) + '\n');

  console.log('');
  console.log(`Synced ${tools.length} plugin(s) to ${OUTPUT_FILE}`);
  if (skipped > 0) {
    console.log(`Skipped ${skipped} item(s)`);
  }
}

// Run the sync
syncPlugins().catch((err) => {
  console.error('Sync failed:', err);
  process.exit(1);
});
