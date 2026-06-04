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
  - quantum-unipotent-coordinate-rings
  - dual-canonical-bases
  - determinantial-modules
related_topics:
  - quantum-cluster-algebras
  - monoidal-categorification
  - quiver-hecke-category-localization
maturity: definition-ready
---

## 개요

Quantum coordinate ring은 classical coordinate ring을 $q$-deformation한 algebraic object이다. Lie-theoretic setting에서는 quantum enveloping algebra의 dual 쪽에서 만들어지며, functions on a group or unipotent subgroup을 quantum algebra language로 다루게 해 준다.

기본 objects는 $A_q(\mathfrak g)$, $A_q(\mathfrak n)$, 그리고 Weyl group element $w$에 붙는 $A_q(\mathfrak n(w))$이다. 이 notation들은 ambient quantum group, nilpotent part, unipotent subgroup 쪽을 각각 가리킨다.

Quantum coordinate rings는 monoidal categorification, quantum cluster algebra, dual canonical basis가 만나는 coordinate-ring-level target으로 쓰인다. Category에서 얻은 Grothendieck ring을 coordinate-ring-level algebra와 비교할 때 어느 algebra와 비교하고 있는지를 고정한다.

## 준비와 notation

먼저 [[topics/01-quantum-groups/quantum-groups|Quantum Groups]]에서 quantum enveloping algebra $U_q(\mathfrak g)$와 nilpotent part $U_q(\mathfrak n)$를 생각한다. Root and weight notation은 [[topics/01-quantum-groups/root-systems-and-weight-lattices|Root Systems and Weight Lattices]]에서 온다.

$U_q(\mathfrak n)$와 $U_q(\mathfrak n(w))$는 enveloping-algebra side의 objects이다. $A_q(\mathfrak n)$와 $A_q(\mathfrak n(w))$는 coordinate-ring side의 objects이다. 아래 정의에서 두 side는 map $\Psi$를 통해 연결된다.

$A_q(\mathfrak g)$는 full quantum coordinate ring이다. $A_q(\mathfrak n)$는 $U_q(\mathfrak n)$의 graded dual로 나타나는 coordinate-ring side object이고, $w\in W$에 대해 $A_q(\mathfrak n(w))$는 Weyl group element $w$에 붙은 quantum unipotent coordinate ring이다.

GLS11에서 쓰는 map
$$
\Psi:U_q(\mathfrak n)\longrightarrow A_q(\mathfrak n)
$$
는 enveloping-algebra side의 element를 coordinate-ring side의 element로 읽게 해 준다. 따라서 $A_q(\mathfrak n(w))$를 정의할 때 먼저 $U_q(\mathfrak n(w))$를 만들고, 그 image를 coordinate-ring side에서 읽는다.

## 정의

### Full quantum coordinate ring

$A_q(\mathfrak g)$는 $U_q(\mathfrak g)^*$ 안의 subring으로 정의된다. 그 원소는 linear form $\psi\in U_q(\mathfrak g)^*$ 중에서, $\psi$가 생성하는 left and right $U_q(\mathfrak g)$-submodules가 integrable category에 놓이는 것들이다. 곱은 $U_q(\mathfrak g)$의 comultiplication에 dual한 convolution product로 주어진다.

### $A_q(\mathfrak n)$

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

### $A_q(\mathfrak n(w))$

Weyl group element $w$와 reduced expression을 고르면 Lusztig braid operators로 quantum root vectors $E(\beta_k)$를 만든다. 이 root vectors의 divided powers가 span하는 subspace는 reduced expression의 선택과 무관하며 $U_q(\mathfrak n(w))$로 쓴다. 그런 다음
$$
A_q(\mathfrak n(w)):=\Psi(U_q(\mathfrak n(w)))
$$
로 unipotent subgroup 쪽 quantum coordinate ring을 정의한다. 따라서 $A_q(\mathfrak n(w))$는 $A_q(\mathfrak n)$의 subalgebra이다.

## 핵심 관점

이 topic에서 가장 중요한 구분은 enveloping-algebra side와 coordinate-ring side의 구분이다.

$$
\begin{array}{ccc}
U_q(\mathfrak n) & \xrightarrow{\ \Psi\ } & A_q(\mathfrak n) \\
\cup & & \cup \\
U_q(\mathfrak n(w)) & \xrightarrow{\ \Psi\ } & A_q(\mathfrak n(w))
\end{array}
$$

왼쪽은 quantum enveloping algebra side이고, 오른쪽은 coordinate-ring side이다. Map $\Psi$를 통해 $U_q(\mathfrak n)$의 element와 basis language를 $A_q(\mathfrak n)$의 coordinate-ring language로 읽을 수 있다.

Monoidal categorification에서는 또 하나의 층위가 추가된다. Category의 simple objects와 tensor product는 Grothendieck ring을 만들고, 그 Grothendieck ring이 coordinate-ring-level algebra와 비교된다. 따라서 category-level statement를 읽을 때에는 그것이 $U_q(\mathfrak n)$ 자체에 관한 말인지, $A_q(\mathfrak n(w))$에 관한 말인지, 또는 Grothendieck ring의 realization에 관한 말인지 구분해야 한다.

## 기본 성질

### Enveloping-algebra side와 coordinate-ring side

$A_q(\mathfrak n)$는 map $\Psi$를 통해 $U_q(\mathfrak n)$과 algebra isomorphism으로 연결된다. 이 성질 때문에 $U_q(\mathfrak n)$에서 만든 basis나 root-vector construction을 coordinate-ring side에서 읽을 수 있다.

### Quantum unipotent subgroup

$A_q(\mathfrak n(w))$는 $A_q(\mathfrak n)$의 subalgebra로 들어간다. 여기서 $w$는 Weyl group element이고, $A_q(\mathfrak n(w))$는 그 $w$에 대응하는 quantum unipotent subgroup의 coordinate-ring side object로 읽힌다.

### Cluster-algebra comparison

$\mathcal C_w$에서 오는 quantum cluster algebra는 $A_q(\mathfrak n(w))$와 isomorphic하다. 이 말은 category-level construction의 Grothendieck ring이 coordinate-ring-level algebra를 실현한다는 뜻으로 읽어야 한다.

### Basis language

특정 hypotheses 아래의 unipotent quantum minors는 dual canonical basis $B^*$에 속한다. 그래서 quantum minors, determinantial modules, cluster variables를 비교할 때 basis-level language와 coordinate-ring-level language가 함께 등장한다.

## 다른 topic들과의 관계

[[topics/01-quantum-groups/quantum-groups|Quantum Groups]]는 $U_q(\mathfrak g)$와 $U_q(\mathfrak n)$를 제공한다. Quantum coordinate ring은 이 quantum enveloping algebra의 dual 쪽에서 만들어지므로, 먼저 $U_q(\mathfrak g)$의 generators, relations, Hopf algebra structure를 알고 있어야 한다.

[[topics/01-quantum-groups/dual-canonical-bases|Dual Canonical Bases]]는 unipotent quantum minors와 $B^*$의 관계를 읽는 basis-level 배경이다. Coordinate ring 안의 특별한 elements를 distinguished basis와 비교할 때 이 연결이 필요하다.

[[topics/04-cluster-algebras/quantum-cluster-algebras|Quantum Cluster Algebras]]는 $A_q(\mathfrak n(w))$와 비교되는 cluster-algebra side를 설명한다. 여기서는 coordinate ring이 cluster variables와 quantum mutation을 담는 algebra로 등장한다.

[[topics/05-monoidal-categorification/monoidal-categorification|Monoidal Categorification]]은 $\mathcal C_w$에서 오는 quantum cluster algebra와 $A_q(\mathfrak n(w))$ 사이의 bridge를 제공한다. Category-level tensor product가 Grothendieck ring에서 multiplication이 되고, 그 ring이 coordinate-ring-level algebra와 비교된다.

[[topics/06-quiver-hecke-klr-algebras/determinantial-modules|Determinantial Modules]]는 determinantial-module language와 quantum-minor language를 비교할 때 coordinate-ring side를 사용한다. 이 관계에서는 module의 class가 어떤 quantum minor에 대응하는지가 중요하다.

[[topics/08-localization-of-categories/quiver-hecke-category-localization|Quiver-Hecke Category Localization]]은 category-level construction과 coordinate-ring-level target을 분리해서 읽는 데 도움이 된다. Localization에서 얻은 category나 Grothendieck ring을 coordinate ring과 비교할 때 이 topic의 level 구분을 사용한다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/01-quantum-groups/root-systems-and-weight-lattices|Root Systems and Weight Lattices]]에서 Weyl group과 weight notation을 읽고, [[topics/01-quantum-groups/quantum-groups|Quantum Groups]]에서 $U_q(\mathfrak g)$와 $U_q(\mathfrak n)$를 읽는다.
- 상위 개념: [[topics/01-quantum-groups/quantum-groups|Quantum Groups]]가 ambient quantum algebra를 제공한다.
- 다음에 읽을 것: [[topics/01-quantum-groups/dual-canonical-bases|Dual Canonical Bases]]에서는 basis-level distinguished elements를 읽고, [[topics/04-cluster-algebras/quantum-cluster-algebras|Quantum Cluster Algebras]]에서는 quantum cluster side를 읽고, [[topics/05-monoidal-categorification/monoidal-categorification|Monoidal Categorification]]에서는 Grothendieck-ring comparison을 읽고, [[topics/06-quiver-hecke-klr-algebras/determinantial-modules|Determinantial Modules]]에서는 minors와 관련된 category-level objects를 읽는다.

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
