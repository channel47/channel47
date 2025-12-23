---
featured: false
draft: false
---

## What it does

Build Model Context Protocol (MCP) servers without wrestling with boilerplate. This plugin generates complete MCP implementations—tools, resources, prompts—with proper TypeScript types, error handling, and testing scaffolds.

## Key Features

- **Scaffold complete servers**: Generate project structure, dependencies, configuration
- **Tool definitions**: Create MCP tools with JSON schema validation
- **Resource providers**: Implement file, database, or API resource access
- **Prompt templates**: Define reusable prompt templates with parameter substitution
- **TypeScript-first**: Proper types, interfaces, and error handling
- **Testing setup**: Jest configuration with example tests for your tools
- **Transport options**: Supports stdio, HTTP, and WebSocket transports

## Real-world use cases

I use this to quickly build MCP servers for:

- Database access (query tools, schema inspection, data export)
- API integrations (third-party services as MCP tools)
- File system operations (project-specific file handling)
- Custom workflows (company-specific automation tools)
- Development utilities (code generation, refactoring helpers)

The plugin handles all the protocol boilerplate so you can focus on implementing your actual tool logic.

## What makes it different

Building MCP servers from scratch requires:

- Understanding the protocol specification
- Setting up TypeScript configuration
- Implementing transport layer (stdio/HTTP/WebSocket)
- Writing JSON schemas for tool parameters
- Handling errors and edge cases
- Creating test infrastructure

This plugin generates all of that. You just describe what your server should do, and it creates a working implementation you can customize.

## Setup

1. Install: `/plugin install mcp-builder@channel47`
2. Create server: `/mcp-builder "database query server with PostgreSQL connection"`
3. Customize generated code in `./mcp-servers/<server-name>/`

## Example workflows

**Create new MCP server:**

```
/mcp-builder "Notion API integration with page search and content extraction tools"
```

Generates complete project with tool definitions, TypeScript types, and transport setup.

**Add tools to existing server:**

```
/mcp-builder add-tool "search pages by title" --server notion-mcp
```

Adds new tool definition to existing server with proper schema validation.

**Scaffold resource provider:**

```
/mcp-builder add-resource "notion pages as resources" --server notion-mcp
```

Implements resource provider for exposing Notion pages via MCP resource protocol.

## Available skills

- `/mcp-builder` - Build Model Context Protocol servers with proper structure and types

The skill generates:

- Complete project structure (package.json, tsconfig.json, src/ directory)
- Tool implementations with JSON schema validation
- Resource providers for data access
- Prompt templates for reusable prompts
- Transport layer configuration (stdio/HTTP/WebSocket)
- Testing setup with example tests
- README with usage examples

Output is a working MCP server you can immediately test and deploy.
