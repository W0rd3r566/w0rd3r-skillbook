---
name: security-audit
description: Review application code and configuration for realistic security weaknesses and prioritize actionable remediation.
---

# Security Audit

## Use this skill when

Defensive review of code, dependencies, or configuration.

## Workflow

1. Identify system boundaries, assets, trust levels, entry points, and sensitive data.
2. Inspect authentication, authorization, validation, encoding, secrets, dependencies, logging, and storage.
3. Trace untrusted input to sensitive operations and verify access checks at enforcement points.
4. Prioritize by exploitability, impact, exposure, and confidence; include concrete evidence.
5. Recommend minimal mitigations and regression tests; distinguish confirmed issues from questions.

## Verification

Re-check findings against code paths; run approved static or dependency checks and report scope.

## Boundaries

Keep work defensive. Do not exploit live systems, exfiltrate data, or change production without authorization.
