# Topic Maturity Audit Prompt

Use this prompt to audit every topic page against the canonical maturity levels and the universal article structure. This audit may update workflow registries, but it must not rewrite topic pages unless separately approved.

## Inputs To Read

- `content/topics/AGENTS.md`
- `content/topics/STYLE_GUIDE.md`
- all topic pages under `content/topics/`
- `data/topics.yml`
- `data/topic_maturity.yml`
- `data/research_queue.yml`
- `data/source_candidates.yml`
- `data/review_backlog.yml`
- `reports/roadmap/next-actions.md`

## Maturity Levels

Allowed `maturity` values:

- `stub`
- `orientation`
- `definition-ready`
- `example-ready`
- `study-ready`
- `reviewed`

Allowed `missing_components` values:

- `definition`
- `setup and notation`
- `basic picture`
- `example`
- `main facts`
- `source notes`
- `connections`

## Audit Checks

- Does the topic follow the universal structure?
- Is the fourth section an allowed variant?
- Are source notes present and visually secondary?
- Are definitions, examples, and main facts source-supported?
- Does the page separate object-level, class-level, and algebra-level statements where relevant?
- Does the page expose workflow state or editorial status in reader-facing prose?
- Does the page use local notation from `content/glossary/notation.md` and `data/notation.yml`?

## Allowed Outputs

- Update `data/topic_maturity.yml`.
- Update `data/research_queue.yml`.
- Add or update `data/review_backlog.yml` items.
- Update `reports/roadmap/next-actions.md`.
- Optionally write `reports/reviews/YYYY-MM-DD-topic-maturity-audit.md`.

## Safety Rules

- Do not rewrite topic pages during the audit.
- Do not add claims, source notes, or graph edges.
- Do not download or intake sources.
- Mark topic rewrites, claim additions, and source intake as approval-required actions.
