---
name: database-design
description: Design reliable data models, constraints, indexes, and migrations with integrity and operational safety in mind.
---

# Database Design

## Use this skill when

A schema, query, migration, or persistence layer needs design or review.

## Workflow

1. Inspect database engine, schema conventions, data volume, and migration system.
2. Model entities around domain rules; define nullability, uniqueness, and referential integrity.
3. Choose indexes based on query patterns and measured or expected access paths.
4. Plan migrations for existing data, locks, backfills, rollback, and mixed application versions.
5. Use transactions for multi-step changes that must remain consistent.

## Verification

Test migrations on disposable or staging data; validate constraints and representative queries.

## Boundaries

Never run destructive migrations or production data changes without authorization and verified backup/rollback.
