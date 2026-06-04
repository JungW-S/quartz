---
id: demazure-crystals
title: Demazure Crystals
level: core
topic_kind: object-family
parent_topics:
  - crystal-bases
  - b-infinity-crystal
prerequisite_topics:
  - highest-weight-crystals
  - b-infinity-crystal
child_topics:
  - string-parametrizations-of-demazure-crystals
related_topics:
  - cellular-crystals
  - demazure-subcategories-of-quiver-hecke-modules
maturity: example-ready
---

## 개요

Demazure crystal은 highest weight crystal $B(\lambda)$ 또는 negative-half crystal $B(\infty)$ 안에서 Weyl group element $w$가 정하는 distinguished subset이다. 이 subset은 Demazure module을 crystal-level에서 추적하기 위해 나타난다.

중요한 점은 Demazure crystal이 완전히 새로운 ambient crystal이 아니라는 것이다. 먼저 $B(\lambda)$나 $B(\infty)$가 있고, 그 안에서 Weyl group element $w$가 선택하는 부분을
$$
B_w(\lambda),
\qquad
B_w(\infty)
$$
처럼 표시한다.

이 topic은 [[topics/02-crystal-bases/cellular-crystals|Cellular Crystals]]와 [[topics/06-quiver-hecke-klr-algebras/demazure-subcategories-of-quiver-hecke-modules|Demazure Subcategories of Quiver-Hecke Modules]]를 읽기 전에 필요하다. 두 topic 모두 $B_w(\infty)$ 쪽 crystal-level 조건을 category-level 또는 coordinate-level object와 비교한다.

## 준비와 notation

$W$를 Weyl group이라고 하고, $s_i$를 simple reflection이라고 하자. $W$ 위의 순서는 Bruhat order로 쓴다. 조건 $s_iw<w$는 왼쪽에서 $s_i$를 곱하면 $w$의 length가 줄어드는 상황을 나타낸다.

$\lambda\in P_+$에 대해 $B(\lambda)$는 [[topics/02-crystal-bases/highest-weight-crystals|highest weight crystal]]이고, $u_\lambda$는 그 highest-weight element이다. $B(\infty)$는 [[topics/02-crystal-bases/b-infinity-crystal|The Crystal B(infinity)]]에서 다루는 negative-half crystal이며, weight $0$의 distinguished element를 $u_\infty$로 쓴다.

여기서는 lower global basis element를
$$
G_\lambda(b)\qquad (b\in B(\lambda))
$$
로 표시한다. 즉 $b$는 crystal element이고, $G_\lambda(b)$는 module 안의 대응하는 global-basis element이다. $B(\infty)$ 쪽 global-basis element는 $G(b)$로 쓴다.

Root operators는 ordinary crystal notation을 따른다.
$$
\widetilde e_i,\widetilde f_i.
$$

## 정의

$\lambda\in P_+$와 $w\in W$를 고정하자. $V(\lambda)$를 highest weight $\lambda$의 irreducible module이라고 하고, $u_{w\lambda}$를 weight $w\lambda$의 lower global basis element라고 하자. Demazure module은
$$
V_w(\lambda)
=
U_q^+(\mathfrak g)\,u_{w\lambda}
$$
로 둔다.

Demazure crystal $B_w(\lambda)$는 $B(\lambda)$의 subset으로, 이 Demazure module을 global-basis elements로 전개했을 때 나타나는 labels이다. 즉
$$
V_w(\lambda)
=
\bigoplus_{b\in B_w(\lambda)}
\mathbb Q(q)\,G_\lambda(b)
$$
를 만족하는 subset
$$
B_w(\lambda)\subset B(\lambda)
$$
을 $w$에 대응하는 Demazure crystal이라고 부른다.

또한 $s_iw<w$이면
$$
B_w(\lambda)
=
\{\widetilde f_i^k b
\mid
b\in B_{s_iw}(\lambda),\ k\ge 0,\ \widetilde f_i^k b\ne 0\}
$$
로 기술된다.

$B(\infty)$ 쪽 Demazure crystal은 다음 recursion으로 정해지는 unique subsets
$$
B_w(\infty)\subset B(\infty)
$$
이다. 먼저 identity element $1\in W$에 대해서는
$$
B_1(\infty)=\{u_\infty\}.
$$
그리고 $s_iw<w$이면
$$
B_w(\infty)
=
\{\widetilde f_i^k b
\mid
b\in B_{s_iw}(\infty),\ k\ge 0,\ \widetilde f_i^k b\ne 0\}.
$$

같은 방식으로 $B_w(\lambda)$도 reduced expression을 따라 $\widetilde f_i$를 반복 적용하여 기술된다. 따라서 Demazure crystal은 Weyl group element의 combinatorics와 crystal root operators가 만나는 지점이다.

## 기본 예시

### 실제 예시: simple reflection case

$w=s_i$라고 하자. 그러면 $s_iw=1<w$이므로 recursion을 한 번만 적용하면 된다.

$B(\infty)$ 쪽에서는
$$
B_{s_i}(\infty)
=
\{\widetilde f_i^k u_\infty
\mid
k\ge 0,\ \widetilde f_i^k u_\infty\ne 0\}
$$
이다. 즉 identity case의 한 점
$$
B_1(\infty)=\{u_\infty\}
$$
에서 시작해, $i$-direction으로 $\widetilde f_i$를 가능한 만큼 적용한 string이 $B_{s_i}(\infty)$가 된다.

Highest weight crystal 쪽에서도 같은 방식으로
$$
B_{s_i}(\lambda)
=
\{\widetilde f_i^k u_\lambda
\mid
k\ge 0,\ \widetilde f_i^k u_\lambda\ne 0\}
$$
라고 읽을 수 있다. 여기서는 ambient crystal이 $B(\lambda)$이므로 string이 $B(\lambda)$ 안에서 끝날 수 있다.

검증: 논문 예시

## 핵심 관점

핵심 그림은 다음과 같다.

$$
V_w(\lambda)
\quad\longleftrightarrow\quad
B_w(\lambda)\subset B(\lambda),
$$
$$
w
\quad\longmapsto\quad
B_w(\infty)\subset B(\infty).
$$

왼쪽은 module-level object이고, 오른쪽은 crystal-level subset이다. Demazure crystal은 module 안의 Demazure part를 crystal graph 안에서 보이게 만드는 장치이다.

Recursion은 $w$를 한 simple reflection씩 줄이는 방식으로 작동한다. $s_iw<w$이면 먼저 length가 더 작은 $B_{s_iw}(\infty)$를 알고 있다고 보고, 거기에 $\widetilde f_i$를 가능한 만큼 적용해 $B_w(\infty)$를 만든다.

따라서 Demazure crystal을 읽을 때는 두 가지를 구분해야 한다. $B_w(\lambda)$는 highest weight crystal 안의 subset이고, $B_w(\infty)$는 negative-half crystal 안의 subset이다. 두 notation은 서로 관련되어 있지만, ambient crystal이 다르다.

## 기본 성질

### Demazure module을 crystal subset으로 읽기

$B_w(\lambda)$는 Demazure module $V_w(\lambda)$를 global basis로 전개했을 때 정확히 나타나는 crystal labels이다. 따라서 $B_w(\lambda)$는 module-level Demazure construction을 crystal-level subset으로 옮긴 것이다.

### Identity에서 시작하는 recursion

$B_w(\infty)$는 $B_1(\infty)=\{u_\infty\}$에서 시작해, $s_iw<w$일 때 $\widetilde f_i$를 반복 적용하는 recursion으로 정해진다. 이 recursion은 Demazure crystal을 reduced expression과 crystal operators로 계산할 수 있게 한다.

### Raising operators에 대한 안정성

Demazure crystal subsets는 raising operators에 대해 안정적인 방향을 가진다. 즉
$$
\widetilde e_i B_w(\lambda)\subset B_w(\lambda)\cup\{0\},
\qquad
\widetilde e_i B_w(\infty)\subset B_w(\infty)\cup\{0\}
$$
형태의 안정성이 나타난다.

### Bruhat order와 포함 관계

Bruhat order에서 $w'\le w$이면 작은 쪽의 Demazure piece는 큰 쪽의 Demazure piece 안에 들어간다. 이 성질은 $w$가 커질수록 더 큰 crystal subset을 얻는다는 그림을 준다.

### $i$-string 안에서 가능한 형태

$B(\infty)$의 한 $i$-string $S$가 highest-weight vector를 가지면,
$$
B_w(\infty)\cap S
$$
는 세 가지 형태 중 하나이다.

- 비어 있다.
- $S$ 전체이다.
- $S$의 highest-weight vector 하나만이다.

같은 종류의 statement가 $B(\lambda)$ 안의 $i$-strings에 대해서도 성립한다. 이 성질은 Demazure subset이 crystal graph의 colored strings 안에서 아무렇게나 잘리는 것이 아니라, 매우 제한된 방식으로 놓인다는 뜻이다.

## 다른 topic들과의 관계

**Highest Weight Crystals.** [[topics/02-crystal-bases/highest-weight-crystals|Highest Weight Crystals]]는 $B_w(\lambda)\subset B(\lambda)$의 ambient crystal을 제공한다.

**The Crystal $B(\infty)$.** [[topics/02-crystal-bases/b-infinity-crystal|The Crystal B(infinity)]]는 $B_w(\infty)\subset B(\infty)$의 ambient crystal을 제공한다.

**String Parametrizations of Demazure Crystals.** [[topics/02-crystal-bases/string-parametrizations-of-demazure-crystals|String Parametrizations of Demazure Crystals]]는 Demazure-type crystal의 원소를 reduced expression에 따른 coordinate tuple로 읽는 다음 단계이다.

**Cellular Crystals.** [[topics/02-crystal-bases/cellular-crystals|Cellular Crystals]]는 reduced expression에서 만든 coordinate model이다. Demazure crystals는 $w$와 root operators가 만드는 ordinary crystal-side prerequisite이다.

**Demazure Subcategories of Quiver-Hecke Modules.** [[topics/06-quiver-hecke-klr-algebras/demazure-subcategories-of-quiver-hecke-modules|Demazure Subcategories of Quiver-Hecke Modules]]는 $B_w(\infty)$를 quiver-Hecke module category의 simple objects로 실현하는 category-level topic이다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/02-crystal-bases/highest-weight-crystals|Highest Weight Crystals]]에서 $B(\lambda)$와 $u_\lambda$를 읽고, [[topics/02-crystal-bases/b-infinity-crystal|The Crystal B(infinity)]]에서 $B(\infty)$와 $u_\infty$를 읽는다.
- 상위 개념: [[topics/02-crystal-bases/crystal-bases|Crystal Bases]]는 Demazure crystals가 사용하는 ordinary crystal language를 제공한다.
- 다음에 읽을 것: [[topics/02-crystal-bases/string-parametrizations-of-demazure-crystals|String Parametrizations of Demazure Crystals]]에서 ordinary coordinate extraction을 읽고, [[topics/02-crystal-bases/cellular-crystals|Cellular Crystals]]에서 reduced-expression coordinate model을 읽고, [[topics/06-quiver-hecke-klr-algebras/demazure-subcategories-of-quiver-hecke-modules|Demazure Subcategories of Quiver-Hecke Modules]]에서 $B_w(\infty)$의 category-level realization을 읽는다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/kashiwara93-crystal-base-demazure-character-formula|Kashiwara 1993]], Section 3.2, pp.853-854: Demazure module $V_w(\lambda)=U_q^+(\mathfrak g)u_{w\lambda}$ and the global-basis setup.
- Kashiwara 1993, Proposition 3.2.3, p.854: subset $B_w(\lambda)\subset B(\lambda)$, the global-basis decomposition of $V_w(\lambda)$, raising-operator stability, and recursive description when $s_iw<w$.
- Kashiwara 1993, Propositions 3.2.3 and 3.2.5, pp.854-855: the simple-reflection examples obtained by applying the recursion to $w=s_i$.
- Kashiwara 1993, Proposition 3.2.5, pp.854-855: unique subsets $B_w(\infty)\subset B(\infty)$, the initial condition $B_1(\infty)=\{u_\infty\}$, recursive construction, raising-operator stability, and Bruhat-order containment.
- Kashiwara 1993, Theorem 3.3.2 and Propositions 3.3.4-3.3.5, pp.855-856: controlled $i$-string behavior for $B_w(\infty)$ and $B_w(\lambda)$.

</details>
