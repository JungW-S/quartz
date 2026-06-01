---
title: Notation
---

This page records local notation conventions for the study wiki. Source notes may quote a paper's notation, but reader-facing topic pages should use the local display conventions below.

## Grothendieck Rings

- Use $K_0(\mathcal C)$ for the Grothendieck ring of a monoidal category $\mathcal C$ in topic-page prose.
- Use $K_0(\mathcal C_{w,v})$ for the Grothendieck ring attached to the KKOP18 category $\mathcal C_{w,v}$.
- KKKO14 writes $K(\mathcal C)$; source notes may mention this, but topic pages normalize it to $K_0(\mathcal C)$.

## Category Notation

- Use $\mathcal C_{w,v}$, not `Cw,v`.
- Use $\mathcal C_w$, not `Cw`.
- Use $\widetilde{\mathcal C}_w$, not `tCw` or `\tCw`, for the localized category in Kashiwara-Nakashima 2025.
- Use $\mathcal C_{*,v}$, not `C*,v`.
- Use $\mathcal C_u$, not `Cu`.
- Use $R\text{-gmod}$ for the graded quiver-Hecke/KLR module category.

## Crystal Notation

- Use $\operatorname{Irr}(\widetilde{\mathcal C}_w)$ for simple objects of the localized category up to grading shifts.
- Use $\mathcal B_w$ for the cellular crystal associated with $w$.
- Use $\widetilde E_i$ and $\widetilde F_i$ for localized crystal operators when the source context is Kashiwara-Nakashima 2025.
- Use $\widetilde e_i$ and $\widetilde f_i$ for ordinary crystal operators.
- Use Kashiwara tensor-product convention for ordinary crystal tensor products. Bump-Schilling, Schilling notes, and SageMath may use the opposite convention, so formulas from those references need an explicit translation note before appearing in topic prose.

## Kashiwara-Nakashima Localized Categories

- Use $\mathfrak B_w$ for the Demazure-side full subcategory in Kashiwara-Nakashima 2025; do not use the deprecated local alias $\mathcal C_{\mathcal B_w}$.
- Use $\Phi_w:\mathcal C_w\to\widetilde{\mathcal C}_w$ for the localization functor from $\mathcal C_w$ to the localized category.
- Use $\widetilde Q_i$ for the localized simple-root object. Introduce it before use, usually as $\widetilde Q_i=\Phi_w(\langle i\rangle)$ in localized-root-operator contexts.
- Use $\mathsf d_i$ for the scalar root-direction degree, $\widetilde\Lambda(X,Y)$ for the modified localized R-matrix degree, and $\mathfrak d(X,Y)$ for the two-sided R-matrix degree invariant.
- Use $A\nabla B$ for the simple head of the convolution product $A\circ B$.
- Use $\operatorname{CP}$ for the comparison map from localized simple objects to cellular-crystal coordinates.
- Use $\psi_*$ for the reverse monoidal equivalence; do not identify it with the duality functor $\mathscr D^{\pm1}$.

## Algebra Targets

- Use $A_{w,v}$, not `Aw,v`.
- Use $A_q(\mathfrak n(w))$ for the GLS11 quantum coordinate ring of a quantum unipotent subgroup.
- Do not identify $A_{w,v}$ with $A_q(\mathfrak n(w))$ unless a source-backed comparison has been explicitly imported.

## Products And Shifts

- Use $M\circ N$ for convolution product of module objects.
- Use $[M][N]=[M\circ N]$ for the induced multiplication of Grothendieck-ring classes.
- Write `$q$-commuting` and `grading shift by $q$` in prose.
- Use $q^aM$ only when the source location supports an explicit shifted object.

## Determinantial Modules

- Use $M(w_{\le k}\Lambda, v_{\le k}\Lambda)$ for the indexed determinantial-module family.
- Read $M(w_{\le k}\Lambda, v_{\le k}\Lambda)$ as an object of $\mathcal C_{w,v}$ before passing to its class in $K_0(\mathcal C_{w,v})$.

<!-- CODEX-MANAGED: may append source-backed material here -->

## Source Translation Notes

- KKKO14: source notation $K(\mathcal C)$ is rendered as $K_0(\mathcal C)$ in topic pages.
- KKOP18: source shorthand such as `Cw,v`, `K0(Cw,v)`, and `Aw,v` is rendered as $\mathcal C_{w,v}$, $K_0(\mathcal C_{w,v})$, and $A_{w,v}$.
- Kashiwara-Nakashima 2025: source macros such as `\CBw`, `\Qti`, `\tLa`, `\hconv`, and `\CP` are rendered as $\mathfrak B_w$, $\widetilde Q_i$, $\widetilde\Lambda$, $\nabla$, and $\operatorname{CP}$ in topic pages.
- Crystal tensor products: local topic pages follow Kashiwara's tensor-product convention. Schilling/SageMath convention formulas are not copied verbatim into topic prose without translation.

<!-- NEEDS-HUMAN-REVIEW -->

The comparison between $A_{w,v}$ and other quantum coordinate-ring notation should be reviewed before merging notation across sources.
