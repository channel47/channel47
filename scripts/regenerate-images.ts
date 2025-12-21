// scripts/regenerate-images.ts
import * as fs from 'fs/promises';
import * as path from 'path';
import { fileURLToPath } from 'url';
import matter from 'gray-matter';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

async function regenerateImages(slug: string): Promise<void> {
  // Find the blog post
  const draftPath = path.join('drafts', 'blog');
  const files = await fs.readdir(draftPath);
  const matchingFile = files.find(f => f.includes(slug));

  if (!matchingFile) {
    console.error(`❌ No blog post found matching slug: ${slug}`);
    console.error(`   Available posts in drafts/blog/:`);
    files.forEach(f => console.error(`   - ${f}`));
    process.exit(1);
  }

  const filePath = path.join(draftPath, matchingFile);
  const fileContent = await fs.readFile(filePath, 'utf-8');
  const parsed = matter(fileContent);

  const visualMetaphor = parsed.data.visualMetaphor;
  if (!visualMetaphor) {
    console.error(`❌ No visual metaphor found in ${matchingFile}`);
    console.error(`   The post needs a visualMetaphor field in frontmatter`);
    process.exit(1);
  }

  const outputDir = path.join('public', 'images', 'blog-heroes', slug);

  // Style A: Brand-consistent abstract
  const styleAPrompt = `A modern, minimalist abstract composition using geometric shapes and clean lines.
Color palette: warm coral red (#E8735C), soft cream white (#FAF9F6), and deep charcoal (#2E2E2E).
Geometric elements like circles, rectangles, rounded squares, and flowing curves arranged in a balanced, contemporary layout.
Flat design style with subtle gradients.
Apple-inspired aesthetic: spacious, refined, uncluttered.
Wide aspect ratio (16:9 for blog hero).
Professional, modern, tech-forward feeling.`;

  // Style D: Minimalist conceptual with metaphor
  const styleDPrompt = `${visualMetaphor} in a minimalist illustration style.
Clean, simple composition with maximum one or two visual elements.
Limited color palette: primarily black/white/gray with one accent color.
Lots of negative space. Conceptual and metaphorical, not literal.
Flat design, no realistic textures or shadows.
Wide aspect ratio (16:9 for blog hero).
Zen-like simplicity that hints at meaning without being obvious.`;

  console.log(`\n📋 Image Regeneration Guide for: ${slug}\n`);
  console.log(`Output directory: ${outputDir}/\n`);
  console.log(`Visual metaphor: ${visualMetaphor}\n`);
  console.log(`━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n`);

  console.log(`🎨 STYLE A - Brand Abstract\n`);
  console.log(`Use this prompt with your MCP server:`);
  console.log(`\n---\n${styleAPrompt}\n---\n`);
  console.log(`Save the generated image to: ${outputDir}/style-a.png\n`);
  console.log(`━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n`);

  console.log(`🎨 STYLE D - Conceptual Metaphor\n`);
  console.log(`Use this prompt with your MCP server:`);
  console.log(`\n---\n${styleDPrompt}\n---\n`);
  console.log(`Save the generated image to: ${outputDir}/style-d.png\n`);
  console.log(`━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n`);

  console.log(`\n📝 Next steps:`);
  console.log(`1. Copy each prompt above`);
  console.log(`2. Ask Claude Code to generate the image using your MCP server`);
  console.log(`3. Move the generated image from your MCP output dir to the specified path`);
  console.log(`4. Review both images`);
  console.log(`5. Rename your chosen image to hero.png and delete the other\n`);
}

// Main
const slug = process.argv[2];
if (!slug) {
  console.error('Usage: npx tsx scripts/regenerate-images.ts <slug>');
  console.error('Example: npx tsx scripts/regenerate-images.ts channel47-implementation');
  process.exit(1);
}

regenerateImages(slug).catch(console.error);
