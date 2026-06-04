---
id: quiver-hecke-module-categories
title: Quiver-Hecke Module Categories
level: core
topic_kind: category
parent_topics:
  - quiver-hecke-algebras
prerequisite_topics:
  - quiver-hecke-algebras
child_topics:
  - type-a-klr-segment-modules
  - quiver-hecke-subcategories
  - r-matrix-renormalization
  - shuffle-lemmas-for-quiver-hecke-modules
  - head-simplicity-of-convolutions
related_topics:
  - monoidal-categorification
maturity: example-ready
---

## 개요

Quiver-Hecke module category는 quiver-Hecke algebra의 graded modules를 모은 category-level object이다. Algebra $H_\alpha$ 자체는 generator와 relation으로 정의되는 object-level algebra이고, 그 modules를 모은 category에서는 convolution product, Grothendieck group, induction과 restriction 같은 category-level 구조를 다룬다.

Quiver-Hecke algebra에서 localization에 쓰이는 subcategory로 넘어가려면 먼저 module category layer를 거쳐야 한다. Localization에서 쓰는 $\mathcal C_w$는 quiver-Hecke algebra 자체가 아니라 이런 module category 안의 monoidal subcategory로 놓인다.

## 준비와 notation

$\alpha\in Q_+$에 대해 $H_\alpha$를 quiver-Hecke algebra라고 하자. 여러 $\alpha$에 대한 algebras를 한꺼번에 다룰 때는 $R$을 generic quiver-Hecke algebra notation으로 쓴다.

$R\text{-gmod}$는 finite-dimensional graded $R$-modules의 category를 뜻한다. 두 objects $M,N$의 category-level product는 convolution product
$$
M\circ N
$$
으로 쓴다. Grothendieck-ring level에서는 object $M$의 class를 $[M]$ 또는 $[M]\in K_0(\mathcal C)$로 쓴다.

## 정의

### Graded module category

Quiver-Hecke module category는 quiver-Hecke algebra $H_\alpha$ 또는 그 family에서 얻는 graded module category이다. 이 category의 objects는 graded $H_\alpha$-modules이고, morphisms는 grading을 보존하는 module homomorphisms로 읽는다.

### Monoidal structure

Symmetric quiver-Hecke setting에서 이후 topic들은 이 module categories를 $R\text{-gmod}$라고 쓰고, convolution product $M\circ N$을 monoidal product로 사용한다. 따라서 $R\text{-gmod}$는 quiver-Hecke algebra presentation에서 monoidal categorification과 localization으로 넘어가는 category-level ambient space이다.

## 기본 예시

### 실제 예시

Type $A_2$의 quiver underlying graph가 $1-2$이고 $\alpha=\alpha_1+\alpha_2$일 때, degree shift를 제외한 irreducible graded $H_\alpha$-modules는 $L(12)$와 $L(21)$ 두 개이다. 여기서 $12$와 $21$은 weight $\alpha_1+\alpha_2$를 갖는 words를 표시한다.

Simple modules $L(1)$과 $L(2)$의 convolution product는 두 순서에서 다음 graded characters를 갖는다.

$$
\operatorname{Ch}(L(1)\circ L(2))=12+q21,
$$

$$
\operatorname{Ch}(L(2)\circ L(1))=21+q12.
$$

따라서 같은 두 simple factors를 사용하더라도 convolution의 factor order가 graded character에 나타난다. 이 예시는 [[topics/06-quiver-hecke-klr-algebras/type-a-klr-segment-modules|Type A KLR Segment Modules]]에서 interval-shaped modules를 읽기 전에, convolution product가 실제 category-level operation이라는 점을 보여준다.

검증: 문헌 예시

## 핵심 관점

$$
H_\alpha
\quad\leadsto\quad
H_\alpha\text{-gmod}
\quad\leadsto\quad
R\text{-gmod}
\quad\leadsto\quad
K_0(\mathcal C)
$$

첫 번째 단계는 algebra-level에서 category-level로 넘어가는 단계이다. 마지막 단계는 objects와 convolution product를 Grothendieck-ring-level multiplication으로 내려보내는 단계이다.

## 기본 성질

### Induction과 restriction

Quiver-Hecke category의 horizontal composition은 $\beta,\gamma\in Q_+$에 대해 non-unital algebra embedding
$$
H_\beta\otimes H_\gamma\hookrightarrow H_{\beta+\gamma}
$$
을 준다. 이 embedding에서 오는 idempotent를 사용하면 induction functor $\operatorname{Ind}_{\beta,\gamma}^{\beta+\gamma}$와 restriction functor $\operatorname{Res}_{\beta,\gamma}^{\beta+\gamma}$가 정의된다.

두 graded modules $X\in H_\beta\text{-gmod}$, $Y\in H_\gamma\text{-gmod}$에 대해 convolution product는
$$
X\circ Y=\operatorname{Ind}_{\beta,\gamma}^{\beta+\gamma}(X\boxtimes Y)
$$
이다. 따라서 induction은 module category의 monoidal product를 만들고, restriction은 Grothendieck group에서 그 product와 짝을 이루는 comultiplication을 만든다.

### Simple objects와 categorification

Symmetric quiver-Hecke setting에서는 real simple modules와 commuting simple modules를 사용해 convolution product의 simple behavior를 추적한다. Monoidal categorification에서는 category 안의 real simple objects가 cluster monomials의 classes를 대표하는 역할을 한다.

## 다른 topic들과의 관계

**Quiver-Hecke Algebras.** [[topics/06-quiver-hecke-klr-algebras/quiver-hecke-algebras|Quiver-Hecke Algebras]]는 $H_\alpha$의 generators, relations, grading을 제공한다. 여기서는 그 algebra들을 modules의 category로 올려서 읽는다.

**Type A KLR Segment Modules.** [[topics/06-quiver-hecke-klr-algebras/type-a-klr-segment-modules|Type A KLR Segment Modules]]는 type $A_\infty$ KLR category에서 segment modules와 ordered multisegment parameter를 제공한다.

**Quiver-Hecke Subcategories.** [[topics/06-quiver-hecke-klr-algebras/quiver-hecke-subcategories|Quiver-Hecke Subcategories]]는 $R\text{-gmod}$ 안의 $\mathcal C_w$와 $\mathcal C_{w,v}$ 같은 subcategories를 다룬다. Localization path에서는 이 subcategory layer가 다음 단계이다.

**Monoidal Categorification.** [[topics/05-monoidal-categorification/monoidal-categorification|Monoidal Categorification]]은 module category의 Grothendieck ring을 cluster algebra나 quantum cluster algebra와 비교하는 framework이다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/06-quiver-hecke-klr-algebras/quiver-hecke-algebras|Quiver-Hecke Algebras]]에서 algebra presentation을 읽는다.
- 상위 개념: [[topics/06-quiver-hecke-klr-algebras/quiver-hecke-algebras|Quiver-Hecke Algebras]]가 더 넓은 algebraic source이다.
- 다음에 읽을 것: type $A$ Schur-Weyl 예시가 필요하면 [[topics/06-quiver-hecke-klr-algebras/type-a-klr-segment-modules|Type A KLR Segment Modules]]를 먼저 읽는다. Localization 방향으로 가려면 [[topics/06-quiver-hecke-klr-algebras/quiver-hecke-subcategories|Quiver-Hecke Subcategories]]에서 $\mathcal C_w$와 $\mathcal C_{w,v}$를 읽고, [[topics/05-monoidal-categorification/monoidal-categorification|Monoidal Categorification]]에서는 Grothendieck-ring comparison을 읽는다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/brundan13-quiver-hecke-algebras-categorification|Brundan 2013]], Sections 2-3: quiver-Hecke algebras, graded modules, and Grothendieck-group categorification.
- Brundan 2013, Section 3, arXiv p.18: type $A_2$ example where the irreducible graded $H_{\alpha_1+\alpha_2}$-modules up to degree shift are $L(12)$ and $L(21)$.
- [[sources/papers/kkko14-monoidal-categorification-cluster-algebras|KKKO14]], Definitions 1.7 and 2.12, and Proposition 2.13: real simple modules, commuting simple modules, and convolution products for symmetric quiver-Hecke algebras.

</details>
