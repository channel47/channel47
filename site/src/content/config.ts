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

/**
 * Skills Collection
 * For MCP skill files with distribution metadata
 */
const skillsCollection = defineCollection({
  type: 'content',
  schema: z.object({
    // Core metadata
    title: z.string(),
    description: z.string(),
    version: z.string().default('1.0.0'),

    // Categorization
    category: z.enum([
      'google-ads',
      'analytics',
      'automation',
      'reporting',
      'optimization',
      'other'
    ]).default('other'),
    tags: z.array(z.string()).optional(),

    // Distribution
    tier: z.enum(['free', 'premium']).default('free'),
    price: z.number().optional(), // USD, only for premium
    stripeProductId: z.string().optional(), // For Stripe checkout
    stripePriceId: z.string().optional(),

    // Skill file reference
    skillFile: z.string().optional(), // Path to actual .md skill file

    // Status
    draft: z.boolean().default(false),
    featured: z.boolean().default(false),

    // Dates
    publishedAt: z.coerce.date(),
    updatedAt: z.coerce.date().optional(),

    // Social proof
    downloads: z.number().default(0),
  }),
});

export const collections = {
  posts: postsCollection,
  pages: pagesCollection,
  skills: skillsCollection,
};
