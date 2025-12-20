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
