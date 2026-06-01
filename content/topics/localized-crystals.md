---
id: localized-crystals
title: Localized Crystals
level: advanced
topic_kind: construction
parent_topics:
  - crystal-bases
  - quiver-hecke-category-localization
prerequisite_topics:
  - crystal-bases
  - cellular-crystals
  - quiver-hecke-category-localization
child_topics:
  - localized-root-operators
  - crystal-comparison-map
related_topics:
  - monoidal-categorification
maturity: study-ready
---

## 개요

Localized crystal은 localized quantum unipotent coordinate category $\widetilde{\mathcal C}_w$의 simple objects를 vertices로 삼는 [[topics/crystal-bases|crystal structure]]이다. 더 정확히는 grading shift까지 같은 것으로 보는 simple objects의 집합
$$
\operatorname{Irr}(\widetilde{\mathcal C}_w)
$$
위에 crystal operators $\widetilde E_i,\widetilde F_i$를 정의한 구조를 말한다.

일반적인 crystal graph처럼 arrows는 crystal-level data이지만, vertices는 combinatorial symbols가 아니라 localized monoidal category 안의 simple objects이다. Kashiwara-Nakashima의 결과는 이 category-level crystal이 cellular crystal $\mathcal B_w$와 같다는 것을 보여 준다.

Crystal base theory에서는 basis element 위에 operators $\widetilde e_i,\widetilde f_i$가 작용하여 crystal graph를 만든다. Monoidal categorification 쪽에서는 basis element 대신 module category의 simple objects를 다루므로, 같은 crystal graph를 category 안에서 직접 실현할 방법이 필요하다.

## 준비와 notation

$\mathfrak g$를 symmetrizable Kac-Moody Lie algebra로 두고, $W$를 Weyl group, $I$를 simple root index set으로 둔다. $R\text{-gmod}$는 quiver-Hecke algebra의 finite-dimensional graded module category이다.

$w\in W$에 대해 $\mathcal C_w$는 $R\text{-gmod}$ 안의 monoidal subcategory이고, $\widetilde{\mathcal C}_w$는 $\mathcal C_w$를 determinantial objects $\mathsf M(w\Lambda_i,\Lambda_i)$에 대해 localization한 category이다. Localization functor는 objects를 $\mathcal C_w$에서 $\widetilde{\mathcal C}_w$로 보낸다.

$\operatorname{Irr}(\widetilde{\mathcal C}_w)$는 $\widetilde{\mathcal C}_w$의 simple objects를 grading shift까지 같은 것으로 본 집합이다. Weight, $\widetilde e_i$, $\widetilde f_i$, $\varepsilon_i$, $\varphi_i$, tensor product 같은 일반 crystal notation은 [[topics/crystal-bases|Crystal Bases]]에서 정리한다.

$I_w$는 $w\Lambda_i\ne\Lambda_i$인 simple root indices의 집합이다. 각 $i\in I_w$에 대해 localized construction은 localized simple root object
$$
\widetilde Q_i=\Phi_w(\langle i\rangle)
$$
를 사용한다. 여기서 $\Phi_w$는 localization functor이고, $\langle i\rangle$는 quiver-Hecke module category 쪽의 simple root object이다.

Operator formula를 읽을 때 필요한 notation은 [[topics/localized-root-operators|Localized Root Operators]]에서 모아 둔다. 거기서는 $\mathsf d_i=(\alpha_i,\alpha_i)/2$, modified R-matrix degree $\widetilde\Lambda$, 양방향 degree invariant $\mathfrak d$, convolution product의 simple head $\nabla$, 그리고 duality functor $\mathscr D$를 도입한 뒤 $\widetilde E_i,\widetilde F_i$를 정의한다.

## 구성

Kashiwara-Nakashima의 localized crystal construction은 다음 data로 이루어진다.

1. Vertex set은 grading shift까지 같은 것으로 보는 simple objects의 집합 $\operatorname{Irr}(\widetilde{\mathcal C}_w)$이다.
2. 각 $i\in I_w$에 대해 localized simple-root object $\widetilde Q_i$와 R-matrix degree data를 사용하여 maps $\widetilde E_i,\widetilde F_i$와 starred maps를 만든다.
3. 같은 data에서 $\varepsilon_i,\varphi_i$와 starred analogues를 정의하여 ordinary crystal의 numerical functions와 맞춘다.
4. $i\notin I_w$인 direction은 이 localized crystal에서 active arrow를 만들지 않는다.

정확한 operator formulas는 [[topics/localized-root-operators|Localized Root Operators]]의 내용이다. 여기서는 그 formulas를 반복하지 않고, 그 maps가 $\operatorname{Irr}(\widetilde{\mathcal C}_w)$ 위의 crystal structure를 만든다는 구성 수준의 진술에 집중한다.

Kashiwara-Nakashima Theorem 6.13은 위 data가 $\operatorname{Irr}(\widetilde{\mathcal C}_w)$ 위의 crystal structure를 이룬다고 말한다.

## 기본 예시

### 실제 예시

Kashiwara-Nakashima는 $\mathfrak g=A_3$이고
$$
w=s_2w_0=s_1s_2s_3s_2s_1
$$
인 경우를 예로 든다. 이 예시에서는 localized category $\widetilde{\mathcal C}_w$의 simple objects가 crystal vertices가 되고, localized root operators가 arrows를 만든다.

같은 예시는 comparison map $\operatorname{CP}$가 localized simple-object crystal을 cellular crystal 좌표와 비교하는 데도 쓰인다. $\operatorname{CP}$의 구체적인 coordinate formula와 type $A_3$ 계산은 [[topics/crystal-comparison-map|Crystal Comparison Map]]에서 다룬다.

검증: 논문 예시

## 핵심 관점

$$
\mathcal C_w
\;\xrightarrow{\;\text{localize}\;}\;
\widetilde{\mathcal C}_w
\;\xrightarrow{\;\operatorname{Irr}\;}\;
\operatorname{Irr}(\widetilde{\mathcal C}_w)
\;\xrightarrow{\;\operatorname{CP}\;}\;
\mathcal B_w
$$

왼쪽 두 단계는 category-level construction이다. 가운데 집합의 vertices는 simple objects이고, [[topics/localized-root-operators|Localized Root Operators]]가 crystal-level arrows를 만든다. 마지막 map $\operatorname{CP}$는 이 crystal을 cellular crystal $\mathcal B_w$와 비교한다.

## 기본 성질

### 구성 수준의 사실

- $\widetilde{\mathcal C}_w$는 $\mathcal C_w$의 localization으로 얻어지는 rigid monoidal category이다.
- [[topics/localized-root-operators|Localized Root Operators]]에서 정의한 maps는 $\operatorname{Irr}(\widetilde{\mathcal C}_w)$ 위의 crystal structure를 정의한다.

### 비교 정리

- $\operatorname{CP}:\operatorname{Irr}(\widetilde{\mathcal C}_w)\to\mathcal B_w$는 crystal morphism이다.
- Main Theorem 9.3은 $\operatorname{CP}$가 crystal isomorphism이라고 말한다.

### 결과

- 이 isomorphism의 응용으로 cellular crystal $\mathcal B_w$는 connected crystal graph가 된다.

## 다른 topic들과의 관계

- [[topics/quiver-hecke-category-localization|Quiver-Hecke Category Localization]]은 $\widetilde{\mathcal C}_w$를 만드는 category-level localization을 제공한다.
- [[topics/crystal-bases|Crystal Bases]]는 crystal operators와 crystal morphisms의 일반 crystal-level language를 제공한다.
- [[topics/cellular-crystals|Cellular Crystals]]는 localized simple-object crystal이 비교되는 target crystal이다.
- [[topics/localized-root-operators|Localized Root Operators]]는 $\widetilde E_i,\widetilde F_i$와 starred operators의 formula-level definition을 담는다.
- [[topics/crystal-comparison-map|Crystal Comparison Map]]은 $\operatorname{CP}$가 localized crystal을 cellular crystal과 비교하는 방식을 설명한다.
- [[topics/determinantial-modules|Determinantial Modules]]는 localization에서 invertible하게 되는 central objects를 제공한다.
- [[topics/monoidal-categorification|Monoidal Categorification]]은 $\widetilde{\mathcal C}_w$가 cluster algebra를 categorify하는 상황을 설명한다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/crystal-bases|Crystal Bases]]에서 abstract crystal language를 읽고, [[topics/cellular-crystals|Cellular Crystals]]에서 combinatorial target을 읽고, [[topics/quiver-hecke-category-localization|Quiver-Hecke Category Localization]]에서 $\widetilde{\mathcal C}_w$를 읽는다.
- 상위 개념: [[topics/crystal-bases|Crystal Bases]]와 [[topics/quiver-hecke-category-localization|Quiver-Hecke Category Localization]]이 더 넓은 setting이다.
- 다음에 읽을 것: [[topics/localized-root-operators|Localized Root Operators]]에서는 formula-level arrows를 읽고, [[topics/crystal-comparison-map|Crystal Comparison Map]]에서는 $\mathcal B_w$와의 비교를 읽고, [[topics/monoidal-categorification|Monoidal Categorification]]에서는 cluster-algebra context를 읽고, [[topics/determinantial-modules|Determinantial Modules]]에서는 crystal construction 전에 invertible하게 만드는 objects를 읽는다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/kashiwara-nakashima25-crystal-structure-localized-quantum-unipotent-coordinate-category|Kashiwara-Nakashima 2025]], Abstract and Sections 5.1-5.2: construction of $\widetilde{\mathcal C}_w$ by localization.
- Kashiwara-Nakashima 2025, Definition 6.11 and Theorem 6.13: root operators and the crystal structure on $\operatorname{Irr}(\widetilde{\mathcal C}_w)$.
- Kashiwara-Nakashima 2025, Section 6.4, Main Theorem 7.1, and Main Theorem 9.3: the map $\operatorname{CP}$ and the crystal isomorphism with $\mathcal B_w$.
- Kashiwara-Nakashima 2025, Example 9.6: the $A_3$ example briefly referenced here; the detailed $\operatorname{CP}$ coordinate formula belongs on [[topics/crystal-comparison-map|Crystal Comparison Map]].
- [[sources/papers/kashiwara93-crystal-base-demazure-character-formula|Kashiwara 1993]], Sections 1.2-1.3: general crystal, morphism, and tensor-product background.

</details>
