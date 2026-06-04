---
id: quantum-minors-and-frozen-variables
title: Quantum Minors and Frozen Variables
level: advanced
topic_kind: concept
parent_topics:
  - quantum-unipotent-coordinate-rings
prerequisite_topics:
  - quantum-unipotent-coordinate-rings
  - dual-canonical-bases
  - quantum-cluster-algebras
child_topics: []
related_topics:
  - determinantial-modules
  - quantum-cluster-algebras
  - localized-crystals
maturity: definition-ready
---

## 개요

Quantum minor는 quantum coordinate ring 안에서 특별한 matrix coefficient처럼 쓰이는 distinguished element이다. 이 path에서 주로 쓰는 것은 unipotent quantum minor이며, notation은 $D_{u(\lambda),v(\lambda)}$ 또는 $\Psi^{-1}$로 옮긴 $d_{u(\lambda),v(\lambda)}$로 나타난다.

Frozen variable은 cluster-algebra-level 용어이다. Quantum seed 안의 variables 중 mutation direction으로 쓰지 않는 variables가 frozen variables이다. 따라서 quantum minor와 frozen variable은 같은 level의 object가 아니다. Quantum minor는 coordinate-ring/basis language에 속하고, frozen variable은 cluster-algebra seed에서의 역할을 가리킨다.

이 구분이 필요한 이유는 [[topics/01-quantum-groups/quantum-unipotent-coordinate-rings|Quantum Unipotent Coordinate Rings]]가 [[topics/04-cluster-algebras/quantum-cluster-algebras|Quantum Cluster Algebras]], [[topics/06-quiver-hecke-klr-algebras/determinantial-modules|Determinantial Modules]], [[topics/08-localization-of-categories/localized-crystals|Localized Crystals]]와 만날 때 두 language가 동시에 나타나기 때문이다.

## 준비와 notation

먼저 [[topics/01-quantum-groups/quantum-unipotent-coordinate-rings|Quantum Unipotent Coordinate Rings]]에서 $A_q(\mathfrak n)$, $A_q(\mathfrak n(w))$, 그리고 algebra isomorphism
$$
\Psi:U_q(\mathfrak n)\longrightarrow A_q(\mathfrak n)
$$
을 읽는다. [[topics/01-quantum-groups/dual-canonical-bases|Dual Canonical Bases]]에서는 $U_q(\mathfrak n)$의 canonical basis $B$와 dual canonical basis $B^*$를 읽는다.

Quantum cluster algebra 쪽에서는 quantum seed
$$
S=(\{x_i\}_{i\in J},L,\widetilde B)
$$
를 사용한다. Index set은
$$
J=J_{\mathrm{ex}}\sqcup J_{\mathrm{fr}}
$$
로 나뉜다. $J_{\mathrm{ex}}$는 mutation directions이고, $J_{\mathrm{fr}}$는 frozen variables의 index set이다.

## 정의

### Unipotent quantum minor

$\lambda\in P_+$이고 $u,v\in W$가 $u(\lambda)-v(\lambda)\in Q_+$를 만족한다고 하자. Unipotent quantum minor $D_{u(\lambda),v(\lambda)}$는 $A_q(\mathfrak n)$ 쪽의 coordinate-ring element이다.

이 element를 $\Psi$를 통해 $U_q(\mathfrak n)$ 쪽으로 옮긴 것을
$$
d_{u(\lambda),v(\lambda)}
:=
\Psi^{-1}\bigl(D_{u(\lambda),v(\lambda)}\bigr)
$$
로 쓴다. Equivalently, $d_{u(\lambda),v(\lambda)}$는
$$
D_{u(\lambda),v(\lambda)}(x)
=
\bigl(d_{u(\lambda),v(\lambda)},x\bigr)
\qquad
(x\in U_q(\mathfrak n))
$$
를 만족하는 $U_q(\mathfrak n)$의 element이다.

### Frozen variable

Quantum seed $S=(\{x_i\}_{i\in J},L,\widetilde B)$에서 $i\in J_{\mathrm{fr}}$에 대응하는 variable $x_i$를 frozen variable이라고 부른다. Mutation은 $J_{\mathrm{ex}}$ 방향에서만 일어난다. 따라서 frozen variable은 seed 안에 남아 있지만 mutation direction으로 쓰이지 않는 variable이다.

Coordinate-ring comparison을 할 때에는 quantum cluster algebra의 variables가 $A_q(\mathfrak n(w))$ 안의 elements와 비교된다. 이때 frozen variable이라는 말은 그 element가 cluster seed에서 수행하는 역할을 가리키며, quantum minor라는 말은 coordinate-ring/basis 쪽의 distinguished element family를 가리킨다.

## 핵심 관점

이 topic의 핵심은 level을 분리해서 읽는 것이다.

$$
\begin{array}{ccc}
\text{basis-level} &:& B^*,\ d_{u(\lambda),v(\lambda)} \\
\text{coordinate-ring-level} &:& A_q(\mathfrak n),\ A_q(\mathfrak n(w)),\ D_{u(\lambda),v(\lambda)} \\
\text{cluster-algebra-level} &:& \text{cluster variables and frozen variables}
\end{array}
$$

Unipotent quantum minor는 dual canonical basis와 만나는 coordinate-ring element이다. Frozen variable은 cluster seed에서 mutation하지 않는 variable이다. Monoidal categorification과 localization에서는 이 두 language가 같은 algebra를 서로 다른 방식으로 설명하기 때문에 함께 나타난다.

## 기본 성질

### Dual canonical basis와의 관계

관련 hypotheses 아래에서 $d_{u(\lambda),v(\lambda)}$는 dual canonical basis $B^*$에 속한다. 이 성질은 unipotent quantum minors를 단순한 coordinate-ring elements가 아니라 distinguished basis elements로 읽게 해 준다.

### Quantum cluster algebra와의 관계

$\mathcal C_w$에 붙은 quantum cluster algebra는 $A_q(\mathfrak n(w))$와 isomorphic하다. 따라서 quantum cluster variables와 frozen variables는 이 비교를 통해 quantum unipotent coordinate ring 쪽 language와 만난다.

### Frozen variable은 mutation direction이 아니다

Frozen variable은 cluster 안에 포함되지만 mutation direction으로 선택되지 않는다. Localization이나 localized crystal 쪽에서 frozen directions가 등장할 때에는, 이 cluster-algebra-level 역할과 coordinate-ring-level elements를 구분해서 읽어야 한다.

## 다른 topic들과의 관계

[[topics/01-quantum-groups/quantum-unipotent-coordinate-rings|Quantum Unipotent Coordinate Rings]]는 $A_q(\mathfrak n(w))$라는 ambient coordinate-ring object를 제공한다. Quantum minors는 이 coordinate-ring language 안에서 distinguished elements로 등장한다.

[[topics/01-quantum-groups/dual-canonical-bases|Dual Canonical Bases]]는 $B^*$를 제공한다. Unipotent quantum minors가 $B^*$에 속한다는 사실 때문에, quantum minor language는 basis-level language와 직접 연결된다.

[[topics/04-cluster-algebras/quantum-cluster-algebras|Quantum Cluster Algebras]]는 frozen variable이라는 seed-level language를 제공한다. 이 topic에서는 frozen variable을 coordinate-ring element의 이름으로 쓰지 않고, cluster seed에서의 역할로 읽는다.

[[topics/06-quiver-hecke-klr-algebras/determinantial-modules|Determinantial Modules]]는 module-category side에서 quantum-minor language와 만나는 object-level topic이다. 여기서는 module 자체, Grothendieck-ring class, coordinate-ring element를 같은 것으로 취급하지 않도록 level을 분리해야 한다.

[[topics/08-localization-of-categories/localized-crystals|Localized Crystals]]와 [[topics/08-localization-of-categories/localized-pbw-parametrizations|Localized PBW Parametrizations]]에서는 frozen directions를 invert하거나 좌표화한다. 이 topic은 그 전에 quantum minor와 frozen variable이라는 두 이름이 서로 다른 level에서 나온다는 점을 고정한다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/01-quantum-groups/quantum-unipotent-coordinate-rings|Quantum Unipotent Coordinate Rings]], [[topics/01-quantum-groups/dual-canonical-bases|Dual Canonical Bases]], [[topics/04-cluster-algebras/quantum-cluster-algebras|Quantum Cluster Algebras]].
- 상위 개념: [[topics/01-quantum-groups/quantum-unipotent-coordinate-rings|Quantum Unipotent Coordinate Rings]]가 coordinate-ring setting을 제공한다.
- 다음에 읽을 것: [[topics/06-quiver-hecke-klr-algebras/determinantial-modules|Determinantial Modules]]에서 module side와 quantum-minor language의 접점을 읽고, [[topics/08-localization-of-categories/localized-crystals|Localized Crystals]]와 [[topics/08-localization-of-categories/localized-pbw-parametrizations|Localized PBW Parametrizations]]에서 frozen directions가 localized setting으로 넘어가는 방식을 읽는다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/gls11-cluster-structures-quantum-coordinate-rings|GLS11]], Section 6.2: definition of the dual canonical basis \(B^*\).
- GLS11, Section 6.5 and Proposition 6.3: unipotent quantum minors \(D_{u(\lambda),v(\lambda)}\), their \(\Psi^{-1}\)-images \(d_{u(\lambda),v(\lambda)}\), and containment in \(B^*\) under the stated hypotheses.
- GLS11, Theorem 12.3: identification of the quantum cluster algebra attached to \(\mathcal C_w\) with \(A_q(\mathfrak n(w))\).
- General seed/frozen-variable vocabulary is used through the prerequisite page [[topics/04-cluster-algebras/quantum-cluster-algebras|Quantum Cluster Algebras]].

</details>
