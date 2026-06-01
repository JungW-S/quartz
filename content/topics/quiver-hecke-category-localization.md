---
id: quiver-hecke-category-localization
title: Quiver-Hecke Category Localization
level: advanced
topic_kind: construction
parent_topics:
  - category-localization
  - quiver-hecke-subcategories
prerequisite_topics:
  - category-localization
  - quiver-hecke-subcategories
  - determinantial-modules
  - monoidal-categorification
child_topics:
  - localized-crystals
  - root-objects-in-localized-categories
  - reverse-equivalence-of-localized-categories
related_topics:
  - quantum-coordinate-rings
maturity: study-ready
---

## 개요

Quiver-Hecke category localization은 [[topics/quiver-hecke-subcategories|$\mathcal C_w$ 같은 quiver-Hecke subcategory]]에서 특정 determinantial objects를 invertible하게 만드는 category-level construction이다. 여기서 localize되는 것은 quiver-Hecke algebra 자체가 아니라 monoidal subcategory이고, output은 localized category $\widetilde{\mathcal C}_w$이다.

이 construction은 localized crystal을 만들기 위한 category-level 출발점이다. 먼저 $\mathcal C_w$를 $\widetilde{\mathcal C}_w$로 보내고, 그 다음 $\widetilde{\mathcal C}_w$의 simple objects 위에서 crystal operators를 정의한다.

## 준비와 notation

$R\text{-gmod}$는 quiver-Hecke algebra $R$의 finite-dimensional graded module category이다. $w\in W$에 대해 $\mathcal C_w$는 $R\text{-gmod}$ 안의 full monoidal subcategory이다. 이 ambient category와 subcategory notation은 [[topics/quiver-hecke-module-categories|Quiver-Hecke Module Categories]]와 [[topics/quiver-hecke-subcategories|Quiver-Hecke Subcategories]]에서 먼저 분리해 둔다.

$\Lambda_i$는 fundamental weights이고, $\mathsf M(w\Lambda_i,\Lambda_i)$는 determinantial module이다. 이 objects는 graded left braiders의 real commuting family를 이룬다.

Localization functor를
$$
\Phi_w:\mathcal C_w\longrightarrow\widetilde{\mathcal C}_w
$$
로 쓰면, $\widetilde{\mathcal C}_w$는 $\mathsf M(w\Lambda_i,\Lambda_i)$를 invertible하게 만든 localized monoidal category이다.
이 formal localization construction은 [[topics/category-localization|Category Localization]]에서 설명한 real commuting family of braiders에 대한 localization의 quiver-Hecke instance이다.

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

이 예시에서 $\widetilde{\mathcal C}_w$는 cluster algebra의 monoidal categorification으로 나타난다. 여기서는 determinantial objects가 localization에서 invertible하게 쓰인다는 점만 사용하고, cellular crystal 좌표와의 비교는 [[topics/crystal-comparison-map|Crystal Comparison Map]]에서 읽는다.

검증: 논문 예시

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

### Localization에 쓰이는 data

- $\mathcal C_w$는 $R\text{-gmod}$ 안의 full monoidal subcategory이다.
- Determinantial objects $\mathsf M(w\Lambda_i,\Lambda_i)$는 localization에 쓰이는 graded left braiders의 real commuting family를 이룬다.
- $\widetilde{\mathcal C}_w$는 이 family에 대한 localization으로 얻어진다.

### Category-level 사실

- $\widetilde{\mathcal C}_w$는 rigid monoidal category이다.

### Crystal 쪽 쓰임

- $\operatorname{Irr}(\widetilde{\mathcal C}_w)$에는 Kashiwara-Nakashima의 crystal structure가 정의된다.

Localized category는 crystal structure를 만들기 위한 ambient category가 된다. Root operators $\widetilde E_i,\widetilde F_i$는 $\widetilde{\mathcal C}_w$ 안의 localized simple root objects와 convolution을 사용해서 정의된다.

## 다른 topic들과의 관계

- [[topics/category-localization|Category Localization]]은 chosen data를 invertible하게 만드는 더 넓은 category-level idea이다.
- [[topics/quiver-hecke-module-categories|Quiver-Hecke Module Categories]]는 $R\text{-gmod}$와 convolution product가 사는 ambient category를 제공한다.
- [[topics/quiver-hecke-subcategories|Quiver-Hecke Subcategories]]는 localization input인 $\mathcal C_w$를 제공한다.
- [[topics/determinantial-modules|Determinantial Modules]]는 localization에서 invertible하게 되는 objects를 제공한다.
- [[topics/monoidal-categorification|Monoidal Categorification]]은 localized category가 cluster algebra를 categorify하는 방식을 설명한다.
- [[topics/quantum-coordinate-rings|Quantum Coordinate Rings]]는 quantum unipotent coordinate category라는 이름이 가리키는 coordinate-ring side를 제공한다.
- [[topics/localized-crystals|Localized Crystals]]는 $\operatorname{Irr}(\widetilde{\mathcal C}_w)$ 위의 crystal structure를 localization의 주요 응용으로 사용한다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/category-localization|Category Localization]]에서 더 넓은 construction slot을 읽고, [[topics/quiver-hecke-subcategories|Quiver-Hecke Subcategories]]에서 $\mathcal C_w$를 읽고, [[topics/determinantial-modules|Determinantial Modules]]에서 invertible하게 만드는 objects를 읽고, [[topics/monoidal-categorification|Monoidal Categorification]]에서 Grothendieck-ring context를 읽는다.
- 상위 개념: [[topics/category-localization|Category Localization]]가 더 넓은 localization setting이고, [[topics/quiver-hecke-subcategories|Quiver-Hecke Subcategories]]가 직접적인 quiver-Hecke category setting이다.
- 다음에 읽을 것: [[topics/localized-crystals|Localized Crystals]]에서는 $\operatorname{Irr}(\widetilde{\mathcal C}_w)$ 위의 crystal operators를 읽고, [[topics/cellular-crystals|Cellular Crystals]]에서는 combinatorial target을 읽는다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/kashiwara-nakashima25-crystal-structure-localized-quantum-unipotent-coordinate-category|Kashiwara-Nakashima 2025]], Sections 5.1-5.2 and Theorem 5.3: construction and rigidity of $\widetilde{\mathcal C}_w$.
- Kashiwara-Nakashima 2025, Definition 6.11 and Theorem 6.13: localized root operators and crystal structure.
- Kashiwara-Nakashima 2025, Example 9.6: the $A_3$ monoidal-categorification example.
- [[sources/papers/kkop21-localizations-quiver-hecke-algebras|KKOP21]], Definitions 2.1-2.2, Theorem 2.7, Proposition 5.1, Section 5.1, Corollary 5.4, and Corollary 5.11: braider localization machinery, the construction $\mathcal C_w\to\widetilde{\mathcal C}_w$, Grothendieck-ring localization, and left rigidity.
- [[sources/papers/kkko14-monoidal-categorification-cluster-algebras|KKKO14]], Definition 1.7, Definition 2.12, and Proposition 2.13: real simple modules, commuting, and convolution products of commuting real simples.
- [[sources/papers/kkop18-monoidal-categories-strata-flag-manifolds|KKOP18]], Section 2.2 and Corollary 5.4: earlier category notation and finite ADE category comparison used here.

</details>
