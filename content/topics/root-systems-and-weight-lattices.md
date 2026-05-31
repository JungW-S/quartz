---
id: root-systems-and-weight-lattices
title: Root Systems and Weight Lattices
level: core
topic_kind: root
parent_topics: []
prerequisite_topics: []
child_topics: []
related_topics:
  - lie-algebras-and-hopf-algebras
  - quantum-groups
  - crystal-bases
  - quiver-hecke-algebras
maturity: study-ready
---

# Root Systems and Weight Lattices

## 개요

Root system은 real inner product space 안의 finite set of nonzero vectors로, reflections와 integrality 조건을 만족하는 구조이다. Weight lattice는 roots를 담고 coroots와 integer pairing을 갖는 lattice로, weights와 dominant weights를 말할 수 있게 해 주는 배경 공간이다.

이 topic은 crystal graph의 색, weight, dominant highest weight를 정하는 가장 낮은 combinatorial layer로 나타난다. 또한 [[topics/quantum-groups|Quantum Groups]]의 Cartan datum과 [[topics/quiver-hecke-algebras|Quiver-Hecke Algebras]]의 simple root notation을 읽기 위한 prerequisite이다.

## 준비와 notation

$V$를 real inner product space라고 하자. Inner product는 $\langle-,-\rangle$로 쓴다.

Nonzero vector $\alpha\in V$에 대해 reflection은
$$
r_\alpha(x)=x-2\frac{\langle x,\alpha\rangle}{\langle\alpha,\alpha\rangle}\alpha
$$
로 정의된다. Coroot는
$$
\alpha^\vee=\frac{2\alpha}{\langle\alpha,\alpha\rangle}
$$
이다.

Root system의 simple roots는 $\alpha_i$로 쓰고, index set은 $I$로 쓴다. Weight lattice는 보통 $\Lambda$ 또는 $P$로 쓰며, crystal pages에서는 Kashiwara notation에 맞추어 $P$를 기본 weight lattice notation으로 사용한다.

## 정의

Finite root system $\Phi\subset V$는 다음 성질을 갖는 nonzero vectors의 finite set이다.

- 각 $\alpha\in\Phi$에 대해 reflection $r_\alpha$가 $\Phi$를 보존한다.
- 모든 $\alpha,\beta\in\Phi$에 대해 $\langle\alpha,\beta^\vee\rangle$는 integer이다.
- $\Phi$ 안에서 한 root의 scalar multiple로 다시 root가 되는 것은 $\pm\alpha$뿐이다.

Weight lattice $\Lambda$는 $\Phi$에 대한 finitely generated abelian subgroup of $V$로, $V$를 span하고 $\Phi$를 포함하며
$$
\langle\lambda,\alpha^\vee\rangle\in\mathbb Z
$$
가 모든 $\lambda\in\Lambda$, $\alpha\in\Phi$에 대해 성립한다.

## 기본 예시

### 실제 예시

Type $A_{n-1}$의 $GL(n)$ version에서는
$$
V=\mathbb R^n,\qquad \Lambda=\mathbb Z^n,
$$
이고 root system은
$$
\Phi=\{e_i-e_j\mid i\ne j\}
$$
이다. Positive roots는 $e_i-e_j$ with $i<j$이고, simple roots는
$$
\alpha_i=e_i-e_{i+1}\qquad (i=1,\ldots,n-1)
$$
이다.

Dominant weights는
$$
\lambda=(\lambda_1,\ldots,\lambda_n)\in\mathbb Z^n,
\qquad
\lambda_1\ge\lambda_2\ge\cdots\ge\lambda_n
$$
인 weights이다. Fundamental weights는
$$
\omega_i=e_1+\cdots+e_i
$$
로 잡을 수 있다.

## 핵심 관점

Root system은 가능한 root directions의 finite geometry이다. Weight lattice는 그 geometry 위에 놓인 integer grid이고, dominant weights는 simple coroots와 nonnegative pairing을 갖는 weights이다.

Crystal graph에서 arrow color $i$는 simple root $\alpha_i$에 대응한다. Vertex $b$에서 $\widetilde f_i$를 적용하면 weight는 $\alpha_i$ direction으로 내려가고, $\widetilde e_i$를 적용하면 반대 방향으로 올라간다.

## 기본 성질

- Root system은 reflections로 닫혀 있으므로 Weyl group action을 만든다.
- Coroots는 weights와 integer pairing을 만들고, 이 pairing이 dominant weights를 정의한다.
- Type $A_{n-1}$에서는 roots가 coordinate differences $e_i-e_j$로 나타나므로, crystal arrows가 weights의 neighboring coordinates를 바꾸는 그림으로 보인다.
- Hong-Kang의 Cartan datum에서는 generalized Cartan matrix와 함께 $P$, $P^\vee$, simple roots, simple coroots, fundamental weights, root lattice가 한 번에 도입된다.

## 다른 topic들과의 관계

**Crystal bases.** [[topics/crystal-bases|Crystal Bases and Crystal Graphs]]의 weight map과 root operators는 root, coroot, weight-lattice notation을 사용한다. Expressions such as $\operatorname{wt}(b)$, $\langle h_i,\operatorname{wt}(b)\rangle$, $\widetilde e_i$, and $\widetilde f_i$ need this coordinate system.

**Quantum groups.** [[topics/quantum-groups|Quantum Groups]]는 generalized Cartan matrix와 Cartan datum에서 정의된다. Simple roots, simple coroots, and weight lattice data are part of that setup.

**Quiver-Hecke algebras.** [[topics/quiver-hecke-algebras|Quiver-Hecke Algebras]] use the same simple-root indexing, positive root lattice, and Cartan matrix notation before introducing KLR generators and relations.

## 더 읽을 topic

- Prerequisite topics: 없음. Root and weight notation의 출발점이다.
- Parent topics: 없음. 이 topic은 prerequisite root topic으로 둔다.
- Next topics: [[topics/quantum-groups|Quantum Groups]] for Cartan datum in quantum-group form; [[topics/crystal-bases|Crystal Bases and Crystal Graphs]] for weight-changing crystal operators; [[topics/quiver-hecke-algebras|Quiver-Hecke Algebras]] for positive roots in KLR notation.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/lectures/marberg20-combinatorics-crystal-bases-lectures|Marberg 2020]], Lecture 4, Definitions 3.3-3.4: finite root systems and weight lattices.
- Marberg 2020, Lecture 4, Examples 3.1-3.2 and Lecture 5, Example 1.1: type $A_{n-1}$ examples.
- [[sources/books/hong-kang02-introduction-quantum-groups-crystal-bases|Hong-Kang 2002]], Chapter 2, Section 2.1: Cartan datum, weight lattice $P$, dual weight lattice $P^\vee$, simple roots, simple coroots, fundamental weights, root lattice, and Weyl group notation.

</details>
