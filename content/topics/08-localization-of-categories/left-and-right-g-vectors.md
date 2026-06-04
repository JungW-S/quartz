---
id: left-and-right-g-vectors
title: Left and Right g-Vectors
level: advanced
topic_kind: concept
parent_topics:
  - localized-crystals
prerequisite_topics:
  - localized-crystals
  - quantum-cluster-algebras
  - determinantial-modules
  - localized-pbw-parametrizations
  - localized-string-parametrizations
child_topics: []
related_topics:
  - quantum-twist-automorphisms
maturity: definition-ready
---

## 개요

Left and right $g$-vectors는 localized crystal $\widetilde B(w)$의 elements를 cluster seed에 의존하는 coordinate language로 읽는 방법이다. [[topics/08-localization-of-categories/localized-pbw-parametrizations|Localized PBW Parametrizations]]와 [[topics/08-localization-of-categories/localized-string-parametrizations|Localized String Parametrizations]]가 PBW side와 string side의 좌표를 제공한다면, left/right $g$-vectors는 같은 elements를 seed-dependent degree data로 읽는다.

이름에 left와 right가 모두 들어가는 이유는 category-level에서 좌표를 읽는 방향이 두 가지이기 때문이다. [[topics/06-quiver-hecke-klr-algebras/determinantial-modules|Determinantial Modules]]에서 오는 seed objects를 simple object의 왼쪽에 convolution하는 방식과 오른쪽에 convolution하는 방식이 서로 다른 coordinate data를 만든다.

이 coordinate language는 [[topics/08-localization-of-categories/coordinate-formulas-for-quantum-twist-on-localized-crystals|Coordinate Formulas for Quantum Twist on Localized Crystals]]에서 PBW coordinates, string coordinates, $g$-vectors, quantum twist automorphism을 비교할 때 사용된다.

## 준비와 notation

먼저 [[topics/04-cluster-algebras/quantum-cluster-algebras|Quantum Cluster Algebras]]에서 seed-dependent degree language를 읽는다. 그다음 [[topics/06-quiver-hecke-klr-algebras/determinantial-modules|Determinantial Modules]]에서 category-level seed objects가 어디서 오는지 확인한다. Localized crystal input은 [[topics/08-localization-of-categories/localized-crystals|Localized Crystals]]에서 온다.

$w$는 Weyl group element이고, $\mathbf i$는 $w$의 reduced expression이다. 이 reduced expression은 quantum unipotent coordinate ring 쪽의 GLS seed와 quiver-Hecke category 쪽의 monomial seed를 고정한다.

$\widetilde B(w)$는 localized crystal이다. 이 coordinate language에서는 $\widetilde B(w)$의 element를 localized upper global basis element로 읽은 뒤, 그 basis element에 붙은 left/right $g$-vector data를 사용한다.

Notation은 다음처럼 읽는다.

- $\mathrm g^{\mathrm L}_{\mathbf i}$: chosen seed에 대한 left $g$-vector.
- $\mathrm g^{\mathrm R}_{\mathbf i}$: chosen seed에 대한 right $g$-vector.

여기서 $\mathbf i$가 표시되는 것은 이 data가 reduced expression, equivalently seed choice에 의존한다는 뜻이다.

## 정의

먼저 cluster-algebra level에서 $g$-vector가 무엇인지 고정한다. Seed의 index set을
$$
J=J_{\mathrm{ex}}\sqcup J_{\mathrm{fr}},
\qquad
n=|J_{\mathrm{ex}}|
$$
로 쓰자. Initial seed $t_0$를 고정하고, cluster variable $X_i(t)$를 $q^{1/2}\mapsto 1$로 specialize했을 때
$$
X_i(t)\big|_{q^{1/2}\mapsto 1}
=
X^{\widetilde g_i(t)}F(Y_1,\ldots,Y_n)
$$
로 쓰는 extended degree vector
$$
\widetilde g_i(t)\in\mathbb Z^J
$$
를 extended $g$-vector라고 한다. Exchangeable components만 남긴 vector가 $g$-vector이다.

이 cluster-theoretic language에서는 seed $t$에 degree lattice $D(t)$가 붙고, dominance order가
$$
\eta'\prec_t\eta
\quad\Longleftrightarrow\quad
\eta'=\eta+\widetilde B(t)v
\ \text{for some }0\ne v\in\mathbb N^{J_{\mathrm{ex}}}
$$
로 정의된다. Quantum torus $\mathcal T(t)$ 안의 element가 dominance order에 대해 유일한 leading term을 갖고 그 coefficient가 $1$이면 그 element는 pointed element이다. 이때 유일한 leading term의 degree가 그 element의 seed-dependent coordinate이다.

Localized crystal setting에서는 reduced expression $\mathbf i$가 GLS seed를 고정한다. $\mathrm g^{\mathrm L}_{\mathbf i}$와 $\mathrm g^{\mathrm R}_{\mathbf i}$는 이 seed에 대해 localized basis/simple-object data를 degree와 codegree 방향으로 읽는 두 coordinate maps이다. 여기서 left/right는 basic cluster algebra 안의 두 가지 mutation rule이 아니라, determinantial seed modules를 simple object의 왼쪽 또는 오른쪽에서 convolution하여 coordinate를 읽는 category-level distinction이다.

## 핵심 관점

핵심은 세 level을 구분하는 것이다.

1. Cluster-algebra level에서는 $g$-vector가 seed에 대한 degree/codegree data로 나타난다.
2. Category level에서는 determinantial seed modules를 어느 쪽에서 convolution하는지가 left/right distinction을 만든다.
3. Crystal level에서는 같은 data를 $\widetilde B(w)$의 elements 위에서 읽는다.

따라서 left/right $g$-vectors는 새로운 localized crystal을 만드는 construction이 아니다. 이미 있는 localized crystal을 cluster seed와 monoidal category가 제공하는 coordinate language로 읽는 방법이다.

## 기본 성질

### Seed dependence

Left/right $g$-vectors는 reduced expression $\mathbf i$가 정하는 seed에 의존한다. 같은 localized crystal element라도 seed를 바꾸면 coordinate data가 달라질 수 있다.

### Left-right distinction

Left $g$-vector와 right $g$-vector의 차이는 category-level에서 determinantial seed modules가 simple object의 왼쪽에 놓이는지, 오른쪽에 놓이는지에서 온다. 이 차이는 noncommutative monoidal category를 통해 좌표를 읽기 때문에 나타난다.

### Bridge to PBW and string coordinates

Left/right $g$-vectors는 localized PBW coordinates와 localized string coordinates를 quantum twist comparison과 연결하기 위한 중간 layer이다. 정확한 theorem-level comparison은 [[topics/08-localization-of-categories/coordinate-formulas-for-quantum-twist-on-localized-crystals|Coordinate Formulas for Quantum Twist on Localized Crystals]]에서 다룬다.

## 다른 topic들과의 관계

[[topics/04-cluster-algebras/quantum-cluster-algebras|Quantum Cluster Algebras]]는 seed, frozen variables, $g$-vector language가 나오는 cluster-algebra side의 배경이다.

[[topics/06-quiver-hecke-klr-algebras/determinantial-modules|Determinantial Modules]]는 category-level seed objects가 어디서 오는지 설명한다. Left/right distinction은 이 determinantial seed modules와 simple objects의 convolution 방향에서 나타난다.

[[topics/08-localization-of-categories/localized-crystals|Localized Crystals]]는 $\widetilde B(w)$ 자체를 제공한다. Left/right $g$-vectors는 그 crystal의 elements를 seed-dependent coordinate data로 읽는다.

[[topics/08-localization-of-categories/localized-pbw-parametrizations|Localized PBW Parametrizations]]와 [[topics/08-localization-of-categories/localized-string-parametrizations|Localized String Parametrizations]]는 같은 localized crystal을 다른 coordinate language로 읽는 companion topics이다.

[[topics/08-localization-of-categories/quantum-twist-automorphisms|Quantum Twist Automorphisms]]와 [[topics/08-localization-of-categories/coordinate-formulas-for-quantum-twist-on-localized-crystals|Coordinate Formulas for Quantum Twist on Localized Crystals]]는 left/right $g$-vectors가 실제로 쓰이는 다음 단계이다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/04-cluster-algebras/quantum-cluster-algebras|Quantum Cluster Algebras]], [[topics/06-quiver-hecke-klr-algebras/determinantial-modules|Determinantial Modules]], [[topics/08-localization-of-categories/localized-crystals|Localized Crystals]], [[topics/08-localization-of-categories/localized-pbw-parametrizations|Localized PBW Parametrizations]], [[topics/08-localization-of-categories/localized-string-parametrizations|Localized String Parametrizations]].
- 상위 개념: [[topics/08-localization-of-categories/localized-crystals|Localized Crystals]].
- 다음에 읽을 것: [[topics/08-localization-of-categories/coordinate-formulas-for-quantum-twist-on-localized-crystals|Coordinate Formulas for Quantum Twist on Localized Crystals]].

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/qin17-triangular-bases-quantum-cluster-algebras|Qin17]], Section 2.1, pp.9-10: extended \(g\)-vector and \(g\)-vector language for cluster variables.
- Qin17, Definition 3.1.1, p.13: dominance order on \(D(t)\).
- Qin17, Definitions 3.1.4 and 3.1.5, pp.14-15: pointed elements and pointed sets.
- [[sources/papers/jp25-crystals-quantum-twist-automorphisms|JP25]], local TeX lines 1335-1388 and 1687-1776: the left/right localized-crystal \(g\)-vector setting, the GLS seed fixed by \(\mathbf i\), and the degree/codegree reading used later in coordinate formulas.

The JP25 theorem formulas, comparison matrices, and type \(A_2\) coordinate example are not used on this page.

</details>
