# Localized PBW Parametrizations Source-Location Review

Date: 2026-06-04

## Scope

This is a report-only review for `Localized PBW Parametrizations`.

Files inspected:

- `inbox/papers2/Tex/JP25, Crystals and quantum twist automorphisms, arXiv/CT.tex`
- `content/sources/papers/jp25-crystals-quantum-twist-automorphisms.md`
- `reports/reviews/2026-06-03-jp25-localized-crystals-binfinity-route.md`
- `content/topics/08-localization-of-categories/localized-pbw-parametrizations.md`

No paper was downloaded. No topic page, claim, source note, example, theorem statement, coordinate formula, Sage code, image, or new topic was added.

## Verdict

JP25 gives a precise source location for the localized PBW parametrization of the localized crystal.

The safe scope is narrow:

- explain that a reduced expression of \(w\) is fixed;
- recall that ordinary PBW parametrization is first used on \(B(w)\);
- explain that frozen crystal elements contribute fixed PBW direction vectors;
- explain that localized PBW coordinates extend ordinary PBW coordinates by allowing integer shifts in those frozen directions;
- record that this gives a bijective parametrization of \(\mathcal B(w)\) with respect to the chosen reduced expression.

This is enough for an orientation or carefully bounded definition page. It is not enough for a full study-ready page because the wiki still lacks readable prerequisite pages for ordinary PBW parametrization, quantum unipotent coordinate rings, and frozen quantum minors.

## Exact Source Locations

### Setup

- `CT.tex:1559-1563`: fixes a reduced expression \(\mathbf i=(i_1,\ldots,i_m)\in R(w)\) and announces PBW and string parametrizations of \(\mathcal B(w)\).

### Ordinary PBW Input

- `CT.tex:1569-1573`: defines the PBW coordinate of \(b\in B(w)\) through the upper global basis element and records the ordinary PBW parametrization map from \(B(w)\).
- This line cites Lusztig's book for the ordinary PBW parametrization. A topic page should not pretend that JP25 is a beginner source for ordinary PBW theory.

### Frozen PBW Directions

- `CT.tex:1575-1580`: defines the PBW vector \(P_j\) attached to a frozen crystal element and records the coordinate pattern for that vector.
- This passage cites Kimura and KKOP18. A future full exposition should either keep this as a JP25-recorded fact or evaluate those sources before expanding the background.

### Extension To The Localized Crystal

- `CT.tex:1581-1586`: extends PBW coordinates from \(B(w)\) to elements of \(\mathcal B(w)\) by adding integer frozen-direction shifts, and states independence from the chosen expression of the localized element.

### Localized PBW Parameter Set

- `CT.tex:1587-1596`: defines the localized PBW parameter set and the bijection from \(\mathcal B(w)\); the final sentence names this set the PBW parametrization of the localized crystal with respect to the chosen reduced expression.

## What Can Be Used Later

A later topic-page edit may safely add:

- a compact setup paragraph fixing \(w\), a reduced expression, \(B(w)\), and \(\mathcal B(w)\);
- a level-separated explanation of ordinary PBW coordinates versus localized PBW coordinates;
- a statement that frozen elements add integer directions to the ordinary nonnegative PBW coordinates;
- a brief note that the parametrization depends on the reduced expression;
- a relation paragraph pointing to `Localized String Parametrizations` and `Left and Right g-Vectors`.

The page should remain `orientation` or at most `definition-ready` until the missing prerequisites are filled.

## What Should Not Be Used Yet

Do not import into `Localized PBW Parametrizations` yet:

- JP25 Theorem 3.2 formulas;
- the PBW/string/g-vector comparison diagram as a theorem-level statement;
- the type \(A_2\) coordinate example;
- matrices, piecewise-linear maps, or the nonlinear \(\psi_{\mathbf i}\) warning as visible exposition;
- minuscule, Young diagram, periodicity, or SageMath material.

Those belong after `Localized String Parametrizations` and `Left and Right g-Vectors` are readable.

## Prerequisite Gaps

The main blockers are:

- `Quantum Unipotent Coordinate Rings` is still a stub.
- `Quantum Minors and Frozen Variables` is still a stub.
- There is no ordinary PBW parametrization topic for \(B(w)\) or \(B(\infty)\).
- `Localized String Parametrizations` and `Left and Right g-Vectors` are still stubs.

For a narrow orientation page, these gaps can be linked and recorded. For a definition-ready page, they should be addressed first or explicitly kept outside the visible exposition.

## Recommended Next Step

Use this report to fill only a compact orientation page for `Localized PBW Parametrizations`, or first review the coordinate-ring prerequisites if the goal is a definition-ready page.

Recommended prompt:

```text
Using reports/reviews/2026-06-04-localized-pbw-parametrizations-source-location-review.md, fill only a compact orientation page for Localized PBW Parametrizations. Keep missing prerequisite definitions out of the page body. Do not add claims, examples, theorem statements, Theorem 3.2 formulas, PBW/string/g-vector formulas, Sage code, images, source notes, or new topics.
```
