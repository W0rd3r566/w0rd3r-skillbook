#!/usr/bin/env python3
"""Validate SKILL.md metadata and required sections without executing skill content."""
from __future__ import annotations
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML is required: python -m pip install pyyaml", file=sys.stderr)
    raise SystemExit(2)

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REQUIRED = ("## Use this skill when", "## Workflow", "## Verification", "## Boundaries")

def main() -> int:
    errors: list[str] = []
    seen: dict[str, Path] = {}
    paths = sorted(SKILLS.glob("**/SKILL.md"))
    if not paths:
        errors.append("No SKILL.md files found under skills/")
    for path in paths:
        raw = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT)
        if not raw.startswith("---") or raw.splitlines()[0] != "---":
            errors.append(f"{rel}: missing YAML frontmatter opener")
            continue
        parts = raw.split("---", 2)
        if len(parts) != 3:
            errors.append(f"{rel}: unterminated YAML frontmatter")
            continue
        try:
            meta = yaml.safe_load(parts[1]) or {}
        except yaml.YAMLError as exc:
            errors.append(f"{rel}: invalid YAML: {exc}")
            continue
        name, description = meta.get("name"), meta.get("description")
        if not isinstance(name, str) or not NAME_RE.fullmatch(name):
            errors.append(f"{rel}: name must be lowercase kebab-case")
        else:
            if name in seen:
                errors.append(f"{rel}: duplicate name {name!r} (also {seen[name]})")
            seen[name] = rel
            if path.parent.name != name:
                errors.append(f"{rel}: folder name must match frontmatter name {name!r}")
        if not isinstance(description, str) or len(description.strip()) < 40:
            errors.append(f"{rel}: description must contain at least 40 characters")
        body = parts[2]
        for section in REQUIRED:
            if section not in body:
                errors.append(f"{rel}: missing section {section}")
        if len(body.strip()) < 300:
            errors.append(f"{rel}: body is too short (<300 characters)")
    print(f"Found {len(paths)} SKILL.md files.")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("All skills passed structural and basic quality checks.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
