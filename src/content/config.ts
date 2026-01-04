/**
 * Channel 47 Content Collections
 *
 * Defines the schema for markdown content collections.
 * See: https://docs.astro.build/en/guides/content-collections/
 */

import { defineCollection, z } from 'astro:content';

/**
 * Posts Collection
 * For blog posts, articles, and general content
 */
const postsCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    date: z.coerce.date(),
    draft: z.boolean().default(false),
    tags: z.array(z.string()).optional(),
    author: z.string().optional(),
    image: z.object({
      src: z.string(),
      alt: z.string(),
    }).optional(),
  }),
});

/**
 * Pages Collection
 * For static pages like About, Contact, etc.
 */
const pagesCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    draft: z.boolean().default(false),
  }),
});

export const collections = {
  posts: postsCollection,
  pages: pagesCollection,
};
