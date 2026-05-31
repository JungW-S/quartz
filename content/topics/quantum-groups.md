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
maturity: definition-ready
---

# Quantum Groups

## 개요

Quantum group $U_q(\mathfrak g)$는 Lie algebra $\mathfrak g$의 universal enveloping algebra를 parameter $q$가 있는 algebra로 deform한 object이다. Crystal bases는 이런 quantum group representation을 $q=0$ 근처에서 combinatorial하게 읽기 위해 등장한다.

이 topic은 crystal bases를 읽기 전에 필요한 algebraic setup으로 쓰인다. Weight notation, raising and lowering operators, highest-weight modules, and tensor products all come from this quantum-group background.

## 준비와 notation

먼저 [[topics/lie-algebras-and-hopf-algebras|Lie Algebras and Hopf Algebras]]에서 Lie algebra, universal enveloping algebra, and Hopf algebra language를 확인하고, [[topics/root-systems-and-weight-lattices|Root Systems and Weight Lattices]]에서 Cartan datum을 고정한다. Index set을 $I$라고 쓰고, simple roots와 simple coroots를 각각 $\alpha_i$, $h_i$로 쓴다. Weight lattice는 $P$이다.

Hong-Kang의 notation에서는 symmetrizable generalized Cartan matrix에 대해 positive integers $s_i$를 잡아 $s_i a_{ij}=s_j a_{ji}$가 되게 한다. 그리고
$$
q_i=q^{s_i},\qquad K_i=q^{s_i h_i}
$$
를 쓴다.

Quantum group $U_q(\mathfrak g)$의 기본 generators는 lowering generator $f_i$, raising generator $e_i$, 그리고 Cartan part를 나타내는 $q^h$이다.

Quantum Serre relations에는 $q_i$-binomial coefficients가 들어간다. 여기서는
$$
[m]_i=\frac{q_i^m-q_i^{-m}}{q_i-q_i^{-1}},\qquad
\begin{bmatrix}m\\r\end{bmatrix}_i
=
\frac{[m]_i!}{[r]_i![m-r]_i!}
$$
를 사용한다.

## 정의

Quantum group $U_q(\mathfrak g)$는 field $\mathbb F(q)$ 위의 associative algebra로, generators
$$
e_i,\quad f_i\quad (i\in I),\qquad q^h\quad (h\in P^\vee)
$$
를 갖고 Cartan datum에서 온 relations를 만족한다.

정의 relations는 다음과 같이 나뉜다.

- Cartan part:
  $$
  q^0=1,\qquad q^h q^{h'}=q^{h+h'}.
  $$
- Weight action:
  $$
  q^h e_i q^{-h}=q^{\langle h,\alpha_i\rangle}e_i,\qquad
  q^h f_i q^{-h}=q^{-\langle h,\alpha_i\rangle}f_i.
  $$
- Raising/lowering relation:
  $$
  e_i f_j-f_j e_i
  =
  \delta_{ij}\frac{K_i-K_i^{-1}}{q_i-q_i^{-1}}.
  $$
- Quantum Serre relations: $i\ne j$일 때
  $$
  \sum_{r=0}^{1-a_{ij}}
  (-1)^r
  \begin{bmatrix}1-a_{ij}\\r\end{bmatrix}_i
  e_i^{\,1-a_{ij}-r}e_j e_i^{\,r}=0,
  $$
  $$
  \sum_{r=0}^{1-a_{ij}}
  (-1)^r
  \begin{bmatrix}1-a_{ij}\\r\end{bmatrix}_i
  f_i^{\,1-a_{ij}-r}f_j f_i^{\,r}=0.
  $$

이 relations가 $U_q(\mathfrak g)$를 associative algebra로 결정한다. 마지막 quantum Serre relations가 generalized Cartan matrix의 off-diagonal entries를 반영한다.

## 기본 예시

## 핵심 관점

Classical enveloping algebra에서는 Lie algebra의 generators가 representation 위에 linear operators로 작용한다. Quantum group에서는 이 operators가 $q$-deformed relations를 만족한다.

Representation을 weight spaces로 분해하면
$$
V^q=\bigoplus_{\mu\in P}V^q_\mu
$$
처럼 쓸 수 있다. $e_i$와 $f_i$는 simple root direction을 따라 weights를 올리거나 내리는 operators로 해석된다. Crystal base theory는 이 weight-space picture에서 $q=0$의 combinatorial skeleton을 뽑아낸다.

## 기본 성질

- $U_q(\mathfrak g)$는 Hopf algebra structure를 갖는다. 따라서 tensor product representations를 만들 수 있다.
- Weight module에서는 module이 weight spaces의 direct sum으로 분해되고, 각 weight space는 $q^h$의 eigenvalue 조건으로 구분된다.
- Maximal vector는 모든 $e_i$에 의해 죽는 weight vector이다. Highest-weight representation과 crystal graph의 맨 위 vertex를 연결하는 기본 언어가 된다.
- Crystal bases는 $U_q(\mathfrak g)$-modules에서 정의되며, 이후에는 그 basis-level data가 crystal이라는 combinatorial object로 추상화된다.

## 다른 topic들과의 관계

**Lie and Hopf algebra background.** [[topics/lie-algebras-and-hopf-algebras|Lie Algebras and Hopf Algebras]] supplies universal enveloping algebra and Hopf algebra language. Quantum groups deform that background.

**Root and weight notation.** [[topics/root-systems-and-weight-lattices|Root Systems and Weight Lattices]] supplies Cartan datum, simple roots, simple coroots, and weight lattice notation.

**Crystal bases.** [[topics/crystal-bases|Crystal Bases and Crystal Graphs]] abstract the $q=0$ combinatorics of quantum group representations.

**Quantum coordinate rings.** [[topics/quantum-coordinate-rings|Quantum Coordinate Rings]] appear on the dual or coordinate-ring side of quantum group theory.

## 더 읽을 topic

- Prerequisite topics: [[topics/lie-algebras-and-hopf-algebras|Lie Algebras and Hopf Algebras]]; [[topics/root-systems-and-weight-lattices|Root Systems and Weight Lattices]].
- Parent topics: [[topics/lie-algebras-and-hopf-algebras|Lie Algebras and Hopf Algebras]] gives the enveloping algebra background.
- Next topics: [[topics/crystal-bases|Crystal Bases and Crystal Graphs]] for $q=0$ combinatorics; [[topics/quantum-coordinate-rings|Quantum Coordinate Rings]] for the coordinate-ring side.

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
