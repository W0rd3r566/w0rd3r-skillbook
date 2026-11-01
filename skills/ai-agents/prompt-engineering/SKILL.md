---
name: prompt-engineering
description: Write clear, testable instructions for language models and agents with explicit goals, constraints, and output expectations.
---

# Prompt Engineering

## Use this skill when

System prompts, agent instructions, task prompts, or reusable workflows.

## Workflow

1. Define task, target model or environment, user context, and success criteria.
2. Separate trusted instructions from untrusted input and retrieved content.
3. State required steps, constraints, tool boundaries, and output format explicitly.
4. Use examples only to resolve ambiguity; remove contradictory and redundant rules.
5. Design evaluation cases for normal, ambiguous, adversarial, and failure inputs.

## Verification

Test representative cases against explicit criteria; record model-specific assumptions.

## Boundaries

Do not promise deterministic behavior or place secrets and private data in prompts unnecessarily.
