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
maturity: definition-ready
---

## 개요

Dual canonical basis는 quantum group과 quantum coordinate ring 사이를 오갈 때 distinguished elements를 추적하는 basis-level structure이다. GLS11의 notation에서는 $U_q(\mathfrak n)$의 canonical basis $B$에 대해, scalar product에 adjoint인 basis $B^*$를 dual canonical basis라고 부른다.

이 basis는 coordinate-ring side와도 연결된다. Isomorphism $\Psi:U_q(\mathfrak n)\to A_q(\mathfrak n)$를 통해 $U_q(\mathfrak n)$의 element를 $A_q(\mathfrak n)$의 coordinate-ring element로 읽을 수 있다.

## 준비와 notation

[[topics/quantum-coordinate-rings|Quantum Coordinate Rings]]에서 $U_q(\mathfrak n)$, $A_q(\mathfrak n)$, 그리고 isomorphism
$$
\Psi:U_q(\mathfrak n)\longrightarrow A_q(\mathfrak n)
$$
을 사용한다. $B$는 $U_q(\mathfrak n)$의 canonical basis이고, $B^*$는 이 basis에 adjoint인 basis이다.

Adjoint라는 말은 $U_q(\mathfrak n)$에 주어진 scalar product를 기준으로 한다. 여기서는 $B^*$를 basis-level object로 보고, $\Psi$를 통해 coordinate-ring-level object와 연결한다.

## 정의

$B^*$는 $U_q(\mathfrak n)$의 canonical basis $B$에 adjoint인 basis이다. 구체적으로 $U_q(\mathfrak n)$에 주어진 scalar product를 $(\, ,\, )$라고 하면, 각 $b\in B$에 대해 $b^*\in B^*$는
$$
(b^*,b')=\delta_{b,b'}
\qquad (b'\in B)
$$
를 만족하도록 정해진다. 이 조건이 $B$에 dual한 basis $B^*$를 결정한다.

GLS11은 $B^*$를 $\Psi$를 통해 $A_q(\mathfrak n)$ 안의 dual basis와 identify할 수 있다고 설명한다.

## 기본 예시

### 실제 예시

Unipotent quantum minor $d_{u(\lambda),v(\lambda)}$는 GLS11의 hypotheses가 만족될 때 $B^*$에 속한다. 이 family는 quantum minors가 dual canonical basis와 직접 만나는 기본 예시이다.

검증: 논문 예시

## 핵심 관점

$$
\text{canonical basis }B
\;\longleftrightarrow\;
\text{dual canonical basis }B^*
\;\xrightarrow{\ \Psi\ }\;
A_q(\mathfrak n)
$$

Basis-level statement와 coordinate-ring-level statement는 $\Psi$를 통해 연결된다.

## 기본 성질

- $B^*$는 canonical basis $B$에 adjoint인 basis이다.
- $B^*$는 $\Psi$를 통해 $A_q(\mathfrak n)$의 dual basis와 연결된다.
- 특정 unipotent quantum minors는 $B^*$에 속한다.

## 다른 topic들과의 관계

- [[topics/quantum-coordinate-rings|Quantum Coordinate Rings]]는 $A_q(\mathfrak n)$와 $A_q(\mathfrak n(w))$에서 $B^*$와 quantum minors를 비교하는 coordinate-ring background를 제공한다.
- [[topics/crystal-bases|Crystal Bases]]는 quantum group에서 나오는 또 다른 basis-level structure를 제공한다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/quantum-groups|Quantum Groups]]에서 ambient quantum algebra를 읽고, [[topics/quantum-coordinate-rings|Quantum Coordinate Rings]]에서 $\Psi$와 $A_q(\mathfrak n)$를 읽는다.
- 상위 개념: [[topics/quantum-coordinate-rings|Quantum Coordinate Rings]]가 여기서 $B^*$가 쓰이는 coordinate-ring setting이다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/gls11-cluster-structures-quantum-coordinate-rings|GLS11]], Section 6.2 and Proposition 6.3: $B^*$ is the basis adjoint to $B$, and unipotent quantum minors satisfying the stated hypotheses belong to $B^*$.

</details>
