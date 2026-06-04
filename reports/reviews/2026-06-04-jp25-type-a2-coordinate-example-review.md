# JP25 Type A2 Coordinate Example Review

Date: 2026-06-04

## Scope

This is a report-only review of the type \(A_2\) example in JP25 for possible later use on `Coordinate Formulas for Quantum Twist on Localized Crystals`.

Files inspected:

- `inbox/papers2/Tex/JP25, Crystals and quantum twist automorphisms, arXiv/CT.tex`
- `reports/reviews/2026-06-04-coordinate-formulas-for-quantum-twist-source-location-review.md`
- `content/topics/08-localization-of-categories/coordinate-formulas-for-quantum-twist-on-localized-crystals.md`
- `data/research_queue.yml`
- `reports/roadmap/next-actions.md`

No paper was downloaded. No topic page, claim, source note, theorem statement, coordinate formula, matrix formula, example, Sage code, image, or new topic was added.

## Verdict

The JP25 type \(A_2\) example is a valid paper-verified example candidate, but it is not suitable as the first visible example in the current orientation-level topic page.

The reason is not source weakness. The source is strong. The problem is readability and dependency order:

- the example assumes the theorem-level comparison setup;
- it uses localized PBW and string parameter sets;
- it uses frozen directions;
- it uses the PBW-string map explicitly;
- it uses the comparison matrices;
- it ends with a left/right \(g\)-vector relation.

Putting this directly into the current page would force several formulas into a page whose theorem statement is intentionally absent. It should be deferred until the theorem statement and notation boundary are explicitly approved.

## Exact Source Locations

### Setup And Coordinate Names

- `CT.tex:1888-1896`: fixes type \(A_2\), the reduced expression \(\mathbf i=(1,2,1)\), and names PBW data, string data, right \(g\)-vector data, and left \(g\)-vector data.

This is useful later for a compact example setup, but only after the page has introduced the theorem notation.

### Seed Objects And Frozen Directions

- `CT.tex:1898-1904`: identifies the three quantum minors and determinantial modules in the example and records which upper-global-basis elements are frozen.
- `CT.tex:1905-1915`: gives the frozen PBW directions, frozen string directions, and the localized PBW/string parameter sets.

This is the most educational part of the example, but it depends on the reader already understanding localized PBW/string parametrizations and frozen directions.

### PBW-String Map

- `CT.tex:1917-1924`: gives the explicit PBW-string map in type \(A_2\), records its nonlinearity, and records its compatibility with frozen-direction shifts.

This is valuable, but it is formula-level content. It should not be imported before the theorem statement is approved.

### Comparison Matrices And Left/Right \(g\)-Vectors

- `CT.tex:1925-1944`: gives the matrices \(N_{\mathbf i}\), \(M_{\mathbf i}\), their inverses, the corresponding maps, and a displayed relation between right and left \(g\)-vectors.

This is too dense for a first visible example on the current page. It belongs after the theorem formulas or in a separate worked-example page.

## Recommended Use

Do not add this example to the current orientation page.

Later, after theorem-level content is approved, use it in one of two ways:

1. As a compact paper-verified example under `Coordinate Formulas for Quantum Twist on Localized Crystals`, but only if the page already displays the theorem statement and notation.
2. As a separate worked-example topic if the theorem page becomes too dense.

If used visibly, the example should be split into short stages:

- first show the type \(A_2\) setup and coordinate names;
- then show frozen PBW/string directions;
- then show the PBW-string map;
- only after that show the matrix and \(g\)-vector relation.

## What Should Not Be Done Yet

Do not yet import:

- the type \(A_2\) coordinate formulas;
- the explicit PBW-string map;
- the matrices \(M_{\mathbf i}\), \(N_{\mathbf i}\), or their inverses;
- the final left/right \(g\)-vector relation;
- a visual figure generated without Sage or source-derived verification;
- any Sage reconstruction unless the code is written and checked separately.

## Prerequisite Gaps

The example remains blocked by:

- no visible theorem statement on the coordinate-formula page;
- no definition-ready page for `Left and Right g-Vectors`;
- only orientation-level pages for localized PBW and localized string parametrizations;
- thin background for quantum cluster algebra \(g\)-vectors, pointed/copointed bases, and dominance order.

## Recommended Next Step

The next safe task is not to import the example. It is to evaluate a focused cluster-theoretic \(g\)-vector source, or to request explicit approval for a theorem-statement edit before using the example.

Recommended prompt:

```text
Evaluate one focused source for cluster-theoretic g-vectors, pointed/copointed bases, and dominance order as prerequisites for Left and Right g-Vectors and the quantum twist coordinate-formula theorem. Do not download or ingest until I approve the exact source.
```
