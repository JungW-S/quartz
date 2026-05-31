---
id: quantum-groups
title: Quantum Groups
level: core
topic_kind: algebra
parent_topics:
  - lie-algebras-and-hopf-algebras
prerequisite_topics:
  - lie-algebras-and-hopf-algebras
  - root-systems-and-weight-lattices
child_topics:
  - crystal-bases
  - quantum-coordinate-rings
related_topics:
  - dual-canonical-bases
maturity: study-ready
---

# Quantum Groups

## What it is

Quantum group $U_q(\mathfrak g)$는 Lie algebra $\mathfrak g$의 universal enveloping algebra를 parameter $q$가 있는 algebra로 deform한 object이다. Crystal bases는 이런 quantum group representation을 $q=0$ 근처에서 combinatorial하게 읽기 위해 등장한다.

이 페이지에서는 quantum group 자체의 깊은 representation theory가 아니라, crystal bases를 읽기 전에 필요한 기본 setup을 설명한다.

## Why it appears

Crystal은 처음부터 단순한 graph로 정의된 물건이 아니라, quantum group representation의 basis theory에서 나온 combinatorial shadow이다. Operators $\widetilde e_i,\widetilde f_i$와 weight notation은 $U_q(\mathfrak g)$의 generators, weights, highest-weight modules를 배경으로 갖는다.

따라서 crystal graph를 공부할 때도 underlying root datum, weight lattice, raising and lowering operators가 어떤 algebraic structure에서 왔는지 알아야 한다.

## Setup and notation

먼저 [[topics/lie-algebras-and-hopf-algebras|Lie Algebras and Hopf Algebras]]에서 Lie algebra, universal enveloping algebra, and Hopf algebra language를 확인하고, [[topics/root-systems-and-weight-lattices|Root Systems and Weight Lattices]]에서 Cartan datum을 고정한다. Index set을 $I$라고 쓰고, simple roots와 simple coroots를 각각 $\alpha_i$, $h_i$로 쓴다. Weight lattice는 $P$이다.

Hong-Kang의 notation에서는 symmetrizable generalized Cartan matrix에 대해 positive integers $s_i$를 잡아 $s_i a_{ij}=s_j a_{ji}$가 되게 한다. 그리고
$$
q_i=q^{s_i},\qquad K_i=q^{s_i h_i}
$$
를 쓴다.

Quantum group $U_q(\mathfrak g)$의 기본 generators는 lowering generator $f_i$, raising generator $e_i$, 그리고 Cartan part를 나타내는 $q^h$이다.

## Definition

Quantum group $U_q(\mathfrak g)$는 field $\mathbb F(q)$ 위의 associative algebra로, generators
$$
e_i,\quad f_i,\quad q^h
$$
를 갖고 Cartan datum에서 온 relations를 만족한다.

핵심 관계는 세 층으로 나뉜다.

- Cartan part: $q^h q^{h'}=q^{h+h'}$이고 $q^0=1$이다.
- Weight action: $q^h$는 $e_i$와 $f_i$를 conjugation으로 각각 $\langle h,\alpha_i\rangle$만큼 rescale한다.
- Raising/lowering relation: $e_i$와 $f_j$의 commutator는 $i=j$일 때 $K_i$와 $K_i^{-1}$로 표현되고, $i\ne j$일 때는 사라진다.

이 relations에 더해 quantum Serre relations가 들어가며, 이것이 generalized Cartan matrix의 off-diagonal entries를 반영한다.

## Basic picture

Classical enveloping algebra에서는 Lie algebra의 generators가 representation 위에 linear operators로 작용한다. Quantum group에서는 이 operators가 $q$-deformed relations를 만족한다.

Representation을 weight spaces로 분해하면
$$
V^q=\bigoplus_{\mu\in P}V^q_\mu
$$
처럼 쓸 수 있다. $e_i$와 $f_i$는 simple root direction을 따라 weights를 올리거나 내리는 operators로 해석된다.

Crystal base theory는 이 weight-space picture에서 $q=0$의 combinatorial skeleton을 뽑아낸다. 그 skeleton에서 남는 것이 crystal operators와 crystal graph이다.

## Example

### Schematic example

$\mathfrak{sl}_2$에 해당하는 경우에는 simple root direction이 하나뿐이다. 따라서 quantum group에는 하나의 raising generator $e$, 하나의 lowering generator $f$, 그리고 Cartan part $q^h$가 나타난다.

이 경우 crystal graph는 한 가지 색의 arrows만 갖는다. Highest-weight representation의 crystal은 가장 위 vertex에서 $\widetilde f$를 반복해서 아래로 내려가는 string으로 생각할 수 있다.

## Main facts

- $U_q(\mathfrak g)$는 Hopf algebra structure를 갖는다. 따라서 tensor product representations를 만들 수 있다.
- Weight module에서는 module이 weight spaces의 direct sum으로 분해되고, 각 weight space는 $q^h$의 eigenvalue 조건으로 구분된다.
- Maximal vector는 모든 $e_i$에 의해 죽는 weight vector이다. Highest-weight representation과 crystal graph의 맨 위 vertex를 연결하는 기본 언어가 된다.
- Crystal bases는 $U_q(\mathfrak g)$-modules에서 정의되며, 이후에는 그 basis-level data가 crystal이라는 combinatorial object로 추상화된다.

## Why it matters

Quantum group은 crystal bases가 왜 단순한 colored graph 이상의 의미를 갖는지 설명한다. Crystal graph의 arrows는 임의로 붙인 combinatorial arrows가 아니라, quantum group representation의 raising and lowering structure가 $q=0$에서 남긴 흔적이다.

이 배경을 알면 [[topics/crystal-bases|Crystal Bases and Crystal Graphs]]에서 weight, root operators, tensor product crystals가 왜 같은 package 안에 들어가는지 이해하기 쉽다.

## Connections

- [[topics/root-systems-and-weight-lattices|Root Systems and Weight Lattices]]: Cartan datum, simple roots, simple coroots, and weight lattice notation을 제공한다.
- [[topics/lie-algebras-and-hopf-algebras|Lie Algebras and Hopf Algebras]]: universal enveloping algebra and Hopf algebra language를 제공한다.
- [[topics/crystal-bases|Crystal Bases and Crystal Graphs]]: quantum group representation의 $q=0$ combinatorics를 crystal로 추상화한다.
- [[topics/quantum-coordinate-rings|Quantum Coordinate Rings]]: quantum group의 dual 또는 관련 subalgebra에서 coordinate-ring-side objects가 등장한다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/books/hong-kang02-introduction-quantum-groups-crystal-bases|Hong-Kang 2002]], Chapter 2, Section 2.1 and Definition 2.1.1: Cartan datum, weight lattice, simple roots, and simple coroots.
- Hong-Kang 2002, Chapter 1, Definition 1.2.3 and Definition 1.5.3: universal enveloping algebra and Hopf algebra prerequisites.
- Hong-Kang 2002, Definition 2.1.3: Kac-Moody algebra associated with a Cartan datum.
- Hong-Kang 2002, Definition 3.1.1: definition of $U_q(\mathfrak g)$.
- Hong-Kang 2002, Proposition 3.1.2: Hopf algebra structure on $U_q(\mathfrak g)$.
- Hong-Kang 2002, Section 3.2: weight modules, maximal vectors, and characters.

</details>
