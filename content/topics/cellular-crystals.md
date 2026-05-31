---
id: cellular-crystals
title: Cellular Crystals
level: advanced
---

# Cellular Crystals

## What it is

Cellular crystal $\mathcal B_w$는 Weyl group element $w$의 reduced expression에서 만들어지는 crystal이다. Reduced expression
$$
w=s_{i_1}\cdots s_{i_m}
$$
을 고르면, $\mathcal B_w$는 elementary crystals $B_{i_1},\ldots,B_{i_m}$의 tensor product 안에 놓이는 crystal로 정의된다.

Kashiwara-Nakashima의 localized category 결과에서 $\mathcal B_w$는 target combinatorial crystal이다. 즉 localized category의 simple-object crystal $\operatorname{Irr}(\widetilde{\mathcal C}_w)$가 $\mathcal B_w$와 isomorphic하다.

## Why it appears

Localized category의 simple objects는 category-level objects라서 직접 계산하기 어렵다. Cellular crystal은 같은 crystal을 tensor-product coordinates로 표현해 주는 combinatorial model이다.

이 model을 쓰면 root operators의 작용을 좌표 변화로 읽을 수 있다. Kashiwara-Nakashima의 map $\operatorname{CP}$는 localized simple object를 이런 좌표형 crystal로 보내는 비교 map이다.

## Setup and notation

$W$를 Weyl group이라 하고, $w\in W$의 reduced expression을
$$
w=s_{i_1}\cdots s_{i_m}
$$
으로 고른다. 각 $i\in I$에 대해 $B_i$는 elementary crystal이다.

Tensor product
$$
B_{i_1}\otimes\cdots\otimes B_{i_m}
$$
의 원소는 좌표
$$
x=(x_1,\ldots,x_m)
$$
로 쓸 수 있다. Source에서는 $x_k$를 $\widetilde f_{i_k}^{x_k}(0)_{i_k}$에 대응시키며, $x_k<0$일 때는 $\widetilde e_{i_k}^{-x_k}(0)_{i_k}$로 해석한다.

## Definition

Reduced expression $w=s_{i_1}\cdots s_{i_m}$에 대해 Kashiwara-Nakashima는
$$
\mathcal B_w\subset B_{i_1}\otimes\cdots\otimes B_{i_m}
$$
를 그 reduced expression에 associated cellular crystal이라고 부른다.

Source는 다른 reduced expressions를 고르더라도 braid-type isomorphisms를 통해 isomorphic crystals가 된다고 기록한다.

## Basic picture

$$
w=s_{i_1}\cdots s_{i_m}
\quad\leadsto\quad
B_{i_1}\otimes\cdots\otimes B_{i_m}
\quad\leadsto\quad
\mathcal B_w
$$

Reduced word는 tensor factors의 순서를 정한다. Tensor product rule은 $\widetilde e_i,\widetilde f_i$가 어느 좌표를 바꾸는지를 결정하고, source의 formulas는 그 좌표 변화를 명시한다.

## Example

### Schematic example

$w=s_i$가 simple reflection이면 reduced expression의 길이는 $1$이다. 이 경우 cellular crystal은 하나의 elementary crystal
$$
\mathcal B_{s_i}\subset B_i
$$
로 읽을 수 있다.

길이가 더 긴 $w=s_{i_1}\cdots s_{i_m}$에서는 한 vertex가 $m$개의 좌표를 갖는다. Crystal operator는 tensor product rule에 따라 선택된 좌표 하나를 증가시키거나 감소시키는 방식으로 작동한다.

## Main facts

- $\mathcal B_w$는 reduced expression에서 만들어지는 tensor-product crystal이다.
- Reduced expression을 다르게 골라도 source는 braid-type isomorphisms를 통해 같은 crystal type을 얻는다고 설명한다.
- Source는 좌표 $x=(x_1,\ldots,x_m)$에서 $\varepsilon_i$, $\varphi_i$, $\widetilde e_i$, $\widetilde f_i$, weight를 계산하는 formulas를 준다.
- Kashiwara-Nakashima의 Main Theorem 9.3은 $\operatorname{Irr}(\widetilde{\mathcal C}_w)$와 $\mathcal B_w$가 isomorphic crystals라고 말한다.
- Section 9.2의 theorem은 $\mathcal B_w$가 connected crystal graph라고 말한다.

## Why it matters

Cellular crystal은 localized category의 simple-object crystal을 계산 가능한 combinatorial object로 바꿔 준다. Category 안의 simple object를 직접 추적하는 대신, reduced expression에서 온 좌표와 crystal operators를 사용할 수 있다.

이 주제는 crystal-level structure와 category-level categorification 사이의 bridge이다. $\operatorname{CP}$가 crystal isomorphism이라는 사실은 두 표현 방식이 같은 crystal graph를 보고 있다는 뜻이다.

## Connections

- [[topics/localized-crystals|Localized Crystals]]: $\mathcal B_w$는 localized simple-object crystal의 target model이다.
- [[topics/quiver-hecke-algebra-localization|Quiver-Hecke Algebra Localization]]: source category $\widetilde{\mathcal C}_w$를 제공한다.
- [[topics/monoidal-categorification|Monoidal Categorification]]: source example에서는 cluster-algebra data가 cellular crystal 좌표로 표현된다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/kashiwara-nakashima25-crystal-structure-localized-quantum-unipotent-coordinate-category|Kashiwara-Nakashima 2025]], Section 2.4: construction and coordinate formulas for $\mathcal B_w$.
- Kashiwara-Nakashima 2025, Main Theorem 9.3: $\operatorname{Irr}(\widetilde{\mathcal C}_w)\simeq\mathcal B_w$ as crystals.
- Kashiwara-Nakashima 2025, Section 9.2: connectedness of $\mathcal B_w$.

</details>
