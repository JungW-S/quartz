#!/usr/bin/env python3
"""Generate the public topic readiness dashboard."""

from pathlib import Path
import sys

try:
    import yaml
except ImportError:
    print("Missing dependency: PyYAML. Install with: python -m pip install PyYAML", file=sys.stderr)
    sys.exit(2)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "content" / "maps" / "topic-status.md"
STATUSES = {
    "publishable": "게시가능",
    "incomplete": "미완성",
}
COMPONENT_LABELS = {
    "definition": "정의",
    "setup and notation": "준비와 notation",
    "basic picture": "핵심 관점",
    "example": "기본 예시",
    "main facts": "기본 성질",
    "source notes": "Source notes",
    "connections": "관계 설명",
    "missing prerequisite page": "선행 topic page",
}


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


def wiki_link(topic):
    page = str(topic.get("page") or "")
    title = str(topic.get("title") or topic.get("id"))
    if page.startswith("content/") and page.endswith(".md"):
        target = page[len("content/") : -len(".md")]
        return f"[[{target}|{title}]]"
    return title


def inferred_status(maturity, missing):
    if maturity in {"study-ready", "reviewed"} and not missing:
        return "publishable"
    if maturity in {"definition-ready", "example-ready"} and not missing:
        return "publishable"
    return "incomplete"


def component_list(items):
    if not items:
        return "없음"
    return ", ".join(COMPONENT_LABELS.get(str(item), str(item)) for item in items)


def render(topics, maturity_by_id):
    counts = {"publishable": 0, "incomplete": 0}
    grouped = {"publishable": [], "incomplete": []}

    for topic in topics:
        topic_id = topic.get("id")
        maturity = maturity_by_id.get(topic_id, {})
        missing = maturity.get("missing_components") or []
        blockers = maturity.get("blocking_components")
        if blockers is None:
            blockers = missing

        status = maturity.get("publication_status") or inferred_status(topic.get("maturity"), missing)
        if status not in STATUSES:
            print(f"data/topic_maturity.yml: invalid publication_status {status!r} for {topic_id}", file=sys.stderr)
            sys.exit(1)

        counts[status] += 1
        note = maturity.get("publication_note")
        if not note:
            note = "핵심 학습 흐름에 사용할 수 있습니다." if status == "publishable" else "채워야 할 구성요소가 남아 있습니다."

        grouped[status].append(
            {
                "link": wiki_link(topic),
                "maturity": topic.get("maturity", ""),
                "blockers": component_list(blockers),
                "note": note,
                "next_review": maturity.get("next_review") or "",
            }
        )

    def render_group(status):
        entries = []
        for item in grouped[status]:
            entries.extend(
                [
                    f"### {item['link']}",
                    "",
                    f"- Maturity: {item['maturity']}",
                    f"- 막는 구성: {item['blockers']}",
                    f"- 평가: {item['note']}",
                    f"- 다음 검토: {item['next_review'] or '기록 없음'}",
                    "",
                ]
            )
        return "\n".join(entries).rstrip()

    return f"""---
title: Topic Status
---

이 페이지는 topic page 본문과 분리된 공개 readiness dashboard이다. Topic 본문은 계속 수학 공부 글로 유지하고, 미완성 여부와 다음 검토 정보는 이 페이지에서 확인한다.

## Summary

- 게시가능: {counts["publishable"]}
- 미완성: {counts["incomplete"]}

## 게시가능

{render_group("publishable")}

## 미완성

{render_group("incomplete")}
"""


def main():
    topics = load_yaml("data/topics.yml").get("topics", [])
    maturity_items = load_yaml("data/topic_maturity.yml").get("topic_maturity", [])
    if not isinstance(topics, list):
        print("data/topics.yml: 'topics' must be a list", file=sys.stderr)
        sys.exit(1)
    if not isinstance(maturity_items, list):
        print("data/topic_maturity.yml: 'topic_maturity' must be a list", file=sys.stderr)
        sys.exit(1)

    maturity_by_id = {
        str(item.get("topic_id")): item
        for item in maturity_items
        if isinstance(item, dict) and item.get("topic_id")
    }
    OUTPUT.write_text(render(topics, maturity_by_id), encoding="utf-8")
    print(f"Generated {OUTPUT.relative_to(ROOT).as_posix()}.")


if __name__ == "__main__":
    main()
