---
featured: false
draft: false
---

## What it does

Deploy to Vercel directly from Claude Code. No switching to terminal, no remembering CLI commands—just `/deploy` and your site goes live with preview URLs, deployment logs, and automatic rollback on failures.

## Key Features

- **One-command deploys**: `/deploy` handles authentication, build, and deployment
- **Preview URLs**: Get shareable URLs immediately after deployment
- **Live logs**: Stream build and deployment logs in real-time
- **Environment management**: Switch between production, preview, and development environments
- **Automatic rollback**: Reverts to previous deployment if build fails
- **Project linking**: Auto-detects Vercel projects or guides setup for new projects

## Real-world use cases

I use this constantly for:

- Quick preview deployments when testing features (get shareable URL in seconds)
- Production deployments without context switching (stay in editor)
- Debugging failed builds (logs stream directly in Claude Code)
- Environment variable updates (no hunting through web dashboard)
- Checking deployment status (skip opening browser)

## What makes it different

Instead of:

- Opening terminal
- Running `vercel deploy`
- Copying URL from output
- Opening browser to check logs
- Switching back to editor

You just type `/deploy` and continue working. The plugin handles authentication, shows live progress, and gives you the preview URL without leaving your workflow.

## Setup

1. Install: `/plugin install vercel@claude-plugins-official`
2. First deploy: `/setup` (authenticates and links project)
3. Subsequent deploys: `/deploy`

## Example workflows

**Quick preview deploy:**

```
/deploy
```

Deploys current branch to Vercel preview environment. Returns shareable URL.

**Production deployment:**

```
/deploy --prod
```

Deploys to production after confirmation prompt.

**Check deployment logs:**

```
/logs
```

Shows recent deployment logs and status.

**Initial setup:**

```
/setup
```

Authenticates with Vercel and links current directory to project.

## Available skills

- `/deploy` - Deploy the current project to Vercel
- `/logs` - View deployment logs from Vercel
- `/setup` - Set up Vercel CLI and configure the project

All commands work with both personal and team accounts. The plugin detects your project configuration automatically.
