# Совместимость с AI-агентами

W0rd3r Skillbook хранит каждый навык в одном переносимом формате `SKILL.md` и ведёт реестр путей, по которым поддерживаемые агенты обнаруживают установленные навыки.

> **Важно:** известный путь установки не доказывает, что агент загрузил навык или следует ему. Репозиторий пока не проводил runtime-тесты каждого агента из списка.

## Статусы совместимости

| Статус | Значение |
|---|---|
| `documented` | Агент указан в поддерживаемом каталоге Agent Skills с документированным путём. Runtime-поведение здесь не тестировалось. |
| `installer-listed` | Агент указан в установщике, но реестр не утверждает, что нативное обнаружение проверено. |
| `adapter-required` | Нужен отдельный адаптер. |
| `experimental` | Экспериментальная поддержка, требуется ручная проверка. |

Поле `runtime_tested` намеренно равно `false`, пока не будет проведён воспроизводимый тест с конкретным агентом и его версией.

## Каталог агентов

Машиночитаемый источник: [`agents/registry.json`](../agents/registry.json). В нём указаны пути для проекта и пользователя, разработчик, тип агента, статус и источники.

| Агент | Путь проекта | Глобальный путь | Статус |
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
| Mistral Vibe (`mistral-vibe`) | Не подтверждён | Не подтверждён | `installer-listed` |

## Установка навыка

Навык представляет собой папку с файлом `SKILL.md` и необязательными вспомогательными материалами. Скопируй папку навыка в документированный каталог нужного агента. Например, для проекта в Codex используется `.agents/skills/<название-навыка>/`, а в Claude Code — `.claude/skills/<название-навыка>/`.

Некоторые агенты используют общий каталог `.agents/skills/`. Не создавай дополнительные копии без необходимости, указанной в документации агента.

## Совместимость функций

Реестр отслеживает только **базовую установку и обнаружение навыков**. Он не обещает одинаковую поддержку дополнительных полей метаданных, ограничений инструментов, хуков, контекста субагентов, синтаксиса вызова и других расширений конкретных поставщиков. Эти возможности нужно документировать и тестировать отдельно.

## Источники и обновления

- [Vercel Skills: поддерживаемые агенты и пути установки](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)
- [GitHub CLI: `gh skill install` и поддерживаемые агенты](https://cli.github.com/manual/gh_skill_install)

Пути могут меняться между версиями агентов. Перед обновлением пути проверяй документацию самого агента и обновляй ссылку на источник. Не отмечай агент как протестированный без повторяемого теста и зафиксированной версии.

## Как добавить агента

1. Подтверди поддержку Agent Skills или опиши необходимый адаптер.
2. Найди официальную или поддерживаемую документацию по установке.
3. Добавь уникальную запись в `agents/registry.json`.
4. Оставь `runtime_tested: false`, пока не проведён реальный тест.
5. Запусти `python scripts/validate_skills.py` и отправь Pull Request.
