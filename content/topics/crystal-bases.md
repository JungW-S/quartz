---
id: crystal-bases
title: Crystal Bases and Crystal Graphs
level: core
topic_kind: basis
parent_topics:
  - quantum-groups
prerequisite_topics:
  - root-systems-and-weight-lattices
  - quantum-groups
child_topics:
  - cellular-crystals
  - localized-crystals
related_topics:
  - dual-canonical-bases
maturity: study-ready
---

# Crystal Bases and Crystal Graphs

## 개요

Crystal은 set $B$ 위에 weight map, root operators, 그리고 각 simple root direction의 길이 정보를 둔 combinatorial structure이다. Crystal base theory에서는 quantum group representation의 basis-level 정보를 $q=0$의 combinatorial shadow로 남기며, 그 shadow를 vertex와 colored arrows로 그리면 crystal graph로 볼 수 있다.

Crystal language는 representation-theoretic data를 colored graph로 바꾸기 위해 나타난다. 이 language는 [[topics/cellular-crystals|Cellular Crystals]]와 [[topics/localized-crystals|Localized Crystals]]처럼 서로 다른 constructions를 같은 crystal-level object로 비교할 때 사용된다.

## 준비와 notation

$I$를 simple roots의 index set이라고 하자. 각 $i\in I$에 대해 simple root를 $\alpha_i$, simple coroot를 $h_i$라고 쓰고, $P$를 weight lattice라고 쓴다.

Root-system and weight-lattice notation is reviewed in [[topics/root-systems-and-weight-lattices|Root Systems and Weight Lattices]]. The quantum-group origin of the $q=0$ picture is reviewed in [[topics/quantum-groups|Quantum Groups]].

Crystal $B$의 원소 $b$에는 다음 data가 붙는다.

- weight: $\operatorname{wt}(b)\in P$
- 길이 함수: $\varepsilon_i(b),\varphi_i(b)\in\mathbb Z\cup\{-\infty\}$
- root operators:
  $$
  \widetilde e_i,\widetilde f_i:B\to B\cup\{0\}
  $$

여기서 $0$은 $B$의 원소가 아니라 operator가 더 이상 적용되지 않을 때 쓰는 formal symbol이다.

Tensor products in this page follow Kashiwara's convention. Some combinatorics texts and SageMath use the opposite tensor convention, so tensor-product formulas from those references should be translated before being compared with the formulas here.

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

## 핵심 관점

Crystal graph는 원소 $b\in B$를 vertex로 그리고, $\widetilde f_i b=b'$일 때 색 $i$의 arrow를
$$
b\xrightarrow{\ i\ } b'
$$
로 그리는 해석이다. Operator $\widetilde e_i$는 같은 arrow를 거꾸로 따라가는 역할을 한다.

한 fixed $i$에 대해서 graph를 보면 $i$-colored string들이 나타난다. 이런 string 안에서 $\varepsilon_i(b)$는 위쪽으로 얼마나 올라갈 수 있는지, $\varphi_i(b)$는 아래쪽으로 얼마나 내려갈 수 있는지를 측정하는 함수로 읽을 수 있다.

## 기본 성질

- Crystals form a category. Morphisms preserve weight, $\varepsilon_i$, $\varphi_i$, and are compatible with root operators where the images are defined.
- A crystal is normal when $\varepsilon_i(b)$ and $\varphi_i(b)$ record the maximal number of times $\widetilde e_i$ and $\widetilde f_i$ can be applied.
- Crystals have direct sums and tensor products. The tensor product $B_1\otimes B_2$ has explicit formulas for $\operatorname{wt}$, $\varepsilon_i$, $\varphi_i$, $\widetilde e_i$, and $\widetilde f_i$, and tensor product is associative.
- For a dominant weight $\lambda$, $B(\lambda)$ is the normal crystal associated with the crystal base of the simple highest-weight module of highest weight $\lambda$.
- Demazure crystal subsets have controlled behavior along $i$-strings: their intersection with an $i$-string is empty, the whole string, or just the highest-weight vector.

## 다른 topic들과의 관계

**Quantum groups.** [[topics/quantum-groups|Quantum Groups]] supplies the representation-theoretic source of crystal bases. Crystal graph arrows are not arbitrary; they come from raising and lowering structure that remains at $q=0$.

**Root systems and weight lattices.** [[topics/root-systems-and-weight-lattices|Root Systems and Weight Lattices]] supplies the root, coroot, and weight-lattice notation behind $\operatorname{wt}$, $\varepsilon_i$, and $\varphi_i$.

**Cellular and localized crystals.** [[topics/cellular-crystals|Cellular Crystals]] use tensor products of elementary crystals. [[topics/localized-crystals|Localized Crystals]] use crystal operators on simple objects of a localized monoidal category.

**Dual canonical bases.** [[topics/dual-canonical-bases|Dual Canonical Bases]] are another basis-level structure near quantum coordinate rings; crystal bases provide the combinatorial side of this basis language.

## 더 읽을 topic

- Prerequisite topics: [[topics/root-systems-and-weight-lattices|Root Systems and Weight Lattices]]; [[topics/quantum-groups|Quantum Groups]].
- Parent topics: [[topics/quantum-groups|Quantum Groups]] explains the representation-theoretic source.
- Next topics: [[topics/cellular-crystals|Cellular Crystals]] for tensor-product crystal coordinates; [[topics/localized-crystals|Localized Crystals]] for category-level simple-object crystals.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/kashiwara93-crystal-base-demazure-character-formula|Kashiwara 1993]], Definition 1.2.1: abstract definition of crystals.
- Kashiwara 1993, Section 1.2: morphisms, strict morphisms, direct sums, normal crystals, and examples $T_\lambda$, $C$, $B_i$, $B(\lambda)$, and $B(\infty)$.
- Kashiwara 1993, Section 1.3 and Proposition 1.3.1: tensor product of crystals and associativity.
- Kashiwara 1993, Theorem 3.3.2 and Propositions 3.3.4-3.3.5: $i$-string behavior for Demazure crystal subsets.

</details>
