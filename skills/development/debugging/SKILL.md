---
name: debugging
description: Find root causes through reproducible evidence instead of guessing, masking symptoms, or making unrelated changes.
---

# Evidence-Led Debugging

## Use this skill when

A bug, regression, crash, failing test, or unexpected behavior.

## Workflow

1. Define observed and expected behavior; isolate the smallest reproducible case.
2. Inspect relevant code, recent changes, logs, stack traces, configuration, and environment.
3. Form testable hypotheses and choose observations that distinguish them.
4. Reproduce before editing when practical; add a focused regression test.
5. Make the smallest root-cause fix and avoid unrelated cleanup.

## Verification

Re-run the reproducer and relevant regression tests; confirm adjacent behavior remains intact.

## Boundaries

Do not delete failing tests, suppress errors, or assert an unproven root cause. Ask before destructive data repair.
