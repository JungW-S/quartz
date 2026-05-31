#!/usr/bin/env python3
"""Validate basic Obsidian wikilinks in content Markdown."""

from collections import defaultdict
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
WIKILINK_RE = re.compile(r"!?\[\[([^\]\n]+)\]\]")


def display(path):
    return path.relative_to(ROOT).as_posix()


def is_escaped(text, index):
    count = 0
    cursor = index - 1
    while cursor >= 0 and text[cursor] == "\\":
        count += 1
        cursor -= 1
    return count % 2 == 1


def split_unescaped(text, delimiter):
    for index, char in enumerate(text):
        if char == delimiter and not is_escaped(text, index):
            return text[:index], text[index + 1 :]
    return text, ""


def clean_target(raw_target):
    before_alias, _alias = split_unescaped(raw_target.strip(), "|")
    before_heading, _heading = split_unescaped(before_alias.strip(), "#")
    return before_heading.strip().replace(r"\|", "|").replace(r"\#", "#")


def normalize_target(target):
    target = target.replace("\\", "/").strip().lstrip("/")
    if target.startswith("content/"):
        target = target[len("content/") :]
    return target


def is_external(target):
    return re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", target) is not None


def is_asset(target):
    suffix = Path(target).suffix.lower()
    return bool(suffix and suffix != ".md")


def build_indexes(markdown_paths):
    relative_paths = {path.relative_to(CONTENT).as_posix() for path in markdown_paths}
    by_stem = defaultdict(list)
    for relative_path in sorted(relative_paths):
        by_stem[Path(relative_path).stem].append(relative_path)
    return relative_paths, by_stem


def resolve(target, relative_paths, by_stem):
    normalized = normalize_target(target)
    if not normalized:
        return "skip", []

    candidates = [normalized]
    if not normalized.endswith(".md"):
        candidates.append(f"{normalized}.md")
    candidates.append(f"{normalized.rstrip('/')}/index.md")

    for candidate in candidates:
        if candidate in relative_paths:
            return "resolved", [candidate]

    stem = Path(normalized).stem if normalized.endswith(".md") else Path(normalized).name
    stem_matches = by_stem.get(stem, [])
    if len(stem_matches) == 1:
        return "resolved", stem_matches
    if len(stem_matches) > 1:
        return "ambiguous", stem_matches
    return "unresolved", []


def validate_file(path, relative_paths, by_stem):
    errors = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        for match in WIKILINK_RE.finditer(line):
            target = clean_target(match.group(1))
            if target.startswith("^") or is_external(target) or is_asset(target):
                continue

            status, matches = resolve(target, relative_paths, by_stem)
            if status == "unresolved":
                errors.append(f"{display(path)}:{line_number}: unresolved wikilink {match.group(0)}")
            elif status == "ambiguous":
                errors.append(
                    f"{display(path)}:{line_number}: ambiguous wikilink {match.group(0)}; "
                    f"candidates: {', '.join(matches)}"
                )
    return errors


def main():
    markdown_paths = sorted(CONTENT.rglob("*.md"))
    relative_paths, by_stem = build_indexes(markdown_paths)

    errors = []
    for path in markdown_paths:
        errors.extend(validate_file(path, relative_paths, by_stem))

    if errors:
        print("Link validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        sys.exit(1)

    print("Link validation passed.")


if __name__ == "__main__":
    main()
