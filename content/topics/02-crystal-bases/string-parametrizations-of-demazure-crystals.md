---
id: string-parametrizations-of-demazure-crystals
title: String Parametrizations of Demazure Crystals
level: core
topic_kind: concept
parent_topics:
  - crystal-bases
  - demazure-crystals
prerequisite_topics:
  - abstract-crystals
  - b-infinity-crystal
  - demazure-crystals
child_topics: []
related_topics:
  - localized-string-parametrizations
  - localized-pbw-parametrizations
maturity: definition-ready
---

## 개요

String parametrization은 reduced expression을 하나 고정한 뒤, Demazure-type crystal의 원소를 Kashiwara operators와 $\varepsilon_i$ functions가 만드는 coordinate tuple로 기록하는 방법이다. 이 topic에서는 localization을 하지 않은 ordinary crystal-level construction만 다룬다.

이 construction이 필요한 이유는 [[topics/08-localization-of-categories/localized-string-parametrizations|Localized String Parametrizations]]에서 ordinary string coordinates를 먼저 만든 뒤 frozen directions를 더하기 때문이다. 따라서 localized string 좌표를 읽기 전에, ordinary crystal 안에서 string coordinates가 어떤 data를 추출하는지 분리해서 알아야 한다.

## 준비와 notation

먼저 [[topics/02-crystal-bases/abstract-crystals|Abstract Crystals]]에서 $\widetilde e_i$, $\widetilde f_i$, $\varepsilon_i$, $\varphi_i$를 읽고, [[topics/02-crystal-bases/b-infinity-crystal|The Crystal B(infinity)]]와 [[topics/02-crystal-bases/demazure-crystals|Demazure Crystals]]에서 $w$가 정하는 ordinary crystal subset을 읽는다.

$w$는 Weyl group element이고,
$$
\mathbf i=(i_1,\ldots,i_m)\in R(w)
$$
는 $w$의 reduced expression이다. 이 reduced expression은 string coordinates를 뽑는 simple-root directions의 순서를 고정한다.

$B(w)$는 $B(\infty)$ 안의 $w$-indexed ordinary crystal subset으로 쓴다. 이 notation은 localized crystal $\mathcal B(w)$가 아니라 localization 이전의 crystal-level object를 가리킨다.

## 정의

$b\in B(w)$를 고정한다. String coordinate
$$
\operatorname{STR}_{\mathbf i}(b)=(t_1,\ldots,t_m)
$$
는 다음 recursion으로 정의된다.

먼저
$$
t_1=\varepsilon_{i_1}(b)
$$
로 둔다. 그 다음 $k\ge2$에 대해
$$
t_k
=
\varepsilon_{i_k}
\bigl(
\widetilde e_{i_{k-1}}^{t_{k-1}}
\cdots
\widetilde e_{i_1}^{t_1}(b)
\bigr)
$$
로 둔다.

즉 먼저 $i_1$-direction에서 올라갈 수 있는 최대 길이를 기록하고, 그만큼 $\widetilde e_{i_1}$를 적용한 뒤, 다음 direction $i_2$에서 다시 같은 과정을 반복한다. 이 과정을 reduced expression의 순서대로 끝까지 진행하여 integer tuple을 얻는다.

Image set은
$$
\mathcal S_{\mathbf i}(w)
=
\{\operatorname{STR}_{\mathbf i}(b)\mid b\in B(w)\}
$$
로 쓴다. String parametrization은 $B(w)$의 원소를 이 coordinate tuple language로 읽는 방법이다.

## 핵심 관점

String coordinate는 crystal graph 전체를 한 번에 그리는 대신, 한 원소 $b$에서 시작해 reduced expression이 지시하는 directions를 차례로 따라가며 숫자를 뽑는다.

각 숫자 $t_k$는 그 단계에서 $\widetilde e_{i_k}$를 얼마나 적용할 수 있는지를 기록한다. 따라서 tuple $(t_1,\ldots,t_m)$는 $b$가 chosen reduced expression의 simple-root directions에 대해 어디에 놓이는지를 나타내는 coordinate data이다.

이 관점은 localized string parametrization의 ordinary part가 된다. Localization에서는 여기에 frozen elements가 만드는 integer directions를 더하지만, ordinary string coordinate 자체는 먼저 $B(w)$ 위에서 정의된다.

## 기본 성질

### Reduced-expression dependence

String coordinates는 $\mathbf i$를 고정해야 정의된다. 같은 $w$에 대해 다른 reduced expression을 선택하면 coordinate extraction의 순서가 달라지므로, 같은 crystal element도 다른 tuple로 표현될 수 있다.

### Crystal-level construction

이 construction은 module-level이나 category-level 정의가 아니다. 입력은 ordinary crystal element $b\in B(w)$이고, 사용하는 operations는 crystal-level maps $\widetilde e_i$와 functions $\varepsilon_i$이다.

### Localized version의 ordinary input

[[topics/08-localization-of-categories/localized-string-parametrizations|Localized String Parametrizations]]는 이 ordinary coordinate map을 $B(w)$에서 시작한 뒤, frozen crystal elements가 만드는 fixed directions를 더해 $\mathcal B(w)$로 확장한다.

## 다른 topic들과의 관계

[[topics/02-crystal-bases/abstract-crystals|Abstract Crystals]]는 $\widetilde e_i$와 $\varepsilon_i$의 의미를 제공한다. String coordinate의 recursion은 이 notation 없이는 읽을 수 없다.

[[topics/02-crystal-bases/demazure-crystals|Demazure Crystals]]는 $w$가 crystal 안에서 어떤 subset을 선택하는지 설명한다. String parametrization은 그런 $w$-indexed subset을 coordinate tuple로 읽는 방법이다.

[[topics/08-localization-of-categories/localized-string-parametrizations|Localized String Parametrizations]]는 이 ordinary coordinate construction에 frozen directions를 더해 localized crystal $\mathcal B(w)$까지 확장한다.

[[topics/08-localization-of-categories/localized-pbw-parametrizations|Localized PBW Parametrizations]]는 같은 localized crystal을 PBW-coordinate language로 읽는 companion construction이다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/02-crystal-bases/abstract-crystals|Abstract Crystals]], [[topics/02-crystal-bases/b-infinity-crystal|The Crystal B(infinity)]], [[topics/02-crystal-bases/demazure-crystals|Demazure Crystals]].
- 상위 개념: [[topics/02-crystal-bases/crystal-bases|Crystal Bases]], [[topics/02-crystal-bases/demazure-crystals|Demazure Crystals]].
- 다음에 읽을 것: [[topics/08-localization-of-categories/localized-string-parametrizations|Localized String Parametrizations]].

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/jp25-crystals-quantum-twist-automorphisms|Jung-Park 2025]], local TeX lines 1600-1608: recursive string-coordinate definition on $B(w)$ and the image set $\mathcal S_{\mathbf i}(w)$.
- [[sources/papers/jp25-crystals-quantum-twist-automorphisms|Jung-Park 2025]], local TeX lines 1611-1625: the source records the resulting map as the string parametrization of $B(w)$. The proof is not used here.
- Review report: `reports/reviews/2026-06-04-ordinary-string-parametrization-prerequisite-review.md`.

</details>
