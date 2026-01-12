import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import vercel from '@astrojs/vercel';

export default defineConfig({
  site: 'https://channel47.dev',
  output: 'static',
  adapter: vercel({
    webAnalytics: {
      enabled: true
    },
    functionPerRoute: false,
    runtime: 'nodejs20.x'
  }),
  integrations: [sitemap()],
  redirects: {
    '/setup': '/tools/google-ads',
    '/skills': '/tools',
    '/skills/google-ads': '/tools/google-ads',
    '/skills/ad-creative': '/tools/creative-designer',
    // Redirect old blog posts to archive
    '/blog/mcp-servers-marketers': '/archive/blog/mcp-servers-marketers',
    '/blog/gaql-queries-guide': '/archive/blog/gaql-queries-guide',
    '/blog/claude-google-ads-audits': '/archive/blog/claude-google-ads-audits'
  }
});
