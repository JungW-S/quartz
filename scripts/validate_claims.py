#!/usr/bin/env python3
"""Validate claim registry entries."""

from pathlib import Path
import sys

try:
    import yaml
except ImportError:
    print("Missing dependency: PyYAML. Install with: python -m pip install PyYAML", file=sys.stderr)
    sys.exit(2)


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FIELDS = {
    "id",
    "status",
    "level",
    "source",
    "source_location",
    "topic_pages",
    "statement",
    "paraphrase",
    "verified_by_user",
}
STATUSES = {"draft", "needs_source", "sourced", "verified", "deprecated"}
LEVELS = {"overview", "prerequisite", "core", "advanced", "reference"}
WIKI_INTERPRETATION_SOURCE = "wiki-interpretation"


def load_yaml(relative_path):
    path = ROOT / relative_path
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except FileNotFoundError:
        print(f"{relative_path}: file not found", file=sys.stderr)
        sys.exit(1)
    except yaml.YAMLError as exc:
        print(f"{relative_path}: invalid YAML: {exc}", file=sys.stderr)
        sys.exit(1)

    if not isinstance(data, dict):
        print(f"{relative_path}: expected a mapping at document root", file=sys.stderr)
        sys.exit(1)
    return data


def get_list(data, key, relative_path):
    items = data.get(key, [])
    if not isinstance(items, list):
        print(f"{relative_path}: {key!r} must be a list", file=sys.stderr)
        sys.exit(1)
    return items


def collect_ids(items):
    return {
        item["id"]
        for item in items
        if isinstance(item, dict) and isinstance(item.get("id"), str)
    }


def label(item, index):
    if isinstance(item, dict) and item.get("id"):
        return item["id"]
    return f"index {index}"


def validate_claim(claim, index, source_ids):
    if not isinstance(claim, dict):
        return [f"claims[{index}]: expected a mapping"]

    name = label(claim, index)
    errors = []

    for field in sorted(REQUIRED_FIELDS):
        if field not in claim:
            errors.append(f"claims[{index}] {name!r}: missing required field {field!r}")

    status = claim.get("status")
    if status is not None and status not in STATUSES:
        errors.append(f"claims[{index}] {name!r}: invalid status {status!r}")

    level = claim.get("level")
    if level is not None and level not in LEVELS:
        errors.append(f"claims[{index}] {name!r}: invalid level {level!r}")

    source = claim.get("source")
    if source is not None and source != WIKI_INTERPRETATION_SOURCE and source not in source_ids:
        errors.append(f"claims[{index}] {name!r}: unknown source {source!r}")

    topic_pages = claim.get("topic_pages")
    if topic_pages is not None:
        if not isinstance(topic_pages, list):
            errors.append(f"claims[{index}] {name!r}: topic_pages must be a list")
        else:
            for page in topic_pages:
                if not isinstance(page, str):
                    errors.append(f"claims[{index}] {name!r}: topic page {page!r} is not a string")
                elif not (ROOT / page).is_file():
                    errors.append(f"claims[{index}] {name!r}: topic page {page!r} does not exist")

    return errors


def main():
    claims_data = load_yaml("data/claims.yml")
    sources_data = load_yaml("data/sources.yml")

    claims = get_list(claims_data, "claims", "data/claims.yml")
    sources = get_list(sources_data, "sources", "data/sources.yml")
    source_ids = collect_ids(sources)

    errors = []
    for index, claim in enumerate(claims):
        errors.extend(validate_claim(claim, index, source_ids))

    if errors:
        print("Claim validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        sys.exit(1)

    print("Claim validation passed.")


if __name__ == "__main__":
    main()
