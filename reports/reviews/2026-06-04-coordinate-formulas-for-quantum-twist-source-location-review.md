# Coordinate Formulas For Quantum Twist Source-Location Review

Date: 2026-06-04

## Scope

This is a report-only review for `Coordinate Formulas for Quantum Twist on Localized Crystals`.

Files inspected:

- `inbox/papers2/Tex/JP25, Crystals and quantum twist automorphisms, arXiv/CT.tex`
- `content/topics/08-localization-of-categories/coordinate-formulas-for-quantum-twist-on-localized-crystals.md`
- `content/sources/papers/jp25-crystals-quantum-twist-automorphisms.md`
- `reports/reviews/2026-06-04-left-right-g-vectors-source-location-review.md`
- `reports/roadmap/next-actions.md`

No paper was downloaded. No topic page, claim, source note, example, theorem statement, coordinate formula, Sage code, image, or new topic was added.

## Verdict

JP25 gives exact source support for the theorem-level coordinate formulas relating quantum twist on the localized coordinate-ring side, the crystal permutation on \(\widetilde B(w)\), localized PBW coordinates, localized string coordinates, and left/right \(g\)-vectors.

The source support is strong, but the safe topic-page scope is still narrow. The theorem statement is formula-heavy and depends on several pages that are only orientation-level. A later edit may fill a compact orientation page explaining what the theorem compares, but it should not yet display the five formulas of JP25 Theorem 3.2 or the type \(A_2\) example.

## Exact Source Locations

### Conceptual Role In The Introduction

- `CT.tex:1011-1020`: introduces the crystal-level counterpart \(\mathfrak D_w\), the localized PBW and string parametrizations, the bijection between them, and says that the main theorem describes \(\mathfrak D_w\) through this bijection and the two triangular matrices \(M_{\mathbf i}\), \(N_{\mathbf i}\). It also identifies the \(g\)-vector sets as the bridge from the quiver-Hecke side.

This range is safe for a meaning-level orientation paragraph. It should not be used as a substitute for the theorem statement.

### Crystal-Level Twist Permutation

- `CT.tex:1546-1555`: defines the permutation \(\mathfrak D_w\) on \(\widetilde B(w)\) by the commutative diagram involving localized simple objects, localized upper global basis elements, right duality, and the quantum twist automorphism.

This supports the setup phrase "crystal-level counterpart of quantum twist." It should stay connected to `Localized Crystals` and `Quantum Twist Automorphisms`.

### Coordinate Setup

- `CT.tex:1687-1695`: fixes \(w\), a reduced expression \(\mathbf i\), recalls localized PBW and string parametrizations, and defines the PBW-string bijection \(\psi_{\mathbf i}\). It also records that this bijection is not \(\mathbb Z\)-linear.
- `CT.tex:1697-1713`: recalls left/right \(g\)-vectors on \(\widetilde B(w)\) and the integer-lattice target sets.
- `CT.tex:1717-1738`: defines the matrices \(N_{\mathbf i}\) and \(M_{\mathbf i}\), and states their role in comparing PBW/string coordinates with \(g\)-vector coordinates.
- `CT.tex:1741-1776`: states the proposition giving the maps from \(g\)-vectors to string coordinates and from PBW coordinates to right \(g\)-vectors.
- `CT.tex:1811-1823`: records that the matrices are upper triangular with diagonal entries \(1\), the comparison maps are \(\mathbb Z\)-linear, and the relevant PBW/string parameter sets are integer lattices.

These ranges are prerequisite setup for the theorem. A later orientation page can name these ingredients, but should not reproduce the matrix entries yet.

### The Main Coordinate Formula Theorem

- `CT.tex:1826-1836`: gives the comparison diagram among \(\widetilde B(w)\), localized PBW parameters, localized string parameters, and left/right \(g\)-vector parameter sets.
- `CT.tex:1838-1852`: states the main theorem with five formulas: one comparing left and right \(g\)-vectors, two formulas for the action of \(\mathfrak D_w\) on left/right \(g\)-vectors, one formula for PBW coordinates after \(\mathfrak D_w\), and one formula for string coordinates after \(\mathfrak D_w\).
- `CT.tex:1853-1860`: proves the theorem from the relation between right \(g\)-vectors and left \(g\)-vectors after the crystal duality permutation, together with the comparison diagram.

This is exact theorem support. It should be imported only when the user explicitly approves a theorem-level page edit.

### Warning About Nonlinearity

- `CT.tex:1863-1885`: warns that the PBW-string bijection is not \(\mathbb Z\)-linear and gives a type \(A_3\) counterexample to an invalid simplification.

This is important for avoiding a false formula. It is not yet a visible example candidate because the page does not yet carry the theorem formulas.

### Type \(A_2\) Worked Example

- `CT.tex:1888-1947`: gives a type \(A_2\) example with PBW data, string data, frozen directions, the PBW-string map, the \(N_{\mathbf i}\) and \(M_{\mathbf i}\) matrices, and a relation between left and right \(g\)-vectors.

This is a strong paper-verified example candidate, but it is too formula-dense to import before the theorem statement and notation are stabilized. It should receive a separate example-specific review before visible use.

## What Can Be Used Later

A later topic-page edit may safely add only an orientation page that explains:

- the theorem compares four coordinate languages on the same localized crystal: PBW, string, left \(g\)-vector, and right \(g\)-vector;
- the quantum twist automorphism is read on the crystal side through the permutation \(\mathfrak D_w\);
- the PBW-string bijection is essential and is not linear;
- triangular maps connect PBW/string coordinates with left/right \(g\)-vectors;
- the explicit theorem formulas are deferred until the notation is stable.

The page should remain `orientation` unless the theorem statement is explicitly approved.

## What Should Not Be Used Yet

Do not import into the topic page yet:

- the five formulas of JP25 Theorem 3.2;
- the full comparison diagram;
- explicit matrix entries for \(M_{\mathbf i}\) and \(N_{\mathbf i}\);
- explicit formulas for \(\mathcal M_{\mathbf i}\), \(\mathcal N_{\mathbf i}\), or \(\psi_{\mathbf i}\);
- the type \(A_2\) worked example;
- the type \(A_3\) warning as a visible example;
- the proof of the theorem;
- minuscule, Young diagram, periodicity, or SageMath material.

## Prerequisite Gaps

The main blockers are:

- `Localized PBW Parametrizations`, `Localized String Parametrizations`, and `Left and Right g-Vectors` are orientation-level, not definition-ready.
- `Quantum Cluster Algebras` does not yet explain pointed/copointed bases, dominance order, or \(g\)-vectors.
- `Quantum Unipotent Coordinate Rings` and `Quantum Minors and Frozen Variables` are still too thin for the theorem setup.
- The type \(A_2\) example needs a separate review to decide whether it should appear as the first visible example or remain in source notes.

## Recommended Next Step

Use this report to fill only a compact orientation page for `Coordinate Formulas for Quantum Twist on Localized Crystals`.

Recommended prompt:

```text
Using reports/reviews/2026-06-04-coordinate-formulas-for-quantum-twist-source-location-review.md, fill only a compact orientation page for Coordinate Formulas for Quantum Twist on Localized Crystals. Do not add theorem statements, coordinate formulas, matrix formulas, examples, claims, source notes, Sage code, images, or new topics.
```
