# Quantum Affine Schur-Weyl Density Review

## Scope

This is a report-only review of:

- `content/topics/07-quantum-affine-algebras/quantum-affine-schur-weyl-duality.md`

No source was downloaded. No claim was added. No source note was created. No topic page was edited.

The question was whether the KKK18A construction layer made the page too dense, and whether good modules/affinizations or strong duality data should become separate prerequisite topics.

## Verdict

The page is still acceptable as a definition-ready advanced topic, but it is now close to the upper density limit for a first reader-facing page.

The next split should not be `Strong Duality Data`.

The next split should be a small prerequisite topic for the construction input:

- proposed topic id: `quantum-affine-r-matrix-denominators`
- proposed title: `Quantum Affine R-Matrix Denominators`
- parent topic: `quantum-affine-algebras`
- prerequisite topics:
  - `quantum-affine-algebras`
  - `r-matrix-renormalization`
  - `affine-objects-in-monoidal-categories`
- target maturity: `definition-ready`

This topic should explain only the data needed before reading the KKK18A construction:

- chosen good \(U_q'(\mathfrak g)\)-modules;
- spectral parameters \(X(i)\);
- normalized R-matrix denominator \(d_{M,N}(z)\);
- zero orders \(d_{ij}\);
- how those orders determine the KLR quiver and the polynomials \(Q_{ij}(u,v)\).

It should not import type \(A\) localization, \(T_J\), \(C_J\), Grothendieck-ring comparison, or examples.

## Why This Split Is Better

### Keep strong duality data inside the Schur-Weyl page for now

Strong duality datum is not just a background prerequisite. On the current page it is the exact hypothesis for the visible simple-to-simple theorem, invariant comparison theorem, and Grothendieck-ring corollary. If it is moved out now, the page will become harder to read because the theorem hypotheses will be separated from the theorem statements.

Root module and strong duality datum should become a separate topic only when later pages start using them repeatedly, for example in affine cuspidal modules or PBW theory.

### Do not split affinizations alone

`Affine Objects in Monoidal Categories` already explains the categorical idea of \((\widehat M,z)\), special fiber, rational center, and renormalized R-matrix. The Schur-Weyl page links to it. A separate `Affinizations of Quantum Affine Modules` topic would probably duplicate existing material unless a later source-backed example requires it.

### Split the denominator/KLR-parameter layer

The construction paragraph now jumps from normalized R-matrix denominators to KLR parameters \(Q_{ij}(u,v)\). That is mathematically correct, but it is the least reader-friendly point in the page.

This layer is neither fully covered by `R-Matrix Renormalization` nor by `Affine Objects in Monoidal Categories`:

- `R-Matrix Renormalization` explains degree invariants and renormalized morphisms.
- `Affine Objects in Monoidal Categories` explains pro-object and affinization language.
- The missing bridge is how quantum-affine denominator poles define the quiver-Hecke algebra used by the functor.

That bridge is exactly what KKK18A Section 3.1 supports.

## Page-Level Readability Findings

The page has a good high-level route:

1. categories compared;
2. duality datum;
3. construction mechanism;
4. strong hypothesis;
5. theorem-level consequences.

The main readability strain is that the setup section now introduces:

- \(R_{\mathsf C}\operatorname{-gmod}\);
- \(\mathcal C_{\mathfrak g}\);
- duals \(M^*,{}^*M\);
- \(\mathfrak d(M,N)\);
- chosen modules \(V_s\);
- spectral parameters \(X(i)\);
- denominator polynomials;
- KLR parameters.

This is too much notation for one setup section if the page later receives an example. Before adding examples, the denominator/KLR-parameter material should either move to a prerequisite page or be shortened in the Schur-Weyl page.

## Recommendation

Create a small prerequisite page `Quantum Affine R-Matrix Denominators` before adding examples to `Quantum Affine Schur-Weyl Duality`.

Use only already ingested KKK18A material:

- `kkk18a-rmatrix-denominator-klr-parameters`;
- KKK18A source note, Section 3.1, arXiv PDF pp.26-27, lines 2088-2134.

The new page should not add new claims. It can reuse the existing claim and source note.

After that, the Schur-Weyl page can be polished by replacing the construction paragraph with a shorter pointer to the new prerequisite page.

## Not Recommended Now

- Do not create `Strong Duality Data` yet.
- Do not create `Root Modules` yet.
- Do not add the KKK18A type \(A\) vector-representation localization material as an example yet.
- Do not import \(T_J\), \(C_J\), or Grothendieck-ring comparison into the current page.
- Do not add a visible example before the denominator/KLR-parameter layer is easier to read.

## Next Recommended Prompt

```text
Create a small prerequisite topic `Quantum Affine R-Matrix Denominators` under Quantum Affine Algebras using only the already ingested KKK18A source note and existing claim `kkk18a-rmatrix-denominator-klr-parameters`. Make it definition-ready, do not add claims, do not add examples, and do not import type A localization, `T_J`, `C_J`, or Grothendieck-ring comparison.
```
