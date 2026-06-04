---
id: localized-string-parametrizations
title: Localized String Parametrizations
level: advanced
topic_kind: concept
parent_topics:
  - localized-crystals
prerequisite_topics:
  - localized-crystals
  - abstract-crystals
  - string-parametrizations-of-demazure-crystals
child_topics: []
related_topics:
  - localized-pbw-parametrizations
  - left-and-right-g-vectors
maturity: definition-ready
---

## 개요

Localized string parametrization은 localized crystal $\mathcal B(w)$의 elements를 string-coordinate language로 기록하는 방법이다. 이 construction은 [[topics/08-localization-of-categories/localized-crystals|Localized Crystals]]에서 만든 localized crystal을 새로 정의하지 않고, Kashiwara operators가 주는 string-coordinate side에서 읽는다.

이 topic을 읽으려면 ordinary crystal notation, ordinary string parametrization, localized crystal construction 순서가 필요하다. [[topics/08-localization-of-categories/localized-pbw-parametrizations|Localized PBW Parametrizations]]는 필수 선행 topic이라기보다 같은 localized crystal을 PBW-coordinate language로 읽는 companion topic이다.

PBW coordinates, string coordinates, $g$-vectors, quantum twist automorphism 사이의 관계를 비교하려면 먼저 localized crystal의 string-coordinate description이 분리되어 있어야 한다.

## 준비와 notation

먼저 [[topics/02-crystal-bases/abstract-crystals|Abstract Crystals]]에서 Kashiwara operators와 $\varepsilon_i$ functions를 읽는다. 그다음 [[topics/02-crystal-bases/string-parametrizations-of-demazure-crystals|String Parametrizations of Demazure Crystals]]에서 localization 이전의 ordinary string coordinates를 고정한다. Localized crystal input은 [[topics/08-localization-of-categories/localized-crystals|Localized Crystals]]에서 온다.

$w$는 Weyl group element이고, $\mathbf i$는 $w$의 reduced expression이다. 이 reduced expression을 고정해야 string-coordinate language가 정해진다.

$B(w)$는 [[topics/02-crystal-bases/b-infinity-crystal|The Crystal B(infinity)]] 안에 놓이는 Demazure-type crystal이고, $\mathcal B(w)$는 [[topics/08-localization-of-categories/localized-crystals|Localized Crystals]]에서 frozen crystal elements를 invert해 얻는 localized crystal이다.

Ordinary string coordinates는 먼저 $B(w)$의 element에 대해 정의된다. 이 좌표는 [[topics/02-crystal-bases/string-parametrizations-of-demazure-crystals|String Parametrizations of Demazure Crystals]]에서처럼 reduced expression의 simple directions를 따라 Kashiwara operators와 $\varepsilon_i$ functions가 주는 string data를 차례로 기록하는 방식으로 읽는다.

Localized string coordinates는 이 ordinary string data에 frozen crystal elements가 만드는 fixed string directions를 더해 $\mathcal B(w)$의 elements까지 확장한다.

## 정의

Reduced expression
$$
\mathbf i=(i_1,\ldots,i_m)\in R(w)
$$
를 고정한다. \(b\in B(w)\)에 대해 string coordinate
$$
\operatorname{STR}_{\mathbf i}(b)=(t_k)_{k\in[1,m]}
$$
는 다음 재귀식으로 정의된다.
$$
t_k
=
\varepsilon_{i_k}
\bigl(
\widetilde e_{i_{k-1}}^{t_{k-1}}
\cdots
\widetilde e_{i_2}^{t_2}
\widetilde e_{i_1}^{t_1}(b)
\bigr)
\qquad
(k\in[1,m]).
$$
이때 \(k=1\)에서는 앞의 \(\widetilde e\)-product가 없으므로 \(t_1=\varepsilon_{i_1}(b)\)로 읽는다.

Image set을
$$
\mathcal S_{\mathbf i}(w)
=
\{\operatorname{STR}_{\mathbf i}(b)\mid b\in B(w)\}
$$
라고 둔다. 이 재귀 과정은
$$
\widetilde e_{i_m}^{t_m}
\cdots
\widetilde e_{i_2}^{t_2}
\widetilde e_{i_1}^{t_1}(b)
=
\mathbf 1
$$
에 도달하고, map
$$
\operatorname{STR}_{\mathbf i}:B(w)\to\mathcal S_{\mathbf i}(w)
$$
은 bijective이다.

각 \(j\in I\)에 대해 frozen crystal element를 \(z_j\)라고 쓰고
$$
S_j:=\operatorname{STR}_{\mathbf i}(z_j)
$$
로 둔다. \(S_j=(t_k)_{k\in[1,m]}\)의 components는
$$
t_k
=
\left\langle
h_{i_k},
s_{i_{k+1}}\cdots s_{i_m}\Lambda_j
\right\rangle
\qquad
(k\in[1,m])
$$
로 주어진다.

이제 localized crystal element를
$$
x=b\cdot\prod_{i\in I}z_i^{a_i}
\qquad
(b\in B(w),\ a_i\in\mathbb Z)
$$
꼴로 쓴다. Localized string coordinate는
$$
\operatorname{STR}_{\mathbf i}(x)
=
\operatorname{STR}_{\mathbf i}(b)+\sum_{i\in I}a_iS_i
\in
\mathbb Z^{[1,m]}
$$
로 정의된다. 이 값은 \(x\)를 위처럼 표현하는 방법에 의존하지 않는다.

Localized string parameter set은
$$
\widetilde{\mathcal S}_{\mathbf i}(w)
:=
\mathcal S_{\mathbf i}(w)+\sum_{k\in I}\mathbb ZS_k
\subset
\mathbb Z^{[1,m]}
$$
이고, localized string parametrization은 bijection
$$
\operatorname{STR}_{\mathbf i}:
\mathcal B(w)
\xrightarrow{\sim}
\widetilde{\mathcal S}_{\mathbf i}(w)
$$
이다.

## 핵심 관점

읽는 순서는 다음과 같다.

1. $B(w)$의 element를 ordinary string coordinates로 읽는다.
2. Frozen crystal elements가 string-coordinate space 안에서 만드는 fixed directions를 기록한다.
3. $\mathcal B(w)$의 element를 ordinary string part와 frozen-direction shifts가 합쳐진 coordinate data로 읽는다.

따라서 localized string parametrization은 새로운 crystal structure가 아니다. 이미 만들어진 localized crystal $\mathcal B(w)$를 chosen reduced expression에 의존하는 string-coordinate system으로 읽는 방법이다.

## 기본 성질

### Reduced-expression dependence

String coordinates는 reduced expression $\mathbf i$를 고정한 뒤 정해진다. 따라서 같은 localized crystal element라도 reduced expression을 바꾸면 좌표 표현이 달라질 수 있다.

### Ordinary-to-localized extension

Ordinary string coordinates는 $B(w)$에서 시작한다. Localized string coordinates는 frozen crystal elements가 만드는 directions를 더해서 $\mathcal B(w)$의 localized elements까지 다룬다.

### Frozen string directions

Localization에서는 frozen elements를 invert한다. String-coordinate language에서는 이 invert된 frozen elements가 fixed integer directions로 나타나며, localized elements는 ordinary string part에 이런 direction shifts를 더한 형태로 읽힌다.

### Coordinate formulas와의 경계

Localized string parametrization은 PBW/string comparison, $g$-vectors, quantum twist formulas의 입력이다. 그 coordinate formulas 자체는 [[topics/08-localization-of-categories/left-and-right-g-vectors|Left and Right g-Vectors]]와 [[topics/08-localization-of-categories/coordinate-formulas-for-quantum-twist-on-localized-crystals|Coordinate Formulas for Quantum Twist on Localized Crystals]]에서 다룬다.

## 다른 topic들과의 관계

[[topics/08-localization-of-categories/localized-crystals|Localized Crystals]]는 $\mathcal B(w)$ 자체를 제공한다. Localized string parametrization은 그 crystal을 string-coordinate language로 읽는 방법이다.

[[topics/02-crystal-bases/abstract-crystals|Abstract Crystals]]는 Kashiwara operators, $\varepsilon_i$, $\varphi_i$, weight function 같은 ordinary crystal notation을 제공한다.

[[topics/02-crystal-bases/string-parametrizations-of-demazure-crystals|String Parametrizations of Demazure Crystals]]는 localization 이전의 ordinary string-coordinate map을 제공한다.

[[topics/08-localization-of-categories/localized-pbw-parametrizations|Localized PBW Parametrizations]]는 같은 localized crystal을 PBW-coordinate language로 읽는 companion topic이다. Localized string parametrization의 정의에 필요하다기보다, 나중에 coordinate formulas를 비교할 때 함께 놓인다.

[[topics/08-localization-of-categories/left-and-right-g-vectors|Left and Right g-Vectors]]는 localized PBW coordinates와 localized string coordinates가 quantum twist formulas와 만나는 다음 coordinate layer이다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/02-crystal-bases/abstract-crystals|Abstract Crystals]], [[topics/02-crystal-bases/string-parametrizations-of-demazure-crystals|String Parametrizations of Demazure Crystals]], [[topics/08-localization-of-categories/localized-crystals|Localized Crystals]].
- 상위 개념: [[topics/08-localization-of-categories/localized-crystals|Localized Crystals]].
- 다음에 읽을 것: [[topics/08-localization-of-categories/localized-pbw-parametrizations|Localized PBW Parametrizations]], [[topics/08-localization-of-categories/left-and-right-g-vectors|Left and Right g-Vectors]], [[topics/08-localization-of-categories/coordinate-formulas-for-quantum-twist-on-localized-crystals|Coordinate Formulas for Quantum Twist on Localized Crystals]].

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/jp25-crystals-quantum-twist-automorphisms|Jung-Park 2025]], local TeX lines 1600-1675: recursive string-coordinate definition on \(B(w)\), bijectivity on \(B(w)\), frozen string directions, extension to \(\mathcal B(w)\), and the localized string parameter set.
- Review report: `reports/reviews/2026-06-04-localized-string-parametrizations-source-location-review.md`.
- String bijectivity lemma proof and the PBW-string bridge \(\psi_{\mathbf i}\) are deferred to formula-level topics.

</details>
