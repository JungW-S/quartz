---
id: cellular-crystals
title: Cellular Crystals
level: advanced
topic_kind: object-family
parent_topics:
  - crystal-bases
prerequisite_topics:
  - root-systems-and-weight-lattices
  - crystal-bases
child_topics: []
related_topics:
  - localized-crystals
maturity: study-ready
---

## 개요

Cellular crystal $\mathcal B_w$는 Weyl group element $w$의 reduced expression에서 만들어지는 combinatorial-level [[topics/crystal-bases|crystal]]이다. Reduced expression
$$
w=s_{i_1}\cdots s_{i_m}
$$
을 고르면, $\mathcal B_w$는 elementary crystals $B_{i_1},\ldots,B_{i_m}$를 그 순서대로 tensor product한 crystal로 정의된다.

Kashiwara-Nakashima의 localized category 결과에서 $\mathcal B_w$는 category-level simple objects와 비교되는 target crystal이다. 핵심 비교는 localized category의 simple-object crystal $\operatorname{Irr}(\widetilde{\mathcal C}_w)$가 $\mathcal B_w$와 isomorphic하다는 것이다.

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
처럼 작용한다. Weight, $\widetilde e_i$, $\widetilde f_i$, tensor product 같은 일반 crystal 용어는 [[topics/crystal-bases|Crystal Bases]]에서 정리한다.

Tensor product
$$
B_{i_1}\otimes\cdots\otimes B_{i_m}
$$
의 원소는 좌표
$$
x=(x_1,\ldots,x_m)
$$
로 쓸 수 있다. 이 좌표 표기에서 $x_k$는 $\widetilde f_{i_k}^{x_k}(0)_{i_k}$에 대응하며, $x_k<0$일 때는 $\widetilde e_{i_k}^{-x_k}(0)_{i_k}$로 해석한다.

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
\widetilde f_{i_1}^{x_1}(0)_{i_1}
\otimes\cdots\otimes
\widetilde f_{i_m}^{x_m}(0)_{i_m}
$$
이다. $x_k<0$인 경우에는 $\widetilde f_{i_k}^{x_k}(0)_{i_k}$를 $\widetilde e_{i_k}^{-x_k}(0)_{i_k}$로 해석한다. 따라서 $\mathcal B_w$의 underlying set과 crystal structure는 reduced expression과 elementary crystal tensor product에서 결정된다.

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

Reduced word는 tensor factors의 순서를 정한다. Tensor product rule은 $\widetilde e_i,\widetilde f_i$가 어느 좌표를 바꾸는지를 결정하고, cellular-crystal formulas는 그 좌표 변화를 명시한다.

이 model을 쓰면 localized simple object에 대한 root operators의 작용을 좌표 변화로 읽을 수 있다. 비교 map $\operatorname{CP}$는 localized simple object를 이런 좌표형 crystal로 보내는 map이다.

## 기본 성질

### 정의에서 바로 나오는 성질

- $\mathcal B_w$는 reduced expression에서 만들어지는 tensor-product crystal이다.
- Reduced expression을 다르게 골라도 braid-type isomorphisms를 통해 isomorphic crystals를 얻는다.
- 좌표 $x=(x_1,\ldots,x_m)$에서 $\varepsilon_i$, $\varphi_i$, $\widetilde e_i$, $\widetilde f_i$, weight를 계산하는 formulas가 있다.

### 정리 수준의 사실

- $\operatorname{Irr}(\widetilde{\mathcal C}_w)$와 $\mathcal B_w$는 isomorphic crystals이다.
- $\mathcal B_w$는 connected crystal graph이다.

### 해석

Cellular crystal은 localized category의 simple-object crystal을 계산 가능한 combinatorial object로 바꿔 준다. Category 안의 simple object를 직접 추적하는 대신, reduced expression에서 온 좌표와 crystal operators를 사용할 수 있다.

## 다른 topic들과의 관계

- [[topics/crystal-bases|Crystal Bases]]는 tensor product crystals와 root operators의 일반 언어를 제공한다.
- [[topics/localized-crystals|Localized Crystals]]는 $\mathcal B_w$를 localized simple-object crystal의 target model로 사용한다.
- [[topics/quiver-hecke-category-localization|Quiver-Hecke Category Localization]]은 $\widetilde{\mathcal C}_w$라는 category-level 출발점을 제공한다.
- [[topics/monoidal-categorification|Monoidal Categorification]]은 category-level data를 combinatorial 또는 Grothendieck-ring-level data와 비교하는 배경을 제공한다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/root-systems-and-weight-lattices|Root Systems and Weight Lattices]]에서 Weyl group notation을 읽고, [[topics/crystal-bases|Crystal Bases]]에서 tensor product와 root operator를 읽는다.
- 상위 개념: [[topics/crystal-bases|Crystal Bases]]가 더 넓은 crystal-theoretic setting이다.
- 다음에 읽을 것: [[topics/localized-crystals|Localized Crystals]]에서는 $\mathcal B_w$와 비교되는 category-level crystal을 읽고, [[topics/quiver-hecke-category-localization|Quiver-Hecke Category Localization]]에서는 그 뒤의 localized category를 읽는다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/kashiwara-nakashima25-crystal-structure-localized-quantum-unipotent-coordinate-category|Kashiwara-Nakashima 2025]], Section 2.4 and lines 1413-1530 of `inbox/papers/crystal.tex`: elementary crystal $B_i$, construction and coordinate formulas for $\mathcal B_w$, and the length-one specialization $\mathcal B_{s_i}=B_i$.
- Kashiwara-Nakashima 2025, Main Theorem 9.3: $\operatorname{Irr}(\widetilde{\mathcal C}_w)\simeq\mathcal B_w$ as crystals.
- Kashiwara-Nakashima 2025, Section 9.2: connectedness of $\mathcal B_w$.
- [[sources/papers/kashiwara93-crystal-base-demazure-character-formula|Kashiwara 1993]], Sections 1.2-1.3: general crystal, elementary crystal, and tensor-product background.

</details>
