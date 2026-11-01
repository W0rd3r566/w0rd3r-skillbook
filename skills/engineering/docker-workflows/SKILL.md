---
name: docker-workflows
description: Build reproducible, secure container workflows for development, testing, and deployment.
---

# Docker Workflows

## Use this skill when

Dockerfiles, Compose, images, or container workflows.

## Workflow

1. Inspect runtime needs, existing images, Compose files, build context, and deployment environment.
2. Use trusted base images and pin versions appropriately for reproducibility.
3. Use multi-stage builds when they materially reduce image size or attack surface.
4. Run as non-root where practical; keep secrets out of images and build arguments.
5. Define health checks, volumes, networks, and resource expectations.

## Verification

Build and run the image; inspect logs and health; test persistence and shutdown where relevant.

## Boundaries

Do not use privileged mode or mount the host Docker socket without an approved need.
