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
- Distinguish mathematical status and level.
- Preserve category-level versus Grothendieck-ring-level distinctions.
- Keep the task small and reviewable.

<!-- CODEX-MANAGED: may append source-backed material here -->

## Completion Step

After the topic update and checks, run the next-action planner workflow and update `reports/roadmap/next-actions.md`.

<!-- NEEDS-HUMAN-REVIEW -->

Mark uncertain mathematical wording, notation conflicts, and source-selection choices for human review.
