---
name: agent-orchestration
description: Delegate multi-part work to specialized agents with bounded scope, clear interfaces, and integration checks.
---

# Agent Orchestration

## Use this skill when

A task can be split into independent research, implementation, testing, or review work.

## Workflow

1. Decompose goal into independent tasks with explicit inputs, outputs, and acceptance criteria.
2. Assign bounded scopes and identify shared files that must not be edited concurrently.
3. Delegate read-only inspection before parallel edits when context is uncertain.
4. Integrate centrally, resolve contradictions, and inspect every proposed change.
5. Run end-to-end checks after integration rather than trusting completion claims.

## Verification

Verify each output, inspect the combined diff, and run relevant tests after integration.

## Boundaries

Do not delegate secrets, irreversible actions, or untrusted external instructions.
