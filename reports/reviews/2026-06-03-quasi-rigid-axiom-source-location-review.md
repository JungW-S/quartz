# Quasi-Rigid Axiom Source-Location Review

Date: 2026-06-03

## Scope

This report records the exact KN25 source locations for the quasi-rigid monoidal category axiom and its dependency role in the localized-crystal study path.

Only `inbox/papers/crystal.tex` and existing registries were checked. No topic page was edited. No claims were added. No sources were downloaded.

## Current Page State

`content/topics/03-category-theory/quasi-rigid-monoidal-categories.md` is still a title-only stub. This is intentional until the exact axiom and its local role are verified.

The page should not become a broad survey of rigidity in monoidal categories. In KN25, quasi-rigidity is a technical ambient axiom that lets R-matrix images control simple heads, simple socles, and degree estimates for affreal objects.

## Source Locations

- `inbox/papers/crystal.tex:1168-1177`: the introduction explains why affinizations, R-matrices, and rigidity are needed; it says that if $M$ is affreal and $N$ is simple in a quasi-rigid category, then an R-matrix $r_{M,N}$ exists.
- `inbox/papers/crystal.tex:1845-1847`: starts the subsection "Quasi-rigid Axiom" after recalling duality in monoidal categories.
- `inbox/papers/crystal.tex:1850-1863`: Lemma `lem:MNDM` records how $\Lambda$-definability behaves with duality in a rigid category.
- `inbox/papers/crystal.tex:1864-1876`: defines a quasi-rigid monoidal category. The axiom requires:
  - an abelian monoidal category with bi-exact tensor product;
  - a subobject-intersection/extraction condition for $X\subset L\otimes M$ and $Y\subset M\otimes N$;
  - the left-right analogue for $X\subset M\otimes N$ and $Y\subset L\otimes M$.
- `inbox/papers/crystal.tex:1882-1891`: Lemma `lem:monoepi` uses quasi-rigidity to prove that a certain two-step tensor composition of nonzero morphisms does not vanish when the middle factor is simple.
- `inbox/papers/crystal.tex:1893-1895`: Lemma `lem:q-rigid>rigid` states that an abelian rigid monoidal category is quasi-rigid.
- `inbox/papers/crystal.tex:1900-1905`: Example `ex:q-rigid` says that $R\text{-gMod}$, $R\text{-gmod}$, and $\mathcal C_w$ are quasi-rigid; since $\widetilde{\mathcal C}_w$ is rigid, it is also quasi-rigid.
- `inbox/papers/crystal.tex:1911-1952`: Proposition `prop:simplehd` uses quasi-rigidity plus an affreal object to control simple heads, simple socles, R-matrix images, $\Lambda$-degrees, and endomorphism rings.
- `inbox/papers/crystal.tex:1958-1965`: Lemma `lem:invhvonv` says quasi-rigidity gives inverse behavior for head convolution with an affreal simple object, and explicitly notes that this is important for defining the crystal structure on $\operatorname{Irr}(\widetilde{\mathcal C}_w)$.
- `inbox/papers/crystal.tex:1967-2018`: Proposition `prop:ddd` gives divisibility and nonnegativity control for $\mathfrak d$ and $\Lambda$ when a real simple object has an affinization; the following remark says these results apply to $R\text{-gmod}$, $\mathcal C_w$, and $\widetilde{\mathcal C}_w$.
- `inbox/papers/crystal.tex:2394-2422`: the normal-sequence section starts under a quasi-rigid monoidal-category hypothesis.
- `inbox/papers/crystal.tex:3546-3600`: root-object arguments use the head-convolution and degree-control results from Proposition `prop:simplehd` and Proposition `prop:ddd`.

## Dependency Role

Quasi-rigidity sits between the categorical setup and the localized-crystal construction:

- `Graded Monoidal Categories` supplies the tensor and grading environment.
- `Affine Objects in Monoidal Categories` supplies affreal objects through affinizations.
- `R-Matrix Renormalization` supplies $\Lambda$, $\mathfrak d$, and renormalized R-matrix maps.
- `Quasi-Rigid Monoidal Categories` supplies the axiom that lets those R-matrix maps control heads, socles, and nonvanishing compositions.
- `Root Objects in Localized Categories`, `Normal Sequences`, and `Localized Root Operators` use these consequences.

## Safe Future Page Scope

A later topic edit can safely fill a small definition-ready page with:

- the two subobject conditions in the quasi-rigid axiom;
- the fact that abelian rigid monoidal categories are quasi-rigid;
- the KN25 examples $R\text{-gMod}$, $R\text{-gmod}$, $\mathcal C_w$, and $\widetilde{\mathcal C}_w$;
- the local role: affreal simple objects have controlled R-matrix head/socle behavior in quasi-rigid categories.

Do not add a broad category-theory survey. Do not introduce examples beyond the KN25 examples unless a separate source or code route is approved.

## Next Step

If approved, fill `content/topics/03-category-theory/quasi-rigid-monoidal-categories.md` as a compact definition-ready prerequisite page from this report. Do not add claims or new sources.
