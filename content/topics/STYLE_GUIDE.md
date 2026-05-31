---
id: topic-page-style-guide
title: Topic Page Style Guide
level: reference
---

# Topic Page Style Guide

Topic pages are concise mathematical study articles. They should be readable without knowing that `data/claims.yml` exists.

## Universal Structure

Use this default structure:

1. `What it is`
2. `Why it appears`
3. `Setup and notation`
4. `Definition`
5. `Basic picture`
6. `Example`
7. `Main facts`
8. `Why it matters`
9. `Connections`
10. `Source notes`

Controlled variants for the fourth section:

- Construction topics may use `Construction`.
- Theorem topics may use `Statement`.
- Map or operation topics may use `Definition of the map`.
- Basis, category, algebra, object, and object-family topics should usually keep `Definition`.

Do not use `Where they live` or `Toy model` as top-level headings. Put schematic examples under `## Example` as `### Schematic example`; put real examples under `## Example` as `### Concrete example`.

## Reader-Facing Rules

- Start `What it is` with a direct definition-style sentence.
- Do not mention wiki workflow, source intake, missing imports, claim registries, or editorial status in the main exposition.
- Do not mention topic maturity, review backlog, audit status, research queue entries, or roadmap state in reader-facing topic prose.
- Do not use phrases such as "currently this wiki", "currently this page", "not yet imported", "source-poor", "future source work", "needs later source expansion", "claim metadata", "source-backed claim", "current limitations", or "editorial notes".
- Move review tasks, unresolved bibliographic issues, missing source work, and claim IDs to source notes, YAML metadata, or roadmap reports.
- Keep `Source notes` last and visually secondary.
- Preserve provenance, but do not let provenance dominate the article.

## Section Rules

- `What it is`: identify the mathematical kind of the topic immediately.
- `Why it appears`: explain the structural need or problem the topic addresses.
- `Setup and notation`: introduce ambient data, assumptions, domains, codomains, categories, rings, bases, or symbols.
- `Definition` / variant: state the stable source-supported formulation cleanly.
- `Basic picture`: provide a diagram, formula, or mental model that supports the definition.
- `Example`: prefer one concrete example; otherwise use a clearly labeled schematic example.
- `Main facts`: list central facts in readable prose with brief mathematical significance.
- `Why it matters`: explain what the topic enables.
- `Connections`: explain mathematical relationships to nearby topics.
- `Source notes`: use collapsible `<details>` when possible and keep notes short.

## Topic-Type Rules

- Object or object-family topics: use `Definition`, `Setup and notation`, `Example`, and `Main facts`.
- Construction topics: use `Construction` when it is clearer than `Definition`.
- Theorem topics: use `Statement`; put assumptions in `Setup and notation`.
- Map or operation topics: use `Definition of the map`; put domain and codomain in `Setup and notation`.
- Category or algebra topics: use `Definition`, `Example`, and `Main facts`; avoid object-centric headings.

## Readability Rules

- Use Korean explanatory prose with English mathematical technical terms.
- Keep paragraphs short, usually 2-4 sentences.
- Prefer one clear displayed formula over many inline formulas.
- Use bullet lists only for parallel information.
- Explain symbols before using them heavily.
- Avoid vague phrases such as "coordinate-like data", "controlled behavior", "surrounding background", and "algebraic target" unless immediately clarified.
- Use proper Markdown math delimiters: inline `$...$`, displayed `$$...$$`.
- Follow `content/glossary/notation.md`.
- Use `templates/readability-audit-prompt.md` for audit-only passes; audits should report deviations in `data/review_backlog.yml` or `reports/reviews/`, not in the topic page itself.
- Use `templates/topic-maturity-audit-prompt.md` to update maturity metadata without exposing maturity labels in reader-facing prose.
