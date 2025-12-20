# GitHub Actions Secrets Setup for Synthesis Workflow

**Date:** 2025-12-20
**Tags:** github-actions, secrets, api-keys, workflow

---

> User: I just added a 'repository secret' for the anthropic api key in the github repo. Is this correct, or do I need a specific 'environment secret'?

Great question! You're correct - a **repository secret** is exactly what you need.

Looking at your workflow, it references the secret like this:

```yaml
- name: Synthesize content
  env:
    ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
```

## Repository Secrets vs Environment Secrets

**Repository Secrets** (what you set up):
- Available to all workflows in the repository
- Referenced as `${{ secrets.SECRET_NAME }}`
- No additional configuration needed
- Perfect for API keys used across multiple workflows

**Environment Secrets** (not needed here):
- Tied to specific environments (production, staging, etc.)
- Require the workflow to specify which environment to use
- Add protection rules like approvals and branch restrictions
- Would require adding `environment: production` to the job

Since your workflow doesn't specify an environment, it pulls from repository secrets by default.

## When to Use Each Type

**Use Repository Secrets when:**
- The secret is used across multiple workflows
- No environment-specific protection is needed
- You want simple, straightforward access

**Use Environment Secrets when:**
- Deploying to production and need approval gates
- Different credentials for staging vs production
- Want to restrict which branches can access secrets

> User: So I'm all set then?

Yes! Your setup is correct. The workflow will now:
1. Detect new log files on push
2. Access the API key from your repository secret
3. Call Claude API to synthesize content
4. Create a PR with generated blog posts and X content

The repository secret you added is exactly what the workflow needs.
