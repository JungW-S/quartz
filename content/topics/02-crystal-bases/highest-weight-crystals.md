---
id: highest-weight-crystals
title: Highest Weight Crystals
level: core
topic_kind: object-family
parent_topics:
  - crystal-bases
prerequisite_topics:
  - abstract-crystals
  - tensor-products-of-crystals
  - quantum-groups
child_topics: []
related_topics:
  - b-infinity-crystal
maturity: example-ready
---

## 개요

Highest weight crystal은 highest weight module 자체가 아니라, 그 module의 crystal base에서 얻는 crystal-level object이다. Dominant weight $\lambda$에 대해 보통
$$
B(\lambda)
$$
라고 쓰며, 이 crystal에는 weight $\lambda$를 갖는 distinguished highest-weight element가 있다.

이 family는 [[topics/02-crystal-bases/abstract-crystals|Abstract Crystals]]의 axioms가 실제 representation-theoretic object에서 어떻게 나타나는지 보여 주는 첫 표준 family이다. 수학적 level로는 module 자체가 아니라, simple highest-weight module의 crystal base에서 얻는 crystal-level object를 다룬다.

Highest weight crystals가 필요한 이유는 이후 [[topics/02-crystal-bases/b-infinity-crystal|The Crystal B(infinity)]]와 [[topics/02-crystal-bases/demazure-crystals|Demazure Crystals]]를 읽을 때 기준점이 되기 때문이다. $B(\lambda)$는 highest weight representation에서 출발하는 표준 crystal이고, Demazure crystal은 이런 highest-weight crystal 또는 $B(\infty)$ 안의 distinguished part를 추적한다.

## 준비와 notation

$P_+$를 dominant weights의 set이라고 하자. $\lambda\in P_+$에 대해 $V(\lambda)$는 highest weight $\lambda$를 갖는 simple highest-weight module을 나타내는 notation으로 쓴다.

여기서 다루는 crystal은
$$
B(\lambda)
$$
이다. 이 notation에서 $B(\lambda)$는 highest weight $\lambda$를 갖는 simple module의 crystal base에 붙는 normal crystal이다. 그 안의 weight $\lambda$인 unique element는
$$
u_\lambda
$$
로 쓴다.

Root operators와 string functions는 [[topics/02-crystal-bases/abstract-crystals|Abstract Crystals]]의 notation을 따른다.
$$
\widetilde e_i,\widetilde f_i,
\qquad
\varepsilon_i,\varphi_i.
$$

## 정의

$\lambda\in P_+$에 대해 highest weight crystal $B(\lambda)$는 highest weight $\lambda$를 갖는 simple module의 crystal base에서 얻는 normal crystal이다. 이 crystal에서 weight $\lambda$인 unique element를
$$
u_\lambda\in B(\lambda)
$$
라고 쓴다.

따라서 $B(\lambda)$는 abstract crystal의 모든 data
$$
\operatorname{wt},\quad
\varepsilon_i,\quad
\varphi_i,\quad
\widetilde e_i,\quad
\widetilde f_i
$$
를 갖는다. 차이는 이 data가 임의로 주어진 것이 아니라, highest weight simple module의 crystal base에서 온다는 점이다.

## 기본 예시

### 실제 예시: $U_q(\mathfrak{sl}_2)$의 finite string

$m\in\mathbb Z_{\ge 0}$에 대해 $V(m)$을 highest weight $m$을 갖는 $(m+1)$-dimensional irreducible $U_q(\mathfrak{sl}_2)$-module이라고 하자. Highest weight vector를 $u$라고 쓰면 Hong-Kang의 Example 4.2.6은
$$
\mathcal L(m)=\bigoplus_{k=0}^m A_0 f^{(k)}u,
\qquad
\mathcal B(m)=\{\overline u,\overline{fu},\ldots,\overline{f^{(m)}u}\}
$$
를 crystal basis로 둔다. 여기서 $A_0$는 $q=0$에서 regular한 rational functions의 local ring이고, $\overline{x}$는 $x$의 image를 quotient $\mathcal L(m)/q\mathcal L(m)$에서 본 것이다.

이 crystal graph는 finite line이다.
$$
\overline u\longrightarrow \overline{fu}\longrightarrow
\overline{f^{(2)}u}\longrightarrow\cdots\longrightarrow
\overline{f^{(m)}u}.
$$

이 finite string에서는 각 vertex에 대해
$$
\operatorname{wt}(\overline{f^{(k)}u})=m-2k,
\qquad
\varepsilon(\overline{f^{(k)}u})=k,
\qquad
\varphi(\overline{f^{(k)}u})=m-k
$$
가 된다고 기록한다. 따라서 $\overline u$는 top vertex이고, $\widetilde f$를 반복하면 finite string을 따라 내려간다.

검증: 논문 예시

## 핵심 관점

$B(\lambda)$는 abstract crystal axioms에 representation-theoretic origin을 부여한다. Abstract crystal에서는 vertex와 arrows만 보지만, highest weight crystal에서는 그 vertex들이 highest weight module의 crystal basis에서 온다.

가장 단순한 그림은 one-color finite string이다. $U_q(\mathfrak{sl}_2)$의 $V(m)$에서 top vertex $\overline u$에서 출발해 $\widetilde f$를 반복하면
$$
\overline u,\ \overline{fu},\ \overline{f^{(2)}u},\ldots,\overline{f^{(m)}u}
$$
를 지나고, string 끝에서 더 내려갈 수 없다.

이 관점에서 $\varepsilon$와 $\varphi$는 finite string 안에서 위치를 세는 함수로 보인다. $\varepsilon$는 위로 올라갈 수 있는 횟수이고, $\varphi$는 아래로 내려갈 수 있는 횟수이다.

## 기본 성질

### Highest-weight vertex

$B(\lambda)$에는 weight $\lambda$인 unique element $u_\lambda$가 있다. 이 element는 highest-weight module의 highest weight를 crystal-level에서 나타내는 vertex이다.

### Normal crystal structure

$B(\lambda)$는 normal crystal이다. Normality는 $\varepsilon_i$와 $\varphi_i$가 root operators를 최대로 몇 번 적용할 수 있는지를 기록한다는 뜻이다.

### Trivial highest weight case

$B(0)$는 one-element crystal $C$와 isomorphic하다. 즉 highest weight가 $0$인 경우에는 crystal graph가 하나의 vertex만 갖는다.

## 다른 topic들과의 관계

**Abstract Crystals.** [[topics/02-crystal-bases/abstract-crystals|Abstract Crystals]]는 $B(\lambda)$가 만족해야 하는 crystal axioms를 제공한다.

**Tensor Products of Crystals.** [[topics/02-crystal-bases/tensor-products-of-crystals|Tensor Products of Crystals]]는 highest weight crystals를 다른 crystals와 결합할 때 필요한 convention을 제공한다.

**Quantum Groups.** [[topics/01-quantum-groups/quantum-groups|Quantum Groups]]는 $V(\lambda)$와 $U_q(\mathfrak g)$가 무엇인지 설명하는 representation-theoretic 배경이다.

**The Crystal $B(\infty)$.** [[topics/02-crystal-bases/b-infinity-crystal|The Crystal B(infinity)]]는 highest weight module 하나가 아니라 negative half $U_q^-(\mathfrak g)$ 쪽에서 나오는 crystal이다.

**Demazure Crystals.** [[topics/02-crystal-bases/demazure-crystals|Demazure Crystals]]는 $B(\lambda)$ 또는 $B(\infty)$ 안에서 Weyl group element에 의해 선택되는 부분을 추적한다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/02-crystal-bases/abstract-crystals|Abstract Crystals]]에서 crystal axioms를 읽고, [[topics/01-quantum-groups/quantum-groups|Quantum Groups]]에서 highest weight module이 나오는 배경을 읽는다.
- 상위 개념: [[topics/02-crystal-bases/crystal-bases|Crystal Bases]]는 highest weight crystals가 crystal base theory 안에서 어떤 역할을 하는지 설명한다.
- 다음에 읽을 것: [[topics/02-crystal-bases/b-infinity-crystal|The Crystal B(infinity)]]에서 negative-half crystal을 읽고, [[topics/02-crystal-bases/demazure-crystals|Demazure Crystals]]에서 Weyl group element가 정하는 subcrystal을 읽는다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/kashiwara93-crystal-base-demazure-character-formula|Kashiwara 1993]], Example 1.2.7, p.843: $B(\lambda)$ as the normal crystal associated with the crystal base of the simple module with highest weight $\lambda$, and the notation $u_\lambda$.
- Kashiwara 1993, Example 1.2.7, p.843: $B(0)\simeq C$.
- [[sources/books/hong-kang02-introduction-quantum-groups-crystal-bases|Hong-Kang 2002]], Example 4.2.6, pp.68-69: the finite-dimensional $U_q(\mathfrak{sl}_2)$ module $V(m)$, the lattice $\mathcal L(m)$, the crystal basis $\mathcal B(m)$, and the finite line graph.
- Hong-Kang 2002, Section 4.3, p.73: the weight, $\varepsilon$, and $\varphi$ values on $\mathcal B(m)$.

</details>
