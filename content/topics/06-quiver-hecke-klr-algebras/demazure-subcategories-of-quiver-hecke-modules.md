---
id: demazure-subcategories-of-quiver-hecke-modules
title: Demazure Subcategories of Quiver-Hecke Modules
level: advanced
topic_kind: category
parent_topics:
  - quiver-hecke-subcategories
prerequisite_topics:
  - demazure-crystals
  - quiver-hecke-subcategories
child_topics: []
related_topics:
  - demazure-crystals
  - cellular-crystals
  - localized-crystals
maturity: study-ready
---

## 개요

Demazure subcategory $\mathfrak B_w$는 quiver-Hecke module category $R\text{-gmod}$ 안에서 simple subquotients가 Demazure crystal $B_w(\infty)$에 대응하도록 골라진 full subcategory이다. 즉 $\mathfrak B_w$는 [[topics/02-crystal-bases/demazure-crystals|Demazure crystal]]의 crystal-level elements를 category-level simple modules로 실현하는 category이다.

이 subcategory가 필요한 이유는 $\mathcal C_w$만으로는 root operator를 적용한 뒤의 simple module을 안정적으로 담기 어렵기 때문이다. $\mathfrak B_w$는 $\mathcal C_w$보다 큰 category-level 입력을 제공하고, 그 simple classes는 $B_w(\infty)$와 같은 crystal로 식별된다.

[[topics/08-localization-of-categories/localized-crystals|Localized Crystals]]에서는 먼저 $\mathfrak B_w$의 simple object에서 cellular-crystal coordinates를 뽑고, 그 뒤 localized category $\widetilde{\mathcal C}_w$의 simple objects로 $\operatorname{CP}$를 확장한다. 따라서 $\mathfrak B_w$는 quiver-Hecke subcategory와 localized crystal comparison 사이의 중간층이다.

## 준비와 notation

$W$를 Weyl group이라고 하고 $w\in W$를 고정한다. $B(\infty)$는 negative half에 붙는 crystal이고, $B_w(\infty)\subset B(\infty)$는 $w$에 대응하는 Demazure crystal이다. 이 notation은 crystal-level에서 쓰인다.

$R\text{-gmod}$는 finite-dimensional graded quiver-Hecke modules의 category이다. $\operatorname{Irr}(R\text{-gmod})$는 simple modules를 grading shift까지 같은 것으로 본 집합이다. 이 notation은 category-level에서 쓰인다. Lauda-Vazirani crystal isomorphism을 통해
$$
\operatorname{Irr}(R\text{-gmod})
\simeq
B(\infty)
$$
로 볼 수 있다.

$b\in B(\infty)$에 대응하는 self-dual simple module을 $S(b)$라고 쓴다. 이 notation 아래에서 $b\in B_w(\infty)$라는 crystal-level 조건은 $S(b)$가 $w$-Demazure side에 놓인다는 category-level 조건으로 번역된다.

$\mathcal C_w$는 [[topics/06-quiver-hecke-klr-algebras/quiver-hecke-subcategories|Quiver-Hecke Subcategories]]에서 나오는 full monoidal subcategory이다. 여기서 다루는 핵심 category는
$$
\mathfrak B_w
$$
이며, $\mathfrak B_w$는 $\mathcal C_w$와 같다고 가정하면 안 된다.

## 정의

먼저 simple $R$-module $M$에 대해 $w$-Demazure membership 조건을 둔다. 다음 조건들은 같은 class의 simple modules를 판별하는 동치 조건으로 사용된다.

### Crystal-label condition

$M$은 어떤 $b\in B_w(\infty)$에 대해 $S(b)$와 grading shift까지 동형이다. 이 조건은 membership을 Demazure crystal 안의 label로 판별한다.

### Quotient condition

Reduced expression $\underline w=s_{i_1}\cdots s_{i_\ell}$에 대해, 어떤 nonnegative integers $n_1,\ldots,n_\ell$가 있어서 $M$은
$$
\langle i_1^{n_1}\rangle\circ\cdots\circ\langle i_\ell^{n_\ell}\rangle
$$
의 quotient로 나타난다. 이 조건은 $M$을 ordered convolution product의 quotient로 판별한다.

### Idempotent-support condition

같은 reduced expression에 대해 $M$의 idempotent support 중
$$
e(i_1^{n_1},\ldots,i_\ell^{n_\ell})M
$$
이 0이 아닌 경우가 있다. 이 조건은 module의 word support가 chosen reduced expression과 맞는지를 본다.

$\mathfrak B_w$는 다음 조건을 만족하는 objects $M\in R\text{-gmod}$로 이루어진 full subcategory이다.

$$
M\in\mathfrak B_w
\quad\Longleftrightarrow\quad
\text{every simple subquotient of }M
\text{ satisfies the }w\text{-Demazure membership conditions.}
$$

따라서 $\mathfrak B_w$의 정의는 algebra를 localize하는 정의가 아니다. Ambient category $R\text{-gmod}$ 안에서 simple subquotients가 $B_w(\infty)$ 쪽에 놓이는 modules만 모으는 full subcategory 정의이다.

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

왼쪽은 quiver-Hecke subcategory에서 오는 simple classes이고, 가운데는 Demazure crystal 전체를 category-level simple classes로 보는 부분이다. 오른쪽 $\mathcal B_{\underline w}$는 reduced expression에서 온 [[topics/02-crystal-bases/cellular-crystals|cellular crystal]]이다.

따라서 $\mathfrak B_w$는 category-level simple modules와 combinatorial crystal 사이의 번역 구간이다. $\operatorname{CP}$ map은 이 구간에서 simple object에 root operators를 반복 적용하여 cellular-crystal coordinates를 추출한다.

## 기본 성질

### Simple classes가 만드는 Demazure crystal

Simple classes는 crystal로서
$$
\operatorname{Irr}(\mathfrak B_w)
\simeq
B_w(\infty)
$$
와 식별된다. 또한 $\operatorname{Irr}(\mathcal C_w)$는 $\operatorname{Irr}(\mathfrak B_w)$ 안에 들어간다. 따라서 $\mathfrak B_w$는 $\mathcal C_w$에서 오는 simple classes를 포함하면서도 Demazure crystal 전체를 category-level에서 담는 더 큰 입력이다.

### Root operators에 대한 안정성

$\operatorname{Irr}(\mathfrak B_w)\sqcup\{0\}$는 $\widetilde E_i$와 $\widetilde E_i^*$에 대해 안정적이다. 이 안정성 때문에 $\mathfrak B_w$ 안에서 root-operator step을 적용해도 Demazure side의 simple classes를 벗어나지 않는 형태로 추적할 수 있다.

### 짧은 Weyl group element로 내려가는 step

$w'=ws_i<w$일 때, simple $S\in\mathfrak B_w$가 $\varepsilon_i^*(S)=0$을 만족하면 $S\in\mathfrak B_{w'}$이다. 같은 상황에서 $(\widetilde F_i^*)^m(S)$는 $S\circ\langle i^m\rangle$와 동형이고, 다시 $\mathfrak B_w$ 안에 놓인다.

이 성질들은 $\widetilde E_i^{*\max}$를 사용해 $\operatorname{Irr}(\mathfrak B_w)$에서 $\operatorname{Irr}(\mathfrak B_{w'})$로 내려가는 step을 만든다.

### Cellular-coordinate extraction

짧은 Weyl group element로 내려가는 step은 comparison map의 recursive coordinate extraction에 쓰인다. 이때 $\mathfrak B_w$는 root-operator recursion을 category-level에서 수행하는 domain 역할을 하고, cellular crystal은 추출된 coordinates가 도착하는 target 역할을 한다.

## 다른 topic들과의 관계

[[topics/02-crystal-bases/demazure-crystals|Demazure Crystals]]는 $\mathfrak B_w$가 category-level에서 실현하는 crystal subset $B_w(\infty)$를 제공한다. 먼저 $B_w(\infty)\subset B(\infty)$를 ordinary crystal-side에서 읽어야 $\mathfrak B_w$의 membership condition이 자연스럽다.

[[topics/06-quiver-hecke-klr-algebras/quiver-hecke-subcategories|Quiver-Hecke Subcategories]]는 ambient subcategory $\mathcal C_w$를 제공한다. $\mathfrak B_w$는 이 $\mathcal C_w$와 동일한 category가 아니라, Demazure crystal 쪽 simple classes를 담는 더 넓은 category-level 입력이다.

[[topics/06-quiver-hecke-klr-algebras/determinantial-modules|Determinantial Modules]]는 quiver-Hecke category 안의 distinguished simple modules를 설명한다. $w$-dominant $\lambda$에 붙은 generalized determinantial module $\mathsf M_w(w\lambda,\lambda)$는 $\mathfrak B_w$ 안에 놓이므로, determinantial-type objects는 localized category에서 invertible하게 쓰이는 것과 별도로 Demazure subcategory의 simple-object side에도 나타난다. 여기서 $\mathsf M_w(w\lambda,\lambda)$는 $\mathcal C_{w,v}$의 indexed family $M(w_{\le k}\Lambda,v_{\le k}\Lambda)$와 같은 notation layer가 아니므로 두 family를 동일시하지 않는다.

[[topics/02-crystal-bases/cellular-crystals|Cellular Crystals]]는 reduced expression $\underline w$에서 얻는 target crystal $\mathcal B_{\underline w}$를 제공한다. $\mathfrak B_w$는 이 target으로 보내기 전의 category-level domain을 제공한다.

[[topics/08-localization-of-categories/localized-crystals|Localized Crystals]]는 $\mathfrak B_w$의 simple objects에서 cellular-crystal coordinates를 만드는 construction을 localized simple objects로 확장하고, comparison map이 최종적으로 비교하는 localized category의 crystal structure를 제공한다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/02-crystal-bases/b-infinity-crystal|The Crystal B(infinity)]]와 [[topics/02-crystal-bases/demazure-crystals|Demazure Crystals]]에서 $B_w(\infty)$를 읽고, [[topics/06-quiver-hecke-klr-algebras/quiver-hecke-subcategories|Quiver-Hecke Subcategories]]에서 $R\text{-gmod}$와 $\mathcal C_w$를 읽는다.
- 상위 개념: [[topics/06-quiver-hecke-klr-algebras/quiver-hecke-subcategories|Quiver-Hecke Subcategories]]가 더 넓은 quiver-Hecke category 쪽 배경이다.
- 다음에 읽을 것: [[topics/08-localization-of-categories/localized-crystals|Localized Crystals]]에서는 $\mathfrak B_w$에서 cellular-crystal coordinates로 가는 $\operatorname{CP}$ map과 localized simple-object crystal을 읽는다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/kashiwara-nakashima25-crystal-structure-localized-quantum-unipotent-coordinate-category|Kashiwara-Nakashima 2025]], lines 1359-1373 of `inbox/papers/crystal.tex`: Demazure crystal $B_w(\infty)$.
- Kashiwara-Nakashima 2025, lines 2188-2209 and 3096-3101: $\operatorname{Irr}(R\text{-gmod})\simeq B(\infty)$ and notation $S(b)$.
- Kashiwara-Nakashima 2025, lines 3102-3128: equivalent membership conditions and definition of $\mathfrak B_w$.
- Kashiwara-Nakashima 2025, lines 3130-3147: $\operatorname{Irr}(\mathcal C_w)\subset\operatorname{Irr}(\mathfrak B_w)$, crystal isomorphism with $B_w(\infty)$, and stability under $\widetilde E_i,\widetilde E_i^*$.
- Kashiwara-Nakashima 2025, lines 3190-3193: type $A_2$ example distinguishing $\mathcal C_w$ from $\mathfrak B_w$.
- Kashiwara-Nakashima 2025, lines 2586-2624 and 3196-3200: generalized determinantial modules $\mathsf M_w(w\lambda,\lambda)$ and their membership in $\mathfrak B_w$ for $w$-dominant $\lambda$.
- Kashiwara-Nakashima 2025, lines 3202-3210 and 3945-3971: starred root-operator step from $\mathfrak B_w$ toward $\mathfrak B_{w'}$.
- Kashiwara-Nakashima 2025, lines 4114-4145: use of $\mathfrak B_w$ in the comparison map.
- Source-location review: `reports/reviews/2026-06-01-demazure-subcategories-source-location-review.md`.

</details>
