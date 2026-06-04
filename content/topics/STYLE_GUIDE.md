---
id: topic-page-style-guide
title: Topic Page Style Guide
level: reference
---

Topic pages are concise mathematical study articles. They should be readable without knowing that `data/claims.yml` exists.

## Universal Structure

Use this learning-order structure for new or rewritten topic pages:

1. `개요`
2. `준비와 notation`
3. `정의`
4. `기본 예시`
5. `핵심 관점`
6. `기본 성질`
7. Optional: `성질이 작동하는 방식`
8. `다른 topic들과의 관계`
9. `더 읽을 topic`
10. `Source notes`

Controlled variants for the third section:

- Construction topics may use `구성`.
- Theorem topics may use `정리의 진술`.
- Map or operation topics may use `map의 정의`.
- Basis, category, algebra, object, and object-family topics should usually keep `정의`.

Do not use `Toy model` as a heading. Put schematic examples under `## 기본 예시` as `### 구조 예시`; schematic examples still require paper support or Sage verification. Use real verified examples directly under `## 기본 예시` or with a concise descriptive subheading.

## Reader-Facing Rules

- Write in learning order, not source order.
- Use a title that names one central mathematical object, construction, theorem, map, or category.
- Avoid joining separate topics with `and` in the title unless the combination is a standard tightly coupled study unit. `Root Systems and Weight Lattices` is acceptable because the page is a prerequisite unit for root and weight notation; a page should not be titled by unrelated prerequisites merely because both appear later.
- If a page uses several prerequisite notions, title it by the central notion and explain the others in `준비와 notation`, `기본 성질`, or `다른 topic들과의 관계`.
- Match the title to the mathematical level: object-level, category-level, Grothendieck-ring-level, coordinate-ring-level, cluster-algebra-level, crystal-level, geometric-level, or combinatorial-level.
- Start `개요` with a direct characterization of the mathematical topic.
- In `개요`, answer what the topic is, why it appears, and where it is used.
- Do not fill any section merely because the template contains that section.
- If a section cannot be filled accurately from studied approved sources or explicit user-approved exposition, leave the visible section body empty or omit the optional section; do not add placeholder text, caveats, apology prose, or workflow status.
- If a definition, setup explanation, example, viewpoint, property, mechanism, connection, reader-navigation item, or source note is not source-backed or user-approved as exposition-only, record the gap in workflow metadata instead of inventing content.
- Do not mention wiki workflow, source intake, missing imports, claim registries, or editorial status in the main exposition.
- Do not mention topic maturity, review backlog, audit status, research queue entries, or roadmap state in reader-facing topic prose.
- Do not use phrases such as "현재 이 wiki", "현재 page", "currently this wiki", "currently this page", "not yet imported", "source-poor", "future source work", "needs later source expansion", "claim metadata", "source-backed claim", "current limitations", or "editorial notes".
- Move review tasks, unresolved bibliographic issues, missing source work, intentionally unfilled components, and claim IDs to source notes, YAML metadata, or roadmap reports.
- Keep `Source notes` last and visually secondary, except for the short verification label required directly under visible examples.
- Preserve provenance, but do not let provenance dominate the article.

## Hierarchy Metadata

- Every topic should have hierarchy metadata in `data/topics.yml`: `topic_kind`, `parent_topics`, `prerequisite_topics`, `child_topics`, `related_topics`, and `maturity`.
- Parent topics are broader mathematical concepts under which the current topic sits.
- Prerequisite topics are topics a reader should understand before the current topic.
- Child topics are narrower topics directly below the current topic.
- Related topics are useful nearby topics, but they are not prerequisites and not broader/narrower hierarchy links.
- Explain hierarchy naturally in `## 다른 topic들과의 관계`; do not add a visible workflow/status section just to display registry metadata.
- Use `## 더 읽을 topic` for reader navigation through prerequisites, parent topics, and natural next topics.
- A specialized topic should not be isolated. If it truly has no parent yet, mark it as `topic_kind: provisional` in `data/topics.yml` and record the missing parent in the research queue.

## Section Rules

- `개요`: identify the mathematical kind of the topic, the reason it appears, and the main places it is used. If those roles are not supported, leave unsupported parts out and record the gap.
- `준비와 notation`: introduce only source-backed ambient data, assumptions, domains, codomains, categories, rings, bases, or symbols before heavy use.
- `정의` / variant: state the stable source-supported definition, construction, theorem statement, or map definition cleanly and completely relative to the page level. If the exact definition cannot be written, leave the section body empty and record the `definition` gap.
- `기본 예시`: give a paper-verified or Sage-verified example immediately after the definition when available. Put a short verification label directly below the example, and put detailed provenance in final `Source notes`. If no verified example exists, omit visible example content and record the gap outside the topic page.
- `핵심 관점`: provide the main diagram, slogan, formula, or mental model only when it is mathematically safe and supported by approved sources or user-approved exposition.
- `기본 성질`: list only source-backed central properties or theorem-level facts in readable prose with brief mathematical significance.
- `성질이 작동하는 방식`: include only when there is a source-backed meaningful computation, worked example, or mechanism; omit when unsupported or when it would only repeat `기본 성질`.
- `다른 topic들과의 관계`: explain only mathematical relationships to linked topics that are source-backed, hierarchy-backed, or user-approved.
- `더 읽을 topic`: list prerequisite topics, parent topics, and natural next topics only when the relation is established in hierarchy metadata or workflow decisions.
- `Source notes`: use collapsible `<details>` when possible and keep notes short; include only sources actually used by the visible page.

## Empty Section Policy

- The universal structure may keep a heading even when its body is empty, so readers and audits can see which learning step is intentionally awaiting support.
- Do not write "not yet known", "needs source", or other workflow-status prose under an empty section.
- Record each intentionally empty or deferred section in `data/topic_maturity.yml`, `data/research_queue.yml`, `data/review_backlog.yml`, or `reports/roadmap/next-actions.md`.
- If an optional section such as `성질이 작동하는 방식` has no safe content, omit the section entirely.

## Example Policy

- Visible examples require either an approved source location or checked Sage code stored in this repository.
- Use exactly one short verification label directly under each visible example:
  - `검증: 논문 예시` for an example, computation, figure, table, or page explicitly present in an approved source.
  - `검증: Sage 계산` for an example verified by a Sage script under `scripts/examples/<topic-id>/<example-id>.sage`.
  - `검증: 논문 그림` for a visual example captured or converted from an approved source figure, table, or page.
- Detailed provenance belongs in final `Source notes`: exact source location, PDF path, Sage command, code path, generated image path, and reproduction notes when applicable.
- Schematic examples must be labeled `### 구조 예시`.
- Schematic examples may explain only a general mechanism; they must not assert theorem-level facts, source-specific computations, or unsupported terminology. They still require paper support or Sage verification.
- Do not use LLM-generated mathematical examples or LLM-generated mathematical figures as topic-page examples unless independently verified by an approved source or checked Sage code.
- Sage-based examples must first construct and check the mathematical object, then generate any image from the checked data.
- Store Sage example code under `scripts/examples/<topic-id>/`, generated example images under `content/assets/images/examples/<topic-id>/`, and optional verification reports under `reports/examples/`.
- Do not invent examples to satisfy the template. If no verified example exists, record the missing example in `data/research_queue.yml`, `data/review_backlog.yml`, or `reports/roadmap/next-actions.md`.

## Definition Completeness Policy

- A definition section must state the ambient context and input data before or inside the definition.
- A definition of an algebra, category, basis, object family, construction, theorem, map, or operation must include the required relations, conditions, maps, universal property, or source-defined membership criterion that makes the object mathematically determined.
- Definitions must distinguish object-level, category-level, Grothendieck-ring-level, coordinate-ring-level, cluster-algebra-level, crystal-level, geometric-level, and combinatorial-level statements when more than one level appears.
- Slogans, motivation, analogies, and "acts like" explanations belong in `개요` or `핵심 관점`, not as replacements for the formal definition.
- If an approved source supports only an orientation-level description, record `definition` as missing in metadata and leave the visible definition section empty rather than writing a stronger visible definition.

## User Discussion Policy

- User discussions may support exposition, motivation, learning order, analogy, and notation decisions.
- User discussions must not support theorem-level claims, source-backed definitions, real examples, or claim additions.
- Store user-approved discussion material in `data/discussion_notes.yml` with labels such as `user-approved-exposition`, `user-approved-interpretation`, `notation-decision`, or `learning-order-decision`.
- Keep discussion-based guidance distinguishable from paper, book, and lecture sources.

## Topic-Type Rules

- Object or object-family topics: use `정의`, `준비와 notation`, `기본 예시`, and `기본 성질`.
- Construction topics: use `구성` when it is clearer than `정의`.
- Theorem topics: use `정리의 진술`; put assumptions in `준비와 notation`.
- Map or operation topics: use `map의 정의`; put domain and codomain in `준비와 notation`.
- Category or algebra topics: use `정의`, `기본 예시`, and `기본 성질`; avoid object-centric headings.

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
- The `topic 수정` / `토픽수정` trigger is an edit pass, not an audit-only pass: choose one low-count topic, improve only sentence clarity and learning-order structure, and record the completed pass in `data/topic_polish_log.yml`.
