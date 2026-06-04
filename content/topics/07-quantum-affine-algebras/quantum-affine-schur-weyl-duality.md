---
id: quantum-affine-schur-weyl-duality
title: Quantum Affine Schur-Weyl Duality
level: advanced
topic_kind: construction
parent_topics:
  - quantum-affine-algebras
prerequisite_topics:
  - quantum-affine-r-matrix-denominators
  - hernandez-leclerc-categories
  - quiver-hecke-module-categories
  - type-a-klr-segment-modules
  - r-matrix-renormalization
  - affine-objects-in-monoidal-categories
child_topics: []
related_topics:
  - monoidal-categorification
  - quiver-hecke-algebras
maturity: example-ready
---

## 개요

Quantum affine Schur-Weyl duality는 quiver-Hecke algebra의 module category와 quantum affine algebra의 finite-dimensional module category를 monoidal functor로 비교하는 construction이다. 중심 functor는
$$
\mathcal F_{\mathscr D}:R_{\mathsf C}\operatorname{-gmod}\longrightarrow \mathcal C_{\mathfrak g}
$$
이다.

여기서 source category는 symmetric quiver-Hecke algebra $R_{\mathsf C}$의 finite-dimensional graded modules이고, target category는 quantum affine algebra $U_q'(\mathfrak g)$의 finite-dimensional integrable modules로 이루어진 category $\mathcal C_{\mathfrak g}$이다. Functor를 만들려면 target category 안에서 quiver-Hecke Cartan matrix를 반영하는 simple modules의 family를 골라야 한다.

이 construction이 중요한 이유는 두 종류의 tensor product를 같은 언어로 비교하게 해 주기 때문이다. Strong duality datum이 주어지면 simple modules가 simple modules로 가고, R-matrix degree invariants가 보존되며, Grothendieck ring level의 injective map도 얻는다.

## 준비와 notation

$\mathsf C=(c_{ij})_{i,j\in J}$를 symmetric generalized Cartan matrix라고 하자. $R_{\mathsf C}$는 이에 붙는 symmetric quiver-Hecke algebra이고,
$$
R_{\mathsf C}\operatorname{-gmod}
$$
는 finite-dimensional graded $R_{\mathsf C}$-modules의 category이다.

$U_q'(\mathfrak g)$는 quantum affine algebra의 derived part이고,
$$
\mathcal C_{\mathfrak g}
$$
는 finite-dimensional integrable $U_q'(\mathfrak g)$-modules의 monoidal category이다. Hernandez-Leclerc category $\mathcal C_{\mathfrak g}^0$는 이 category 안의 주요 subcategory이다.

Simple object $M$이 real이라는 것은 $M\otimes M$이 simple이라는 뜻이다. Quantum affine category에서 $M$의 right dual과 left dual은 각각
$$
M^*,\qquad {}^*M
$$
로 쓴다. 정수 $k$에 대해 $M^{*k}$는 $k>0$이면 right dual을 $k$번 취한 object, $k<0$이면 left dual을 $-k$번 취한 object, $k=0$이면 $M$ 자체를 뜻한다.

두 simple objects 사이의 R-matrix degree invariant는
$$
\mathfrak d(M,N)
$$
로 쓴다. 이 invariant의 construction은 [[topics/06-quiver-hecke-klr-algebras/r-matrix-renormalization|R-Matrix Renormalization]]에서 쓰는 renormalized R-matrix language와 연결된다.

구성 수준에서는 선택된 $U_q'(\mathfrak g)$-modules와 spectral parameters도 사용한다. 선택된 두 modules 사이의 normalized R-matrix denominator가 quiver-Hecke algebra 쪽 Cartan data와 KLR parameters를 정하는 방식은 [[topics/07-quantum-affine-algebras/quantum-affine-r-matrix-denominators|Quantum Affine R-Matrix Denominators]]에서 분리해서 읽는다. Type $A$ 예시에서 functor에 넣는 구체적인 KLR-side modules는 [[topics/06-quiver-hecke-klr-algebras/type-a-klr-segment-modules|Type A KLR Segment Modules]]에서 고정한다.

## 구성

### Duality datum

Quantum affine Schur-Weyl functor의 입력은 duality datum이다. Simple modules의 family
$$
\mathscr D=\{\mathcal R_i\}_{i\in J}\subset\mathcal C_{\mathfrak g}
$$
가 Cartan matrix $\mathsf C$에 대한 duality datum이라는 것은 다음 두 조건을 만족한다는 뜻이다.

1. 각 $\mathcal R_i$는 real simple module이다.
2. $i\ne j$이면
   $$
   \mathfrak d(\mathcal R_i,\mathcal R_j)=-c_{ij}
   $$
   이다.

### Functor

이 data가 주어지면 quiver-Hecke category에서 quantum affine category로 가는 monoidal functor
$$
\mathcal F_{\mathscr D}:R_{\mathsf C}\operatorname{-gmod}\longrightarrow \mathcal C_{\mathfrak g}
$$
를 만든다. 이 functor가 quantum affine Schur-Weyl duality functor이다.

### Construction mechanism

구성의 핵심은 다음과 같다. 먼저 각 $\mathcal R_i$의 affinization을 사용하여 tensor products
$$
\mathcal R_{\nu_1}^{\mathrm{Aff}}\otimes\cdots\otimes
\mathcal R_{\nu_\ell}^{\mathrm{Aff}}
$$
을 만든다. 그런 다음 renormalized R-matrices를 이용해 이 object 위에 quiver-Hecke algebra $R_{\mathsf C}$의 오른쪽 작용을 정의한다. $M\in R(\beta)\operatorname{-gmod}$에 대해 완성된 object와 tensor product를 취하면 $\mathcal F_{\mathscr D}(M)$이 얻어진다.

이 construction은 affine objects를 보존하도록 조정된다. 즉 quiver-Hecke side의 affinization을 먼저 한 뒤 functor를 적용하는 것과, functor를 적용한 뒤 quantum affine side에서 affinization을 하는 것이 compatible하다.

KKK18A의 construction-level form에서는 이 과정을 더 구체적으로 다음과 같이 쓴다. Denominator data로 quiver-Hecke algebra $R^J(\beta)$를 정한 뒤, 선택된 modules의 affinizations로 completed tensor object
$$
\widehat V^{\otimes\beta}
$$
를 만든다. Normalized R-matrices가 이 object 위의 오른쪽 quiver-Hecke action을 주며,
$$
F_\beta(M)=\widehat V^{\otimes\beta}\otimes_{R^J(\beta)}M
$$
으로 functor를 정의한다.

## 기본 예시

### 실제 예시

Type $A_{N-1}^{(1)}$ Schur-Weyl construction에서 [[topics/06-quiver-hecke-klr-algebras/type-a-klr-segment-modules|Type A KLR Segment Modules]]의 segment module $L(a,b)$는 functor $F$ 아래에서 fundamental representation으로 간다. [[topics/07-quantum-affine-algebras/quantum-affine-r-matrix-denominators|Quantum Affine R-Matrix Denominators]]에서 denominator data가 type $A_\infty$ KLR input을 만들고, 여기서는 그 input 위의 module $L(a,b)$를 functor에 넣는다. Segment $(a,b)$의 length를
$$
\ell=b-a+1
$$
이라고 하면, $0\le \ell\le N$일 때
$$
F(L(a,b))\simeq V(\varpi_\ell)_{(-q)^{a+b}}
$$
를 준다. 반면 $\ell>N$이면
$$
F(L(a,b))\simeq 0
$$
이다.

따라서 이 예시에서 functor $F$는 type $A_\infty$ KLR side의 interval $(a,b)$를 quantum affine side의 fundamental representation index $\ell$과 spectral parameter $(-q)^{a+b}$로 읽는다.

검증: 문헌 예시

## 핵심 관점

핵심 그림은 다음이다.

$$
R_{\mathsf C}\operatorname{-gmod}
\xrightarrow{\ \mathcal F_{\mathscr D}\ }
\mathcal C_{\mathfrak g}.
$$

왼쪽 category에서는 convolution product와 quiver-Hecke R-matrices를 사용한다. 오른쪽 category에서는 tensor product, spectral parameters, renormalized R-matrices를 사용한다. Quantum affine Schur-Weyl duality는 이 두 구조가 같은 combinatorial Cartan data를 보고 있음을 functorial하게 연결한다.

Duality datum $\mathscr D$는 이 비교의 dictionary 역할을 한다. Simple root direction에 해당하는 quiver-Hecke simple modules가 오른쪽의 chosen simple modules $\mathcal R_i$로 보내지고, 그 사이의 R-matrix degree가 Cartan matrix의 off-diagonal entries와 맞도록 고정된다.

Strong duality datum은 이 dictionary가 좋은 성질을 갖기 위한 강화 조건이다. 이 조건 아래에서는 단순히 functor가 존재하는 것을 넘어, simple modules와 R-matrix invariants가 안정적으로 비교된다.

## 기본 성질

**정의: root module.** Object $L\in\mathcal C_{\mathfrak g}$가 root module이라는 것은 $L$이 real simple module이고 모든 $k\in\mathbb Z$에 대해
$$
\mathfrak d(L,L^{*k})=\delta(k=\pm1)
$$
을 만족한다는 뜻이다. 여기서 $L^{*k}$는 iterated dual을 나타내는 notation이다.

**정의: strong duality datum.** Duality datum $\mathscr D=\{\mathcal R_i\}_{i\in J}$가 strong duality datum이라는 것은, 모든 $\mathcal R_i$가 root module이고 $i\ne j$에 대해
$$
\mathfrak d(\mathcal R_i,\mathcal R_j^{*k})
=-\delta(k=0)c_{ij}
\qquad(k\in\mathbb Z)
$$
를 만족한다는 뜻이다.

**정리: simple object 보존.** $\mathscr D$가 simply-laced finite type Cartan matrix에 대한 strong duality datum이면, duality functor $\mathcal F_{\mathscr D}$는 simple $R_{\mathsf C}$-modules를 simple objects of $\mathcal C_{\mathfrak g}$로 보낸다.

**정리: R-matrix invariant 비교.** 같은 strong duality datum 가정 아래에서 $\mathcal F_{\mathscr D}$는 simple modules 사이의 R-matrix degree invariants를 보존하거나 quantum affine side의 corresponding invariants로 해석한다. 특히 $\Lambda$, $\mathfrak d$, weight pairing, dual-shift degree data가 functor를 통해 비교된다.

**따름정리: Grothendieck ring map.** Strong duality datum의 경우 $\mathcal F_{\mathscr D}$는 Grothendieck ring level에서 injective ring homomorphism을 유도한다.

**정리: KKK18A tensor functor와 exactness.** KKK18A construction에서 functors $F_\beta$는 direct sum
$$
F=\bigoplus_\beta F_\beta
$$
을 통해 tensor functor를 이룬다. Associated quiver가 finite type ADE이면 각 $F_\beta$는 exact functor이다.

## 다른 topic들과의 관계

**Quantum Affine Algebras.** [[topics/07-quantum-affine-algebras/quantum-affine-algebras|Quantum Affine Algebras]]는 target category $\mathcal C_{\mathfrak g}$와 spectral-parameter/R-matrix language를 제공한다.

**Quantum Affine R-Matrix Denominators.** [[topics/07-quantum-affine-algebras/quantum-affine-r-matrix-denominators|Quantum Affine R-Matrix Denominators]]는 functor construction의 KLR input을 정하는 denominator-to-KLR-parameter step을 제공한다.

**Hernandez-Leclerc Categories.** [[topics/07-quantum-affine-algebras/hernandez-leclerc-categories|Hernandez-Leclerc Categories]]는 $\mathcal C_{\mathfrak g}$ 안에서 cluster algebra와 비교되는 subcategory를 제공하며, Schur-Weyl functor의 image를 읽는 category-level 배경이 된다.

**Quiver-Hecke Module Categories.** [[topics/06-quiver-hecke-klr-algebras/quiver-hecke-module-categories|Quiver-Hecke Module Categories]]는 source category $R_{\mathsf C}\operatorname{-gmod}$와 convolution product를 제공한다.

**Type A KLR Segment Modules.** [[topics/06-quiver-hecke-klr-algebras/type-a-klr-segment-modules|Type A KLR Segment Modules]]는 type $A$ 예시에서 functor에 넣는 구체적인 KLR modules $L(a,b)$와 ordered multisegment language를 제공한다.

**R-Matrix Renormalization.** [[topics/06-quiver-hecke-klr-algebras/r-matrix-renormalization|R-Matrix Renormalization]]은 functor construction과 invariant comparison에 들어가는 R-matrix degree language를 제공한다.

**Affine Objects in Monoidal Categories.** [[topics/03-category-theory/affine-objects-in-monoidal-categories|Affine Objects in Monoidal Categories]]는 functor가 affinizations와 compatible하다는 statement를 읽기 위한 categorical language를 제공한다.

**Monoidal Categorification.** [[topics/05-monoidal-categorification/monoidal-categorification|Monoidal Categorification]]은 Grothendieck ring으로 내려간 비교가 cluster algebra/categorification 문제로 이어지는 방향을 설명한다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/07-quantum-affine-algebras/quantum-affine-algebras|Quantum Affine Algebras]], [[topics/07-quantum-affine-algebras/quantum-affine-r-matrix-denominators|Quantum Affine R-Matrix Denominators]], [[topics/07-quantum-affine-algebras/hernandez-leclerc-categories|Hernandez-Leclerc Categories]], [[topics/06-quiver-hecke-klr-algebras/quiver-hecke-module-categories|Quiver-Hecke Module Categories]], [[topics/06-quiver-hecke-klr-algebras/type-a-klr-segment-modules|Type A KLR Segment Modules]]. Type $A$ 예시를 읽을 때는 denominator page에서 KLR input이 생기는 과정을 보고, segment-module page에서 $L(a,b)$를 고정한 뒤 이 page의 functor image를 읽는다.
- 상위 개념: [[topics/07-quantum-affine-algebras/quantum-affine-algebras|Quantum Affine Algebras]].
- 다음에 읽을 것: affine cuspidal modules와 PBW theory는 이 functor를 사용해 quantum affine category 안의 simple modules를 ordered tensor products로 구성하는 방향이다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/kkop24-pbw-theory-quantum-affine-algebras|Kashiwara-Kim-Oh-Park 2024]], local TeX lines 803-821 and 884-896: overall role of quantum affine Schur-Weyl duality, duality data, and the duality functor.
- Kashiwara-Kim-Oh-Park 2024, local TeX lines 2731-2747: definition of duality datum and existence of the monoidal functor $\mathcal F_{\mathscr D}$.
- Kashiwara-Kim-Oh-Park 2024, local TeX lines 2888-2948 and 2952-2971: modified construction using affinizations and compatibility with affinizations.
- Kashiwara-Kim-Oh-Park 2024, local TeX lines 2153-2159 and 3226-3249: root modules and strong duality data.
- Kashiwara-Kim-Oh-Park 2024, local TeX lines 3482-3522 and 3593-3612: simple-to-simple theorem, invariant comparison, and Grothendieck-ring consequence under strong duality datum hypotheses.
- [[sources/papers/kang-kashiwara-kim18-symmetric-quiver-hecke-algebras-r-matrices|Kang-Kashiwara-Kim 2018]], Section 3.1, arXiv PDF pp.26-30: R-matrix denominator data, KLR parameters, and the completed bimodule $\widehat V^{\otimes\beta}$.
- Kang-Kashiwara-Kim 2018, Section 3.2 and Theorem 3.3.3, arXiv PDF pp.30-33: the functor $F_\beta$, tensor functor property, and exactness in finite ADE type.
- Kang-Kashiwara-Kim 2018, Section 4.2 and Proposition 4.3.1, arXiv PDF pp.36 and 43-44: type $A$ segment modules and the compact image formula $F(L(a,b))$ used in the visible example; details are isolated in [[topics/06-quiver-hecke-klr-algebras/type-a-klr-segment-modules|Type A KLR Segment Modules]].

</details>
