# Source Extraction Checklist

Paper intake 이후 human review에 사용할 checklist입니다.

## Source Metadata

- [ ] Real source만 등록했습니다.
- [ ] Source ID가 lowercase hyphenated format입니다.
- [ ] `data/sources.yml` entry와 source note ID가 일치합니다.
- [ ] Bibliographic fields가 paper 또는 supplied BibTeX와 일치합니다.
- [ ] Missing metadata는 intake report에 기록했습니다.

## Source Note

- [ ] `content/sources/papers/` 아래에 있습니다.
- [ ] Frontmatter에 `id`, `title`, `source_type`이 있습니다.
- [ ] Source note는 long summary가 아닙니다.
- [ ] Extracted unit마다 source location이 있습니다.
- [ ] Uncertain item은 `<!-- NEEDS-HUMAN-REVIEW -->` 또는 report에 기록했습니다.

## Claims

- [ ] Unsupported theorem statement가 없습니다.
- [ ] Invented theorem number가 없습니다.
- [ ] Statement와 paraphrase가 source보다 강하지 않습니다.
- [ ] `verified_by_user: false`를 기본값으로 유지했습니다.

## Topics

- [ ] Topic page는 concept-first입니다.
- [ ] Category-level과 Grothendieck-ring-level statement를 섞지 않았습니다.
- [ ] Notation과 terminology conflict는 glossary 또는 review item에 남겼습니다.

## Validation

- [ ] `python3 scripts/run_all_checks.py`가 통과했습니다.
- [ ] Build warning이나 failure를 intake report에 기록했습니다.
