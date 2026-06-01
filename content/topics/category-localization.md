---
id: category-localization
title: Category Localization
level: core
topic_kind: root
parent_topics: []
prerequisite_topics: []
child_topics:
  - quiver-hecke-category-localization
related_topics:
  - monoidal-categorification
maturity: example-ready
---

## 개요

Category localization은 monoidal category 안의 선택된 objects를 invertible하게 만들기 위해 category 자체를 바꾸는 construction이다. KKOP21에서 쓰는 형태는 단순히 multiplicative subset을 invert하는 ring localization이 아니라, braider data를 가진 objects를 monoidal category 안에서 invertible objects로 만드는 category-level localization이다.

이 construction은 [[topics/quiver-hecke-category-localization|Quiver-Hecke Category Localization]]을 읽기 위한 직접적인 prerequisite이다. Quiver-Hecke setting에서는 $\mathcal C_w$에서 출발해 determinantial modules $M(w\Lambda_i,\Lambda_i)$를 invertible하게 사용할 수 있는 localized category $\widetilde{\mathcal C}_w$로 이동한다.

## 준비와 notation

$\mathcal T$를 monoidal category라고 하자. Tensor product는 $\otimes$로 쓰고, unit object는 $\mathbf 1$로 쓴다.

Localization에 넣는 하나의 object는 그냥 object $C$가 아니라 left braider
$$
(C,R_C)
$$
이다. 여기서 $R_C(X)$는 각 $X\in\mathcal T$에 대해 주어진 morphism
$$
R_C(X):C\otimes X\longrightarrow X\otimes C
$$
이며, $X$에 functorial하고 tensor product 및 unit object와 compatible해야 한다.

Index set $I$에 대해 localization에 넣을 family를
$$
\{(C_i,R_{C_i})\}_{i\in I}
$$
라고 쓴다. 이 family가 real commuting family이면, 각 $C_i$는 자기 자신과 real하게 commute하고 서로도 scalar identity 수준으로 commute한다.

## 구성

KKOP21의 localization input은 monoidal category $\mathcal T$와 real commuting family of braiders
$$
\{(C_i,R_{C_i})\}_{i\in I}
$$
이다. 이 data에서 localized monoidal category
$$
\mathcal T[C_i^{\otimes -1}\mid i\in I]
$$
와 monoidal functor
$$
\Upsilon:\mathcal T\longrightarrow \mathcal T[C_i^{\otimes -1}\mid i\in I]
$$
를 만든다.

이 construction의 defining property는 다음 두 가지이다.

- 각 $\Upsilon(C_i)$는 localized category 안에서 invertible object가 된다.
- 각 braider morphism $R_{C_i}(X):C_i\otimes X\to X\otimes C_i$는 localized category로 보낸 뒤 isomorphism이 된다.

Theorem 2.7의 universal property는 이 construction이 위 조건을 만족시키는 monoidal functor들 중 universal하다고 말한다. 즉, 다른 monoidal functor가 같은 방식으로 $C_i$들을 invertible하게 만들고 $R_{C_i}(X)$들을 isomorphism으로 만들면, 그 functor는 localized category를 통해 유일하게 factor된다.

## 기본 예시

### Quiver-Hecke subcategory example

$R\text{-gmod}$를 quiver-Hecke algebra $R$의 finite-dimensional graded module category라고 하자. Weyl group element $w$에 대해 $\mathcal C_w$는 $R\text{-gmod}$ 안의 monoidal subcategory이고, dominant weight $\Lambda$에 대해 KKOP21은 determinantial module
$$
C_{w,\Lambda}:=M(w\Lambda,\Lambda)
$$
를 사용한다.

Fundamental weight $\Lambda_i$에 대해
$$
C_i:=C_{w,\Lambda_i}=M(w\Lambda_i,\Lambda_i)
$$
라고 두면, Proposition 5.1은 이 $C_i$들이 graded braiders의 real commuting family를 이룬다고 말한다. 따라서 Section 5.1에서
$$
\widetilde{\mathcal C}_w
:=
\mathcal C_w[C_i^{\circ -1}\mid i\in I]
$$
를 정의할 수 있다.

검증: 논문 예시

## 핵심 관점

$$
\mathcal T
\quad\longrightarrow\quad
\mathcal T[C_i^{-1}]
$$

Category localization의 핵심은 object-level data를 category-level construction으로 옮기는 것이다. 왼쪽 category에서 $C_i$는 distinguished object이고, 오른쪽 category에서는 그 image가 tensor inverse를 가진다.

Quiver-Hecke setting에서는 같은 그림이 다음 form으로 나타난다.

$$
\mathcal C_w
\quad\xrightarrow{\;\Phi_w\;}\quad
\widetilde{\mathcal C}_w
$$

여기서 localize되는 것은 quiver-Hecke algebra 자체가 아니라 monoidal subcategory $\mathcal C_w$이다. Algebra-level 또는 Grothendieck-ring-level localization은 이 category-level construction의 shadow로 나타난다.

## 기본 성질

### Category-level

- Theorem 2.7은 $\mathcal T[C_i^{\otimes -1}\mid i\in I]$의 universal property를 준다. 이 property 때문에 localization은 선택된 braider objects를 invertible하게 만드는 가장 표준적인 monoidal category로 읽을 수 있다.
- Theorem 2.12는 graded setting에서도 같은 localization construction이 작동한다고 말한다.
- Proposition 2.13은 원래 graded monoidal category가 abelian이고 tensor product가 exact이면, localized category도 abelian이고 tensor product가 exact이며 localization functor도 exact라고 말한다.

### Quiver-Hecke category-level

- Proposition 5.1은 $C_i=M(w\Lambda_i,\Lambda_i)$가 $\mathcal C_w$의 localization에 필요한 graded braider family를 제공한다고 말한다.
- Corollary 5.11은 $\widetilde{\mathcal C}_w$가 left rigid라고 말한다.
- Theorem 5.13은 finite type에서 longest element $w_0$에 대해 $\widetilde{\mathcal C}_{w_0}$가 rigid라고 말한다.

### Grothendieck-ring-level

Corollary 5.4는 Grothendieck ring에서
$$
K_0(\widetilde{\mathcal C}_w)
$$
가 $K_0(\mathcal C_w)$를 $q$의 powers와 $[C_i]$들이 생성하는 multiplicative subset에 대해 localize한 ring으로 나타난다고 말한다. 따라서 category-level localization은 Grothendieck-ring-level에서는 frozen-variable classes를 invert하는 과정으로 보인다.

## 다른 topic들과의 관계

- [[topics/quiver-hecke-category-localization|Quiver-Hecke Category Localization]]는 이 construction을 $\mathcal C_w$와 determinantial modules에 적용한 specialized construction이다.
- [[topics/quiver-hecke-subcategories|Quiver-Hecke Subcategories]]는 quiver-Hecke instance의 input category $\mathcal C_w$를 제공한다.
- [[topics/determinantial-modules|Determinantial Modules]]는 quiver-Hecke instance에서 invertible하게 만드는 objects $M(w\Lambda_i,\Lambda_i)$를 제공한다.
- [[topics/monoidal-categorification|Monoidal Categorification]]은 localized category의 Grothendieck ring이 cluster-algebra와 coordinate-ring side에서 어떻게 읽히는지를 설명하는 주변 context이다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/quiver-hecke-subcategories|Quiver-Hecke Subcategories]]에서 $\mathcal C_w$를 읽고, [[topics/determinantial-modules|Determinantial Modules]]에서 $M(w\Lambda_i,\Lambda_i)$를 읽는다.
- 다음에 읽을 것: [[topics/quiver-hecke-category-localization|Quiver-Hecke Category Localization]]에서 위 construction이 $\mathcal C_w\to\widetilde{\mathcal C}_w$로 specialized되는 방식을 읽는다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/kkop21-localizations-quiver-hecke-algebras|KKOP21]], Definitions 2.1-2.2 and Theorem 2.7: left braider, real commuting family of braiders, and monoidal localization universal property.
- KKOP21, Theorem 2.12 and Proposition 2.13: graded localization and exactness preservation.
- KKOP21, Proposition 5.1, Section 5.1, Corollary 5.4, Corollary 5.11, and Theorem 5.13: the quiver-Hecke localization $\mathcal C_w\to\widetilde{\mathcal C}_w$, Grothendieck-ring localization, and rigidity facts.
- [[sources/papers/kashiwara-nakashima25-crystal-structure-localized-quantum-unipotent-coordinate-category|Kashiwara-Nakashima 2025]], Sections 5.1-5.2 and Theorem 5.3: the instance $\mathcal C_w\to\widetilde{\mathcal C}_w$.

</details>
