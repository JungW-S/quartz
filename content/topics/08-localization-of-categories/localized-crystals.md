---
id: localized-crystals
title: Localized Crystals
level: advanced
topic_kind: construction
parent_topics:
  - quiver-hecke-category-localization
prerequisite_topics:
  - crystal-bases
  - cellular-crystals
  - demazure-subcategories-of-quiver-hecke-modules
  - quiver-hecke-category-localization
child_topics:
  - quantum-twist-automorphisms
  - localized-root-operators
  - localized-pbw-parametrizations
  - localized-string-parametrizations
  - left-and-right-g-vectors
related_topics:
  - crystal-bases
  - monoidal-categorification
maturity: study-ready
---

## 개요

Localized crystal은 localized quantum unipotent coordinate category $\widetilde{\mathcal C}_w$의 simple objects를 vertices로 삼는 [[topics/02-crystal-bases/crystal-bases|crystal structure]]이다. 더 정확히는 grading shift까지 같은 것으로 보는 simple objects의 집합
$$
\operatorname{Irr}(\widetilde{\mathcal C}_w)
$$
위에 crystal operators $\widetilde E_i,\widetilde F_i$를 정의한 구조를 말한다.

일반적인 crystal graph처럼 arrows는 crystal-level data이지만, vertices는 combinatorial symbols가 아니라 localized monoidal category 안의 simple objects이다. 비교 정리는 이 category-level crystal이 cellular crystal $\mathcal B_w$와 같다는 것을 보여 준다.

Crystal base theory에서는 basis element 위에 operators $\widetilde e_i,\widetilde f_i$가 작용하여 crystal graph를 만든다. Monoidal categorification 쪽에서는 basis element 대신 module category의 simple objects를 다루므로, 같은 crystal graph를 category 안에서 직접 실현할 방법이 필요하다.

같은 object는 [[topics/02-crystal-bases/b-infinity-crystal|$B(\infty)$]] 쪽에서도 나타난다. $B(\infty)$ 안의 부분 $B(w)$를 frozen directions로 확장하면 localized crystal $\mathcal B(w)$가 되고, 이 $\mathcal B(w)$가 localized basis와 localized simple objects를 함께 index한다. 그래서 이 topic에는 두 관점이 동시에 들어온다: category 안의 simple-object crystal과 $B(\infty)$에서 온 crystal-level avatar.

## 준비와 notation

$\mathfrak g$를 symmetrizable Kac-Moody Lie algebra로 두고, $W$를 Weyl group, $I$를 simple root index set으로 둔다. $R\text{-gmod}$는 quiver-Hecke algebra의 finite-dimensional graded module category이다.

$w\in W$에 대해 $\mathcal C_w$는 $R\text{-gmod}$ 안의 monoidal subcategory이고, $\widetilde{\mathcal C}_w$는 $\mathcal C_w$를 determinantial objects $\mathsf M(w\Lambda_i,\Lambda_i)$에 대해 localization한 category이다. Localization functor는 objects를 $\mathcal C_w$에서 $\widetilde{\mathcal C}_w$로 보낸다.

$\operatorname{Irr}(\widetilde{\mathcal C}_w)$는 $\widetilde{\mathcal C}_w$의 simple objects를 grading shift까지 같은 것으로 본 집합이다. Weight, $\widetilde e_i$, $\widetilde f_i$, $\varepsilon_i$, $\varphi_i$, tensor product 같은 일반 crystal notation은 [[topics/02-crystal-bases/crystal-bases|Crystal Bases]]에서 정리한다.

$\mathfrak B_w$는 [[topics/06-quiver-hecke-klr-algebras/demazure-subcategories-of-quiver-hecke-modules|Demazure Subcategories of Quiver-Hecke Modules]]에서 다루는 category-level subcategory이다. $\mathfrak B_w$의 simple objects는 $B_w(\infty)$와 대응하며, $\operatorname{CP}$의 recursive coordinate extraction은 먼저 이 category-level input에서 정의된다.

$B(w)$는 [[topics/02-crystal-bases/b-infinity-crystal|$B(\infty)$]] 안에서 upper global basis element가 $A_q(\mathfrak n(w))$에 놓이는 원소들로 이루어진 부분이다. $\mathfrak z_i^w$는 quantum unipotent minor $\Delta(w\Lambda_i,\Lambda_i)$에 대응하는 frozen crystal element이고, $\mathcal B(w)$는 이 frozen directions를 invert한 localized crystal model이다.

$I_w$는 $w\Lambda_i\ne\Lambda_i$인 simple root indices의 집합이다. 각 $i\in I_w$에 대해 localized construction은 localized simple root object
$$
\widetilde Q_i=\Phi_w(\langle i\rangle)
$$
를 사용한다. 여기서 $\Phi_w$는 localization functor이고, $\langle i\rangle$는 quiver-Hecke module category 쪽의 simple root object이다.

Operator formula를 읽을 때 필요한 notation은 [[topics/08-localization-of-categories/localized-root-operators|Localized Root Operators]]에서 모아 둔다. 거기서는 $\mathsf d_i=(\alpha_i,\alpha_i)/2$, modified R-matrix degree $\widetilde\Lambda$, 양방향 degree invariant $\mathfrak d$, convolution product의 simple head $\nabla$, 그리고 duality functor $\mathscr D$를 도입한 뒤 $\widetilde E_i,\widetilde F_i$를 정의한다.

## 구성

Localized crystal construction은 다음 data로 이루어진다.

1. Vertex set은 grading shift까지 같은 것으로 보는 simple objects의 집합 $\operatorname{Irr}(\widetilde{\mathcal C}_w)$이다.
2. 각 $i\in I_w$에 대해 localized simple-root object $\widetilde Q_i$와 R-matrix degree data를 사용하여 maps $\widetilde E_i,\widetilde F_i$와 starred maps를 만든다.
3. 같은 data에서 $\varepsilon_i,\varphi_i$와 starred analogues를 정의하여 ordinary crystal의 numerical functions와 맞춘다.
4. $i\notin I_w$인 direction은 이 localized crystal에서 active arrow를 만들지 않는다.

정확한 operator formulas는 [[topics/08-localization-of-categories/localized-root-operators|Localized Root Operators]]의 내용이다. 여기서는 그 formulas를 반복하지 않고, 그 maps가 $\operatorname{Irr}(\widetilde{\mathcal C}_w)$ 위의 crystal structure를 만든다는 구성 수준의 진술에 집중한다.

### Simple-object crystal

위 data는 $\operatorname{Irr}(\widetilde{\mathcal C}_w)$ 위의 crystal structure를 이룬다. 여기서 vertices는 localized category의 simple objects이고, arrows는 localized root operators가 만든다.

### Cellular-coordinate target

이 crystal을 cellular coordinates와 비교하기 위해 reduced expression
$$
\underline w=s_{i_1}\cdots s_{i_\ell}
$$
을 고정하고 cellular crystal
$$
\mathcal B_{\underline w}=B_{i_1}\otimes\cdots\otimes B_{i_\ell}
$$
를 둔다. $\mathcal B_{\underline w}$는 comparison map의 combinatorial-level target이다.

### Recursive coordinate extraction

Category-level input $\mathfrak B_w$의 simple object $M$에 대해 $M_\ell=M$으로 두고, $k=\ell,\ell-1,\ldots,1$에 대해
$$
c_k=\varepsilon^*_{i_k}(M_k),
\qquad
M_{k-1}=(\widetilde E^*_{i_k})^{c_k}(M_k)
$$
를 반복한다. 이때
$$
\operatorname{CP}(M)=(c_1,\ldots,c_\ell)
\in \mathcal B_{\underline w}
$$
로 둔다. 이 recursion은 starred root operators로 $\mathfrak B_w$ 안에서 내려가면서 cellular coordinates를 추출한다.

### Extension to localized simples

Localized simple object가
$$
\widetilde C_\Lambda^{-1}\circ\Phi_w(M)
$$
꼴로 표현되면 comparison map은
$$
\operatorname{CP}(\widetilde C_\Lambda^{-1}\circ\Phi_w(M))
=\operatorname{CP}(M)-\operatorname{CP}(\widetilde C_\Lambda)
$$
로 확장된다. 따라서 comparison map은
$$
\operatorname{CP}:
\operatorname{Irr}(\widetilde{\mathcal C}_w)
\longrightarrow
\mathcal B_{\underline w}
$$
이다.

## 기본 예시

### 실제 예시: type $A_3$

Type $A_3$에서
$$
w=s_2w_0=s_1s_2s_3s_2s_1
$$
인 경우를 보자. 이때 쓰는 subcategory는
$$
\mathcal C_w=\{M\in R\text{-gmod}\mid E_2M\simeq0\}
$$
이고, localized category $\widetilde{\mathcal C}_w$는 네 개의 clusters를 갖는 cluster algebra를 monoidal categorification한다.

이 예시에서 frozen variables는
$$
\Delta_{\Lambda_1}=\langle321\rangle,\qquad
\Delta_{\Lambda_2}=\langle132\rangle,\qquad
\Delta_{\Lambda_3}=\langle123\rangle
$$
이다. $C_1$ chart의 monomial은
$$
\langle1\rangle^x\circ
\langle3\rangle^y\circ
\langle321\rangle^a\circ
\langle132\rangle^b\circ
\langle123\rangle^c
$$
처럼 쓸 수 있다. 여기서 $x,y\in\mathbb Z_{\ge0}$이고 $a,b,c\in\mathbb Z$이다. 이 monomial에 대해 comparison map은
$$
\operatorname{CP}(
\langle1\rangle^x\circ
\langle3\rangle^y\circ
\langle321\rangle^a\circ
\langle132\rangle^b\circ
\langle123\rangle^c)
=(c+b,c,y+a+b+c,a+b,x+a)
$$
를 준다. 따라서 이 example에서는 localized category 안의 cluster monomial이 five-coordinate cellular-crystal point로 바뀐다.

같은 예시는 나머지 세 cluster charts에 대해서도 analogous formulas를 주며, 네 charts의 images를 cellular crystal 안의 네 regions로 나타낸다. 이 전체 region picture는 cluster-chart mechanism을 더 설명해야 하므로 여기서는 formula 하나만 기본 예시로 둔다.

검증: 논문 예시

## 핵심 관점

$$
\mathcal C_w
\;\xrightarrow{\;\text{localize}\;}\;
\widetilde{\mathcal C}_w
\;\xrightarrow{\;\operatorname{Irr}\;}\;
\operatorname{Irr}(\widetilde{\mathcal C}_w)
\;\xrightarrow{\;\operatorname{CP}\;}\;
\mathcal B_w
$$

왼쪽 두 단계는 category-level construction이다. 가운데 집합의 vertices는 simple objects이고, [[topics/08-localization-of-categories/localized-root-operators|Localized Root Operators]]가 crystal-level arrows를 만든다. 마지막 map $\operatorname{CP}$는 이 crystal을 cellular crystal $\mathcal B_w$와 비교한다.

## 기본 성질

### Localized category input

$\widetilde{\mathcal C}_w$는 $\mathcal C_w$의 localization으로 얻어지는 rigid monoidal category이다. 이 category가 localized crystal의 ambient category이다.

### Crystal operators

[[topics/08-localization-of-categories/localized-root-operators|Localized Root Operators]]에서 정의한 maps는 $\operatorname{Irr}(\widetilde{\mathcal C}_w)$ 위의 crystal structure를 정의한다. 이 statement는 localized simple objects가 ordinary crystal graph의 vertices처럼 작동한다는 뜻이다.

### Comparison map

$\operatorname{CP}:\operatorname{Irr}(\widetilde{\mathcal C}_w)\to\mathcal B_w$는 crystal morphism이고, 실제로 crystal isomorphism이다. 따라서 localized simple-object crystal은 cellular crystal과 같은 crystal-level object로 읽힌다.

### Coordinate dependence

Coordinate map은 reduced expression $\underline w$를 사용한다. 다른 reduced expressions에서 얻은 cellular crystals는 braid-type crystal isomorphisms로 연결되지만, 좌표계 자체가 문자 그대로 같은 것은 아니다.

### Connectedness consequence

이 isomorphism의 응용으로 cellular crystal $\mathcal B_w$는 connected crystal graph가 된다.

### B(infinity)-based avatar

$\mathcal B(w)$는 $B(w)\subset B(\infty)$에서 얻는 crystal-level avatar이다. 이 avatar는 localized upper global basis $\widetilde{\mathbf G}^{\mathrm{up}}(w)$와 localized simple-object classes를 동시에 index한다.

Categorification 관점에서는 coordinate ring의 element를 localized category의 simple object class로 읽는다. 따라서 coordinate-ring-level automorphism을 categorify한다는 것은, 그 automorphism이 Grothendieck ring에서 어떤 functor가 유도하는 map으로 보이는지를 찾는다는 뜻이다.

이 dictionary에서는 quantum twist automorphism $\eta_w$가 localized category의 right dual functor와 연결된다. 방향을 정확히 말하면, $\eta_w$는 simple-object class 쪽에서 inverse right dual functor가 유도하는 작용과 맞고, 이에 대응하는 crystal operation의 inverse가 $\mathcal B(w)$ 위에서 나타난다. 반대로 $\mathfrak D_w$ 자체는 right dual functor와 대응한다.

따라서 여기서 중요한 의미는 구체 좌표식이 아니라, twist automorphism이 categorification 쪽에서 duality functor로 보인다는 점이다. Localized crystal은 basis elements, simple objects, duality operation을 한 crystal-level language 안에서 비교하게 해 준다.

## 다른 topic들과의 관계

[[topics/08-localization-of-categories/quiver-hecke-category-localization|Quiver-Hecke Category Localization]]은 $\widetilde{\mathcal C}_w$를 만드는 category-level localization을 제공한다. Localized crystal은 이 category의 simple objects 위에 만들어진다.

[[topics/06-quiver-hecke-klr-algebras/demazure-subcategories-of-quiver-hecke-modules|Demazure Subcategories of Quiver-Hecke Modules]]는 $\operatorname{CP}$를 먼저 정의하는 category-level input $\mathfrak B_w$를 제공한다. 여기서 recursive coordinate extraction이 시작된다.

[[topics/02-crystal-bases/crystal-bases|Crystal Bases]]는 crystal operators와 crystal morphisms의 일반 crystal-level language를 제공한다. Localized crystal은 이 language를 category-level simple objects 위에 실현한다.

[[topics/02-crystal-bases/b-infinity-crystal|The Crystal B(infinity)]]는 $B(w)$가 들어 있는 ambient crystal을 제공한다. 여기서 $B(w)$를 frozen directions로 확장하면 $\mathcal B(w)$가 되고, 이 object가 localized basis와 localized simple objects를 잇는다.

[[topics/02-crystal-bases/cellular-crystals|Cellular Crystals]]는 localized simple-object crystal이 비교되는 target crystal이다. $\operatorname{CP}$는 localized simple objects를 cellular coordinates로 보낸다.

[[topics/08-localization-of-categories/localized-root-operators|Localized Root Operators]]는 $\widetilde E_i,\widetilde F_i$와 starred operators가 어떻게 정의되는지 설명한다. Localized Crystals에서는 그 operators가 만드는 crystal structure와 comparison map을 다룬다.

[[topics/06-quiver-hecke-klr-algebras/determinantial-modules|Determinantial Modules]]는 localization에서 invertible하게 되는 central objects를 제공한다.

[[topics/05-monoidal-categorification/monoidal-categorification|Monoidal Categorification]]은 $\widetilde{\mathcal C}_w$가 cluster algebra를 categorify하는 상황을 설명한다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/02-crystal-bases/crystal-bases|Crystal Bases]]에서 abstract crystal language를 읽고, [[topics/02-crystal-bases/b-infinity-crystal|The Crystal B(infinity)]]에서 $B(\infty)$와 $B(w)$가 들어갈 ambient crystal을 읽고, [[topics/02-crystal-bases/cellular-crystals|Cellular Crystals]]에서 combinatorial target을 읽고, [[topics/06-quiver-hecke-klr-algebras/demazure-subcategories-of-quiver-hecke-modules|Demazure Subcategories of Quiver-Hecke Modules]]에서 $\mathfrak B_w$와 $B_w(\infty)$의 category-level realization을 읽고, [[topics/08-localization-of-categories/quiver-hecke-category-localization|Quiver-Hecke Category Localization]]에서 $\widetilde{\mathcal C}_w$를 읽는다.
- 상위 개념: [[topics/02-crystal-bases/crystal-bases|Crystal Bases]]와 [[topics/08-localization-of-categories/quiver-hecke-category-localization|Quiver-Hecke Category Localization]]이 더 넓은 배경이다.
- 다음에 읽을 것: [[topics/08-localization-of-categories/localized-root-operators|Localized Root Operators]]에서는 localized root operators의 정의를 읽고, [[topics/02-crystal-bases/cellular-crystals|Cellular Crystals]]에서는 $\operatorname{CP}$의 target 좌표 model을 읽고, [[topics/05-monoidal-categorification/monoidal-categorification|Monoidal Categorification]]에서는 cluster-algebra context를 읽고, [[topics/06-quiver-hecke-klr-algebras/determinantial-modules|Determinantial Modules]]에서는 crystal construction 전에 invertible하게 만드는 objects를 읽는다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/kashiwara-nakashima25-crystal-structure-localized-quantum-unipotent-coordinate-category|Kashiwara-Nakashima 2025]], Abstract and Sections 5.1-5.2: construction of $\widetilde{\mathcal C}_w$ by localization.
- Kashiwara-Nakashima 2025, Definition 6.11 and Theorem 6.13: root operators and the crystal structure on $\operatorname{Irr}(\widetilde{\mathcal C}_w)$.
- Kashiwara-Nakashima 2025, Section 6.4: recursive definition of $\operatorname{CP}$ and its extension to localized simple objects.
- Kashiwara-Nakashima 2025, Main Theorem 7.1 and the following corollary: crystal-operator compatibility and crystal morphism statement.
- Kashiwara-Nakashima 2025, Proposition 9.2 and Main Theorem 9.3: bijectivity and crystal isomorphism with $\mathcal B_w$.
- Kashiwara-Nakashima 2025, Example 9.6: compact type $A_3$ example for the $\operatorname{CP}$ formula on one cluster monomial.
- Exact line review: `reports/reviews/2026-06-01-crystal-comparison-map-source-location-review.md`.
- Example review: `reports/reviews/2026-06-01-crystal-comparison-map-a3-example-review.md`.
- [[sources/papers/kashiwara93-crystal-base-demazure-character-formula|Kashiwara 1993]], Sections 1.2-1.3: general crystal, morphism, and tensor-product background.
- [[sources/papers/jp25-crystals-quantum-twist-automorphisms|Jung-Park 2025]], local TeX lines 1480-1555: \(B(w)\subset B(\infty)\), frozen crystal elements, the localized crystal \(\mathcal B(w)\), the bijections with \(\widetilde{\mathbf G}^{\mathrm{up}}(w)\) and localized simple objects, and the permutation \(\mathfrak D_w\) corresponding to quantum twist/right duality.

</details>
