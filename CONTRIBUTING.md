# Contributing

Thanks for improving W0rd3r Skillbook.

## A good skill

- Solves a recognizable, recurring task.
- Has a precise trigger in its description.
- Gives actionable steps, not generic advice.
- Includes verification and clear boundaries.
- Does not duplicate an existing skill.

## Required structure

```text
skills/<category>/<skill-name>/SKILL.md
```

Use lowercase kebab-case. The frontmatter `name` must match the folder name. Keep skills focused; add references or scripts only when they materially help.

## Writing checklist

1. Explain when the skill applies.
2. Inspect project context before recommending changes.
3. Give a practical workflow.
4. Explain how to verify results.
5. State safety boundaries and when to ask the user.
6. Never claim that tools ran if they did not.

## Validate

```bash
python -m pip install pyyaml
python scripts/validate_skills.py
```
