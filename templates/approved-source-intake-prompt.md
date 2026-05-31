# Approved Source Intake Prompt

Use this prompt only after the user explicitly approves one specific source by `id`, exact title, or local file path. This workflow may ingest one approved open-access source, but it remains small and source-location-first.

## Required User Approval

Before starting, confirm the user has explicitly approved:

- the exact source id, title, or file path
- downloading the PDF if it is not already local
- the intended target topic ids, if any

If approval is ambiguous, stop and ask for clarification.

## Inputs To Read

- the approved source entry in `data/source_candidates.yml`, if present
- `data/sources.yml`
- `data/claims.yml`
- `data/topics.yml`
- `data/edges.yml`
- `data/topic_maturity.yml`
- relevant topic pages
- relevant source notes
- `content/topics/STYLE_GUIDE.md`
- `reports/roadmap/next-actions.md`

## Allowed Workflow

1. Download only a legitimate open-access PDF, or use the user-provided local file.
2. Preserve the PDF under `content/assets/pdfs/` only when approved.
3. Create one concise source note under `content/sources/papers/`.
4. Add one source entry to `data/sources.yml`.
5. Add at most 8 reusable source-located claims to `data/claims.yml`.
6. Update at most 3 existing topic pages, only with source-backed material. Do not force any missing template section.
   When updating a definition/construction section, make it mathematically complete relative to the source: ambient setting, inputs, output object, and required conditions, relations, maps, or universal property.
7. Update topic hierarchy in `data/topics.yml` and typed hierarchy/context edges in `data/edges.yml`.
8. If a needed parent topic does not exist, create at most one source-backed stub parent topic only when the user has approved new topic creation; otherwise add it to `data/research_queue.yml`.
9. Update `data/source_candidates.yml`, `data/topic_maturity.yml`, and `data/research_queue.yml`; record intentionally unfilled overview, setup/notation, definition, example, viewpoint, property, mechanism, connection, navigation, or source-note components rather than inventing them.
10. Update `reports/roadmap/next-actions.md`.
11. Run the repository checks requested by the current task.

## Prohibitions

- Do not ingest an unapproved source.
- Do not download paywalled, unauthorized, or dubious PDFs.
- Do not create long paper summaries.
- Do not add unsupported claims, invented theorem numbers, fake DOIs, or inferred metadata.
- Do not fill any topic section merely because the template contains it.
- If the approved source does not support accurate content for a section, leave the visible section body empty or omit the optional section, and record the gap outside the topic page.
- Do not force examples. Real examples require an approved source location; schematic examples must be labeled `구조 예시` and explain only a general mechanism.
- Do not create new topic pages unless the user explicitly approves new topic creation.
- Do not rewrite topic pages beyond the approved scope.
- Do not leave a specialized topic isolated in `data/topics.yml`; set parent and prerequisite topics, or mark it provisional and queue the missing parent.

## Source Note Requirements

The source note must be concise and navigational. Prefer:

- bibliographic identity
- what the source is used for in this wiki
- exact theorem, proposition, definition, section, or page references
- notation translation notes
- material intentionally not imported

## Roadmap Update

End by updating `reports/roadmap/next-actions.md` with:

- one safest next task
- up to three alternatives
- approval requirement for each action
- new-source requirement for each action
- intentionally unfilled components and where each gap was recorded
- exact prompt text the user can paste
