---
id: quiver-hecke-subcategories
title: Quiver-Hecke Subcategories
level: advanced
topic_kind: category
parent_topics:
  - quiver-hecke-module-categories
prerequisite_topics:
  - quiver-hecke-module-categories
  - quantum-coordinate-rings
child_topics:
  - determinantial-modules
  - quiver-hecke-category-localization
  - demazure-subcategories-of-quiver-hecke-modules
related_topics:
  - monoidal-categorification
maturity: example-ready
---

## 개요

Quiver-Hecke subcategories는 $R\text{-gmod}$ 안에서 Weyl group data에 따라 골라지는 full monoidal subcategories이다. Localization에서 등장하는 $\mathcal C_w$와 determinantial modules가 놓이는 $\mathcal C_{w,v}$는 quiver-Hecke algebra 자체가 아니라 이 category-level subcategory 층에 속한다.

이 topic은 [[topics/quiver-hecke-module-categories|Quiver-Hecke Module Categories]]와 [[topics/quiver-hecke-category-localization|Quiver-Hecke Category Localization]] 사이의 중간 층이다. 먼저 $R\text{-gmod}$ 안의 $\mathcal C_w$나 $\mathcal C_{w,v}$를 구분해야, 그 다음에 어떤 category를 localization하는지 말할 수 있다.

## 준비와 notation

$W$를 Weyl group이라고 하고, $w,v\in W$를 사용한다. $R\text{-gmod}$는 symmetric quiver-Hecke algebra의 finite-dimensional graded module category이다. $Q_+$는 positive root lattice의 nonnegative cone이고 $Q_-=-Q_+$이다. $\Delta_+$와 $\Delta_-$는 positive roots와 negative roots의 집합이다.

$M\in R(\beta)\text{-gmod}$에 대해 두 support-type 집합을 쓴다.

$$
\mathsf W(M)
=
\{\gamma\in Q_+\cap(\beta-Q_+)\mid e(\gamma,\beta-\gamma)M\ne 0\},
$$

$$
\mathsf W^*(M)
=
\{\gamma\in Q_+\cap(\beta-Q_+)\mid e(\beta-\gamma,\gamma)M\ne 0\}.
$$

여기서 $e(\gamma,\beta-\gamma)$와 $e(\beta-\gamma,\gamma)$는 quiver-Hecke algebra의 idempotent notation이다. 부분집합 $A\subset \mathbb R\otimes Q$에 대해 $\operatorname{Cone}(A)$는 $A\cup\{0\}$를 포함하는 가장 작은 convex cone이다.

이 page에서 쓰는 category notation은 다음과 같다.

- $\mathcal C_w$: $\mathsf W(M)$ 조건으로 정의되는 full monoidal subcategory.
- $\mathcal C_{*,v}$: $\mathsf W^*(M)$ 조건으로 정의되는 full subcategory.
- $\mathcal C_{w,v}$: $\mathcal C_w$와 $\mathcal C_{*,v}$의 교집합으로 정의되는 full subcategory.
- $K_0(\mathcal C_{w,v})$: $\mathcal C_{w,v}$의 Grothendieck ring.
- $A_{w,v}$: $K_0(\mathcal C_{w,v})$와 비교되는 coordinate-ring-level algebra.

## 정의

$w\in W$에 대해 $\mathcal C_w$는 다음 조건을 만족하는 objects로 이루어진 $R\text{-gmod}$의 full subcategory이다.

$$
\mathcal C_w
=
\{M\in R\text{-gmod}\mid
\mathsf W(M)\subset \operatorname{Cone}(\Delta_+\cap w\Delta_-)\}.
$$

동치인 lattice 조건으로는

$$
M\in\mathcal C_w
\Longleftrightarrow
\mathsf W(M)\subset Q_+\cap wQ_-
$$

를 사용할 수 있다.

$v\in W$에 대해 $\mathcal C_{*,v}$는 다음 조건을 만족하는 objects로 이루어진 $R\text{-gmod}$의 full subcategory이다.

$$
\mathcal C_{*,v}
=
\{M\in R\text{-gmod}\mid
\mathsf W^*(M)\subset \operatorname{Cone}(\Delta_+\cap v\Delta_+)\}.
$$

동치인 lattice 조건은

$$
M\in\mathcal C_{*,v}
\Longleftrightarrow
\mathsf W^*(M)\subset Q_+\cap vQ_+
$$

이다.

$w,v\in W$에 대해 $\mathcal C_{w,v}$는 $\mathcal C_w$와 $\mathcal C_{*,v}$ 양쪽에 속하는 objects로 이루어진 $R\text{-gmod}$의 full subcategory이다. 즉 object 조건은

$$
M\in\mathcal C_{w,v}
\Longleftrightarrow
M\in\mathcal C_w
\text{ and }
M\in\mathcal C_{*,v}
$$

이다.

이 정의는 다음 세 층을 분리한다.

- category-level: $\mathcal C_w$, $\mathcal C_{*,v}$, $\mathcal C_{w,v}$;
- Grothendieck-ring-level: $K_0(\mathcal C_{w,v})$;
- coordinate-ring-level: $A_{w,v}$.

## 기본 예시

Type $A_2$에서 $w=s_1s_2s_1$이면 Kashiwara-Nakashima 2025의 example에 따라

$$
\mathcal C_w=R\text{-gmod}
$$

이다. 이 경우 $\mathcal C_w$는 ambient finite-dimensional graded quiver-Hecke module category 전체와 같다.

검증: 논문 예시

## 핵심 관점

$$
\mathcal C_{w,v}
=
\mathcal C_w\cap\mathcal C_{*,v}
\subset
R\text{-gmod}
\quad\rightsquigarrow\quad
K_0(\mathcal C_{w,v})
\quad\leftrightarrow\quad
A_{w,v}
$$

이 diagram의 핵심은 level separation이다. Determinantial module은 category 안의 object이고, 그 class는 Grothendieck ring에 놓이며, 비교 대상 $A_{w,v}$는 coordinate-ring level의 algebra이다.

## 기본 성질

- $\mathcal C_w$, $\mathcal C_{*,v}$, $\mathcal C_{w,v}$는 subquotients, extensions, convolution products, grading shifts에 대해 닫혀 있다.
- 이 닫힘 성질 때문에 이 subcategory들은 monoidal categorification에서 사용할 수 있는 category-level 환경이 된다.
- Grothendieck-ring identification 아래에서 $K_0(\mathcal C_{w,v})$는 $A_{w,v}$와 비교된다.
- Determinantial-module construction에서 나타나는 objects $M(w_{\le k}\Lambda,v_{\le k}\Lambda)$는 $\mathcal C_{w,v}$ 안에 놓이고, 해당 family에는 strong-commutation 성질이 있다.

## 다른 topic들과의 관계

- [[topics/quiver-hecke-module-categories|Quiver-Hecke Module Categories]]는 ambient category $R\text{-gmod}$를 제공한다.
- [[topics/determinantial-modules|Determinantial Modules]]는 $\mathcal C_{w,v}$ 같은 subcategory 안에서 구별되는 objects를 다룬다.
- [[topics/quiver-hecke-category-localization|Quiver-Hecke Category Localization]]은 $\widetilde{\mathcal C}_w$로 가기 전에 $\mathcal C_w$를 category-level input으로 사용한다.
- [[topics/quantum-coordinate-rings|Quantum Coordinate Rings]]는 $A_{w,v}$와 $A_q(\mathfrak n(w))$ 같은 notation이 놓이는 coordinate-ring side를 제공한다.
- [[topics/monoidal-categorification|Monoidal Categorification]]은 monoidal category의 Grothendieck ring을 cluster algebra나 coordinate algebra와 비교하는 이유를 설명한다.

## 더 읽을 topic

- 먼저 읽을 것: $R\text{-gmod}$를 보려면 [[topics/quiver-hecke-module-categories|Quiver-Hecke Module Categories]]를 읽고, coordinate-ring side를 보려면 [[topics/quantum-coordinate-rings|Quantum Coordinate Rings]]를 읽는다.
- 상위 개념: [[topics/quiver-hecke-module-categories|Quiver-Hecke Module Categories]]가 더 넓은 category setting이다.
- 다음에 읽을 것: $\mathcal C_{w,v}$ 안의 objects는 [[topics/determinantial-modules|Determinantial Modules]]에서 이어지고, $\mathcal C_w$의 localization은 [[topics/quiver-hecke-category-localization|Quiver-Hecke Category Localization]]에서 이어진다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/kkop18-monoidal-categories-strata-flag-manifolds|KKOP18]], Section 2.2 and Proposition 2.16: $\mathcal C_{w,v}$ and stability properties of $\mathcal C_w$, $\mathcal C_{*,v}$, and $\mathcal C_{w,v}$.
- KKOP18, Section 2.2: cone conditions and equivalent lattice conditions for $\mathcal C_w$ and $\mathcal C_{*,v}$.
- KKOP18, Theorem 2.20(ii)(c): comparison between $K_0(\mathcal C_{w,v})$ and $A_{w,v}$.
- KKOP18, Proposition 4.8 and Theorem 4.10: determinantial modules inside $\mathcal C_{w,v}$ and strong commutation.
- [[sources/papers/kashiwara-nakashima25-crystal-structure-localized-quantum-unipotent-coordinate-category|Kashiwara-Nakashima 2025]], Sections 5.1-5.2: $\mathcal C_w$ as input to the localized category $\widetilde{\mathcal C}_w$.
- Kashiwara-Nakashima 2025, local TeX lines 3990-3995, reviewed in `reports/reviews/2026-06-01-quiver-hecke-subcategories-example-review.md`: type $A_2$ example where $w=s_1s_2s_1$ gives $\mathcal C_w=R\text{-gmod}$.

</details>
