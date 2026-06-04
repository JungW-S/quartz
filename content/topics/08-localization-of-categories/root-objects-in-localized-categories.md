---
id: root-objects-in-localized-categories
title: Root Objects in Localized Categories
level: advanced
topic_kind: object-family
parent_topics:
  - quiver-hecke-category-localization
  - quasi-rigid-monoidal-categories
prerequisite_topics:
  - affine-objects-in-monoidal-categories
  - r-matrix-renormalization
  - quiver-hecke-category-localization
child_topics:
  - localized-root-operators
related_topics:
  - localized-crystals
maturity: study-ready
---

## 개요

Root object는 localized monoidal category $\widetilde{\mathcal C}_w$ 안의 real simple object 중에서, affinization과 duality에 대한 R-matrix degree 조건을 만족하는 object이다. 이 개념은 simple root 방향을 category 안에서 다루기 위한 object-level 입력으로 나타난다.

Crystal graph에서는 simple root index $i$가 arrow 방향을 정한다. [[topics/08-localization-of-categories/localized-root-operators|Localized Root Operators]]에서는 그 방향을 실제 simple object와 convolution으로 표현해야 하므로, 어떤 simple object가 root direction처럼 작동하는지 판별하는 조건이 필요하다. Root object는 바로 그 조건을 만족하는 simple object이다.

## 준비와 notation

$w$를 Weyl group의 원소로 두고, $\widetilde{\mathcal C}_w$를 [[topics/08-localization-of-categories/quiver-hecke-category-localization|Quiver-Hecke Category Localization]]에서 얻는 localized monoidal category로 둔다. 이 category는 duality functor를 가지며, 아래에서는 그 functor를 $\mathscr D$로 쓴다.

$L$이 $\widetilde{\mathcal C}_w$의 simple object일 때, $L$이 real이라는 것은 $L\circ L$이 다시 simple object라는 뜻이다. 여기서 $\circ$는 convolution product이다. Root object의 후보는 먼저 이 real simple object여야 한다.

Root object의 정의에 필요한 affinization data는 pair $(\widehat L,z)$이다. 여기서 $\widehat L$은 affine object이고, $z$는 positive homogeneous degree를 가지는 endomorphism이며, $\widehat L/z\widehat L\simeq L$이다. $\deg(z)$가 affinization의 degree이다.

Simple objects $M,N$ 사이의 [[topics/06-quiver-hecke-klr-algebras/r-matrix-renormalization|R-matrix degree]]를 $\Lambda(M,N)$로 쓰고, 양방향 R-matrix degree가 정의되는 경우
$$
\mathfrak d(M,N)
=\frac{\Lambda(M,N)+\Lambda(N,M)}{2}
$$
로 둔다. Root object의 정의에는 $\mathfrak d(L,\mathscr D^{-1}L)$이 들어간다.

$i\in I_w$에 붙는 localized simple-root object는
$$
\widetilde Q_i=Q_w(\langle i\rangle)
$$
로 쓴다. 이 object는 localized root operators에서 중요하지만, root object의 정의 자체는 임의의 real simple object $L$에 대한 조건이다.

## 정의

$L\in\widetilde{\mathcal C}_w$를 real simple object라고 하자. 양의 정수 $d_L\in\mathbb Z_{>0}$에 대해, $L$이 degree $d_L$의 root object라는 것은 다음 두 조건을 만족한다는 뜻이다.

1. $L$은 affinization $(\widehat L,z)$를 가지며
   $$
   \deg(z)=2d_L
   $$
   이다.
2. Duality와 R-matrix degree invariant가
   $$
   \mathfrak d(L,\mathscr D^{-1}L)=d_L
   $$
   을 만족한다.

따라서 root object는 단순히 real simple object인 것만으로 정해지지 않는다. Affinization의 degree와 dual object에 대한 R-matrix degree가 같은 정수 $d_L$로 맞아떨어져야 한다.

## 기본 예시

### 조건부 예시

$i\in I_w$이고 $X$가 $\widetilde{\mathcal C}_w$의 simple object라고 하자. Localized simple-root object
$$
\widetilde Q_i=Q_w(\langle i\rangle)
$$
에 대해
$$
\mathsf d_i(X)>0
$$
인 branch에서는 $\widetilde Q_i$가 root object로 작동한다.

이 예시는 root object가 localized simple-root object와 만나는 방식을 보여 준다. $\widetilde Q_i$가 모든 경우에 root object인 것은 아니지만, $\mathsf d_i(X)>0$인 branch에서는 invertible case가 아니라 root-object case에 놓이고, localized root operator의 convolution input으로 쓰인다.

검증: 논문 예시

## 핵심 관점

Root object의 핵심은 crystal의 simple root 방향을 localized category 안에서 object-level로 다룰 수 있게 만드는 것이다. Crystal graph에서는 $i$-arrow가 combinatorial operation으로 주어지지만, $\widetilde{\mathcal C}_w$에서는 그 방향이 simple object와 head convolution을 통해 표현된다.

따라서 어떤 simple object가 root direction처럼 작동하려면, 단순히 real simple object인 것만으로는 부족하다. Affinization과 R-matrix degree가 서로 맞아야 한다.

정의의 두 조건은 같은 object $L$을 두 방식으로 측정한다. Affinization $(\widehat L,z)$는 $L$을 positive-degree parameter $z$로 들어 올렸을 때의 deformation degree를 준다. 반면 $\mathfrak d(L,\mathscr D^{-1}L)$은 $L$과 duality로 옮긴 object 사이의 R-matrix degree 정보를 기록한다. Root object 조건은 이 두 측정값이 같은 정수 $d_L$로 정렬된다는 요구이다.

이 관점에서 root object는 localized root operator의 입력을 준비하는 중간 개념이다. $\widetilde Q_i$ 같은 localized simple-root object가 등장하지만, 모든 $\widetilde Q_i$가 root object인 것은 아니다. Root object 조건은 어떤 경우에 simple-root object가 실제 root-direction object로 쓰일 수 있는지를 가르는 검증 조건으로 읽어야 한다.

## 기본 성질

### Duality에 대한 안정성

- $L$이 root object이면 $\mathscr D L$과 $\mathscr D^{-1}L$도 root object이다.

### Simple-root objects에 대한 주의

- Simple root index $i$가 $s_iw<w$ 또는 $ws_i<w$를 만족하면 $\widetilde Q_i$는 root object이거나 invertible object이다.
- 일반적으로 $\widetilde Q_i$가 항상 root object라고 말할 수는 없다. $\widetilde Q_i$가 root object도 invertible object도 아닌 경우가 존재한다.

## 다른 topic들과의 관계

- [[topics/08-localization-of-categories/quiver-hecke-category-localization|Quiver-Hecke Category Localization]]은 root object가 사는 ambient category $\widetilde{\mathcal C}_w$를 제공한다. Root object의 정의는 이 localized category 안의 real simple object에서 시작한다.
- [[topics/03-category-theory/affine-objects-in-monoidal-categories|Affine Objects in Monoidal Categories]]는 $(\widehat L,z)$와 $\deg z$를 설명하는 prerequisite이다. Root object의 첫 번째 조건은 $L$이 degree $2d_L$의 affinization을 가져야 한다는 조건이다.
- [[topics/06-quiver-hecke-klr-algebras/r-matrix-renormalization|R-Matrix Renormalization]]은 $\Lambda(-,-)$와 $\mathfrak d(-,-)$의 의미를 제공한다. Root object의 두 번째 조건은 $L$과 $\mathscr D^{-1}L$ 사이의 R-matrix degree invariant를 사용한다.
- [[topics/08-localization-of-categories/localized-root-operators|Localized Root Operators]]는 root object가 쓰이는 다음 단계이다. Root object의 역할은 $\widetilde E_i,\widetilde F_i$를 정의하기 전에 필요한 object-level 조건을 제공하는 데 있고, 실제 operator formula는 localized root operator에서 다룬다.
- [[topics/08-localization-of-categories/localized-crystals|Localized Crystals]]는 이 object-level 조건들이 모여 crystal structure로 해석되는 상위 construction이다. Root object는 그 construction에서 simple root 방향을 category 안의 object와 연결하는 역할을 한다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/03-category-theory/affine-objects-in-monoidal-categories|Affine Objects in Monoidal Categories]], [[topics/06-quiver-hecke-klr-algebras/r-matrix-renormalization|R-Matrix Renormalization]], [[topics/08-localization-of-categories/quiver-hecke-category-localization|Quiver-Hecke Category Localization]]를 먼저 읽는다.
- 상위 개념: [[topics/08-localization-of-categories/quiver-hecke-category-localization|Quiver-Hecke Category Localization]]와 [[topics/03-category-theory/quasi-rigid-monoidal-categories|Quasi-Rigid Monoidal Categories]]가 더 넓은 배경이다.
- 다음에 읽을 것: [[topics/08-localization-of-categories/localized-root-operators|Localized Root Operators]]와 [[topics/08-localization-of-categories/localized-crystals|Localized Crystals]]에서 root object가 operator와 crystal construction에 들어가는 방식을 읽는다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/kashiwara-nakashima25-crystal-structure-localized-quantum-unipotent-coordinate-category|Kashiwara-Nakashima 2025]], Section 5.1-5.2: localized category $\widetilde{\mathcal C}_w$ and its rigidity.
- Kashiwara-Nakashima 2025, Definitions around affine objects and affinizations: the data $(\widehat L,z)$ used in the root-object definition.
- Kashiwara-Nakashima 2025, R-matrix degree definitions: the notation $\Lambda$ and $\mathfrak d$ used in the root-object condition.
- Kashiwara-Nakashima 2025, Section 6.1, Definition labeled `def:rootob`: root object of degree $d_L$.
- Kashiwara-Nakashima 2025, lemmas following the root-object definition: closure under $\mathscr D^{\pm1}$.
- Kashiwara-Nakashima 2025, Proposition 6.5 and the following remark: the conditional statement for $\widetilde Q_i$ and the warning that $\widetilde Q_i$ need not always be root or invertible.
- Kashiwara-Nakashima 2025, lines 3857-3871 and 4576-4585 of `inbox/papers/crystal.tex`: the conditional positive example where $\widetilde Q_i$ is a root object in the $\mathsf d_i(X)>0$ branch.
- Source-location review: `reports/reviews/2026-06-01-root-objects-source-location-review.md`.
- Positive-example review: `reports/reviews/2026-06-01-root-object-positive-example-review.md`.

</details>
