# Notation Audit Prompt

Use this prompt to audit notation consistency in reader-facing topic pages and source notes. The audit may update the notation registry and review backlog, but it must not rewrite topic pages unless separately approved.

## Inputs To Read

- `content/glossary/notation.md`
- `data/notation.yml`
- topic pages under `content/topics/`
- source notes under `content/sources/`
- `data/review_backlog.yml`
- `data/topic_maturity.yml`
- `reports/roadmap/next-actions.md`

## Raw Patterns To Detect

Search for raw or deprecated forms such as:

- `Cw,v`
- `Aw,v`
- `K0(Cw,v)`
- `K(C)`
- `M(w<=k Lambda, v<=k Lambda)`
- `R-gmod`
- `q commuting`

## Checks

- Reader-facing topic pages use local notation from `content/glossary/notation.md`.
- Source-specific notation appears only in source notes or source translation notes.
- Grothendieck-ring notation is written as $K_0(\mathcal C)$ or $K_0(\mathcal C_{w,v})$ as appropriate.
- Object-level modules, Grothendieck classes, and coordinate-ring elements are not collapsed into one statement.
- $A_{w,v}$ is not identified with $A_q(\mathfrak n(w))$ unless an approved source-backed comparison has been ingested.

## Allowed Outputs

- Add or refine entries in `data/notation.yml`.
- Add actionable fixes to `data/review_backlog.yml`.
- Update notation notes in `data/topic_maturity.yml`.
- Write `reports/reviews/YYYY-MM-DD-notation-audit.md` when requested.
- Update `reports/roadmap/next-actions.md`.

## Safety Rules

- Do not rewrite topic pages during the audit.
- Do not add claims or source notes.
- Do not normalize notation in a way that changes mathematical meaning.
- Mark notation changes requiring mathematical judgment as approval-required.
