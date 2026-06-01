---
id: quantum-coordinate-rings
title: Quantum Coordinate Rings
level: core
topic_kind: algebra
parent_topics:
  - quantum-groups
prerequisite_topics:
  - root-systems-and-weight-lattices
  - quantum-groups
child_topics:
  - dual-canonical-bases
  - determinantial-modules
related_topics:
  - monoidal-categorification
  - quiver-hecke-category-localization
maturity: definition-ready
---

## 개요

Quantum coordinate ring은 classical coordinate ring을 $q$-deformation한 algebraic object이다. Lie-theoretic setting에서는 quantum enveloping algebra의 dual 쪽에서 만들어지며, functions on a group or unipotent subgroup을 quantum algebra language로 다루게 해 준다.

핵심 예시는 $A_q(\mathfrak g)$, $A_q(\mathfrak n)$, 그리고 Weyl group element $w$에 붙는 $A_q(\mathfrak n(w))$이다. 이 notation들은 ambient quantum group, nilpotent part, unipotent subgroup 쪽을 각각 가리킨다.

Quantum coordinate rings는 monoidal categorification, quantum cluster algebra, dual canonical basis가 만나는 coordinate-ring-level target으로 쓰인다. Category에서 얻은 Grothendieck ring을 coordinate-ring-level algebra와 비교할 때 이 topic이 필요하다.

## 준비와 notation

먼저 [[topics/quantum-groups|Quantum Groups]]에서 quantum enveloping algebra $U_q(\mathfrak g)$와 nilpotent part $U_q(\mathfrak n)$를 생각한다. Root and weight notation은 [[topics/root-systems-and-weight-lattices|Root Systems and Weight Lattices]]에서 온다.

$A_q(\mathfrak g)$는 full quantum coordinate ring이다. $A_q(\mathfrak n)$는 $U_q(\mathfrak n)$의 graded dual로 나타나는 coordinate-ring side object이고, $w\in W$에 대해 $A_q(\mathfrak n(w))$는 Weyl group element $w$에 붙은 quantum unipotent coordinate ring이다.

GLS11에서 쓰는 map
$$
\Psi:U_q(\mathfrak n)\longrightarrow A_q(\mathfrak n)
$$
는 enveloping-algebra side의 element를 coordinate-ring side의 element로 읽게 해 준다.

## 정의

$A_q(\mathfrak g)$는 $U_q(\mathfrak g)^*$ 안의 subring으로 정의된다. 그 원소는 linear form $\psi\in U_q(\mathfrak g)^*$ 중에서, $\psi$가 생성하는 left and right $U_q(\mathfrak g)$-submodules가 integrable category에 놓이는 것들이다. 곱은 $U_q(\mathfrak g)$의 comultiplication에 dual한 convolution product로 주어진다.

$A_q(\mathfrak n)$는 $U_q(\mathfrak n)$의 graded dual
$$
A_q(\mathfrak n)
=
\bigoplus_{\alpha\in Q_+}
\operatorname{Hom}_{\mathbb Q(q)}
\bigl(U_q(\mathfrak n)_\alpha,\mathbb Q(q)\bigr)
\subset U_q(\mathfrak n)^*
$$
이다. $U_q(\mathfrak n)^*$의 곱은 $U_q(\mathfrak b)$ 안으로 연장한 linear forms의 곱을 다시 제한해서 정의한다. Bilinear form에서 오는 map
$$
\Psi:U_q(\mathfrak n)\longrightarrow A_q(\mathfrak n),
\qquad
x\longmapsto (y\mapsto (x,y))
$$
는 algebra isomorphism이다.

Weyl group element $w$와 reduced expression을 고르면 Lusztig braid operators로 quantum root vectors $E(\beta_k)$를 만든다. 이 root vectors의 divided powers가 span하는 subspace는 reduced expression의 선택과 무관하며 $U_q(\mathfrak n(w))$로 쓴다. 그런 다음
$$
A_q(\mathfrak n(w)):=\Psi(U_q(\mathfrak n(w)))
$$
로 unipotent subgroup 쪽 quantum coordinate ring을 정의한다. 따라서 $A_q(\mathfrak n(w))$는 $A_q(\mathfrak n)$의 subalgebra이다.

## 핵심 관점

$$
\begin{array}{ccc}
U_q(\mathfrak n) & \xrightarrow{\ \Psi\ } & A_q(\mathfrak n) \\
\cup & & \cup \\
U_q(\mathfrak n(w)) & \xrightarrow{\ \Psi\ } & A_q(\mathfrak n(w))
\end{array}
$$

왼쪽은 quantum enveloping algebra side이고, 오른쪽은 coordinate-ring side이다. Map $\Psi$를 통해 $U_q(\mathfrak n)$의 element와 basis language를 $A_q(\mathfrak n)$의 coordinate-ring language로 읽을 수 있다.

## 기본 성질

- $A_q(\mathfrak n)$는 $U_q(\mathfrak n)$과 algebra isomorphism으로 연결된다.
- $A_q(\mathfrak n(w))$는 $A_q(\mathfrak n)$의 subalgebra로 들어간다.
- $\mathcal C_w$에서 오는 quantum cluster algebra는 $A_q(\mathfrak n(w))$와 isomorphic하다.
- 특정 hypotheses 아래의 unipotent quantum minors는 dual canonical basis $B^*$에 속한다.

## 다른 topic들과의 관계

- [[topics/quantum-groups|Quantum Groups]]는 $U_q(\mathfrak g)$와 $U_q(\mathfrak n)$를 제공하며, coordinate ring은 이 quantum enveloping algebra의 dual 쪽에서 만들어진다.
- [[topics/dual-canonical-bases|Dual Canonical Bases]]는 unipotent quantum minors와 $B^*$의 관계를 읽는 basis-level 배경이다.
- [[topics/monoidal-categorification|Monoidal Categorification]]은 $\mathcal C_w$에서 오는 quantum cluster algebra와 $A_q(\mathfrak n(w))$ 사이의 bridge를 제공한다.
- [[topics/determinantial-modules|Determinantial Modules]]는 determinantial-module language와 quantum-minor language를 비교할 때 coordinate-ring side를 사용한다.
- [[topics/quiver-hecke-category-localization|Quiver-Hecke Category Localization]]은 category-level construction과 coordinate-ring-level target을 분리해서 읽는 데 도움이 된다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/root-systems-and-weight-lattices|Root Systems and Weight Lattices]]에서 Weyl group과 weight notation을 읽고, [[topics/quantum-groups|Quantum Groups]]에서 $U_q(\mathfrak g)$와 $U_q(\mathfrak n)$를 읽는다.
- 상위 개념: [[topics/quantum-groups|Quantum Groups]]가 ambient quantum algebra를 제공한다.
- 다음에 읽을 것: [[topics/dual-canonical-bases|Dual Canonical Bases]]에서는 basis-level distinguished elements를 읽고, [[topics/monoidal-categorification|Monoidal Categorification]]에서는 Grothendieck-ring comparison을 읽고, [[topics/determinantial-modules|Determinantial Modules]]에서는 minors와 관련된 category-level objects를 읽는다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/gls11-cluster-structures-quantum-coordinate-rings|GLS11]], Section 2.4: definition of $A_q(\mathfrak g)$ as a quantum coordinate ring.
- GLS11, Section 4.2 and Proposition 4.1: $A_q(\mathfrak n)$ as graded dual and $\Psi:U_q(\mathfrak n)\to A_q(\mathfrak n)$ as an algebra isomorphism.
- GLS11, Sections 7.1-7.2: construction of $A_q(\mathfrak n(w))$.
- GLS11, Theorem 12.3: quantum cluster algebra attached to $\mathcal C_w$ is isomorphic to $A_q(\mathfrak n(w))$.
- GLS11, Section 6.2 and Proposition 6.3: unipotent quantum minors and the dual canonical basis $B^*$.
- [[sources/papers/kkop18-monoidal-categories-strata-flag-manifolds|KKOP18]], Theorem 2.20(ii)(c): comparison involving $K_0(\mathcal C_{w,v})$ and $A_{w,v}$.

</details>
