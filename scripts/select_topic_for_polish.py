#!/usr/bin/env python3
"""Select the next topic for the `topic 수정` / `토픽수정` trigger."""

from pathlib import Path
import sys

try:
    import yaml
except ImportError:
    print("Missing dependency: PyYAML. Install with: python -m pip install PyYAML", file=sys.stderr)
    sys.exit(2)


ROOT = Path(__file__).resolve().parents[1]
TOPICS_PATH = ROOT / "data" / "topics.yml"
MATURITY_PATH = ROOT / "data" / "topic_maturity.yml"
POLISH_PATH = ROOT / "data" / "topic_polish_log.yml"

MATURITY_RANK = {
    "reviewed": 0,
    "study-ready": 1,
    "example-ready": 2,
    "definition-ready": 3,
    "orientation": 4,
    "stub": 5,
}


def load_yaml(path):
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except FileNotFoundError:
        return {}
    except yaml.YAMLError as exc:
        print(f"{path.relative_to(ROOT)}: invalid YAML: {exc}", file=sys.stderr)
        sys.exit(1)
    return data if isinstance(data, dict) else {}


def topic_has_visible_prose(topic):
    page = ROOT / str(topic.get("page") or "")
    try:
        text = page.read_text(encoding="utf-8")
    except FileNotFoundError:
        return False

    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            text = text[end + 5 :]

    return "## " in text and len(text.strip()) >= 500


def index_by(items, key):
    return {
        str(item.get(key)): item
        for item in items
        if isinstance(item, dict) and item.get(key)
    }


def polish_count(entry):
    try:
        return int(entry.get("polish_count") or 0)
    except (TypeError, ValueError):
        return 0


def main():
    topics = load_yaml(TOPICS_PATH).get("topics", [])
    maturity_items = load_yaml(MATURITY_PATH).get("topic_maturity", [])
    polish_items = load_yaml(POLISH_PATH).get("topic_polish", [])

    if not isinstance(topics, list):
        print("data/topics.yml: 'topics' must be a list", file=sys.stderr)
        sys.exit(1)
    if not isinstance(maturity_items, list):
        maturity_items = []
    if not isinstance(polish_items, list):
        polish_items = []

    maturity_by_id = index_by(maturity_items, "topic_id")
    polish_by_id = index_by(polish_items, "topic_id")

    candidates = []
    for topic in topics:
        topic_id = str(topic.get("id") or "")
        if not topic_id:
            continue
        if not topic_has_visible_prose(topic):
            continue

        maturity = maturity_by_id.get(topic_id, {})
        polish = polish_by_id.get(topic_id, {})
        publication_status = str(maturity.get("publication_status") or "incomplete")
        topic_maturity = str(topic.get("maturity") or maturity.get("maturity") or "stub")

        candidates.append(
            {
                "topic_id": topic_id,
                "title": topic.get("title") or topic_id,
                "page": topic.get("page") or "",
                "polish_count": polish_count(polish),
                "publication_status": publication_status,
                "maturity": topic_maturity,
                "next_review": maturity.get("next_review") or "",
            }
        )

    candidates.sort(
        key=lambda item: (
            item["polish_count"],
            0 if item["publication_status"] == "publishable" else 1,
            MATURITY_RANK.get(item["maturity"], 99),
            item["topic_id"],
        )
    )

    if not candidates:
        print("No topic with visible prose is available for a polish pass.")
        return

    chosen = candidates[0]
    print("Chosen topic for `topic 수정`:")
    print(f"- topic_id: {chosen['topic_id']}")
    print(f"- title: {chosen['title']}")
    print(f"- page: {chosen['page']}")
    print(f"- polish_count: {chosen['polish_count']}")
    print(f"- publication_status: {chosen['publication_status']}")
    print(f"- maturity: {chosen['maturity']}")
    if chosen["next_review"]:
        print(f"- next_review: {chosen['next_review']}")

    print("\nLowest-count alternatives:")
    for item in candidates[:5]:
        print(
            f"- {item['topic_id']} | count={item['polish_count']} | "
            f"{item['publication_status']} | {item['maturity']}"
        )


if __name__ == "__main__":
    main()
