---
id: monoidal-categorification
title: Monoidal Categorification
level: advanced
topic_kind: root
parent_topics: []
prerequisite_topics:
  - quantum-coordinate-rings
  - quiver-hecke-module-categories
child_topics:
  - determinantial-modules
  - graded-monoidal-categories
related_topics:
  - quiver-hecke-subcategories
  - quiver-hecke-category-localization
  - localized-crystals
maturity: definition-ready
---

## 개요

Monoidal categorification은 cluster algebra나 quantum cluster algebra를 monoidal category의 Grothendieck ring으로 실현하는 방법이다. Category 안의 simple objects가 cluster variables와 cluster monomials의 역할을 하고, object들의 convolution product가 Grothendieck ring에서 multiplication으로 내려간다.

핵심은 세 층을 동시에 보되 섞지 않는 것이다. Object-level에서는 modules와 product $M\circ N$을 다루고, Grothendieck-ring-level에서는 classes $[M]$를 다루며, cluster-algebra-level에서는 cluster variables와 cluster monomials를 다룬다.

Monoidal categorification은 quiver-Hecke module categories, determinantial modules, localized categories, and quantum coordinate rings를 한 framework 안에서 비교할 때 사용된다.

## 준비와 notation

$\mathcal C$를 monoidal category라고 하고, $K_0(\mathcal C)$를 그 Grothendieck ring이라고 쓰자. Object $M\in\mathcal C$의 class는 $[M]\in K_0(\mathcal C)$로 쓴다.

Quiver-Hecke setting에서는 objects의 product를 convolution product
$$
M\circ N
$$
으로 쓴다. Cluster algebra 또는 quantum cluster algebra 쪽 target을 $\mathcal A$라고 쓰면, monoidal categorification은 $K_0(\mathcal C)$와 $\mathcal A$를 비교한다.

## 정의

Monoidal categorification of a cluster algebra $\mathcal A$는 다음 data와 조건으로 이루어진다.

- $k$-linear abelian monoidal category $\mathcal C$.
- Grothendieck ring isomorphism
  $$
  K_0(\mathcal C)\simeq \mathcal A.
  $$
- Monoidal seed $S=(\{M_i\}_{i\in J},\widetilde B)$ in $\mathcal C$ such that the classes
  $$
  [S]=(\{[M_i]\}_{i\in J},\widetilde B)
  $$
  form the initial seed of $\mathcal A$.
- The seed $S$ admits successive mutations in all exchange directions, so mutated cluster variables are still represented by classes of objects in $\mathcal C$.

Quantum monoidal categorification replaces this by the graded comparison
$$
\mathbb Z[q^{\pm 1/2}]
\otimes_{\mathbb Z[q^{\pm 1}]}K_0(\mathcal C)
\simeq
\mathcal A
$$
with a quantum monoidal seed. In KKKO14 this seed has data
$$
(\{M_i\}_{i\in J},L,\widetilde B,D),
$$
where the $M_i$ are real simple objects, $L$ records $q$-commutation, $\widetilde B$ is the exchange matrix, and $D$ records weights or degrees. Under this definition, quantum cluster monomials are represented by real simple objects up to a power of $q^{1/2}$.

## 핵심 관점

$$
\text{real simple objects } M_i\in\mathcal C
\;\xrightarrow{\;[-]\;}\;
K_0(\mathcal C)
\;\xrightarrow{\;\sim\;}\;
\mathcal A
$$

$\mathcal C$는 monoidal category이고, $K_0(\mathcal C)$는 그 Grothendieck ring이다. Isomorphism $K_0(\mathcal C)\simeq\mathcal A$는 categorical object의 class를 cluster algebra의 element로 읽게 해 준다.

## 기본 성질

- Real simple object는 self-convolution $M\circ M$이 simple인 simple object이다.
- Commuting family of real simple modules의 convolution product는 real simple로 남는다.
- Monoidal categorification에서는 cluster monomials가 real simple objects의 classes로 나타난다.
- Quantum monoidal seed는 $q$-commuting real simple objects와 exchange-matrix data를 함께 담는다.
- Admissible pair는 quantum monoidal seed와 mutation을 검증하기 위한 category-level criterion을 제공한다.

## 다른 topic들과의 관계

- [[topics/quiver-hecke-module-categories|Quiver-Hecke Module Categories]]는 convolution product와 Grothendieck ring이 나오는 ambient category를 제공한다.
- [[topics/quiver-hecke-subcategories|Quiver-Hecke Subcategories]]는 $\mathcal C_w$와 $\mathcal C_{w,v}$처럼 monoidal categorification에서 쓰이는 smaller category environments를 제공한다.
- [[topics/quiver-hecke-category-localization|Quiver-Hecke Category Localization]]은 symmetric quiver-Hecke module category에서 localization을 통해 monoidal categorification이 작동하는 주요 category-level 배경을 제공한다.
- [[topics/determinantial-modules|Determinantial Modules]]는 $\mathcal C_{w,v}$ 안의 distinguished objects로서 monoidal categorification에서 object-level anchors로 쓰인다.
- [[topics/quantum-coordinate-rings|Quantum Coordinate Rings]]는 Grothendieck-ring comparison의 coordinate-ring-level target을 제공한다.
- [[topics/dual-canonical-bases|Dual Canonical Bases]]는 algebra side에서 distinguished basis language를 제공한다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/quantum-coordinate-rings|Quantum Coordinate Rings]]에서 coordinate-ring target을 읽고, [[topics/quiver-hecke-module-categories|Quiver-Hecke Module Categories]]에서 examples에 쓰이는 module categories를 읽는다.
- 상위 개념: 별도의 상위 topic 없이 categorification 쪽의 출발점으로 읽는다.
- 다음에 읽을 것: [[topics/determinantial-modules|Determinantial Modules]]에서는 distinguished objects를 읽고, [[topics/quiver-hecke-category-localization|Quiver-Hecke Category Localization]]에서는 localized monoidal categories를 읽고, [[topics/localized-crystals|Localized Crystals]]에서는 simple objects 위의 crystal structures를 읽는다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/kkko14-monoidal-categorification-cluster-algebras|KKKO14]], Definition 1.7: real simple modules.
- KKKO14, Definition 5.3 and Definition 5.8: monoidal categorification of cluster algebras and quantum cluster algebras; this page writes the Grothendieck ring as $K_0(\mathcal C)$.
- KKKO14, Definition 5.4: quantum monoidal seed.
- KKKO14, Definition 6.1, Proposition 6.2, Theorem 6.3, and Corollary 6.4: admissible pairs and the categorification criterion.
- [[sources/papers/kkop18-monoidal-categories-strata-flag-manifolds|KKOP18]], Section 2.2 and Theorem 2.20(ii)(c): $\mathcal C_{w,v}$ and the comparison with $A_{w,v}$.
- [[sources/papers/gls11-cluster-structures-quantum-coordinate-rings|GLS11]], Theorem 12.3: quantum cluster algebra attached to $\mathcal C_w$ and $A_q(\mathfrak n(w))$.

</details>
