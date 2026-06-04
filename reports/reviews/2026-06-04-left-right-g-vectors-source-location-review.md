# Left And Right g-Vectors Source-Location Review

Date: 2026-06-04

## Scope

This is a report-only review for `Left and Right g-Vectors`.

Files inspected:

- `inbox/papers2/Tex/JP25, Crystals and quantum twist automorphisms, arXiv/CT.tex`
- `content/topics/08-localization-of-categories/left-and-right-g-vectors.md`
- `content/sources/papers/jp25-crystals-quantum-twist-automorphisms.md`
- `reports/roadmap/next-actions.md`

No paper was downloaded. No topic page, claim, source note, example, theorem statement, coordinate formula, Sage code, image, or new topic was added.

## Verdict

JP25 gives enough source support for a compact orientation page explaining why left and right \(g\)-vectors appear in the localized-crystal coordinate story.

The safe scope is narrow:

- fix a reduced expression \(\mathbf i\) and the corresponding GLS seed;
- explain that the localized upper-global-basis side and localized simple-object side are pointed/copointed with respect to that seed;
- describe \(\mathrm g^{\mathrm L}_{\mathbf i}\) and \(\mathrm g^{\mathrm R}_{\mathbf i}\) as degree/codegree data attached to that seed;
- separate the category-level reading: left multiplication by determinantial seed modules gives the left \(g\)-vector, while right multiplication gives the right \(g\)-vector;
- explain that JP25 extends these \(g\)-vectors to the localized crystal \(\widetilde B(w)\) through upper global basis elements;
- record that the \(g\)-vector sets are identified with an integer lattice after the reduced expression is fixed;
- say only at a meaning level that the PBW, string, and \(g\)-vector coordinate systems are compared by triangular linear maps and a PBW-string bijection.

This is not enough for a definition-ready page unless the wiki also explains the cluster-theoretic background of pointed/copointed bases, dominance order, degree/codegree, and \(g\)-vectors.

## Exact Source Locations

### Seed And Monoidal-Categorification Setup

- `CT.tex:1335-1369`: fixes a reduced expression \(\mathbf i\), defines the GLS seed data for \(A_q(\mathfrak n(w))\), records frozen variables, and passes to the monomial seed in \(\mathcal C_w\).

This range supports the setup paragraph for any future orientation page. It should not be expanded into a full cluster-algebra definition here.

### Left And Right \(g\)-Vectors

- `CT.tex:1371`: says that the bases \(\widetilde G^{\mathrm{up}}(w)\) and \(\widetilde{\mathbf G}(w)\) are pointed/copointed with respect to the seed and that two \(g\)-vectors \(\mathrm g^{\mathrm L}_{\mathbf i}\) and \(\mathrm g^{\mathrm R}_{\mathbf i}\) are well-defined as degree and codegree with respect to the dominance order.

This line is safe for a meaning-level orientation. It relies on external references for the actual definitions, so it should not be used alone to write a complete definition.

### Category-Level Reading

- `CT.tex:1373-1388`: states that for a simple object \(X\), left convolution with determinantial seed-module monomials gives \(\mathrm g^{\mathrm L}_{\mathbf i}(X)\), while right convolution gives \(\mathrm g^{\mathrm R}_{\mathbf i}(X)\).

This is the best source location for explaining why the page has both "left" and "right" in the title. It should be kept as category-level intuition unless the determinantial-module and head-convolution prerequisites are being developed in detail.

### Comparison Lemma Used Later

- `CT.tex:1390-1408`: introduces a lemma used later for comparing \(g\)-vectors on the upper-global-basis side and the simple-object side.

This belongs in source notes or later proof-oriented pages. It is too technical for the first reader-facing orientation page.

### Extension To Localized Crystals

- `CT.tex:1687-1713`: fixes \(w\), \(\mathbf i\), recalls PBW and string parametrizations, defines \(\mathrm g^{\mathrm L}_{\mathbf i}(x)\) and \(\mathrm g^{\mathrm R}_{\mathbf i}(x)\) for \(x\in \widetilde B(w)\) via upper global basis elements, and states that the left and right \(g\)-vector maps are bijections to integer-lattice target sets.

This is the main safe source location for a compact orientation page.

### Linear Comparison Maps

- `CT.tex:1717-1738`: defines the matrices \(N_{\mathbf i}\) and \(M_{\mathbf i}\) and says that the maps from PBW/string coordinates to right/left \(g\)-vectors are described by these matrices.
- `CT.tex:1741-1776`: states the proposition identifying \(g\)-vectors of localized crystal elements with \(g\)-vectors of corresponding localized simple objects, and defines the maps \(\mathcal M_{\mathbf i}\) and \(\mathcal N_{\mathbf i}\).
- `CT.tex:1811-1823`: records that these matrices are upper triangular with diagonal entries \(1\), that the corresponding maps are \(\mathbb Z\)-linear, and that the upper-global-basis and simple-object \(g\)-vectors coincide for the purposes of the paper.

These lines support a relation paragraph, but the explicit matrix formulas should stay out of the first orientation page.

### Coordinate-Formula Layer

- `CT.tex:1826-1860`: gives the comparison diagram and Theorem 3.2 formulas relating left/right \(g\)-vectors, PBW coordinates, string coordinates, and the crystal-level quantum twist.

Do not import this into `Left and Right g-Vectors` yet. It belongs to the theorem-level topic `Coordinate Formulas for Quantum Twist on Localized Crystals` after PBW, string, and \(g\)-vector prerequisites are readable.

### Warnings And Examples

- `CT.tex:1863-1885`: warns that the PBW-string map is not \(\mathbb Z\)-linear and gives a type \(A_3\) counterexample to an invalid simplification.
- `CT.tex:1888-1947`: gives a type \(A_2\) example computing PBW data, string data, matrices, and a relation between left and right \(g\)-vectors.

Do not import these yet. They are examples/formula-level material and require a separate example review before visible use.

## What Can Be Used Later

A later topic-page edit may safely add:

- a compact setup paragraph fixing the reduced expression and seed;
- a short explanation that left/right \(g\)-vectors are seed-dependent coordinate data;
- a category-level paragraph saying left and right refer to which side determinantial seed modules are convolved on;
- a localized-crystal paragraph saying JP25 reads these vectors on \(\widetilde B(w)\) via upper global basis elements;
- a relation paragraph connecting localized PBW coordinates, localized string coordinates, and future twist-coordinate formulas.

The page should remain `orientation` until the cluster-theoretic definition of \(g\)-vectors is sourced from Qin/KK/KKOP or another approved prerequisite source.

## What Should Not Be Used Yet

Do not import into `Left and Right g-Vectors` yet:

- JP25 Theorem 3.2 formulas;
- the full comparison diagram;
- explicit \(M_{\mathbf i}\), \(N_{\mathbf i}\), \(\mathcal M_{\mathbf i}\), or \(\mathcal N_{\mathbf i}\) matrix formulas;
- the type \(A_2\) worked example;
- the type \(A_3\) nonlinearity counterexample as a visible example;
- proof details using the \(\varepsilon_i\) comparison lemma;
- any minuscule, Young diagram, periodicity, or SageMath material.

## Prerequisite Gaps

The main blockers are:

- `Quantum Cluster Algebras` does not yet explain \(g\)-vectors, pointed/copointed bases, or dominance order.
- `Determinantial Modules` and `Normal Sequences` are readable but not enough by themselves to explain the determinantial-seed-module monomials used in JP25.
- `Localized PBW Parametrizations` and `Localized String Parametrizations` are only orientation-level.
- `Coordinate Formulas for Quantum Twist on Localized Crystals` should stay empty until the \(g\)-vector page is at least orientation-level.

## Recommended Next Step

Use this report to fill only a compact orientation page for `Left and Right g-Vectors`.

Recommended prompt:

```text
Using reports/reviews/2026-06-04-left-right-g-vectors-source-location-review.md, fill only a compact orientation page for Left and Right g-Vectors. Keep the exact definition, examples, Theorem 3.2 formulas, PBW/string/g-vector formulas, matrix formulas, Sage code, images, source notes, and new topics out of the page.
```
