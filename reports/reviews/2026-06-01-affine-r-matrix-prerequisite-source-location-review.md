# Affine Objects and R-Matrix Prerequisites Source-Location Review

Date: 2026-06-01

## Scope

This report reviews exact source locations for the title-only prerequisite topics:

- `content/topics/affine-objects-in-monoidal-categories.md`
- `content/topics/r-matrix-renormalization.md`

Only `inbox/papers/crystal.tex` was checked. No topic page was edited. No claims were added. No sources were downloaded.

The purpose is to prepare the prerequisite layer needed to read `content/topics/root-objects-in-localized-categories.md`.

## Source Locations

### 1. Pro-category and graded setup for affine objects

- `inbox/papers/crystal.tex:1519-1524`: starts the general graded monoidal category section and the subsection "Affine objects in $\operatorname{Pro}(\mathscr C)$".
- `inbox/papers/crystal.tex:1526-1548`: defines pro-objects, $\operatorname{Pro}(\mathscr C)$, and the co-directed projective limit notation $\varprojlim$.
- `inbox/papers/crystal.tex:1550-1577`: states the finite-length graded category assumptions on $\mathscr C$ and records that $\mathscr C$ sits inside $\operatorname{Pro}(\mathscr C)$.
- `inbox/papers/crystal.tex:1578-1621`: defines the graded algebra $A$, the category $\operatorname{Mod}^{\mathrm{gr}}(A,\operatorname{Pro}(\mathscr C))$, and the coherent pro-object subcategory $\operatorname{Pro}^{\mathrm{coh}}(A,\mathscr C)$.

These lines are the setup for saying what kind of object an affine object is. A future topic page should not skip directly to root objects without first explaining that affine objects live in a pro-category completion.

### 2. Definition of affine object

- `inbox/papers/crystal.tex:1623-1642`: Definition `Def: affine objects`.
  For a homogeneous indeterminate $z$ of positive degree, an object of $\operatorname{Pro}^{\mathrm{coh}}(\mathbf k[z],\mathscr C)$ is a pair $(\widehat M,z)$ satisfying:
  - $\widehat M\in\operatorname{Pro}(\mathscr C)$ and $z$ is a homogeneous endomorphism of $\widehat M$;
  - $\widehat M/z\widehat M\in\mathscr C$;
  - $\widehat M\simeq\varprojlim_n\widehat M/z^n\widehat M$.
  If $z$ is also a monomorphism, the pair is called an affine object in $\mathscr C$.
- `inbox/papers/crystal.tex:1640-1642`: defines $\operatorname{Aff}(\mathscr C)$ as the category of affine objects.

This is the safest source-backed definition for a future `Affine Objects in Monoidal Categories` page.

### 3. Monoidal structure and rational affine objects

- `inbox/papers/crystal.tex:1646-1669`: gives the graded monoidal category assumptions, compatibility with the grading shift $q$, and the monoidal structure on $\operatorname{Pro}(\mathscr C)$.
- `inbox/papers/crystal.tex:1692-1713`: defines the category $\operatorname{Rat}(\mathscr C)$ of rational affine objects and records the faithful essentially surjective functor $\operatorname{Aff}(\mathscr C)\to\operatorname{Rat}(\mathscr C)$.
- `inbox/papers/crystal.tex:1717-1728`: defines the monoidal product on $\operatorname{Aff}(\mathscr C)$:
  $$
  \widehat M\otimes_z\widehat N
  =
  \operatorname{Coker}
  \bigl(
  \widehat M\otimes\widehat N
  \xrightarrow{z\otimes1-1\otimes z}
  \widehat M\otimes\widehat N
  \bigr),
  $$
  and states that if $\mathscr C$ is rigid, then $\operatorname{Aff}(\mathscr C)$ is rigid.

These statements explain why affine objects form a category suitable for R-matrix and duality arguments.

### 4. Basic R-matrix degree notation

- `inbox/papers/crystal.tex:1731-1747`: Definition `def:rmat`.
  For simple objects $M,N\in\mathscr C$, if
  $$
  \dim\operatorname{HOM}(M\otimes N,N\otimes M)=1,
  $$
  the pair is $\Lambda$-definable, a nonzero morphism
  $$
  R_{M,N}:M\otimes N\to N\otimes M
  $$
  is called the R-matrix, and
  $$
  \Lambda(M,N)=\deg R_{M,N}.
  $$
  If both $(M,N)$ and $(N,M)$ are $\Lambda$-definable, then
  $$
  \mathfrak d(M,N)
  =
  \frac{\Lambda(M,N)+\Lambda(N,M)}{2}.
  $$

This is the notation needed in the root-object condition $\mathfrak d(L,\mathscr D^{-1}L)=d_L$.

### 5. Rational centers and affinizations

- `inbox/papers/crystal.tex:1754-1769`: states the additional graded monoidal category decomposition used for rational centers and affinizations.
- `inbox/papers/crystal.tex:1777-1790`: defines a rational center as a triple $(\widehat M,\phi,R_{\widehat M})$ with functorial isomorphisms in $\operatorname{Rat}(\mathscr C)$ satisfying compatibility diagrams.
- `inbox/papers/crystal.tex:1798-1804`: defines an affinization of $M\in\mathscr C$ as an affine object $(\widehat M,z)$ endowed with a rational center and an isomorphism
  $$
  \widehat M/z\widehat M\simeq M
  $$
  with $\deg z=d$.

This is the exact distinction a future topic page must keep: an affine object is the pro-object pair, while an affinization of $M$ is an affine object with rational-center data and special fiber $M$.

### 6. Renormalized R-matrix from a rational center

- `inbox/papers/crystal.tex:1806-1828`: Proposition `pro:rren`.
  Given a rational center $(\widehat M,R_{\widehat M})$ and $L\in\mathscr C$, there are unique integer powers of $z$ producing morphisms
  $$
  R^{\mathrm{ren}}_{\widehat M,L}:\widehat M\otimes L\to L\otimes\widehat M
  $$
  and
  $$
  R^{\mathrm{ren}}_{L,\widehat M}:L\otimes\widehat M\to\widehat M\otimes L
  $$
  in $\operatorname{Pro}^{\mathrm{coh}}(\mathbf k[z],\mathscr C)$ whose specialization at $z=0$ does not vanish.
- `inbox/papers/crystal.tex:1830-1834`: when two affine objects have compatible $z$-degrees, the renormalized R-matrix induces a morphism in $\operatorname{Aff}(\mathscr C)$
  $$
  \widehat M\otimes_z\widehat N
  \to
  \widehat N\otimes_z\widehat M.
  $$

These lines are the safest source locations for the `R-Matrix Renormalization` topic.

### 7. Real and affreal simple objects

- `inbox/papers/crystal.tex:1837-1842`: defines a real simple object by simplicity of $M\otimes M$, and defines an affreal simple object as a real simple object with an affinization.
- `inbox/papers/crystal.tex:1958-1965`: states the inverse-head lemma for an affreal simple object and says it is important for defining the crystal structure on $\operatorname{Irr}(\widetilde{\mathcal C}_w)$.
- `inbox/papers/crystal.tex:1967-2010`: gives divisibility/control properties for $\mathfrak d$ and $\Lambda$ when a real simple object has an affinization of degree $2d$.

These statements explain why affine objects and R-matrix degrees are not optional technicalities for localized crystals.

### 8. Quiver-Hecke specialization

- `inbox/papers/crystal.tex:2331-2340`: defines the universal R-matrix for quiver-Hecke modules using intertwiners.
- `inbox/papers/crystal.tex:2348-2363`: recalls the quiver-Hecke module definition of an affinization $(\widehat M,z_{\widehat M})$ of a simple module $M$.
- `inbox/papers/crystal.tex:2366-2371`: identifies this quiver-Hecke affinization with the general affinization notion via the universal R-matrix and the pro-limit $\varprojlim_k\widehat M/z_{\widehat M}^k\widehat M$.
- `inbox/papers/crystal.tex:2373-2375`: gives a safe basic example: the simple module $L(i)=\langle i\rangle$ is affreal.

This is the safest candidate for a future first visible example on the affine-object side. It should be used only after the page introduces the general and quiver-Hecke specialization levels.

### 9. Localization compatibility

- `inbox/papers/crystal.tex:2976-3022`: Proposition `prop:aff-simple` says an affinization of a simple $R$-module passes through the localization functor $Q$ to an affinization in the localized category.
- `inbox/papers/crystal.tex:3317-3337`: Lemma `lem:LaQt` compares R-matrix degrees before and after localization. The proof explicitly uses a renormalized R-matrix and records that $\Lambda(M,N)$ is the homogeneous degree of that renormalized R-matrix.
- `inbox/papers/crystal.tex:3349-3354`: defines the modified localized degree
  $$
  \widetilde\Lambda(X,Y)
  =
  \frac{\Lambda(X,Y)+(\operatorname{wt}X,\operatorname{wt}Y)}{2}
  $$
  for $\Lambda$-definable simple objects of $\widetilde{\mathcal C}_w$.

These lines connect the prerequisites directly to `Root Objects in Localized Categories` and `Localized Root Operators`.

### 10. Root-object dependency

- `inbox/papers/crystal.tex:3546-3553`: the root-object definition requires an affinization $(\widehat L,z)$ with $\deg z=2d_L$ and the R-matrix degree condition $\mathfrak d(L,\mathscr D^{-1}L)=d_L$.
- `inbox/papers/crystal.tex:3654-3657`: in the simple-root-object proposition, the source uses the fact that $\widetilde Q_i$ has an affinization of degree $2\mathsf d_i$ and then reduces the root-object check to an inequality involving $\mathfrak d$.

This confirms that the two prerequisite topics should sit before root objects in the learning order.

## Safe Page Scope

For `Affine Objects in Monoidal Categories`, a later approved topic edit can safely state:

- affine objects are pairs $(\widehat M,z)$ in $\operatorname{Pro}^{\mathrm{coh}}(\mathbf k[z],\mathscr C)$ satisfying a completeness condition and monomorphism condition for $z$;
- $\operatorname{Aff}(\mathscr C)$ is the category of affine objects;
- an affinization of $M$ is an affine object with rational-center data and special fiber $M$;
- real simple objects with affinizations are called affreal;
- in the quiver-Hecke specialization, $L(i)=\langle i\rangle$ is affreal.

For `R-Matrix Renormalization`, a later approved topic edit can safely state:

- for $\Lambda$-definable simple pairs, the R-matrix is a one-dimensional Hom-space generator and $\Lambda(M,N)$ is its degree;
- $\mathfrak d(M,N)$ is the half-sum of the two opposite $\Lambda$-degrees when both directions are definable;
- rational centers allow powers of $z$ to renormalize R-matrices so that specialization at $z=0$ remains nonzero;
- in the localized category, $\widetilde\Lambda(X,Y)$ modifies $\Lambda(X,Y)$ by the weight pairing.

## Do Not Write Yet

- Do not treat every affine object as an affinization of a fixed object $M$; the source separates affine objects from affinizations.
- Do not hide the pro-category level. The definition of affine object is not just "$M$ with a formal parameter"; it lives in $\operatorname{Pro}^{\mathrm{coh}}(\mathbf k[z],\mathscr C)$.
- Do not state a universal R-matrix for arbitrary monoidal categories. The universal R-matrix in the source appears in the quiver-Hecke module specialization.
- Do not use the $L(i)=\langle i\rangle$ affreal example as a general example for every affine object; it is a quiver-Hecke specialization example.
- Do not fill theorem-level consequences about root operators on these prerequisite pages unless the page clearly explains their role as downstream applications.

## Proposed Next Edit After Approval

Fill `content/topics/affine-objects-in-monoidal-categories.md` and `content/topics/r-matrix-renormalization.md` from the source locations above, keeping both pages small:

- `Affine Objects in Monoidal Categories`: overview, pro-category setup, definition of affine object, definition of affinization, the $L(i)=\langle i\rangle$ affreal example, and relation to root objects.
- `R-Matrix Renormalization`: overview, $\Lambda$-definability, $\Lambda$ and $\mathfrak d$, renormalized R-matrix from a rational center, $\widetilde\Lambda$, and relation to root objects/localized root operators.

Do not add new claims and do not download any source.

## Validation

- `git diff --check`: passed.
- `python3 scripts/run_all_checks.py`: passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 51 content files.
- `npx quartz build`: failed with the known Node heap out-of-memory failure in the standalone npx path.
