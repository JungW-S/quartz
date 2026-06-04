---
id: quantum-twist-automorphisms
title: Quantum Twist Automorphisms
level: advanced
topic_kind: operation
parent_topics:
  - localized-crystals
prerequisite_topics:
  - localized-crystals
  - quantum-coordinate-rings
child_topics:
  - coordinate-formulas-for-quantum-twist-on-localized-crystals
related_topics:
  - reverse-equivalence-of-localized-categories
  - quantum-unipotent-coordinate-rings
maturity: orientation
---

## 개요

Quantum twist automorphism은 quantum coordinate-ring side의 operation이고, localized crystal 관점에서는 이 operation이 category side의 duality functor와 같은 crystal-level motion으로 읽힌다. 이 topic의 역할은 automorphism의 좌표식을 계산하는 것이 아니라, 같은 operation이 coordinate-ring-level, category-level, crystal-level에서 각각 무엇으로 보이는지를 분리하는 것이다.

Coordinate-ring-level에서는 quantum twist automorphism $\eta_w$를 본다. Category-level에서는 localized category $\widetilde{\mathcal C}_w$의 right dual functor를 본다. Crystal-level에서는 localized crystal $\mathcal B(w)$ 위의 permutation $\mathfrak D_w$를 본다.

따라서 여기서 중요한 관점은 세 object가 서로 다른 종류의 object라는 점이다. $\eta_w$는 algebra automorphism이고, right dual은 functor이며, $\mathfrak D_w$는 crystal-level indexing set 위의 map이다.

## 준비와 notation

먼저 [[topics/01-quantum-groups/quantum-coordinate-rings|Quantum Coordinate Rings]]에서 coordinate-ring side를 읽고, [[topics/08-localization-of-categories/localized-crystals|Localized Crystals]]에서 localized category와 localized crystal $\mathcal B(w)$를 읽는다.

$w$는 Weyl group element이다. $\mathcal B(w)$는 $B(w)\subset B(\infty)$에서 frozen directions를 invert하여 얻는 localized crystal이고, 같은 index set이 localized upper global basis와 localized simple-object classes를 함께 기록한다.

$\eta_w$는 quantum twist automorphism을 나타낸다. 이 automorphism은 coordinate-ring-level operation이다.

$\mathfrak D_w$는 $\mathcal B(w)$ 위의 crystal-level operation이다. 이 symbol은 coordinate-ring side의 quantum twist와 category side의 right duality를 localized crystal language로 비교할 때 쓰인다.

Right dual functor는 localized category 안의 object를 dual object로 보내는 category-level operation이다. 이 functor가 simple-object classes에 유도하는 작용을 보면 coordinate-ring side의 automorphism과 비교할 수 있다.

## 핵심 관점

한 index $x\in\mathcal B(w)$는 두 방식으로 읽힌다.

- Coordinate-ring-level에서는 $x$가 localized upper global basis element를 가리킨다.
- Category-level에서는 $x$가 localized category의 simple-object class를 가리킨다.

이 dictionary를 통해 coordinate-ring-level automorphism을 category-level operation과 비교할 수 있다. Quantum twist automorphism $\eta_w$는 simple-object class 쪽에서 inverse right dual functor가 유도하는 action과 맞는다. 반대로 $\mathfrak D_w$ 자체는 right dual functor에 대응하는 crystal-level operation으로 읽는다.

즉, localized crystal은 quantum twist automorphism을 직접 계산하기 위한 좌표표가 아니라, coordinate-ring operation과 categorical duality가 같은 indexing set 위에서 비교되는 장소이다.

## 기본 성질

### Level separation

Quantum twist automorphism은 coordinate-ring-level operation이다. Right dual functor는 category-level operation이다. $\mathfrak D_w$는 crystal-level operation이다. 세 층을 구분해야 twist를 functor로 categorify한다는 말이 정확해진다.

### Categorification viewpoint

Categorification 관점에서는 coordinate-ring element를 localized category의 simple-object class로 읽는다. 그러면 coordinate-ring automorphism이 Grothendieck ring에서 어떤 functor가 유도한 map으로 보이는지를 묻는다.

### Direction of duality

이 비교에서 $\eta_w$와 right dual functor는 같은 방향으로 적히지 않는다. $\eta_w$는 simple-object class 쪽에서 inverse right dual functor가 유도하는 action과 맞고, $\mathfrak D_w$는 right dual functor 자체에 대응하는 crystal-level operation으로 읽는다.

### Boundary with coordinate formulas

좌표식은 별도 topic인 [[topics/08-localization-of-categories/coordinate-formulas-for-quantum-twist-on-localized-crystals|Coordinate Formulas for Quantum Twist on Localized Crystals]]에서 다룬다. 그 topic을 읽으려면 [[topics/08-localization-of-categories/localized-pbw-parametrizations|Localized PBW Parametrizations]], [[topics/08-localization-of-categories/localized-string-parametrizations|Localized String Parametrizations]], [[topics/08-localization-of-categories/left-and-right-g-vectors|Left and Right g-Vectors]]가 먼저 필요하다.

## 다른 topic들과의 관계

[[topics/08-localization-of-categories/localized-crystals|Localized Crystals]]는 $\mathcal B(w)$와 localized simple-object classes가 만나는 장소를 제공한다. Quantum twist automorphism은 이 dictionary 위에서 right duality와 비교된다.

[[topics/01-quantum-groups/quantum-coordinate-rings|Quantum Coordinate Rings]]는 $\eta_w$가 사는 coordinate-ring-level 배경이다. 이 page를 읽지 않으면 twist가 algebra automorphism이라는 level이 보이지 않는다.

[[topics/08-localization-of-categories/reverse-equivalence-of-localized-categories|Reverse Equivalence of Localized Categories]]는 localized category에서 duality와 reversal이 어떻게 나타나는지 설명하는 가까운 theorem-level topic이다.

[[topics/01-quantum-groups/quantum-unipotent-coordinate-rings|Quantum Unipotent Coordinate Rings]]는 $B(w)$와 localized coordinate-ring basis를 이해하기 위해 필요한 coordinate-ring background로 남아 있다.

[[topics/08-localization-of-categories/coordinate-formulas-for-quantum-twist-on-localized-crystals|Coordinate Formulas for Quantum Twist on Localized Crystals]]는 이 topic보다 뒤에 읽을 formula-level child topic이다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/01-quantum-groups/quantum-coordinate-rings|Quantum Coordinate Rings]], [[topics/08-localization-of-categories/localized-crystals|Localized Crystals]].
- 상위 개념: [[topics/08-localization-of-categories/localized-crystals|Localized Crystals]].
- 다음에 읽을 것: [[topics/08-localization-of-categories/reverse-equivalence-of-localized-categories|Reverse Equivalence of Localized Categories]], [[topics/08-localization-of-categories/localized-pbw-parametrizations|Localized PBW Parametrizations]], [[topics/08-localization-of-categories/localized-string-parametrizations|Localized String Parametrizations]], [[topics/08-localization-of-categories/left-and-right-g-vectors|Left and Right g-Vectors]].

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/jp25-crystals-quantum-twist-automorphisms|Jung-Park 2025]], local TeX lines 1546-1555: the commutative diagram relating $\mathcal B(w)$, localized upper global basis elements, localized simple-object classes, $\eta_w$, and the right dual functor.
- [[sources/papers/jp25-crystals-quantum-twist-automorphisms|Jung-Park 2025]], local TeX lines 1480-1541: the localized crystal $\mathcal B(w)$ and its two avatars as localized upper global basis elements and localized simple-object classes.

</details>
