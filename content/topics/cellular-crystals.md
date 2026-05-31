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

# Cellular Crystals

## 개요

Cellular crystal $\mathcal B_w$는 Weyl group element $w$의 reduced expression에서 만들어지는 [[topics/crystal-bases|crystal]]이다. Reduced expression
$$
w=s_{i_1}\cdots s_{i_m}
$$
을 고르면, $\mathcal B_w$는 elementary crystals $B_{i_1},\ldots,B_{i_m}$의 tensor product로 정의된다.

Kashiwara-Nakashima의 localized category 결과에서 $\mathcal B_w$는 target combinatorial crystal이다. 즉 localized category의 simple-object crystal $\operatorname{Irr}(\widetilde{\mathcal C}_w)$가 $\mathcal B_w$와 isomorphic하다.

Localized category의 simple objects는 category-level objects라서 직접 계산하기 어렵다. Cellular crystal은 같은 crystal을 tensor-product coordinates로 표현해 주는 combinatorial model이다.

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
처럼 작용한다. General crystal terminology such as weight, $\widetilde e_i$, $\widetilde f_i$, and tensor product is reviewed in [[topics/crystal-bases|Crystal Bases and Crystal Graphs]].

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
이다. 여기서 오른쪽은 elementary crystals의 tensor product이며, $\operatorname{wt}$, $\varepsilon_i$, $\varphi_i$, $\widetilde e_i$, $\widetilde f_i$는 crystal tensor product rule로 결정된다.

Reduced expression을 다르게 고르면 braid-type isomorphisms를 통해 isomorphic crystals를 얻는다.

좌표로 쓰면 원소는
$$
x=(x_1,\ldots,x_m)
=
\widetilde f_{i_1}^{x_1}(0)_{i_1}
\otimes\cdots\otimes
\widetilde f_{i_m}^{x_m}(0)_{i_m}
$$
이다. $x_k<0$인 경우에는 $\widetilde f_{i_k}^{x_k}(0)_{i_k}$를 $\widetilde e_{i_k}^{-x_k}(0)_{i_k}$로 해석한다. 따라서 $\mathcal B_w$의 underlying set, weight, length functions, root operators는 모두 reduced expression과 elementary crystal tensor product에서 정해진다.

## 기본 예시

### 실제 예시

$w=s_i$가 simple reflection이면 reduced expression의 길이는 $1$이다. 이 경우 cellular crystal은 하나의 elementary crystal
$$
\mathcal B_{s_i}=B_i
$$
로 읽을 수 있다.

## 핵심 관점

$$
w=s_{i_1}\cdots s_{i_m}
\quad\leadsto\quad
B_{i_1}\otimes\cdots\otimes B_{i_m}
\quad\leadsto\quad
\mathcal B_w
$$

Reduced word는 tensor factors의 순서를 정한다. Tensor product rule은 $\widetilde e_i,\widetilde f_i$가 어느 좌표를 바꾸는지를 결정하고, cellular-crystal formulas는 그 좌표 변화를 명시한다.

이 model을 쓰면 localized simple object에 대한 root operators의 작용을 좌표 변화로 읽을 수 있다. Kashiwara-Nakashima의 map $\operatorname{CP}$는 localized simple object를 이런 좌표형 crystal로 보내는 비교 map이다.

## 기본 성질

- $\mathcal B_w$는 reduced expression에서 만들어지는 tensor-product crystal이다.
- Reduced expression을 다르게 골라도 braid-type isomorphisms를 통해 같은 crystal type을 얻는다.
- 좌표 $x=(x_1,\ldots,x_m)$에서 $\varepsilon_i$, $\varphi_i$, $\widetilde e_i$, $\widetilde f_i$, weight를 계산하는 formulas가 있다.
- Kashiwara-Nakashima의 Main Theorem 9.3은 $\operatorname{Irr}(\widetilde{\mathcal C}_w)$와 $\mathcal B_w$가 isomorphic crystals라고 말한다.
- Section 9.2의 theorem은 $\mathcal B_w$가 connected crystal graph라고 말한다.

Cellular crystal은 localized category의 simple-object crystal을 계산 가능한 combinatorial object로 바꿔 준다. Category 안의 simple object를 직접 추적하는 대신, reduced expression에서 온 좌표와 crystal operators를 사용할 수 있다.

## 다른 topic들과의 관계

- [[topics/crystal-bases|Crystal Bases and Crystal Graphs]]는 tensor product crystals와 root operators의 일반 언어를 제공한다.
- [[topics/localized-crystals|Localized Crystals]]는 $\mathcal B_w$를 localized simple-object crystal의 target model로 사용한다.
- [[topics/quiver-hecke-algebra-localization|Quiver-Hecke Algebra Localization]]은 $\widetilde{\mathcal C}_w$라는 category-level 출발점을 제공한다.
- [[topics/monoidal-categorification|Monoidal Categorification]]은 cluster-algebra data가 cellular crystal 좌표로 표현되는 배경을 제공한다.

## 더 읽을 topic

- Prerequisite topics: [[topics/root-systems-and-weight-lattices|Root Systems and Weight Lattices]] for Weyl group notation; [[topics/crystal-bases|Crystal Bases and Crystal Graphs]] for tensor products and root operators.
- Parent topics: [[topics/crystal-bases|Crystal Bases and Crystal Graphs]] is the broader crystal-theoretic setting.
- Next topics: [[topics/localized-crystals|Localized Crystals]] for the category-level crystal identified with $\mathcal B_w$; [[topics/quiver-hecke-algebra-localization|Quiver-Hecke Algebra Localization]] for the localized category behind it.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/kashiwara-nakashima25-crystal-structure-localized-quantum-unipotent-coordinate-category|Kashiwara-Nakashima 2025]], Section 2.4: construction and coordinate formulas for $\mathcal B_w$.
- Kashiwara-Nakashima 2025, Main Theorem 9.3: $\operatorname{Irr}(\widetilde{\mathcal C}_w)\simeq\mathcal B_w$ as crystals.
- Kashiwara-Nakashima 2025, Section 9.2: connectedness of $\mathcal B_w$.
- [[sources/papers/kashiwara93-crystal-base-demazure-character-formula|Kashiwara 1993]], Sections 1.2-1.3: general crystal, elementary crystal, and tensor-product background.

</details>
