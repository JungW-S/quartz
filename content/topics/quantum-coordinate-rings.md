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
  - quiver-hecke-algebra-localization
maturity: study-ready
---

# Quantum Coordinate Rings

## What it is

Quantum coordinate ring은 classical coordinate ring을 $q$-deformation한 algebraic object이다. Lie-theoretic setting에서는 quantum enveloping algebra의 dual 쪽에서 만들어지며, functions on a group or unipotent subgroup을 quantum algebra language로 다루게 해 준다.

핵심 예시는 $A_q(\mathfrak g)$, $A_q(\mathfrak n)$, 그리고 Weyl group element $w$에 붙는 $A_q(\mathfrak n(w))$이다. 이 notation들은 ambient quantum group, nilpotent part, unipotent subgroup 쪽을 각각 가리킨다.

## Basic picture

$$
\begin{array}{ccc}
U_q(\mathfrak n) & \xrightarrow{\ \Psi\ } & A_q(\mathfrak n) \\
\cup & & \cup \\
U_q(\mathfrak n(w)) & \xrightarrow{\ \Psi\ } & A_q(\mathfrak n(w))
\end{array}
$$

왼쪽은 quantum enveloping algebra side이고, 오른쪽은 coordinate-ring side이다. Map $\Psi$를 통해 $U_q(\mathfrak n)$의 element와 basis language를 $A_q(\mathfrak n)$의 coordinate-ring language로 읽을 수 있다.

## Definition

$A_q(\mathfrak g)$는 $U_q(\mathfrak g)^*$ 안의 subring으로 정의된다. 좌우 $U_q(\mathfrak g)$-submodule이 integrable category에 놓이는 linear forms를 모아 만든다.

$A_q(\mathfrak n)$는 $U_q(\mathfrak n)$의 graded dual이며, bilinear form에서 오는 map
$$
\Psi:U_q(\mathfrak n)\longrightarrow A_q(\mathfrak n)
$$
이 algebra isomorphism을 준다.

Weyl group element $w$에 대해서는 quantum root vector들로 $U_q(\mathfrak n(w))$를 만들고,
$$
A_q(\mathfrak n(w)):=\Psi(U_q(\mathfrak n(w)))
$$
로 unipotent subgroup 쪽 quantum coordinate ring을 정의한다.

## Example

**schematic.** $w$를 하나 고르면 $N(w)$는 classical side의 unipotent subgroup이고, $A_q(\mathfrak n(w))$는 그 coordinate ring을 quantum side에서 보는 object이다. 이 안에서 quantum minors, cluster variables, basis elements를 같은 algebra 안의 distinguished elements로 비교할 수 있다.

## Main facts

- $A_q(\mathfrak n)$는 $U_q(\mathfrak n)$과 algebra isomorphism으로 연결된다.
- $A_q(\mathfrak n(w))$는 $A_q(\mathfrak n)$의 subalgebra로 들어간다.
- $\mathcal C_w$에서 오는 quantum cluster algebra는 $A_q(\mathfrak n(w))$와 isomorphic하다.
- 특정 hypotheses 아래의 unipotent quantum minors는 dual canonical basis $B^*$에 속한다.

## Why it matters

Quantum coordinate rings는 category, basis, cluster algebra를 하나의 algebraic target 위에서 만나는 장소로 만든다. Monoidal categorification에서 Grothendieck-ring-level object가 coordinate-ring-level object와 비교될 때, 어떤 algebra가 target인지 이해하려면 이 topic이 필요하다.

## Connections

- [[topics/dual-canonical-bases|Dual Canonical Bases]]: unipotent quantum minors와 $B^*$의 관계를 읽는 배경이다.
- [[topics/monoidal-categorification|Monoidal Categorification]]: $\mathcal C_w$에서 오는 quantum cluster algebra와 $A_q(\mathfrak n(w))$ 사이의 bridge를 제공한다.
- [[topics/determinantial-modules|Determinantial Modules]]: determinantial-module language와 quantum-minor language를 비교할 때 coordinate-ring side를 제공한다.
- [[topics/quiver-hecke-algebra-localization|Quiver-Hecke Algebra Localization]]: category-level construction과 coordinate-ring-level target을 분리해서 읽는 데 도움이 된다.

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
