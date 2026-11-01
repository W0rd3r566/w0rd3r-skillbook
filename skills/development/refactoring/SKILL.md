---
name: refactoring
description: Improve code structure while preserving externally observable behavior and keeping changes reviewable.
---

# Safe Refactoring

## Use this skill when

Readability, duplication, or maintainability needs improvement without intended behavior change.

## Workflow

1. Map current behavior, public interfaces, side effects, and callers.
2. Inspect tests and add characterization tests for fragile behavior.
3. Choose one refactoring objective and define invariants that must remain unchanged.
4. Refactor in small steps, preserving interfaces unless change is required.
5. Remove code only after confirming it is unused and safe to delete.

## Verification

Run focused tests after each step and broader relevant tests at the end.

## Boundaries

Do not combine large feature work with refactoring. Ask before changing public APIs or persisted formats.
