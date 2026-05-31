# Source Discovery Prompt

Use this prompt to suggest source candidates for weak topics. This workflow is candidate-only; it does not download, ingest, cite, or make mathematical claims from candidate sources.

## Inputs To Read

- `data/topic_maturity.yml`
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
- Do not invent bibliographic metadata. Use `null` or `[]` when metadata is not verified.
- Mark inferred relevance and notation risk in `risk_notes`.
- Keep proposed actions small and approval-gated when they require source approval or topic edits.
