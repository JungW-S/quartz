---
id: graded-monoidal-categories
title: Graded Monoidal Categories
level: advanced
topic_kind: category
parent_topics:
  - monoidal-categorification
prerequisite_topics:
  - quiver-hecke-module-categories
child_topics:
  - affine-objects-in-monoidal-categories
  - r-matrix-renormalization
  - quasi-rigid-monoidal-categories
related_topics:
  - localized-crystals
maturity: definition-ready
---

## 개요

Graded monoidal category는 grading shift와 tensor product가 서로 호환되는 monoidal category이다. 이 page에서는 일반 monoidal category 이론 전체가 아니라, [[topics/affine-objects-in-monoidal-categories|affine objects]], [[topics/r-matrix-renormalization|R-matrix renormalization]], rational centers, localized root objects를 읽는 데 필요한 finite-length graded monoidal setting만 정리한다.

핵심은 object를 shift하는 functor $q$와 tensor product $\otimes$가 함께 움직인다는 점이다. 따라서 morphism의 degree, R-matrix의 degree $\Lambda(M,N)$, affine object의 parameter $z$의 degree 같은 수치가 같은 category 안에서 비교될 수 있다.

## 준비와 notation

$\mathbf k$를 base field라고 하자. $\mathscr C$는 abelian $\mathbf k$-linear category이고, 모든 object가 finite length를 가진다고 한다. Grading shift autoequivalence를
$$
q:\mathscr C\to\mathscr C
$$
로 쓴다.

Objects $M,N\in\mathscr C$에 대해 graded morphism space는
$$
\operatorname{HOM}_{\mathscr C}(M,N)
=
\bigoplus_{n\in\mathbb Z}
\operatorname{Hom}_{\mathscr C}(q^nM,N)
$$
로 모은다. 즉 degree $n$ morphism은 $q^nM$에서 $N$으로 가는 ordinary morphism으로 기록된다.

Tensor product는
$$
\otimes:\mathscr C\times\mathscr C\to\mathscr C
$$
로 쓴다. Unit object는 $\mathbf 1$로 쓴다.

## 정의

$\mathscr C$가 이 page의 의미에서 graded monoidal category라는 것은 다음 data와 조건을 가진다는 뜻이다.

1. $\mathscr C$는 finite-length abelian $\mathbf k$-linear graded category이고, grading shift autoequivalence $q$를 가진다.
2. Tensor product $\otimes$는 $\mathbf k$-bilinear이고 bi-exact이다.
3. Unit object $\mathbf 1$은 simple이고
   $$
   \operatorname{End}_{\mathscr C}(\mathbf 1)\simeq\mathbf k
   $$
   를 만족한다.
4. Tensor product는 grading shift와 호환된다.
   $$
   q(X\otimes Y)
   \simeq
   (qX)\otimes Y
   \simeq
   X\otimes(qY).
   $$

이 호환성 때문에 $q$는 invertible central object $q\mathbf 1$로 tensoring하는 것처럼 다룰 수 있다.

Object $X$의 right dual이 $Y$라는 것은 morphisms
$$
\varepsilon:X\otimes Y\to\mathbf 1,
\qquad
\eta:\mathbf 1\to Y\otimes X
$$
가 있어서 두 composite
$$
X\simeq X\otimes\mathbf 1
\xrightarrow{\operatorname{id}_X\otimes\eta}
X\otimes Y\otimes X
\xrightarrow{\varepsilon\otimes\operatorname{id}_X}
\mathbf 1\otimes X\simeq X
$$
와
$$
Y\simeq \mathbf 1\otimes Y
\xrightarrow{\eta\otimes\operatorname{id}_Y}
Y\otimes X\otimes Y
\xrightarrow{\operatorname{id}_Y\otimes\varepsilon}
Y\otimes\mathbf 1\simeq Y
$$
가 identity가 된다는 뜻이다. Left dual도 반대 방향으로 정의한다. 모든 object가 right dual과 left dual을 가지면 monoidal category를 rigid라고 한다.

## 기본 예시

### 구조 예시

Grading shift와 tensor product의 호환성은 tensor product 안에서 shift를 어느 factor에 둘지 바꾸어도 같은 object로 볼 수 있게 한다.

$$
q(X\otimes Y)
\simeq
(qX)\otimes Y
\simeq
X\otimes(qY).
$$

따라서 degree를 가진 morphism
$$
f\in\operatorname{Hom}_{\mathscr C}(q^nM,N)
$$
을 tensor product와 함께 사용할 때, $q$-shift가 tensor product 전체의 degree bookkeeping과 양립한다. 이 예시는 concrete category의 예가 아니라, later pages에서 R-matrix degree와 $z$-degree를 읽기 위한 구조 예시이다.

검증: 논문 예시

## 핵심 관점

이 setting의 핵심은 세 가지 structure를 동시에 유지하는 것이다.

$$
\text{finite-length abelian category}
\quad+\quad
\text{grading shift }q
\quad+\quad
\text{tensor product }\otimes.
$$

[[topics/r-matrix-renormalization|R-Matrix Renormalization]]에서는 morphism
$$
R_{M,N}:M\otimes N\to N\otimes M
$$
의 homogeneous degree가 $\Lambda(M,N)$로 기록된다. [[topics/affine-objects-in-monoidal-categories|Affine Objects in Monoidal Categories]]에서는 affine parameter $z$도 positive homogeneous degree를 가진다. 두 이야기가 같은 language로 이어지려면 grading shift와 tensor product가 호환되어야 한다.

## 기본 성질

- $\operatorname{HOM}_{\mathscr C}(M,N)$는 ordinary morphism spaces $\operatorname{Hom}_{\mathscr C}(q^nM,N)$를 모든 degree $n$에 대해 모은 graded morphism space이다.
- Tensor product가 bi-exact이므로 짧은 exact-sequence 정보가 tensor product와 잘 맞는 setting에서 쓰인다.
- Unit object $\mathbf 1$은 simple이고 endomorphism ring이 $\mathbf k$이다.
- Shift $q$는 tensor product와 호환되며, 이 setting에서는 $q\mathbf 1$이라는 invertible central object와 동일시해서 쓴다.
- $\operatorname{Pro}(\mathscr C)$에도 monoidal structure가 있으며, affine-object construction은 이 pro-category level의 tensor product를 사용한다.
- $\mathscr C$가 rigid이면 [[topics/affine-objects-in-monoidal-categories|affine objects]]의 category $\operatorname{Aff}(\mathscr C)$도 rigid monoidal category가 된다.

## 다른 topic들과의 관계

- [[topics/pro-categories|Pro-Categories]]는 $\mathscr C$를 completed objects가 사는 $\operatorname{Pro}(\mathscr C)$로 확장하는 language를 제공한다.
- [[topics/affine-objects-in-monoidal-categories|Affine Objects in Monoidal Categories]]는 graded monoidal setting 위에서 $(\widehat M,z)$와 $\operatorname{Aff}(\mathscr C)$를 정의한다.
- [[topics/r-matrix-renormalization|R-Matrix Renormalization]]는 graded morphism의 degree를 사용해 $\Lambda(M,N)$, $\mathfrak d(M,N)$, $\widetilde\Lambda(X,Y)$를 정의한다.
- [[topics/quiver-hecke-module-categories|Quiver-Hecke Module Categories]]는 이 wiki에서 later applications가 일어나는 concrete category-level setting을 제공한다.
- [[topics/quasi-rigid-monoidal-categories|Quasi-Rigid Monoidal Categories]]는 root-object arguments에서 필요한 후속 monoidal-category condition이다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/quiver-hecke-module-categories|Quiver-Hecke Module Categories]]에서 concrete module-category setting을 읽고, [[topics/pro-categories|Pro-Categories]]에서 affine object에 쓰이는 pro-object completion을 읽는다.
- 상위 개념: [[topics/monoidal-categorification|Monoidal Categorification]]이 더 넓은 categorical framework이다.
- 다음에 읽을 것: [[topics/affine-objects-in-monoidal-categories|Affine Objects in Monoidal Categories]]에서는 $z$-adic affine object를 읽고, [[topics/r-matrix-renormalization|R-Matrix Renormalization]]에서는 R-matrix degree를 읽고, [[topics/quasi-rigid-monoidal-categories|Quasi-Rigid Monoidal Categories]]에서는 뒤의 root-object argument에 필요한 categorical condition을 읽는다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/kashiwara-nakashima25-crystal-structure-localized-quantum-unipotent-coordinate-category|Kashiwara-Nakashima 2025]], lines 1550-1577 of `inbox/papers/crystal.tex`: finite-length graded $\mathbf k$-linear category assumptions, grading shift $q$, and $\operatorname{HOM}_{\mathscr C}(M,N)$.
- Kashiwara-Nakashima 2025, lines 1646-1669: graded monoidal category assumptions, bi-exact tensor product, simple unit, and compatibility with $q$.
- Kashiwara-Nakashima 2025, lines 1670-1676: $q$ as the invertible central object $q\mathbf 1$ and monoidal structure on $\operatorname{Pro}(\mathscr C)$.
- Kashiwara-Nakashima 2025, lines 1679-1690: left and right duals and rigidity.
- Kashiwara-Nakashima 2025, lines 1717-1728: monoidal product on $\operatorname{Aff}(\mathscr C)$ and rigidity of $\operatorname{Aff}(\mathscr C)$ when $\mathscr C$ is rigid.
- Fillability review: `reports/reviews/2026-06-01-pro-graded-prerequisite-fillability-review.md`.

</details>
