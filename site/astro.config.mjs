import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://channel47.dev',
  integrations: [sitemap()],
  redirects: {
    '/setup': '/tools/google-ads',
    '/skills': '/tools',
    '/skills/google-ads': '/tools/google-ads',
    '/skills/ad-creative': '/tools/creative-designer'
  }
});
