// scripts/types/marketplace.ts
export interface MarketplacePlugin {
  name: string;
  source: string;
  description: string;
  version: string;
  author: string;
  category: string;
  tags: string[];
}

export interface MarketplaceData {
  name: string;
  owner: {
    name: string;
    url: string;
  };
  description: string;
  metadata: {
    pluginRoot: string;
  };
  plugins: MarketplacePlugin[];
}

export interface PluginMerged extends MarketplacePlugin {
  editorialContent?: string;
  relatedPosts?: Array<{
    title: string;
    slug: string;
    date: string;
  }>;
}
