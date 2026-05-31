---
id: determinantial-modules
title: Determinantial Modules
level: advanced
topic_kind: object-family
parent_topics:
  - quiver-hecke-algebras
  - monoidal-categorification
  - quantum-coordinate-rings
prerequisite_topics:
  - quiver-hecke-algebras
  - monoidal-categorification
  - quantum-coordinate-rings
child_topics: []
related_topics:
  - quiver-hecke-algebra-localization
maturity: study-ready
---

# Determinantial Modules

## What it is

Determinantial modules는 quiver Hecke algebra의 module category에서 나타나는 distinguished module objects로, monoidal categorification에서 determinant-type coordinate data를 category 안에서 다루게 해 주는 family이다. 이름의 determinantial은 determinant나 minor처럼 작동하는 coordinate-ring data와의 관계를 가리키지만, module object 자체가 coordinate function인 것은 아니다.

이 modules는 먼저 $\mathcal C_{w,v}$ 안의 objects로 놓인다. 그 다음 Grothendieck ring으로 내려가 classes를 만들고, 이 classes를 $A_{w,v}$와 비교하면서 coordinate-ring side의 정보를 읽는다.

## Why it appears

Coordinate ring에서는 determinant나 minor 같은 elements가 계산과 구조를 잡아 주는 역할을 한다. Monoidal categorification에서는 이런 역할을 algebra element가 아니라 category 안의 module object로 들어 올려서 다루고자 한다.

Category 안의 module object는 그 자체로 ring element가 아니므로, Grothendieck ring으로 내려가는 단계가 필요하다. Convolution product는 $K_0(\mathcal C_{w,v})$에서 multiplication으로 기록되고, 그 뒤 $A_{w,v}$와의 comparison을 통해 coordinate-ring language와 연결된다.

## Setup and notation

$v \leq w$인 Weyl group elements를 고정하고, $w$의 reduced expression을 하나 고른다. Index $k$는 이 reduced expression을 따라 읽는다.

- $\mathcal C_{w,v}$는 determinantial modules가 놓이는 ambient monoidal category이다.
- $K_0(\mathcal C_{w,v})$는 $\mathcal C_{w,v}$의 Grothendieck ring이다.
- $A_{w,v}$는 $K_0(\mathcal C_{w,v})$와 비교되는 coordinate-ring side의 algebra이다.
- $M(w_{\le k}\Lambda, v_{\le k}\Lambda)$는 chosen reduced expression과 weight parameter $\Lambda$에 붙은 determinantial-module family의 한 member를 나타낸다.

## Definition

고정된 $v \leq w$와 $w$의 chosen reduced expression에 대해 determinantial modules는 indexed family
$$
M(w_{\le k}\Lambda, v_{\le k}\Lambda)
$$
로 나타난다.

이 family의 각 member는 $\mathcal C_{w,v}$의 object이다. Family 전체는 선택한 reduced expression과 함께 읽으며, $k$는 그 expression 안의 위치를 추적한다.

## Basic picture

$$
M(w_{\le k}\Lambda, v_{\le k}\Lambda)\in \mathcal C_{w,v}
\;\longrightarrow\;
\bigl[M(w_{\le k}\Lambda, v_{\le k}\Lambda)\bigr]\in K_0(\mathcal C_{w,v})
\;\longrightarrow\;
A_{w,v}
$$

왼쪽은 module object이고, 가운데는 그 Grothendieck-ring class이다. 오른쪽은 coordinate-ring side와의 comparison으로 도달하는 algebra이다.

## Example

### Schematic example

Toy monoidal category $\mathcal C$ 안에 objects
$$
M_1,M_2\in \mathcal C
$$
가 있다고 하자. Grothendieck ring으로 내려가면 이들은 classes
$$
[M_1],[M_2]\in K_0(\mathcal C)
$$
를 주고, monoidal product는 class multiplication으로 반영된다:
$$
[M_1]\,[M_2]=[M_1\circ M_2].
$$

이 schematic example은 object-level에서 Grothendieck-ring-level로 내려가는 방식을 보여 준다. 특정 reduced expression에 대한 실제 determinantial-module 계산은 아니다.

## Main facts

- $M(w_{\le k}\Lambda, v_{\le k}\Lambda)$는 $\mathcal C_{w,v}$ 안에 놓인다. 이 사실은 determinantial modules를 coordinate-ring expression이 아니라 category 안의 concrete module objects로 다루게 해 준다.
- 관련 indexed family는 strongly commute한다. 이 사실은 family의 convolution products를 Grothendieck-ring classes와 비교할 때 필요한 monoidal compatibility를 제공한다.
- $K_0(\mathcal C_{w,v})$는 $A_{w,v}$와 비교된다. 이 사실은 module objects에서 coordinate-ring side의 algebra로 이동하는 통로를 만든다.

## Why it matters

Determinantial modules는 monoidal categorification에서 coordinate-ring data를 object-level로 붙잡아 주는 anchors이다. 이를 통해 determinant-type structure를 단순한 formula가 아니라 module family와 그 products로 추적할 수 있다.

Strong commutation은 이 family가 monoidal product와 잘 맞는다는 정보를 준다. Grothendieck ring으로 내려가면 이런 categorical information이 multiplication of classes로 바뀌고, $A_{w,v}$와의 comparison을 통해 coordinate-ring side의 구조와 연결된다.

## Connections

**Quantum minors.** Quantum minors는 determinantial이라는 이름을 이해하게 해 주는 coordinate-ring model이다. Determinantial module 자체는 module object이고, coordinate function과의 관계는 class와 comparison을 거쳐 읽는다.

**Quantum coordinate rings.** $A_{w,v}$는 determinantial modules의 classes를 비교하는 coordinate-ring side의 algebra이다. 이 연결은 $\mathcal C_{w,v}$에서 $K_0(\mathcal C_{w,v})$로 내려간 뒤 나타난다.

**Dual canonical bases.** Dual canonical bases는 coordinate-ring side에서 distinguished elements를 조직하는 basis language이다. Determinantial modules와 basis elements를 비교할 때는 object와 class를 구별해서 읽는다.

**Localization.** Localization은 quiver Hecke algebra categories를 비교하거나 바꾸는 categorical construction과 관련된다. Determinantial modules는 그런 category-level setting 안에서 distinguished family로 사용된다.

**Frozen variables.** Frozen-variable language는 cluster-theoretic intuition을 제공한다. 여기에서 직접 쓰는 구조는 determinantial-module family의 strong commutation이다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/kkop18-monoidal-categories-strata-flag-manifolds|KKOP18]], Proposition 4.8 and Theorem 4.10: determinantial modules lie in $\mathcal C_{w,v}$ and the relevant family strongly commutes.
- KKOP18, Section 2.2 and Proposition 2.16: $\mathcal C_{w,v}$ is the ambient category used here.
- KKOP18, Theorem 2.20(ii)(c): $K_0(\mathcal C_{w,v})$ is compared with $A_{w,v}$.

</details>
