---
id: localized-root-operators
title: Localized Root Operators
level: advanced
topic_kind: operation
parent_topics:
  - localized-crystals
  - root-objects-in-localized-categories
prerequisite_topics:
  - root-objects-in-localized-categories
  - r-matrix-renormalization
  - quiver-hecke-category-localization
child_topics: []
related_topics:
  - cellular-crystals
maturity: definition-ready
---

## 개요

Localized root operators는 localized category $\widetilde{\mathcal C}_w$의 simple objects 위에 정의되는 maps $\widetilde E_i,\widetilde F_i$이다. 이 maps는 [[topics/root-objects-in-localized-categories|root object]]와 localized simple-root object $\widetilde Q_i$를 사용하여, category-level convolution으로 crystal-level arrows를 만든다.

Ordinary crystal에서는 $\widetilde e_i,\widetilde f_i$가 crystal graph의 $i$-colored arrows를 만든다. Localized setting에서는 vertices가 combinatorial symbols가 아니라 $\widetilde{\mathcal C}_w$ 안의 simple objects이므로, arrow를 만들려면 simple object를 다른 simple object로 보내는 category-level construction이 필요하다.

## 준비와 notation

$w$를 Weyl group의 원소로 두고, $\widetilde{\mathcal C}_w$를 [[topics/quiver-hecke-category-localization|Quiver-Hecke Category Localization]]에서 얻는 localized monoidal category라고 하자. $\operatorname{Irr}(\widetilde{\mathcal C}_w)$는 $\widetilde{\mathcal C}_w$의 simple objects를 grading shift까지 같은 것으로 본 집합이다.

$I_w$는
$$
I_w=\{i\in I\mid w\Lambda_i\ne\Lambda_i\}
$$
로 정의되는 simple root index set이다. Localized root operators는 $i\in I_w$에 대해 실제로 정의된다.

$i\in I_w$에 대해 localized simple-root object를
$$
\widetilde Q_i=\Phi_w(\langle i\rangle)
$$
로 쓴다. 여기서 $\Phi_w$는 localization functor이고, $\langle i\rangle$는 quiver-Hecke module category 쪽의 simple root object이다. [[topics/root-objects-in-localized-categories|Root Objects in Localized Categories]]에서 설명한 것처럼, $\widetilde Q_i$를 항상 root object라고 말할 수는 없다.

$\mathsf d_i=(\alpha_i,\alpha_i)/2$로 둔다. Simple objects $X,Y$ 사이의 [[topics/r-matrix-renormalization|modified R-matrix degree]]를
$$
\widetilde\Lambda(X,Y)
=\frac{\Lambda(X,Y)+(\operatorname{wt}X,\operatorname{wt}Y)}{2}
$$
로 쓴다. 또한 $\mathfrak d(X,Y)$는 양방향 R-matrix degree에서 얻는 invariant이다.

$\nabla$는 convolution product의 simple head를 나타낸다. 따라서 $A\nabla B$는 $A\circ B$ 자체가 아니라 그 simple head이다. $\mathscr D$는 localized category의 duality functor이다.

## map의 정의

$i\in I_w$이고 $X\in\operatorname{Irr}(\widetilde{\mathcal C}_w)$라고 하자. 먼저
$$
\varepsilon_i(X)=\mathsf d_i^{-1}\widetilde\Lambda(\widetilde Q_i,X),
\qquad
\varepsilon_i^*(X)=\mathsf d_i^{-1}\widetilde\Lambda(X,\widetilde Q_i)
$$
를 정의한다. Weight pairing을 이용하여
$$
\varphi_i(X)=\varepsilon_i(X)+\langle h_i,\operatorname{wt}X\rangle,
\qquad
\varphi_i^*(X)=\varepsilon_i^*(X)+\langle h_i,\operatorname{wt}X\rangle
$$
로 둔다. 또한
$$
d_i(X)
=\mathsf d_i^{-1}\mathfrak d(\widetilde Q_i,X)
=\varepsilon_i(X)+\varepsilon_i^*(X)+\langle h_i,\operatorname{wt}X\rangle
$$
로 둔다.

Localized root operators는 다음 maps이다.
$$
\widetilde F_iX
=q_i^{\varepsilon_i(X)}\,\widetilde Q_i\nabla X,
\qquad
\widetilde E_iX
=q_i^{\varphi_i(X)+1}\,X\nabla\mathscr D\widetilde Q_i.
$$
여기서 $q_i$의 거듭제곱은 $i$ 방향의 grading shift를 나타낸다.

오른쪽 convolution 방향을 쓰는 starred operators도 함께 정의된다.
$$
\widetilde F_i^*X
=q_i^{\varepsilon_i^*(X)}\,X\nabla\widetilde Q_i,
\qquad
\widetilde E_i^*X
=q_i^{\varphi_i^*(X)+1}\,\mathscr D^{-1}\widetilde Q_i\nabla X.
$$

$i\notin I_w$인 경우에는
$$
\widetilde F_iX=\widetilde E_iX=0,
\qquad
\varepsilon_i(X)=\varepsilon_i^*(X)=d_i(X)=-\infty
$$
로 둔다.

## 핵심 관점

Localized root operator의 핵심은 crystal graph의 arrow를 localized category 안의 head convolution으로 구현하는 것이다. Ordinary crystal에서는 $\widetilde f_i$가 vertex를 다른 vertex로 보내는 combinatorial map이지만, 여기서는 vertex가 $\widetilde{\mathcal C}_w$의 simple object이므로, $\widetilde Q_i$와 convolution의 simple head를 이용해 새 simple object를 만든다.

정의에서 $\varepsilon_i(X)$와 $\varepsilon_i^*(X)$는 $\widetilde Q_i$가 $X$의 왼쪽 또는 오른쪽에서 얼마나 강하게 상호작용하는지를 modified R-matrix degree로 측정한다. 그 값이 grading shift와 head convolution에 들어가면서 $\widetilde F_iX$와 $\widetilde F_i^*X$가 만들어진다. $\widetilde E_i$와 $\widetilde E_i^*$는 duality functor $\mathscr D$를 사용해 반대 방향으로 돌아가는 operators이다.

따라서 localized root operator는 단순히 object를 하나 더 tensoring하는 조작이 아니다. R-matrix degree, duality, head convolution이 함께 맞아야 crystal axiom에 맞는 arrow가 되며, inverse property와 crystal-structure theorem은 이 data가 실제 crystal structure를 만든다는 사실을 보장한다.

## 기본 성질

- $\widetilde F_i$와 $\widetilde E_i$는 서로 inverse이다.
- $\widetilde F_i^*$와 $\widetilde E_i^*$도 서로 inverse이다.
- 위 data는 $\operatorname{Irr}(\widetilde{\mathcal C}_w)$ 위의 crystal structure를 정의한다.

## 다른 topic들과의 관계

- [[topics/root-objects-in-localized-categories|Root Objects in Localized Categories]]는 operators에 들어가는 $\widetilde Q_i$와 duality/R-matrix degree 조건을 이해하기 위한 object-level prerequisite이다.
- [[topics/localized-crystals|Localized Crystals]]는 이 operators를 모아 $\operatorname{Irr}(\widetilde{\mathcal C}_w)$ 위의 crystal structure로 보는 construction topic이다.
- [[topics/cellular-crystals|Cellular Crystals]]는 localized crystal이 비교되는 combinatorial-level target을 제공한다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/root-objects-in-localized-categories|Root Objects in Localized Categories]]에서 $\widetilde Q_i$와 root-object 주의점을 읽고, [[topics/r-matrix-renormalization|R-Matrix Renormalization]]에서 $\Lambda$, $\mathfrak d$, $\widetilde\Lambda$를 읽고, [[topics/quiver-hecke-category-localization|Quiver-Hecke Category Localization]]에서 $\widetilde{\mathcal C}_w$를 읽는다.
- 상위 개념: [[topics/localized-crystals|Localized Crystals]]와 [[topics/root-objects-in-localized-categories|Root Objects in Localized Categories]]가 더 넓은 setting이다.
- 다음에 읽을 것: [[topics/crystal-comparison-map|Crystal Comparison Map]]에서는 cellular crystal과의 비교를 읽는다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/kashiwara-nakashima25-crystal-structure-localized-quantum-unipotent-coordinate-category|Kashiwara-Nakashima 2025]], Section 5.1-5.2: localized category $\widetilde{\mathcal C}_w$ and localization functors.
- Kashiwara-Nakashima 2025, Section 6.1: root-object prerequisite and caution about $\widetilde Q_i$.
- Kashiwara-Nakashima 2025, Definition labeled `def:rootop`: localized root operators and starred operators.
- Kashiwara-Nakashima 2025, proposition following the definition: inverse property for $\widetilde E_i,\widetilde F_i$ and for $\widetilde E_i^*,\widetilde F_i^*$.
- Kashiwara-Nakashima 2025, theorem following the definition: crystal structure on $\operatorname{Irr}(\widetilde{\mathcal C}_w)$.
- Source-location review: `reports/reviews/2026-06-01-localized-root-operators-source-location-review.md`.

</details>
