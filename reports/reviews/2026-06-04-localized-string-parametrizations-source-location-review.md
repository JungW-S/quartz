# Localized String Parametrizations Source-Location Review

Date: 2026-06-04

## Scope

This is a report-only review for `Localized String Parametrizations`.

Files inspected:

- `inbox/papers2/Tex/JP25, Crystals and quantum twist automorphisms, arXiv/CT.tex`
- `content/sources/papers/jp25-crystals-quantum-twist-automorphisms.md`
- `reports/reviews/2026-06-04-localized-pbw-parametrizations-source-location-review.md`
- `content/topics/08-localization-of-categories/localized-string-parametrizations.md`

No paper was downloaded. No topic page, claim, source note, example, theorem statement, coordinate formula, Sage code, image, or new topic was added.

## Verdict

JP25 gives exact source locations for the localized string parametrization of the localized crystal.

The safe scope is narrow:

- explain that a reduced expression of \(w\) is fixed;
- recall that ordinary string coordinates are first defined on \(B(w)\) using successive Kashiwara operators and the functions \(\varepsilon_i\);
- record that JP25 proves the resulting map on \(B(w)\) is bijective;
- explain that frozen crystal elements contribute fixed string direction vectors;
- explain that localized string coordinates extend ordinary string coordinates by allowing integer shifts in those frozen directions;
- record that this gives a bijective parametrization of \(\mathcal B(w)\) with respect to the chosen reduced expression.

This is enough for an orientation page, and possibly for a carefully bounded definition-ready page later. It is not enough for a study-ready page because the wiki still lacks a full ordinary string parametrization prerequisite, and the visible example should not be imported before PBW/string/g-vector comparison is prepared.

## Exact Source Locations

### String Coordinates On \(B(w)\)

- `CT.tex:1600-1608`: defines \(\operatorname{STR}_{\mathbf i}(b)\) for \(b\in B(w)\) using the recursive string-coordinate procedure and defines the image set \(\mathcal S_{\mathbf i}(w)\).

### Bijectivity On \(B(w)\)

- `CT.tex:1611-1625`: states the lemma that the recursive lowering/extraction process reaches the unit element and that the map from \(B(w)\) to \(\mathcal S_{\mathbf i}(w)\) is bijective.
- `CT.tex:1626-1649`: proves this using dual PBW root vectors, quantum unipotent minors, Kashiwara operators, and generation of \(A_q(\mathfrak n(w))\). This proof is too dense for the first orientation page.
- `CT.tex:1651-1652`: notes an alternative proof route through quiver-Hecke algebras. This should remain out of the topic page unless that route is separately reviewed.

### Frozen String Directions

- `CT.tex:1655-1659`: defines \(S_j=\operatorname{STR}_{\mathbf i}(\mathfrak z_j)\) and gives a formula for its coordinates using simple coroot pairings and the tail of the reduced expression.

### Extension To The Localized Crystal

- `CT.tex:1660-1665`: extends string coordinates from \(B(w)\) to localized elements of \(\mathcal B(w)\) by adding integer frozen-direction shifts and states independence from the chosen expression of the localized element.

### Localized String Parameter Set

- `CT.tex:1666-1675`: defines the localized string parameter set and the bijection from \(\mathcal B(w)\); the final sentence names this set the string parametrization of the localized crystal with respect to the chosen reduced expression.

### PBW-String Bridge

- `CT.tex:1691-1695`: defines the bijection \(\psi_{\mathbf i}\) from localized PBW parameters to localized string parameters and records that it is not \(\mathbb Z\)-linear.

This bridge is important, but it should not be imported into `Localized String Parametrizations` as formula-level content yet. It belongs after both the PBW and string orientation pages exist, and before any \(g\)-vector or twist-formula page is written.

## What Can Be Used Later

A later topic-page edit may safely add:

- a compact setup paragraph fixing \(w\), a reduced expression, \(B(w)\), and \(\mathcal B(w)\);
- a level-separated explanation of ordinary string coordinates versus localized string coordinates;
- a statement that string coordinates are built from repeated Kashiwara-operator extraction;
- a statement that frozen elements add integer directions to ordinary string coordinates;
- a brief note that the parametrization depends on the reduced expression;
- a relation paragraph pointing back to `Localized PBW Parametrizations` and forward to `Left and Right g-Vectors`.

The page should remain `orientation` until ordinary string parametrization and frozen-direction prerequisites are readable enough.

## What Should Not Be Used Yet

Do not import into `Localized String Parametrizations` yet:

- JP25 Theorem 3.2 formulas;
- the full PBW/string/g-vector comparison diagram;
- the type \(A_2\) coordinate example;
- matrices, piecewise-linear maps, or nonlinear \(\psi_{\mathbf i}\) formulas as visible exposition;
- the proof of the string bijectivity lemma;
- minuscule, Young diagram, periodicity, or SageMath material.

Those belong after `Left and Right g-Vectors` and the coordinate-formula page are prepared.

## Prerequisite Gaps

The main blockers are:

- `Localized PBW Parametrizations` is only orientation-level.
- There is no ordinary string parametrization prerequisite topic.
- `Quantum Unipotent Coordinate Rings` and `Quantum Minors and Frozen Variables` are still stubs.
- `Left and Right g-Vectors` is still a stub.

For a narrow orientation page, these gaps can remain recorded in metadata. For a definition-ready page, at least ordinary string parametrization and frozen directions should be explained more fully.

## Recommended Next Step

Use this report to fill only a compact orientation page for `Localized String Parametrizations`, or first review whether ordinary string parametrization needs its own prerequisite topic.

Recommended prompt:

```text
Using reports/reviews/2026-06-04-localized-string-parametrizations-source-location-review.md, fill only a compact orientation page for Localized String Parametrizations. Keep missing prerequisite definitions out of the page body. Do not add claims, examples, theorem statements, Theorem 3.2 formulas, PBW/string/g-vector formulas, Sage code, images, source notes, or new topics.
```
