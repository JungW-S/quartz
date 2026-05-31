# Intake Reports

Intake report는 workflow record입니다. Paper summary가 아닙니다.

## Location

```text
reports/intake/<source-id>.md
```

## Required Sections

- Source metadata
- Files touched
- Extracted items summary
- Claims added or updated
- Edges added or updated
- `NEEDS-HUMAN-REVIEW` items
- Validation and build results

## Rules

- Unsupported theorem statement를 report에 결과처럼 쓰지 않습니다.
- Invented citation이나 theorem number를 만들지 않습니다.
- Ambiguous mathematical point는 review item으로 남깁니다.
- Long prose summary 대신 source location 중심으로 기록합니다.
