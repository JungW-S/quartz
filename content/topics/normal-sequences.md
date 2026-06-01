---
id: normal-sequences
title: Normal Sequences
level: advanced
topic_kind: concept
parent_topics:
  - r-matrix-renormalization
prerequisite_topics:
  - r-matrix-renormalization
  - affine-objects-in-monoidal-categories
child_topics:
  - head-simplicity-of-convolutions
related_topics:
  - root-objects-in-localized-categories
  - localized-root-operators
maturity: definition-ready
---

## 개요

Normal sequence는 simple objects의 ordered sequence에 대해, 앞쪽 object들을 R-matrix로 하나씩 뒤로 넘겨 전체 순서를 뒤집는 morphism이 0이 되지 않는다는 조건이다. 즉 pairwise R-matrix가 존재하는 것만으로는 충분하지 않고, 그 R-matrix들을 정해진 순서로 합성했을 때 전체 convolution product의 head와 socle을 통제할 수 있어야 한다.

이 개념은 [[topics/r-matrix-renormalization|R-Matrix Renormalization]] 이후에 나타난다. R-matrix degree $\Lambda$와 affreal objects가 있으면, normal sequence 조건은 convolution product의 simple head를 안전하게 다룰 수 있는 상황을 표시한다.

Localized crystal 쪽에서는 $\nabla$로 쓰는 head convolution이 자주 등장한다. Normal sequence는 그런 head convolution이 어느 순서에서 잘 작동하는지를 보장하는 중간 언어이다.

## 준비와 notation

$\mathscr C$를 quasi-rigid monoidal category라고 하자. 이 글에서는 quiver-Hecke module category와 이어지도록 tensor product를 주로
$$
M\circ N
$$
으로 쓴다.

$M,N$이 simple objects일 때, $M\circ N$의 head와 socle을 각각
$$
\operatorname{hd}(M\circ N),
\qquad
\operatorname{soc}(M\circ N)
$$
로 쓴다. Head convolution notation은
$$
M\nabla N:=\operatorname{hd}(M\circ N)
$$
이다.

두 simple objects $M,N$ 사이의 R-matrix와 degree $\Lambda(M,N)$는 [[topics/r-matrix-renormalization|R-Matrix Renormalization]]에서 먼저 읽는다. Pair $(M,N)$이 $\Lambda$-definable이라는 말은 $M\circ N\to N\circ M$ 방향의 R-matrix degree가 well-defined인 상황을 뜻한다.

Affreal object는 [[topics/affine-objects-in-monoidal-categories|Affine Objects in Monoidal Categories]]에서 설명한 affinizations를 가진 real simple object이다. Normal sequence의 주요 정리들은 sequence의 항들 중 대부분이 affreal인 경우에 적용된다.

## 정의

Simple objects의 sequence
$$
(M_1,\ldots,M_r)
$$
가 almost affreal이라는 것은, 많아야 하나의 index를 제외하고 모든 $M_k$가 affreal이라는 뜻이다.

이 sequence가 normal sequence라는 것은 다음 두 조건을 만족한다는 뜻이다.

첫째, 모든 $1\le j<k\le r$에 대해 pair $(M_j,M_k)$가 $\Lambda$-definable이어야 한다. 따라서 각 pair에 대해 R-matrix
$$
r_{M_j,M_k}:M_j\circ M_k\to M_k\circ M_j
$$
를 사용할 수 있다.

둘째, 이 pairwise R-matrix들을 합성해 전체 순서를 뒤집는 morphism
$$
r_{M_1,\ldots,M_r}:
M_1\circ\cdots\circ M_r
\longrightarrow
M_r\circ\cdots\circ M_1
$$
이 0이 아니어야 한다. 이 합성은 $M_1$을 뒤쪽으로 넘기고, 그 다음 $M_2$를 뒤쪽으로 넘기는 식으로 pairwise R-matrix들을 정해진 순서로 합성한 것이다.

## 핵심 관점

Normal sequence는 "ordered convolution product가 하나의 simple head로 정리되는가"를 판단하기 위한 R-matrix condition이다.

$$
M_1\circ\cdots\circ M_r
\xrightarrow{\;r_{M_1,\ldots,M_r}\;}
M_r\circ\cdots\circ M_1
$$

이 morphism이 nonzero이면, R-matrix가 단지 pairwise로 존재하는 데서 끝나지 않고 전체 product의 head/socle 구조까지 연결한다. Almost affreal 조건은 simple head/socle theorem을 적용할 수 있는 realness hypothesis를 제공한다.

따라서 normal sequence는 object-level ordering condition이다. Grothendieck ring에서 보면 product의 leading simple term을 추적하는 장치처럼 보이지만, 실제 정의는 category 안의 R-matrix composition과 그 image에 대한 조건이다.

## 기본 성질

### Head와 socle

Almost affreal normal sequence
$$
(M_1,\ldots,M_r)
$$
에 대해, composed R-matrix의 image
$$
\operatorname{Im}(r_{M_1,\ldots,M_r})
$$
는 simple object이다. 이 object는 $M_1\circ\cdots\circ M_r$의 head와 isomorphic이고, 동시에 reversed product $M_r\circ\cdots\circ M_1$의 socle과 isomorphic이다.

### Real simple factor가 주는 배경

Quiver-Hecke algebra setting에서 $M$이 real simple이고 $N$이 simple이면, $M\circ N$과 $N\circ M$은 simple head와 simple socle을 가진다. 또한 renormalized R-matrix의 image가 그 head/socle을 식별한다.

이 사실은 normal sequence에서 head convolution이 왜 핵심 notation이 되는지를 설명한다. Normal sequence는 이 pair-level head/socle behavior를 여러 항의 ordered product로 확장해서 쓰는 방식이다.

### Normality를 확인하는 기준

Normality는 정의를 그대로 확인할 수도 있지만, 실제 계산에서는 다음 recognition criteria가 자주 쓰인다.

- 첫 항 $L_1$이 affreal이면, $(L_1,\ldots,L_r)$의 normality는 tail sequence $(L_2,\ldots,L_r)$의 normality와
  $$
  \Lambda(L_1,\operatorname{hd}(L_2\circ\cdots\circ L_r))
  =
  \sum_{2\le j\le r}\Lambda(L_1,L_j)
  $$
  라는 degree equality로 검사할 수 있다.
- 마지막 항 $L_r$이 affreal이면, 앞쪽 sequence $(L_1,\ldots,L_{r-1})$와 analogous degree equality로 검사한다.
- Rigid category에서는 triple $(L,M,N)$의 normality가 $(M,N,\mathscr D L)$의 normality와 연결된다.
- Quiver-Hecke module category에서 almost affreal triple $(L,M,N)$에 대해 $\widetilde\Lambda(L,N)=0$이고 $L$ 또는 $N$ 중 하나가 affreal이면, 이 triple은 normal sequence이다.

## 다른 topic들과의 관계

- [[topics/r-matrix-renormalization|R-Matrix Renormalization]]은 $\Lambda$-definable pair, R-matrix degree, $\widetilde\Lambda$ notation을 제공한다.
- [[topics/affine-objects-in-monoidal-categories|Affine Objects in Monoidal Categories]]는 affreal object의 의미를 제공한다.
- [[topics/quiver-hecke-module-categories|Quiver-Hecke Module Categories]]는 convolution product $\circ$와 simple module setting을 제공한다.
- [[topics/head-simplicity-of-convolutions|Head Simplicity of Convolutions]]는 normal sequence 이후에 읽을 theorem-level topic이다.
- [[topics/root-objects-in-localized-categories|Root Objects in Localized Categories]]와 [[topics/localized-root-operators|Localized Root Operators]]는 head convolution과 normal sequence criteria를 localized crystal construction 안에서 사용한다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/r-matrix-renormalization|R-Matrix Renormalization]]에서 $\Lambda$와 R-matrix degree를 읽고, [[topics/affine-objects-in-monoidal-categories|Affine Objects in Monoidal Categories]]에서 affreal object를 읽는다.
- 상위 개념: [[topics/r-matrix-renormalization|R-Matrix Renormalization]]이 normality condition의 degree language를 제공한다.
- 다음에 읽을 것: [[topics/head-simplicity-of-convolutions|Head Simplicity of Convolutions]]에서 simple head theorem을 읽고, [[topics/localized-root-operators|Localized Root Operators]]에서 $\nabla$가 crystal operator formulas에 들어가는 방식을 읽는다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/kashiwara-nakashima25-crystal-structure-localized-quantum-unipotent-coordinate-category|Kashiwara-Nakashima 2025]], Definition 4.8, pp.23-24: almost affreal sequence and normal sequence.
- Kashiwara-Nakashima 2025, Lemma 4.9, p.24: image of the composed R-matrix as simple head and reversed simple socle.
- Kashiwara-Nakashima 2025, Lemmas 4.10-4.11 and Proposition 4.12, pp.24-25: recognition criteria for normal sequences.
- [[sources/papers/kkko15-simplicity-heads-socles-tensor-products|KKKO15]], Theorem 3.2, pp.385-386: simple head/socle behavior for convolution with a real simple factor.

</details>
