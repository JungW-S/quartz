---
id: kkko14-monoidal-categorification-cluster-algebras
title: Monoidal Categorification of Cluster Algebras
source_type: paper
---

This source note records provenance for the approved KKKO14 intake. It is an extraction index, not a long paper summary.

## Bibliographic Data

- Authors: Seok-Jin Kang, Masaki Kashiwara, Myungho Kim, Se-jin Oh
- Year: 2014
- arXiv: [1412.8106v1](https://arxiv.org/abs/1412.8106)
- Local PDF: `content/assets/pdfs/kkko14-monoidal-categorification-cluster-algebras.pdf`

## Why This Source Matters

KKKO14 supplies the general definition of monoidal categorification used for cluster algebras and quantum cluster algebras for symmetric quiver-Hecke algebras. It also gives a criterion, via admissible pairs, for producing a monoidal categorification from categorical data.

<!-- CODEX-MANAGED: may append source-backed material here -->

## Imported Definitions

- `kkko14-real-simple-module-definition`: real simple module. Source location: Definition 1.7, p.12.
- `kkko14-commuting-simply-linked-definition`: commuting and simply-linked simple modules. Source location: Definition 2.12, p.16.
- `kkko14-cluster-algebra-recall`: recalled cluster algebra definition by initial seed, mutation, cluster variables, and cluster monomials. Source location: Introduction, pp.1-2; Section 5.1, p.30.
- `kkko14-quantum-seed-definition`: quantum torus, \(L\)-commuting families, compatible pairs, quantum seeds, and quantum cluster monomials. Source location: Section 4.1, pp.27-28.
- `kkko14-quantum-cluster-algebra-definition`: mutation of quantum seeds and the associated quantum cluster algebra \(A_{q^{1/2}}(S)\). Source location: Section 4.2 and Definition 4.2, pp.28-29.
- `kkko14-monoidal-categorification-cluster-definition`: monoidal categorification of a cluster algebra. Source location: Definition 5.3, p.30.
- `kkko14-quantum-monoidal-seed-definition`: quantum monoidal seed. Source location: Definition 5.4, pp.31-32.
- `kkko14-monoidal-categorification-quantum-definition`: monoidal categorification of a quantum cluster algebra. Source location: Definition 5.8, p.34.
- `kkko14-admissible-pair-definition`: admissible pair. Source location: Definition 6.1, p.35.

## Imported Theorems And Propositions

- `kkko14-commuting-real-family-product`: a commuting family of real simple modules has real simple convolution product. Source location: Proposition 2.13, p.16.
- `kkko14-admissible-pair-categorification-criterion`: under the paper's Grothendieck-ring hypothesis, an admissible pair gives a monoidal categorification of the associated quantum cluster algebra. Source location: Theorem 6.3 and Corollary 6.4, pp.37-43.

## Imported Examples

- No standalone computed example was imported as a claim in this batch.
- The rank-two example in [[topics/04-cluster-algebras/cluster-algebras|Cluster Algebras]] is not a paper example from KKKO14; it is a Sage-verified calculation using the mutation formula recalled in Section 5.1.
- The rank-two example in [[topics/04-cluster-algebras/quantum-cluster-algebras|Quantum Cluster Algebras]] is not a paper example from KKKO14; it is a Sage-verified calculation using the quantum seed and mutation definitions in Sections 4.1-4.2.

## Notation Translation

- The paper writes convolution product as `\circ`; topic pages render this as $M\circ N$ for object-level products.
- The paper uses `K(\mathcal C)` for the Grothendieck ring of a monoidal category; topic pages normalize this as $K_0(\mathcal C)$.
- A real simple object is one whose self-convolution is simple.
- Quantum cluster monomials are represented in the categorifying category by real simple objects up to a power of $q^{1/2}$, i.e. up to grading shift in the quantum case.

## Topic Pages Updated

- [[topics/04-cluster-algebras/cluster-algebras|Cluster Algebras]]
- [[topics/04-cluster-algebras/quantum-cluster-algebras|Quantum Cluster Algebras]]
- [[topics/05-monoidal-categorification/monoidal-categorification|Monoidal Categorification]]
- [[topics/06-quiver-hecke-klr-algebras/quiver-hecke-module-categories|Quiver-Hecke Module Categories]]
- [[topics/08-localization-of-categories/quiver-hecke-category-localization|Quiver-Hecke Category Localization]]

## Claims Not Imported

- The proof details of Leclerc's conjecture on products of upper global basis elements were not extracted as reusable claims in this batch.
- The full machinery of R-matrices and heads/socles of tensor products was not imported beyond the real/commuting-module definitions needed for topic navigation.
- Statements about forthcoming applications to $\mathcal C_w$ were not imported as claims.
- Detailed examples and computations from adjacent cluster-algebra literature were not imported.

<!-- NEEDS-HUMAN-REVIEW -->

## Review Notes

- The local registry keeps the citekey `kkko14-monoidal-categorification-cluster-algebras`, while the arXiv entry is `1412.8106v1`.
- If a later page needs exact KKKO14 source notation, record the source form `K(\mathcal C)` in the source note and keep $K_0(\mathcal C)$ in reader-facing topic prose.
