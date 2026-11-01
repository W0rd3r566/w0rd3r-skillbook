---
name: github-actions
description: Create maintainable GitHub Actions workflows with least privilege, reliable triggers, and useful feedback.
---

# GitHub Actions

## Use this skill when

Creating or changing CI, GitHub Actions, or repository automation.

## Workflow

1. Inspect language, package manager, workflows, branch strategy, and required checks.
2. Use narrow GITHUB_TOKEN permissions and pin third-party actions to immutable SHAs where feasible.
3. Define triggers, concurrency, caching, timeouts, and failure behavior explicitly.
4. Separate validation from publishing or deployment; gate privileged steps behind trusted conditions.
5. Avoid printing secrets or passing untrusted pull-request data into privileged contexts.

## Verification

Validate YAML and workflow syntax; test commands locally and inspect trigger and permission behavior.

## Boundaries

Never expose secrets. Do not deploy, publish, or change repository settings without authorization.
