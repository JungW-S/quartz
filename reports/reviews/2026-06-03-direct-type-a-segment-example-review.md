# Direct Type A Segment Example Review

## Scope

This is a report-only review of whether a direct KKK18A-style worked two-segment example for `Type A Segment Module Convolutions` can be made from KKK18A alone or from Sage verification.

Inspected local files and tools:

- `content/topics/06-quiver-hecke-klr-algebras/type-a-segment-module-convolutions.md`
- `content/sources/papers/kang-kashiwara-kim18-symmetric-quiver-hecke-algebras-r-matrices.md`
- `reports/reviews/2026-06-03-type-a-segment-convolution-example-source-review.md`
- `content/assets/pdfs/kang-kashiwara-kim18-symmetric-quiver-hecke-algebras-r-matrices.pdf`
- local Sage namespace search for KLR / quiver-Hecke module support

No paper was downloaded. No topic page, claim, source note, localization material, Grothendieck-ring comparison, Sage-generated example, or new topic page was added.

## Verdict

Yes, but the safe route is KKK18A alone, not Sage.

KKK18A does not give a small numbered numerical example such as fixed intervals \((1,2)\) and \((2,2)\). However, KKK18A does use a concrete adjacent-case family in the proof of Proposition 4.3.1:

$$
0
\to
L(a,b)
\to
L(b)\circ L(a,b-1)
\xrightarrow{\,r_{(b),(a,b-1)}\,}
L(a,b-1)\circ L(b)
\to
L(a,b)
\to
0,
$$

with grading omitted in that proof. The paper states that this exact sequence is given by Proposition 4.2.3(vi).

This is better than an editor-chosen arbitrary substitution because the paper itself selects this adjacent case family for an argument. It can serve as a visible paper-verified example, if it is clearly presented as an adjacent-family example and not as a Sage computation.

## KKK18A Source Locations

KKK18A Section 4.2, arXiv PDF p.36:

- defines a segment \((a,b)\);
- defines the one-dimensional module \(L(a,b)\);
- sets the notation \(L(a)=L(a,a)\).

KKK18A Proposition 4.2.3, arXiv PDF pp.37-39:

- gives the two-segment case analysis;
- part (vi) gives the adjacent case \(a=b'+1\);
- in the fully graded statement, this gives an exact sequence of the form
  \[
  0
  \to
  qL(a',b)
  \to
  L(a,b)\circ L(a',b')
  \to
  q^{-1}L(a',b')\circ L(a,b)
  \to
  q^{-1}L(a',b)
  \to
  0.
  \]

KKK18A Proposition 4.3.1 proof, arXiv PDF pp.43-44:

- applies Proposition 4.2.3(vi) to the adjacent pair \(L(b)\) and \(L(a,b-1)\);
- explicitly records the exact sequence
  \[
  0
  \to
  L(a,b)
  \to
  L(b)\circ L(a,b-1)
  \to
  L(a,b-1)\circ L(b)
  \to
  L(a,b)
  \to
  0
  \]
  after saying that grading is omitted in the proof.

## Sage Verification Status

Local Sage inspection did not find built-in KLR or quiver-Hecke module category support.

The Sage namespace search found only general objects such as:

- `ClusterQuiver`
- `QuiverMutationType`
- `HeckeAlgebraSymmetricGroupT`
- `HeckeModules`
- `IwahoriHeckeAlgebra`

It did not expose a built-in object for KLR algebras, segment modules \(L(a,b)\), convolution products, renormalized R-matrix maps, or head/socle computations. Therefore a Sage-verified example is not currently available without writing and auditing a custom KLR verification script.

Such a custom script would be a separate project. It would need to implement enough of the type \(A\) KLR algebra action, induced modules, maps, and exactness/head-socle checks to be trusted. That is too large for the current example-fill task.

## Recommended Visible Example

If approved, add a compact `기본 예시` to `Type A Segment Module Convolutions` using the adjacent-family exact sequence.

Recommended mathematical content:

- say that this is the adjacent case;
- take \(a\le b\) with \(b-a+1\ge2\);
- look at the two factors \(L(b)\) and \(L(a,b-1)\);
- explain that the intervals \([b,b]\) and \([a,b-1]\) touch at the boundary, so this is Proposition 4.2.3(vi);
- display the exact sequence, preferably with the grading shifts from Proposition 4.2.3(vi):
  \[
  0
  \to
  qL(a,b)
  \to
  L(b)\circ L(a,b-1)
  \to
  q^{-1}L(a,b-1)\circ L(b)
  \to
  q^{-1}L(a,b)
  \to
  0.
  \]
- note briefly that KKK18A uses the same adjacent family in the proof of Proposition 4.3.1 after omitting grading.

Recommended verification label:

```text
검증: KKK18A Proposition 4.2.3(vi), and the adjacent family used in the proof of Proposition 4.3.1.
```

## Do Not Add

Do not call this a Sage-verified example.

Do not add the full proof of Proposition 4.2.3, the morphisms \(\xi_{a,c,b}\), the full R-matrix proof, localization material, \(T_J\), \(C_J\), Theorems 4.7.4-4.7.5, or Grothendieck-ring comparison.

Do not add a numerical computation unless a separate Sage or paper verification is completed.

## Recommended Next Action

```text
Using reports/reviews/2026-06-03-direct-type-a-segment-example-review.md, add only the adjacent-family exact sequence example to the 기본 예시 section of Type A Segment Module Convolutions. Label it as verified by KKK18A Proposition 4.2.3(vi) and the proof of Proposition 4.3.1. Do not add claims, new source notes beyond a minimal source-location bullet if needed, Sage-generated material, localization material, Grothendieck-ring comparison, or new topic pages.
```
