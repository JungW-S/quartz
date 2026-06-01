# Demazure Subcategories Source-Location Review

Date: 2026-06-01

## Scope

This report reviews exact source locations for the title-only topic `content/topics/demazure-subcategories-of-quiver-hecke-modules.md`.

Only `inbox/papers/crystal.tex` and already ingested source-note context were checked. No topic page was edited. No claims were added. No sources were downloaded.

## Notation Decision

The source notation for the category used before the comparison map is
$$
\mathfrak B_w,
$$
not $\mathcal C_{\mathcal B_w}$.

The macro is defined at `inbox/papers/crystal.tex:922` as `\CBw=\mathfrak{B}_w`. A later approved topic edit should use $\mathfrak B_w$ as the reader-facing notation and should normalize any local prose that currently says $\mathcal C_{\mathcal B_w}$.

## Source Locations

### 1. Demazure crystal background

- `inbox/papers/crystal.tex:1359-1373`: recalls the Kashiwara 1993 Demazure crystal subset $B_w(\infty)\subset B(\infty)$.
  It is characterized by:
  $$
  B_1(\infty)=\{u_\infty\}
  $$
  and, when $s_iw<w$,
  $$
  B_w(\infty)=\bigcup_{k\ge0}\widetilde f_i^k B_{s_iw}(\infty).
  $$
  The same proposition records $\widetilde e_i B_w(\infty)\subset B_{s_iw}(\infty)$ and monotonicity under Bruhat order.
- `inbox/papers/crystal.tex:2188-2209`: recalls the Lauda-Vazirani crystal isomorphism
  $$
  \Psi:\operatorname{Irr}(R\text{-gmod})\xrightarrow{\sim}B(\infty),
  $$
  where simple modules are taken up to grading shifts.
- `inbox/papers/crystal.tex:3096-3101`: fixes the notation $S(b)$ for the self-dual simple $R$-module corresponding to $b\in B(\infty)$ and points back to the subset $B_w(\infty)$.

### 2. Equivalent membership conditions for simple modules

- `inbox/papers/crystal.tex:3102-3123`: Proposition 5.8 gives equivalent conditions for a simple $R$-module $M$ to lie on the $w$-Demazure side. The equivalent conditions include:
  - nonzero idempotent support of the form $e(i_1^{n_1},\ldots,i_\ell^{n_\ell})M$ for a reduced expression $\underline w=s_{i_1}\cdots s_{i_\ell}$;
  - reduction to the unit object by maximal root operators;
  - being a quotient of
    $$
    \langle i_1^{n_1}\rangle\circ\cdots\circ\langle i_\ell^{n_\ell}\rangle;
    $$
  - being isomorphic up to grading shift to $S(b)$ for some $b\in B_w(\infty)$;
  - nonvanishing and simplicity after the localization functor $Q$;
  - determinantial-module conditions involving $\mathsf C^w_\Lambda$.

This proposition is the safest source-backed membership criterion for the future topic definition.

### 3. Definition of $\mathfrak B_w$

- `inbox/papers/crystal.tex:3126-3128`: defines $\mathfrak B_w$ as the full subcategory of $R\text{-gmod}$ consisting of modules $M$ such that every simple subquotient $S$ of $M$ satisfies the equivalent conditions in Proposition 5.8.

Thus $\mathfrak B_w$ is a category-level enlargement that packages the Demazure crystal side inside $R\text{-gmod}$.

### 4. Simple classes and inclusion of $\mathcal C_w$

- `inbox/papers/crystal.tex:3130-3139`: defines $\operatorname{Irr}(\mathcal C_w)$ and $\operatorname{Irr}(\mathfrak B_w)$ as simple modules up to grading shifts, and records
  $$
  \operatorname{Irr}(\mathcal C_w)\subset\operatorname{Irr}(\mathfrak B_w).
  $$

### 5. Crystal relation with $B_w(\infty)$

- `inbox/papers/crystal.tex:3141-3147`: states the crystal isomorphism
  $$
  \operatorname{Irr}(\mathfrak B_w)\simeq B_w(\infty),
  $$
  and then states that $\operatorname{Irr}(\mathfrak B_w)\sqcup\{0\}$ is stable under $\widetilde E_i$ and $\widetilde E_i^*$.

This is the main bridge from the quiver-Hecke category side to the Demazure crystal.

### 6. Why $\mathfrak B_w$ is larger than $\mathcal C_w$

- `inbox/papers/crystal.tex:3190-3193`: gives a type $A_2$ warning/example:
  for $\mathfrak g=A_2$ and $w=s_1s_2$,
  $$
  \langle12\rangle\in\mathcal C_w,\qquad
  \widetilde E_1\langle12\rangle\simeq\langle2\rangle\notin\mathcal C_w,
  $$
  but $\langle2\rangle\in\mathfrak B_w$.

This is a good candidate for a later basic example because it shows why $\mathfrak B_w$ is needed.

### 7. Determinantial-module examples inside $\mathfrak B_w$

- `inbox/papers/crystal.tex:3196-3200`: states that for any $w$-dominant $\lambda$,
  $$
  \mathsf M_w(w\lambda,\lambda)\in\mathfrak B_w.
  $$

This can be used later as a bridge to `Determinantial Modules`, but it should not be the first visible example unless determinantial notation is already explained on the page.

### 8. Truncation and starred root-operator input

- `inbox/papers/crystal.tex:3202-3210`: if $w'=ws_i<w$, then:
  - if simple $S\in\mathfrak B_w$ satisfies $\varepsilon_i^*(S)=0$, then $S\in\mathfrak B_{w'}$;
  - if $S\in\mathfrak B_w$ is simple, then $(\widetilde F_i^*)^m(S)\simeq S\circ\langle i^m\rangle\in\mathfrak B_w$ for $m\ge0$.
- `inbox/papers/crystal.tex:3945-3971`: uses this to define
  $$
  \widetilde E_i^{*\max}:\operatorname{Irr}(\mathfrak B_w)\to\operatorname{Irr}(\mathfrak B_{w'})
  $$
  and then extends it to the localized map
  $$
  E_i^*:\operatorname{Irr}(\widetilde{\mathcal C}_w)\to\operatorname{Irr}(\widetilde{\mathcal C}_{w'}).
  $$
- `inbox/papers/crystal.tex:4055-4061`: gives a commutative diagram relating $\operatorname{Irr}(\mathfrak B_w)$, $\operatorname{Irr}(\widetilde{\mathcal C}_w)$, and the map $E_i^*$.

These statements explain why $\mathfrak B_w$ is the category input for the recursive comparison-map construction.

### 9. Use in the comparison map

- `inbox/papers/crystal.tex:4114-4128`: recalls the cellular crystal $\mathcal B_{\underline w}$ and defines $\operatorname{CP}(M)$ for a simple $M\in\mathfrak B_w$ by recursively applying starred localized root operators and recording the coordinates.
- `inbox/papers/crystal.tex:4129-4145`: states the inclusions
  $$
  \operatorname{Irr}(\mathcal C_w)\hookrightarrow
  \operatorname{Irr}(\mathfrak B_w)\hookrightarrow
  \mathcal B_{\underline w}
  $$
  and gives the commutative diagram extending $\operatorname{CP}$ from $\operatorname{Irr}(\mathcal C_w)$ to $\operatorname{Irr}(\widetilde{\mathcal C}_w)$.

## Safe Page Scope

The future topic page should state:

- $\mathfrak B_w$ is a full subcategory of $R\text{-gmod}$.
- A module belongs to $\mathfrak B_w$ when all simple subquotients satisfy the equivalent Demazure-side conditions of Proposition 5.8.
- The simple classes $\operatorname{Irr}(\mathfrak B_w)$ form the Demazure crystal $B_w(\infty)$.
- $\operatorname{Irr}(\mathcal C_w)$ sits inside $\operatorname{Irr}(\mathfrak B_w)$.
- $\mathfrak B_w$ is the category-side input from which $\operatorname{CP}$ first extracts cellular-crystal coordinates.

## Proposed Next Edit After Approval

Fill only these sections of `content/topics/demazure-subcategories-of-quiver-hecke-modules.md`:

- `개요`: characterize $\mathfrak B_w$ as the quiver-Hecke module subcategory whose simple objects model the Demazure crystal $B_w(\infty)$.
- `준비와 notation`: introduce $B(\infty)$, $B_w(\infty)$, $S(b)$, $\operatorname{Irr}(R\text{-gmod})$, $\mathcal C_w$, and $\mathfrak B_w$.
- `정의`: define $\mathfrak B_w$ by the simple-subquotient criterion and give the safest subset of Proposition 5.8's equivalent conditions.
- `기본 예시`: use the type $A_2$ example at `crystal.tex:3190-3193`.
- `핵심 관점`: include the level diagram
  $$
  \operatorname{Irr}(\mathcal C_w)\subset
  \operatorname{Irr}(\mathfrak B_w)\simeq B_w(\infty)
  \to
  \mathcal B_{\underline w}.
  $$
- `기본 성질`: include stability under $\widetilde E_i,\widetilde E_i^*$ and the role of $\widetilde E_i^{*\max}$ in passing from $w$ to $w'=ws_i$.
- `다른 topic들과의 관계`: link `Quiver-Hecke Subcategories`, `Crystal Bases`, `Cellular Crystals`, and `Crystal Comparison Map`.
- `Source notes`: cite the exact source locations above.

Also update `content/topics/crystal-comparison-map.md` to replace the local alias $\mathcal C_{\mathcal B_w}$ with source notation $\mathfrak B_w$.

## Do Not Write Yet

- Do not call $\mathfrak B_w$ a localization; it is a full subcategory of $R\text{-gmod}$.
- Do not identify $\mathfrak B_w$ with $\mathcal C_w$.
- Do not keep the unsupported notation $\mathcal C_{\mathcal B_w}$ unless it is explicitly introduced as a local alias; the source notation is $\mathfrak B_w$.
- Do not use the determinantial-module family as the first visible example unless its notation is reintroduced.

## Validation

- `git diff --check`: passed.
- `python3 scripts/run_all_checks.py`: passed, including generated maps, generated topic status, link validation, and its internal Quartz build over 51 content files.
- `npx quartz build`: failed with the known Node heap out-of-memory failure in the standalone npx path.
