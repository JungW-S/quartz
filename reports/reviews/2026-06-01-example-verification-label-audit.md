# Example Verification Label Audit

Date: 2026-06-01

## Scope

This report audits every non-empty `## 기본 예시` section in `content/topics/*.md` against the new example verification policy.

No topic page was rewritten. No claims were added. No sources were downloaded. No Sage code or images were generated.

## Checks

- A visible example must eventually have exactly one label: `검증: 논문 예시`, `검증: Sage 계산`, or `검증: 논문 그림`.
- A visible example must be supported by an approved source location or checked Sage code.
- A visual example must come from an approved source figure/table/page or from checked Sage code.
- Schematic examples under `### 구조 예시` still need paper or Sage verification.

## Summary

- Non-empty `기본 예시` sections found: 17.
- Existing verification labels found: 0.
- Existing Sage example scripts found: 0, excluding README files.
- Existing generated example images found: 0, excluding README files.
- Paper/source-label-ready examples: 12.
- Examples needing source-location tightening or a Sage verification decision before labeling: 5.

No topic currently uses an image in its `기본 예시` section, so no `검증: 논문 그림` case is currently ready.

## Label-Ready Examples

These examples appear label-ready as `검증: 논문 예시` in a later approved topic-page edit. The edit should add the visible label below the example and add or tighten final `Source notes` only as needed.

| Topic | Current example | Existing evidence |
| --- | --- | --- |
| `affine-objects-in-monoidal-categories` | $L(i)=\langle i\rangle$ is affreal | Kashiwara-Nakashima 2025, `crystal.tex:2373-2375`; source-location review `2026-06-01-affine-r-matrix-prerequisite-source-location-review.md`. |
| `crystal-bases` | $T_\lambda$ and elementary crystal $B_i$ | Kashiwara 1993, Examples 1.2.4-1.2.8, pp.842-843. |
| `crystal-comparison-map` | Type $A_3$ comparison-map formula | Kashiwara-Nakashima 2025, `crystal.tex:4819-4873`; example review `2026-06-01-crystal-comparison-map-a3-example-review.md`. |
| `demazure-subcategories-of-quiver-hecke-modules` | Type $A_2$ distinction between $\mathcal C_w$ and $\mathfrak B_w$ | Kashiwara-Nakashima 2025, `crystal.tex:3190-3193`; source-location review `2026-06-01-demazure-subcategories-source-location-review.md`. |
| `dual-canonical-bases` | Unipotent quantum minors in $B^*$ | GLS11, Section 6.2 and Proposition 6.3. |
| `localized-crystals` | Type $A_3$ localized-crystal example pointing to $\operatorname{CP}$ | Kashiwara-Nakashima 2025, Example 9.6; detailed example review recorded for `Crystal Comparison Map`. |
| `quiver-hecke-category-localization` | Type $A_3$ localization/cluster example | Kashiwara-Nakashima 2025, Example 9.6. |
| `quiver-hecke-subcategories` | Type $A_2$ case $\mathcal C_w=R\text{-gmod}$ | Kashiwara-Nakashima 2025 example reviewed in `2026-06-01-quiver-hecke-subcategories-example-review.md`. |
| `r-matrix-renormalization` | Quiver-Hecke universal R-matrix as the concrete R-matrix setting | Kashiwara-Nakashima 2025, `crystal.tex:2331-2371`; affine/R-matrix source-location review. |
| `root-objects-in-localized-categories` | Conditional branch where $\widetilde Q_i$ is a root object | Kashiwara-Nakashima 2025, `crystal.tex:4576-4585`; positive-example review `2026-06-01-root-object-positive-example-review.md`. |
| `root-systems-and-weight-lattices` | Type $A_{n-1}$ root and weight-lattice example | Marberg 2020, Lecture 4, Examples 3.1-3.2 and Lecture 5, Example 1.1. |
| `universal-enveloping-algebras` | $\mathfrak{sl}_2$ and its enveloping-algebra commutator relations | Hong-Kang 2002, Chapter 1, Section 1.3, p.6. |

## Needs Review Before Labeling

These examples are not safe to label immediately from the current recorded evidence.

| Topic | Current example | Why not label-ready | Recommended action |
| --- | --- | --- | --- |
| `cellular-crystals` | $w=s_i$ gives $\mathcal B_{s_i}=B_i$ | This is a natural special case of the definition, but the current source notes do not record it as an explicit source example or checked computation. | Verify whether Kashiwara-Nakashima 2025 Section 2.4 or Kashiwara 1993 explicitly supports the $m=1$ example, or create a checked Sage example before labeling. |
| `graded-monoidal-categories` | `구조 예시` for $q(X\otimes Y)\simeq(qX)\otimes Y\simeq X\otimes(qY)$ | The source locations support the compatibility relation, but the current policy has no separate label for source-supported structural mechanisms. | Decide in a later report-only pass whether this can be labeled `검증: 논문 예시` as a source-supported structural example, or leave the example section empty. |
| `pro-categories` | `구조 예시` for recovering $\widehat M$ from $z$-adic quotients | The source locations support the mechanism, but the current policy has no separate label for source-supported structural mechanisms. | Decide in a later report-only pass whether this can be labeled `검증: 논문 예시` as a source-supported structural example, or leave the example section empty. |
| `quiver-hecke-algebras` | Nil-Hecke special case plus type $A_2$ module/path-algebra example | The source note records Section 2 and says type $A_2$ examples were used, but it does not record exact locations for all visible example statements. | Run a Brundan 2013 source-location tightening pass before adding a verification label. |
| `quiver-hecke-module-categories` | Type $A_2$ irreducible graded modules $L(12)$ and $L(21)$ | The example depends on the same Brundan type $A_2$ source detail, but exact source location is not recorded in the source note. | Run the same Brundan 2013 source-location tightening pass before adding a verification label. |

## Empty Example Sections

These topic pages have an empty `## 기본 예시` section and therefore do not violate the new label rule:

- `category-localization`
- `determinantial-modules`
- `head-simplicity-of-convolutions`
- `localized-root-operators`
- `monoidal-categorification`
- `normal-sequences`
- `quantum-coordinate-rings`
- `quantum-groups`
- `quasi-rigid-monoidal-categories`
- `reverse-equivalence-of-localized-categories`
- `shuffle-lemmas-for-quiver-hecke-modules`

Their existing missing-example backlog items remain the correct place to track future examples.

## Recommended Follow-Up

1. With explicit topic-page edit approval, add verification labels to the 12 label-ready examples and add concise provenance lines in final `Source notes` where needed.
2. Run a report-only source-location tightening pass for the 5 examples listed under "Needs Review Before Labeling".
3. Do not generate images or Sage examples until a specific example is approved for that workflow.

## Validation

Validation is recorded in `reports/roadmap/next-actions.md`.
