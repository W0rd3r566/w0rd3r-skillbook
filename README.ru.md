<div align="center">

<img src="assets/skillbook-mark.svg" width="112" alt="W0rd3r Skillbook">

# W0rd3r Skillbook

**Практическая библиотека навыков для ИИ-агентов разработки.**

[![Проверка](https://github.com/W0rd3r566/w0rd3r-skillbook/actions/workflows/validate.yml/badge.svg)](https://github.com/W0rd3r566/w0rd3r-skillbook/actions/workflows/validate.yml) [![MIT](https://img.shields.io/badge/license-MIT-8b83d7.svg)](LICENSE) [![Навыки](https://img.shields.io/badge/skills-25-718ebb.svg)](#каталог)

[English](README.md) · [Русский](README.ru.md)

</div>

---

W0rd3r Skillbook — коллекция практических рабочих процессов для Codex, Claude Code и других совместимых ИИ-агентов. Каждый навык объясняет, когда его применять, что изучить перед работой, как действовать и как проверить результат.

> Навыки задают инструкции, но не выдают разрешения, не гарантируют правильность и не заменяют проверку человеком.

## Быстрый старт

### Codex

```bash
mkdir -p ~/.agents/skills
cp -r skills/development/debugging ~/.agents/skills/
```

Для одного проекта: `.agents/skills/<название-навыка>/`.

### Claude Code

```bash
mkdir -p ~/.claude/skills
cp -r skills/development/debugging ~/.claude/skills/
```

Для одного проекта: `.claude/skills/<название-навыка>/`.

Формат SKILL.md общий, но пути обнаружения зависят от агента. Сверяйся с документацией своей версии. На Android можно просматривать папки на GitHub и скачивать файлы, а устанавливать их позже в подходящую среду.

## Каталог

| [`python-pro`](skills/development/python-pro/) | Write maintainable Python with idiomatic patterns, useful typing, and clear error handling. |
| [`typescript-pro`](skills/development/typescript-pro/) | Build robust TypeScript with strict types, clear module boundaries, and safe handling of untrusted data. |
| [`debugging`](skills/development/debugging/) | Find root causes through reproducible evidence instead of guessing, masking symptoms, or making unrelated changes. |
| [`code-review`](skills/development/code-review/) | Review changes for correctness, regressions, security, maintainability, and missing tests with actionable findings. |
| [`refactoring`](skills/development/refactoring/) | Improve code structure while preserving externally observable behavior and keeping changes reviewable. |
| [`testing`](skills/development/testing/) | Design focused automated tests for behavior, edge cases, and regressions without brittle implementation coupling. |
| [`anti-ai-slop`](skills/design/anti-ai-slop/) | Design distinctive, purposeful interfaces while avoiding generic AI-generated visual patterns and superficial polish. |
| [`ui-ux-design`](skills/design/ui-ux-design/) | Translate user needs into clear flows, layouts, interaction states, and accessible interface behavior. |
| [`frontend-development`](skills/design/frontend-development/) | Implement reliable, responsive frontend features that fit the existing framework and user experience. |
| [`design-system`](skills/design/design-system/) | Create consistent design tokens, reusable components, and usage guidance without overengineering. |
| [`accessibility`](skills/design/accessibility/) | Find and fix practical accessibility barriers in interfaces, content, and interactions. |
| [`system-architecture`](skills/engineering/system-architecture/) | Understand and evolve software architecture around explicit boundaries, constraints, and maintainable dependencies. |
| [`api-design`](skills/engineering/api-design/) | Design predictable, secure, versionable APIs with clear contracts, errors, and compatibility expectations. |
| [`database-design`](skills/engineering/database-design/) | Design reliable data models, constraints, indexes, and migrations with integrity and operational safety in mind. |
| [`linux-engineering`](skills/engineering/linux-engineering/) | Work safely with Linux applications, services, permissions, packaging, and system configuration. |
| [`docker-workflows`](skills/engineering/docker-workflows/) | Build reproducible, secure container workflows for development, testing, and deployment. |
| [`performance-engineering`](skills/engineering/performance-engineering/) | Diagnose and improve software performance using representative measurements, explicit budgets, and evidence-led optimization. |
| [`github-actions`](skills/devops/github-actions/) | Create maintainable GitHub Actions workflows with least privilege, reliable triggers, and useful feedback. |
| [`git-workflow`](skills/devops/git-workflow/) | Use clear, safe Git operations for focused changes, collaboration, and reviewable history. |
| [`release-manager`](skills/devops/release-manager/) | Prepare predictable software releases with verified artifacts, clear notes, and rollback awareness. |
| [`documentation`](skills/devops/documentation/) | Write accurate, navigable documentation that helps users and contributors complete real tasks. |
| [`agent-orchestration`](skills/ai-agents/agent-orchestration/) | Delegate multi-part work to specialized agents with bounded scope, clear interfaces, and integration checks. |
| [`mcp-development`](skills/ai-agents/mcp-development/) | Design MCP servers and clients with explicit schemas, safe tool boundaries, and useful errors. |
| [`prompt-engineering`](skills/ai-agents/prompt-engineering/) | Write clear, testable instructions for language models and agents with explicit goals, constraints, and output expectations. |
| [`security-audit`](skills/ai-agents/security-audit/) | Review application code and configuration for realistic security weaknesses and prioritize actionable remediation. |

## Формат навыка

Каждый навык содержит YAML-поля `name` и `description`, а также разделы «Когда применять», «Рабочий процесс», «Проверка» и «Ограничения». Дополнительные файлы добавляются только при необходимости.

## Принципы качества

- Узкая задача: один навык решает один узнаваемый класс задач.
- Практичность: конкретные действия вместо общих пожеланий.
- Проверяемость: проверки и ограничения указаны явно.
- Безопасность: сначала изучение, подтверждение перед разрушительными действиями.
- Честность: нельзя заявлять о проверке, которая не запускалась.
- Переносимость: минимум ненужной привязки к одному поставщику.

## Проверка

Нужны Python 3.10+ и PyYAML:

```bash
python -m pip install pyyaml
python scripts/validate_skills.py
```

## Участие в проекте

Правила добавления навыков описаны в [CONTRIBUTING.md](CONTRIBUTING.md).

## Лицензия

MIT. Подробности в [LICENSE](LICENSE).
