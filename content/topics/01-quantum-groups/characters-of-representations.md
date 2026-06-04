---
id: characters-of-representations
title: Characters of Representations
level: core
topic_kind: concept
parent_topics:
  - weight-modules
prerequisite_topics:
  - weight-modules
child_topics: []
related_topics:
  - demazure-crystals
  - crystal-bases
maturity: example-ready
---

## 개요

Character of a representation은 weight module에서 각 weight space의 dimension을 formal expression으로 모은 것이다. 즉 representation을 그대로 보존하지 않고, 어떤 weights가 어떤 multiplicity로 나타나는지만 남긴다.

이 notation은 [[topics/01-quantum-groups/weight-modules|Weight Modules]]를 읽은 뒤 바로 필요한 representation-theoretic bookkeeping이다. 이후 [[topics/01-quantum-groups/highest-weight-modules|Highest-Weight Modules]]의 weight distribution을 쓰거나, [[topics/02-crystal-bases/demazure-crystals|Demazure Crystals]]에서 Demazure character formula를 읽을 때 같은 언어가 반복된다.

## 준비와 notation

$P$를 weight lattice라고 하자. $U_q(\mathfrak g)$-module $V^q$가 weight module이면
$$
V^q=\bigoplus_{\mu\in P}V^q_\mu
$$
로 분해된다. 여기서
$$
V^q_\mu
=
\{v\in V^q\mid q^h v=q^{\langle h,\mu\rangle}v
\text{ for all }h\}
$$
이다.

각 $\mu\in P$에 대해 $e^\mu$는 weight $\mu$에 붙인 formal symbol이다. Character는 이 formal symbols의 linear combination으로 쓴다.

## 정의

Weight module $V^q$의 character는
$$
\operatorname{ch} V^q
=
\sum_{\mu\in P}(\dim V^q_\mu)e^\mu
$$
이다.

계수 $\dim V^q_\mu$는 weight $\mu$의 multiplicity이다. 따라서 character는 각 weight space의 dimension을 기록한다.

## 기본 예시

### 실제 예시: $U_q(\mathfrak{sl}_2)$의 $V(m)$

$m\in\mathbb Z_{\ge 0}$에 대해 Hong-Kang Example 4.2.6은 $V(m)$을 highest weight $m$을 갖는 $(m+1)$-dimensional irreducible $U_q(\mathfrak{sl}_2)$-module로 둔다. Section 4.3은 finite string의 vertices에 대해
$$
\operatorname{wt}(\overline{f^{(k)}u})=m-2k
\qquad (0\le k\le m)
$$
를 기록한다.

따라서 이 example의 weight pattern은
$$
m,\ m-2,\ m-4,\ldots,-m
$$
이다. 이 finite string에서는 각 weight가 한 번씩 나타나므로 character expression은
$$
\operatorname{ch} V(m)
=
e^m+e^{m-2}+e^{m-4}+\cdots+e^{-m}.
$$

검증: 논문 예시

## 핵심 관점

Character는 weight module을 다음 data로 압축한다.
$$
V^q
\longmapsto
\{\dim V^q_\mu\}_{\mu\in P}.
$$

이 data를 formal expression으로 쓰면 $\operatorname{ch}V^q$가 된다. 그래서 character는 weight labels와 multiplicities를 비교하기에는 좋지만, module action의 전체 구조를 담는 invariant는 아니다.

## 기본 성질

### 계수가 의미하는 것

- $V^q_\mu=0$이면 $e^\mu$의 coefficient는 $0$이다.
- $\dim V^q_\mu=n$이면 $\operatorname{ch}V^q$에서 $e^\mu$의 coefficient는 $n$이다.
- Character가 같은 두 modules는 같은 weight multiplicities를 갖지만, module structure가 같다는 결론은 character만으로는 나오지 않는다.

### $U_q(\mathfrak{sl}_2)$ finite string에서 보이는 형태

- $U_q(\mathfrak{sl}_2)$의 $V(m)$에서는 weights가 $m,m-2,\ldots,-m$로 나타난다.
- 이 finite string example에서 character는 각 vertex의 weight를 formal term으로 기록한다.

## 다른 topic들과의 관계

**Weight Modules.** [[topics/01-quantum-groups/weight-modules|Weight Modules]]는 character 정의에 필요한 weight space decomposition을 제공한다.

**Highest-Weight Modules.** [[topics/01-quantum-groups/highest-weight-modules|Highest-Weight Modules]]는 highest weight vector에서 생성되는 weight modules를 다룬다. 이런 modules의 character는 highest weight에서 시작하는 weight multiplicity data를 기록한다.

**Demazure Crystals.** [[topics/02-crystal-bases/demazure-crystals|Demazure Crystals]]에서는 Demazure crystal subsets와 Demazure character formulas가 연결된다.

**Crystal Bases.** [[topics/02-crystal-bases/crystal-bases|Crystal Bases]]는 representation의 weight data를 crystal-level combinatorics로 남긴다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/01-quantum-groups/weight-modules|Weight Modules]]
- 상위 개념: [[topics/01-quantum-groups/weight-modules|Weight Modules]]
- 다음에 읽을 것: [[topics/01-quantum-groups/highest-weight-modules|Highest-Weight Modules]]에서 highest weight에서 내려오는 weights를 보고, 그 다음 [[topics/02-crystal-bases/demazure-crystals|Demazure Crystals]]에서 character formula가 crystal subsets와 만나는 방식을 읽는다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/books/hong-kang02-introduction-quantum-groups-crystal-bases|Hong-Kang 2002]], Section 3.2, p.43: character notation for weight modules, written as \(\operatorname{ch}V^q=\sum_{\mu\in P}(\dim V^q_\mu)e^\mu\).
- Hong-Kang 2002, Example 4.2.6, pp.68-69, and Section 4.3, p.73: the finite-dimensional \(U_q(\mathfrak{sl}_2)\)-module \(V(m)\) and the weights \(m-2k\) in its finite string example.

</details>
