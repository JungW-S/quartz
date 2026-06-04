---
id: weight-modules
title: Weight Modules
level: core
topic_kind: object-family
parent_topics:
  - lie-algebra-representations
prerequisite_topics:
  - lie-algebra-representations
  - root-systems-and-weight-lattices
child_topics:
  - highest-weight-modules
  - characters-of-representations
  - category-o
related_topics:
  - quantum-groups
  - crystal-bases
maturity: example-ready
---

## 개요

Weight module은 representation을 weights로 분해할 수 있는 module이다. Quantum group representation에서는 Cartan part가 vector의 weight를 측정하고, raising/lowering generators가 weight를 simple root만큼 바꾼다.

이 구조는 [[topics/01-quantum-groups/highest-weight-modules|Highest-Weight Modules]], [[topics/01-quantum-groups/characters-of-representations|Characters of Representations]], [[topics/02-crystal-bases/crystal-bases|Crystal Bases]]의 공통 배경이다.

## 준비와 notation

$P$를 weight lattice라고 하자. Quantum group은 $U_q(\mathfrak g)$로 쓰고, $V^q$를 $U_q(\mathfrak g)$-module이라고 하자. Cartan part는 $q^h$로 쓴다.

$\mu\in P$와 $h$에 대해 pairing은
$$
\langle h,\mu\rangle
$$
로 쓴다. 이 pairing은 weight $\mu$가 Cartan element $h$에 대해 주는 eigenvalue exponent를 나타낸다.

## 정의

### Weight space

$\mu\in P$에 대해 weight $\mu$의 weight space는
$$
V^q_\mu
=
\{v\in V^q\mid q^h v=q^{\langle h,\mu\rangle}v
\text{ for all }h\}.
$$

### Weight module

$V^q$가 weight module이라는 것은
$$
V^q=\bigoplus_{\mu\in P}V^q_\mu
$$
로 분해된다는 뜻이다.

### Weight vector and maximal vector

Nonzero element $v\in V^q_\mu$를 weight vector of weight $\mu$라고 한다.

Weight vector $v$가 모든 $i\in I$에 대해
$$
e_i v=0
$$
을 만족하면 maximal vector라고 한다.

### Character

Weight module의 character는 weight multiplicities를 formal sum으로 기록한 object이다.
$$
\operatorname{ch} V^q
=
\sum_{\mu\in P}(\dim V^q_\mu)e^\mu
$$
형태로 weight-space dimensions를 기록한다.

## 기본 예시

### 실제 예시: $U_q(\mathfrak{sl}_2)$의 $V(m)$

$m\in\mathbb Z_{\ge 0}$에 대해 finite-dimensional irreducible $U_q(\mathfrak{sl}_2)$-module $V(m)$을 둔다. 이 module의 finite string vertices에 대해
$$
\operatorname{wt}(\overline{f^{(k)}u})=m-2k
\qquad (0\le k\le m)
$$
가 성립한다.

Weight-module 관점에서는 이 example의 weights가
$$
m,\ m-2,\ m-4,\ldots,-m
$$
처럼 나열된다. 즉 $U_q(\mathfrak{sl}_2)$에서 lowering direction은 이 normalization에서 weight label을 $2$씩 낮추는 방식으로 보인다.

이 예시는 character formula나 highest-weight generation을 설명하려는 것이 아니라, 하나의 module 안에서 weight labels가 어떻게 분리되어 나타나는지만 보여준다.

검증: 문헌 예시

## 핵심 관점

Weight module은 module을 Cartan part의 simultaneous eigenspaces로 나누어 보는 구조이다.

$$
V^q=\bigoplus_{\mu\in P}V^q_\mu.
$$

Raising/lowering generators는 이 decomposition 위에서 weight label을 바꾸는 operators로 보인다.

$$
e_i:V^q_\mu\to V^q_{\mu+\alpha_i},
\qquad
f_i:V^q_\mu\to V^q_{\mu-\alpha_i}.
$$

따라서 highest-weight theory로 넘어갈 때 중요한 것은 module 전체가 아니라, weight spaces와 그 사이를 잇는 raising/lowering directions이다.

## 기본 성질

### Weight-space decomposition

Weight space decomposition은 module을 Cartan part의 simultaneous eigenspaces로 분해한다.

### Raising and lowering

$e_i$와 $f_i$는 weight spaces 사이를 이동시키는 operators이다. Cartan relation에 의해 $e_i$는 weight를 $\alpha_i$만큼 올리고, $f_i$는 weight를 $\alpha_i$만큼 내리는 operator로 작용한다.

### Maximal vector

Maximal vector는 raising generators $e_i$에 의해 annihilated되는 weight vector이다. Highest-weight modules는 이런 vector가 module 전체를 생성하는 특수한 weight modules이다.

### Character

Character는 module 자체를 잊고 weight multiplicities만 기록한다. 이 때문에 character는 representation을 weight-level data로 비교할 때 쓰인다.

## 다른 topic들과의 관계

**Lie Algebra Representations.** [[topics/01-quantum-groups/lie-algebra-representations|Lie Algebra Representations]]는 representation과 module action의 기본 언어를 제공한다. Weight module은 그 위에 Cartan eigenvalue decomposition을 추가한 구조이다.

**Highest-Weight Modules.** [[topics/01-quantum-groups/highest-weight-modules|Highest-Weight Modules]]는 maximal vector에서 generated되는 weight modules이다.

**Characters of Representations.** [[topics/01-quantum-groups/characters-of-representations|Characters of Representations]]는 weight module의 weight multiplicities를 formal sum으로 기록한다.

**Quantum Groups.** [[topics/01-quantum-groups/quantum-groups|Quantum Groups]]에서는 $U_q(\mathfrak g)$-modules의 weight spaces가 Cartan generators의 action으로 정의된다.

**Crystal Bases.** [[topics/02-crystal-bases/crystal-bases|Crystal Bases]]는 weight data와 Kashiwara operators를 combinatorial object로 남긴다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/01-quantum-groups/lie-algebra-representations|Lie Algebra Representations]]에서 module action language를 읽고, [[topics/01-quantum-groups/root-systems-and-weight-lattices|Root Systems and Weight Lattices]]에서 $P$, $\alpha_i$, $h_i$ notation을 읽는다.
- 상위 개념: [[topics/01-quantum-groups/lie-algebra-representations|Lie Algebra Representations]]가 더 넓은 representation-theoretic setting이다.
- 다음에 읽을 것: [[topics/01-quantum-groups/highest-weight-modules|Highest-Weight Modules]]에서 maximal vector가 module 전체를 생성하는 경우를 읽고, [[topics/01-quantum-groups/characters-of-representations|Characters of Representations]]에서 weight multiplicities를 formal sum으로 기록하는 방법을 읽는다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/books/hong-kang02-introduction-quantum-groups-crystal-bases|Hong-Kang 2002]], Section 3.2, p.43: weight spaces, weight modules, weight vectors, maximal vectors, and characters for $U_q(\mathfrak g)$-modules.
- Hong-Kang 2002, Example 4.2.6, pp.68-69, and Section 4.3, p.73: the finite-dimensional $U_q(\mathfrak{sl}_2)$-module $V(m)$ and the weights $m-2k$ in its finite string example.

</details>
