# 2026-06-01 Global Wiki Review

This report is advisory. It does not authorize source download, source intake, claim additions, topic rewrites, or new topic creation.

This is a same-day follow-up review after the `crystal.tex` topic-slot work, the topic publishability dashboard, the affine/R-matrix prerequisite pass, and the root-object example pass. It supersedes the earlier 12-topic snapshot in this file.

## Scope

Reviewed the topic-centered study wiki across:

- authoring policy in `AGENTS.md`, `content/topics/AGENTS.md`, and `content/topics/STYLE_GUIDE.md`
- topic pages under `content/topics/*.md`
- topic maps under `content/maps/`
- source notes under `content/sources/`
- YAML registries under `data/`
- roadmap, review backlog, previous review reports, and reusable workflow prompts

No papers were downloaded. No claims were added. No topic pages were rewritten during this review.

## Checks Run

- Topic heading audit against the Korean learning-order structure.
- Public readiness check through `content/maps/topic-status.md`.
- Topic-title audit for forced `and` titles and old misleading localization titles.
- Old-title/id scan for `lie-algebras-and-hopf-algebras`, `crystal-bases-and-crystal-graphs`, `quiver-hecke-algebra-localization`, and `localized-category-duality`.
- Prohibited phrase scan on reader-facing topic pages.
- Raw notation scan for deprecated forms such as `Cw,v`, `Aw,v`, `K0(Cw,v)`, and `M(w<=k Lambda, v<=k Lambda)`.
- Review-backlog scan for already recorded open issues.
- Roadmap check for the single safest next task.

## Current Topic State

- Total topic pages: 28.
- Public status count: 16 `publishable`, 12 `incomplete`.
- All topic pages use the Korean learning-order structure with a final `Source notes` section.
- No reader-facing prohibited workflow/status phrase violations were found in topic pages.
- No deprecated raw notation forms were found in reader-facing topic exposition.
- Historical old ids/titles appear only in reports/backlog contexts, not as canonical topic pages or reader-facing topic exposition.
- The only accepted `and` title remains `Root Systems and Weight Lattices`, where the two concepts are tightly coupled prerequisites.

## Findings

### Medium: Root Objects still lacks the reader-facing viewpoint bridge

Files involved:

- `content/topics/08-localization-of-categories/root-objects-in-localized-categories.md`
- `reports/reviews/2026-06-01-root-objects-source-location-review.md`
- `reports/reviews/2026-06-01-affine-r-matrix-prerequisite-source-location-review.md`
- `reports/reviews/2026-06-01-localized-root-operators-source-location-review.md`
- `data/review_backlog.yml`

Issue: `Root Objects in Localized Categories` now has a source-backed definition and conditional example, but the `핵심 관점` and `다른 topic들과의 관계` sections are still empty. This blocks the page from becoming publishable because the reader does not yet see how affinization, R-matrix degree, root objects, and localized root operators fit together.

Recommended action: use only the existing root-object, affine-object, R-matrix, and localized-root-operator reports to propose compact wording for those two sections. Keep it report-only until explicitly approved for topic-page editing.

Requires new source: no.

Requires user approval: yes, before topic-page edits.

Backlog id: `review-2026-06-01-root-objects-viewpoint-relations-gap`.

### Medium: Localized Root Operators still lacks an example and compact viewpoint

Files involved:

- `content/topics/08-localization-of-categories/localized-root-operators.md`
- `reports/reviews/2026-06-01-localized-root-operators-source-location-review.md`
- `data/review_backlog.yml`

Issue: the operator formulas and basic properties are filled, but the `핵심 관점` and `기본 예시` sections remain empty. This is appropriate under the no-fabrication rule, but the page remains incomplete as a study article.

Recommended action: first review whether Kashiwara-Nakashima 2025 contains a concrete operator example or safe mechanism explanation. Do not use the $A_2/A_3$ warnings about $\varepsilon_i(\Phi_w(M))$ as positive examples without a separate decision.

Requires new source: no.

Requires user approval: yes, before topic-page edits.

Backlog id: `review-2026-06-01-localized-root-operators-example-gap`.

### Medium: Four `crystal.tex` intermediate topics are still title-only or near-title-only

Files involved:

- `content/topics/06-quiver-hecke-klr-algebras/normal-sequences.md`
- `content/topics/03-category-theory/quasi-rigid-monoidal-categories.md`
- `content/topics/06-quiver-hecke-klr-algebras/head-simplicity-of-convolutions.md`
- `content/topics/06-quiver-hecke-klr-algebras/shuffle-lemmas-for-quiver-hecke-modules.md`
- `content/maps/topic-status.md`
- `data/topic_maturity.yml`
- `data/review_backlog.yml`

Issue: the missing topic slots were correctly created so the hierarchy can show the path through `crystal.tex`, but these four topics still need exact source-location review before definitions, theorem statements, examples, or mechanism prose can be written.

Recommended action: review one topic at a time using already available source locations. Start with the topic that best supports later localized-root-operator or root-object exposition; do not add content until the exact statement/definition boundary is clear.

Requires new source: no.

Requires user approval: yes, before topic-page edits.

Backlog id: `review-2026-06-01-crystal-tex-stub-topic-backlog`.

### Medium: Several basic example sections remain intentionally empty

Files involved:

- `content/topics/01-quantum-groups/quantum-groups.md`
- `content/topics/01-quantum-groups/quantum-coordinate-rings.md`
- `content/topics/05-monoidal-categorification/monoidal-categorification.md`
- `content/topics/06-quiver-hecke-klr-algebras/determinantial-modules.md`
- `content/topics/08-localization-of-categories/reverse-equivalence-of-localized-categories.md`
- `data/review_backlog.yml`

Issue: the no-forced-completion policy is being followed correctly: unsupported examples were not invented. These pages remain incomplete until exact source-backed examples are reviewed and approved.

Recommended action: use already ingested sources to identify exact real-example candidates and proposed wording. Keep the review report-only unless the user approves topic-page edits.

Requires new source: no.

Requires user approval: yes, before topic-page edits.

Backlog ids:

- `review-2026-06-01-topic-empty-example-sections`
- `review-2026-06-01-reverse-equivalence-example-gap`

### Low: Localization of Categories remains a provisional parent topic

Files involved:

- `content/topics/08-localization-of-categories/category-localization.md`
- `content/topics/08-localization-of-categories/quiver-hecke-category-localization.md`
- `data/research_queue.yml`
- `data/review_backlog.yml`

Issue: the topic hierarchy correctly has a broader `Localization of Categories` node, but the page is intentionally sparse because no general localization source has been approved. This is a gap in the prerequisite path, not a topic-page failure.

Recommended action: evaluate a general or KKOP localization source before adding the formal definition, examples, or theorem-level facts.

Requires new source: yes.

Requires user approval: yes.

Backlog id: `review-2026-06-01-category-localization-source-gap`.

## Clean Checks

- Topic structure: all topic pages follow the Korean learning-order headings.
- Title quality: no misleading canonical topic titles remain from the earlier title audit.
- Reader-facing workflow leakage: none found in topic pages.
- Notation: deprecated raw forms appear only in policy/audit/notation/report contexts, not as topic exposition.
- Candidate-source boundary: candidate sources remain candidates only and are not used as citations.
- Review-state separation: incomplete/publishable status is visible through `content/maps/topic-status.md`, not embedded in topic exposition.

## Residual Risks

- This review did not inspect any new source.
- Historical reports still mention old ids such as `localized-category-duality`; these are archival references and should not be treated as canonical topic ids.
- The current public readiness count depends on generated status metadata; after topic edits, `python3 scripts/run_all_checks.py` should regenerate and validate it.
- The remaining blank sections are intentional under the no-fabrication rule.

## Review Backlog Updates

- Added a completed global review record for this refreshed follow-up review.
- Added an open backlog item for the remaining `crystal.tex` stub-topic cluster.
- Kept the existing root-object viewpoint/relations item as the single safest next task.

## Validation

- `git diff --check`: passed.
- `python3 scripts/run_all_checks.py`: passed, including frontmatter, claims, topics, edges, generated maps, generated topic status, link validation, and the internal Quartz build over 51 content files.
- `npx quartz build`: failed with the known standalone Node heap out-of-memory failure. The Quartz build inside `run_all_checks.py` passed.
