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
- Template section을 채우기 위해 unsupported material을 만들지 않습니다.
- 이 규칙은 `개요`, `준비와 notation`, `정의` or its variants, `기본 예시`, `핵심 관점`, `기본 성질`, `성질이 작동하는 방식`, `다른 topic들과의 관계`, `더 읽을 topic`, and `Source notes` 모두에 적용됩니다.
- Missing overview, setup/notation, definition, example, viewpoint, property, mechanism, connection, navigation, or source note content는 topic page에서 꾸며내지 말고 section body를 비워두거나 optional section을 생략한 뒤 workflow metadata에 기록합니다.
- `정의`, `구성`, `정리의 진술`, or `map의 정의`를 수정할 때는 ambient setting, input data, output object, and required conditions/relations/maps/universal property를 source-backed 범위 안에서 명료하게 적습니다.
- Source가 complete definition을 뒷받침하지 않으면 visible definition을 과장하지 말고 정의 section body를 비워두며 `definition` gap으로 기록합니다.
- Real example은 approved source location이 필요합니다. Schematic example은 `구조 예시`로 표시하고 general mechanism만 설명합니다.
- Main exposition에는 claim ID를 쓰지 않습니다. Provenance는 final `Source notes` section이나 YAML/source-note metadata에 짧게 표시합니다.
- Category-level과 Grothendieck-ring-level wording을 분리합니다.
- Uncertain material은 `<!-- NEEDS-HUMAN-REVIEW -->`로 남깁니다.
- Local Mermaid map은 navigation 목적일 때만 업데이트합니다.

## Avoid

- Long source-by-source summary.
- Source table dump.
- Unsupported theorem statement.
- Invented theorem numbering.
- Forced template completion.
- Placeholder prose in empty sections.
- Unsupported real examples.
- Analogy를 theorem으로 바꾸는 문장.

## Checks

```zsh
python3 scripts/run_all_checks.py
```
