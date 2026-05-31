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

## 개요

Quiver-Hecke algebra localization은 quiver-Hecke, or KLR, algebra의 graded module category에서 특정 determinantial objects를 invertible하게 만드는 category-level construction이다. 이 construction은 $\mathcal C_w$ 같은 monoidal subcategory에서 시작해 localized category $\widetilde{\mathcal C}_w$를 만든다.

## 준비와 notation

$R\text{-gmod}$는 quiver-Hecke algebra $R$의 finite-dimensional graded module category이다. $w\in W$에 대해 $\mathcal C_w$는 $R\text{-gmod}$ 안의 full monoidal subcategory이다.

$\Lambda_i$는 fundamental weights이고, $\mathsf M(w\Lambda_i,\Lambda_i)$는 determinantial module이다. 이 objects는 graded left braiders의 real commuting family를 이룬다.

Localization functor를
$$
\Phi_w:\mathcal C_w\longrightarrow\widetilde{\mathcal C}_w
$$
로 쓰면, $\widetilde{\mathcal C}_w$는 $\mathsf M(w\Lambda_i,\Lambda_i)$를 invertible하게 만든 localized monoidal category이다.

## 구성

$\widetilde{\mathcal C}_w$의 input은 monoidal category $\mathcal C_w$와 graded left braiders로 이루어진 real commuting family
$$
\{\mathsf M(w\Lambda_i,\Lambda_i)\}_{i\in I}
$$
이다. Localization은 이 family의 각 object가 invertible object가 되도록 $\mathcal C_w$를 확장하고, 그 확장으로 가는 monoidal functor
$$
\Phi_w:\mathcal C_w\to\widetilde{\mathcal C}_w
$$
를 만든다.

구성의 output은 localized monoidal category $\widetilde{\mathcal C}_w$이다. 이 category 안에서는 $\Phi_w(\mathsf M(w\Lambda_i,\Lambda_i))$들이 tensor inverse를 가지며, $\mathcal C_w$의 objects는 localization functor를 통해 $\widetilde{\mathcal C}_w$ 안에서 비교된다.

Theorem 5.3은 이 localized category가 rigid monoidal category라고 말한다. 또한 $R\text{-gmod}$의 simple module $M$을 localization하면 $\widetilde{\mathcal C}_w$ 안에서 simple object가 되거나 zero가 된다.

## 기본 예시

### 실제 예시

Kashiwara-Nakashima는 $\mathfrak g=A_3$와
$$
w=s_2w_0=s_1s_2s_3s_2s_1
$$
인 경우를 예로 든다. 이때 $\mathcal C_w$는 $E_2M\simeq0$인 $R\text{-gmod}$의 objects로 표현된다.

이 example에서 $\widetilde{\mathcal C}_w$는 네 개의 clusters를 갖는 cluster algebra의 monoidal categorification으로 나타난다. Frozen variables에 해당하는 determinantial objects와 cellular crystal 좌표로 가는 map $\operatorname{CP}$가 함께 나타난다.

## 핵심 관점

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

## 기본 성질

- $\mathcal C_w$는 $R\text{-gmod}$ 안의 full monoidal subcategory이다.
- Determinantial objects $\mathsf M(w\Lambda_i,\Lambda_i)$는 localization에 쓰이는 graded left braiders의 real commuting family를 이룬다.
- $\widetilde{\mathcal C}_w$는 이 family에 대한 localization으로 얻어진다.
- $\widetilde{\mathcal C}_w$는 rigid monoidal category이다.
- $\operatorname{Irr}(\widetilde{\mathcal C}_w)$에는 Kashiwara-Nakashima의 crystal structure가 정의된다.

또한 localized category는 crystal structure를 만들기 위한 ambient category가 된다. Root operators $\widetilde E_i,\widetilde F_i$는 $\widetilde{\mathcal C}_w$ 안의 localized simple root objects와 convolution을 사용해서 정의된다.

## 다른 topic들과의 관계

- [[topics/quiver-hecke-algebras|Quiver-Hecke Algebras]]는 $R\text{-gmod}$와 convolution product가 사는 ambient category를 제공한다.
- [[topics/determinantial-modules|Determinantial Modules]]는 localization에서 invertible하게 되는 objects를 제공한다.
- [[topics/monoidal-categorification|Monoidal Categorification]]은 localized category가 cluster algebra를 categorify하는 방식을 설명한다.
- [[topics/quantum-coordinate-rings|Quantum Coordinate Rings]]는 quantum unipotent coordinate category라는 이름이 가리키는 coordinate-ring side를 제공한다.
- [[topics/localized-crystals|Localized Crystals]]는 $\operatorname{Irr}(\widetilde{\mathcal C}_w)$ 위의 crystal structure를 localization의 주요 응용으로 사용한다.

## 더 읽을 topic

- Prerequisite topics: [[topics/quiver-hecke-algebras|Quiver-Hecke Algebras]] for $R\text{-gmod}$; [[topics/determinantial-modules|Determinantial Modules]] for the objects being inverted; [[topics/monoidal-categorification|Monoidal Categorification]] for Grothendieck-ring context.
- Parent topics: [[topics/quiver-hecke-algebras|Quiver-Hecke Algebras]] is the broader algebra/category setting.
- Next topics: [[topics/localized-crystals|Localized Crystals]] for crystal operators on $\operatorname{Irr}(\widetilde{\mathcal C}_w)$; [[topics/cellular-crystals|Cellular Crystals]] for the combinatorial target.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/kashiwara-nakashima25-crystal-structure-localized-quantum-unipotent-coordinate-category|Kashiwara-Nakashima 2025]], Sections 5.1-5.2 and Theorem 5.3: construction and rigidity of $\widetilde{\mathcal C}_w$.
- Kashiwara-Nakashima 2025, Definition 6.11 and Theorem 6.13: localized root operators and crystal structure.
- Kashiwara-Nakashima 2025, Example 9.6: the $A_3$ monoidal-categorification example.
- [[sources/papers/kkko14-monoidal-categorification-cluster-algebras|KKKO14]], Definition 1.7, Definition 2.12, and Proposition 2.13: real simple modules, commuting, and convolution products of commuting real simples.
- [[sources/papers/kkop18-monoidal-categories-strata-flag-manifolds|KKOP18]], Section 2.2 and Corollary 5.4: earlier category notation and finite ADE category comparison used by this wiki.

</details>
