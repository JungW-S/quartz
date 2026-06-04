---
id: quasi-rigid-monoidal-categories
title: Quasi-Rigid Monoidal Categories
level: advanced
topic_kind: category
parent_topics:
  - graded-monoidal-categories
prerequisite_topics:
  - affine-objects-in-monoidal-categories
  - r-matrix-renormalization
child_topics:
  - root-objects-in-localized-categories
related_topics:
  - localized-crystals
maturity: definition-ready
---

## 개요

Quasi-rigid monoidal category는 세 tensor factor
$$
L\otimes M\otimes N
$$
안에서 왼쪽과 오른쪽의 subobject 정보가 양립할 때, 그 양립성이 가운데 factor $M$의 subobject에서 온다고 요구하는 abelian monoidal category이다. 이 조건은 head, socle, R-matrix image를 category 안에서 통제하기 위해 쓰인다.

Localized crystal construction에서는 affreal simple object와 simple object의 tensor product를 반복해서 다룬다. Quasi-rigidity가 있으면 R-matrix image가 simple head와 simple socle을 통제하고, head convolution에 대한 inverse-type statement와 R-matrix degree estimate를 사용할 수 있다.

여기서 필요한 내용은 일반 category theory의 넓은 rigidity 이론이 아니다. 목적은 [[topics/03-category-theory/affine-objects-in-monoidal-categories|Affine Objects in Monoidal Categories]], [[topics/06-quiver-hecke-klr-algebras/r-matrix-renormalization|R-Matrix Renormalization]], [[topics/08-localization-of-categories/root-objects-in-localized-categories|Root Objects in Localized Categories]] 사이에서 쓰이는 정확한 axiom을 고정하는 것이다.

## 준비와 notation

$\mathscr A$를 monoidal category라고 하자. Tensor product는
$$
\otimes
$$
로 쓴다. $X\subset L\otimes M$은 $L\otimes M$ 안의 subobject를 뜻한다.

정의에서 세 objects
$$
L,\quad M,\quad N
$$
이 등장한다. 여기서 $M$은 가운데 factor이다. Quasi-rigid axiom의 핵심은 $L\otimes M\otimes N$ 안에서 왼쪽 두 factor와 오른쪽 두 factor의 subobject 조건이 양립할 때, 그 양립성이 가운데 factor $M$ 안의 어떤 subobject $K\subset M$에서 온다고 말하는 것이다.

Head와 socle은 각각
$$
\operatorname{hd}(X),
\qquad
\operatorname{soc}(X)
$$
로 쓴다. Head convolution은
$$
M\nabla N:=\operatorname{hd}(M\otimes N)
$$
으로 쓴다.

## 정의

Monoidal category $(\mathscr A,\otimes)$가 quasi-rigid monoidal category라는 것은 다음 조건들을 만족한다는 뜻이다.

1. $\mathscr A$는 abelian category이고, tensor product $\otimes$는 bi-exact이다.

2. 임의의 $L,M,N\in\mathscr A$와 subobjects
   $$
   X\subset L\otimes M,
   \qquad
   Y\subset M\otimes N
   $$
   가 주어졌다고 하자. 만약 $L\otimes M\otimes N$ 안에서
   $$
   X\otimes N
   \subset
   L\otimes Y
   \subset
   L\otimes M\otimes N
   $$
   이면, 어떤 subobject $K\subset M$이 존재해서
   $$
   X\subset L\otimes K,
   \qquad
   K\otimes N\subset Y
   $$
   를 만족해야 한다.

3. 반대 방향 조건도 요구한다. 임의의 $L,M,N\in\mathscr A$와 subobjects
   $$
   X\subset M\otimes N,
   \qquad
   Y\subset L\otimes M
   $$
   가 주어졌고
   $$
   L\otimes X
   \subset
   Y\otimes N
   \subset
   L\otimes M\otimes N
   $$
   이면, 어떤 subobject $K\subset M$이 존재해서
   $$
   X\subset K\otimes N,
   \qquad
   L\otimes K\subset Y
   $$
   를 만족해야 한다.

## 기본 예시

Quiver-Hecke module setting에서 다음 monoidal categories는 quasi-rigid이다.

$$
R\text{-gMod},
\qquad
R\text{-gmod},
\qquad
\mathcal C_w.
$$

또한 abelian rigid monoidal category는 quasi-rigid이다. 따라서 localized category
$$
\widetilde{\mathcal C}_w
$$
가 rigid임을 알고 있으면, $\widetilde{\mathcal C}_w$도 quasi-rigid이다.

검증: 논문 예시

## 핵심 관점

Quasi-rigidity는 tensor product의 가운데 factor를 통제하는 조건이다. 세 factor
$$
L\otimes M\otimes N
$$
안에서 왼쪽의 subobject 정보와 오른쪽의 subobject 정보가 양립하면, 그 양립성이 가운데 object $M$의 subobject $K$를 통해 설명된다는 것이 핵심이다.

이 조건은 추상적인 subobject axiom처럼 보이지만, 실제 역할은 R-matrix image가 사라지지 않고 head나 socle에 도달하도록 만드는 데 있다. 특히 가운데 factor가 simple일 때, 두 nonzero morphisms를 tensor product 안에서 이어 붙인 composition이 nonzero임을 보장하는 lemma가 이 axiom에서 나온다.

## 기본 성질

### Rigid category와의 관계

Abelian rigid monoidal category는 quasi-rigid이다. 따라서 duality가 충분히 존재하는 rigid setting에서는 quasi-rigid axiom을 별도로 다시 확인하지 않고 사용할 수 있다.

### Nonvanishing composition

$M_1,M_2,M_3$가 nonzero objects이고 $M_2$가 simple이라고 하자. Nonzero morphisms
$$
\varphi_1:L\to M_1\otimes M_2,
\qquad
\varphi_2:M_2\otimes M_3\to L'
$$
가 있으면, quasi-rigidity는 composition
$$
L\otimes M_3
\xrightarrow{\varphi_1\otimes M_3}
M_1\otimes M_2\otimes M_3
\xrightarrow{M_1\otimes\varphi_2}
M_1\otimes L'
$$
이 0이 되지 않도록 보장한다.

### Affreal object와 head/socle

$\mathscr A$가 quasi-rigid이고 $M$이 affreal object, $N$이 simple object이면 $M\otimes N$과 $N\otimes M$은 simple head와 simple socle을 가진다. 이때 R-matrix image는 head와 socle을 식별한다.

이 성질은 [[topics/06-quiver-hecke-klr-algebras/head-simplicity-of-convolutions|Head Simplicity of Convolutions]]와 [[topics/06-quiver-hecke-klr-algebras/normal-sequences|Normal Sequences]]에서 쓰이는 category-level 기반이다.

### Degree control

Real simple object $L$이 degree $2d$의 affinization을 가지면, quasi-rigidity는 $\mathfrak d(L,X)$와 $\Lambda$-degree에 대한 divisibility와 nonnegativity control을 제공한다.

이 결과는 [[topics/08-localization-of-categories/root-objects-in-localized-categories|Root Objects in Localized Categories]]에서 root-object condition과 head convolution의 degree 변화를 다룰 때 필요하다.

## 다른 topic들과의 관계

**Graded Monoidal Categories.** [[topics/03-category-theory/graded-monoidal-categories|Graded Monoidal Categories]]는 tensor product, grading shift, bi-exactness가 놓이는 ambient language를 제공한다.

**Affine Objects in Monoidal Categories.** [[topics/03-category-theory/affine-objects-in-monoidal-categories|Affine Objects in Monoidal Categories]]는 affreal object를 정의하는 데 필요한 affinization을 제공한다.

**R-Matrix Renormalization.** [[topics/06-quiver-hecke-klr-algebras/r-matrix-renormalization|R-Matrix Renormalization]]는 $\Lambda$, $\mathfrak d$, R-matrix image notation을 제공한다.

**Normal Sequences.** [[topics/06-quiver-hecke-klr-algebras/normal-sequences|Normal Sequences]]는 quasi-rigid monoidal category 위에서 composed R-matrix가 head와 socle을 통제하는 상황을 다룬다.

**Root Objects in Localized Categories.** [[topics/08-localization-of-categories/root-objects-in-localized-categories|Root Objects in Localized Categories]]는 quasi-rigidity에서 얻은 head/socle 및 degree-control 도구를 localized category 안의 root direction에 적용한다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/03-category-theory/graded-monoidal-categories|Graded Monoidal Categories]]에서 tensor product와 exactness setting을 읽고, [[topics/03-category-theory/affine-objects-in-monoidal-categories|Affine Objects in Monoidal Categories]]에서 affreal object를 읽는다.
- 상위 개념: [[topics/03-category-theory/graded-monoidal-categories|Graded Monoidal Categories]]가 더 넓은 categorical 배경이다.
- 다음에 읽을 것: [[topics/06-quiver-hecke-klr-algebras/head-simplicity-of-convolutions|Head Simplicity of Convolutions]]에서 simple head/socle theorem을 읽고, [[topics/08-localization-of-categories/root-objects-in-localized-categories|Root Objects in Localized Categories]]에서 $\mathfrak d$ condition으로 넘어간다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/kashiwara-nakashima25-crystal-structure-localized-quantum-unipotent-coordinate-category|Kashiwara-Nakashima 2025]], lines 1845-1876 of `inbox/papers/crystal.tex`: quasi-rigid axiom.
- Kashiwara-Nakashima 2025, lines 1882-1895: nonvanishing composition lemma and rigid-implies-quasi-rigid lemma.
- Kashiwara-Nakashima 2025, lines 1900-1905: examples $R\text{-gMod}$, $R\text{-gmod}$, $\mathcal C_w$, and $\widetilde{\mathcal C}_w$.
- Kashiwara-Nakashima 2025, lines 1911-1952: simple head/socle and R-matrix image control for an affreal object and a simple object.
- Kashiwara-Nakashima 2025, lines 1958-2018: inverse behavior for head convolution and degree-control consequences.
- Source-location review: `reports/reviews/2026-06-03-quasi-rigid-axiom-source-location-review.md`.

</details>
