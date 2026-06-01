# 2026-06-01 Topic Overlap Audit

This report is advisory. It proposes edits but does not authorize topic-page rewrites, source download, source intake, or claim additions.

## Scope

Reviewed topic pages and hierarchy metadata for cases where two pages are effectively explaining the same concept, repeating the same example, or mixing parent-topic exposition with child-topic details.

No topic pages were rewritten. No claims were added. No papers were downloaded.

## Summary

The wiki does not have obvious duplicate topic pages that should be merged. The current hierarchy is mostly mathematically meaningful: broad prerequisite pages, category-level pages, object-family pages, operation pages, map pages, and theorem pages are distinct.

The main issue is not duplicate topics but duplicated exposition:

- parent pages sometimes include child-page formulas;
- the same $A_3$ localized-crystal example appears at several levels;
- some pages repeat determinantial-module facts that belong more naturally on `Determinantial Modules`;
- some low-level prerequisite pages restate enough notation to be readable, but should be kept compact during later polishing.

## High-Priority Findings

### 1. `Localized Crystals` duplicates child-page operator formulas

Files involved:

- `content/topics/localized-crystals.md`
- `content/topics/localized-root-operators.md`
- `content/topics/root-objects-in-localized-categories.md`
- `content/topics/r-matrix-renormalization.md`

Issue: `Localized Crystals` is a parent construction page, but it currently states the localized root-operator formulas in detail. The dedicated child page `Localized Root Operators` already contains the setup, $\widetilde Q_i$, $\mathsf d_i$, $\widetilde\Lambda$, $\mathfrak d$, $\nabla$, $\mathscr D$, and the formulas for $\widetilde E_i,\widetilde F_i,\widetilde E_i^*,\widetilde F_i^*$.

This creates two problems:

- it duplicates the child page;
- it makes the parent page harder to maintain, as shown by the notation mismatch found in the notation audit.

Proposed fix: slim `Localized Crystals` so it defines the crystal structure at the construction level:

- keep $\operatorname{Irr}(\widetilde{\mathcal C}_w)$;
- say that the crystal operators are the maps defined in `Localized Root Operators`;
- keep Theorem 6.13 and the comparison with cellular crystals;
- remove or compress the full operator formulas from the parent page.

Then keep all explicit formulas on `Localized Root Operators`.

Requires new source: no.

Requires user approval: yes.

### 2. The same $A_3$ / $\operatorname{CP}$ example appears at too many levels

Files involved:

- `content/topics/quiver-hecke-category-localization.md`
- `content/topics/localized-crystals.md`
- `content/topics/crystal-comparison-map.md`
- `content/topics/cellular-crystals.md`

Issue: the $A_3$ example with $w=s_2w_0=s_1s_2s_3s_2s_1$, four clusters, frozen/determinantial objects, and $\operatorname{CP}$ appears in multiple pages. The detailed example belongs most naturally on `Crystal Comparison Map`, because that page actually studies $\operatorname{CP}$.

The other pages need only the part matching their own topic:

- `Quiver-Hecke Category Localization`: use the example only to show the localized category $\widetilde{\mathcal C}_w$ and inverted determinantial objects.
- `Localized Crystals`: use the example only to say that localized simple objects can be compared with a cellular crystal.
- `Cellular Crystals`: use the example only as motivation for the target combinatorial model.
- `Crystal Comparison Map`: keep the actual $\operatorname{CP}$ coordinate formula.

Proposed fix: make `Crystal Comparison Map` the single detailed home for the $A_3$ formula. In the other pages, replace repeated example details with one compact sentence and a link to `Crystal Comparison Map`.

Requires new source: no.

Requires user approval: yes.

### 3. `Quiver-Hecke Subcategories` repeats determinantial-module details

Files involved:

- `content/topics/quiver-hecke-subcategories.md`
- `content/topics/determinantial-modules.md`

Issue: `Quiver-Hecke Subcategories` correctly defines $\mathcal C_w$, $\mathcal C_{*,v}$, and $\mathcal C_{w,v}$. It also states that the family
$$
M(w_{\le k}\Lambda,v_{\le k}\Lambda)
$$
lies in $\mathcal C_{w,v}$ and strongly commutes. That material is more naturally centered on `Determinantial Modules`, where the family is defined and explained.

Proposed fix: keep only the containment role on `Quiver-Hecke Subcategories`:

- "Determinantial modules provide important objects inside $\mathcal C_{w,v}$."

Move the indexed-family and strong-commutation emphasis to `Determinantial Modules`, where it already belongs.

Requires new source: no.

Requires user approval: yes.

## Medium-Priority Findings

### 4. `Category Localization` and `Quiver-Hecke Category Localization` are not duplicates, but the boundary is fragile

Files involved:

- `content/topics/category-localization.md`
- `content/topics/quiver-hecke-category-localization.md`

Issue: `Category Localization` is intentionally a provisional parent topic. It currently uses the quiver-Hecke instance as its only visible schematic picture. That is acceptable while the page is a stub, but if expanded later it should not become a second version of `Quiver-Hecke Category Localization`.

Proposed fix: when a general localization source is approved, rewrite `Category Localization` around the general construction and keep the quiver-Hecke instance as a short example only.

Requires new source: yes.

Requires user approval: yes.

### 5. `Cellular Crystals` repeats basic crystal notation, but this is currently acceptable

Files involved:

- `content/topics/crystal-bases.md`
- `content/topics/cellular-crystals.md`
- `content/topics/crystal-comparison-map.md`

Issue: `Cellular Crystals` restates elementary crystal notation and tensor-product coordinates. Some overlap with `Crystal Bases` is necessary because the cellular-crystal definition is a tensor product of elementary crystals. The page is not a duplicate.

Proposed fix: during later polishing, keep only the local data needed to define $\mathcal B_w$ and link back to `Crystal Bases` for the general tensor-product rule.

Requires new source: no.

Requires user approval: yes.

### 6. `Affine Objects`, `R-Matrix Renormalization`, and `Graded Monoidal Categories` overlap by design

Files involved:

- `content/topics/graded-monoidal-categories.md`
- `content/topics/affine-objects-in-monoidal-categories.md`
- `content/topics/r-matrix-renormalization.md`

Issue: these pages all mention grading, affinizations, rational centers, and R-matrix degrees. This is not a merge candidate: each page is a different layer.

- `Graded Monoidal Categories`: ambient category structure.
- `Affine Objects`: $z$-adic object/family layer.
- `R-Matrix Renormalization`: morphism and degree layer.

Proposed fix: no merge. Keep cross-links and avoid moving detailed renormalized R-matrix formulas into `Affine Objects`.

Requires new source: no.

Requires user approval: no unless topic prose is edited.

### 7. `Quantum Coordinate Rings` and `Monoidal Categorification` share bridge language but are not duplicates

Files involved:

- `content/topics/quantum-coordinate-rings.md`
- `content/topics/monoidal-categorification.md`
- `content/topics/determinantial-modules.md`

Issue: both pages discuss the passage from category-level data to coordinate-ring-level targets. This overlap is necessary, but future edits should keep the level distinction explicit:

- `Quantum Coordinate Rings`: algebra target such as $A_q(\mathfrak n(w))$.
- `Monoidal Categorification`: mechanism using $K_0(\mathcal C)$.
- `Determinantial Modules`: object-family whose classes are compared with coordinate-ring elements.

Proposed fix: no merge. Keep the existing level separation and do not identify $A_{w,v}$ with $A_q(\mathfrak n(w))$ without a separate bridge review.

Requires new source: no.

Requires user approval: yes before topic-page bridge prose.

## Suggested Edit Order

1. Normalize and slim `Localized Crystals`: remove detailed operator formulas from the parent page and point to `Localized Root Operators`.
2. Make `Crystal Comparison Map` the only detailed home for the $A_3$ $\operatorname{CP}$ coordinate formula.
3. Slim determinantial-module facts on `Quiver-Hecke Subcategories`, leaving detailed family and strong-commutation discussion to `Determinantial Modules`.
4. Add Kashiwara-Nakashima notation registry entries before any more KN25 topic polishing.
5. Later, after a source is approved, fill `Category Localization` as a genuinely general parent page.

## Backlog Updates

Recommended new backlog items:

- `review-2026-06-01-localized-crystals-child-page-dedup`
- `review-2026-06-01-a3-cp-example-single-home`
- `review-2026-06-01-subcategories-determinantial-detail-dedup`
- `review-2026-06-01-category-localization-boundary`

## Validation

- `git diff --check`: passed.
- `python3 scripts/run_all_checks.py`: passed, including frontmatter, claims, topics, edges, generated maps, generated topic status, link validation, and the internal Quartz build over 51 content files.
- `npx quartz build`: failed with the known standalone Node heap out-of-memory failure. The Quartz build inside `run_all_checks.py` passed.
