import type { APIRoute } from 'astro';
import { createMcpHandler } from '@vercel/mcp-adapter';
import { z } from 'zod';

// Create the MCP handler with tools
const handler = createMcpHandler(
  (server) => {
    // Test tool - proves the MCP endpoint is working
    server.tool(
      'hello_world',
      'A simple test tool that returns a greeting',
      { name: z.string().optional().describe('Name to greet') },
      async ({ name }) => {
        const greeting = name
          ? `Hello, ${name}! Welcome to Channel 47.`
          : 'Hello from Channel 47! Your MCP connection is working.';
        return {
          content: [{ type: 'text', text: greeting }],
        };
      }
    );

    // Placeholder for Google Ads tools - will be implemented in Phase 1.3
    server.tool(
      'get_account_info',
      'Get basic information about your Google Ads account (placeholder)',
      {
        customer_id: z.string().describe('Google Ads customer ID (without dashes)')
      },
      async ({ customer_id }) => {
        // TODO: Implement actual Google Ads API call with user credentials
        return {
          content: [{
            type: 'text',
            text: `[Placeholder] Would fetch account info for customer ID: ${customer_id}\n\nThis tool will be fully functional after OAuth integration.`
          }],
        };
      }
    );

    server.tool(
      'get_campaign_performance',
      'Get performance metrics for campaigns (placeholder)',
      {
        customer_id: z.string().describe('Google Ads customer ID'),
        date_range: z.enum(['TODAY', 'YESTERDAY', 'LAST_7_DAYS', 'LAST_30_DAYS', 'THIS_MONTH']).optional().describe('Date range for metrics')
      },
      async ({ customer_id, date_range = 'LAST_7_DAYS' }) => {
        // TODO: Implement actual Google Ads API call
        return {
          content: [{
            type: 'text',
            text: `[Placeholder] Would fetch campaign performance for:\n- Customer ID: ${customer_id}\n- Date Range: ${date_range}\n\nThis tool will return real metrics after OAuth integration.`
          }],
        };
      }
    );
  },
  {
    capabilities: {
      tools: {}
    }
  },
  {
    basePath: '/api/mcp',
    verboseLogs: true,
    maxDuration: 60,
  }
);

// Astro API route handlers
export const GET: APIRoute = async ({ request }) => {
  return handler(request);
};

export const POST: APIRoute = async ({ request }) => {
  return handler(request);
};

export const DELETE: APIRoute = async ({ request }) => {
  return handler(request);
};
