---
id: dual-canonical-bases
title: Dual Canonical Bases
level: core
topic_kind: basis
parent_topics:
  - quantum-coordinate-rings
prerequisite_topics:
  - quantum-groups
  - quantum-coordinate-rings
child_topics: []
related_topics:
  - crystal-bases
  - quantum-minors-and-frozen-variables
maturity: definition-ready
---

## 개요

Dual canonical basis는 canonical basis와 duality pairing으로 연결된 basis이다. $U_q(\mathfrak n)$의 canonical basis $B$에 대해, scalar product에 dual한 basis를 $B^*$로 쓴다.

이 basis가 중요한 이유는 quantum coordinate ring 쪽의 distinguished elements와 연결되기 때문이다. Isomorphism $\Psi:U_q(\mathfrak n)\to A_q(\mathfrak n)$를 통해 $U_q(\mathfrak n)$의 element를 $A_q(\mathfrak n)$의 coordinate-ring element로 읽을 수 있다.

## 준비와 notation

[[topics/01-quantum-groups/quantum-coordinate-rings|Quantum Coordinate Rings]]에서 $U_q(\mathfrak n)$, $A_q(\mathfrak n)$, 그리고 isomorphism
$$
\Psi:U_q(\mathfrak n)\longrightarrow A_q(\mathfrak n)
$$
을 사용한다. $B$는 $U_q(\mathfrak n)$의 canonical basis이고, $B^*$는 이 basis에 adjoint인 basis이다.

Duality는 $U_q(\mathfrak n)$에 주어진 scalar product를 기준으로 한다. $B^*$는 먼저 $U_q(\mathfrak n)$ 안의 basis-level object로 정의되고, 그 뒤 $\Psi$를 통해 coordinate-ring-level object와 연결된다.

## 정의

$B^*$는 $U_q(\mathfrak n)$의 canonical basis $B$에 dual한 basis이다. 구체적으로 $U_q(\mathfrak n)$에 주어진 scalar product를 $(\, ,\, )$라고 하면, 각 $b\in B$에 대응하는 element $b^*\in B^*$는
$$
(b^*,b')=\delta_{b,b'}
\qquad (b'\in B)
$$
를 만족하도록 정해진다. 이 조건이 $B$에 dual한 basis $B^*$를 결정한다.

이 정의는 basis-level 정의이다. Coordinate-ring-level에서는 $\Psi$를 통해 $B^*$를 $A_q(\mathfrak n)$ 안의 dual basis와 비교한다.

## 기본 예시

### 실제 예시

Unipotent quantum minor $d_{u(\lambda),v(\lambda)}$는 해당 조건이 만족되는 경우 $B^*$에 속한다. 이 family는 quantum minors가 dual canonical basis와 직접 만나는 기본 예시이다.

검증: 논문 예시

## 핵심 관점

$$
\text{canonical basis }B
\;\longleftrightarrow\;
\text{dual basis }B^*
\;\xrightarrow{\ \Psi\ }\;
A_q(\mathfrak n)
$$

먼저 $B$와 $B^*$의 관계는 scalar product로 정해지는 basis-level duality이다. 그 다음 $\Psi$가 이 basis data를 coordinate-ring side로 옮긴다.

## 기본 성질

### Basis-level duality

$B^*$는 canonical basis $B$에 dual한 basis이다. 정의의 핵심은 scalar product에 대한 조건 $(b^*,b')=\delta_{b,b'}$이다.

### Coordinate-ring comparison

$\Psi:U_q(\mathfrak n)\to A_q(\mathfrak n)$는 $B^*$를 coordinate-ring side에서 읽을 수 있게 한다. 따라서 $B^*$에 대한 statement는 $U_q(\mathfrak n)$ 안의 basis statement이면서, 동시에 $A_q(\mathfrak n)$ 안의 coordinate-ring statement로도 해석된다.

### Quantum minors

특정 unipotent quantum minors는 $B^*$에 속한다. 이 사실 때문에 dual canonical basis는 quantum coordinate rings와 cluster-theoretic constructions를 연결하는 데 쓰인다.

## 다른 topic들과의 관계

**Quantum Coordinate Rings.** [[topics/01-quantum-groups/quantum-coordinate-rings|Quantum Coordinate Rings]]는 $A_q(\mathfrak n)$와 $A_q(\mathfrak n(w))$에서 $B^*$와 quantum minors를 비교하는 coordinate-ring background를 제공한다.

**Crystal Bases.** [[topics/02-crystal-bases/crystal-bases|Crystal Bases]]는 $q\to0$ limit에서 나타나는 combinatorial basis language를 제공한다. Dual canonical basis는 coordinate-ring side의 distinguished basis language이고, crystal bases는 representation과 quantum group 쪽의 combinatorial shadow를 제공한다.

**Quantum Cluster Algebras.** [[topics/04-cluster-algebras/quantum-cluster-algebras|Quantum Cluster Algebras]]에서는 quantum coordinate ring 안의 distinguished elements와 cluster variables를 비교하는 문제가 나타난다. Dual canonical basis는 이 비교에서 기준이 되는 basis family 중 하나이다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/01-quantum-groups/quantum-groups|Quantum Groups]]에서 ambient quantum algebra를 읽고, [[topics/01-quantum-groups/quantum-coordinate-rings|Quantum Coordinate Rings]]에서 $\Psi$와 $A_q(\mathfrak n)$를 읽는다.
- 상위 개념: [[topics/01-quantum-groups/quantum-coordinate-rings|Quantum Coordinate Rings]]가 여기서 $B^*$가 쓰이는 coordinate-ring 쪽 배경이다.
- 다음에 읽을 것: [[topics/04-cluster-algebras/quantum-cluster-algebras|Quantum Cluster Algebras]]에서 coordinate-ring elements와 quantum cluster variables가 만나는 방향을 읽는다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/gls11-cluster-structures-quantum-coordinate-rings|GLS11]], Section 6.2 and Proposition 6.3: $B^*$ is the basis adjoint to $B$, and unipotent quantum minors satisfying the stated hypotheses belong to $B^*$.

</details>
