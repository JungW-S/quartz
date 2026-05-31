---
id: localized-crystals
title: Localized Crystals
level: advanced
---

# Localized Crystals

## What it is

Localized crystal은 localized quantum unipotent coordinate category $\widetilde{\mathcal C}_w$의 simple objects에 붙는 crystal structure이다. 더 정확히는 grading shift까지 같은 것으로 보는 simple objects의 집합
$$
\operatorname{Irr}(\widetilde{\mathcal C}_w)
$$
위에 crystal operators $\widetilde E_i,\widetilde F_i$를 정의한 구조를 말한다.

여기서 crystal은 combinatorial graph이지만, vertex는 combinatorial symbol이 아니라 localized monoidal category 안의 simple object이다. Kashiwara-Nakashima의 결과는 이 category-level crystal이 cellular crystal $\mathcal B_w$와 같다는 것을 보여 준다.

## Why it appears

Crystal base theory에서는 basis element 위에 operators $\widetilde e_i,\widetilde f_i$가 작용하여 crystal graph를 만든다. Monoidal categorification 쪽에서는 basis element 대신 module category의 simple objects를 다루므로, 같은 crystal graph를 category 안에서 직접 실현할 방법이 필요하다.

Localization은 $\mathcal C_w$ 안의 determinantial objects를 invertible하게 만들어 더 큰 monoidal category $\widetilde{\mathcal C}_w$를 만든다. 이 localized setting에서는 root objects와 head convolution을 이용해 simple object를 다른 simple object로 보내는 operators를 정의할 수 있다.

## Setup and notation

$\mathfrak g$를 symmetrizable Kac-Moody Lie algebra로 두고, $W$를 Weyl group, $I$를 simple root index set으로 둔다. $R\text{-gmod}$는 quiver-Hecke algebra의 finite-dimensional graded module category이다.

$w\in W$에 대해 $\mathcal C_w$는 $R\text{-gmod}$ 안의 monoidal subcategory이고, $\widetilde{\mathcal C}_w$는 $\mathcal C_w$를 determinantial objects $\mathsf M(w\Lambda_i,\Lambda_i)$에 대해 localization한 category이다. Localization functor는 objects를 $\mathcal C_w$에서 $\widetilde{\mathcal C}_w$로 보낸다.

$\operatorname{Irr}(\widetilde{\mathcal C}_w)$는 $\widetilde{\mathcal C}_w$의 simple objects를 grading shift까지 같은 것으로 본 집합이다. $I_w$는 $w\Lambda_i\ne\Lambda_i$인 simple root indices의 집합이다. 각 $i\in I_w$에 대해 source는 localized simple root object $\widetilde Q_i$를 사용한다.

## Definition

$i\in I_w$와 simple object $X\in\widetilde{\mathcal C}_w$에 대해 Kashiwara-Nakashima는 $\varepsilon_i(X)$, $\varphi_i(X)$, 그리고 root operators
$$
\widetilde F_iX,\qquad \widetilde E_iX
$$
를 정의한다. 이 operators는 $\widetilde Q_i$와 $X$의 convolution, simple head, duality, grading shift를 사용한다.

이 data가 $\operatorname{Irr}(\widetilde{\mathcal C}_w)$ 위의 crystal structure를 이룬다는 것이 이 paper의 Theorem 6.13이다.

## Basic picture

$$
\mathcal C_w
\;\xrightarrow{\;\text{localize}\;}\;
\widetilde{\mathcal C}_w
\;\xrightarrow{\;\operatorname{Irr}\;}\;
\operatorname{Irr}(\widetilde{\mathcal C}_w)
\;\xrightarrow{\;\operatorname{CP}\;}\;
\mathcal B_w
$$

왼쪽 두 단계는 category-level construction이다. 가운데 집합의 vertices는 simple objects이고, $\widetilde E_i,\widetilde F_i$가 crystal-level arrows를 만든다. 마지막 map $\operatorname{CP}$는 이 crystal을 cellular crystal $\mathcal B_w$와 비교한다.

## Example

### Source example

Kashiwara-Nakashima는 $\mathfrak g=A_3$이고
$$
w=s_2w_0=s_1s_2s_3s_2s_1
$$
인 경우를 예로 든다. 이때 $\mathcal C_w=\{M\in R\text{-gmod}\mid E_2M\simeq0\}$로 나타나며, $\mathsf C_{\Lambda_1}$, $\mathsf C_{\Lambda_2}$, $\mathsf C_{\Lambda_3}$에 해당하는 determinantial objects가 frozen variables처럼 작동한다.

이 예시는 $\widetilde{\mathcal C}_w$가 cluster algebra의 monoidal categorification으로 나타나는 상황에서, $\operatorname{CP}$가 cluster data를 cellular crystal의 좌표 영역으로 보내는 방식을 보여 준다.

## Main facts

- $\widetilde{\mathcal C}_w$는 $\mathcal C_w$의 localization으로 얻어지는 rigid monoidal category이다.
- Definition 6.11의 root operators는 $\operatorname{Irr}(\widetilde{\mathcal C}_w)$ 위의 crystal structure를 정의한다.
- $\operatorname{CP}:\operatorname{Irr}(\widetilde{\mathcal C}_w)\to\mathcal B_w$는 crystal morphism이다.
- Main Theorem 9.3은 $\operatorname{CP}$가 crystal isomorphism이라고 말한다.
- 이 isomorphism의 응용으로 cellular crystal $\mathcal B_w$는 connected crystal graph가 된다.

## Why it matters

Localized crystal은 category-level localization과 crystal-level combinatorics를 직접 연결한다. Simple object를 vertex로 보고 convolution과 duality에서 오는 operators를 arrows로 보면, localized category 자체가 crystal graph를 carrying하는 구조가 된다.

이 관점은 cellular crystal $\mathcal B_w$를 단순한 combinatorial model로만 보지 않게 한다. $\mathcal B_w$의 vertex는 localized category의 simple object와 대응하고, 그 대응은 crystal operators와 호환된다.

## Connections

- [[topics/quiver-hecke-algebra-localization|Quiver-Hecke Algebra Localization]]: $\widetilde{\mathcal C}_w$를 만드는 category-level localization을 제공한다.
- [[topics/cellular-crystals|Cellular Crystals]]: localized simple-object crystal이 비교되는 target crystal이다.
- [[topics/determinantial-modules|Determinantial Modules]]: localization에서 invertible하게 되는 central objects의 source이다.
- [[topics/monoidal-categorification|Monoidal Categorification]]: source example은 $\widetilde{\mathcal C}_w$가 cluster algebra를 categorify하는 상황을 보여 준다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/kashiwara-nakashima25-crystal-structure-localized-quantum-unipotent-coordinate-category|Kashiwara-Nakashima 2025]], Abstract and Sections 5.1-5.2: construction of $\widetilde{\mathcal C}_w$ by localization.
- Kashiwara-Nakashima 2025, Definition 6.11 and Theorem 6.13: root operators and the crystal structure on $\operatorname{Irr}(\widetilde{\mathcal C}_w)$.
- Kashiwara-Nakashima 2025, Section 6.4, Main Theorem 7.1, and Main Theorem 9.3: the map $\operatorname{CP}$ and the crystal isomorphism with $\mathcal B_w$.
- Kashiwara-Nakashima 2025, Example 9.6: the $A_3$ example summarized here.

</details>
