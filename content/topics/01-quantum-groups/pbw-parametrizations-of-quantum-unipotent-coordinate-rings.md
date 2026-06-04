---
id: pbw-parametrizations-of-quantum-unipotent-coordinate-rings
title: PBW Parametrizations of Quantum Unipotent Coordinate Rings
level: advanced
topic_kind: concept
parent_topics:
  - quantum-unipotent-coordinate-rings
prerequisite_topics:
  - quantum-groups
  - quantum-unipotent-coordinate-rings
  - dual-canonical-bases
child_topics: []
related_topics:
  - localized-pbw-parametrizations
  - quantum-minors-and-frozen-variables
maturity: definition-ready
---

## 개요

PBW parametrization은 reduced expression을 하나 고정했을 때, quantum group의 positive part에 있는 PBW-type monomial basis와 canonical basis elements를 integer coordinate data로 비교하는 방법이다. 이 topic은 [[topics/08-localization-of-categories/localized-pbw-parametrizations|Localized PBW Parametrizations]]를 읽기 전에 ordinary PBW coordinates가 무엇을 기록하는지 설명한다.

이 construction이 나타나는 이유는 quantum unipotent coordinate ring 쪽의 distinguished basis elements를 좌표로 읽어야 하기 때문이다. Reduced expression은 ordered root-vector factors를 정하고, exponent vector는 그 ordered product에서 각 factor가 몇 번 쓰이는지를 기록한다.

## 준비와 notation

[[topics/01-quantum-groups/quantum-groups|Quantum Groups]]에서 \(U_q(\mathfrak g)\)와 positive part \(U^+\)를 사용한다. \(W\)는 Weyl group이고, \(w\in W\)에 대해
$$
w=s_{i_1}\cdots s_{i_n}
$$
은 reduced expression이다.

Lusztig의 notation에서는 braid-group symmetry를 적용해 \(E_{i_k}\)에서 ordered positive factors를 만든다. 이 factors를 divided powers로 올리고, exponent vector
$$
c=(c_1,\ldots,c_n)\in\mathbb N^n
$$
를 넣어 ordered monomial을 만든다.

Coordinate-ring side에서는 [[topics/01-quantum-groups/quantum-unipotent-coordinate-rings|Quantum Unipotent Coordinate Rings]]와 [[topics/01-quantum-groups/dual-canonical-bases|Dual Canonical Bases]]를 함께 읽어야 한다. PBW basis는 algebra-level object이고, localized crystal에서 쓰이는 \(G^{\mathrm{up}}(b)\)는 basis element를 coordinate-ring side에서 읽는 notation이다.

## 정의

Reduced expression \(w=s_{i_1}\cdots s_{i_n}\)을 고정한다. \(T'_{i,e}\)는 Lusztig braid-group symmetry이고 \(e=\pm1\)은 convention choice이다. 각 \(k\)에 대해 ordered positive factor는
$$
E_{\mathbf i,k}
=
T'_{i_1,e}\cdots T'_{i_{k-1},e}(E_{i_k})
\in U^+
$$
로 주어진다. 여기서 \(k=1\)이면 앞의 braid-group symmetry product는 비어 있는 product로 본다.

Exponent vector \(c=(c_1,\ldots,c_n)\in\mathbb N^n\)에 대해 PBW-type element는 divided-power product
$$
E_{\mathbf i}^{(c)}
=
E_{\mathbf i,1}^{(c_1)}
E_{\mathbf i,2}^{(c_2)}
\cdots
E_{\mathbf i,n}^{(c_n)}
$$
이다. 이 elements가 \(c\in\mathbb N^n\)로 indexed된 basis를 이루는 subspace를 \(U^+(w,e)\)라고 쓴다. \(U^+(w,e)\)는 \(w\)와 \(e\)에 의해 정해지고, reduced expression을 바꾸면 basis coordinates는 달라질 수 있지만 subspace 자체는 바뀌지 않는다.

Integral form 위에서도 같은 construction은 \(A\)-basis를 준다. 그 integral PBW-type element는 canonical basis element 하나를 \(v^{-1}\)-adic leading term으로 결정한다.

따라서 이 topic에서 말하는 PBW parametrization은 다음 data를 묶은 것이다.

- reduced expression \(w=s_{i_1}\cdots s_{i_n}\);
- 그 reduced expression에서 생기는 ordered PBW factors;
- exponent vector \(c\in\mathbb N^n\);
- PBW-type element와 canonical-basis element를 leading congruence로 비교하는 correspondence.

## 기본 예시

## 핵심 관점

$$
\text{reduced expression}
\longrightarrow
\text{ordered PBW factors}
\longrightarrow
c\in\mathbb N^n
\longrightarrow
\text{canonical-basis label}
$$

이 순서가 핵심이다. Reduced expression은 coordinate axes를 고르고, exponent vector \(c\)는 그 axes에 대한 integer coordinates를 준다. Canonical basis와의 관계는 PBW monomial 자체를 canonical basis라고 말하는 것이 아니라, integral PBW element가 canonical-basis element를 leading congruence로 고른다는 방식으로 나타난다.

## 기본 성질

### Reduced expression gives ordered factors

Reduced expression에서 나오는 successive braid transforms는 \(U^+\) 안에 놓인다. 이 사실이 ordered PBW factors를 positive part 안에서 다룰 수 있게 한다.

### PBW basis for \(U^+(w,e)\)

Exponent vector \(c\in\mathbb N^n\)로 indexed된 ordered monomials는 \(U^+(w,e)\)의 basis를 이룬다. Reduced expression을 바꾸면 coordinates는 달라질 수 있지만, subspace \(U^+(w,e)\)는 \(w\)에 의해 정해진다.

### Integral form compatibility

PBW-type basis는 integral form에서도 \(A\)-basis로 작동한다. 이 단계가 canonical basis와 비교할 수 있는 integral framework를 제공한다.

### Canonical-basis comparison

Integral PBW-type element는 unique canonical-basis element를 modulo \(v^{-1}\)로 결정한다. 따라서 PBW coordinates는 canonical basis를 reduced-expression coordinate data로 읽는 방법을 제공한다.

## 다른 topic들과의 관계

[[topics/01-quantum-groups/quantum-unipotent-coordinate-rings|Quantum Unipotent Coordinate Rings]]는 PBW basis와 dual PBW basis가 coordinate-ring side에서 쓰이는 ambient object를 제공한다.

[[topics/01-quantum-groups/dual-canonical-bases|Dual Canonical Bases]]는 canonical basis와 coordinate-ring basis가 만나는 basis-level language를 제공한다. PBW parametrization은 reduced-expression coordinate data를 이 basis language와 비교한다.

[[topics/08-localization-of-categories/localized-pbw-parametrizations|Localized PBW Parametrizations]]는 ordinary PBW coordinates에 frozen directions를 더해 localized crystal \(\mathcal B(w)\)까지 확장한다.

[[topics/01-quantum-groups/quantum-minors-and-frozen-variables|Quantum Minors and Frozen Variables]]는 localized PBW coordinates에서 frozen directions가 어디서 오는지 설명해야 하는 다음 prerequisite이다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/01-quantum-groups/quantum-groups|Quantum Groups]], [[topics/01-quantum-groups/quantum-unipotent-coordinate-rings|Quantum Unipotent Coordinate Rings]], [[topics/01-quantum-groups/dual-canonical-bases|Dual Canonical Bases]].
- 상위 개념: [[topics/01-quantum-groups/quantum-unipotent-coordinate-rings|Quantum Unipotent Coordinate Rings]].
- 다음에 읽을 것: [[topics/08-localization-of-categories/localized-pbw-parametrizations|Localized PBW Parametrizations]], [[topics/01-quantum-groups/quantum-minors-and-frozen-variables|Quantum Minors and Frozen Variables]].

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/books/lusztig94-introduction-quantum-groups|Lusztig 1994]], Chapter 40, Proposition 40.1.3 and Proposition 40.2.1: reduced-expression root-vector factors and PBW-type bases of \(U^+(w,e)\).
- [[sources/books/lusztig94-introduction-quantum-groups|Lusztig 1994]], Chapter 41, Proposition 41.1.4 and Proposition 41.1.6: integral PBW basis and canonical-basis congruence.
- [[sources/papers/gls11-cluster-structures-quantum-coordinate-rings|GLS11]], Sections 7.1-7.2: quantum unipotent coordinate-ring and dual PBW-basis context.
- The local Lusztig book PDF is not staged as a public asset.

</details>
