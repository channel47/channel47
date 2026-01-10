import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://channel47.dev',
  integrations: [sitemap()],
  redirects: {
    '/setup': '/tools/google-ads-specialist',
    '/skills': '/tools',
    '/skills/google-ads': '/tools/google-ads-specialist',
    '/skills/ad-creative': '/tools/designer',
    // Legacy redirects for old URLs
    '/tools/google-ads': '/tools/google-ads-specialist',
    '/tools/creative-designer': '/tools/designer',
    '/tools/copywriting': '/tools/copywriter',
    '/tools/prompt-enhancer': '/tools/prompt-engineer'
  }
});
