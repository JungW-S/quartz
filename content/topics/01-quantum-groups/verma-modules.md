---
id: verma-modules
title: Verma Modules
level: advanced
topic_kind: object-family
parent_topics:
  - highest-weight-modules
  - category-o
prerequisite_topics:
  - quantum-groups
  - highest-weight-modules
  - category-o
child_topics: []
related_topics:
  - highest-weight-crystals
maturity: example-ready
---

## 개요

Verma module은 prescribed highest weight에서 출발해 만드는 universal highest-weight module이다. Quantum-group notation에서는 weight $\lambda\in P$마다
$$
M^q(\lambda)
$$
를 만들고, 이 module은 highest weight $\lambda$와 highest weight vector $v_\lambda$를 갖는다.

Verma module은 [[topics/01-quantum-groups/highest-weight-modules|Highest-Weight Modules]]와 [[topics/01-quantum-groups/category-o|Quantum Category O]] 다음에 읽는 object이다. Highest-weight module은 하나의 highest weight vector가 module 전체를 생성하는 module이고, Verma module은 같은 highest weight를 가진 highest-weight modules로 가는 canonical quotient map을 제공하는 universal source이다.

## 준비와 notation

$U_q(\mathfrak g)$를 quantum group이라고 하자. Generators는
$$
e_i,\quad f_i,\quad q^h
\qquad (i\in I,\ h\in P^\vee)
$$
로 쓴다. Weight lattice는 $P$이고, $\lambda\in P$를 고정한다.

Negative part는
$$
U_q^-
$$
로 쓴다. $U_q^-$는 lowering generators 쪽에서 오는 part이고, Verma module의 underlying size를 설명할 때 쓰인다.

Highest weight vector notation은
$$
v_\lambda
$$
로 쓴다.

## 정의

$J^q(\lambda)$를 $U_q(\mathfrak g)$의 left ideal로 정의한다. 이 left ideal은 다음 elements로 generated된다.
$$
e_i\qquad (i\in I),
$$
그리고
$$
q^h-q^{\lambda(h)}1
\qquad (h\in P^\vee).
$$

Weight $\lambda$의 Verma module은 quotient module
$$
M^q(\lambda)
=
U_q(\mathfrak g)/J^q(\lambda)
$$
이다. Highest weight vector는
$$
v_\lambda=1+J^q(\lambda)
$$
이다.

이 definition에서 바로
$$
q^h v_\lambda=q^{\lambda(h)}v_\lambda,\qquad
e_i v_\lambda=0,\qquad
U_q(\mathfrak g)v_\lambda=M^q(\lambda)
$$
가 성립한다. 따라서 $M^q(\lambda)$는 highest weight $\lambda$와 highest weight vector $v_\lambda$를 갖는 highest-weight module이다.

## 기본 예시

### 실제 예시: $M^q(\lambda)$

$\lambda\in P$를 하나 고정하면 Verma-module construction은 quotient
$$
M^q(\lambda)=U_q(\mathfrak g)/J^q(\lambda)
$$
을 준다. 이 quotient에서는 $e_i$가 highest weight vector를 죽이고, $q^h$가 $q^{\lambda(h)}$로 작용한다.

따라서 $M^q(\lambda)$의 top vector는
$$
v_\lambda=1+J^q(\lambda)
$$
이고, module 전체는 $v_\lambda$에서 생성된다.

검증: 문헌 예시

## 핵심 관점

Verma module은 highest-weight module을 만드는 universal object이다. Weight $\lambda$를 정하면, $v_\lambda$가 가져야 할 highest-weight relations만 quotient로 강제한다.

이 construction은 두 level을 구분한다.

- Object-level: $M^q(\lambda)$는 하나의 $U_q(\mathfrak g)$-module이다.
- Category-level: $\mathcal O^q$ 안의 highest-weight modules는 $M^q(\lambda)$의 homomorphic images로 나타난다.

따라서 Verma module은 irreducible highest-weight module을 바로 정의하는 것이 아니라, 먼저 universal highest-weight module을 만들고 그 quotient를 통해 irreducible object로 내려가는 방식이다.

## 기본 성질

### Free $U_q^-$-module structure

$M^q(\lambda)$는
$$
v_\lambda=1+J^q(\lambda)
$$
가 생성하는 rank $1$ free $U_q^-$-module이다. 따라서 Verma module의 size는 lowering part $U_q^-$가 highest weight vector에 작용해서 생기는 방향으로 이해된다.

### Universal property

Highest weight $\lambda$를 갖는 모든 highest-weight $U_q(\mathfrak g)$-module은 $M^q(\lambda)$의 homomorphic image이다. 이 사실 때문에 Verma module은 prescribed highest weight에서 출발하는 universal highest-weight module이라고 불린다.

### Maximal submodule

$M^q(\lambda)$는 unique maximal submodule을 갖는다. 이 submodule을
$$
N^q(\lambda)
$$
로 쓴다.

### Irreducible quotient

Quotient
$$
V^q(\lambda)=M^q(\lambda)/N^q(\lambda)
$$
는 highest weight $\lambda$를 갖는 irreducible highest-weight module이다.

$$
M^q(\lambda)
\twoheadrightarrow
V^q(\lambda)
$$

이 quotient map은 universal highest-weight module에서 irreducible highest-weight module로 내려가는 표준 경로이다.

## 다른 topic들과의 관계

**Highest-Weight Modules.** [[topics/01-quantum-groups/highest-weight-modules|Highest-Weight Modules]]는 highest weight vector가 생성하는 modules의 일반 정의를 제공한다. Verma modules는 prescribed highest weight를 갖는 universal examples이다.

**Quantum Category O.** [[topics/01-quantum-groups/category-o|Quantum Category O]]는 highest-weight objects가 놓이는 category-level setting $\mathcal O^q$를 제공한다.

**Weight Modules.** [[topics/01-quantum-groups/weight-modules|Weight Modules]]는 highest weights와 characters를 말하는 데 필요한 weight-space language를 제공한다.

**Highest Weight Crystals.** [[topics/02-crystal-bases/highest-weight-crystals|Highest Weight Crystals]]는 Verma module 자체가 아니라 irreducible highest-weight modules에 붙는 crystal-level object를 다룬다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/01-quantum-groups/highest-weight-modules|Highest-Weight Modules]], [[topics/01-quantum-groups/category-o|Quantum Category O]]
- 상위 개념: [[topics/01-quantum-groups/category-o|Quantum Category O]]
- 다음에 읽을 것: [[topics/02-crystal-bases/highest-weight-crystals|Highest Weight Crystals]]

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/books/hong-kang02-introduction-quantum-groups-crystal-bases|Hong-Kang 2002]], Section 3.2, printed p.44: definition of $J^q(\lambda)$, $M^q(\lambda)=U_q(\mathfrak g)/J^q(\lambda)$, and $v_\lambda=1+J^q(\lambda)$.
- Hong-Kang 2002, Proposition 3.2.2, printed pp.44-45: $U_q^-$-freeness, universal property, and unique maximal submodule of $M^q(\lambda)$.
- Hong-Kang 2002, printed p.45: notation $N^q(\lambda)$ and irreducible highest-weight quotient $V^q(\lambda)=M^q(\lambda)/N^q(\lambda)$.

</details>
