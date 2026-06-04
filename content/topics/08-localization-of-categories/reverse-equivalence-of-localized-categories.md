---
id: reverse-equivalence-of-localized-categories
title: Reverse Equivalence of Localized Categories
level: advanced
topic_kind: theorem
parent_topics:
  - quiver-hecke-category-localization
prerequisite_topics:
  - quiver-hecke-category-localization
  - quiver-hecke-module-categories
child_topics: []
related_topics:
  - localized-crystals
maturity: definition-ready
---

## 개요

Reverse equivalence of localized categories는 localized category $\widetilde{\mathcal C}_w$와 inverse Weyl group element에 붙은 localized category $\widetilde{\mathcal C}_{w^{-1}}$를 연결하는 monoidal equivalence이다. Statement는
$$
(\widetilde{\mathcal C}_w)^{\mathrm{rev}}
\simeq
\widetilde{\mathcal C}_{w^{-1}}
$$
이다.

여기서 $\mathrm{rev}$는 tensor product의 순서를 뒤집는다는 뜻이다. 이 equivalence는 object-level left/right duality와 같은 말이 아니다. Category-level에서 convolution order를 뒤집은 뒤, $w$에 붙은 localization을 $w^{-1}$에 붙은 localization과 비교하는 구조이다.

이 equivalence는 localized crystal theory에서 ordinary localized operators와 starred localized operators를 비교하는 배경으로 쓰인다. Connectedness argument에서는 $\operatorname{Irr}(\widetilde{\mathcal C}_w)$의 crystal structure와 $\operatorname{Irr}(\widetilde{\mathcal C}_{w^{-1}})$의 starred crystal structure를 연결하는 데 사용된다.

## 준비와 notation

$R\text{-gmod}$는 quiver-Hecke algebra $R$의 finite-dimensional graded module category이다. $w\in W$에 대해 $\mathcal C_w$는 $R\text{-gmod}$ 안의 monoidal subcategory이고, $\widetilde{\mathcal C}_w$는 determinantial objects를 invertible하게 만든 localization이다.

세 종류의 operation을 구분해야 한다. 첫째, $\mathscr C^{\mathrm{rev}}$는 monoidal category의 tensor product order를 바꾸는 category-level operation이다. 둘째, $\psi_*$는 quiver-Hecke module category에서 word order를 뒤집어 얻는 monoidal equivalence이다. 셋째, $\mathscr D$와 $\mathscr D^{-1}$는 object-level right and left duality이다.

Monoidal category $\mathscr C$에 대해 $\mathscr C^{\mathrm{rev}}$는 같은 objects와 morphisms를 가지지만 tensor product를
$$
M\otimes_{\mathrm{rev}}N:=N\otimes M
$$
로 뒤집은 monoidal category이다.

Automorphism $\psi:R(\beta)\to R(\beta)$는 idempotent word와 generators를 다음처럼 뒤집는다.
$$
\psi(e(\nu_1,\ldots,\nu_n))=e(\nu_n,\ldots,\nu_1),
\qquad
\psi(x_k)=x_{n+1-k},
\qquad
\psi(\tau_l)=-\tau_{n-l}.
$$
이 $\psi$는 monoidal equivalence
$$
\psi_*:(R\text{-gmod})^{\mathrm{rev}}\simeq R\text{-gmod}
$$
를 유도한다.

Localization functor는
$$
Q_w:R\text{-gmod}\to\widetilde{\mathcal C}_w,
\qquad
Q_{w^{-1}}:R\text{-gmod}\to\widetilde{\mathcal C}_{w^{-1}}
$$
로 표시한다. Object-level right dual과 left dual은 각각 $\mathscr D(X)$와 $\mathscr D^{-1}(X)$로 쓴다.

## 정리의 진술

Reverse equivalence theorem은 monoidal equivalence
$$
\psi_*:
(\widetilde{\mathcal C}_w)^{\mathrm{rev}}
\xrightarrow{\sim}
\widetilde{\mathcal C}_{w^{-1}}
$$
이다. 이 equivalence는 ambient equivalence
$$
\psi_*:(R\text{-gmod})^{\mathrm{rev}}\simeq R\text{-gmod}
$$
와 localization functors $Q_w,Q_{w^{-1}}$가 compatible하도록 내려온다. 즉 먼저 $R\text{-gmod}$에서 tensor order reversal을 만든 뒤, localization을 거쳐도 같은 reversal 구조가 남는다.

Compatibility의 핵심 input은 determinantial modules의 변환이다. $w$-dominant weight $\lambda$에 대해
$$
\psi_*\bigl(\mathsf M_w(w\lambda,\lambda)\bigr)
\simeq
\mathsf M_{w^{-1}}(-\lambda,-w\lambda)
$$
를 사용한다. 이 때문에 $w$ 쪽 localization data가 reversed tensor product 아래에서 $w^{-1}$ 쪽 localization data로 이동한다.

## 핵심 관점

핵심 diagram은 ambient category equivalence가 localized categories의 equivalence로 내려간다는 것이다.
$$
\begin{array}{ccc}
(R\text{-gmod})^{\mathrm{rev}}
& \xrightarrow{\ \psi_*\ } &
R\text{-gmod}
\\
\downarrow Q_w && \downarrow Q_{w^{-1}}
\\
(\widetilde{\mathcal C}_w)^{\mathrm{rev}}
& \xrightarrow{\ \psi_*\ } &
\widetilde{\mathcal C}_{w^{-1}}
\end{array}
$$

위쪽은 quiver-Hecke module category 자체의 reversal이다. 아래쪽은 determinantial objects를 invertible하게 만든 뒤에도 같은 reversal이 살아남는다는 statement이다.

따라서 이 theorem을 읽을 때 핵심은 dual object를 계산하는 것이 아니다. 핵심은 convolution product의 순서를 뒤집는 category-level operation이 localization과 호환되고, 그 결과 $w$ 쪽 category가 $w^{-1}$ 쪽 category로 이동한다는 점이다.

## 기본 성질

### Rigidity와 duality

$\widetilde{\mathcal C}_w$는 rigid monoidal category이다. 따라서 각 object는 right dual $\mathscr D(X)$와 left dual $\mathscr D^{-1}(X)$를 갖는다. 하지만 reverse equivalence 자체는 object duality functor가 아니다.

### Tensor order reversal

Reverse equivalence는 monoidal product의 순서를 바꾸는 category-level equivalence이다. Domain이 $\widetilde{\mathcal C}_w$가 아니라 $(\widetilde{\mathcal C}_w)^{\mathrm{rev}}$라는 점이 중요하다.

### Weyl group inverse

$\psi_*$는 $w$ 쪽 localized category를 $w^{-1}$ 쪽 localized category와 비교한다. Determinantial modules의 compatibility는 이 이동이 localization data와 맞아떨어지게 하는 input이다.

### Crystal-level use

Crystal level에서는 이 equivalence가 ordinary localized operators와 starred localized operators를 비교하는 데 사용된다. Connectedness argument에서는
$$
\psi_*:
\bigl(\operatorname{Irr}(\widetilde{\mathcal C}_w),
\{\widetilde E_i,\widetilde F_i\}_{i\in I}\bigr)
\simeq
\bigl(\operatorname{Irr}(\widetilde{\mathcal C}_{w^{-1}}),
\{\widetilde E_i^*,\widetilde F_i^*\}_{i\in I}\bigr)
$$
를 사용한다.

## 다른 topic들과의 관계

[[topics/08-localization-of-categories/quiver-hecke-category-localization|Quiver-Hecke Category Localization]]은 $\widetilde{\mathcal C}_w$와 localization functors가 나오는 parent construction이다. Reverse equivalence는 이 localized category construction에 tensor order reversal을 더한 theorem-level statement이다.

[[topics/08-localization-of-categories/localized-root-operators|Localized Root Operators]]는 ordinary operators와 starred operators를 제공한다. Reverse equivalence는 이 두 종류의 operators가 서로 비교되는 category-level 배경이다.

[[topics/08-localization-of-categories/localized-crystals|Localized Crystals]]는 $\operatorname{Irr}(\widetilde{\mathcal C}_w)$ 위의 crystal structure가 사는 곳이다. Reverse equivalence는 localized simple-object crystal을 cellular crystal과 비교하는 주변에서 $w$와 $w^{-1}$, ordinary operators와 starred operators를 구별하게 해 주는 input이다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/08-localization-of-categories/quiver-hecke-category-localization|Quiver-Hecke Category Localization]]에서 $\widetilde{\mathcal C}_w$와 localization functors를 읽고, [[topics/06-quiver-hecke-klr-algebras/quiver-hecke-module-categories|Quiver-Hecke Module Categories]]에서 $R\text{-gmod}$와 convolution order를 읽는다.
- 상위 개념: [[topics/08-localization-of-categories/quiver-hecke-category-localization|Quiver-Hecke Category Localization]]가 더 넓은 localized category construction이다.
- 다음에 읽을 것: [[topics/08-localization-of-categories/localized-root-operators|Localized Root Operators]]에서는 ordinary and starred operators를 읽고, [[topics/08-localization-of-categories/localized-crystals|Localized Crystals]]에서는 이 equivalence의 crystal-level use를 읽는다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/kashiwara-nakashima25-crystal-structure-localized-quantum-unipotent-coordinate-category|Kashiwara-Nakashima 2025]], Definition 3.1: right dual, left dual, and rigid monoidal category notation.
- Kashiwara-Nakashima 2025, Theorem 5.3: rigidity of $\widetilde{\mathcal C}_w$.
- Kashiwara-Nakashima 2025, Section 5.3 and Theorem 5.7: reverse monoidal equivalence $(\widetilde{\mathcal C}_w)^{\mathrm{rev}}\simeq\widetilde{\mathcal C}_{w^{-1}}$.
- Kashiwara-Nakashima 2025, Lemma 5.6: behavior of determinantial modules under $\psi_*$.
- Kashiwara-Nakashima 2025, Section 9.2: use of $\psi_*$ to compare ordinary and starred localized crystal operators.
- Exact line review: `reports/reviews/2026-06-01-localized-category-duality-source-location-review.md`.

</details>
