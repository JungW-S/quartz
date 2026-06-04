# Localized Crystals Example 9.6 Expansion Review

Date: 2026-06-03

## Scope

This was a report-only wording review for `Localized Crystals`.

Only Kashiwara-Nakashima 2025 Example 9.6 in the local TeX source `inbox/papers/crystal.tex` was checked. No topic page, claim, source note, repository PDF, Sage code, image, or example was changed.

## Current Page State

`content/topics/08-localization-of-categories/localized-crystals.md` already contains the compact type $A_3$ example from Example 9.6:

- the type $A_3$ setup;
- the reduced word $w=s_2w_0=s_1s_2s_3s_2s_1$;
- one explicit $\operatorname{CP}$ formula for a cluster monomial;
- a visible `검증: 논문 예시` label.

Therefore the next safe edit is not to add a new example, but to make the existing example slightly more concrete by adding the source's category condition and cluster label context.

## Source Locations

- `inbox/papers/crystal.tex`, lines 4819-4827: starts Example 9.6, sets $\mathfrak g=A_3$, $w=s_2w_0=s_1s_2s_3s_2s_1$, and identifies
  $$
  \mathcal C_w=\{M\in R\text{-gmod}\mid E_2M\simeq0\}.
  $$
  It also names the frozen variables $\langle321\rangle$, $\langle132\rangle$, and $\langle123\rangle$.
- `inbox/papers/crystal.tex`, lines 4828-4829: displays the four-cluster square with cluster labels $C_1,C_2,C_3,C_4$.
- `inbox/papers/crystal.tex`, lines 4831-4840: gives four explicit $\operatorname{CP}$ formulas for the four cluster monomial charts.
- `inbox/papers/crystal.tex`, lines 4842-4847: records the cellular-crystal coordinates corresponding to the three frozen variables.
- `inbox/papers/crystal.tex`, lines 4849-4851: states $x,y\in\mathbb Z_{\ge0}$, $a,b,c\in\mathbb Z$, and that each $C_k$ consists of a commuting family of simple modules.
- `inbox/papers/crystal.tex`, lines 4853-4865: gives the images $\operatorname{CP}(C_k)$ as four regions in the five-coordinate cellular crystal, cut out by two linear inequalities.
- `inbox/papers/crystal.tex`, lines 4866-4872: draws the two-inequality region picture for the four clusters.

## Decision

A minimal topic-page expansion is safe, but it should stay compact.

The recommended edit should:

- keep the existing single $\operatorname{CP}$ formula rather than adding all four formulas;
- add the source's category condition $\mathcal C_w=\{M\mid E_2M\simeq0\}$;
- say that the displayed monomial belongs to the source's $C_1$ chart;
- mention only in one sentence that the source also gives the other three chart formulas and the four-region image.

The full region partition from lines 4853-4872 is source-backed, but it should not be inserted into the basic example yet. It needs more explanation of cluster charts and the two inequalities, so it belongs to a later optional `성질이 작동하는 방식` or mechanism-oriented expansion.

## Proposed Approved Wording

If the user approves the actual edit, replace only the visible `## 기본 예시` body in `content/topics/08-localization-of-categories/localized-crystals.md` with the following compact version.

```markdown
### 실제 예시: type $A_3$

Kashiwara-Nakashima는 $\mathfrak g=A_3$이고
$$
w=s_2w_0=s_1s_2s_3s_2s_1
$$
인 경우를 예로 든다. 이때 source에서 쓰는 subcategory는
$$
\mathcal C_w=\{M\in R\text{-gmod}\mid E_2M\simeq0\}
$$
이고, localized category $\widetilde{\mathcal C}_w$는 네 개의 clusters를 갖는 cluster algebra를 monoidal categorification한다.

Source notation에서 frozen variables는
$$
\Delta_{\Lambda_1}=\langle321\rangle,\qquad
\Delta_{\Lambda_2}=\langle132\rangle,\qquad
\Delta_{\Lambda_3}=\langle123\rangle
$$
이다. $C_1$ chart의 monomial은
$$
\langle1\rangle^x\circ
\langle3\rangle^y\circ
\langle321\rangle^a\circ
\langle132\rangle^b\circ
\langle123\rangle^c
$$
처럼 쓸 수 있다. 여기서 $x,y\in\mathbb Z_{\ge0}$이고 $a,b,c\in\mathbb Z$이다.

이 monomial에 대해 comparison map은
$$
\operatorname{CP}(
\langle1\rangle^x\circ
\langle3\rangle^y\circ
\langle321\rangle^a\circ
\langle132\rangle^b\circ
\langle123\rangle^c)
=(c+b,c,y+a+b+c,a+b,x+a)
$$
를 준다. 따라서 이 example에서는 localized category 안의 cluster monomial이 five-coordinate cellular-crystal point로 바뀐다.

같은 source는 나머지 세 cluster charts에 대해서도 analogous formulas를 주며, 네 charts의 images를 cellular crystal 안의 네 regions로 나타낸다. 이 전체 region picture는 cluster-chart mechanism을 더 설명해야 하므로 여기서는 formula 하나만 기본 예시로 둔다.

검증: 논문 예시
```

## Do Not Add Yet

- Do not add all four $\operatorname{CP}$ formulas in the basic example.
- Do not add the four-region inequality partition from lines 4853-4865 until the page has a mechanism-oriented section explaining the two inequalities.
- Do not reproduce the diagram from lines 4866-4872 as a generated or redrawn visual without a separate source-figure or code-verified visual workflow.
- Do not turn Example 9.6 into a general theorem about all cluster charts.

## Recommended Next Step

Apply only the compact approved wording above if the user wants the page edited.

After that, keep the full four-region partition deferred unless the user explicitly requests a mechanism section for Example 9.6.
