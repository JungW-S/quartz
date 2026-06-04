---
id: cellular-crystals
title: Cellular Crystals
level: advanced
topic_kind: object-family
parent_topics:
  - crystal-bases
prerequisite_topics:
  - abstract-crystals
  - tensor-products-of-crystals
  - b-infinity-crystal
  - demazure-crystals
child_topics: []
related_topics:
  - localized-crystals
maturity: study-ready
---

## 개요

Cellular crystal $\mathcal B_w$는 Weyl group element $w$의 reduced expression에서 만들어지는 combinatorial-level [[topics/02-crystal-bases/crystal-bases|crystal]]이다. Reduced expression
$$
w=s_{i_1}\cdots s_{i_m}
$$
을 고르면, $\mathcal B_w$는 elementary crystals $B_{i_1},\ldots,B_{i_m}$를 그 순서대로 tensor product한 crystal로 정의된다.

Localized category comparison theorem에서 $\mathcal B_w$는 category-level simple objects와 비교되는 target crystal이다. 핵심 비교는 localized category의 simple-object crystal $\operatorname{Irr}(\widetilde{\mathcal C}_w)$가 $\mathcal B_w$와 isomorphic하다는 것이다.

이 비교에서 cellular crystal의 역할은 계산 가능한 좌표 model을 제공하는 것이다. Category 안의 simple objects를 직접 움직이는 대신, reduced expression에서 온 tensor-product coordinates로 같은 crystal-level 구조를 읽는다.

## 준비와 notation

$W$를 Weyl group이라 하고, $w\in W$의 reduced expression을
$$
w=s_{i_1}\cdots s_{i_m}
$$
으로 고른다. 각 $i\in I$에 대해 $B_i$는 elementary crystal이다. 여기서는
$$
B_i=\{b_i(n)\mid n\in\mathbb Z\}
$$
로 쓰며, $i$-direction의 root operators는
$$
\widetilde e_i b_i(n)=b_i(n+1),
\qquad
\widetilde f_i b_i(n)=b_i(n-1)
$$
처럼 작용한다. Weight, $\widetilde e_i$, $\widetilde f_i$ 같은 abstract crystal 용어는 [[topics/02-crystal-bases/abstract-crystals|Abstract Crystals]]에서 정리하고, tensor product rule은 [[topics/02-crystal-bases/tensor-products-of-crystals|Tensor Products of Crystals]]에서 정리한다.

Tensor product
$$
B_{i_1}\otimes\cdots\otimes B_{i_m}
$$
의 원소는 좌표
$$
x=(x_1,\ldots,x_m)
$$
로 쓸 수 있다. 이 좌표 표기에서 $x_k$는 $B_{i_k}$의 원점 $b_{i_k}(0)$에서 $i_k$-direction으로 얼마나 이동했는지를 기록한다. $x_k\ge 0$이면 $\widetilde f_{i_k}^{x_k}b_{i_k}(0)$로 읽고, $x_k<0$이면 $\widetilde e_{i_k}^{-x_k}b_{i_k}(0)$로 읽는다.

## 정의

Reduced expression $w=s_{i_1}\cdots s_{i_m}$에 붙은 cellular crystal은 tensor-product crystal
$$
\mathcal B_w:=B_{i_1}\otimes\cdots\otimes B_{i_m}
$$
이다. 여기서 오른쪽은 elementary crystals의 tensor product이며, $\operatorname{wt}$, $\varepsilon_i$, $\varphi_i$, $\widetilde e_i$, $\widetilde f_i$는 crystal tensor product rule에 의해 정해진다.

Reduced expression을 다르게 고르면 braid-type isomorphisms를 통해 isomorphic crystals를 얻는다.

좌표로 쓰면 원소는
$$
x=(x_1,\ldots,x_m)
=
\widetilde f_{i_1}^{x_1}b_{i_1}(0)
\otimes\cdots\otimes
\widetilde f_{i_m}^{x_m}b_{i_m}(0)
$$
이다. $x_k<0$인 경우에는 $\widetilde f_{i_k}^{x_k}b_{i_k}(0)$를 $\widetilde e_{i_k}^{-x_k}b_{i_k}(0)$로 해석한다. 따라서 $\mathcal B_w$의 underlying set과 crystal structure는 reduced expression과 elementary crystal tensor product에서 결정된다.

## 기본 예시

### 실제 예시

$w=s_i$가 simple reflection이면 reduced expression의 길이는 $1$이다. 이 경우 cellular crystal은 하나의 elementary crystal
$$
\mathcal B_{s_i}=B_i
$$
로 읽을 수 있다.

검증: 논문 예시

## 핵심 관점

$$
w=s_{i_1}\cdots s_{i_m}
\quad\leadsto\quad
B_{i_1}\otimes\cdots\otimes B_{i_m}
\quad\leadsto\quad
\mathcal B_w
$$

Reduced word는 tensor factors의 순서를 정한다. Tensor product rule은 $\widetilde e_i,\widetilde f_i$가 어느 좌표를 바꾸는지를 결정하고, cellular-crystal coordinate formulas는 그 좌표 변화를 명시한다.

이 model을 쓰면 localized simple object에 대한 root operators의 작용을 좌표 변화로 읽을 수 있다. [[topics/08-localization-of-categories/localized-crystals|Localized Crystals]]에서 정의되는 비교 map $\operatorname{CP}$는 localized simple object를 이런 좌표형 crystal로 보낸다.

## 기본 성질

### Tensor-product construction

$\mathcal B_w$는 reduced expression에서 만들어지는 tensor-product crystal이다. Reduced word는 elementary crystal factors의 순서를 정하고, crystal tensor product rule은 전체 crystal structure를 정한다.

### Reduced-word independence

Reduced expression을 다르게 골라도 braid-type isomorphisms를 통해 isomorphic crystals를 얻는다. 따라서 notation $\mathcal B_w$는 reduced word를 고르는 construction에서 시작하지만, 같은 $w$에 붙은 crystal로 읽을 수 있다.

### Coordinate formulas

좌표 $x=(x_1,\ldots,x_m)$에서 $\varepsilon_i$, $\varphi_i$, $\widetilde e_i$, $\widetilde f_i$, weight를 계산하는 formulas가 있다. 이 formulas는 $\mathcal B_w$를 추상 crystal graph가 아니라 계산 가능한 coordinate model로 쓰게 해 준다.

### Comparison with localized simples

$\operatorname{CP}:\operatorname{Irr}(\widetilde{\mathcal C}_w)\to\mathcal B_w$는 crystal morphism이고 bijective이다. 따라서 $\operatorname{Irr}(\widetilde{\mathcal C}_w)$와 $\mathcal B_w$는 isomorphic crystals이다. 이 비교에서 $\mathcal B_w$는 codomain이다. Coordinate model과 target crystal은 여기서 읽고, $\operatorname{CP}$의 category-level domain과 recursive construction은 [[topics/08-localization-of-categories/localized-crystals|Localized Crystals]]에서 읽는다.

### Connectedness

$\mathcal B_w$는 connected crystal graph이다. 이 성질은 localized simple-object crystal과 cellular crystal을 비교할 때, 하나의 coordinate model 안에서 전체 crystal을 따라갈 수 있게 해 준다.

### 해석

Cellular crystal은 localized category의 simple-object crystal을 계산 가능한 combinatorial object로 바꿔 준다. Category 안의 simple object를 직접 추적하는 대신, reduced expression에서 온 좌표와 crystal operators를 사용할 수 있다.

## 다른 topic들과의 관계

[[topics/02-crystal-bases/abstract-crystals|Abstract Crystals]]는 root operators와 crystal graph language를 제공한다. Cellular crystal은 abstract crystal axioms를 만족하는 구체적인 tensor-product model이다.

[[topics/02-crystal-bases/tensor-products-of-crystals|Tensor Products of Crystals]]는 cellular crystal의 좌표 model에 필요한 tensor product rule을 제공한다. $\mathcal B_w$의 definition 자체가 elementary crystals의 ordered tensor product이므로, 이 prerequisite가 직접 필요하다.

[[topics/02-crystal-bases/b-infinity-crystal|The Crystal B(infinity)]]와 [[topics/02-crystal-bases/demazure-crystals|Demazure Crystals]]는 ordinary crystal-side에서 Weyl group element $w$가 crystal theory에 들어오는 배경을 제공한다. Cellular crystal은 이 $w$-indexed crystal language를 coordinate model 쪽으로 가져온다.

[[topics/08-localization-of-categories/localized-crystals|Localized Crystals]]는 $\mathcal B_w$를 localized simple-object crystal의 target model로 사용한다. $\operatorname{CP}$의 domain과 recursive construction은 localized category side에 속한다.

[[topics/08-localization-of-categories/quiver-hecke-category-localization|Quiver-Hecke Category Localization]]은 $\widetilde{\mathcal C}_w$라는 category-level 출발점을 제공한다. Cellular crystal은 그 category-level object와 비교되는 combinatorial-level target이다.

[[topics/05-monoidal-categorification/monoidal-categorification|Monoidal Categorification]]은 category-level data를 combinatorial 또는 Grothendieck-ring-level data와 비교하는 배경을 제공한다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/01-quantum-groups/root-systems-and-weight-lattices|Root Systems and Weight Lattices]]에서 Weyl group notation을 읽고, [[topics/02-crystal-bases/abstract-crystals|Abstract Crystals]]에서 root operator를 읽고, [[topics/02-crystal-bases/tensor-products-of-crystals|Tensor Products of Crystals]]에서 tensor product를 읽는다. 그 다음 [[topics/02-crystal-bases/b-infinity-crystal|The Crystal B(infinity)]]와 [[topics/02-crystal-bases/demazure-crystals|Demazure Crystals]]에서 $w$-indexed ordinary crystal background를 읽는다.
- 상위 개념: [[topics/02-crystal-bases/crystal-bases|Crystal Bases]]가 더 넓은 crystal-theoretic 배경이다.
- 다음에 읽을 것: [[topics/08-localization-of-categories/localized-crystals|Localized Crystals]]에서는 $\mathcal B_w$와 비교되는 category-level crystal을 읽고, [[topics/08-localization-of-categories/quiver-hecke-category-localization|Quiver-Hecke Category Localization]]에서는 그 뒤의 localized category를 읽는다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/kashiwara-nakashima25-crystal-structure-localized-quantum-unipotent-coordinate-category|Kashiwara-Nakashima 2025]], Section 2.4 and lines 1413-1530 of `inbox/papers/crystal.tex`: elementary crystal $B_i$, construction and coordinate formulas for $\mathcal B_w$, and the length-one specialization $\mathcal B_{s_i}=B_i$.
- Kashiwara-Nakashima 2025, Section 6.4 and Main Theorem 7.1: construction of $\operatorname{CP}$ and crystal morphism compatibility with $\mathcal B_w$ as target.
- Kashiwara-Nakashima 2025, Proposition 9.2 and Main Theorem 9.3: $\operatorname{Irr}(\widetilde{\mathcal C}_w)\simeq\mathcal B_w$ as crystals.
- Kashiwara-Nakashima 2025, Section 9.2: connectedness of $\mathcal B_w$.
- [[sources/papers/kashiwara93-crystal-base-demazure-character-formula|Kashiwara 1993]], Sections 1.2-1.3: general crystal, elementary crystal, and tensor-product background.

</details>
