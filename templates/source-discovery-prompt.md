# Source Discovery Prompt

Use this prompt to suggest source candidates for weak topics. This workflow is candidate-only; it does not download, ingest, cite, or make mathematical claims from candidate sources.

## Inputs To Read

- `data/topic_maturity.yml`
- `data/topics.yml`
- `data/edges.yml`
- `data/research_queue.yml`
- `data/source_candidates.yml`
- `data/sources.yml`
- existing source notes under `content/sources/papers/`
- relevant topic pages under `content/topics/`
- `reports/roadmap/next-actions.md`

## Allowed Outputs

- Add or update entries in `data/source_candidates.yml` using the canonical schema.
- Add review or source-selection follow-up items to `data/review_backlog.yml` when needed.
- Update `reports/roadmap/next-actions.md` with small candidate-evaluation actions.
- Propose hierarchy repairs in `data/research_queue.yml` when a weak topic lacks a parent or prerequisite source path.
- Propose references for missing overview, setup/notation, definitions, real examples, viewpoints, properties, mechanisms, connections, navigation, source notes, and prerequisite explanations. Candidate sources do not fill those gaps until approved and ingested.

## Required Candidate Fields

- `id`
- `title`
- `authors`
- `year`
- `arxiv`
- `doi`
- `reason_for_relevance`
- `target_topics`
- `expected_gaps_filled`
- `access_status`
- `risk_notes`
- `status`

Allowed `status` values: `candidate`, `approved`, `downloaded`, `rejected`.

## Safety Rules

- Do not download, fetch, stage, or intake any source.
- Do not treat a candidate as a citation.
- Do not add claims, source notes, graph edges, or topic-page prose from candidate material.
- Do not create topic pages or hierarchy edges from candidate material.
- Do not invent bibliographic metadata. Use `null` or `[]` when metadata is not verified.
- Mark inferred relevance and notation risk in `risk_notes`.
- Mark which missing components each candidate might fill, especially definitions, setup/notation, examples, and properties, without treating the candidate as evidence.
- Keep proposed actions small and approval-gated when they require source approval or topic edits.
- If a needed parent topic does not exist, add a research-queue item instead of creating it.
