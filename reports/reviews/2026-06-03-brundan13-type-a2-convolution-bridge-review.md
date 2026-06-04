# Brundan13 Type A2 Convolution Bridge Review

## Scope

This is a report-only review of whether Brundan13's type \(A_2\) character-level calculation for

$$
L(1)\circ L(2),\qquad L(2)\circ L(1)
$$

can be used as a lower-level bridge example for the segment-module convolution path.

Inspected files and local text:

- `content/sources/papers/brundan13-quiver-hecke-algebras-categorification.md`
- `content/topics/06-quiver-hecke-klr-algebras/quiver-hecke-module-categories.md`
- `content/topics/06-quiver-hecke-klr-algebras/type-a-klr-segment-modules.md`
- `content/topics/06-quiver-hecke-klr-algebras/type-a-segment-module-convolutions.md`
- local staged PDF text for Brundan13

No paper was downloaded. No claim was added. No source note, topic page, example, localization material, or Grothendieck-ring comparison was added.

## Verdict

Yes, but only as a lower-level bridge example.

Brundan13's type \(A_2\) calculation is safe for showing a first concrete convolution-product phenomenon in a quiver-Hecke module category. It should not be used as the visible example for `Type A Segment Module Convolutions`.

The best placement, if later approved, is the existing `기본 예시` section of `Quiver-Hecke Module Categories`, where the page already introduces Brundan13's type \(A_2\) modules \(L(12)\) and \(L(21)\). The example can be expanded there to show that the two convolution orders have different graded characters.

## Source Support

Brundan13 Section 3, arXiv p.18, gives the type \(A_2\) setup with underlying graph \(1-2\) and \(\alpha=\alpha_1+\alpha_2\). It records:

$$
\operatorname{Ch}(L(1)\circ L(2))=12+q21,
$$

$$
\operatorname{Ch}(L(2)\circ L(1))=21+q12,
$$

and identifies the irreducible graded \(H_\alpha\)-modules up to degree shift as the one-dimensional modules \(L(12)\) and \(L(21)\).

Brundan13 Section 4, arXiv p.23, also explains the finite type \(A\) multisegment interpretation: positive roots are intervals, the corresponding cuspidal modules are one-dimensional homogeneous modules, and irreducible heads of proper standard modules recover irreducibles up to shift.

## What It Can Support

The Brundan13 \(A_2\) calculation can support a reader-facing bridge with the following limited mathematical message:

- convolution product is a real category-level operation, not just notation;
- changing the order of two factors can change the graded character;
- the words \(12\) and \(21\) already appear in the smallest type \(A\) example;
- this prepares the reader to later ask how interval positions control convolution products.

This is enough for a lower-level example in `Quiver-Hecke Module Categories`.

## What It Cannot Support

This example should not be used to fill the `기본 예시` gap in `Type A Segment Module Convolutions`.

It does not by itself provide:

- a KKK18A-style type \(A_\infty\) interval-pair example \(L(a,b)\circ L(a',b')\);
- a worked case of Proposition 4.2.3 with R-matrix zero order;
- the exact sequences from the crossing or adjacent cases;
- the identification of an R-matrix image with head and socle.

Therefore it is a bridge into the topic, not an example inside the theorem/mechanism topic.

## Recommended Later Edit

If approved later, update only `content/topics/06-quiver-hecke-klr-algebras/quiver-hecke-module-categories.md`:

- keep the existing type \(A_2\) example;
- add the two Brundan13 character formulas;
- explain that this is a character-level example of convolution order;
- point forward to `Type A KLR Segment Modules` and `Type A Segment Module Convolutions`;
- do not add claims, source notes, localization material, Grothendieck-ring comparison, or KKK18A exact-sequence statements.

## Recommended Next Action

```text
Using reports/reviews/2026-06-03-brundan13-type-a2-convolution-bridge-review.md, update only the 기본 예시 section of Quiver-Hecke Module Categories with Brundan13's type A2 character formulas for L(1)∘L(2) and L(2)∘L(1). Do not add claims, source notes, topic pages, localization material, Grothendieck-ring comparison, or KKK18A exact-sequence statements.
```
