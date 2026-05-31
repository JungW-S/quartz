#!/usr/bin/env python3
"""Validate topic registry hierarchy metadata."""

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
    "title",
    "level",
    "topic_kind",
    "page",
    "summary",
    "parent_topics",
    "prerequisite_topics",
    "child_topics",
    "related_topics",
    "maturity",
}
LEVELS = {"overview", "prerequisite", "core", "advanced", "reference"}
TOPIC_KINDS = {
    "root",
    "area",
    "concept",
    "construction",
    "theorem",
    "map",
    "operation",
    "category",
    "algebra",
    "basis",
    "object-family",
    "example",
    "provisional",
}
MATURITIES = {
    "stub",
    "orientation",
    "definition-ready",
    "example-ready",
    "study-ready",
    "reviewed",
}
LIST_FIELDS = ("parent_topics", "prerequisite_topics", "child_topics", "related_topics")
FRONTMATTER_FIELDS = ("topic_kind", "parent_topics", "prerequisite_topics", "child_topics", "related_topics", "maturity")
NO_PARENT_KINDS = {"root", "provisional"}


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


def get_topics(data):
    topics = data.get("topics", [])
    if not isinstance(topics, list):
        print("data/topics.yml: 'topics' must be a list", file=sys.stderr)
        sys.exit(1)
    return topics


def label(topic, index):
    if isinstance(topic, dict) and topic.get("id"):
        return topic["id"]
    return f"index {index}"


def find_cycle(edges):
    graph = {}
    for source, target in edges:
        graph.setdefault(source, set()).add(target)
        graph.setdefault(target, set())

    visiting = set()
    visited = set()
    stack = []

    def visit(node):
        if node in visiting:
            start = stack.index(node)
            return stack[start:] + [node]
        if node in visited:
            return None

        visiting.add(node)
        stack.append(node)
        for next_node in sorted(graph.get(node, ())):
            cycle = visit(next_node)
            if cycle:
                return cycle
        stack.pop()
        visiting.remove(node)
        visited.add(node)
        return None

    for node in sorted(graph):
        cycle = visit(node)
        if cycle:
            return cycle
    return None


def read_frontmatter(path):
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        return None, [f"{path.relative_to(ROOT).as_posix()}: cannot read frontmatter: {exc}"]

    if not lines or lines[0].strip() != "---":
        return None, [f"{path.relative_to(ROOT).as_posix()}: missing YAML frontmatter"]

    end = None
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end = index
            break

    if end is None:
        return None, [f"{path.relative_to(ROOT).as_posix()}: missing closing frontmatter delimiter"]

    try:
        data = yaml.safe_load("\n".join(lines[1:end])) or {}
    except yaml.YAMLError as exc:
        return None, [f"{path.relative_to(ROOT).as_posix()}: invalid YAML frontmatter: {exc}"]

    if not isinstance(data, dict):
        return None, [f"{path.relative_to(ROOT).as_posix()}: frontmatter must be a mapping"]

    return data, []


def validate_topic_shape(topic, index, seen_ids):
    if not isinstance(topic, dict):
        return [f"topics[{index}]: expected a mapping"]

    name = label(topic, index)
    errors = []

    for field in sorted(REQUIRED_FIELDS):
        if field not in topic:
            errors.append(f"topics[{index}] {name!r}: missing required field {field!r}")

    topic_id = topic.get("id")
    if isinstance(topic_id, str):
        if topic_id in seen_ids:
            errors.append(f"topics[{index}] {name!r}: duplicate topic id {topic_id!r}")
        seen_ids.add(topic_id)
    elif topic_id is not None:
        errors.append(f"topics[{index}] {name!r}: id must be a string")

    level = topic.get("level")
    if level is not None and level not in LEVELS:
        errors.append(f"topics[{index}] {name!r}: invalid level {level!r}")

    topic_kind = topic.get("topic_kind")
    if topic_kind is not None and topic_kind not in TOPIC_KINDS:
        errors.append(f"topics[{index}] {name!r}: invalid topic_kind {topic_kind!r}")

    maturity = topic.get("maturity")
    if maturity is not None and maturity not in MATURITIES:
        errors.append(f"topics[{index}] {name!r}: invalid maturity {maturity!r}")

    page = topic.get("page")
    if page is not None:
        if not isinstance(page, str):
            errors.append(f"topics[{index}] {name!r}: page must be a string")
        elif not (ROOT / page).is_file():
            errors.append(f"topics[{index}] {name!r}: page {page!r} does not exist")
        else:
            frontmatter, frontmatter_errors = read_frontmatter(ROOT / page)
            errors.extend(frontmatter_errors)
            if frontmatter is not None:
                for field in FRONTMATTER_FIELDS:
                    if field not in frontmatter:
                        errors.append(f"topics[{index}] {name!r}: page frontmatter missing {field!r}")
                    elif frontmatter[field] != topic.get(field):
                        errors.append(
                            f"topics[{index}] {name!r}: page frontmatter {field!r} does not match data/topics.yml"
                        )

    for field in LIST_FIELDS:
        values = topic.get(field)
        if values is None:
            continue
        if not isinstance(values, list):
            errors.append(f"topics[{index}] {name!r}: {field} must be a list")
            continue
        if len(values) != len(set(values)):
            errors.append(f"topics[{index}] {name!r}: {field} contains duplicate entries")
        for value in values:
            if not isinstance(value, str):
                errors.append(f"topics[{index}] {name!r}: {field} entry {value!r} is not a string")
            elif value == topic_id:
                errors.append(f"topics[{index}] {name!r}: {field} cannot reference itself")

    return errors


def validate_topic_refs(topics_by_id):
    errors = []

    for topic_id, topic in topics_by_id.items():
        topic_kind = topic.get("topic_kind")
        parents = topic.get("parent_topics", [])
        prerequisites = topic.get("prerequisite_topics", [])
        children = topic.get("child_topics", [])
        related = topic.get("related_topics", [])

        if topic_kind not in NO_PARENT_KINDS and not parents:
            errors.append(f"{topic_id!r}: non-root topic must list at least one parent topic")

        if topic_kind not in NO_PARENT_KINDS and not any((parents, prerequisites, children, related)):
            errors.append(f"{topic_id!r}: orphan topic has no hierarchy or related-topic links")

        for field in LIST_FIELDS:
            for ref in topic.get(field, []):
                if ref not in topics_by_id:
                    errors.append(f"{topic_id!r}: {field} references unknown topic {ref!r}")

    for topic_id, topic in topics_by_id.items():
        for parent_id in topic.get("parent_topics", []):
            if parent_id in topics_by_id and topic_id not in topics_by_id[parent_id].get("child_topics", []):
                errors.append(
                    f"{topic_id!r}: parent topic {parent_id!r} does not list {topic_id!r} in child_topics"
                )

        for child_id in topic.get("child_topics", []):
            if child_id in topics_by_id and topic_id not in topics_by_id[child_id].get("parent_topics", []):
                errors.append(
                    f"{topic_id!r}: child topic {child_id!r} does not list {topic_id!r} in parent_topics"
                )

    parent_edges = set()
    prerequisite_edges = set()
    for topic_id, topic in topics_by_id.items():
        for parent_id in topic.get("parent_topics", []):
            if parent_id in topics_by_id:
                parent_edges.add((parent_id, topic_id))
        for child_id in topic.get("child_topics", []):
            if child_id in topics_by_id:
                parent_edges.add((topic_id, child_id))
        for prerequisite_id in topic.get("prerequisite_topics", []):
            if prerequisite_id in topics_by_id:
                prerequisite_edges.add((prerequisite_id, topic_id))

    parent_cycle = find_cycle(parent_edges)
    if parent_cycle:
        errors.append(f"parent/child hierarchy contains a cycle: {' -> '.join(parent_cycle)}")

    prerequisite_cycle = find_cycle(prerequisite_edges)
    if prerequisite_cycle:
        errors.append(f"prerequisite hierarchy contains a cycle: {' -> '.join(prerequisite_cycle)}")

    return errors


def main():
    topics_data = load_yaml("data/topics.yml")
    topics = get_topics(topics_data)

    errors = []
    seen_ids = set()
    for index, topic in enumerate(topics):
        errors.extend(validate_topic_shape(topic, index, seen_ids))

    topics_by_id = {
        topic["id"]: topic
        for topic in topics
        if isinstance(topic, dict) and isinstance(topic.get("id"), str)
    }
    errors.extend(validate_topic_refs(topics_by_id))

    if errors:
        print("Topic validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        sys.exit(1)

    print("Topic validation passed.")


if __name__ == "__main__":
    main()
