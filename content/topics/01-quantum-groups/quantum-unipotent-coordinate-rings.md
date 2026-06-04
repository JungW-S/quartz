---
id: quantum-unipotent-coordinate-rings
title: Quantum Unipotent Coordinate Rings
level: advanced
topic_kind: algebra
parent_topics:
  - quantum-coordinate-rings
prerequisite_topics:
  - quantum-coordinate-rings
child_topics:
  - pbw-parametrizations-of-quantum-unipotent-coordinate-rings
  - quantum-minors-and-frozen-variables
related_topics:
  - dual-canonical-bases
  - determinantial-modules
  - localized-crystals
maturity: definition-ready
---

## 개요

Quantum unipotent coordinate ring은 Weyl group element $w$에 붙는 coordinate-ring-level algebra $A_q(\mathfrak n(w))$이다. 이 object는 [[topics/01-quantum-groups/quantum-coordinate-rings|Quantum Coordinate Rings]]의 nilpotent part 안에서 만들어지며, $w$가 정하는 unipotent subgroup 방향을 quantum coordinate ring으로 읽게 해 준다.

이 topic이 필요한 이유는 $A_q(\mathfrak n(w))$가 여러 다른 층위의 공통 target으로 나타나기 때문이다. [[topics/04-cluster-algebras/quantum-cluster-algebras|Quantum Cluster Algebras]]에서는 cluster-algebra-level object와 비교되고, [[topics/05-monoidal-categorification/monoidal-categorification|Monoidal Categorification]]에서는 category에서 오는 Grothendieck ring과 비교된다. [[topics/08-localization-of-categories/localized-crystals|Localized Crystals]]와 [[topics/08-localization-of-categories/localized-pbw-parametrizations|Localized PBW Parametrizations]]를 읽을 때에도 이 coordinate-ring-level object가 배경이 된다.

## 준비와 notation

먼저 [[topics/01-quantum-groups/quantum-groups|Quantum Groups]]에서 $U_q(\mathfrak g)$와 nilpotent part $U_q(\mathfrak n)$를 사용한다. [[topics/01-quantum-groups/quantum-coordinate-rings|Quantum Coordinate Rings]]에서는 $U_q(\mathfrak n)$의 graded dual로 $A_q(\mathfrak n)$을 만들고, bilinear form에서 오는 algebra isomorphism
$$
\Psi:U_q(\mathfrak n)\longrightarrow A_q(\mathfrak n)
$$
을 고정한다.

$W$는 Weyl group이고 $w\in W$이다. $U_q(\mathfrak n(w))$는 $w$에 붙는 quantum unipotent subgroup 쪽 algebra이다. Reduced expression을 고르면 Lusztig quantum root vectors가 생기고, 이 root-vector construction이 $U_q(\mathfrak n(w))$를 만든다. Reduced-expression에 따른 PBW coordinate language는 [[topics/01-quantum-groups/pbw-parametrizations-of-quantum-unipotent-coordinate-rings|PBW Parametrizations of Quantum Unipotent Coordinate Rings]]에서 따로 다룬다.

## 정의

$w\in W$를 고정한다. $U_q(\mathfrak n(w))$는 $w$에 대응하는 Lusztig quantum root vectors로부터 $U_q(\mathfrak n)$ 안에 만들어지는 quantum unipotent subgroup algebra이다.

Quantum unipotent coordinate ring $A_q(\mathfrak n(w))$는 이 algebra를 $\Psi$로 coordinate-ring side에 보낸 image로 정의한다.
$$
A_q(\mathfrak n(w)):=\Psi\bigl(U_q(\mathfrak n(w))\bigr)
\subset A_q(\mathfrak n).
$$

따라서 $U_q(\mathfrak n(w))$는 enveloping-algebra side의 object이고, $A_q(\mathfrak n(w))$는 coordinate-ring side의 object이다. 두 object는 같은 정보를 다른 층위에서 표현하지만, 여기서는 coordinate-ring side인 $A_q(\mathfrak n(w))$를 중심으로 읽는다.

## 핵심 관점

핵심은 $w$가 먼저 quantum enveloping algebra 쪽 subalgebra를 고르고, 그 다음 $\Psi$가 그것을 coordinate-ring side로 옮긴다는 점이다.

$$
\begin{array}{ccc}
U_q(\mathfrak n) & \xrightarrow{\ \Psi\ } & A_q(\mathfrak n) \\
\cup & & \cup \\
U_q(\mathfrak n(w)) & \xrightarrow{\ \Psi\ } & A_q(\mathfrak n(w))
\end{array}
$$

이 diagram은 세 층위를 분리해서 읽게 해 준다. $U_q(\mathfrak n(w))$는 algebra-level construction이고, $A_q(\mathfrak n(w))$는 coordinate-ring-level target이며, $\mathcal C_w$에서 오는 quantum cluster algebra는 cluster-algebra-level realization이다.

## 기본 성질

### $A_q(\mathfrak n)$의 subalgebra

$A_q(\mathfrak n(w))$는 $A_q(\mathfrak n)$의 subalgebra이다. 이 성질 때문에 full nilpotent coordinate ring $A_q(\mathfrak n)$ 안에서 $w$가 정하는 부분만 따로 떼어 읽을 수 있다.

### $\Psi$를 통한 level 이동

$\Psi:U_q(\mathfrak n)\to A_q(\mathfrak n)$은 algebra isomorphism이고, $A_q(\mathfrak n(w))$는 $U_q(\mathfrak n(w))$의 image로 정의된다. 그래서 PBW basis, root-vector construction, canonical-basis comparison처럼 $U_q(\mathfrak n)$에서 만들어진 data를 coordinate-ring-level language로 옮겨 읽을 수 있다.

### Quantum cluster algebra와의 비교

$\mathcal C_w$에 붙는 quantum cluster algebra는 $A_q(\mathfrak n(w))$와 isomorphic하다. 이 비교는 cluster-algebra-level structure와 coordinate-ring-level object가 같은 algebra를 다른 언어로 나타낸다는 의미로 읽어야 한다.

### Quantum minors와 basis language

Unipotent quantum minors $d_{u(\lambda),v(\lambda)}$는 같은 nilpotent coordinate-ring framework에서 distinguished elements로 나타난다. 관련 hypotheses 아래에서 이 minors는 dual canonical basis $B^*$에 속한다. 이 사실은 [[topics/01-quantum-groups/dual-canonical-bases|Dual Canonical Bases]], [[topics/01-quantum-groups/quantum-minors-and-frozen-variables|Quantum Minors and Frozen Variables]], [[topics/06-quiver-hecke-klr-algebras/determinantial-modules|Determinantial Modules]]를 연결할 때 basis-level language와 coordinate-ring-level language를 함께 쓰게 한다.

## 다른 topic들과의 관계

[[topics/01-quantum-groups/quantum-coordinate-rings|Quantum Coordinate Rings]]는 상위 개념이다. 거기서는 $A_q(\mathfrak g)$, $A_q(\mathfrak n)$, $A_q(\mathfrak n(w))$가 어떤 coordinate-ring family에 속하는지 전체 그림을 잡는다.

[[topics/01-quantum-groups/pbw-parametrizations-of-quantum-unipotent-coordinate-rings|PBW Parametrizations of Quantum Unipotent Coordinate Rings]]는 $A_q(\mathfrak n(w))$를 reduced expression에서 오는 integer coordinates로 읽기 위한 다음 layer이다. 이 topic이 ambient coordinate ring을 고정하고, PBW topic이 그 안의 coordinate language를 분리해서 설명한다.

[[topics/01-quantum-groups/quantum-minors-and-frozen-variables|Quantum Minors and Frozen Variables]]는 coordinate-ring/basis language의 quantum minors와 cluster-seed language의 frozen variables를 분리해서 설명하는 child topic이다.

[[topics/04-cluster-algebras/quantum-cluster-algebras|Quantum Cluster Algebras]]는 $A_q(\mathfrak n(w))$와 비교되는 cluster-algebra-level structure를 제공한다. [[topics/05-monoidal-categorification/monoidal-categorification|Monoidal Categorification]]은 category-level simple objects와 tensor product가 Grothendieck ring을 통해 이 coordinate ring과 만나는 방식을 설명한다.

[[topics/08-localization-of-categories/localized-crystals|Localized Crystals]]는 $A_q(\mathfrak n(w))$를 frozen directions로 localize한 뒤, 그 basis elements를 crystal-level object로 읽는 쪽으로 넘어간다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/01-quantum-groups/quantum-groups|Quantum Groups]]에서 $U_q(\mathfrak g)$와 $U_q(\mathfrak n)$를 읽고, [[topics/01-quantum-groups/quantum-coordinate-rings|Quantum Coordinate Rings]]에서 $A_q(\mathfrak n)$와 $\Psi$를 읽는다.
- 상위 개념: [[topics/01-quantum-groups/quantum-coordinate-rings|Quantum Coordinate Rings]]가 full coordinate-ring setting을 제공한다.
- 다음에 읽을 것: [[topics/01-quantum-groups/pbw-parametrizations-of-quantum-unipotent-coordinate-rings|PBW Parametrizations of Quantum Unipotent Coordinate Rings]]에서 reduced-expression coordinates를 읽고, [[topics/01-quantum-groups/quantum-minors-and-frozen-variables|Quantum Minors and Frozen Variables]]에서 frozen directions로 이어지는 distinguished elements를 읽는다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/gls11-cluster-structures-quantum-coordinate-rings|GLS11]], Section 4.2 and Proposition 4.1: $A_q(\mathfrak n)$ as the graded dual of $U_q(\mathfrak n)$ and $\Psi:U_q(\mathfrak n)\to A_q(\mathfrak n)$ as an algebra isomorphism.
- GLS11, Sections 7.1-7.2: construction of $U_q(\mathfrak n(w))$ from Lusztig quantum root vectors and definition $A_q(\mathfrak n(w)):=\Psi(U_q(\mathfrak n(w)))$.
- GLS11, Theorem 12.3: identification of the quantum cluster algebra attached to $\mathcal C_w$ with $A_q(\mathfrak n(w))$.
- GLS11, Section 6.2 and Proposition 6.3: dual canonical basis context for unipotent quantum minors.

</details>
