#!/usr/bin/env python3
"""Validate topic graph edge registry entries."""

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
    "from",
    "to",
    "relation",
    "level",
    "source",
    "confidence",
    "visible_in_graph",
    "verified_by_user",
}
RELATIONS = {
    "child_of",
    "construction_inside",
    "context_for",
    "depends_on",
    "example_of",
    "generalizes",
    "motivates",
    "parent_of",
    "prerequisite_for",
    "cites",
    "supports",
    "states",
    "proves",
    "mentions",
    "related",
    "specializes",
    "specializes_to",
}
CONFIDENCES = {"low", "medium", "high"}


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


def collect_topic_ids(topics):
    return {
        item["id"]
        for item in topics
        if isinstance(item, dict) and isinstance(item.get("id"), str)
    }


def label(item, index):
    if isinstance(item, dict) and item.get("id"):
        return item["id"]
    return f"index {index}"


def validate_edge(edge, index, topic_ids):
    if not isinstance(edge, dict):
        return [f"edges[{index}]: expected a mapping"]

    name = label(edge, index)
    errors = []

    for field in sorted(REQUIRED_FIELDS):
        if field not in edge:
            errors.append(f"edges[{index}] {name!r}: missing required field {field!r}")

    relation = edge.get("relation")
    if relation is not None and relation not in RELATIONS:
        errors.append(f"edges[{index}] {name!r}: invalid relation {relation!r}")

    confidence = edge.get("confidence")
    if confidence is not None and confidence not in CONFIDENCES:
        errors.append(f"edges[{index}] {name!r}: invalid confidence {confidence!r}")

    for field in ("from", "to"):
        topic_id = edge.get(field)
        if topic_id is not None and topic_id not in topic_ids:
            errors.append(f"edges[{index}] {name!r}: {field!r} topic {topic_id!r} does not exist")

    return errors


def main():
    edges_data = load_yaml("data/edges.yml")
    topics_data = load_yaml("data/topics.yml")

    edges = get_list(edges_data, "edges", "data/edges.yml")
    topics = get_list(topics_data, "topics", "data/topics.yml")
    topic_ids = collect_topic_ids(topics)

    errors = []
    for index, edge in enumerate(edges):
        errors.extend(validate_edge(edge, index, topic_ids))

    if errors:
        print("Edge validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        sys.exit(1)

    print("Edge validation passed.")


if __name__ == "__main__":
    main()
