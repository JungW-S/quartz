# Topic Polish Trigger Prompt

이 prompt는 사용자가 `topic 수정` 또는 `토픽수정`이라고 말했을 때 실행한다. 이 trigger phrase는 정확히 한 topic page에 대한 reader-facing polish approval로 취급한다.

## Goal

수정횟수가 적은 topic 중 하나를 고르고, 문장과 구성이 실제로 개선될 수 있는지 판단한 뒤, 안전한 범위에서 topic page를 다듬는다.

## Selection

1. Run:

```zsh
python3 scripts/select_topic_for_polish.py
```

2. 선택 후보는 `data/topic_polish_log.yml`의 `polish_count`가 낮은 topic을 우선한다.
3. 같은 count 안에서는 visible prose가 있고, 새 source 없이 문장/구성 개선이 가능한 topic을 고른다.
4. Title-only stub, source-backed 정의가 부족한 topic, 새 source가 필요한 topic은 문장 polish 대상으로 삼지 말고 다음 후보를 고른다.

## Allowed Edits

- Korean prose clarity.
- Paragraph splitting, ordering, and transition cleanup.
- Removing duplicated explanation.
- Making hierarchy/navigation prose more reader-facing.
- Clarifying level distinctions already present in the page.
- Hiding empty visible sections when they interrupt reading.
- Updating `data/topic_polish_log.yml`.
- Updating `data/topic_maturity.yml` readability metadata if the polish affects readiness.
- Updating `reports/roadmap/next-actions.md`.

## Forbidden Edits

- Do not download or fetch sources.
- Do not add claims.
- Do not add definitions, theorem statements, examples, source notes, or mathematical facts not already supported by approved sources or user-approved exposition.
- Do not create new topic pages.
- Do not expand a page merely to fill the template.
- Do not expose maturity, review backlog, source-ingestion, or claim metadata in reader-facing prose.

## Required Workflow

1. Inspect the chosen topic page, `content/topics/STYLE_GUIDE.md`, the corresponding `data/topics.yml` entry, `data/topic_maturity.yml`, and `data/topic_polish_log.yml`.
2. Identify concrete polish candidates.
3. Judge whether each candidate is rational:
   - Does it improve undergraduate readability?
   - Does it preserve mathematical meaning?
   - Does it avoid adding unsupported material?
   - Does it improve the learning order or topic hierarchy?
4. Apply only rational edits.
5. Increment that topic's `polish_count` by 1 in `data/topic_polish_log.yml`.
6. Append a history item with date, changed file, and a short summary.
7. Run:

```zsh
git diff --check
python3 scripts/run_all_checks.py
npx quartz build
```

If standalone `npx quartz build` fails with the known Node heap out-of-memory issue while `run_all_checks.py` passes its internal Quartz build, report it as an environment-specific npx failure.

## Final Report

Report:

- selected topic,
- previous and new polish count,
- proposed fixes and why they were rational,
- actual files changed,
- validation result,
- build result,
- next recommended task.
