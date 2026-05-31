---
id: monoidal-categorification
title: Monoidal Categorification
level: advanced
---

# Monoidal Categorification

## What it is

Monoidal categorification은 cluster algebra나 quantum cluster algebra를 monoidal category의 Grothendieck ring으로 실현하는 방법이다. Category 안의 simple objects가 cluster variables와 cluster monomials의 역할을 하고, object들의 convolution product가 Grothendieck ring에서 multiplication으로 내려간다.

핵심은 세 층을 동시에 보되 섞지 않는 것이다. Object-level에서는 modules와 product $M\circ N$을 다루고, Grothendieck-ring-level에서는 classes $[M]$를 다루며, cluster-algebra-level에서는 cluster variables와 cluster monomials를 다룬다.

## Basic picture

$$
\text{real simple objects } M_i\in\mathcal C
\;\xrightarrow{\;[-]\;}\;
K_0(\mathcal C)
\;\xrightarrow{\;\sim\;}\;
\mathcal A
$$

$\mathcal C$는 monoidal category이고, $K_0(\mathcal C)$는 그 Grothendieck ring이다. Isomorphism $K_0(\mathcal C)\simeq\mathcal A$는 categorical object의 class를 cluster algebra의 element로 읽게 해 준다.

## Definition

Monoidal categorification은 monoidal category $\mathcal C$와 algebra $\mathcal A$ 사이의 Grothendieck-ring identification을 기본 자료로 가진다. 이 identification 아래에서 어떤 monoidal seed의 object classes가 $\mathcal A$의 initial seed가 되고, mutation도 category 안에서 대응되어야 한다.

Quantum version에서는 $\mathbb Z[q^{\pm 1/2}]$-linear Grothendieck ring을 quantum cluster algebra와 비교한다. 이때 quantum cluster monomials는 grading shift by $q$까지 허용하면 real simple objects의 classes로 나타난다.

## Example

**schematic.** Monoidal category $\mathcal C$ 안에 real simple objects $M_1,M_2$가 있고 서로 commute한다고 하자. 그러면 convolution product가 다시 real simple object로 작동하는 상황을 생각할 수 있고, Grothendieck ring에서는
$$
[M_1]\,[M_2]=[M_1\circ M_2]
$$
로 보인다.

이 예시는 object-level product가 class-level multiplication으로 바뀌는 방식을 보여 주는 schematic example이다.

## Main facts

- Real simple object는 self-convolution $M\circ M$이 simple인 simple object이다.
- Commuting family of real simple modules의 convolution product는 real simple로 남는다.
- Monoidal categorification에서는 cluster monomials가 real simple objects의 classes로 나타난다.
- Quantum monoidal seed는 $q$-commuting real simple objects와 exchange-matrix data를 함께 담는다.
- Admissible pair는 quantum monoidal seed와 mutation을 검증하기 위한 category-level criterion을 제공한다.

## Why it matters

Monoidal categorification은 cluster algebra의 combinatorics를 category 안의 objects와 exact sequences로 해석하게 해 준다. Cluster variable을 단순한 generator로만 보지 않고, concrete module object의 class로 읽을 수 있기 때문이다.

Strong commutation과 real simplicity는 cluster monomial이 하나의 simple object로 유지되는지를 통제한다. Grothendieck ring으로 내려가면 이 categorical information이 algebraic multiplication과 positivity statement를 설명하는 구조가 된다.

## Connections

- [[topics/quiver-hecke-algebra-localization|Quiver-Hecke Algebra Localization]]: symmetric quiver-Hecke module category는 monoidal categorification이 작동하는 주요 category-level 배경이다.
- [[topics/determinantial-modules|Determinantial Modules]]: $\mathcal C_{w,v}$ 안의 distinguished objects가 monoidal categorification에서 object-level anchors로 쓰인다.
- [[topics/quantum-coordinate-rings|Quantum Coordinate Rings]]: Grothendieck-ring comparison의 coordinate-ring-level target을 제공한다.
- [[topics/dual-canonical-bases|Dual Canonical Bases]]: algebra side에서 distinguished basis language를 제공한다.

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
