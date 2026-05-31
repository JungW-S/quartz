#!/usr/bin/env python3
"""Generate the global Mermaid topic graph from data/topics.yml and data/edges.yml."""

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
OUTPUT = ROOT / "content" / "maps" / "global-topic-graph.md"


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


def graph_lines(topics, edges):
    used_nodes = {}
    node_by_topic = {}
    title_by_topic = {}

    for topic in topics:
        if not isinstance(topic, dict) or "id" not in topic:
            continue
        topic_id = str(topic["id"])
        node_by_topic[topic_id] = node_id(topic_id, used_nodes)
        title_by_topic[topic_id] = str(topic.get("title") or topic_id)

    lines = ["flowchart TD"]

    for topic_id in sorted(node_by_topic):
        lines.append(f'  {node_by_topic[topic_id]}["{label(title_by_topic[topic_id])}"]')

    for edge in edges:
        if not isinstance(edge, dict):
            continue
        if edge.get("visible_in_graph") is False:
            continue

        source = edge.get("from")
        target = edge.get("to")
        if source not in node_by_topic or target not in node_by_topic:
            continue

        relation = label(edge.get("relation") or "related")
        lines.append(f"  {node_by_topic[source]} -->|{relation}| {node_by_topic[target]}")

    return lines


def render_page(lines):
    return f"""---
title: Global Topic Graph
---

# Global Topic Graph

```mermaid
{chr(10).join(lines)}
```
"""


def main():
    topics = load_yaml("data/topics.yml").get("topics", [])
    edges = load_yaml("data/edges.yml").get("edges", [])
    if not isinstance(topics, list):
        topics = []
    if not isinstance(edges, list):
        edges = []

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(render_page(graph_lines(topics, edges)), encoding="utf-8")
    print(f"Generated {OUTPUT.relative_to(ROOT).as_posix()}.")


if __name__ == "__main__":
    main()
