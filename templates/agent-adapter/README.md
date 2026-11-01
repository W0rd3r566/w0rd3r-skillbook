# Agent adapter template

Use this template only when an agent cannot consume the canonical skill layout directly.

## Before creating an adapter

1. Confirm the agent's official skill format and discovery paths.
2. Check whether it already reads `.agents/skills/` or another shared location.
3. Prefer copying/linking the canonical skill folder over rewriting its content.
4. Never silently drop safety boundaries, verification steps, or required metadata.

## Adapter contract

An adapter should:
- declare the target agent and supported versions;
- map canonical skill files to the target's documented location;
- preserve the original skill content;
- report unsupported metadata instead of silently discarding it;
- include a repeatable install/discovery test.

See [`agent.json`](agent.json) for the metadata template.
