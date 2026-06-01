---
id: crystal-comparison-map
title: Crystal Comparison Map
level: advanced
topic_kind: map
parent_topics:
  - localized-crystals
prerequisite_topics:
  - localized-root-operators
  - cellular-crystals
  - quiver-hecke-category-localization
  - demazure-subcategories-of-quiver-hecke-modules
child_topics: []
related_topics:
  - crystal-bases
maturity: example-ready
---

## 개요

Crystal comparison map은 localized category의 simple-object crystal
$$
\operatorname{Irr}(\widetilde{\mathcal C}_w)
$$
를 reduced expression에서 온 cellular crystal
$$
\mathcal B_{\underline w}
$$
로 보내는 map이다. 이 map은 category-level crystal operators로 얻은 구조와 tensor-product coordinates로 표현되는 combinatorial crystal이 같은 crystal이라는 것을 비교한다.

이 map이 필요한 이유는 $\operatorname{Irr}(\widetilde{\mathcal C}_w)$의 vertices가 category 안의 simple objects라서 직접 보기 어렵기 때문이다. Crystal comparison map은 이 simple objects를 integer coordinates로 읽게 해 주며, Kashiwara-Nakashima의 theorem은 이 coordinate map이 crystal isomorphism임을 말한다.

## 준비와 notation

$w\in W$를 고정하고, reduced expression을
$$
\underline w=s_{i_1}\cdots s_{i_\ell}
$$
로 둔다. 이 reduced expression에 붙은 target cellular crystal은
$$
\mathcal B_{\underline w}
=B_{i_1}\otimes\cdots\otimes B_{i_\ell}
$$
이다.

좌표 $(c_1,\ldots,c_\ell)$는
$$
\widetilde f_{i_1}^{c_1}(0)_{i_1}
\otimes\cdots\otimes
\widetilde f_{i_\ell}^{c_\ell}(0)_{i_\ell}
\in \mathcal B_{\underline w}
$$
로 읽는다. Reduced expression이 고정되어 있을 때 이 글에서는 comparison map을 $\operatorname{CP}$라고 쓴다.

Domain은 localized category $\widetilde{\mathcal C}_w$의 simple objects이다. 정확히는 grading shift까지 같은 것으로 보는 집합
$$
\operatorname{Irr}(\widetilde{\mathcal C}_w)
$$
위에서 map을 정의한다. Localization functor는
$$
\Phi_w:\mathcal C_w\to\widetilde{\mathcal C}_w
$$
로 쓴다.

$\widetilde E_i^*$는 [[topics/localized-root-operators|localized starred root operator]]이다. 또한 $\widetilde C_\Lambda$는 localization에서 determinantial object가 invertible하게 된 object를 나타내며, $\circ$는 localized monoidal category의 monoidal product를 나타낸다.

## map의 정의

먼저 category-level input $\mathfrak B_w$의 simple object $M$에 대해 map을 정의한다. $M_\ell=M$으로 두고, $k=\ell,\ell-1,\ldots,1$에 대해
$$
c_k=\varepsilon^*_{i_k}(M_k),
\qquad
M_{k-1}=(\widetilde E^*_{i_k})^{c_k}(M_k)
$$
를 반복해서 정의한다. 그러면
$$
\operatorname{CP}(M)=(c_1,\ldots,c_\ell)
\in \mathcal B_{\underline w}
$$
로 둔다.

다음으로 localized simple object가
$$
\widetilde C_\Lambda^{-1}\circ\Phi_w(M)
$$
꼴로 표현될 때, comparison map은
$$
\operatorname{CP}(\widetilde C_\Lambda^{-1}\circ\Phi_w(M))
=\operatorname{CP}(M)-\operatorname{CP}(\widetilde C_\Lambda)
$$
로 확장된다. 따라서 최종 map은
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
인 경우를 보자. 이때 quiver-Hecke subcategory는
$$
\mathcal C_w=\{M\in R\text{-gmod}\mid E_2M\simeq0\}
$$
로 주어진다.

이 예시에서 localized category $\widetilde{\mathcal C}_w$는 네 개의 clusters를 갖는 cluster algebra의 monoidal categorification으로 나타난다. 한 cluster의 monomial은
$$
\langle1\rangle^x\circ
\langle3\rangle^y\circ
\langle321\rangle^a\circ
\langle132\rangle^b\circ
\langle123\rangle^c
$$
처럼 쓸 수 있다. 여기서 $x,y\in\mathbb Z_{\ge0}$이고 $a,b,c\in\mathbb Z$이다.

이 monomial에 대해 comparison map은
$$
\operatorname{CP}(
\langle1\rangle^x\circ
\langle3\rangle^y\circ
\langle321\rangle^a\circ
\langle132\rangle^b\circ
\langle123\rangle^c)
=(c+b,c,y+a+b+c,a+b,x+a)
$$
를 준다. 따라서 이 example에서는 category 안의 localized cluster monomial이 five-coordinate cellular-crystal point로 바뀐다.

검증: 논문 예시

## 핵심 관점

핵심은 category-level vertex를 cellular-crystal coordinate로 바꾸는 것이다.
$$
\operatorname{Irr}(\widetilde{\mathcal C}_w)
\xrightarrow{\;\operatorname{CP}\;}
\mathcal B_{\underline w}
=B_{i_1}\otimes\cdots\otimes B_{i_\ell}
$$

정의 단계에서는 simple object에 starred root operators를 반복 적용하여 coordinate를 뽑는다. Theorem 단계에서는 이 coordinate extraction이 crystal operators와 호환된다는 것을 증명한다.

## 기본 성질

- $\operatorname{CP}$는 crystal morphism이다. Domain의 crystal structure는 localized root operators로 주어지고, codomain의 crystal structure는 cellular crystal의 tensor-product crystal structure이다.
- $\operatorname{CP}$는 bijective이다.
- 따라서 $\operatorname{CP}$는
  $$
  \operatorname{Irr}(\widetilde{\mathcal C}_w)
  \simeq
  \mathcal B_{\underline w}
  $$
  라는 crystal isomorphism을 준다.
- Coordinate map은 reduced expression $\underline w$를 사용한다. 다른 reduced expressions에서 얻은 cellular crystals는 braid-type crystal isomorphisms로 연결되지만, 좌표계 자체가 문자 그대로 같은 것은 아니다.

## 다른 topic들과의 관계

- [[topics/localized-root-operators|Localized Root Operators]]는 $\operatorname{Irr}(\widetilde{\mathcal C}_w)$ 위의 crystal operators를 제공한다.
- [[topics/cellular-crystals|Cellular Crystals]]는 comparison map의 codomain인 $\mathcal B_{\underline w}$를 제공한다.
- [[topics/localized-crystals|Localized Crystals]]는 이 map이 비교하는 category-level crystal structure의 전체 construction이다.
- [[topics/quiver-hecke-category-localization|Quiver-Hecke Category Localization]]은 $\widetilde{\mathcal C}_w$와 localization functor $\Phi_w$가 나오는 category-level 배경이다.
- [[topics/demazure-subcategories-of-quiver-hecke-modules|Demazure Subcategories of Quiver-Hecke Modules]]는 comparison map을 정의하기 전에 필요한 $\mathcal C_w$와 $\mathfrak B_w$ 쪽 input을 제공한다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/localized-root-operators|Localized Root Operators]]에서 $\widetilde E_i^*$를 읽고, [[topics/cellular-crystals|Cellular Crystals]]에서 $\mathcal B_{\underline w}$를 읽고, [[topics/quiver-hecke-category-localization|Quiver-Hecke Category Localization]]에서 $\widetilde{\mathcal C}_w$와 $\Phi_w$를 읽는다.
- 상위 개념: [[topics/localized-crystals|Localized Crystals]]가 더 넓은 crystal-level construction이다.
- 다음에 읽을 것: [[topics/reverse-equivalence-of-localized-categories|Reverse Equivalence of Localized Categories]]에서는 localized category 주변의 reverse-category input을 읽고, [[topics/demazure-subcategories-of-quiver-hecke-modules|Demazure Subcategories of Quiver-Hecke Modules]]에서는 localization 이전의 category input을 읽는다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/kashiwara-nakashima25-crystal-structure-localized-quantum-unipotent-coordinate-category|Kashiwara-Nakashima 2025]], Section 2.4: cellular crystal $\mathcal B_{\underline w}$ and coordinate notation.
- Kashiwara-Nakashima 2025, Sections 5.1-5.2: localized category $\widetilde{\mathcal C}_w$ and localization functors.
- Kashiwara-Nakashima 2025, Section 6.4: recursive definition of $\operatorname{CP}$ and its extension to localized simple objects.
- Kashiwara-Nakashima 2025, Main Theorem 7.1 and the following corollary: crystal-operator compatibility and crystal morphism statement.
- Kashiwara-Nakashima 2025, Proposition 9.2 and Main Theorem 9.3: bijectivity and crystal isomorphism.
- Kashiwara-Nakashima 2025, Example 9.6: compact type $A_3$ example for the $\operatorname{CP}$ formula on one cluster monomial.
- Exact line review: `reports/reviews/2026-06-01-crystal-comparison-map-source-location-review.md`.
- Example review: `reports/reviews/2026-06-01-crystal-comparison-map-a3-example-review.md`.
- Demazure input notation review: `reports/reviews/2026-06-01-demazure-subcategories-source-location-review.md`.

</details>
