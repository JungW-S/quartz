---
id: type-a-segment-module-convolutions
title: Type A Segment Module Convolutions
level: advanced
topic_kind: theorem
parent_topics:
  - type-a-klr-segment-modules
prerequisite_topics:
  - quiver-hecke-module-categories
  - type-a-klr-segment-modules
  - r-matrix-renormalization
child_topics: []
related_topics:
  - head-simplicity-of-convolutions
  - quantum-affine-schur-weyl-duality
maturity: example-ready
---

## 개요

Type $A$ segment module convolution은 type $A_\infty$ quiver-Hecke category에서 두 segment modules
$$
L(a,b),\qquad L(a',b')
$$
의 convolution product가 두 intervals $[a,b]$, $[a',b']$의 상대 위치에 따라 어떻게 달라지는지를 설명한다. 여기서 핵심은 module $L(a,b)$의 정의가 아니라, 두 modules를 곱했을 때 R-matrix map, irreducibility, exact sequence, head와 socle이 어떻게 나타나는가이다.

이 topic은 [[topics/06-quiver-hecke-klr-algebras/type-a-klr-segment-modules|Type A KLR Segment Modules]] 다음에 온다. Segment module 하나와 ordered multisegment의 기본 언어를 알고 나면, 그 다음 질문은 product
$$
L(a,b)\circ L(a',b')
$$
가 단순한지, 아니라면 어떤 head와 socle을 갖는지이다.

## 준비와 notation

$J=\mathbb Z$인 type $A_\infty$ KLR setting에서 segment $(a,b)$는 $a\le b$인 정수쌍이다. Segment module은
$$
L(a,b)\in R(\epsilon_a-\epsilon_{b+1})\text{-gmod}
$$
로 쓴다.

두 segments $(a,b)$, $(a',b')$에 대해 length와 positive root를
$$
\ell=b-a+1,\qquad \ell'=b'-a'+1,
$$
$$
\beta=\epsilon_a-\epsilon_{b+1},\qquad
\beta'=\epsilon_{a'}-\epsilon_{b'+1}
$$
로 둔다. 두 intervals의 교집합 크기는
$$
p=\#([a,b]\cap[a',b'])
=\max(0,\min(b,b')-\max(a,a')+1)
$$
이다.

Convolution product는
$$
L(a,b)\circ L(a',b')
$$
로 쓴다. 아래에서는 $L(a,b)$를 첫 번째 factor, $L(a',b')$를 두 번째 factor라고 부른다. 따라서 "왼쪽", "오른쪽", "안에 들어간다"는 말은 integer line 위의 intervals $[a,b]$, $[a',b']$의 위치를 가리키고, convolution product의 factor 순서를 가리키지 않는다.

두 factor의 순서를 바꾸는 renormalized R-matrix map은
$$
r_{L(a,b),L(a',b')}:
L(a,b)\circ L(a',b')
\to
L(a',b')\circ L(a,b)
$$
로 쓴다. KKK18A Proposition 4.2.3은 이 map과 convolution product의 구조를 intervals의 상대 위치별로 정리한다.

## 정리의 진술

KKK18A Proposition 4.2.3의 내용은 다음과 같이 읽을 수 있다.

두 segments $(a,b)$와 $(a',b')$가 주어졌다고 하자. Spectral-parameter R-matrix의 zero order를 $s$라고 한다.

### 같은 segment

$(a',b')=(a,b)$이면
$$
s=b-a
$$
이고 renormalized self R-matrix는 identity이다.
$$
r_{L(a,b),L(a,b)}
=
\operatorname{id}_{L(a,b)\circ L(a,b)}.
$$

### Nested case: 두 번째 interval이 안에 들어가는 경우

만약
$$
a\le a'\le b'\le b
$$
이면 convolution product는 irreducible이고, 순서를 바꾼 convolution product와 grading shift를 제외하고 isomorphic이다.
$$
L(a,b)\circ L(a',b')
\simeq
q^{\delta_{a,a'}-\delta_{b,b'}}
L(a',b')\circ L(a,b).
$$

### Right-overlap case: 두 번째 interval이 오른쪽으로 걸쳐 나가는 경우

만약
$$
a\le a'\le b\le b'
$$
이면 zero order는
$$
s=b-a'
$$
이고, nonzero R-matrix homomorphism
$$
f:
L(a,b)\circ L(a',b')
\to
q^{\delta_{a,a'}+\delta_{b,b'}-2}
L(a',b')\circ L(a,b)
$$
이 존재한다.

### Separated case: 두 번째 interval이 왼쪽에 떨어진 경우

만약
$$
b'<a-1
$$
이면 이 순서의 convolution product는 irreducible이고, R-matrix map은 isomorphism이다.
$$
L(a,b)\circ L(a',b')
\xrightarrow{\sim}
L(a',b')\circ L(a,b).
$$

### Crossing case: 겹치지만 어느 한쪽이 포함되지 않는 경우

만약
$$
a'<a\le b'<b
$$
이면 다음 exact sequence가 있다.
$$
0
\to
qL(a',b)\circ L(a,b')
\to
L(a,b)\circ L(a',b')
\xrightarrow{\;g\;}
L(a',b')\circ L(a,b)
\to
q^{-1}L(a',b)\circ L(a,b')
\to
0.
$$
또한 $\operatorname{Im}(g)$는 $L(a,b)\circ L(a',b')$의 head이고, 동시에 $L(a',b')\circ L(a,b)$의 socle이다.

### Adjacent case: 두 intervals가 서로 맞닿는 경우

만약
$$
a=b'+1
$$
이면 다음 exact sequence가 있다.
$$
0
\to
qL(a',b)
\to
L(a,b)\circ L(a',b')
\xrightarrow{\;g\;}
q^{-1}L(a',b')\circ L(a,b)
\to
q^{-1}L(a',b)
\to
0.
$$
이 경우에도 $\operatorname{Im}(g)$는 앞쪽 convolution product의 head이고, shifted reversed product의 socle이다.

### R-matrix degree invariant

같은 proposition은
$$
d(L(a,b),L(a',b'))
=
(\beta,\beta')
-2\delta(a\le a'\le b\le b')
$$
도 기록한다. 여기서 $\delta(\cdots)$는 조건이 참이면 $1$, 거짓이면 $0$이다.

## 기본 예시

### 실제 예시: adjacent family

$a\le b$이고 $b-a+1\ge2$라고 하자. 두 segment modules
$$
L(b),\qquad L(a,b-1)
$$
를 보자. 이때 integer line 위의 intervals는
$$
[b,b],\qquad [a,b-1]
$$
이고, 두 intervals는 끝점에서 바로 맞닿는다. 따라서 이 pair는 adjacent case이다.

Proposition 4.2.3(vi)를 이 pair에 적용하면 다음 exact sequence가 나온다.
$$
0
\to
qL(a,b)
\to
L(b)\circ L(a,b-1)
\to
q^{-1}L(a,b-1)\circ L(b)
\to
q^{-1}L(a,b)
\to
0.
$$

이 예시에서 볼 것은 adjacent라는 위치 관계가 product를 단순한 commutation 문제로 만들지 않는다는 점이다. 두 factors의 순서를 바꾸는 map 주위에 exact sequence가 놓이고, 그 exact sequence의 양끝에는 더 긴 segment module $L(a,b)$가 나타난다.

따라서 adjacent case는 두 intervals의 위치가 convolution product의 구조를 바꾼다는 가장 작은 예시로 읽을 수 있다. KKK18A는 Proposition 4.3.1의 proof에서 같은 adjacent family를 사용하며, 그 proof에서는 grading을 생략한 형태의 exact sequence를 쓴다.

검증: KKK18A Proposition 4.2.3(vi) 및 Proposition 4.3.1의 proof에서 사용된 adjacent family.

## 핵심 관점

위 예시를 일반화하면 핵심 그림은 다음과 같다. 두 intervals를 integer line 위에 놓고, 그 위치 관계를 convolution product의 category-level behavior로 읽는다. 이 위치 관계는 단순성, R-matrix map, exact sequence라는 세 종류의 정보를 구분한다.

첫째, nested case와 separated case에서는 위 정리에 명시된 convolution product가 irreducible하다. 이 경우에는 두 segment modules를 곱해도 head와 socle을 따로 추적할 필요가 거의 없다.

둘째, right-overlap case에서는 spectral-parameter R-matrix의 zero order와 nonzero R-matrix homomorphism을 추적해야 한다. 이 정보는 단순히 "두 factors를 바꾸어도 같다"는 말보다 더 세밀하다.

셋째, crossing case와 adjacent case에서는 exact sequence가 나타난다. 이때 R-matrix map의 image가 한쪽 convolution product의 head와 반대쪽 product의 socle을 동시에 잡는다.

따라서 이 topic은 object-level segment module에서 category-level convolution behavior로 넘어가는 중간 단계이다. Ordered multisegment classification에서 simple module이
$$
\operatorname{hd}\bigl(L(a_1,b_1)\circ\cdots\circ L(a_t,b_t)\bigr)
$$
로 나타나는 이유를 이해하려면, 먼저 두 segment factors의 product가 어떻게 행동하는지 알아야 한다.

## 기본 성질

### Two-segment case에서 ordered multisegment classification으로

Proposition 4.2.3은 두 segment factors에 대한 case analysis이다. Proposition 4.2.5는 ordered multisegment
$$
(a_1,b_1)\ge\cdots\ge(a_t,b_t)
$$
에 대해 simple module이 ordered convolution product의 head로 얻어진다고 말한다. 따라서 Proposition 4.2.3은 ordered multisegment classification을 읽기 위한 local two-factor mechanism이다.

### Ordered convolution의 head와 reversed convolution의 socle

KKK18A Lemma 4.2.6은 ordered multisegment
$$
(a_1,b_1),\ldots,(a_t,b_t)
$$
에 대해
$$
L=L(a_1,b_1)\circ\cdots\circ L(a_t,b_t),
$$
$$
L'=L(a_t,b_t)\circ\cdots\circ L(a_1,b_1)
$$
를 놓고 head와 socle을 비교한다. 적절한 degree $d$에 대해
$$
\operatorname{hd}(L)\simeq q^d\operatorname{soc}(L')
$$
이고, nonzero homomorphism $L\to q^sL'$의 image는 적절한 shift에서 이 head/socle object와 일치한다.

이 lemma는 two-segment behavior가 ordered multisegment 전체의 head/socle statement로 이어진다는 점을 보여 준다.

## 다른 topic들과의 관계

- [[topics/06-quiver-hecke-klr-algebras/type-a-klr-segment-modules|Type A KLR Segment Modules]]는 $L(a,b)$, ordered multisegments, 그리고 $F(L(a,b))$의 기본 Schur-Weyl image를 제공한다.
- [[topics/06-quiver-hecke-klr-algebras/quiver-hecke-module-categories|Quiver-Hecke Module Categories]]는 convolution product $\circ$, head, socle이 사는 category-level 배경이다.
- [[topics/06-quiver-hecke-klr-algebras/r-matrix-renormalization|R-Matrix Renormalization]]은 $r_{M,N}$와 R-matrix degree를 일반적으로 설명한다.
- [[topics/06-quiver-hecke-klr-algebras/head-simplicity-of-convolutions|Head Simplicity of Convolutions]]는 더 일반적인 head/socle theorem이다. 이 topic은 type $A$ segment modules라는 구체적인 family에서 그런 현상이 어떻게 나타나는지 보여 주는 특수한 case이다.
- [[topics/07-quantum-affine-algebras/quantum-affine-schur-weyl-duality|Quantum Affine Schur-Weyl Duality]]는 single segment modules의 functor image를 이미 사용한다. Multiple segment products를 더 깊게 쓰려면 이 convolution topic이 필요해진다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/06-quiver-hecke-klr-algebras/type-a-klr-segment-modules|Type A KLR Segment Modules]]에서 $L(a,b)$와 ordered multisegment를 읽고, [[topics/06-quiver-hecke-klr-algebras/r-matrix-renormalization|R-Matrix Renormalization]]에서 R-matrix notation을 읽는다.
- 상위 개념: [[topics/06-quiver-hecke-klr-algebras/type-a-klr-segment-modules|Type A KLR Segment Modules]].
- 다음에 읽을 것: [[topics/06-quiver-hecke-klr-algebras/head-simplicity-of-convolutions|Head Simplicity of Convolutions]]에서 R-matrix image가 head와 socle을 잡는 일반 theorem을 읽는다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/kang-kashiwara-kim18-symmetric-quiver-hecke-algebras-r-matrices|Kang-Kashiwara-Kim 2018]], Proposition 4.2.3, arXiv PDF pp.37-39: R-matrix and convolution behavior for two segment modules, including irreducibility cases, exact sequences, and the invariant $d(L(a,b),L(a',b'))$.
- Kang-Kashiwara-Kim 2018, Proposition 4.3.1 proof, arXiv PDF pp.43-44: uses the adjacent-family exact sequence for $L(b)\circ L(a,b-1)$ and $L(a,b-1)\circ L(b)$, with grading omitted in the proof.
- Kang-Kashiwara-Kim 2018, Lemma 4.2.6, arXiv PDF pp.39-41: head/socle comparison for ordered convolution products of segment modules.
- Topic-scope review: `reports/reviews/2026-06-03-type-a-segment-module-convolutions-topic-scope-review.md`.
- Example review: `reports/reviews/2026-06-03-direct-type-a-segment-example-review.md`.

</details>
