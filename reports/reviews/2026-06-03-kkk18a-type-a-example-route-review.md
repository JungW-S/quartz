# KKK18A Type A Example Route Review

## Scope

This is a report-only review of the already staged source:

- `kang-kashiwara-kim18-symmetric-quiver-hecke-algebras-r-matrices`
- Seok-Jin Kang, Masaki Kashiwara, Myungho Kim, *Symmetric quiver Hecke algebras and R-matrices of quantum affine algebras*
- Staged PDF: `content/assets/pdfs/kang-kashiwara-kim18-symmetric-quiver-hecke-algebras-r-matrices.pdf`

No paper was downloaded, no claim was added, and no topic page was edited.

The question is whether the type \(A\) denominator formulas or vector-representation material can become a compact source-backed example for either:

- `Quantum Affine R-Matrix Denominators`
- `Quantum Affine Schur-Weyl Duality`

## Verdict

KKK18A Section 4.1 can safely support a compact example for `Quantum Affine R-Matrix Denominators`.

It should not yet be used as a visible basic example for `Quantum Affine Schur-Weyl Duality`. The Schur-Weyl side quickly depends on type \(A_\infty\) KLR segment modules, multisegments, quotient/localization categories, \(T_J\), \(C_J\), and Grothendieck-ring comparison. Those are not yet reader-ready prerequisites in the wiki.

## Safe Example Candidate

The safe candidate is the denominator-to-KLR-data example in KKK18A Section 4.1.

Exact source locations:

- Section 4.1, arXiv PDF p.35: defines \(V=V(\varpi_1)\), the fundamental representation of \(U_q'(\widehat{\mathfrak{sl}}_N)\).
- Equation (4.1.1), arXiv PDF p.35: gives the normalized R-matrix on \(V_z\otimes V_{z'}\).
- Immediately after (4.1.1), arXiv PDF p.35: identifies the denominator as
  $$
  d_{V,V}(z'/z)=z'/z-q^2.
  $$
- Equation (4.1.2), arXiv PDF p.35: with \(J=\mathbb Z\) and \(X(j)=q^{2j}\), gives
  $$
  d_{ij}=\delta(j=i+1).
  $$
- The following paragraph on arXiv PDF p.35: identifies the corresponding Cartan data and says that the associated Khovanov-Lauda-Rouquier algebra is of type \(A_\infty\).

This is exactly the conceptual direction of the denominator topic:

$$
\text{type }A_{N-1}^{(1)}\text{ vector representation}
\longrightarrow
d_{V,V}(z'/z)
\longrightarrow
d_{ij}
\longrightarrow
A_\infty\text{ KLR data}.
$$

## Recommended Use

If the user approves a later topic edit, add only a compact `기본 예시` section to `Quantum Affine R-Matrix Denominators`.

The example should say, in Korean reader-facing prose, that for \(V=V(\varpi_1)\) of \(U_q'(\widehat{\mathfrak{sl}}_N)\), KKK18A computes the normalized R-matrix denominator as \(z'/z-q^2\). Choosing \(J=\mathbb Z\) and \(X(j)=q^{2j}\), the denominator has a zero exactly when \(j=i+1\), so \(d_{ij}=\delta(j=i+1)\). This produces the type \(A_\infty\) KLR data.

Do not add the explicit full normalized R-matrix formula unless the page needs it later. The denominator and \(d_{ij}\) computation are enough for the example.

Do not add \(T_J\), \(C_J\), localization, segment modules, multisegments, or Grothendieck-ring comparison to the denominator page.

## Not Recommended Yet

Do not use Section 4.2-4.7 as a basic example for `Quantum Affine Schur-Weyl Duality` yet.

Source locations showing why it is too dense:

- Section 4.2, arXiv PDF pp.36-43: introduces type \(A\) KLR segment modules \(L(a,b)\), multisegments, R-matrix computations, and several exact sequences.
- Proposition 4.3.1, arXiv PDF pp.43-44: computes \(F(L(a,b))\), but this already relies on the segment-module setup.
- Theorem 4.3.3, arXiv PDF p.45: gives irreducibility behavior of \(F(M)\) for simple \(R\)-modules described by multisegments.
- Sections 4.6-4.7, arXiv PDF pp.58-64: introduce the localization route through \(T_J\), \(C_J\), and Grothendieck-ring comparison.

These statements are valuable, but importing them as an example would force several unprepared notions into the Schur-Weyl page.

## Page Placement Decision

Best first placement:

- `Quantum Affine R-Matrix Denominators`

Reason:

- the example is short;
- it directly illustrates denominator zero order;
- it does not require explaining the functor \(F\);
- it does not require localization categories.

Deferred placement:

- `Quantum Affine Schur-Weyl Duality`

Reason:

- a genuine Schur-Weyl example should show what the functor does to KLR modules;
- KKK18A's available type \(A\) example uses segment modules and multisegment classification;
- that prerequisite layer is not yet present as a readable topic.

## Next Recommended Action

```text
Using only KKK18A Section 4.1, add a compact source-backed 기본 예시 to Quantum Affine R-Matrix Denominators: V=V(varpi_1) for U_q'(widehat sl_N), denominator d_{V,V}(z'/z)=z'/z-q^2, X(j)=q^{2j}, d_{ij}=delta(j=i+1), and the resulting type A_infinity KLR data. Do not add claims, do not import T_J, C_J, localization, segment modules, multisegments, or Grothendieck-ring comparison.
```

## Remaining Gap

If a later Schur-Weyl example is desired, the wiki should first prepare a small prerequisite path for type \(A\) KLR segment modules or run a separate report-only review deciding whether that material deserves its own topic.
