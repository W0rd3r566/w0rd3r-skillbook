---
name: testing
description: Design focused automated tests for behavior, edge cases, and regressions without brittle implementation coupling.
---

# Testing Strategy

## Use this skill when

Adding, repairing, or improving automated tests or test strategy.

## Workflow

1. Inspect test framework, fixtures, naming conventions, and CI commands.
2. Derive tests from observable requirements and realistic failure modes.
3. Cover normal cases, boundaries, invalid input, and relevant failures.
4. Prefer deterministic tests with isolated state; avoid arbitrary sleeps.
5. Mock external boundaries only, not the behavior under test.

## Verification

Run narrow tests first, then broader suites; report flaky, skipped, or environment-dependent tests.

## Boundaries

Do not weaken assertions just to pass. Understand a failing test before changing production code.
