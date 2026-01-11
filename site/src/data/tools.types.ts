/**
 * Type definitions for generated tool data.
 *
 * This file provides TypeScript types for the tools.generated.json file
 * created by the sync-plugins.ts script.
 */

export interface GeneratedTool {
  /** Plugin ID from plugin.json name field */
  id: string;
  /** Plugin version */
  version: string;
  /** Marketing display name */
  displayName: string;
  /** Short tagline for cards */
  tagline: string;
  /** Type label (e.g., "MCP Server + Plugin", "Claude Code Plugin") */
  label: string;
  /** Feature list for detail pages */
  features: string[];
  /** URL path for the tool page */
  href: string;
  /** GitHub repository URL */
  github: string;
  /** Whether the plugin includes an MCP server */
  hasMcp: boolean;
}

export interface GeneratedToolsData {
  /** ISO timestamp of when the data was generated */
  generatedAt: string;
  /** Array of tool data */
  tools: GeneratedTool[];
}
