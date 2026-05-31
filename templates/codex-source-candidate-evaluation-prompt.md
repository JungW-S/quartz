<!-- USER-APPROVED: do not rewrite without explicit instruction -->
# Codex Source Candidate Evaluation Prompt

Use this prompt to evaluate possible sources without downloading or ingesting them.

## Inputs To Read

- `data/source_candidates.yml`
- `data/research_queue.yml`
- Existing topic pages and source notes
- User-supplied candidate metadata, if any

## Evaluation Fields

Record candidate entries with:

- `candidate_id`
- `title`
- `authors`
- `year`
- `reason_for_relevance`
- `proposed_target_topics`
- `source_status`
- `access_status`
- `risk_notes`

Allowed `source_status` values: `candidate`, `approved`, `downloaded`, `rejected`.

Allowed `access_status` values: `unknown`, `open-access`, `local-pdf`, `paywalled`.

<!-- CODEX-MANAGED: may append source-backed material here -->

## Safety Rules

- Candidate sources are not citations.
- Candidate sources do not support claims.
- Do not download, fetch, stage, or intake a candidate source without explicit user approval.
- Do not invent missing metadata.
- Do not treat relevance notes as mathematical claims.

<!-- NEEDS-HUMAN-REVIEW -->

Require human review for source selection, paywalled access decisions, ambiguous bibliographic metadata, and any proposed source whose relevance is inferred rather than supplied by the user.
