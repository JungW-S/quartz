---
id: dual-canonical-bases
title: Dual Canonical Bases
level: core
---

# Dual Canonical Bases

## What it is

Dual canonical basis는 quantum group과 quantum coordinate ring 사이를 오갈 때 distinguished elements를 추적하는 basis-level structure이다. GLS11의 notation에서는 $U_q(\mathfrak n)$의 canonical basis $B$에 대해, scalar product에 adjoint인 basis $B^*$를 dual canonical basis라고 부른다.

이 basis는 coordinate-ring side와도 연결된다. Isomorphism $\Psi:U_q(\mathfrak n)\to A_q(\mathfrak n)$를 통해 $U_q(\mathfrak n)$의 element를 $A_q(\mathfrak n)$의 coordinate-ring element로 읽을 수 있다.

## Basic picture

$$
\text{canonical basis }B
\;\longleftrightarrow\;
\text{dual canonical basis }B^*
\;\xrightarrow{\ \Psi\ }\;
A_q(\mathfrak n)
$$

Basis-level statement와 coordinate-ring-level statement는 $\Psi$를 통해 연결된다. 이 연결 때문에 quantum minors 같은 special elements를 basis language로 비교할 수 있다.

## Definition

$B^*$는 $U_q(\mathfrak n)$의 canonical basis $B$에 adjoint인 basis이다. 여기서 adjoint는 $U_q(\mathfrak n)$에 주어진 scalar product를 기준으로 한다.

GLS11은 $B^*$를 $\Psi$를 통해 $A_q(\mathfrak n)$ 안의 dual basis와 identify할 수 있다고 설명한다.

## Example

**source example.** Unipotent quantum minor $d_{u(\lambda),v(\lambda)}$는 source hypotheses가 만족될 때 $B^*$에 속한다. 이 family는 quantum minors가 dual canonical basis와 직접 만나는 기본 예시이다.

## Main facts

- $B^*$는 canonical basis $B$에 adjoint인 basis이다.
- $B^*$는 $\Psi$를 통해 $A_q(\mathfrak n)$의 dual basis와 연결된다.
- 특정 unipotent quantum minors는 $B^*$에 속한다.

## Why it matters

Dual canonical basis는 quantum coordinate ring 안의 special elements를 정규화된 basis language로 다루게 해 준다. Monoidal categorification이나 cluster algebra와 연결할 때도 module, Grothendieck class, quantum minor, basis element의 level을 구분하는 기준점이 된다.

## Connections

- [[topics/quantum-coordinate-rings|Quantum Coordinate Rings]]: $A_q(\mathfrak n)$와 $A_q(\mathfrak n(w))$에서 $B^*$와 quantum minors를 비교한다.
- [[topics/determinantial-modules|Determinantial Modules]]: determinantial modules와 quantum minors를 비교할 때 basis-level language를 제공한다.
- [[topics/monoidal-categorification|Monoidal Categorification]]: category 안의 object와 algebra side의 distinguished element를 분리해서 읽게 해 준다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/gls11-cluster-structures-quantum-coordinate-rings|GLS11]], Section 6.2 and Proposition 6.3: $B^*$ is the basis adjoint to $B$, and unipotent quantum minors satisfying the stated hypotheses belong to $B^*$.

</details>
