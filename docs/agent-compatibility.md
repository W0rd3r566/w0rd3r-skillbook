# Agent compatibility

W0rd3r Skillbook stores each skill once in the portable `SKILL.md` format and records where supported agents discover installed skills.

> **Important:** a known installation path is not proof that an agent loaded or followed a skill. This repository has not runtime-tested every listed agent.

## Compatibility status

| Status | Meaning |
|---|---|
| `documented` | Listed in the maintained Agent Skills installer directory with a documented target path. Runtime behavior is not tested here. |
| `installer-listed` | Listed by an installer, but this registry does not claim a verified native discovery path. |
| `adapter-required` | A dedicated adapter is needed. |
| `experimental` | Exploratory support; manual verification is required. |

The `runtime_tested` field is deliberately `false` until a reproducible test is run against that agent and version.

## Agent directory

The machine-readable source is [`agents/registry.json`](../agents/registry.json). It records project and global paths, vendor, agent type, status, and source references.

| Agent | Project path | Global path | Status |
|---|---|---|---|
| Claude Code (`claude-code`) | `.claude/skills/` | `~/.claude/skills/` | `documented` |
| Codex (`codex`) | `.agents/skills/` | `~/.agents/skills/` | `documented` |
| Cursor (`cursor`) | `.agents/skills/` | `~/.cursor/skills/` | `documented` |
| GitHub Copilot (`github-copilot`) | `.agents/skills/` | `~/.copilot/skills/` | `documented` |
| Gemini CLI (`gemini-cli`) | `.agents/skills/` | `~/.gemini/skills/` | `documented` |
| Antigravity (`antigravity`) | `.agents/skills/` | `~/.gemini/antigravity/skills/` | `documented` |
| Antigravity CLI (`antigravity-cli`) | `.agents/skills/` | `~/.gemini/antigravity-cli/skills/` | `documented` |
| OpenCode (`opencode`) | `.opencode/skills/` | `~/.config/opencode/skills/` | `documented` |
| Goose (`goose`) | `.goose/skills/` | `~/.config/goose/skills/` | `documented` |
| Kimi Code CLI (`kimi-code-cli`) | `.agents/skills/` | `~/.agents/skills/` | `documented` |
| Qwen Code (`qwen-code`) | `.qwen/skills/` | `~/.qwen/skills/` | `documented` |
| Cline (`cline`) | `.agents/skills/` | `~/.agents/skills/` | `documented` |
| Roo Code (`roo-code`) | `.roo/skills/` | `~/.roo/skills/` | `documented` |
| Windsurf (`windsurf`) | `.windsurf/skills/` | `~/.codeium/windsurf/skills/` | `documented` |
| Junie (`junie`) | `.junie/skills/` | `~/.junie/skills/` | `documented` |
| Continue (`continue`) | `.continue/skills/` | `~/.continue/skills/` | `documented` |
| OpenHands (`openhands`) | `.agents/skills/` | `~/.openhands/agent/skills/` | `documented` |
| Amp (`amp`) | `.agents/skills/` | `~/.config/agents/skills/` | `documented` |
| Zed (`zed`) | `.agents/skills/` | `~/.agents/skills/` | `documented` |
| Augment Code (`augment`) | `.augment/skills/` | `~/.augment/skills/` | `documented` |
| IBM Bob (`ibm-bob`) | `.bob/skills/` | `~/.bob/skills/` | `documented` |
| CodeBuddy (`codebuddy`) | `.codebuddy/skills/` | `~/.codebuddy/skills/` | `documented` |
| Command Code (`command-code`) | `.commandcode/skills/` | `~/.commandcode/skills/` | `documented` |
| Cortex Code (`cortex-code`) | `.cortex/skills/` | `~/.snowflake/cortex/skills/` | `documented` |
| Crush (`crush`) | `.crush/skills/` | `~/.config/crush/skills/` | `documented` |
| Devin for Terminal (`devin`) | `.devin/skills/` | `~/.config/devin/skills/` | `documented` |
| Droid (`factory-droid`) | `.agents/skills/` | `~/.factory/skills/` | `documented` |
| Grok Build (`grok`) | `.grok/skills/` | `~/.grok/skills/` | `documented` |
| Kiro CLI (`kiro-cli`) | `.kiro/skills/` | `~/.kiro/skills/` | `documented` |
| Pi (`pi`) | `.agents/skills/` | `~/.agents/skills/` | `documented` |
| Replit (`replit`) | `.agents/skills/` | `~/.config/agents/skills/` | `documented` |
| Universal (`universal`) | `.agents/skills/` | `~/.config/agents/skills/` | `installer-listed` |
| Warp (`warp`) | `.agents/skills/` | `~/.agents/skills/` | `documented` |
| AiderDesk (`aider-desk`) | `.aider-desk/skills/` | `~/.aider-desk/skills/` | `documented` |
| OpenClaw (`openclaw`) | `skills/` | `~/.openclaw/skills/` | `documented` |
| Mistral Vibe (`mistral-vibe`) | Not verified | Not verified | `installer-listed` |

## Installing a skill

A skill is a directory containing `SKILL.md` and optional supporting files. Copy the skill directory into the target agent's documented skills directory. For example, a project-level install for Codex uses `.agents/skills/<skill-name>/`; Claude Code uses `.claude/skills/<skill-name>/`.

Some agents share a common `.agents/skills/` directory. Do not create duplicate copies unless the agent's documentation requires a separate location.

## Feature compatibility

This registry tracks **basic skill installation/discovery paths** only. It does not claim identical support for optional metadata, tool restrictions, hooks, sub-agent context, invocation syntax, or other vendor-specific extensions. Those capabilities must be documented and tested separately.

## Sources and update policy

- [Vercel Skills: supported agents and installation paths](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)
- [GitHub CLI: `gh skill install` and supported agents](https://cli.github.com/manual/gh_skill_install)

Paths can change between agent versions. Before changing a path, check the agent's own documentation and update the registry source reference. Do not mark an agent as runtime-tested without a repeatable test and recorded version.

## Adding an agent

1. Confirm the agent supports the Agent Skills format or document the adapter needed.
2. Find its official or maintained installation documentation.
3. Add a unique entry to `agents/registry.json`.
4. Set `runtime_tested` to `false` until a real test is completed.
5. Run `python scripts/validate_skills.py` and submit a pull request.
