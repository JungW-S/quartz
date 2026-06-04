---
id: localized-pbw-parametrizations
title: Localized PBW Parametrizations
level: advanced
topic_kind: concept
parent_topics:
  - localized-crystals
prerequisite_topics:
  - localized-crystals
  - b-infinity-crystal
  - quantum-unipotent-coordinate-rings
  - quantum-minors-and-frozen-variables
  - pbw-parametrizations-of-quantum-unipotent-coordinate-rings
child_topics: []
related_topics:
  - localized-string-parametrizations
  - left-and-right-g-vectors
maturity: definition-ready
---

## 개요

Localized PBW parametrization은 localized crystal $\mathcal B(w)$의 elements를 PBW-coordinate language로 기록하는 방법이다. 이 topic은 [[topics/08-localization-of-categories/localized-crystals|Localized Crystals]]에서 만든 object를 새로 정의하지 않고, 이미 주어진 localized crystal을 좌표로 읽는다.

이 topic을 읽으려면 ordinary PBW coordinates와 quantum minors and frozen variables를 먼저 고정한 뒤 localized crystals로 넘어간다. Ordinary PBW parametrization은 $B(w)$의 elements를 nonnegative coordinate data로 기록한다. Localized PBW parametrization은 여기에 frozen crystal elements가 만드는 integer directions를 더해 $\mathcal B(w)$의 elements를 기록한다.

따라서 이 construction은 coordinate-ring-level PBW language와 crystal-level localization을 연결한다. Ordinary PBW theory 자체는 [[topics/01-quantum-groups/pbw-parametrizations-of-quantum-unipotent-coordinate-rings|PBW Parametrizations of Quantum Unipotent Coordinate Rings]]에서 읽고, frozen variables의 의미는 [[topics/01-quantum-groups/quantum-minors-and-frozen-variables|Quantum Minors and Frozen Variables]]에서 먼저 고정한다.

## 준비와 notation

먼저 [[topics/02-crystal-bases/b-infinity-crystal|The Crystal B(infinity)]]에서 $B(\infty)$와 $B(w)$가 들어가는 ambient crystal을 읽는다. 그다음 [[topics/01-quantum-groups/quantum-unipotent-coordinate-rings|Quantum Unipotent Coordinate Rings]]와 [[topics/01-quantum-groups/quantum-minors-and-frozen-variables|Quantum Minors and Frozen Variables]]에서 coordinate-ring side의 terminology를 고정한다.

Ordinary coordinate input은 [[topics/01-quantum-groups/pbw-parametrizations-of-quantum-unipotent-coordinate-rings|PBW Parametrizations of Quantum Unipotent Coordinate Rings]]에서 온다. Localized crystal input은 [[topics/08-localization-of-categories/localized-crystals|Localized Crystals]]에서 온다.

$w$는 Weyl group element이고, $\mathbf i$는 $w$의 reduced expression이다. Localized PBW parametrization은 이 reduced expression을 고정한 뒤 정의된다.

$B(w)$는 $B(\infty)$ 안의 subcrystal이고, $\mathcal B(w)$는 $B(w)$에 frozen crystal elements를 invert하여 얻는 localized crystal이다.

[[topics/01-quantum-groups/pbw-parametrizations-of-quantum-unipotent-coordinate-rings|Ordinary PBW parametrization]]은 먼저 $B(w)$ 위에서 쓰인다. Localized PBW parametrization은 이 ordinary PBW data에 frozen directions가 만드는 integer shifts를 더해 $\mathcal B(w)$까지 확장한다.

## 정의

Reduced expression
$$
\mathbf i=(i_1,\ldots,i_m)\in R(w)
$$
를 고정한다. 먼저 \(b\in B(w)\)에 대해 ordinary PBW coordinate를
$$
\operatorname{PBW}_{\mathbf i}(b)
:=
\operatorname{PBW}_{\mathbf i}\bigl(G^{\mathrm{up}}(b)\bigr)
$$
로 쓴다. 그 image를
$$
\mathcal P_{\mathbf i}(w)
=
\{\operatorname{PBW}_{\mathbf i}(b)\mid b\in B(w)\}
\subset
\mathbb Z_{\ge0}^{[1,m]}
$$
라고 둔다. Ordinary PBW parametrization input은 다음 map이다.
$$
\operatorname{PBW}_{\mathbf i}:B(w)\to\mathcal P_{\mathbf i}(w)
$$

각 \(j\in I\)에 대해 frozen crystal element를 \(z_j\)라고 쓰고
$$
P_j:=\operatorname{PBW}_{\mathbf i}(z_j)
$$
로 둔다. 이 convention에서 이 vector는
$$
P_j=(a_t)_{t\in[1,m]},
\qquad
a_t=\delta_{i_t,j}
$$
로 주어진다.

이제 localized crystal element를
$$
x=b\cdot\prod_{i\in I}z_i^{a_i}
\qquad
(b\in B(w),\ a_i\in\mathbb Z)
$$
꼴로 쓴다. Localized PBW coordinate는
$$
\operatorname{PBW}_{\mathbf i}(x)
=
\operatorname{PBW}_{\mathbf i}(b)+\sum_{i\in I}a_iP_i
\in
\mathbb Z^{[1,m]}
$$
로 정의된다. 이 값은 \(x\)를 위처럼 표현하는 방법에 의존하지 않는다.

Localized PBW parameter set은
$$
\widetilde{\mathcal P}_{\mathbf i}(w)
:=
\mathcal P_{\mathbf i}(w)+\sum_{k\in I}\mathbb ZP_k
\subset
\mathbb Z^{[1,m]}
$$
이고, localized PBW parametrization은 bijection
$$
\operatorname{PBW}_{\mathbf i}:
\mathcal B(w)
\xrightarrow{\sim}
\widetilde{\mathcal P}_{\mathbf i}(w)
$$
이다.

## 핵심 관점

읽는 순서는 다음과 같다.

1. $B(w)$의 element를 ordinary PBW coordinates로 읽는다.
2. Frozen crystal elements가 만드는 fixed PBW directions를 따로 기록한다.
3. $\mathcal B(w)$의 element를 ordinary part와 frozen-direction shifts가 합쳐진 coordinate data로 읽는다.

따라서 localized PBW parametrization은 새로운 crystal을 만드는 construction이 아니다. 이미 만들어진 localized crystal $\mathcal B(w)$를 chosen reduced expression에 의존하는 coordinate system으로 읽는 방법이다.

## 기본 성질

### Reduced-expression dependence

Localized PBW coordinates는 reduced expression $\mathbf i$를 고정한 뒤 정의된다. 따라서 같은 element라도 다른 reduced expression을 고르면 좌표 표현이 달라질 수 있다.

### Ordinary-to-localized extension

Ordinary PBW coordinates는 $B(w)$에서 시작한다. Localized PBW coordinates는 frozen crystal elements가 만드는 directions를 더해서 $\mathcal B(w)$의 localized elements까지 다룬다.

### Integer frozen directions

Ordinary PBW side에서는 nonnegative coordinate data가 기본이다. Localization에서는 frozen elements를 invert하므로, frozen directions에 대해서는 integer shifts가 나타난다.

### Twist formulas와의 경계

Quantum twist automorphism의 coordinate formulas는 별도 topic에서 다룬다. 그 formulas는 [[topics/08-localization-of-categories/localized-string-parametrizations|Localized String Parametrizations]]와 [[topics/08-localization-of-categories/left-and-right-g-vectors|Left and Right g-Vectors]]까지 준비된 뒤 [[topics/08-localization-of-categories/coordinate-formulas-for-quantum-twist-on-localized-crystals|Coordinate Formulas for Quantum Twist on Localized Crystals]]에서 읽는 것이 자연스럽다.

## 다른 topic들과의 관계

[[topics/08-localization-of-categories/localized-crystals|Localized Crystals]]는 $\mathcal B(w)$ 자체를 제공한다. Localized PBW parametrization은 그 crystal을 좌표로 읽는 방법이다.

[[topics/02-crystal-bases/b-infinity-crystal|The Crystal B(infinity)]]는 $B(w)\subset B(\infty)$가 들어가는 ambient crystal을 제공한다. Ordinary PBW coordinates는 이 crystal-side background와 연결된다.

[[topics/01-quantum-groups/quantum-unipotent-coordinate-rings|Quantum Unipotent Coordinate Rings]]는 $B(w)$와 upper global basis가 coordinate-ring side에서 나타나는 배경이다.

[[topics/01-quantum-groups/quantum-minors-and-frozen-variables|Quantum Minors and Frozen Variables]]는 frozen directions를 읽기 전에 quantum minor와 frozen variable이 서로 다른 level의 용어임을 고정한다.

[[topics/01-quantum-groups/pbw-parametrizations-of-quantum-unipotent-coordinate-rings|PBW Parametrizations of Quantum Unipotent Coordinate Rings]]는 reduced expression과 PBW-type coordinates가 ordinary coordinate-ring setting에서 어떻게 나타나는지 설명한다.

[[topics/08-localization-of-categories/localized-string-parametrizations|Localized String Parametrizations]]는 같은 localized crystal을 string-coordinate language로 읽는 companion topic이다.

[[topics/08-localization-of-categories/left-and-right-g-vectors|Left and Right g-Vectors]]는 PBW/string coordinates와 quantum twist formula가 만나는 다음 coordinate layer이다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/08-localization-of-categories/localized-crystals|Localized Crystals]], [[topics/02-crystal-bases/b-infinity-crystal|The Crystal B(infinity)]], [[topics/01-quantum-groups/quantum-unipotent-coordinate-rings|Quantum Unipotent Coordinate Rings]], [[topics/01-quantum-groups/quantum-minors-and-frozen-variables|Quantum Minors and Frozen Variables]], [[topics/01-quantum-groups/pbw-parametrizations-of-quantum-unipotent-coordinate-rings|PBW Parametrizations of Quantum Unipotent Coordinate Rings]].
- 상위 개념: [[topics/08-localization-of-categories/localized-crystals|Localized Crystals]].
- 다음에 읽을 것: [[topics/08-localization-of-categories/localized-string-parametrizations|Localized String Parametrizations]], [[topics/08-localization-of-categories/left-and-right-g-vectors|Left and Right g-Vectors]], [[topics/08-localization-of-categories/coordinate-formulas-for-quantum-twist-on-localized-crystals|Coordinate Formulas for Quantum Twist on Localized Crystals]].

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/jp25-crystals-quantum-twist-automorphisms|Jung-Park 2025]], local TeX lines 1559-1596: reduced expression setup, ordinary PBW input for \(B(w)\), frozen PBW directions, extension to \(\mathcal B(w)\), and the localized PBW parameter set.
- [[sources/books/lusztig94-introduction-quantum-groups|Lusztig 1994]], Chapter 40.2 and Chapter 41.1: ordinary PBW basis and canonical-basis congruence background used by the prerequisite topic.
- Review report: `reports/reviews/2026-06-04-localized-pbw-parametrizations-source-location-review.md`.
- Ordinary PBW background is handled in [[topics/01-quantum-groups/pbw-parametrizations-of-quantum-unipotent-coordinate-rings|PBW Parametrizations of Quantum Unipotent Coordinate Rings]].

</details>
