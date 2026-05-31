# Codex Topic Update Prompt

이 prompt는 already extracted source-backed material로 topic page를 업데이트할 때 사용합니다.

## Goal

Topic page를 concept-first로 개선합니다. Paper summary를 topic page로 옮기지 않습니다.

## Required Context

- Affected topic page.
- `data/topics.yml`
- Relevant entries in `data/claims.yml`, `data/sources.yml`, and `data/edges.yml`
- 필요한 경우 source note.

## Update Rules

- Topic page는 짧고 읽기 쉽게 유지합니다.
- Source-backed claim이나 source note에 근거한 내용만 추가합니다.
- Claim ID 또는 source note link로 provenance를 표시합니다.
- Category-level과 Grothendieck-ring-level wording을 분리합니다.
- Uncertain material은 `<!-- NEEDS-HUMAN-REVIEW -->`로 남깁니다.
- Local Mermaid map은 navigation 목적일 때만 업데이트합니다.

## Avoid

- Long source-by-source summary.
- Source table dump.
- Unsupported theorem statement.
- Invented theorem numbering.
- Analogy를 theorem으로 바꾸는 문장.

## Checks

```zsh
python3 scripts/run_all_checks.py
```
