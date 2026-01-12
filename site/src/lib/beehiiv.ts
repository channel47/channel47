/**
 * Beehiiv API Client
 *
 * Fetches newsletter posts from the beehiiv API.
 * Used by blog pages to display newsletter content.
 *
 * Required environment variables:
 * - BEEHIIV_API_KEY: API key from beehiiv Settings → Integrations
 * - BEEHIIV_PUBLICATION_ID: Publication ID from beehiiv Settings
 */

const API_BASE = 'https://api.beehiiv.com/v2';

// Type definitions for beehiiv API responses
export interface BeehiivPost {
  id: string;
  title: string;
  subtitle: string | null;
  slug: string;
  authors: string[];
  thumbnail_url: string | null;
  web_url: string;
  created: number;
  publish_date: number;
  displayed_date: number;
  status: 'draft' | 'confirmed' | 'archived';
  audience: 'free' | 'premium' | 'both';
  platform: 'web' | 'email' | 'both';
  content_tags: string[];
  meta_default_title: string | null;
  meta_default_description: string | null;
  content?: {
    free?: {
      web?: string;
      email?: string;
      rss?: string;
    };
  };
}

interface BeehiivListResponse {
  data: BeehiivPost[];
  limit: number;
  page: number;
  total_results: number;
  total_pages: number;
}

interface BeehiivSingleResponse {
  data: BeehiivPost;
}

interface GetAllPostsOptions {
  limit?: number;
  page?: number;
}

interface GetAllPostsResult {
  posts: BeehiivPost[];
  pagination: {
    page: number;
    limit: number;
    totalResults: number;
    totalPages: number;
  };
}

/**
 * Gets API credentials from environment variables
 */
function getCredentials(): { apiKey: string; publicationId: string } {
  const apiKey = import.meta.env.BEEHIIV_API_KEY;
  const publicationId = import.meta.env.BEEHIIV_PUBLICATION_ID;

  if (!apiKey || !publicationId) {
    throw new Error(
      'Missing beehiiv configuration. Set BEEHIIV_API_KEY and BEEHIIV_PUBLICATION_ID environment variables.'
    );
  }

  return { apiKey, publicationId };
}

/**
 * Fetches all published posts from beehiiv
 *
 * @param options.limit - Number of posts per page (default: 20, max: 100)
 * @param options.page - Page number (default: 1)
 * @returns Posts array and pagination info
 */
export async function getAllPosts(
  options: GetAllPostsOptions = {}
): Promise<GetAllPostsResult> {
  const { apiKey, publicationId } = getCredentials();
  const { limit = 20, page = 1 } = options;

  const params = new URLSearchParams({
    status: 'confirmed',
    platform: 'web',
    expand: 'free_web_content',
    limit: String(Math.min(limit, 100)),
    page: String(page),
  });

  const response = await fetch(
    `${API_BASE}/publications/${publicationId}/posts?${params}`,
    {
      headers: {
        Authorization: `Bearer ${apiKey}`,
        'Content-Type': 'application/json',
      },
    }
  );

  if (!response.ok) {
    const error = await response.text();
    console.error('Beehiiv API error:', response.status, error);
    throw new Error(`Failed to fetch posts from beehiiv: ${response.status}`);
  }

  const data: BeehiivListResponse = await response.json();

  // Sort by displayed_date descending (newest first)
  const sortedPosts = data.data.sort(
    (a, b) => b.displayed_date - a.displayed_date
  );

  return {
    posts: sortedPosts,
    pagination: {
      page: data.page,
      limit: data.limit,
      totalResults: data.total_results,
      totalPages: data.total_pages,
    },
  };
}

/**
 * Fetches a single post by slug
 *
 * @param slug - The post slug
 * @returns The post or null if not found
 */
export async function getPostBySlug(slug: string): Promise<BeehiivPost | null> {
  const { apiKey, publicationId } = getCredentials();

  // Beehiiv doesn't have a get-by-slug endpoint, so we fetch all and filter
  // In a real implementation, you might cache this or use a different strategy
  const params = new URLSearchParams({
    status: 'confirmed',
    platform: 'web',
    expand: 'free_web_content',
    limit: '100',
  });

  const response = await fetch(
    `${API_BASE}/publications/${publicationId}/posts?${params}`,
    {
      headers: {
        Authorization: `Bearer ${apiKey}`,
        'Content-Type': 'application/json',
      },
    }
  );

  if (!response.ok) {
    const error = await response.text();
    console.error('Beehiiv API error:', response.status, error);
    throw new Error(`Failed to fetch post from beehiiv: ${response.status}`);
  }

  const data: BeehiivListResponse = await response.json();
  const post = data.data.find((p) => p.slug === slug);

  return post || null;
}

/**
 * Fetches the N most recent posts
 *
 * @param count - Number of posts to return
 * @returns Array of recent posts
 */
export async function getRecentPosts(count: number): Promise<BeehiivPost[]> {
  const { posts } = await getAllPosts({ limit: count });
  return posts.slice(0, count);
}

/**
 * Fetches related posts based on content tags
 *
 * @param tags - Tags to match
 * @param excludeSlug - Slug of current post to exclude
 * @param count - Number of posts to return
 * @returns Array of related posts
 */
export async function getRelatedPosts(
  tags: string[],
  excludeSlug: string,
  count: number = 2
): Promise<BeehiivPost[]> {
  const { posts } = await getAllPosts({ limit: 50 });

  // Filter out current post
  const otherPosts = posts.filter((p) => p.slug !== excludeSlug);

  // Find posts with matching tags
  const relatedByTags = otherPosts.filter((post) =>
    post.content_tags.some((tag) => tags.includes(tag))
  );

  if (relatedByTags.length >= count) {
    return relatedByTags.slice(0, count);
  }

  // Fill with recent posts if not enough tag matches
  const remaining = count - relatedByTags.length;
  const recentFiller = otherPosts
    .filter((p) => !relatedByTags.includes(p))
    .slice(0, remaining);

  return [...relatedByTags, ...recentFiller];
}

/**
 * Converts a Unix timestamp to a JavaScript Date
 */
export function timestampToDate(timestamp: number): Date {
  return new Date(timestamp * 1000);
}

/**
 * Formats a date for display
 */
export function formatDate(date: Date): string {
  return new Intl.DateTimeFormat('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
  }).format(date);
}

/**
 * Formats a date in long form
 */
export function formatDateLong(date: Date): string {
  return new Intl.DateTimeFormat('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  }).format(date);
}
