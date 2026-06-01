---
id: demazure-subcategories-of-quiver-hecke-modules
title: Demazure Subcategories of Quiver-Hecke Modules
level: advanced
topic_kind: category
parent_topics:
  - quiver-hecke-subcategories
prerequisite_topics:
  - crystal-bases
  - quiver-hecke-subcategories
child_topics: []
related_topics:
  - cellular-crystals
  - localized-crystals
maturity: example-ready
---

## 개요

Demazure subcategory $\mathfrak B_w$는 quiver-Hecke module category $R\text{-gmod}$ 안에서 simple subquotients가 Demazure crystal $B_w(\infty)$에 대응하도록 골라진 full subcategory이다. 즉 $\mathfrak B_w$는 [[topics/crystal-bases|crystal]]의 Demazure 부분을 category-level simple modules로 실현하는 category이다.

이 subcategory가 필요한 이유는 $\mathcal C_w$만으로는 root operator를 적용한 뒤의 모든 simple module을 안정적으로 담기 어렵기 때문이다. $\mathfrak B_w$는 $\mathcal C_w$보다 큰 category-level 입력을 제공하고, 그 simple classes는 $B_w(\infty)$와 같은 crystal로 식별된다.

[[topics/crystal-comparison-map|Crystal Comparison Map]]에서는 먼저 $\mathfrak B_w$의 simple object에서 cellular-crystal coordinates를 뽑고, 그 뒤 localized category $\widetilde{\mathcal C}_w$의 simple objects로 map을 확장한다. 따라서 $\mathfrak B_w$는 quiver-Hecke subcategory와 localized crystal comparison 사이의 중간층이다.

## 준비와 notation

$W$를 Weyl group이라고 하고 $w\in W$를 고정한다. $B(\infty)$는 negative half에 붙는 crystal이고, $B_w(\infty)\subset B(\infty)$는 $w$에 대응하는 Demazure crystal이다.

$R\text{-gmod}$는 finite-dimensional graded quiver-Hecke modules의 category이다. $\operatorname{Irr}(R\text{-gmod})$는 simple modules를 grading shift까지 같은 것으로 본 집합이다. Lauda-Vazirani crystal isomorphism을 통해
$$
\operatorname{Irr}(R\text{-gmod})
\simeq
B(\infty)
$$
로 볼 수 있다.

$b\in B(\infty)$에 대응하는 self-dual simple module을 $S(b)$라고 쓴다. 이 notation 아래에서 $b\in B_w(\infty)$라는 crystal-level 조건은 $S(b)$가 $w$-Demazure side에 놓인다는 category-level 조건으로 읽힌다.

$\mathcal C_w$는 [[topics/quiver-hecke-subcategories|Quiver-Hecke Subcategories]]에서 나오는 full monoidal subcategory이다. 여기서 다루는 핵심 category는
$$
\mathfrak B_w
$$
이며, $\mathfrak B_w$는 $\mathcal C_w$와 같다고 가정하면 안 된다.

## 정의

먼저 simple $R$-module $M$에 대해 $w$-Demazure membership 조건을 둔다. 다음 조건들은 같은 class의 simple modules를 판별하는 조건으로 사용된다.

- $M$은 어떤 $b\in B_w(\infty)$에 대해 $S(b)$와 grading shift까지 동형이다.
- Reduced expression $\underline w=s_{i_1}\cdots s_{i_\ell}$에 대해, 어떤 nonnegative integers $n_1,\ldots,n_\ell$가 있어서 $M$은
  $$
  \langle i_1^{n_1}\rangle\circ\cdots\circ\langle i_\ell^{n_\ell}\rangle
  $$
  의 quotient로 나타난다.
- 같은 reduced expression에 대해 $M$의 idempotent support 중
  $$
  e(i_1^{n_1},\ldots,i_\ell^{n_\ell})M
  $$
  이 0이 아닌 경우가 있다.

$\mathfrak B_w$는 다음 조건을 만족하는 objects $M\in R\text{-gmod}$로 이루어진 full subcategory이다.

$$
M\in\mathfrak B_w
\quad\Longleftrightarrow\quad
\text{every simple subquotient of }M
\text{ satisfies the }w\text{-Demazure membership conditions.}
$$

따라서 $\mathfrak B_w$의 정의는 algebra를 localize하는 정의가 아니다. Ambient category $R\text{-gmod}$ 안에서 composition-level simple pieces가 $B_w(\infty)$ 쪽에 놓이는 modules만 모으는 full subcategory 정의이다.

## 기본 예시

Type $A_2$에서 $\mathfrak g=A_2$이고 $w=s_1s_2$라고 하자. 이 경우 다음 현상이 나타난다.
$$
\langle 12\rangle\in\mathcal C_w
$$
이지만
$$
\widetilde E_1\langle 12\rangle\simeq \langle 2\rangle
\notin \mathcal C_w
$$
임을 보여 준다. 그러나 같은 object는
$$
\langle 2\rangle\in\mathfrak B_w
$$
를 만족한다.

이 예시는 $\mathfrak B_w$가 왜 $\mathcal C_w$와 구별되어야 하는지 보여 준다. $\mathcal C_w$ 안에서 시작한 simple object라도 root operator를 적용하면 $\mathcal C_w$ 밖으로 나갈 수 있지만, Demazure crystal 쪽 simple class를 담는 $\mathfrak B_w$ 안에는 남을 수 있다.

검증: 논문 예시

## 핵심 관점

핵심 diagram은 다음과 같다.

$$
\operatorname{Irr}(\mathcal C_w)
\subset
\operatorname{Irr}(\mathfrak B_w)
\simeq
B_w(\infty)
\longrightarrow
\mathcal B_{\underline w}.
$$

왼쪽은 quiver-Hecke subcategory에서 오는 simple classes이고, 가운데는 Demazure crystal 전체를 category-level simple classes로 보는 부분이다. 오른쪽 $\mathcal B_{\underline w}$는 reduced expression에서 온 [[topics/cellular-crystals|cellular crystal]]이다.

따라서 $\mathfrak B_w$는 object-level category와 combinatorial crystal 사이의 번역 구간이다. $\operatorname{CP}$ map은 이 구간에서 simple object에 root operators를 반복 적용하여 cellular-crystal coordinates를 추출한다.

## 기본 성질

- Simple classes는 crystal로서
  $$
  \operatorname{Irr}(\mathfrak B_w)
  \simeq
  B_w(\infty)
  $$
  와 식별된다.
- $\operatorname{Irr}(\mathcal C_w)$는 $\operatorname{Irr}(\mathfrak B_w)$ 안에 들어간다.
- $\operatorname{Irr}(\mathfrak B_w)\sqcup\{0\}$는 $\widetilde E_i$와 $\widetilde E_i^*$에 대해 안정적이다.
- $w'=ws_i<w$일 때, simple $S\in\mathfrak B_w$가 $\varepsilon_i^*(S)=0$을 만족하면 $S\in\mathfrak B_{w'}$이다.
- 같은 상황에서 $(\widetilde F_i^*)^m(S)$는 $S\circ\langle i^m\rangle$와 동형이고, 다시 $\mathfrak B_w$ 안에 놓인다.
- 이 성질들은 $\widetilde E_i^{*\max}$를 사용해 $\operatorname{Irr}(\mathfrak B_w)$에서 $\operatorname{Irr}(\mathfrak B_{w'})$로 내려가는 step을 만들고, comparison map의 recursive coordinate extraction에 쓰인다.

## 다른 topic들과의 관계

- [[topics/quiver-hecke-subcategories|Quiver-Hecke Subcategories]]는 ambient subcategory $\mathcal C_w$를 제공한다. $\mathfrak B_w$는 이 $\mathcal C_w$와 동일한 category가 아니라, Demazure crystal 쪽 simple classes를 담는 더 넓은 category-level 입력이다.
- [[topics/crystal-bases|Crystal Bases]]는 $B(\infty)$와 Demazure crystal $B_w(\infty)$를 이해하기 위한 prerequisite이다.
- [[topics/cellular-crystals|Cellular Crystals]]는 reduced expression $\underline w$에서 얻는 target crystal $\mathcal B_{\underline w}$를 제공한다.
- [[topics/crystal-comparison-map|Crystal Comparison Map]]은 $\mathfrak B_w$의 simple objects에서 시작해 cellular-crystal coordinates를 만들고, 이 construction을 localized simple objects로 확장한다.
- [[topics/localized-crystals|Localized Crystals]]는 comparison map이 최종적으로 비교하는 localized category의 crystal structure를 제공한다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/crystal-bases|Crystal Bases]]에서 $B(\infty)$와 Demazure crystal을 읽고, [[topics/quiver-hecke-subcategories|Quiver-Hecke Subcategories]]에서 $R\text{-gmod}$와 $\mathcal C_w$를 읽는다.
- 상위 개념: [[topics/quiver-hecke-subcategories|Quiver-Hecke Subcategories]]가 더 넓은 quiver-Hecke category setting이다.
- 다음에 읽을 것: [[topics/crystal-comparison-map|Crystal Comparison Map]]에서는 $\mathfrak B_w$에서 cellular-crystal coordinates로 가는 map을 읽고, [[topics/localized-crystals|Localized Crystals]]에서는 localized simple-object crystal을 읽는다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/kashiwara-nakashima25-crystal-structure-localized-quantum-unipotent-coordinate-category|Kashiwara-Nakashima 2025]], lines 1359-1373 of `inbox/papers/crystal.tex`: Demazure crystal $B_w(\infty)$.
- Kashiwara-Nakashima 2025, lines 2188-2209 and 3096-3101: $\operatorname{Irr}(R\text{-gmod})\simeq B(\infty)$ and notation $S(b)$.
- Kashiwara-Nakashima 2025, lines 3102-3128: equivalent membership conditions and definition of $\mathfrak B_w$.
- Kashiwara-Nakashima 2025, lines 3130-3147: $\operatorname{Irr}(\mathcal C_w)\subset\operatorname{Irr}(\mathfrak B_w)$, crystal isomorphism with $B_w(\infty)$, and stability under $\widetilde E_i,\widetilde E_i^*$.
- Kashiwara-Nakashima 2025, lines 3190-3193: type $A_2$ example distinguishing $\mathcal C_w$ from $\mathfrak B_w$.
- Kashiwara-Nakashima 2025, lines 3202-3210 and 3945-3971: starred root-operator step from $\mathfrak B_w$ toward $\mathfrak B_{w'}$.
- Kashiwara-Nakashima 2025, lines 4114-4145: use of $\mathfrak B_w$ in the comparison map.
- Source-location review: `reports/reviews/2026-06-01-demazure-subcategories-source-location-review.md`.

</details>
