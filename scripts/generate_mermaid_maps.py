#!/usr/bin/env python3
"""Generate Mermaid topic maps from data/topics.yml and data/edges.yml."""

from pathlib import Path
import hashlib
import re
import sys

try:
    import yaml
except ImportError:
    print("Missing dependency: PyYAML. Install with: python -m pip install PyYAML", file=sys.stderr)
    sys.exit(2)


ROOT = Path(__file__).resolve().parents[1]
MAP_DIR = ROOT / "content" / "maps"
MAPS = {
    "global-topic-graph.md": {
        "title": "Global Topic Graph",
        "mode": "edges",
        "topics": None,
    },
    "topic-hierarchy.md": {
        "title": "Topic Hierarchy",
        "mode": "hierarchy",
        "topics": None,
    },
    "representation-theory-map.md": {
        "title": "Representation Theory Map",
        "mode": "study",
        "topics": {
            "root-systems-and-weight-lattices",
            "universal-enveloping-algebras",
            "quantum-groups",
            "quantum-coordinate-rings",
            "dual-canonical-bases",
            "crystal-bases",
            "cellular-crystals",
            "localized-crystals",
            "quiver-hecke-algebras",
            "quiver-hecke-module-categories",
            "quiver-hecke-subcategories",
            "category-localization",
            "pro-categories",
            "quiver-hecke-category-localization",
            "determinantial-modules",
            "monoidal-categorification",
            "graded-monoidal-categories",
            "affine-objects-in-monoidal-categories",
            "r-matrix-renormalization",
            "normal-sequences",
            "quasi-rigid-monoidal-categories",
            "head-simplicity-of-convolutions",
            "shuffle-lemmas-for-quiver-hecke-modules",
            "demazure-subcategories-of-quiver-hecke-modules",
            "root-objects-in-localized-categories",
            "localized-root-operators",
            "crystal-comparison-map",
            "reverse-equivalence-of-localized-categories",
        },
    },
    "crystal-bases-map.md": {
        "title": "Crystal Bases Map",
        "mode": "study",
        "topics": {
            "root-systems-and-weight-lattices",
            "universal-enveloping-algebras",
            "quantum-groups",
            "crystal-bases",
            "cellular-crystals",
            "localized-crystals",
            "category-localization",
            "pro-categories",
            "quiver-hecke-subcategories",
            "quiver-hecke-category-localization",
            "graded-monoidal-categories",
            "affine-objects-in-monoidal-categories",
            "r-matrix-renormalization",
            "normal-sequences",
            "quasi-rigid-monoidal-categories",
            "demazure-subcategories-of-quiver-hecke-modules",
            "root-objects-in-localized-categories",
            "localized-root-operators",
            "crystal-comparison-map",
            "reverse-equivalence-of-localized-categories",
        },
    },
    "quiver-hecke-algebras-map.md": {
        "title": "Quiver-Hecke Algebras Map",
        "mode": "study",
        "topics": {
            "quiver-hecke-algebras",
            "quiver-hecke-module-categories",
            "quiver-hecke-subcategories",
            "category-localization",
            "quiver-hecke-category-localization",
            "determinantial-modules",
            "monoidal-categorification",
            "quantum-coordinate-rings",
            "localized-crystals",
            "graded-monoidal-categories",
            "affine-objects-in-monoidal-categories",
            "r-matrix-renormalization",
            "normal-sequences",
            "quasi-rigid-monoidal-categories",
            "head-simplicity-of-convolutions",
            "shuffle-lemmas-for-quiver-hecke-modules",
            "demazure-subcategories-of-quiver-hecke-modules",
            "root-objects-in-localized-categories",
            "localized-root-operators",
            "crystal-comparison-map",
            "reverse-equivalence-of-localized-categories",
        },
    },
}


def load_yaml(relative_path):
    path = ROOT / relative_path
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except FileNotFoundError:
        return {}
    except yaml.YAMLError as exc:
        print(f"{relative_path}: invalid YAML: {exc}", file=sys.stderr)
        sys.exit(1)
    return data if isinstance(data, dict) else {}


def node_id(raw_id, used):
    base = re.sub(r"[^A-Za-z0-9_]", "_", str(raw_id)).strip("_") or "topic"
    if not re.match(r"^[A-Za-z_]", base):
        base = f"topic_{base}"

    candidate = base
    if candidate in used and used[candidate] != raw_id:
        digest = hashlib.sha1(str(raw_id).encode("utf-8")).hexdigest()[:8]
        candidate = f"{base}_{digest}"
    used[candidate] = raw_id
    return candidate


def label(text):
    return str(text).replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ")


def topic_index(topics):
    return {
        str(topic["id"]): topic
        for topic in topics
        if isinstance(topic, dict) and isinstance(topic.get("id"), str)
    }


def scoped_topics(topics_by_id, scope):
    if scope is None:
        return topics_by_id
    return {topic_id: topics_by_id[topic_id] for topic_id in sorted(scope) if topic_id in topics_by_id}


def metadata_edges(topics_by_id, scope=None, include_related=False, include_prerequisites=False):
    scope_ids = set(topics_by_id) if scope is None else set(scope)
    edges = set()

    for topic_id, topic in topics_by_id.items():
        if topic_id not in scope_ids:
            continue

        for parent_id in topic.get("parent_topics", []):
            if parent_id in scope_ids:
                edges.add((parent_id, topic_id, "parent"))

        if include_prerequisites:
            for prerequisite_id in topic.get("prerequisite_topics", []):
                if prerequisite_id in scope_ids:
                    edges.add((prerequisite_id, topic_id, "prereq"))

        if include_related:
            for related_id in topic.get("related_topics", []):
                if related_id in scope_ids:
                    edges.add((topic_id, related_id, "related"))

    return edges


def registry_edges(edges, scope=None, relation_filter=None):
    scope_ids = None if scope is None else set(scope)
    rendered = set()

    for edge in edges:
        if not isinstance(edge, dict):
            continue
        if edge.get("visible_in_graph") is False:
            continue

        source = edge.get("from")
        target = edge.get("to")
        relation = str(edge.get("relation") or "related")
        if scope_ids is not None and (source not in scope_ids or target not in scope_ids):
            continue
        if relation_filter is not None and relation not in relation_filter:
            continue
        if source is None or target is None:
            continue

        rendered.add((source, target, relation))

    return rendered


def graph_lines(topics_by_id, edges):
    used_nodes = {}
    node_by_topic = {}
    title_by_topic = {}

    for topic_id in sorted(topics_by_id):
        topic = topics_by_id[topic_id]
        node_by_topic[topic_id] = node_id(topic_id, used_nodes)
        title_by_topic[topic_id] = str(topic.get("title") or topic_id)

    lines = ["flowchart TD"]

    for topic_id in sorted(node_by_topic):
        lines.append(f'  {node_by_topic[topic_id]}["{label(title_by_topic[topic_id])}"]')

    grouped_edges = {}
    for source, target, relation in edges:
        grouped_edges.setdefault((source, target), set()).add(relation)

    relation_order = {
        "parent": 0,
        "parent_of": 0,
        "prereq": 1,
        "prerequisite_for": 1,
        "context_for": 2,
        "construction_inside": 3,
        "motivates": 4,
        "generalizes": 5,
        "specializes_to": 6,
        "example_of": 7,
        "supports": 8,
        "depends_on": 9,
        "related": 10,
    }

    for (source, target), relations in sorted(grouped_edges.items()):
        if source not in node_by_topic or target not in node_by_topic:
            continue
        relation = "/".join(sorted(relations, key=lambda item: (relation_order.get(item, 99), item)))
        lines.append(f"  {node_by_topic[source]} -->|{label(relation)}| {node_by_topic[target]}")

    return lines


def topic_links(topics_by_id):
    links = []
    for topic_id in sorted(topics_by_id):
        topic = topics_by_id[topic_id]
        page = str(topic.get("page") or "")
        title = str(topic.get("title") or topic_id)
        if page.startswith("content/") and page.endswith(".md"):
            target = page[len("content/") : -len(".md")]
            links.append(f"- [[{target}|{title}]]")
        else:
            links.append(f"- {title}")
    return links


def edges_for_map(config, topics_by_id, edges):
    scope = config["topics"]
    mode = config["mode"]

    if mode == "edges":
        return registry_edges(edges, scope)
    if mode == "hierarchy":
        return metadata_edges(topics_by_id, scope)
    if mode == "study":
        return (
            metadata_edges(topics_by_id, scope, include_related=True, include_prerequisites=True)
            | registry_edges(
                edges,
                scope,
                relation_filter={
                    "context_for",
                    "motivates",
                    "construction_inside",
                    "specializes_to",
                    "generalizes",
                    "example_of",
                },
            )
        )

    raise ValueError(f"unknown map mode: {mode}")


def render_page(title, lines, topics_by_id):
    links = "\n".join(topic_links(topics_by_id))
    return f"""---
title: {title}
---

```mermaid
{chr(10).join(lines)}
```

## Topics

{links}
"""


def main():
    topics = load_yaml("data/topics.yml").get("topics", [])
    edges = load_yaml("data/edges.yml").get("edges", [])
    if not isinstance(topics, list):
        topics = []
    if not isinstance(edges, list):
        edges = []

    topics_by_id = topic_index(topics)
    MAP_DIR.mkdir(parents=True, exist_ok=True)

    for filename, config in MAPS.items():
        scoped = scoped_topics(topics_by_id, config["topics"])
        map_edges = edges_for_map(config, topics_by_id, edges)
        output = MAP_DIR / filename
        output.write_text(
            render_page(config["title"], graph_lines(scoped, map_edges), scoped),
            encoding="utf-8",
        )
        print(f"Generated {output.relative_to(ROOT).as_posix()}.")


if __name__ == "__main__":
    main()
