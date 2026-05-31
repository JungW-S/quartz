#!/usr/bin/env python3
"""Validate required frontmatter on topic and source pages."""

from pathlib import Path
import sys

try:
    import yaml
except ImportError:
    print("Missing dependency: PyYAML. Install with: python -m pip install PyYAML", file=sys.stderr)
    sys.exit(2)


ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"

LEVELS = {"overview", "prerequisite", "core", "advanced", "reference"}
SOURCE_TYPES = {"book", "paper", "article", "lecture_notes", "video", "dataset", "software", "other"}


def display(path):
    return path.relative_to(ROOT).as_posix()


def should_skip(path):
    return path.name == "AGENTS.md"


def read_frontmatter(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return None, [f"{display(path)}: missing YAML frontmatter"]

    end = None
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end = index
            break

    if end is None:
        return None, [f"{display(path)}: missing closing frontmatter delimiter"]

    try:
        data = yaml.safe_load("\n".join(lines[1:end])) or {}
    except yaml.YAMLError as exc:
        return None, [f"{display(path)}: invalid YAML frontmatter: {exc}"]

    if not isinstance(data, dict):
        return None, [f"{display(path)}: frontmatter must be a mapping"]

    return data, []


def require_fields(path, frontmatter, fields):
    return [
        f"{display(path)}: missing required frontmatter field {field!r}"
        for field in fields
        if field not in frontmatter
    ]


def validate_topic(path):
    frontmatter, errors = read_frontmatter(path)
    if frontmatter is None:
        return errors

    errors.extend(require_fields(path, frontmatter, ("id", "title", "level")))
    level = frontmatter.get("level")
    if level is not None and level not in LEVELS:
        errors.append(f"{display(path)}: invalid level {level!r}")
    return errors


def validate_source(path):
    frontmatter, errors = read_frontmatter(path)
    if frontmatter is None:
        return errors

    errors.extend(require_fields(path, frontmatter, ("id", "title", "source_type")))
    source_type = frontmatter.get("source_type")
    if source_type is not None and source_type not in SOURCE_TYPES:
        errors.append(f"{display(path)}: invalid source_type {source_type!r}")
    return errors


def main():
    errors = []

    topic_dir = CONTENT / "topics"
    if topic_dir.exists():
        for path in sorted(topic_dir.rglob("*.md")):
            if not should_skip(path):
                errors.extend(validate_topic(path))

    source_dir = CONTENT / "sources"
    if source_dir.exists():
        for path in sorted(source_dir.rglob("*.md")):
            if not should_skip(path):
                errors.extend(validate_source(path))

    if errors:
        print("Frontmatter validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        sys.exit(1)

    print("Frontmatter validation passed.")


if __name__ == "__main__":
    main()
