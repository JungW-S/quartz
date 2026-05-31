---
id: quiver-hecke-algebra-localization
title: Quiver-Hecke Algebra Localization
level: advanced
topic_kind: construction
parent_topics:
  - quiver-hecke-algebras
prerequisite_topics:
  - quiver-hecke-algebras
  - determinantial-modules
  - monoidal-categorification
child_topics:
  - localized-crystals
related_topics:
  - quantum-coordinate-rings
maturity: study-ready
---

# Quiver-Hecke Algebra Localization

## What it is

Quiver-Hecke algebra localization은 quiver-Hecke, or KLR, algebra의 graded module category에서 특정 determinantial objects를 invertible하게 만드는 category-level construction이다. 이 construction은 $\mathcal C_w$ 같은 monoidal subcategory에서 시작해 localized category $\widetilde{\mathcal C}_w$를 만든다.

이 page에서 localization은 ring localization의 analogy로만 이해하면 부족하다. 대상은 elements가 아니라 monoidal category의 objects이고, invertible하게 만드는 data는 determinantial modules와 braiding morphisms이다.

## Why it appears

Monoidal categorification에서는 algebraic multiplication을 module objects의 convolution product로 읽는다. 그런데 어떤 distinguished objects는 coordinate-ring side에서 denominator나 frozen variable처럼 작동하므로, category 안에서도 이 objects를 invertible하게 다룰 필요가 생긴다.

Localization은 이런 objects를 invertible하게 만든 뒤에도 simple objects, convolution, duality, Grothendieck-ring information을 추적할 수 있게 해 준다. Kashiwara-Nakashima의 localized crystal은 이 localized category 위에서 정의된다.

## Setup and notation

$R\text{-gmod}$는 quiver-Hecke algebra $R$의 finite-dimensional graded module category이다. $w\in W$에 대해 $\mathcal C_w$는 $R\text{-gmod}$ 안의 full monoidal subcategory이다.

$\Lambda_i$는 fundamental weights이고, $\mathsf M(w\Lambda_i,\Lambda_i)$는 determinantial module이다. Kashiwara-Nakashima의 source에서는 이 objects가 graded left braiders의 real commuting family를 이룬다.

Localization functor를
$$
\Phi_w:\mathcal C_w\longrightarrow\widetilde{\mathcal C}_w
$$
로 쓰면, $\widetilde{\mathcal C}_w$는 $\mathsf M(w\Lambda_i,\Lambda_i)$를 invertible하게 만든 localized monoidal category이다.

## Construction

$\widetilde{\mathcal C}_w$는 $\mathcal C_w$를 family
$$
\{\mathsf M(w\Lambda_i,\Lambda_i)\}_{i\in I}
$$
에 대해 localization하여 얻는다. Source는 이 family를 central objects로 다루며, 각 object가 다른 object와 교환되는 braiding morphism을 갖는다고 설명한다.

Theorem 5.3은 이 localized category가 rigid monoidal category라고 말한다. 또한 $R\text{-gmod}$의 simple module $M$을 localization하면 $\widetilde{\mathcal C}_w$ 안에서 simple object가 되거나 zero가 된다.

## Basic picture

$$
\mathcal C_w
\;\xrightarrow{\;\Phi_w\;}\;
\widetilde{\mathcal C}_w
\qquad
\mathsf M(w\Lambda_i,\Lambda_i)
\longmapsto
\text{invertible object}
$$

왼쪽 category에서는 determinantial objects가 distinguished objects로 놓인다. 오른쪽 localized category에서는 이 objects를 invertible하게 사용할 수 있고, 이 환경에서 simple-object crystal operators를 정의할 수 있다.

## Example

### Source example

Kashiwara-Nakashima는 $\mathfrak g=A_3$와
$$
w=s_2w_0=s_1s_2s_3s_2s_1
$$
인 경우를 예로 든다. 이때 $\mathcal C_w$는 $E_2M\simeq0$인 $R\text{-gmod}$의 objects로 표현된다.

이 example에서 $\widetilde{\mathcal C}_w$는 네 개의 clusters를 갖는 cluster algebra의 monoidal categorification으로 나타난다. Source는 frozen variables에 해당하는 determinantial objects와 cellular crystal 좌표로 가는 map $\operatorname{CP}$를 함께 기록한다.

## Main facts

- $\mathcal C_w$는 $R\text{-gmod}$ 안의 full monoidal subcategory이다.
- Determinantial objects $\mathsf M(w\Lambda_i,\Lambda_i)$는 localization에 쓰이는 central family를 이룬다.
- $\widetilde{\mathcal C}_w$는 이 family에 대한 localization으로 얻어진다.
- $\widetilde{\mathcal C}_w$는 rigid monoidal category이다.
- $\operatorname{Irr}(\widetilde{\mathcal C}_w)$에는 Kashiwara-Nakashima의 crystal structure가 정의된다.

## Why it matters

Localization은 determinantial objects를 category 안에서 denominator처럼 사용할 수 있게 해 준다. 그 결과 Grothendieck-ring-level comparison이나 cluster-theoretic frozen-variable intuition을 category-level construction으로 다룰 수 있다.

또한 localized category는 crystal structure를 만들기 위한 ambient category가 된다. Root operators $\widetilde E_i,\widetilde F_i$는 $\widetilde{\mathcal C}_w$ 안의 localized simple root objects와 convolution을 사용해서 정의된다.

## Connections

- [[topics/localized-crystals|Localized Crystals]]: $\operatorname{Irr}(\widetilde{\mathcal C}_w)$ 위의 crystal structure가 localization의 주요 응용이다.
- [[topics/determinantial-modules|Determinantial Modules]]: localization에서 invertible하게 되는 objects를 제공한다.
- [[topics/monoidal-categorification|Monoidal Categorification]]: localized category는 cluster algebra를 categorify하는 monoidal category로 나타날 수 있다.
- [[topics/quantum-coordinate-rings|Quantum Coordinate Rings]]: quantum unipotent coordinate category라는 이름은 coordinate-ring side와의 categorification 관계를 반영한다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/kashiwara-nakashima25-crystal-structure-localized-quantum-unipotent-coordinate-category|Kashiwara-Nakashima 2025]], Sections 5.1-5.2 and Theorem 5.3: construction and rigidity of $\widetilde{\mathcal C}_w$.
- Kashiwara-Nakashima 2025, Definition 6.11 and Theorem 6.13: localized root operators and crystal structure.
- Kashiwara-Nakashima 2025, Example 9.6: the $A_3$ monoidal-categorification example.
- [[sources/papers/kkko14-monoidal-categorification-cluster-algebras|KKKO14]], Definition 1.7, Definition 2.12, and Proposition 2.13: real simple modules, commuting, and convolution products of commuting real simples.
- [[sources/papers/kkop18-monoidal-categories-strata-flag-manifolds|KKOP18]], Section 2.2 and Corollary 5.4: earlier category notation and finite ADE category comparison used by this wiki.

</details>
