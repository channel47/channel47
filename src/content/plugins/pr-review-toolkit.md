---
featured: true
draft: false
---

## What it does

Automated code review that actually helps. This plugin analyzes pull requests using specialized agents for security, performance, testing, and architecture—giving you specific feedback instead of generic suggestions.

## Key Features

- **Multi-agent review**: Security, performance, testing, and architecture specialists analyze your PR
- **Actionable feedback**: Specific line-level comments with fix suggestions
- **Security scanning**: Detects common vulnerabilities, SQL injection risks, XSS issues
- **Performance analysis**: Identifies N+1 queries, inefficient algorithms, memory leaks
- **Test coverage gaps**: Flags missing edge cases and untested code paths
- **Architecture consistency**: Ensures changes align with existing patterns

## Real-world use cases

I use this before submitting PRs to:

- Catch security issues before code review (SQL injection, authentication bypasses)
- Find performance bottlenecks early (database query inefficiencies, algorithm complexity)
- Identify missing test cases (edge conditions, error handling paths)
- Ensure consistent patterns (matching existing architecture and code style)
- Get faster approvals (reviewers trust the automated security/performance checks)

## What makes it different

Instead of running multiple linters and scanners separately, this plugin coordinates specialized agents:

- Security agent focuses on authentication, authorization, input validation
- Performance agent analyzes database queries, algorithm complexity, caching
- Testing agent identifies coverage gaps and suggests test cases
- Architecture agent ensures consistency with existing codebase patterns

Each agent provides context-aware feedback specific to your stack and frameworks.

## Setup

1. Install: `/plugin install pr-review-toolkit@claude-plugins-official`
2. Run review: `/review-pr` (analyzes current branch)
3. Or review specific PR: `/review-pr 123`

## Example workflows

**Pre-submission review:**

```
/review-pr
```

Analyzes all changes in your current branch against main. Gets feedback before pushing.

**Review existing PR:**

```
/review-pr 456
```

Reviews GitHub PR #456. Useful for reviewing teammate PRs or double-checking before merge.

**Focus on specific concerns:**

```
/review-pr --focus security,performance
```

Skips testing and architecture agents, runs only security and performance analysis.

## Available skills

- `/review-pr` - Comprehensive PR review using specialized agents

## Agents

Four specialized review agents automatically coordinate:

- **Security Reviewer**: Authentication, authorization, input validation, SQL injection, XSS
- **Performance Analyzer**: Query efficiency, algorithm complexity, memory usage, caching
- **Test Coverage Expert**: Edge cases, error handling, integration test gaps
- **Architecture Guardian**: Pattern consistency, separation of concerns, dependency management

Each agent provides specific line-level feedback with severity ratings and fix suggestions.
