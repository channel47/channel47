// scripts/synthesize.ts
import 'dotenv/config';
import Anthropic from '@anthropic-ai/sdk';
import * as fs from 'fs/promises';
import * as path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const anthropic = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY,
});

// GoogleGenerativeAI SDK initialized when needed in generateImageViaAPI

async function loadPrompt(): Promise<string> {
  const promptPath = path.join(__dirname, 'prompts', 'synthesis.md');
  return fs.readFile(promptPath, 'utf-8');
}

async function generateImageViaAPI(
  prompt: string,
  apiKey: string
): Promise<Buffer> {
  const url = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-image:generateContent?key=${apiKey}`;

  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      contents: [
        {
          parts: [
            {
              text: prompt,
            },
          ],
        },
      ],
      generationConfig: {
        response_modalities: ['image'],
      },
    }),
  });

  if (!response.ok) {
    const errorText = await response.text();
    throw new Error(`Gemini API error: ${response.status} ${response.statusText}\n${errorText}`);
  }

  const result = await response.json();

  // Extract image data from response
  if (
    !result.candidates ||
    !result.candidates[0] ||
    !result.candidates[0].content ||
    !result.candidates[0].content.parts ||
    !result.candidates[0].content.parts[0]
  ) {
    throw new Error('No image data in API response');
  }

  const part = result.candidates[0].content.parts[0];

  if (!part.inlineData || !part.inlineData.data) {
    throw new Error('No inline image data found in response');
  }

  // Decode base64 image data
  const imageBase64 = part.inlineData.data;
  return Buffer.from(imageBase64, 'base64');
}

async function generateHeroImages(
  visualMetaphor: string,
  slug: string,
  outputDir: string
): Promise<{ styleA: string; styleD: string }> {
  console.log(`Generating hero images for: ${slug}`);
  console.log(`Visual metaphor: ${visualMetaphor}`);

  const apiKey = process.env.GEMINI_API_KEY;
  if (!apiKey) {
    throw new Error('GEMINI_API_KEY environment variable is required');
  }

  // Create output directory
  await fs.mkdir(outputDir, { recursive: true });

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

  try {
    console.log('Generating Style A (brand-consistent abstract)...');
    const styleAImage = await generateImageViaAPI(styleAPrompt, apiKey);
    const styleAPath = path.join(outputDir, 'style-a.png');
    await fs.writeFile(styleAPath, styleAImage);
    console.log(`✓ Style A saved to: ${styleAPath}`);

    console.log('Generating Style D (conceptual metaphor)...');
    const styleDImage = await generateImageViaAPI(styleDPrompt, apiKey);
    const styleDPath = path.join(outputDir, 'style-d.png');
    await fs.writeFile(styleDPath, styleDImage);
    console.log(`✓ Style D saved to: ${styleDPath}`);

    return {
      styleA: styleAPath.replace(/^public/, ''),
      styleD: styleDPath.replace(/^public/, ''),
    };
  } catch (error) {
    console.error('Error during image generation:', error);
    throw error;
  }
}

async function synthesize(logPath: string): Promise<void> {
  console.log(`Synthesizing: ${logPath}`);

  const logContent = await fs.readFile(logPath, 'utf-8');
  const systemPrompt = await loadPrompt();

  const message = await anthropic.messages.create({
    model: 'claude-sonnet-4-20250514',
    max_tokens: 8192,
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
    console.error('Response did not contain JSON in expected format.');
    console.error('Response preview (first 500 chars):');
    console.error(responseText.substring(0, 500));
    console.error('\n...and last 500 chars:');
    console.error(responseText.substring(responseText.length - 500));
    throw new Error('Failed to extract JSON from response');
  }

  const result = JSON.parse(jsonMatch[1]);

  // Generate filename from log path
  const logFilename = path.basename(logPath, '.md');
  const date = new Date().toISOString().split('T')[0];
  const slug = logFilename.replace(/^\d{4}-\d{2}-\d{2}-/, '');

  // Generate hero images
  const imagesDir = path.join('public', 'images', 'blog-heroes', slug);
  const heroImages = await generateHeroImages(
    result.visual_metaphor.concept,
    slug,
    imagesDir
  );

  // Write blog draft
  const blogDraftPath = path.join('drafts', 'blog', `${date}-${slug}.md`);
  const blogContent = `---
title: "${result.blog.title}"
description: "${result.blog.description}"
date: ${date}
tags: ${JSON.stringify(result.blog.tags)}
draft: true
heroImages:
  styleA: "${heroImages.styleA}"
  styleD: "${heroImages.styleD}"
  selected: null
visualMetaphor: "${result.visual_metaphor.concept}"
visualMetaphorReasoning: "${result.visual_metaphor.reasoning}"
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
