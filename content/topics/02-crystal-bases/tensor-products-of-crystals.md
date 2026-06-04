---
id: tensor-products-of-crystals
title: Tensor Products of Crystals
level: core
topic_kind: construction
parent_topics:
  - crystal-bases
prerequisite_topics:
  - abstract-crystals
child_topics: []
related_topics:
  - highest-weight-crystals
  - cellular-crystals
maturity: example-ready
---

## 개요

Tensor product of crystals는 두 abstract crystals $B_1,B_2$에서 새 crystal $B_1\otimes B_2$를 만드는 construction이다. 원소는 formal tensor symbols $b_1\otimes b_2$이고, weight는 더해지며, root operators는 두 tensor factors 중 어느 쪽을 바꿀지 Kashiwara의 비교 rule로 결정한다.

이 construction은 crystal bases가 tensor product representations에서 어떻게 행동하는지를 combinatorial level에서 다루기 위해 나타난다. 따라서 tensor product는 [[topics/02-crystal-bases/highest-weight-crystals|Highest Weight Crystals]], [[topics/02-crystal-bases/cellular-crystals|Cellular Crystals]], 그리고 localized crystal 비교를 읽기 전에 convention을 먼저 고정해야 하는 핵심 prerequisite이다.

여기서 쓰는 formula는 Kashiwara convention을 따른다. Schilling의 crystal text와 SageMath는 반대쪽 convention을 쓰는 경우가 있으므로, 그 notation을 이 convention의 formula와 그대로 섞으면 안 된다.

## 준비와 notation

$B_1,B_2$를 [[topics/02-crystal-bases/abstract-crystals|abstract crystals]]라고 하자. 원소는
$$
b_1\in B_1,\qquad b_2\in B_2
$$
로 쓴다.

각 simple root index $i\in I$에 대해
$$
\operatorname{wt}_i(b)=\langle h_i,\operatorname{wt}(b)\rangle
$$
라고 둔다. 여기서 $h_i$는 simple coroot이고 $\operatorname{wt}(b)$는 $b$의 weight이다.

Root operators는
$$
\widetilde e_i,\widetilde f_i
$$
로 쓰고, string functions는
$$
\varepsilon_i,\varphi_i
$$
로 쓴다. Operator가 더 이상 적용되지 않으면 formal symbol $0$이 나온다.

## 구성

### Underlying set

두 crystals $B_1,B_2$의 tensor product는 underlying set
$$
B_1\otimes B_2
=
\{b_1\otimes b_2\mid b_1\in B_1,\ b_2\in B_2\}
$$
으로 정의된다.

### Weight and string functions

Weight와 string functions는 다음과 같이 둔다.
$$
\operatorname{wt}(b_1\otimes b_2)
=
\operatorname{wt}(b_1)+\operatorname{wt}(b_2),
$$
$$
\varepsilon_i(b_1\otimes b_2)
=
\max\{\varepsilon_i(b_1),\varepsilon_i(b_2)-\operatorname{wt}_i(b_1)\},
$$
$$
\varphi_i(b_1\otimes b_2)
=
\max\{\varphi_i(b_2),\varphi_i(b_1)+\operatorname{wt}_i(b_2)\}.
$$

### Kashiwara tensor product rule

Kashiwara convention에서 root operators는 다음 rule로 정의된다.
$$
\widetilde e_i(b_1\otimes b_2)
=
\begin{cases}
\widetilde e_i b_1\otimes b_2,
&\text{if }\varphi_i(b_1)\ge \varepsilon_i(b_2),\\
b_1\otimes \widetilde e_i b_2,
&\text{if }\varphi_i(b_1)<\varepsilon_i(b_2),
\end{cases}
$$
$$
\widetilde f_i(b_1\otimes b_2)
=
\begin{cases}
\widetilde f_i b_1\otimes b_2,
&\text{if }\varphi_i(b_1)>\varepsilon_i(b_2),\\
b_1\otimes \widetilde f_i b_2,
&\text{if }\varphi_i(b_1)\le \varepsilon_i(b_2).
\end{cases}
$$

### Zero convention

여기서
$$
0\otimes b_2=b_1\otimes 0=0
$$
으로 이해한다.

## 기본 예시

### 실제 예시: one-element crystal과 tensor product

$T_\lambda$를 원소 하나 $t_\lambda$만 갖는 one-element crystal이라고 하자. Kashiwara의 tensor product rule을 적용하면 $b\in B$에 대해
$$
\operatorname{wt}(b\otimes t_\lambda)
=
\operatorname{wt}(b)+\lambda,
\qquad
\varepsilon_i(b\otimes t_\lambda)
=
\varepsilon_i(b),
$$
$$
\varphi_i(b\otimes t_\lambda)
=
\varphi_i(b)+\langle h_i,\lambda\rangle
$$
가 된다.

반대로 $T_\lambda$가 왼쪽에 있을 때는
$$
\operatorname{wt}(t_\lambda\otimes b)
=
\operatorname{wt}(b)+\lambda,
\qquad
\varepsilon_i(t_\lambda\otimes b)
=
\varepsilon_i(b)-\langle h_i,\lambda\rangle,
$$
$$
\varphi_i(t_\lambda\otimes b)
=
\varphi_i(b)
$$
가 된다.

이 예시는 one-element crystal이 tensor product에서 weight를 shift하지만, 어느 쪽에 tensor하느냐에 따라 $\varepsilon_i$와 $\varphi_i$ 중 어느 함수가 shift되는지가 달라진다는 점을 보여 준다.

예시 검증: 논문에 근거한 예시

## 핵심 관점

Tensor product rule은 한 vertex $b_1\otimes b_2$에서 root operator가 어느 factor를 바꿀지 결정하는 비교 rule이다. 비교하는 양은 왼쪽 factor의 $\varphi_i(b_1)$와 오른쪽 factor의 $\varepsilon_i(b_2)$이다.

Equality case가 중요하다. Kashiwara convention에서는
$$
\varphi_i(b_1)=\varepsilon_i(b_2)
$$
일 때 $\widetilde e_i$는 왼쪽 factor에 작용하고, $\widetilde f_i$는 오른쪽 factor에 작용한다. 이 boundary choice가 tensor product convention을 결정한다.

따라서 tensor product crystal은 단순히 두 graphs를 나란히 놓은 것이 아니다. 두 factors의 string data가 서로 비교되고, 그 비교 결과에 따라 crystal arrow가 어느 factor를 움직일지가 결정된다.

## 기본 성질

### Crystal 구조

위 formulas로 정의한 $B_1\otimes B_2$는 다시 crystal이다. 즉 tensor product는 crystal-level construction이다.

### Bifunctoriality

Tensor product는 crystals의 category에서 bifunctor로 작동한다. 따라서 crystals와 crystal morphisms를 함께 다룰 때도 tensor product construction을 사용할 수 있다.

### Theorem-level fact: associativity

세 crystals $B_1,B_2,B_3$에 대해
$$
(B_1\otimes B_2)\otimes B_3
\simeq
B_1\otimes (B_2\otimes B_3)
$$
가 되는 natural isomorphism이 있다. 그 isomorphism은
$$
(b_1\otimes b_2)\otimes b_3
\longmapsto
b_1\otimes (b_2\otimes b_3)
$$
로 주어진다.

### Normality 보존

$B_1$과 $B_2$가 normal crystals이면 $B_1\otimes B_2$도 normal crystal이다.

## 다른 topic들과의 관계

**Abstract Crystals.** [[topics/02-crystal-bases/abstract-crystals|Abstract Crystals]]는 $\operatorname{wt}$, $\varepsilon_i$, $\varphi_i$, $\widetilde e_i$, $\widetilde f_i$의 기본 axioms를 제공한다. Tensor product는 그 axioms를 보존하는 새 crystal을 만드는 construction이다.

**Crystal Bases.** [[topics/02-crystal-bases/crystal-bases|Crystal Bases]]는 tensor product rule이 quantum group representations에서 왜 필요한지 설명하는 상위 topic이다.

**Highest Weight Crystals.** [[topics/02-crystal-bases/highest-weight-crystals|Highest Weight Crystals]]에서는 $B(\lambda)$ 같은 standard crystals를 tensor product 안에 넣어 분석하는 일이 나타난다.

**Cellular Crystals.** [[topics/02-crystal-bases/cellular-crystals|Cellular Crystals]]는 elementary crystals
$$
B_{i_1}\otimes\cdots\otimes B_{i_m}
$$
안의 좌표 model을 사용한다. 따라서 cellular crystal의 coordinates를 읽으려면 tensor product convention이 먼저 고정되어야 한다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/02-crystal-bases/abstract-crystals|Abstract Crystals]]에서 crystal axioms와 root-operator notation을 읽는다.
- 상위 개념: [[topics/02-crystal-bases/crystal-bases|Crystal Bases]]는 tensor product rule이 representation-theoretic crystal bases에서 왜 나타나는지 설명한다.
- 다음에 읽을 것: [[topics/02-crystal-bases/highest-weight-crystals|Highest Weight Crystals]]에서 standard examples를 읽고, [[topics/02-crystal-bases/cellular-crystals|Cellular Crystals]]에서 tensor-product coordinate model을 읽는다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/kashiwara93-crystal-base-demazure-character-formula|Kashiwara 1993]], Section 1.3, pp.843-844: tensor product formulas for weight, $\varepsilon_i$, $\varphi_i$, $\widetilde e_i$, and $\widetilde f_i$.
- Kashiwara 1993, Example 1.3.2, p.845: tensor products with the one-element crystal $T_\lambda$.
- Kashiwara 1993, Proposition 1.3.1, p.844: associativity of tensor products.
- Kashiwara 1993, p.844: tensor product is a crystal, tensor product is functorial, and normality is preserved under tensor product.

</details>
