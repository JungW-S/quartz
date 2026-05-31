# 2026-06-01 Global Wiki Review

This report is advisory. It does not authorize source download, source intake, claim additions, topic rewrites, or new topic creation.

## Scope

Reviewed the topic-centered study wiki across:

- `AGENTS.md`, `README.md`, topic authoring rules, and style guide
- topic pages under `content/topics/`
- source notes under `content/sources/`
- YAML registries under `data/`
- roadmap, review reports, and reusable workflow prompts

## Checks Run

- `python3 scripts/validate_frontmatter.py`: passed
- `python3 scripts/validate_claims.py`: passed
- `python3 scripts/validate_topics.py`: passed
- `python3 scripts/validate_edges.py`: passed
- `python3 scripts/validate_links.py`: passed
- Topic-page prohibited phrase search: no reader-facing topic-page violations found
- Raw notation search for `Cw,v`, `Aw,v`, `K0(Cw,v)`, and determinantial-module plain-text forms: no reader-facing topic-page violations found
- Topic heading audit against the universal structure
- Registry consistency spot checks for topic maturity, queue topic ids, claim sources, and candidate target topics

## Findings

### Medium: Some study pages still miss universal sections

Files involved:

- `content/topics/quantum-coordinate-rings.md`
- `content/topics/dual-canonical-bases.md`
- `content/topics/monoidal-categorification.md`

Issue: these pages are readable and source-backed, but they do not yet fully follow the universal topic-page structure. In particular, they lack separate `Why it appears` and/or `Setup and notation` sections.

Recommended action: run a focused topic-page polishing pass for these three pages using only already ingested sources, and request explicit user approval before rewriting topic prose.

Requires new source: no.

Requires user approval: yes, before topic-page edits.

Backlog id: `review-2026-05-31-topic-section-order`.

### Medium: Topic maturity metadata has stale missing-component details

Files involved:

- `data/topic_maturity.yml`
- `content/topics/dual-canonical-bases.md`

Issue: the `dual-canonical-bases` maturity entry still lists `source notes` as missing, but the topic page already has a final `Source notes` section. The same audit should check whether the three section-order pages have current missing-component labels.

Recommended action: run `templates/topic-maturity-audit-prompt.md` for maturity metadata only; do not rewrite topic pages during that audit.

Requires new source: no.

Requires user approval: no for metadata audit; yes for any later topic-page rewrite.

Backlog id: `review-2026-06-01-topic-maturity-metadata-stale`.

### Low: One source candidate targets a noncanonical topic id

File involved:

- `data/source_candidates.yml`

Issue: `marberg20-combinatorics-crystal-bases-lectures` has `root-systems` in `target_topics`, but the canonical topic id is `root-systems-and-weight-lattices`.

Recommended action: perform a registry cleanup replacing the noncanonical target id with `root-systems-and-weight-lattices`.

Requires new source: no.

Requires user approval: no.

Backlog id: `review-2026-06-01-source-candidate-target-topic-id`.

### Closed During Review: Localized-crystals source-coverage warning is stale

Files involved:

- `data/review_backlog.yml`
- `content/topics/localized-crystals.md`

Issue: the old backlog item `review-2026-05-31-localized-crystals-source-coverage` said the page had no approved attached source. That is no longer accurate: `localized-crystals` now cites Kashiwara-Nakashima 2025 and Kashiwara 1993 in its final source notes.

Recommended action: mark the stale backlog item done. No topic-page change is needed.

Requires new source: no.

Requires user approval: no.

Backlog id: `review-2026-05-31-localized-crystals-source-coverage`.

## Residual Risks

- The review did not download or inspect any new source.
- Candidate sources remain candidates only and do not support topic claims.
- `npx quartz build` was not rerun during this review because the requested workflow was audit/report/backlog oriented and the registry validators and link checks passed.
- The highest-value reader-facing follow-up is still a controlled topic-page polishing pass, not an automatic rewrite.
