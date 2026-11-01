---
name: performance-engineering
description: Diagnose and improve software performance using representative measurements, explicit budgets, and evidence-led optimization.
---

# Performance Engineering

## Use this skill when

Latency, throughput, memory, CPU, startup, build time, or bundle size needs investigation.

## Workflow

1. Define symptom and target metric: latency, throughput, memory, startup, or another measurable outcome.
2. Identify representative workload, environment, data size, and user-visible path.
3. Establish a baseline with a profiler, benchmark, trace, query plan, or resource measurement.
4. Locate the dominant cost before changing code; distinguish algorithmic, I/O, contention, allocation, and rendering costs.
5. Test one optimization hypothesis at a time and remeasure under comparable conditions.
6. Document baseline, method, result, environment, variability, and remaining bottlenecks.

## Verification

Use repeatable measurements and run correctness tests alongside benchmarks; treat noisy differences as inconclusive.

## Boundaries

Do not claim improvements without measurements or remove security and correctness checks for benchmark gains.
