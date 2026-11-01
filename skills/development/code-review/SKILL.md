---
name: code-review
description: Review changes for correctness, regressions, security, maintainability, and missing tests with actionable findings.
---

# Code Review

## Use this skill when

A diff, pull request, patch, or proposed implementation needs review.

## Workflow

1. Read the diff and surrounding code to understand callers and behavior.
2. Prioritize concrete defects: correctness, security, data loss, compatibility, and performance.
3. For each finding, cite file and line, explain a failure scenario, and suggest a focused fix.
4. Check test coverage for changed behavior and edge cases.
5. Separate blocking findings from optional improvements and state uncertainty.

## Verification

Verify findings against actual code. If none are found, state scope reviewed and remaining test gaps.

## Boundaries

Do not invent findings or modify code unless asked.
