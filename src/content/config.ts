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
    toolsUsed: z.array(z.object({
      slug: z.string(),
      source: z.enum(['channel47', 'external']),
      installCommand: z.string().optional(),
    })).optional(),
  }),
});

export const collections = { blog };
