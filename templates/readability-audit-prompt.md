# Readability Audit Prompt

Use this prompt to audit topic pages against `content/topics/STYLE_GUIDE.md`. This audit detects reader-facing prose issues and workflow leakage, but it does not rewrite pages unless the user separately approves edits.

## Inputs To Read

- `content/topics/AGENTS.md`
- `content/topics/STYLE_GUIDE.md`
- topic pages under `content/topics/`
- `data/topic_maturity.yml`
- `data/review_backlog.yml`
- `reports/roadmap/next-actions.md`

## Checks

- Universal section structure is present.
- The fourth section is `Definition`, `Construction`, `Statement`, or `Definition of the map`.
- Reader-facing prose does not mention workflow state, claim registries, source intake, editorial status, or roadmap language.
- The page does not include prohibited sections such as `Editorial notes`, `Current limitations`, `Human-review items`, `Human-review needed`, `Source provenance`, `Claim index`, `Roadmap`, or `Next sources needed`.
- Source notes are last and secondary.
- Paragraphs are short and symbols are introduced before heavy use.
- Topic pages use proper Markdown math delimiters.

## Prohibited Phrase Scan

Flag phrases such as:

- "currently this wiki"
- "currently this page"
- "safe to say"
- "not yet imported"
- "source-poor"
- "future source work"
- "needs later source expansion"
- "notation is not normalized"
- "current limitations"
- "editorial notes"
- "claim metadata"
- "source-backed claim"

## Allowed Outputs

- Write `reports/reviews/YYYY-MM-DD-readability-audit.md` when requested.
- Update `data/review_backlog.yml`.
- Update `data/topic_maturity.yml` readability notes.
- Update `reports/roadmap/next-actions.md`.

## Safety Rules

- Do not rewrite topic pages during the audit.
- Do not add claims or source notes.
- Do not make mathematical assertions from readability findings.
- Mark any page rewrite as approval-required.
