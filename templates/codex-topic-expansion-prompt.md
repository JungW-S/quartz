<!-- USER-APPROVED: do not rewrite without explicit instruction -->
# Codex Topic Expansion Prompt

Use this prompt to expand one existing topic page while keeping the page concept-first.

## Inputs To Read

- Target topic page
- `data/topics.yml`
- Relevant entries in `data/claims.yml`
- Relevant entries in `data/sources.yml`
- Relevant source notes
- `data/research_queue.yml`

## Rules

- Use existing source-backed claims first.
- Keep source details near the bottom of the topic page.
- Do not add theorem, definition, example, or construction text without a source-backed claim or explicit source location.
- Do not fill any section merely because the template contains it.
- If studied approved material cannot support accurate content for overview, setup/notation, definition, example, viewpoint, property, mechanism, connection, navigation, or source notes, leave the section body empty or omit the optional section and record the gap outside the topic page.
- Visible examples require an approved source location or checked Sage code stored in this repository. Label each visible example as `검증: 논문 예시`, `검증: Sage 계산`, or `검증: 논문 그림` directly under the example.
- Schematic examples must be labeled `구조 예시`, explain only a general mechanism, and still be paper- or Sage-verified.
- Visual examples must come from an approved source figure/table/page or from checked Sage code that first verifies the mathematical object and then generates the image. Do not use LLM-generated mathematical figures unless independently verified by source or Sage.
- Record missing overview, setup/notation, definitions, examples, viewpoints, properties, mechanisms, connections, prerequisites, navigation, and source notes in `data/topic_maturity.yml`, `data/research_queue.yml`, `data/review_backlog.yml`, or `reports/roadmap/next-actions.md`.
- Distinguish mathematical status and level.
- Preserve category-level versus Grothendieck-ring-level distinctions.
- Keep the task small and reviewable.

<!-- CODEX-MANAGED: may append source-backed material here -->

## Completion Step

After the topic update and checks, run the next-action planner workflow and update `reports/roadmap/next-actions.md`. Include intentionally unfilled components and where each gap was recorded.

<!-- NEEDS-HUMAN-REVIEW -->

Mark uncertain mathematical wording, notation conflicts, and source-selection choices for human review.
