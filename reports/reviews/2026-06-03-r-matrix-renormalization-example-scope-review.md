# R-Matrix Renormalization Example Scope Review

Date: 2026-06-03

## Scope

This report checks whether `content/topics/06-quiver-hecke-klr-algebras/r-matrix-renormalization.md` should add a broader source-backed example beyond the current quiver-Hecke universal R-matrix setup.

Only `inbox/papers/crystal.tex`, the existing topic page, and the earlier source-location review were checked. No topic page was edited. No claims were added. No sources were downloaded.

## Current Page State

The topic page already contains the correct prerequisite-level material:

- $\Lambda$-definable simple pairs and $\Lambda(M,N)$;
- the symmetric degree $\mathfrak d(M,N)$;
- renormalized R-matrices from rational centers and a parameter $z$;
- the modified localized degree $\widetilde\Lambda(X,Y)$;
- the quiver-Hecke universal R-matrix as the visible paper-verified example.

This is enough for the page's current role as a prerequisite for root objects, localized root operators, and normal sequences.

## Source Locations Checked

- `inbox/papers/crystal.tex:1731-1747`: defines $\Lambda$-definable pairs, R-matrices, $\Lambda(M,N)$, and $\mathfrak d(M,N)$.
- `inbox/papers/crystal.tex:1777-1804`: defines rational centers and affinizations.
- `inbox/papers/crystal.tex:1806-1834`: gives the renormalized R-matrix construction and the induced morphism in $\operatorname{Aff}(\mathscr C)$.
- `inbox/papers/crystal.tex:1958-2010`: records quasi-rigid degree-control results for affreal simple objects. These are structural theorems, not examples.
- `inbox/papers/crystal.tex:2331-2371`: defines the quiver-Hecke universal R-matrix and explains its compatibility with the general affinization framework. This supports the current visible example.
- `inbox/papers/crystal.tex:2448-2474`: uses composed R-matrices in normal-sequence arguments. This belongs to `Normal Sequences`, not to the basic R-matrix example.
- `inbox/papers/crystal.tex:2758-2784`: uses a renormalized R-matrix inside an $E_i^*$ argument. This is proof-level material, not a reader-facing worked example.
- `inbox/papers/crystal.tex:3268-3294`: compares localized R-matrix degree with a quotient morphism. This is localization infrastructure, not a simple example.
- `inbox/papers/crystal.tex:3317-3354`: compares $\Lambda(Q(M),Q(N))$ with $\Lambda(M,N)$ and defines $\widetilde\Lambda$. This supports the current property layer.
- `inbox/papers/crystal.tex:3546-3680`: uses $\mathfrak d$ and $\Lambda$ in root-object and simple-root-object arguments. This belongs downstream.

## Decision

Do not add a broader visible example to the R-matrix page now.

The current example is the right level for this page: it shows that quiver-Hecke module categories provide a concrete universal R-matrix construction and that this construction interfaces with the affine-object framework. The other KN25 R-matrix appearances are theorem-level or downstream uses:

- the normal-sequence R-matrix composition belongs on `Normal Sequences`;
- the $E_i^*$ and localization comparison arguments are proof-level mechanisms;
- root-object degree formulas belong on `Root Objects in Localized Categories` or `Localized Root Operators`;
- the type $A_2$ remark around $L=\langle1\rangle$, $M=\langle2\rangle$ is a subcategory-membership warning, not an R-matrix renormalization example.

## Proposed Wording

No wording change is recommended. Keep the current visible example and do not add theorem-level degree-control formulas as examples.

## Next Step

Move to `Normal Sequences`: check whether KN25 or the existing KKKO15 source gives a compact paper-verified normal-sequence example suitable for the intentionally empty example section.
