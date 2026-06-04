# KKK18A Schur-Weyl Source-Location Review

## Scope

This report evaluates only the candidate source:

- `kang-kashiwara-kim18-symmetric-quiver-hecke-algebras-r-matrices`
- Seok-Jin Kang, Masaki Kashiwara, Myungho Kim, *Symmetric quiver Hecke algebras and R-matrices of quantum affine algebras*
- arXiv:1304.0323, Invent. Math. 211 (2018), 591-685

At the time of this report-only review, no PDF was saved to the repository, no source note was created, no claim was added, and no topic page was edited.

A later approved limited intake on 2026-06-03 staged the arXiv PDF and imported only the construction-level material identified below.

The arXiv abstract/PDF was used only to locate source positions for the existing `Quantum Affine Schur-Weyl Duality` topic path.

## Verdict

KKK18A is the right original-source companion for the construction-level part of quantum affine Schur-Weyl duality.

It should not yet be imported wholesale. The paper contains three layers:

1. the general functor construction from normalized quantum-affine R-matrices and a pole-defined KLR algebra;
2. exactness and tensor-functor properties of that construction;
3. the specialized type \(A_{N-1}^{(1)}\) localization story with the category \(T_J\), the category \(C_J\), and Grothendieck-ring comparison.

For the current wiki page, only the first two layers are relevant. The type \(A\) localization and \(T_J/C_J\) material should be deferred to later localized-category or Hernandez-Leclerc comparison pages.

## Exact Source Locations

### Bibliographic And Global Scope

- arXiv abstract page: arXiv records version 3 as submitted on 2021-03-26, with journal reference Invent. Math. 211 (2018), 591-685, and DOI `10.1007/s00222-017-0754-0`.
- arXiv PDF p.1, lines 5-42: the abstract states the construction of functors \(F_\beta\), their tensor compatibility, exactness in finite ADE type, recovery of affine Schur-Weyl duality in the vector-representation type \(A_{n-1}^{(1)}\) case, and the later localization category \(T_J\).
- arXiv PDF pp.3-5, lines 138-300: the introduction explains the motivation from quantum affine Schur-Weyl duality, the role of R-matrices and intertwiners, the pole-defined quiver \(\Gamma_J\), the functor \(F_\beta\), and the later category \(T_J\).

### R-Matrix Input

- Section 2.2, arXiv PDF p.25, lines 1871-1946: recalls normalized R-matrices for good \(U_q'(\mathfrak g)\)-modules and defines the denominator polynomial \(d_{M_1,M_2}(u)\).
- Section 2.2, arXiv PDF p.25, lines 1947-1999: records the inverse relation, Yang-Baxter equation, and iterated normalized R-matrices.
- Theorem 2.2.1, arXiv PDF pp.25-26, lines 2000-2041: gives the basic pole/head/socle facts for tensor products of good modules.
- Example 2.2.2, arXiv PDF p.26, lines 2042-2074: gives the normalized R-matrix and denominator formula for fundamental representations of \(U_q'(\widehat{\mathfrak{sl}}_N)\).
- Remark 2.2.3, arXiv PDF p.26, lines 2075-2086: notes simple-pole behavior in type \(A_{N-1}^{(1)}\) and warns that this need not hold in type \(D_N^{(1)}\).

### KLR Data From R-Matrix Poles

- Section 3.1, arXiv PDF pp.26-27, lines 2088-2109: starts from good modules \(V_s\), spectral parameters \(X(i)\), and the zero order \(d_{ij}\) of the denominator \(d_{V_{S(i)},V_{S(j)}}(z_2/z_1)\), then defines the KLR polynomial \(Q_{ij}(u,v)\).
- Remark 3.1.2, arXiv PDF p.27, lines 2115-2134: identifies the Cartan matrix and quiver \(\Gamma_J\) determined by these orders.

### Bimodule Construction

- Section 3.1, arXiv PDF p.29, lines 2197-2228: defines the completed tensor object \(\widehat V^{\otimes\beta}\) from affinizations of the chosen good modules.
- Section 3.1, arXiv PDF p.29, lines 2229-2280: defines the R-matrix operators \(R^\nu_{a,a+1}\) on adjacent tensor factors using normalized R-matrices.
- Section 3.1, arXiv PDF pp.29-30, lines 2281-2365: uses those R-matrices to define the right action and proves stability under the KLR generators.
- Theorem 3.1.3, arXiv PDF pp.29-30, lines 2319-2326: states that \(\widehat V^{\otimes\beta}\) has a \((U_q'(\mathfrak g),R^J(\beta))\)-bimodule structure.

### Functor Construction

- Section 3.2, arXiv PDF pp.30-31, lines 2366-2405: defines
  $$
  F_\beta(M)=\widehat V^{\otimes\beta}\otimes_{R^J(\beta)}M.
  $$
- Theorem 3.2.1, arXiv PDF p.31, lines 2406-2424: states that \(F=\bigoplus_\beta F_\beta\) is a tensor functor and sends convolution products to tensor products.
- Proposition 3.2.2, arXiv PDF p.32, lines 2472-2526: compares the KLR-side R-matrix on \(L(i)_z\circ L(j)_{z'}\) with the normalized quantum-affine R-matrix after applying \(F\).
- Theorem 3.3.3, arXiv PDF p.33, lines 2587-2600: states exactness of \(F_\beta\) when the associated quiver is finite type ADE.

### Type A Localization Material

This is relevant later, but it should not be imported into the current `Quantum Affine Schur-Weyl Duality` page yet.

- Section 4, arXiv PDF p.35, lines 2715-2726: recalls the exact functor \(F\) in the \(U_q'(\widehat{\mathfrak{sl}}_N)\) vector-representation case.
- Section 4.4, arXiv PDF p.45, lines 3619-3643: defines the Serre subcategory \(S\) and factors \(F\) through the quotient \(A/S\).
- Theorem 4.6.5, arXiv PDF pp.58-59, lines 4738-4790: chooses \(c_{ij}(u,v)\) so that the localization diagram for \(F'\) and central objects commutes.
- Section 4.6, arXiv PDF p.60, lines 4873-4919: obtains the factored functor \(\widetilde F:T_J\to U_q'(\widehat{\mathfrak{sl}}_N)\)-mod and records exactness.
- Section 4.7, arXiv PDF p.60, lines 4934-4937: views \(\widetilde F\) as a functor \(T_J\to C_J\).
- Theorem 4.7.4, arXiv PDF p.62, lines 5071-5074: \(\widetilde F\) induces a Grothendieck-ring isomorphism after forgetting the grading.
- Theorem 4.7.5, arXiv PDF pp.63-64, lines 5113-5258: identifies the \(t\)-deformation \(K_t\) with the scalar extension of \(K(T_J)\).

## Relation To KKOP24

KKOP24 is better for the later duality-datum and strong-duality-datum formulation used by the current wiki page.

KKK18A is better for the original construction mechanism:

- how denominator poles determine the KLR quiver and KLR parameters;
- how affinizations of good quantum-affine modules form the completed tensor object;
- how normalized R-matrices define the right KLR action;
- how the tensor functor \(F\) sends convolution to tensor product.

The two sources should be used together only after an approved intake. KKK18A should not replace the KKOP24 strong-duality-datum statements already used on the page.

## Recommended Future Use

If approved later, KKK18A can support a small expansion of `Quantum Affine Schur-Weyl Duality`:

1. add a source note for KKK18A;
2. add at most three reusable claims:
   - normalized R-matrix denominator data define the KLR parameters;
   - \(\widehat V^{\otimes\beta}\) is a \((U_q'(\mathfrak g),R^J(\beta))\)-bimodule;
   - \(F=\bigoplus_\beta F_\beta\) is a tensor functor, exact in finite ADE type;
3. add one compact paragraph explaining the construction mechanism of \(F\), not the type \(A\) localization theory.

Do not import the \(T_J\), \(C_J\), localization, or Grothendieck-ring comparison material into the current Schur-Weyl page before the localized-category path is ready.

## Remaining Gaps

- The current page still lacks a source-backed example suitable for undergraduate-oriented reading.
- The type \(A\) vector-representation case is a possible future example, but it depends on KLR modules in type \(A_\infty\), localization, and the category \(C_J\).
- A separate prerequisite topic on good modules and affinizations may become necessary if the construction paragraph makes the page too dense.

## Next Recommended Prompt

```text
Run a limited approved-source intake for `kang-kashiwara-kim18-symmetric-quiver-hecke-algebras-r-matrices` using arXiv:1304.0323. Stage the legal arXiv PDF, create a concise source note, add at most 3 claims for the KLR parameters, bimodule construction, and tensor functor. Update only `Quantum Affine Schur-Weyl Duality` if the construction paragraph can stay compact. Do not import the type A localization, `T_J`, `C_J`, or Grothendieck-ring comparison material.
```
