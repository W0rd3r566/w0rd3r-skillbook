---
name: api-design
description: Design predictable, secure, versionable APIs with clear contracts, errors, and compatibility expectations.
---

# API Design

## Use this skill when

Designing or changing HTTP, RPC, library, or internal APIs.

## Workflow

1. Identify consumers, use cases, data ownership, authentication, and compatibility needs.
2. Define operations, request and response schemas, validation, and error format.
3. Use consistent naming, status codes, pagination, filtering, and idempotency where relevant.
4. Specify authorization, rate limits, and sensitive-data handling.
5. Document versioning and deprecation before breaking changes.

## Verification

Test success, validation, authorization failures, missing resources, pagination boundaries, and compatibility.

## Boundaries

Do not expose secrets or stack traces. Do not make breaking changes without a migration plan.
