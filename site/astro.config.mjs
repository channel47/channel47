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
    '/skills/ad-creative': '/tools/creative-designer'
  }
});
