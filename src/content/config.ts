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
