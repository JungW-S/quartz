# Review Reports

Review reports are dated audit records for the research workflow. They are advisory: they may create review backlog items and roadmap actions, but they do not authorize source downloads, source intake, claim additions, topic rewrites, or new topic creation.

## Filename Patterns

Use these names for generated reports:

```text
reports/reviews/YYYY-MM-DD-global-wiki-review.md
reports/reviews/YYYY-MM-DD-readability-audit.md
reports/reviews/YYYY-MM-DD-notation-audit.md
reports/reviews/YYYY-MM-DD-topic-maturity-audit.md
```

If a report is scoped to one topic, append the topic id before the suffix:

```text
reports/reviews/YYYY-MM-DD-determinantial-modules-notation-audit.md
```

## Report Contents

Each report should include:

- scope and files reviewed
- checks performed
- findings ordered by severity
- exact follow-up actions
- whether each action requires a new source
- whether each action requires user approval
- linked backlog ids from `data/review_backlog.yml`

## Rules

- Candidate sources mentioned in reports are candidates only.
- Do not cite candidates as evidence for topic claims.
- Do not download, fetch, stage, or intake sources from a report without explicit user approval.
- Do not rewrite topic pages or add claims from a review report unless the user separately approves that action.
- Keep reader-facing topic pages free of review status, backlog ids, and workflow metadata.
