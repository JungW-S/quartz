# Pro-Categories and Graded Monoidal Categories Fillability Review

Date: 2026-06-01

## Scope

This report checks whether the title-only prerequisite pages

- `content/topics/03-category-theory/pro-categories.md`
- `content/topics/03-category-theory/graded-monoidal-categories.md`

can receive minimal source-backed prerequisite definitions for reading

- `content/topics/03-category-theory/affine-objects-in-monoidal-categories.md`
- `content/topics/06-quiver-hecke-klr-algebras/r-matrix-renormalization.md`

Only already reviewed Kashiwara-Nakashima 2025 source locations in `inbox/papers/crystal.tex` were used. No topic page was edited. No claim was added. No source was downloaded.

## Decision

Both prerequisite pages can be filled in a small approved edit.

- `Pro-Categories` can safely become `definition-ready`.
- `Graded Monoidal Categories` can safely become `definition-ready`, but only for the finite-length graded monoidal setting used by Kashiwara-Nakashima 2025.

Neither page should be expanded into a broad category-theory article from this source alone. The safe purpose is to give enough language for affine objects, R-matrix degrees, rational centers, and root-object prerequisites.

## Pro-Categories

### Safe Source Locations

- `inbox/papers/crystal.tex:1526-1548`: defines the Yoneda functor, directed and co-directed categories, pro-objects, the category $\operatorname{Pro}(\mathscr C)$, and the notation $\varprojlim$ for co-directed projective limits.
- `inbox/papers/crystal.tex:1550-1577`: records the finite-length graded category assumptions and says that $\mathscr C$ sits inside $\operatorname{Pro}(\mathscr C)$ as a full subcategory stable under subquotients.
- `inbox/papers/crystal.tex:1578-1621`: defines $\operatorname{Mod}^{\mathrm{gr}}(A,\operatorname{Pro}(\mathscr C))$ and $\operatorname{Pro}^{\mathrm{coh}}(A,\mathscr C)$ by the quotient and completion conditions.

### What Can Be Written

A minimal `Pro-Categories` page can safely explain:

- a pro-object of $\mathscr C$ is an object in the functor category used by the Yoneda embedding that is isomorphic to a co-directed projective limit of objects of $\mathscr C$;
- $\operatorname{Pro}(\mathscr C)$ is the full subcategory of such pro-objects;
- $\varprojlim$ is the notation for co-directed projective limits in $\operatorname{Pro}(\mathscr C)$;
- in the affine-object setup, $\operatorname{Pro}^{\mathrm{coh}}(A,\mathscr C)$ consists of graded $A$-modules in $\operatorname{Pro}(\mathscr C)$ whose special quotient lies in $\mathscr C$ and which are recovered from their $A$-adic quotients.

This is enough to support the definition of an affine object as an object of $\operatorname{Pro}^{\mathrm{coh}}(\mathbf k[z],\mathscr C)$.

### What Should Stay Out

Do not add yet:

- general examples such as profinite sets or inverse systems of vector spaces unless a lower-level category-theory source is approved;
- broad universal-property statements for pro-categories beyond the source's definition;
- theorem-level facts about exactness, limits, or abelian structure not stated in the checked source locations.

### Recommended Page Level After Edit

`definition-ready`.

The page can include a labeled `구조 예시` explaining the mechanism of a co-directed inverse system, but it should not claim a concrete real example unless another source is approved.

## Graded Monoidal Categories

### Safe Source Locations

- `inbox/papers/crystal.tex:1550-1577`: finite-length graded $\mathbf k$-linear category assumptions; grading shift functor $q$; graded morphism space $\operatorname{HOM}_{\mathscr C}(M,N)$.
- `inbox/papers/crystal.tex:1646-1669`: graded monoidal category assumptions: abelian $\mathbf k$-linear graded category, bi-exact $\mathbf k$-bilinear tensor product, simple unit object, and compatibility of tensor product with the grading shift $q$.
- `inbox/papers/crystal.tex:1670-1676`: identifies the grading shift with the invertible central object $q\mathbf 1$ and states that $\operatorname{Pro}(\mathscr C)$ also has a bi-exact monoidal structure.
- `inbox/papers/crystal.tex:1679-1690`: defines left and right duals and rigidity.
- `inbox/papers/crystal.tex:1717-1728`: records that $\operatorname{Aff}(\mathscr C)$ has a monoidal product and becomes rigid when $\mathscr C$ is rigid.

### What Can Be Written

A minimal `Graded Monoidal Categories` page can safely explain:

- the ambient category $\mathscr C$ is a finite-length abelian $\mathbf k$-linear graded category with a grading shift autoequivalence $q$;
- graded morphisms are collected as
  $$
  \operatorname{HOM}_{\mathscr C}(M,N)
  =
  \bigoplus_{n\in\mathbb Z}\operatorname{Hom}_{\mathscr C}(q^nM,N);
  $$
- a graded monoidal category in the reviewed setup has a $\mathbf k$-bilinear bi-exact tensor product $\otimes$, a simple unit object $\mathbf 1$, and compatibility
  $$
  q(X\otimes Y)\simeq (qX)\otimes Y\simeq X\otimes(qY);
  $$
- the shift $q$ may be regarded as tensoring by the invertible central object $q\mathbf 1$;
- rigidity means having compatible left and right duals;
- these assumptions are the ambient language for affine objects, rational centers, R-matrix degrees, and localized root-object constructions.

### What Should Stay Out

Do not add yet:

- a general survey of monoidal categories;
- examples of graded monoidal categories not explicitly supported by approved sources in the intended wording;
- claims that all graded monoidal categories are finite-length, abelian, rigid, or have simple units;
- theorem-level consequences about R-matrices or affinizations that belong on the affine-object or R-matrix pages.

### Recommended Page Level After Edit

`definition-ready`.

The page should not be marked `example-ready` unless a real source-backed example is added. A structural example of $q$-compatibility may be included as `구조 예시` if it is explicitly framed as mechanism, not as a concrete sourced example.

## Title Check

`Pro-Categories` is acceptable for the current page because the source directly defines pro-objects and $\operatorname{Pro}(\mathscr C)$.

`Graded Monoidal Categories` is acceptable only if the first paragraph makes clear that the page treats the restricted finite-length graded monoidal setting used in the later pages. If a later pass wants stricter title accuracy, `Finite-Length Graded Monoidal Categories` would be more precise, but a rename is not necessary before the minimal prerequisite edit.

## Proposed Approved Edit

If approved, the next edit should:

1. Fill only `content/topics/03-category-theory/pro-categories.md` and `content/topics/03-category-theory/graded-monoidal-categories.md`.
2. Use only the source locations listed in this report.
3. Add no claims to `data/claims.yml`.
4. Add no new source notes.
5. Update `data/topics.yml`, `data/topic_maturity.yml`, `data/research_queue.yml`, `data/review_backlog.yml`, and `reports/roadmap/next-actions.md` only as needed.
6. Keep both pages compact and prerequisite-focused.

## Safe Next Prompt

```text
Using reports/reviews/2026-06-01-pro-graded-prerequisite-fillability-review.md, fill only content/topics/03-category-theory/pro-categories.md and content/topics/03-category-theory/graded-monoidal-categories.md with compact source-backed prerequisite definitions. Use only Kashiwara-Nakashima 2025 source locations listed in the report. Do not add claims, do not download sources, and do not expand beyond definition-ready level.
```

## Validation

- `git diff --check`: passed.
- `python3 scripts/run_all_checks.py`: passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 51 content files.
- `npx quartz build`: failed with the known standalone Node heap out-of-memory failure.
