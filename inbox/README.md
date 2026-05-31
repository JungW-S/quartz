# Intake Inbox

`inbox/`는 paper intake 전 raw input을 잠시 두는 staging area입니다. Canonical source note나 registry가 아닙니다.

## Folders

- `inbox/papers/`: user-supplied PDF staging.
- `inbox/bibtex/`: supplied BibTeX staging.
- `inbox/notes/`: temporary intake notes.

## Rules

- Inbox file만 보고 source-backed claim을 만들지 않습니다.
- BibTeX 원문은 가능한 보존합니다.
- Intake가 끝나면 source note, YAML registry, intake report에 provenance를 남깁니다.
- Long paper summary를 만들지 않습니다.
