---
id: abstract-crystals
title: Abstract Crystals
level: core
topic_kind: concept
parent_topics:
  - crystal-bases
prerequisite_topics:
  - crystal-bases
  - root-systems-and-weight-lattices
child_topics: []
related_topics:
  - tensor-products-of-crystals
maturity: example-ready
---

## 개요

Abstract crystal은 set $B$ 위에 weight, root operators, 그리고 각 simple-root direction에서의 string 길이를 기록하는 maps를 둔 combinatorial structure이다. 이 structure는 [[topics/01-quantum-groups/quantum-groups|quantum group]] representation에서 생기는 crystal base의 $q=0$ 정보를 구체적인 module을 직접 들고 오지 않고 다루기 위해 쓰인다.

Abstract crystal은 basis 자체도 아니고 module category도 아니다. 수학적 level로는 crystal-level object이며, 원소 $b\in B$를 vertex로 보고 root operator $\widetilde f_i$를 colored arrow로 그리면 crystal graph가 된다.

이 언어가 필요한 이유는 서로 다른 construction에서 나온 combinatorial objects를 같은 규칙으로 비교하기 위해서이다. 예를 들어 [[topics/02-crystal-bases/cellular-crystals|Cellular Crystals]]와 [[topics/08-localization-of-categories/localized-crystals|Localized Crystals]]는 모두 abstract crystal의 언어를 사용한다.

## 준비와 notation

$I$를 simple roots의 index set이라고 하자. 각 $i\in I$에 대해 simple root를 $\alpha_i$, simple coroot를 $h_i$라고 쓰고, $P$를 weight lattice라고 쓴다. Pairing은
$$
\langle h_i,\lambda\rangle
$$
처럼 쓴다.

Abstract crystal의 underlying set을 $B$라고 쓴다. $B$의 원소는 보통 $b,b'$로 쓴다. 각 $b\in B$에는 다음 data가 붙는다.

- weight:
  $$
  \operatorname{wt}(b)\in P
  $$
- string functions:
  $$
  \varepsilon_i(b),\varphi_i(b)\in\mathbb Z\cup\{-\infty\}
  $$
- root operators:
  $$
  \widetilde e_i,\widetilde f_i:B\to B\cup\{0\}.
  $$

여기서 $0$은 $B$의 원소가 아니라 operator가 더 이상 적용되지 않을 때 쓰는 formal symbol이다. 따라서 $\widetilde e_i b=0$은 $b$가 $i$-direction으로 더 올라가지 못한다는 뜻이지, $0\in B$라는 뜻이 아니다.

## 정의

Abstract crystal은 set $B$와 maps
$$
\operatorname{wt}:B\to P,
\qquad
\varepsilon_i,\varphi_i:B\to\mathbb Z\cup\{-\infty\},
$$
$$
\widetilde e_i,\widetilde f_i:B\to B\cup\{0\}
\qquad (i\in I)
$$
로 이루어진 data이다. 이 data는 모든 $i\in I$와 $b,b'\in B$에 대해 다음 조건을 만족해야 한다.

1. Weight와 string functions는
   $$
   \varphi_i(b)=\varepsilon_i(b)+\langle h_i,\operatorname{wt}(b)\rangle
   $$
   로 연결된다.

2. $\widetilde e_i b\in B$이면
   $$
   \operatorname{wt}(\widetilde e_i b)=\operatorname{wt}(b)+\alpha_i,
   $$
   $$
   \varepsilon_i(\widetilde e_i b)=\varepsilon_i(b)-1,
   \qquad
   \varphi_i(\widetilde e_i b)=\varphi_i(b)+1.
   $$

3. $\widetilde f_i b\in B$이면
   $$
   \operatorname{wt}(\widetilde f_i b)=\operatorname{wt}(b)-\alpha_i,
   $$
   $$
   \varepsilon_i(\widetilde f_i b)=\varepsilon_i(b)+1,
   \qquad
   \varphi_i(\widetilde f_i b)=\varphi_i(b)-1.
   $$

4. Root operators는 서로 inverse 관계를 가진다.
   $$
   \widetilde e_i b=b'
   \quad\Longleftrightarrow\quad
   b=\widetilde f_i b'.
   $$

5. $\varphi_i(b)=-\infty$이면
   $$
   \widetilde e_i b=\widetilde f_i b=0.
   $$

이 다섯 조건이 abstract crystal의 정의이다. Graph로 볼 때는 $\widetilde f_i b=b'$인 경우에 색 $i$의 arrow
$$
b\xrightarrow{\ i\ }b'
$$
를 그린다.

## 기본 예시

### 실제 예시: one-element crystal

$\lambda\in P$에 대해 $T_\lambda$는 원소 하나 $t_\lambda$만 갖는 crystal이다. 이 crystal에서는
$$
\operatorname{wt}(t_\lambda)=\lambda,
\qquad
\varepsilon_i(t_\lambda)=\varphi_i(t_\lambda)=-\infty,
$$
$$
\widetilde e_i t_\lambda=\widetilde f_i t_\lambda=0
$$
이다. 즉 graph로 보면 vertex 하나만 있고 arrow는 없다.

검증: 논문 예시

### 실제 예시: elementary crystal $B_i$

하나의 simple root direction $i$를 고정한다. Kashiwara의 elementary crystal $B_i$는
$$
B_i=\{b_i(n)\mid n\in\mathbb Z\}
$$
로 주어진다. 이때
$$
\operatorname{wt}(b_i(n))=n\alpha_i,
\qquad
\varphi_i(b_i(n))=n,
\qquad
\varepsilon_i(b_i(n))=-n,
$$
이고 $j\ne i$에 대해서는
$$
\varepsilon_j(b_i(n))=\varphi_j(b_i(n))=-\infty.
$$
Root operators는
$$
\widetilde e_i b_i(n)=b_i(n+1),
\qquad
\widetilde f_i b_i(n)=b_i(n-1),
$$
이며 $j\ne i$이면
$$
\widetilde e_j b_i(n)=\widetilde f_j b_i(n)=0.
$$

따라서 $B_i$는 $i$-colored arrows만 가진, 양쪽으로 무한히 이어지는 line이다. Arrow의 방향은 $\widetilde f_i$가 $n$을 $n-1$로 보내는 방향이다.
$$
\cdots
\xrightarrow{\ i\ }
b_i(1)
\xrightarrow{\ i\ }
b_i(0)
\xrightarrow{\ i\ }
b_i(-1)
\xrightarrow{\ i\ }
\cdots
$$

검증: 논문 예시

## 핵심 관점

Abstract crystal을 읽을 때는 각 $i\in I$에 대해 $\widetilde e_i$와 $\widetilde f_i$가 만드는 $i$-string을 먼저 본다. $\widetilde e_i$는 weight를 $\alpha_i$만큼 올리고, $\widetilde f_i$는 weight를 $\alpha_i$만큼 내린다.

String functions는 이 string에서 원소 $b$의 위치를 수치로 기록한다. Normal crystal에서는 $\varepsilon_i(b)$가 $\widetilde e_i$를 몇 번 적용할 수 있는지, $\varphi_i(b)$가 $\widetilde f_i$를 몇 번 적용할 수 있는지를 그대로 센다.

이 관점에서 crystal graph는 단순한 그림이 아니다. Vertex는 crystal elements이고, arrow는 root operator의 작용이며, weight는 vertex가 weight lattice 안에서 어디에 놓이는지를 기록한다.

## 기본 성질

### 정의: morphism

Crystal morphism은 한 crystal에서 다른 crystal로 가는 map이다. 값이 실제 crystal element일 때는 weight, $\varepsilon_i$, $\varphi_i$를 보존하고 root operators와 호환된다. Strict morphism은 모든 $\widetilde e_i,\widetilde f_i$와 commute하는 morphism이다.

### 정의: normality

Crystal $B$가 upper normal이라는 것은 $\varepsilon_i(b)$가 $\widetilde e_i$를 최대로 적용할 수 있는 횟수를 기록한다는 뜻이다. Lower normal이라는 것은 $\varphi_i(b)$가 $\widetilde f_i$를 최대로 적용할 수 있는 횟수를 기록한다는 뜻이다. 둘 다 만족하면 normal crystal이라고 한다.

### 구조: category와 direct sum

Crystals는 morphisms와 함께 category를 이룬다. Kashiwara는 또한 direct sum of crystals를 정의한다. Tensor product도 정의되지만, tensor product rule은 별도의 topic인 [[topics/02-crystal-bases/tensor-products-of-crystals|Tensor Products of Crystals]]에서 다룬다.

## 다른 topic들과의 관계

**Crystal Bases.** [[topics/02-crystal-bases/crystal-bases|Crystal Bases]]는 abstract crystal이 representation theory에서 왜 나오는지 설명하는 상위 topic이다. Abstract crystal은 그 안에서 쓰이는 combinatorial language만 떼어낸 것이다.

**Root Systems and Weight Lattices.** [[topics/01-quantum-groups/root-systems-and-weight-lattices|Root Systems and Weight Lattices]]는 $\alpha_i$, $h_i$, $P$, 그리고 pairing notation을 제공한다.

**Tensor Products of Crystals.** [[topics/02-crystal-bases/tensor-products-of-crystals|Tensor Products of Crystals]]는 두 abstract crystals를 합쳐 새 crystal을 만드는 rule을 다룬다. 이 rule은 Kashiwara convention을 따라야 하므로 별도로 고정한다.

**Cellular and localized crystals.** [[topics/02-crystal-bases/cellular-crystals|Cellular Crystals]]와 [[topics/08-localization-of-categories/localized-crystals|Localized Crystals]]는 더 advanced한 constructions이지만, 둘 다 abstract crystal axioms와 morphism language를 사용한다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/01-quantum-groups/root-systems-and-weight-lattices|Root Systems and Weight Lattices]]에서 root와 weight notation을 읽는다.
- 상위 개념: [[topics/02-crystal-bases/crystal-bases|Crystal Bases]]는 abstract crystal이 quantum group representation에서 어떻게 나오는지 설명한다.
- 다음에 읽을 것: [[topics/02-crystal-bases/tensor-products-of-crystals|Tensor Products of Crystals]]에서 tensor product rule을 읽고, 그 다음 [[topics/02-crystal-bases/highest-weight-crystals|Highest Weight Crystals]]와 [[topics/02-crystal-bases/b-infinity-crystal|The Crystal B(infinity)]]로 넘어간다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/kashiwara93-crystal-base-demazure-character-formula|Kashiwara 1993]], Definition 1.2.1, pp.841-842: abstract crystal definition and axioms.
- Kashiwara 1993, Section 1.2, p.842: morphisms, strict morphisms, normality, and direct sums.
- Kashiwara 1993, Examples 1.2.4 and 1.2.6, p.842: the one-element crystal $T_\lambda$ and elementary crystal $B_i$.

</details>
