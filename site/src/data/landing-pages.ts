/**
 * Landing Page Configurations
 *
 * Defines which plugins appear on which landing pages.
 * Each landing page targets a specific workflow/profession.
 * Plugins can appear on multiple landing pages.
 */

export interface LandingPage {
  /** URL slug (e.g., "media-buyer" -> /for/media-buyer) */
  slug: string;

  /** Page title for meta tags */
  title: string;

  /** Hero headline */
  headline: string;

  /** Hero description / meta description */
  description: string;

  /** Product section headline */
  productHeadline: string;

  /** Product section description */
  productDescription: string;

  /** Email segmentation tag */
  waitlistTag: string;

  /** Plugin IDs from tools.generated.json */
  plugins: string[];

  /** Optional custom label for tools section */
  toolsHeadline?: string;
}

export const landingPages: LandingPage[] = [
  {
    slug: 'media-buyer',
    title: 'AI Tools for Media Buyers',
    headline: 'Run Google Ads from your IDE.',
    description:
      'Query accounts, generate reports, and manage campaigns without leaving Claude Code.',
    productHeadline: 'Learn the system.',
    productDescription:
      'A complete guide to building an AI-powered ads workflow. From setup to scale.',
    waitlistTag: 'media-buyer',
    plugins: ['google-ads-specialist', 'copywriting-expert', 'creative-designer'],
    toolsHeadline: 'The tools',
  },
];

/**
 * Helper to get a landing page by slug
 */
export function getLandingPage(slug: string): LandingPage | undefined {
  return landingPages.find((page) => page.slug === slug);
}

/**
 * Helper to get all plugin IDs featured on any landing page
 */
export function getFeaturedPluginIds(): string[] {
  const ids = new Set(landingPages.flatMap((page) => page.plugins));
  return Array.from(ids);
}
