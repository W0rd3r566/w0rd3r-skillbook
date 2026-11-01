#!/usr/bin/env python3
"""Validate Skillbook skills and the agent compatibility registry."""
from __future__ import annotations
import json
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
REGISTRY = ROOT / "agents" / "registry.json"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REQUIRED = ("## Use this skill when", "## Workflow", "## Verification", "## Boundaries")
AGENT_STATUSES = {"documented", "installer-listed", "adapter-required", "experimental"}
AGENT_REQUIRED = ("id", "name", "vendor", "type", "status", "runtime_tested", "format")


def validate_skills(errors: list[str]) -> int:
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
    return len(paths)


def validate_registry(errors: list[str]) -> int:
    if not REGISTRY.exists():
        errors.append("Missing agents/registry.json")
        return 0
    try:
        data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        errors.append(f"agents/registry.json: invalid JSON: {exc}")
        return 0
    if data.get("schema_version") != "1.0.0":
        errors.append("agents/registry.json: schema_version must be 1.0.0")
    agents = data.get("agents")
    if not isinstance(agents, list) or not agents:
        errors.append("agents/registry.json: agents must be a non-empty array")
        return 0
    seen: set[str] = set()
    for index, agent in enumerate(agents):
        label = f"agents/registry.json: agents[{index}]"
        if not isinstance(agent, dict):
            errors.append(f"{label} must be an object")
            continue
        for key in AGENT_REQUIRED:
            if key not in agent:
                errors.append(f"{label} missing {key}")
        agent_id = agent.get("id")
        if not isinstance(agent_id, str) or not NAME_RE.fullmatch(agent_id):
            errors.append(f"{label}: id must be lowercase kebab-case")
        elif agent_id in seen:
            errors.append(f"{label}: duplicate id {agent_id!r}")
        else:
            seen.add(agent_id)
        if agent.get("status") not in AGENT_STATUSES:
            errors.append(f"{label}: unsupported status {agent.get('status')!r}")
        if not isinstance(agent.get("runtime_tested"), bool):
            errors.append(f"{label}: runtime_tested must be boolean")
        for key in ("project_path", "global_path"):
            value = agent.get(key)
            if value is not None and (not isinstance(value, str) or not value.endswith("/")):
                errors.append(f"{label}: {key} must be null or a directory path ending in '/'")
        source_ids = agent.get("source_ids")
        if not isinstance(source_ids, list) or not source_ids:
            errors.append(f"{label}: source_ids must be a non-empty array")
    print(f"Found {len(agents)} agent registry entries.")
    return len(agents)


def main() -> int:
    errors: list[str] = []
    skill_count = validate_skills(errors)
    agent_count = validate_registry(errors)
    metadata_path = ROOT / "skillbook.json"
    if metadata_path.exists():
        try:
            metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
            if metadata.get("skills_count") != skill_count:
                errors.append(f"skillbook.json: skills_count is {metadata.get('skills_count')}, found {skill_count}")
            if metadata.get("agents_count") != agent_count:
                errors.append(f"skillbook.json: agents_count is {metadata.get('agents_count')}, found {agent_count}")
        except (json.JSONDecodeError, OSError) as exc:
            errors.append(f"skillbook.json: invalid JSON: {exc}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("All skills and agent registry entries passed structural checks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
