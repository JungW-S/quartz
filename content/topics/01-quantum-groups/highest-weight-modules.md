---
id: highest-weight-modules
title: Highest-Weight Modules
level: core
topic_kind: object-family
parent_topics:
  - weight-modules
prerequisite_topics:
  - weight-modules
child_topics:
  - verma-modules
related_topics:
  - category-o
  - highest-weight-crystals
maturity: example-ready
---

## 개요

Highest-weight module은 하나의 highest weight vector가 module 전체를 생성하는 weight module이다. Quantum group representation에서 이 조건은 weight decomposition, raising generators의 annihilation 조건, 그리고 한 vector의 cyclic generation을 함께 묶는다.

이 topic은 [[topics/01-quantum-groups/weight-modules|Weight Modules]] 다음에 온다. 먼저 weight spaces와 maximal vector의 notation을 고정한 뒤, [[topics/01-quantum-groups/category-o|Quantum Category O]]와 [[topics/01-quantum-groups/verma-modules|Verma Modules]]에서 highest-weight representation을 category와 universal construction 안에서 더 자세히 다룬다.

## 준비와 notation

$U_q(\mathfrak g)$를 quantum group이라고 하자. Simple roots의 index set은 $I$로 쓰고, generators는
$$
e_i,\quad f_i,\quad q^h
\qquad (i\in I)
$$
로 쓴다.

$V^q$를 $U_q(\mathfrak g)$-module이라고 하자. Weight $\mu\in P$에 대한 weight space는
$$
V^q_\mu
=
\{v\in V^q\mid q^h v=q^{\langle h,\mu\rangle}v
\text{ for all }h\}
$$
이다. 이 notation은 [[topics/01-quantum-groups/weight-modules|Weight Modules]]와 같다.

Highest weight는 보통 $\lambda$로 쓰고, 해당 vector는
$$
v_\lambda\in V^q_\lambda
$$
로 쓴다.

## 정의

$U_q(\mathfrak g)$-weight module $V^q$가 highest weight $\lambda$의 highest-weight module이라는 것은 nonzero vector $v_\lambda\in V^q_\lambda$가 존재해서
$$
e_i v_\lambda=0
\qquad\text{for all }i\in I
$$
를 만족하고
$$
V^q=U_q(\mathfrak g)v_\lambda
$$
가 성립한다는 뜻이다.

이 vector $v_\lambda$를 highest weight vector라고 한다. Hong-Kang의 terminology에서 모든 $e_i$에 의해 killed되는 weight vector는 maximal vector이다.

## 기본 예시

### 실제 예시: $U_q(\mathfrak{sl}_2)$의 $V(m)$

$m\in\mathbb Z_{\ge 0}$에 대해 Hong-Kang Example 4.2.6은 $V(m)$을 highest weight $m$을 갖는 $(m+1)$-dimensional irreducible $U_q(\mathfrak{sl}_2)$-module로 둔다. Highest weight vector를 $u$라고 쓰면, 이 example에서 $u$는
$$
e u=0
$$
을 만족하는 highest weight vector이다.

$V(m)$은 irreducible이고 $u\ne 0$이므로 $u$가 생성하는 submodule은 $V(m)$ 전체이다.
$$
V(m)=U_q(\mathfrak{sl}_2)u.
$$

같은 example은 crystal lattice와 crystal basis를
$$
\mathcal L(m)=\bigoplus_{k=0}^m A_0 f^{(k)}u,
\qquad
\mathcal B(m)=\{\overline u,\overline{fu},\ldots,\overline{f^{(m)}u}\}
$$
로 둔다. 여기서 $A_0$는 $q=0$에서 regular한 rational functions의 local ring이다.

이 example에서 highest weight vector는 $u$이고, $f$의 divided powers $f^{(k)}u$가 crystal lattice의 generators로 나타난다.

검증: 문헌 예시

## 핵심 관점

Highest-weight module의 structure는 세 조건으로 묶인다.

- Weight decomposition: module은 weight spaces $V^q_\mu$로 분해된다.
- Highest condition: $v_\lambda$는 모든 raising generator $e_i$에 의해 annihilated된다.
- Generation condition: module 전체는 $v_\lambda$에서 $U_q(\mathfrak g)$의 action으로 생성된다.

따라서 highest-weight module은 일반 weight module보다 더 rigid한 object이다. Weight module은 여러 weight spaces의 direct sum structure만 요구하지만, highest-weight module은 그중 하나의 distinguished vector가 전체 module을 생성해야 한다.

## 기본 성질

### Highest weight vector의 조건

- $v_\lambda\in V^q_\lambda$이므로 $v_\lambda$의 weight는 $\lambda$이다.
- $e_i v_\lambda=0$ for all $i\in I$이므로 $v_\lambda$는 Hong-Kang의 maximal vector이다.

### Cyclic generation

- $V^q=U_q(\mathfrak g)v_\lambda$이므로 $V^q$는 $v_\lambda$가 생성하는 cyclic $U_q(\mathfrak g)$-module이다.

### $U_q(\mathfrak{sl}_2)$ finite example에서 보이는 형태

- $U_q(\mathfrak{sl}_2)$의 $V(m)$은 highest weight $m$을 갖는 finite-dimensional irreducible module이다.
- Hong-Kang의 crystal basis example에서 $\mathcal L(m)$은 $f^{(k)}u$로 생성되는 lattice이고, $\mathcal B(m)$은 그 quotient에서 얻는 finite crystal basis이다.

## 다른 topic들과의 관계

**Weight Modules.** [[topics/01-quantum-groups/weight-modules|Weight Modules]]는 weight spaces, maximal vectors, and characters의 기본 notation을 제공한다. Highest-weight module은 maximal vector가 module 전체를 생성하는 special case이다.

**Characters of Representations.** [[topics/01-quantum-groups/characters-of-representations|Characters of Representations]]는 highest-weight module의 weight multiplicities를 formal sum으로 기록하는 언어이다.

**Highest Weight Crystals.** [[topics/02-crystal-bases/highest-weight-crystals|Highest Weight Crystals]]는 highest-weight module의 crystal base에서 얻는 crystal-level object이다.

**Quantum Category O와 Verma Modules.** [[topics/01-quantum-groups/category-o|Quantum Category O]]와 [[topics/01-quantum-groups/verma-modules|Verma Modules]]는 highest-weight representation theory를 더 구조적인 category와 universal module construction으로 다루는 topics이다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/01-quantum-groups/weight-modules|Weight Modules]]
- 상위 개념: [[topics/01-quantum-groups/weight-modules|Weight Modules]]
- 다음에 읽을 것: [[topics/01-quantum-groups/characters-of-representations|Characters of Representations]], [[topics/02-crystal-bases/highest-weight-crystals|Highest Weight Crystals]], [[topics/01-quantum-groups/category-o|Quantum Category O]], [[topics/01-quantum-groups/verma-modules|Verma Modules]]

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/books/hong-kang02-introduction-quantum-groups-crystal-bases|Hong-Kang 2002]], Section 3.2, p.43: weight spaces, weight modules, weight vectors, maximal vectors, and characters for $U_q(\mathfrak g)$-modules.
- Hong-Kang 2002, Example 4.2.6, pp.68-69: the finite-dimensional irreducible $U_q(\mathfrak{sl}_2)$-module $V(m)$ with highest weight vector $u$, together with the lattice $\mathcal L(m)$ and crystal basis $\mathcal B(m)$.

</details>
