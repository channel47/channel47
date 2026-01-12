import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import vercel from '@astrojs/vercel/serverless';

export default defineConfig({
  site: 'https://channel47.dev',
  output: 'hybrid',
  adapter: vercel(),
  integrations: [sitemap()],
  redirects: {
    '/setup': '/tools/google-ads',
    '/skills': '/tools',
    '/skills/google-ads': '/tools/google-ads',
    '/skills/ad-creative': '/tools/creative-designer'
  }
});
