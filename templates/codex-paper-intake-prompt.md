# Codex Paper Intake Prompt

이 prompt는 future Codex run에서 하나의 mathematical paper를 intake할 때 사용합니다. Workflow는 source-first이며, 이 wiki는 paper-summary archive가 아니라 topic-centered study wiki입니다.

## Required Inputs

- 실제 PDF 또는 user가 제공한 paper file.
- Optional BibTeX.
- Optional source ID. 없으면 짧은 lowercase hyphenated ID를 제안합니다.

## Operating Rules

- Paper를 authority로 다룹니다.
- 모든 extracted mathematical unit은 source location을 가져야 합니다.
- Source note는 provenance record이며 long summary가 아닙니다.
- Topic page는 concept-first로 유지합니다.
- Unsupported theorem statement, invented citation, invented theorem number를 만들지 않습니다.
- Template section을 채우기 위해 unsupported overview, setup/notation, definition, example, viewpoint, property, mechanism, connection, navigation, source note를 만들지 않습니다.
- Real example은 approved source location이 있을 때만 topic page에 넣습니다.
- Schematic example은 `구조 예시`로 표시하고 general mechanism만 설명합니다.
- Safe example이나 section content가 없으면 visible content를 만들지 말고 section body를 비워두거나 optional section을 생략한 뒤 `data/topic_maturity.yml`, `data/research_queue.yml`, `data/review_backlog.yml`, 또는 `reports/roadmap/next-actions.md`에 gap을 기록합니다.
- Category-level statement와 Grothendieck-ring-level statement를 섞지 않습니다.
- Uncertain item은 `<!-- NEEDS-HUMAN-REVIEW -->` 또는 intake report의 `NEEDS-HUMAN-REVIEW` 항목으로 남깁니다.

## Required Workflow

1. PDF를 `inbox/papers/` 또는 `content/assets/pdfs/`에 stage합니다.
2. BibTeX가 있으면 `inbox/bibtex/`에 원문을 보존합니다.
3. `content/sources/papers/` 아래 concise source note를 만듭니다.
4. `data/sources.yml`에 real source metadata를 추가합니다.
5. Definition, theorem-like statement, example, construction, notation candidate를 source location과 함께 추출합니다.
6. Reusable units만 `data/claims.yml`에 추가합니다.
7. Existing topic page에 claim을 연결하거나, 필요할 때만 새 topic shell을 만듭니다.
8. 확실한 관계만 `data/edges.yml`에 추가합니다.
9. `scripts/generate_mermaid_maps.py`를 실행합니다.
10. `python3 scripts/run_all_checks.py`를 실행합니다.
11. `reports/intake/<source-id>.md`를 작성합니다.
12. `templates/codex-next-action-planner-prompt.md`를 따라 `reports/roadmap/next-actions.md`를 업데이트합니다.
    - Exactly top 3 next actions만 제안합니다.
    - Intentionally unfilled components와 그 gap이 기록된 위치를 포함합니다.
    - New source download나 intake는 explicit user approval 전에는 수행하지 않습니다.
    - Existing-source expansion, new-source intake, topic-page polishing, graph cleanup, notation normalization, human-review task 중 하나로 분류합니다.

## Prohibitions

- Long paper summary를 쓰지 않습니다.
- Proof-audit page를 만들지 않습니다.
- Unsupported theorem statement를 만들지 않습니다.
- Missing section을 template 때문에 강제로 채우지 않습니다. 정확히 쓸 수 없는 section은 reader-facing prose로 설명하지 말고 비워둡니다.
- Source-backed real example이 없으면 real example을 만들지 않습니다.
- Analogy나 motivation을 theorem처럼 쓰지 않습니다.
- `NEEDS-HUMAN-REVIEW`를 YAML status 값으로 쓰지 않습니다.
- Candidate source를 imported source나 citation처럼 취급하지 않습니다.
