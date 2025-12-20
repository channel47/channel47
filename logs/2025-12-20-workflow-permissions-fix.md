# GitHub Actions Workflow Permissions Fix

**Date:** 2025-12-20
**Tags:** github-actions, permissions, troubleshooting, workflow

---

> User: The synthesis workflow is failing to create pull requests. What's wrong?

Looking at the workflow logs, I can see the synthesis is working perfectly - the API is being called, content is being generated, but the PR creation step is failing with:

```
GitHub Actions is not permitted to create or approve pull requests.
```

This is a permissions issue. GitHub Actions has strict default permissions, and by default it's not allowed to create pull requests.

## The Solution

You need to enable workflow permissions in your repository settings:

1. Navigate to Repository Settings → Actions → General
2. Find the "Workflow permissions" section
3. Select "Read and write permissions"
4. Enable "Allow GitHub Actions to create and approve pull requests"
5. Save the changes

## Why This Matters

The `peter-evans/create-pull-request` action needs permission to:
- Create new branches
- Commit files to those branches
- Open pull requests

Without these permissions, the workflow can generate the content but can't deliver it via PR.

## What Happens After the Fix

Once permissions are enabled, the workflow will:
1. Detect new log files on push
2. Call Claude API to synthesize content
3. Generate blog posts and X/Twitter content
4. Commit the drafts to a new branch
5. Create a PR with a review checklist
6. You review, edit if needed, and merge

> User: Updated permissions, test the workflow again

Perfect! Let's verify it works end-to-end now.
