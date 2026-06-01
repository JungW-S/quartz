<!-- USER-APPROVED: do not rewrite without explicit instruction -->
# Codex Next-Action Planner Prompt

Use this prompt after every paper-intake or topic-expansion task. The output is an advisory roadmap, not execution permission.

## Inputs To Read

- `data/research_queue.yml`
- `data/source_candidates.yml`
- `data/topics.yml`
- `data/sources.yml`
- `data/claims.yml`
- `data/edges.yml`
- Recent `reports/intake/*.md`
- Topic pages touched by the current task

## Required Output

Update `reports/roadmap/next-actions.md` with exactly top 3 recommended next actions.

For each action, include:

- action type
- why it matters
- exact files likely to change
- whether user approval is required
- expected mathematical benefit
- risk level
- intentionally unfilled components from the completed task, if any, and where each gap was recorded

## Ranking Criteria

- mathematical importance
- current page weakness
- dependency value
- source availability
- risk of hallucination

## Allowed Action Types

- `existing-source expansion`
- `new-source intake`
- `topic-page polishing`
- `graph cleanup`
- `notation normalization`
- `human-review task`

<!-- CODEX-MANAGED: may append source-backed material here -->

## Safety Rules

- Prefer existing-source expansion when existing source-backed claims are enough.
- Mark source proposals as candidates only.
- Do not download, fetch, stage, or intake any new source without explicit user approval.
- Do not create unsupported mathematical claims.
- Do not recommend filling any template section without source-backed material, established hierarchy metadata, or explicit user-approved discussion guidance.
- If a section was intentionally left empty because accurate content is unavailable, recommend source discovery, human review, or metadata cleanup rather than prose filling.
- Visible examples require an approved source location or checked Sage code stored in this repository; otherwise recommend source discovery, a Sage-verifiable example task, or record an example gap.
- Example-related next actions should say whether the target verification label would be `검증: 논문 예시`, `검증: Sage 계산`, or `검증: 논문 그림`.
- Do not turn the wiki into a paper-summary archive.

<!-- NEEDS-HUMAN-REVIEW -->

Record any action that depends on mathematical judgment, notation normalization, citation correction, or source selection as requiring human review.
