# Next Actions

This roadmap is advisory. It does not authorize source download, source intake, claim addition, topic rewrite, or new topic creation.

## Current Workflow State

- The 2026-06-01 global wiki review was completed and recorded at `reports/reviews/2026-06-01-global-wiki-review.md`.
- The 2026-06-01 notation audit was completed and recorded at `reports/reviews/2026-06-01-notation-audit.md`.
- The universal topic template, style guide, and audit prompts use the Korean learning-order structure.
- All topic pages under `content/topics/*.md` follow the Korean learning-order structure: `개요`, `준비와 notation`, `정의` or an approved variant, `기본 예시`, `핵심 관점`, `기본 성질`, `다른 topic들과의 관계`, `더 읽을 topic`, and final `Source notes`.
- A 2026-06-01 definition-completeness pass strengthened `정의` and `구성` sections where approved sources already supported complete data, relations, maps, or construction formulas.
- Follow-up correction: `cellular-crystals` now uses an explicit `정의` section rather than the construction variant, and `crystal-bases` states the abstract crystal axioms as formal conditions.
- The no-forced-completion policy now applies to every topic-page section: unsupported section bodies should remain empty or optional sections should be omitted, with gaps recorded outside reader-facing prose.
- The migration did not download sources, add claims, or add unsupported mathematical statements.
- The 2026-06-01 all-topic unsupported-content pass removed unsupported schematic examples and interpretive wording. The `기본 예시` sections in `quantum-groups`, `quantum-coordinate-rings`, `monoidal-categorification`, and `determinantial-modules` are intentionally empty until exact source-backed examples are approved.
- The determinantial-module definition-depth gap is closed: `determinantial-modules` now includes the KKOP18 Proposition 4.1 recursive construction of $M(\lambda,\mu)$.
- The 2026-06-01 title audit removed forced or misleading titles: `Crystal Bases and Crystal Graphs` became `Crystal Bases`, `Lie Algebras and Hopf Algebras` became `Universal Enveloping Algebras`, and `Quiver-Hecke Algebra Localization` became `Quiver-Hecke Category Localization`.
- Full-review, readability-audit, and topic-maturity prompts now include title-quality checks.
- Remaining registry cleanup: none known after replacing the Marberg lecture candidate target with `root-systems-and-weight-lattices`.
- The refreshed 2026-06-01 global review found no reader-facing prohibited phrase or raw-notation violations in topic pages.
- Current full-review issues are: the localized-root-operator example gap, two remaining sparse `crystal.tex` intermediate topics, intentionally empty example sections, and the optional future scope review for Hopf-algebra material inside the Universal Enveloping Algebras page.
- Validation after the hierarchy pass: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including its internal Quartz build over 37 content files; standalone `npx quartz build` still fails with the known Node heap out-of-memory failure.
- The 2026-06-01 hierarchy pass added intermediate topics: `Quiver-Hecke Module Categories`, `Quiver-Hecke Subcategories`, and provisional `Category Localization`.
- Existing localization pages now route through the category hierarchy `Quiver-Hecke Algebras -> Quiver-Hecke Module Categories -> Quiver-Hecke Subcategories -> Quiver-Hecke Category Localization -> Localized Crystals`.
- `Category Localization` is no longer a stub: KKOP21 now supports left braiders, real commuting families of braiders, the localization universal property, graded exactness, the $\mathcal C_w\to\widetilde{\mathcal C}_w$ construction, Grothendieck-ring localization, and left rigidity.
- The quiver-Hecke map scopes were updated so generated maps include the new intermediate category topics.
- The 2026-06-01 $\mathcal C_w$ / $\mathcal C_{w,v}$ definition verification was completed at `reports/reviews/2026-06-01-cw-cwv-definition-verification.md`. No topic pages, claims, or downloaded sources were changed in that verification pass.
- The verified definitions of $\mathcal C_w$, $\mathcal C_{*,v}$, and $\mathcal C_{w,v}$ were applied to `content/topics/quiver-hecke-subcategories.md`.
- Validation after applying the verified subcategory definitions: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including its internal Quartz build over 37 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
- The 2026-06-01 report-only example review for `Quiver-Hecke Subcategories` was completed at `reports/reviews/2026-06-01-quiver-hecke-subcategories-example-review.md`. It found a safe type $A_2$ example for $\mathcal C_w$, a KN25 non-example, and a KKOP18 determinantial-module family candidate. No topic pages, claims, or downloads were changed in that review pass.
- Validation after the report-only example review: `git diff --check` passed; the validation-script portion of `python3 scripts/run_all_checks.py` passed, but its standard `public` Quartz cleanup failed with `ENOTEMPTY`; a Quartz build to `/tmp/wiki-codex-quartz-example-review-check` passed over 37 content files.
- The reviewed type $A_2$ example $\mathcal C_w=R\text{-gmod}$ was applied to `content/topics/quiver-hecke-subcategories.md`; the page is now example-ready.
- Validation after applying the type $A_2$ example: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including its internal Quartz build over 37 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
- The optional-example decision for `Quiver-Hecke Subcategories` was completed at `reports/reviews/2026-06-01-quiver-hecke-subcategories-optional-example-decision.md`: add the KN25 non-example if approved, but keep the KKOP18 determinantial-module family on the `Determinantial Modules` page.
- Validation after the optional-example decision: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including its internal Quartz build over 37 content files.
- The 2026-06-01 `crystal.tex` topic-slot audit was completed at `reports/reviews/2026-06-01-crystal-tex-topic-slot-audit.md`.
- Title-only stub topics were created for the missing intermediate layers needed to read `crystal.tex`: Pro-Categories, Graded Monoidal Categories, Affine Objects in Monoidal Categories, R-Matrix Renormalization, Normal Sequences, Quasi-Rigid Monoidal Categories, Head Simplicity of Convolutions, Shuffle Lemmas for Quiver-Hecke Modules, Demazure Subcategories of Quiver-Hecke Modules, Root Objects in Localized Categories, Localized Root Operators, Crystal Comparison Map, and the topic now titled Reverse Equivalence of Localized Categories.
- Except for `Root Objects in Localized Categories`, these pages contain no mathematical exposition yet; unsupported definitions, examples, theorem statements, and properties remain unfilled and are recorded in `data/topic_maturity.yml`, `data/research_queue.yml`, and `data/review_backlog.yml`.
- Validation after the topic-slot audit: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including its internal Quartz build over 50 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
- The 2026-06-01 source-location review for `Root Objects in Localized Categories` was completed at `reports/reviews/2026-06-01-root-objects-source-location-review.md`. It found the exact root-object definition and the key caution that $\widetilde Q_i$ is not always a root object.
- Validation after the root-object source-location review: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including its internal Quartz build over 50 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
- The 2026-06-01 topic publishability polish was completed and recorded at `reports/reviews/2026-06-01-topic-publishability-polish.md`.
- A public readiness dashboard is generated at `content/maps/topic-status.md` and linked from the site home page. It keeps publishable/incomplete judgments outside reader-facing topic exposition.
- The first polishing batch tightened Korean learning-order prose and prerequisite links for `Root Systems and Weight Lattices`, `Universal Enveloping Algebras`, `Quantum Groups`, `Crystal Bases`, and `Quiver-Hecke Algebras`.
- Status count after the topic publishability polish: 16 topics were marked `publishable`, and 12 topics were marked `incomplete`.
- Validation after the topic publishability polish: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 51 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
- The reviewed root-object definition was applied to `content/topics/root-objects-in-localized-categories.md`. The page is now definition-ready, while its example, viewpoint, and relation sections remain intentionally unfilled.
- Validation after applying the root-object definition: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 51 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
- The 2026-06-01 source-location review for `Localized Root Operators` was completed at `reports/reviews/2026-06-01-localized-root-operators-source-location-review.md`. No topic page, claim, or source download was changed in that review pass.
- Validation after the localized-root-operators source-location review: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 51 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
- The reviewed localized-root-operator formulas were applied to `content/topics/localized-root-operators.md`. The page is now definition-ready, while its example and viewpoint sections remain intentionally unfilled.
- Validation after applying the localized-root-operator definition: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 51 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
- The 2026-06-01 source-location review for `Crystal Comparison Map` was completed at `reports/reviews/2026-06-01-crystal-comparison-map-source-location-review.md`. No topic page, claim, or source download was changed in that review pass.
- Validation after the crystal-comparison-map source-location review: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 51 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
- The reviewed crystal-comparison-map definition and theorem-level facts were applied to `content/topics/crystal-comparison-map.md`. The page is now definition-ready; its `기본 예시` section remains empty until the $A_3$ example is separately reviewed.
- Validation after applying the crystal-comparison-map page: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 51 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
- The 2026-06-01 report-only A3 example review for `Crystal Comparison Map` was completed at `reports/reviews/2026-06-01-crystal-comparison-map-a3-example-review.md`. It proposes compact wording for a real source-backed example and recommends not adding the full four-cluster region partition yet.
- Validation after the report-only A3 example review: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 51 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
- The compact A3 example was applied to `content/topics/crystal-comparison-map.md`. The page is now example-ready and publishable; the full four-cluster region partition remains deferred.
- Validation after applying the compact A3 example: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 51 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
- The 2026-06-01 source-location review for `Reverse Equivalence of Localized Categories` was completed at `reports/reviews/2026-06-01-localized-category-duality-source-location-review.md`. No topic page, claim, or source download was changed in that review pass.
- Validation after the localized-category-duality source-location review: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 51 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
- `Localized Category Duality` was retitled to `Reverse Equivalence of Localized Categories` and filled from the reviewed source locations. The page is now definition-ready; its example section remains empty.
- Validation after applying the reverse-equivalence page: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 51 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
- The 2026-06-01 source-location review for `Demazure Subcategories of Quiver-Hecke Modules` was completed at `reports/reviews/2026-06-01-demazure-subcategories-source-location-review.md`. It found that the source notation is $\mathfrak B_w$, not the local alias $\mathcal C_{\mathcal B_w}$. No topic page, claim, or source download was changed in that review pass.
- Validation after the demazure-subcategories source-location review: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 51 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
- The reviewed Demazure subcategory page was applied to `content/topics/demazure-subcategories-of-quiver-hecke-modules.md`; the page is now example-ready and publishable. The comparison-map page now uses source notation $\mathfrak B_w$ instead of the unsupported local alias $\mathcal C_{\mathcal B_w}$.
- Validation after applying the Demazure subcategory page: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 51 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
- The 2026-06-01 source-location review for `Affine Objects in Monoidal Categories` and `R-Matrix Renormalization` was completed at `reports/reviews/2026-06-01-affine-r-matrix-prerequisite-source-location-review.md`. No topic page, claim, or source download was changed in that review pass.
- Validation after the affine/R-matrix prerequisite source-location review: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 51 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
- The reviewed affine-object prerequisite page was applied to `content/topics/affine-objects-in-monoidal-categories.md`. At that point, it was example-ready but still incomplete because its parent prerequisite pages `Pro-Categories` and `Graded Monoidal Categories` were title-only.
- Validation after applying the affine-object page: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 51 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
- The reviewed R-matrix renormalization prerequisite page was applied to `content/topics/r-matrix-renormalization.md`. At that point, it was example-ready but still incomplete because `Graded Monoidal Categories` was title-only.
- Validation after applying the R-matrix renormalization page: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 51 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
- The 2026-06-01 report-only prerequisite fillability review was completed at `reports/reviews/2026-06-01-pro-graded-prerequisite-fillability-review.md`. It found that `Pro-Categories` and `Graded Monoidal Categories` can both receive compact definition-ready prerequisite pages from already reviewed Kashiwara-Nakashima 2025 source locations. No topic page, claim, or source download was changed.
- Validation after the pro/graded prerequisite fillability review: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 51 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
- The compact Pro-Categories and Graded Monoidal Categories prerequisite pages were filled from `reports/reviews/2026-06-01-pro-graded-prerequisite-fillability-review.md`. Both pages are now definition-ready and publishable; `Affine Objects in Monoidal Categories` and `R-Matrix Renormalization` are no longer blocked by title-only categorical prerequisites. No claims were added and no source was downloaded.
- Validation after applying the Pro-Categories and Graded Monoidal Categories prerequisite pages: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 51 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
- The 2026-06-01 report-only positive root-object example review was completed at `reports/reviews/2026-06-01-root-object-positive-example-review.md`. It found no clean low-rank standalone example, but it found a safe conditional example: in the $\mathsf d_i(X)>0$ branch, $\widetilde Q_i$ is a root object. No topic page, claim, or source download was changed.
- Validation after the positive root-object example review: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 51 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
- The reviewed conditional root-object example was applied to `content/topics/root-objects-in-localized-categories.md`. The page is now example-ready, but remains incomplete because the `핵심 관점` and `다른 topic들과의 관계` sections are still empty. No claims were added and no source was downloaded.
- Validation after applying the conditional root-object example: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 51 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
- The refreshed 2026-06-01 global wiki review was completed at `reports/reviews/2026-06-01-global-wiki-review.md` after the root-object example pass. It recorded 28 topic pages, 16 publishable topics, 12 incomplete topics, no reader-facing prohibited phrase/raw-notation violations, and a new open backlog item for the remaining sparse `crystal.tex` topic cluster. No papers were downloaded and no claims were added.
- Validation after the refreshed global wiki review: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 51 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
- The refreshed 2026-06-01 notation audit was completed at `reports/reviews/2026-06-01-notation-audit.md`. It found no raw deprecated notation in reader-facing topic pages, but it found that `Localized Crystals` still uses older localized-operator notation and that the notation registry does not yet cover several Kashiwara-Nakashima 2025 symbols. No topic pages were rewritten, no claims were added, and no papers were downloaded.
- `Localized Crystals` is now marked incomplete in `data/topic_maturity.yml` until its operator formulas are normalized against `Localized Root Operators`.
- Status count after the notation audit: 15 topics were marked `publishable`, and 13 topics were marked `incomplete`.
- Validation after the refreshed notation audit: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 51 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
- The 2026-06-01 topic overlap audit was completed at `reports/reviews/2026-06-01-topic-overlap-audit.md`. It found no duplicate topic pages that should be merged, but found duplicated exposition around localized root-operator formulas, the type $A_3$ $\operatorname{CP}$ example, and determinantial-module details on the subcategory page. No topic pages were rewritten, no claims were added, and no papers were downloaded.
- Validation after the topic overlap audit: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 51 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
- The `Localized Crystals` parent page was slimmed after the overlap and notation audits: detailed localized-root-operator formulas now live on `Localized Root Operators`, while `Localized Crystals` keeps the construction-level statement and links to the child operation page. No claims were added and no sources were downloaded.
- `Localized Crystals` is marked publishable again in `data/topic_maturity.yml`; the old operator-notation normalization and parent/child dedup backlog items are closed.
- Status count after slimming `Localized Crystals`: 16 topics were marked `publishable`, and 12 topics were marked `incomplete`.
- Validation after slimming `Localized Crystals`: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 51 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
- The example policy now permits visible examples only when they are verified by an approved source location or checked Sage code. Topic examples must show `검증: 논문 예시`, `검증: Sage 계산`, or `검증: 논문 그림`, and visual examples must come from approved source figures/pages or Sage-generated artifacts.
- Example artifact locations are now documented: Sage code under `scripts/examples/<topic-id>/`, generated images under `content/assets/images/examples/<topic-id>/`, and optional verification reports under `reports/examples/`.
- Validation after implementing the example verification policy: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 52 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
- The report-only example verification label audit was completed at `reports/reviews/2026-06-01-example-verification-label-audit.md`. It found 17 non-empty `기본 예시` sections, 0 existing verification labels, 12 examples ready for `검증: 논문 예시`, 5 examples needing source-location tightening or a Sage verification decision, and no existing Sage/image example artifacts. No topic pages, claims, sources, Sage scripts, or images were changed.
- Validation after the example verification label audit: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 52 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
- The 12 label-ready examples from `reports/reviews/2026-06-01-example-verification-label-audit.md` now display `검증: 논문 예시` directly under the visible example. Source notes were tightened only where needed for `crystal-bases` and `quiver-hecke-subcategories`; no claims, downloads, Sage code, images, or mathematical example rewrites were added.
- Validation after applying example labels: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 52 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
- The report-only source-location tightening for the remaining five visible examples was completed at `reports/reviews/2026-06-01-example-source-location-tightening.md`. It found exact approved-source support for all five examples: `cellular-crystals`, `graded-monoidal-categories`, `pro-categories`, `quiver-hecke-algebras`, and `quiver-hecke-module-categories`. All five can later receive `검증: 논문 예시`; no Sage verification or example removal is needed.
- Validation after the source-location tightening report: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 52 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
- The five tightened examples now display `검증: 논문 예시`, with concise Source notes provenance added for `cellular-crystals`, `pro-categories`, `quiver-hecke-algebras`, and `quiver-hecke-module-categories`. At that point, the 17 visible topic-page examples all had visible paper-verification labels. No example mathematics, claims, downloads, Sage code, or images were added.
- Validation after applying the final five example labels: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 52 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
- Kashiwara-Nakashima 2025 notation registry/glossary coverage was added for $\mathfrak B_w$, $\widetilde Q_i$, $\mathsf d_i$, $\widetilde\Lambda$, $\mathfrak d$, $\nabla$, $\Phi_w$, $\operatorname{CP}$, and $\psi_*$. No topic pages, claims, downloads, or source notes were changed.
- Validation after KN25 notation registry coverage: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 52 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
- The 2026-06-01 report-only root-object viewpoint/relations wording proposal was completed at `reports/reviews/2026-06-01-root-objects-viewpoint-relations-wording.md`. No topic pages, claims, downloads, or source notes were changed.
- Validation after the root-object wording proposal: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 52 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
- The reviewed root-object viewpoint/relations wording was applied to `content/topics/root-objects-in-localized-categories.md`, and hierarchy-based reader navigation was added to `더 읽을 topic`. The page is now marked study-ready and publishable. No claims, examples, downloads, source notes, or formula-level localized-root-operator details were added.
- Current public status count after regenerating `content/maps/topic-status.md`: 17 topics are marked `publishable`, and 11 topics are marked `incomplete`.
- Validation after applying the root-object viewpoint/relations wording: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 52 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
- The 2026-06-01 report-only localized-root-operator example review was completed at `reports/reviews/2026-06-01-localized-root-operator-example-review.md`. It found no clean concrete worked example suitable for `## 기본 예시` in Kashiwara-Nakashima 2025; the A2/A3 computations should remain warnings, not positive examples. No topic pages, claims, downloads, Sage code, images, or source notes were changed.
- Validation after the localized-root-operator example review: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 52 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
- The reviewed localized-root-operator `핵심 관점` wording was applied to `content/topics/localized-root-operators.md`. The `## 기본 예시` section remains intentionally empty. No claims, downloads, source notes, Sage code, images, or examples were added.
- Validation after applying the localized-root-operator viewpoint wording: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 52 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
- The 2026-06-01 report-only localized-root-operator example route decision was completed at `reports/reviews/2026-06-01-localized-root-operator-example-route.md`. It recommends new-source evaluation before Sage/code verification, with `nakashima22-categorified-crystal-localized-quantum-coordinate-rings` as the first candidate. No sources were downloaded, no Sage code was written, no claims were added, and no topic pages were edited.
- Validation after the localized-root-operator example route decision: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 52 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
- The 2026-06-01 report-only Nakashima 2022 localized-root-operator example search was completed at `reports/reviews/2026-06-01-nakashima22-localized-root-operator-example-search.md`. A local arXiv PDF at `inbox/papers2/N22, Categorified crystal structure on localized quantum coordinate rings, arXiv.pdf` was used; no network download was needed. The source gives useful localized-crystal material and Example 9.6, but no direct KN25-style localized-root-operator worked example. No claims, source notes, topic pages, Sage code, images, or visible examples were added.
- Validation after the Nakashima 2022 localized-root-operator example search: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 52 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
- The site readability infrastructure pass removed duplicate body H1 headings from public content, kept Quartz `ArticleTitle` as the title source, disabled the global Graph View, enabled Mermaid rendering, hid empty topic sections, converted `더 읽을 topic` navigation into Korean reader-facing labels, and regenerated Topic Status as grouped readiness sections. No papers were downloaded, no claims were added, and no mathematical topic content was expanded.
- Validation after the site readability infrastructure pass: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including its internal Quartz build over 52 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure. Static public-output checks found one `<h1>` per inspected page and no Graph View component; headless visual verification was limited by the sandbox blocking the Mermaid CDN import used by Quartz.
- The `topic 수정` / `토픽수정` trigger was added. It selects one low-polish-count topic via `scripts/select_topic_for_polish.py`, permits only rational reader-facing sentence/structure edits for that one topic, and records completed passes in `data/topic_polish_log.yml`.
- The root-prerequisite polish pass updated `Root Systems and Weight Lattices`, `Universal Enveloping Algebras`, `Quantum Groups`, `Crystal Bases`, and `Quiver-Hecke Algebras`. The pass shortened learning-order prose and made definition/theorem/structure/interpretation roles more visible without adding claims, sources, examples, or new mathematical facts. Each edited topic now has `polish_count: 1` in `data/topic_polish_log.yml`.
- The report-only Quantum sl2 example support review was completed at `reports/reviews/2026-06-01-quantum-groups-sl2-example-support.md`. It found exact Hong-Kang 2002 support for a compact $U_q(\mathfrak{sl}_2)$ two-dimensional natural-representation example in Example 4.2.1, p.66. No topic page, claim, source download, Sage code, or image was changed.
- Validation after the Quantum sl2 example support review: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 52 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
- The reviewed Hong-Kang 2002 Example 4.2.1 $U_q(\mathfrak{sl}_2)$ two-dimensional natural-representation example was applied to `content/topics/quantum-groups.md`, with `검증: 논문 예시` and a matching final Source notes line. No claims, downloads, Sage code, images, or broader representation material were added.
- `Quantum Groups` is now marked `study-ready` and publishable. Current public status count after regenerating `content/maps/topic-status.md`: 18 topics are marked `publishable`, and 10 topics are marked `incomplete`.
- Validation after applying the Quantum sl2 example: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 52 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
- The report-only Crystal Bases sl2 example support review was completed at `reports/reviews/2026-06-01-crystal-bases-sl2-example-support.md`. It found exact Hong-Kang 2002 support for a compact finite string crystal example from $V(m)$ in Example 4.2.6, pp.68-69, and Section 4.3, p.73. No topic page, claim, source download, Sage code, or image was changed.
- Validation after the Crystal Bases sl2 example support review: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 52 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
- The reviewed Hong-Kang 2002 finite string crystal example for $V(m)$ was applied to `content/topics/crystal-bases.md`, with `검증: 논문 예시` and matching final Source notes lines. The Hong-Kang source note now records that `Crystal Bases` uses Example 4.2.6 and Section 4.3 for this example, bringing the visible verified example count to 18. No claims, downloads, Sage code, images, or Theorems 4.3.1-4.3.2 were added.
- Validation after applying the Crystal Bases finite string example: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 52 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
- The report-only Crystal Bases rank-two example need review was completed at `reports/reviews/2026-06-01-crystal-bases-rank-two-example-need-review.md`. It reviewed Kashiwara 1993 Examples 2.2.5-2.2.7 and decided not to add them to the main `Crystal Bases` page now, because they are coordinate descriptions of $B(\infty)$ in rank two rather than a simple first study example. No topic page, claim, source download, Sage code, or image was changed.
- Validation after the Crystal Bases rank-two example need review: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 52 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
- The `topic 수정` trigger polished `Cellular Crystals`: the overview and setup now read more directly, the English prerequisite sentence was converted to Korean reader prose, and `기본 성질` now separates definition-level facts, theorem-level facts, and interpretation. No claims, downloads, new examples, Sage code, images, or topic creation were involved.
- Validation after the `Cellular Crystals` polish pass: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 52 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
- The `topic 수정` trigger polished `Localized Crystals`: the overview now emphasizes category-level simple objects as vertices, the remaining English prerequisite sentence was converted to Korean reader prose, and `기본 성질` now separates construction-level facts, comparison facts, and consequences. No claims, downloads, new examples, Sage code, images, or topic creation were involved.
- Validation after the `Localized Crystals` polish pass: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 52 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
- The `topic 수정` trigger polished `Quiver-Hecke Category Localization`: the overview now emphasizes that the monoidal subcategory, not the algebra itself, is localized; the $A_3$ example was slimmed to this page's localization role; and `기본 성질` now separates localization data, category-level facts, and crystal use. No claims, downloads, new examples, Sage code, images, or topic creation were involved.
- Validation after the `Quiver-Hecke Category Localization` polish pass: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 52 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
- The `topic 수정` trigger polished `Root Objects in Localized Categories`: the page now states the object-level role of root objects more directly, the core viewpoint is split into shorter paragraphs, and `기본 성질` now separates duality stability from simple-root-object cautions. No claims, downloads, new examples, Sage code, images, or topic creation were involved.
- Validation after the `Root Objects in Localized Categories` polish pass: `git diff --check` passed; `python3 scripts/run_all_checks.py` passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 52 content files; standalone `npx quartz build` failed with the known Node heap out-of-memory failure.
- KKOP21 was processed from the user-provided local PDF and staged at `content/assets/pdfs/kkop21-localizations-quiver-hecke-algebras.pdf`. The source note `content/sources/papers/kkop21-localizations-quiver-hecke-algebras.md` was created, six claims were added, `Category Localization` was expanded to a source-backed example-ready page, and `Quiver-Hecke Category Localization` now points explicitly to that prerequisite.
- KKKO15 was processed from the user-provided local PDF and staged at `content/assets/pdfs/kkko15-simplicity-heads-socles-tensor-products.pdf`. The source note `content/sources/papers/kkko15-simplicity-heads-socles-tensor-products.md` was created.
- `Normal Sequences` was expanded from title-only to definition-ready using KN25 Definition 4.8, Lemmas 4.9-4.11, Proposition 4.12, and KKKO15 Theorem 3.2. Four claims were added. The example section remains omitted because no compact verified example was selected.
- `Head Simplicity of Convolutions` was expanded from title-only to definition-ready using KKKO15 Theorem 3.2, KKKO15 Corollaries 3.3-3.4, and KN25 Section 4.5. Three claims were added. The example section remains omitted because no compact verified worked example was selected.

## Single Safest Next Task

### Fill Shuffle Lemmas For Quiver-Hecke Modules

- Action type: `existing-source expansion`
- New source required: no.
- User approval required: no if continuing the current broad study pass.
- Why it matters: `Head Simplicity of Convolutions` now points to the remaining theorem-level child topic needed before localized-root-operator arguments can be read smoothly.
- Likely files to inspect:
  - `content/topics/shuffle-lemmas-for-quiver-hecke-modules.md`
  - `content/topics/head-simplicity-of-convolutions.md`
  - `content/sources/papers/kashiwara-nakashima25-crystal-structure-localized-quantum-unipotent-coordinate-category.md`
- Expected mathematical benefit: fills the next exact lemma layer relating head/socle behavior, restrictions, and the combinatorics needed by localized crystal constructions.
- Risk level: medium, because the statements must keep KN25's hypotheses and functor notation explicit and examples should stay empty unless verified.
- Exact prompt to paste:

```text
Fill only the statement/setup layer of Shuffle Lemmas for Quiver-Hecke Modules from Kashiwara-Nakashima 2025 Section 4.7 and immediately needed preceding notation. Add no example unless paper-verified, add at most 4 claims, and leave unsupported sections empty.
```

## Alternatives

### 1. Find A Head-Convolution Example

- Action type: `existing-source expansion`
- New source required: no.
- User approval required: yes before adding visible example text.
- Why it matters: `Head Simplicity of Convolutions` is definition-ready but remains incomplete because it has no compact paper-verified worked example.
- Likely files to inspect:
  - `content/topics/head-simplicity-of-convolutions.md`
  - `content/sources/papers/kkko15-simplicity-heads-socles-tensor-products.md`
  - `content/sources/papers/kashiwara-nakashima25-crystal-structure-localized-quantum-unipotent-coordinate-category.md`
- Expected mathematical benefit: makes the theorem easier to learn without inventing a toy example.
- Risk level: medium
- Exact prompt to paste:

```text
Using only KKKO15 and Kashiwara-Nakashima 2025, review whether there is a compact paper-verified example suitable for content/topics/head-simplicity-of-convolutions.md. Report only; do not edit topic pages, add claims, or create images.
```

### 2. Evaluate KKOP Localization Parts II And III

- Action type: `new-source intake`
- New source required: yes, but local PDFs are already available.
- User approval required: no if continuing the current broad study pass; otherwise ask before intake.
- Why it matters: Parts II and III may be needed for deeper localization comparison facts, but they should not be ingested until a precise topic need is identified.
- Likely files to inspect:
  - `inbox/papers2/KKOP23, Localizations for quiver Hecke algebras II, PLMS, arxiv ver.pdf`
  - `inbox/papers2/KKOP24, Localizations for quiver Hecke algebras III, Math Ann, arxiv ver.pdf`
  - `content/topics/quiver-hecke-category-localization.md`
  - `content/topics/localized-crystals.md`
- Expected mathematical benefit: prepares stronger localization machinery only if later localized-crystal proofs need it.
- Risk level: medium
- Exact prompt to paste:

```text
Review the local KKOP Part II and Part III PDFs for exact localization comparison statements needed by the localized-crystal path. Report first; do not add claims or rewrite pages until exact statements are selected.
```

### 3. Run `topic 수정`

- Action type: `topic-page polishing`
- New source required: no.
- User approval required: no if the trigger is invoked directly.
- Why it matters: polish passes continue improving publishable pages without changing mathematical scope.
- Likely files to inspect:
  - `scripts/select_topic_for_polish.py`
  - `data/topic_polish_log.yml`
- Expected mathematical benefit: improves reader-facing clarity while respecting source boundaries and the no-forced-completion rule.
- Risk level: low
- Exact prompt to paste:

```text
topic 수정
```

## Ranking Basis

- Mathematical importance: shuffle lemmas are the next theorem-level bridge from head/socle simplicity toward localized root-operator and crystal-comparison arguments.
- Current page weakness: `Shuffle Lemmas for Quiver-Hecke Modules` is still title-only.
- Dependency value: filling it reduces one of the last blank intermediate layers in the `crystal.tex` study path.
- Source availability: KN25 is already staged/source-noted.
- Hallucination risk: medium unless the next pass keeps hypotheses explicit and omits examples without verification.

<!-- NEEDS-HUMAN-REVIEW -->

Keep future work focused on small, source-backed topic improvements and clearly recorded gaps.
