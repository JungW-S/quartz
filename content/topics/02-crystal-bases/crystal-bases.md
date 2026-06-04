---
id: crystal-bases
title: Crystal Bases
level: core
topic_kind: basis
parent_topics:
  - quantum-groups
prerequisite_topics:
  - root-systems-and-weight-lattices
  - quantum-groups
child_topics:
  - abstract-crystals
  - tensor-products-of-crystals
  - highest-weight-crystals
  - b-infinity-crystal
  - demazure-crystals
  - string-parametrizations-of-demazure-crystals
  - cellular-crystals
related_topics:
  - dual-canonical-bases
  - localized-crystals
maturity: study-ready
---

## 개요

Crystal은 set $B$ 위에 weight map, root operators, 그리고 각 simple root direction의 길이 정보를 둔 combinatorial structure이다. Crystal base theory에서는 quantum group representation의 basis-level 정보를 $q=0$의 combinatorial shadow로 남기며, 그 shadow를 vertex와 colored arrows로 그리면 crystal graph로 볼 수 있다.

Crystal language는 representation-theoretic data를 colored graph로 바꾸기 위해 나타난다. 이 language는 [[topics/02-crystal-bases/cellular-crystals|Cellular Crystals]]와 [[topics/08-localization-of-categories/localized-crystals|Localized Crystals]]처럼 서로 다른 constructions를 같은 crystal-level object로 비교할 때 사용된다.

## 준비와 notation

$I$를 simple roots의 index set이라고 하자. 각 $i\in I$에 대해 simple root를 $\alpha_i$, simple coroot를 $h_i$라고 쓰고, $P$를 weight lattice라고 쓴다.

Root-system notation과 weight-lattice notation은 [[topics/01-quantum-groups/root-systems-and-weight-lattices|Root Systems and Weight Lattices]]에서 정리한다. $q=0$ 그림의 quantum-group origin은 [[topics/01-quantum-groups/quantum-groups|Quantum Groups]]에서 정리한다.

Crystal $B$의 원소 $b$에는 다음 data가 붙는다.

- weight: $\operatorname{wt}(b)\in P$
- 길이 함수: $\varepsilon_i(b),\varphi_i(b)\in\mathbb Z\cup\{-\infty\}$
- root operators:
  $$
  \widetilde e_i,\widetilde f_i:B\to B\cup\{0\}
  $$

여기서 $0$은 $B$의 원소가 아니라 operator가 더 이상 적용되지 않을 때 쓰는 formal symbol이다.

여기서 쓰는 tensor product는 Kashiwara convention을 따른다. 일부 combinatorics texts와 SageMath는 opposite tensor convention을 쓰므로, 그쪽 formulas를 비교할 때는 convention을 먼저 변환해야 한다.

## 정의

Crystal은 set $B$와, 각 $i\in I$에 대해 주어진 maps
$$
\operatorname{wt}:B\to P,\qquad
\varepsilon_i,\varphi_i:B\to\mathbb Z\cup\{-\infty\},
$$
$$
\widetilde e_i,\widetilde f_i:B\to B\cup\{0\}
$$
로 이루어진 data이다. 여기서 $0$은 $B$의 원소가 아닌 formal symbol이다. 이 data는 모든 $b,b'\in B$와 $i\in I$에 대해 다음 조건을 만족해야 한다.

- Weight, $\varepsilon_i$, $\varphi_i$는
$$
\varphi_i(b)=\varepsilon_i(b)+\langle h_i,\operatorname{wt}(b)\rangle
$$
로 연결된다.
- $\widetilde e_i b\in B$이면
$$
\operatorname{wt}(\widetilde e_i b)=\operatorname{wt}(b)+\alpha_i,
\qquad
\varepsilon_i(\widetilde e_i b)=\varepsilon_i(b)-1,
\qquad
\varphi_i(\widetilde e_i b)=\varphi_i(b)+1.
$$
- $\widetilde f_i b\in B$이면
$$
\operatorname{wt}(\widetilde f_i b)=\operatorname{wt}(b)-\alpha_i,
\qquad
\varepsilon_i(\widetilde f_i b)=\varepsilon_i(b)+1,
\qquad
\varphi_i(\widetilde f_i b)=\varphi_i(b)-1.
$$
- Root operators는 서로 inverse 조건을 만족한다.
$$
\widetilde f_i b=b'
\quad\Longleftrightarrow\quad
b=\widetilde e_i b'.
$$
- $\varphi_i(b)=-\infty$이면
$$
\widetilde e_i b=\widetilde f_i b=0.
$$

Root operators를 $B\cup\{0\}$까지 확장해서 쓸 때는 $\widetilde e_i0=\widetilde f_i0=0$으로 둔다.

이 조건들이 abstract crystal을 결정한다. Crystal graph는 $\widetilde f_i b=b'$일 때 $b\xrightarrow{\ i\ } b'$라는 colored arrow를 그려 얻는다.

## 기본 예시

### 실제 예시

$T_\lambda$는 하나의 원소 $t_\lambda$만 갖는 crystal이다. 이 원소의 weight는 $\lambda$이고, 모든 root operator는 $0$을 준다.

Elementary crystal $B_i$는
$$
B_i=\{b_i(n)\mid n\in\mathbb Z\}
$$
로 주어진다. 이 notation에서
$$
\operatorname{wt}(b_i(n))=n\alpha_i,\qquad
\widetilde e_i b_i(n)=b_i(n+1),\qquad
\widetilde f_i b_i(n)=b_i(n-1).
$$
따라서 $i$-direction만 보면 $B_i$는 양쪽으로 끝없이 이어지는 colored line이다.

검증: 논문 예시

Highest weight representation에서 나오는 finite string example은 [[topics/02-crystal-bases/highest-weight-crystals|Highest Weight Crystals]]에서 다룬다.

## 핵심 관점

Crystal graph는 원소 $b\in B$를 vertex로 그리고, $\widetilde f_i b=b'$일 때 색 $i$의 arrow를
$$
b\xrightarrow{\ i\ } b'
$$
로 그리는 해석이다. Operator $\widetilde e_i$는 같은 arrow를 거꾸로 따라가는 역할을 한다.

한 fixed $i$에 대해서 graph를 보면 $i$-colored string들이 나타난다. 이런 string 안에서 $\varepsilon_i(b)$는 위쪽으로 얼마나 올라갈 수 있는지, $\varphi_i(b)$는 아래쪽으로 얼마나 내려갈 수 있는지를 측정하는 함수로 읽을 수 있다.

## 기본 성질

### 구조

- Crystals는 category를 이룬다. Morphism은 weight, $\varepsilon_i$, $\varphi_i$를 보존하고, image가 정의되는 곳에서는 root operators와 호환된다.
- Crystals에는 direct sum과 tensor product가 있다. Tensor product $B_1\otimes B_2$에는 $\operatorname{wt}$, $\varepsilon_i$, $\varphi_i$, $\widetilde e_i$, $\widetilde f_i$에 대한 explicit formulas가 있고, tensor product는 associative이다.

### 해석

- Normal crystal에서는 $\varepsilon_i(b)$와 $\varphi_i(b)$가 $\widetilde e_i$와 $\widetilde f_i$를 최대 몇 번 적용할 수 있는지를 기록한다.
- Dominant weight $\lambda$에 대해 $B(\lambda)$는 highest weight $\lambda$를 갖는 simple highest-weight module의 crystal base에서 얻는 normal crystal이다.

## 다른 topic들과의 관계

**Quantum groups.** [[topics/01-quantum-groups/quantum-groups|Quantum Groups]]는 crystal bases의 representation-theoretic source를 제공한다. Crystal graph arrows는 임의의 graph data가 아니라, $q=0$에 남는 raising/lowering structure에서 온다.

**Root systems and weight lattices.** [[topics/01-quantum-groups/root-systems-and-weight-lattices|Root Systems and Weight Lattices]]는 $\operatorname{wt}$, $\varepsilon_i$, $\varphi_i$ 뒤에 있는 root, coroot, weight-lattice notation을 제공한다.

**Abstract crystals and tensor products.** [[topics/02-crystal-bases/abstract-crystals|Abstract Crystals]]는 crystal axioms와 graph language를 전용 prerequisite로 정리한다. [[topics/02-crystal-bases/tensor-products-of-crystals|Tensor Products of Crystals]]는 여러 crystal factors를 합치는 rule을 별도로 다룬다.

**Coordinate and localized crystals.** [[topics/02-crystal-bases/string-parametrizations-of-demazure-crystals|String Parametrizations of Demazure Crystals]]는 Demazure-type crystal을 reduced-expression coordinate로 읽는 중간층이다. [[topics/02-crystal-bases/cellular-crystals|Cellular Crystals]]는 elementary crystals의 tensor products를 사용한다. [[topics/08-localization-of-categories/localized-crystals|Localized Crystals]]는 localized monoidal category의 simple objects 위에 crystal operators를 만든다.

**Dual canonical bases.** [[topics/01-quantum-groups/dual-canonical-bases|Dual Canonical Bases]]는 [[topics/01-quantum-groups/quantum-coordinate-rings|Quantum Coordinate Rings]] 근처의 또 다른 basis-level structure이다. Crystal bases는 이 basis language의 combinatorial side를 제공한다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/01-quantum-groups/root-systems-and-weight-lattices|Root Systems and Weight Lattices]]; [[topics/01-quantum-groups/quantum-groups|Quantum Groups]].
- 상위 개념: [[topics/01-quantum-groups/quantum-groups|Quantum Groups]]는 crystal bases의 representation-theoretic source를 설명한다.
- 다음에 읽을 것: [[topics/02-crystal-bases/abstract-crystals|Abstract Crystals]]에서 axioms를 정리하고, [[topics/02-crystal-bases/tensor-products-of-crystals|Tensor Products of Crystals]]에서 tensor rule을 읽은 뒤, [[topics/02-crystal-bases/string-parametrizations-of-demazure-crystals|String Parametrizations of Demazure Crystals]], [[topics/02-crystal-bases/cellular-crystals|Cellular Crystals]], [[topics/08-localization-of-categories/localized-crystals|Localized Crystals]] 순서로 넘어간다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/kashiwara93-crystal-base-demazure-character-formula|Kashiwara 1993]], Definition 1.2.1: abstract definition of crystals.
- Kashiwara 1993, Section 1.2 and Examples 1.2.4-1.2.8: morphisms, strict morphisms, direct sums, normal crystals, and examples $T_\lambda$, $C$, $B_i$, $B(\lambda)$, and $B(\infty)$.
- Kashiwara 1993, Section 1.3 and Proposition 1.3.1: tensor product of crystals and associativity.
- Kashiwara 1993, Theorem 3.3.2 and Propositions 3.3.4-3.3.5: $i$-string behavior for Demazure crystal subsets.
</details>
