---
id: hernandez-leclerc-categories
title: Hernandez-Leclerc Categories
level: advanced
topic_kind: category
parent_topics:
  - quantum-affine-algebras
prerequisite_topics:
  - quantum-affine-algebras
  - cluster-algebras
  - monoidal-categorification
child_topics: []
related_topics:
  - quantum-cluster-algebras
  - quiver-hecke-module-categories
maturity: example-ready
---

## 개요

Hernandez-Leclerc categories는 quantum affine algebra의 finite-dimensional representation category 안에서 고른 full monoidal subcategories $\mathcal C_\ell$이다. 이 subcategories는 composition factors의 Drinfeld polynomials에 나타나는 roots를 제한해서 정의된다.

목적은 전체 category $\mathcal C$의 tensor product 문제를 더 작은 category 안에서 다루는 것이다. $\mathcal C_\ell$을 만들면 category-level tensor product 정보가 Grothendieck ring으로 내려가고, 이 ring을 cluster algebra와 비교할 수 있다.

특히 $\ell=1$에서는 distinguished simple objects와 cluster variables를 비교하는 그림이 나타난다. 이 경우 $\mathcal C_1$이 cluster algebra의 monoidal categorification이 된다는 conjectural picture가 핵심이다.

## 준비와 notation

$\mathfrak g$를 type $A_n$, $D_n$, $E_n$의 complex simple Lie algebra라고 하자. $I$는 Dynkin diagram의 vertex set이고, $U_q(\widehat{\mathfrak g})$는 대응하는 quantum affine algebra이다. 여기서 $q\in\mathbb C^\times$는 root of unity가 아니라고 둔다.

$\mathcal C$는 finite-dimensional type 1 $U_q(\widehat{\mathfrak g})$-modules의 category이다. 이 category는 abelian monoidal category이고, Hernandez-Leclerc categories는 이 $\mathcal C$ 안의 full subcategories로 정의된다.

$\mathcal C_\ell$의 Grothendieck ring은
$$
K_0(\mathcal C_\ell)
$$
로 쓴다. 아래에서는 같은 ring을 HL10의 notation에 맞춰 $R_\ell$로도 쓴다.

Simple object $S\in\mathcal C$는 Drinfeld polynomials
$$
\pi_S=(\pi_{i,S}(u))_{i\in I}
$$
로 parametrized된다. Fundamental module $V_{i,a}$는 $i\in I$, $a\in\mathbb C^\times$에 대해 Drinfeld polynomials
$$
\pi_{j,V_{i,a}}(u)=
\begin{cases}
1-au,& j=i,\\
1,& j\ne i
\end{cases}
$$
로 정의되는 simple object이다.

Dynkin diagram은 bipartite이므로
$$
I=I_0\sqcup I_1
$$
로 나누고,
$$
\xi_i=
\begin{cases}
0,& i\in I_0,\\
1,& i\in I_1
\end{cases}
$$
로 둔다.

## 정의

정의는 두 단계로 이루어진다. 먼저 spectral parameters가 integral lattice 위에 놓이는 full subcategory $\mathcal C_{\mathbb Z}$를 만든다. 그 다음 $\mathcal C_{\mathbb Z}$ 안에서 finite window를 골라 $\mathcal C_\ell$을 정의한다.

$\mathcal C_{\mathbb Z}$는 $\mathcal C$의 full subcategory로서, object $V$가 다음 조건을 만족할 때 그 안에 들어간다.

모든 composition factor $S$ of $V$와 모든 $i\in I$에 대해, Drinfeld polynomial $\pi_{i,S}(u)$의 roots가
$$
q^{2\mathbb Z+\xi_i}
$$
안에 놓인다.

$\ell\in\mathbb N$에 대해 Hernandez-Leclerc category $\mathcal C_\ell$은 $\mathcal C_{\mathbb Z}$의 full subcategory이다. Object $V\in\mathcal C_{\mathbb Z}$가 $\mathcal C_\ell$에 들어간다는 것은 다음 조건을 만족한다는 뜻이다.

모든 composition factor $S$ of $V$와 모든 $i\in I$에 대해, Drinfeld polynomial $\pi_{i,S}(u)$의 roots가 finite set
$$
\{q^{-2k-\xi_i}\mid 0\le k\le \ell\}
$$
안에 놓인다.

따라서 $\mathcal C_\ell$은 Drinfeld polynomial roots, 즉 spectral parameter data를 허용된 finite window 안에 두는 subcategory이다.

## 기본 예시

### 실제 예시: 가장 작은 window $\mathcal C_0$

$\ell=0$이면 허용되는 roots는 각 $i\in I$에 대해 하나의 값
$$
q^{-\xi_i}
$$
뿐이다. 이 경우 $\mathcal C_0$은 Hernandez-Leclerc categories 중 가장 단순한 첫 예시가 된다.

$\mathcal C_0$ 안에서는 fundamental modules의 tensor products가 simple이다. 또한 $\mathcal C_0$의 모든 simple object는 Drinfeld polynomials의 irreducible factors에 대응하는 fundamental modules의 tensor product와 isomorphic하다.

따라서 $\mathcal C_0$ 안의 simple objects끼리 tensor product를 해도 simple object가 된다. 이 점이 $\mathcal C_0$을 높은 $\ell$의 category와 구별하는 기본적인 단순성이다.

검증: 논문 예시

## 핵심 관점

Hernandez-Leclerc categories는 다음 세 층을 한 줄로 연결한다.

$$
\mathcal C_\ell
\quad\longrightarrow\quad
K_0(\mathcal C_\ell)
\quad\longleftrightarrow\quad
\text{cluster algebra}.
$$

Category-level에서는 $\mathcal C_\ell$의 simple objects와 tensor products를 본다. Grothendieck-ring-level에서는 object의 class $[S]$를 곱한다. Cluster-algebra-level에서는 cluster variables, frozen variables, cluster monomials가 나타난다.

핵심은 $\mathcal C_\ell$이 단순한 notation이 아니라, tensor product를 cluster algebra와 비교할 수 있게 만드는 category-level filter라는 점이다. Cluster algebra와의 비교는 $\ell=1$에서 가장 먼저 강하게 나타나며, 그 자세한 내용은 monoidal categorification language로 읽는다.

## 기본 성질

**Proposition.** $\mathcal C_\ell$은 abelian monoidal category이다. 또한 Grothendieck ring은 fundamental module classes로 생성되는 polynomial ring
$$
R_\ell
=
\mathbb Z\bigl[\, [V_{i,q^{2k+\xi_i}}]\mid i\in I,\ 0\le k\le \ell\,\bigr]
$$
이다.

**Example.** $\mathcal C_0$에서는 simple objects의 tensor product가 simple로 남는다. 이 때문에 $\mathcal C_0$의 tensor structure는 높은 $\ell$보다 훨씬 단순하다.

**Conjecture.** $\ell=1$에서는 cluster algebra $\mathcal A$와 Grothendieck ring $R_1$을 비교하는 map을 두고, $\mathcal C_1$이 $\mathcal A$의 monoidal categorification이 된다는 conjecture가 제시된다. 이 statement에서는 cluster variables와 frozen variables가 distinguished simple objects의 classes와 대응한다.

## 성질이 작동하는 방식

### 고급 예시: type $A_3$에서 $\mathcal C_1$

$\mathcal C_0$에서는 tensor product 구조가 단순하지만, $\mathcal C_1$에서는 cluster combinatorics가 실제로 보이기 시작한다. Type $A_3$에서 $I_0=\{1,3\}$, $I_1=\{2\}$로 잡으면 $\Phi_{\ge -1}$는 세 negative simple roots와 여섯 positive roots로 이루어진다.

$\mathcal C_1$의 cluster comparison에서는 이 almost positive roots에 대응하는 objects
$$
S(\beta)\qquad(\beta\in\Phi_{\ge -1})
$$
와 frozen objects $F_1,F_2,F_3$가 prime simple objects의 finite list를 이룬다.

이 예시의 핵심은 cluster 하나가 tensor product를 허용하는 prime simple objects의 compatible family를 지정한다는 점이다. 예를 들어 exchange relation
$$
x[-\alpha_2]x[\alpha_2]
=
f_2+x[-\alpha_1]x[-\alpha_3]
$$
은 Grothendieck ring에서 $S(-\alpha_2)\otimes S(\alpha_2)$의 composition factors가 $F_2$와 $S(-\alpha_1)\otimes S(-\alpha_3)$로 나타나는 현상을 보여 준다.

검증: 논문 예시

## 다른 topic들과의 관계

- [[topics/07-quantum-affine-algebras/quantum-affine-algebras|Quantum Affine Algebras]]: Hernandez-Leclerc categories는 finite-dimensional $U_q(\widehat{\mathfrak g})$-module category 안에서 정의되는 subcategories이다.
- [[topics/04-cluster-algebras/cluster-algebras|Cluster Algebras]]: $K_0(\mathcal C_\ell)$과 비교되는 target language가 cluster variables, frozen variables, cluster monomials를 가진 cluster algebra이다.
- [[topics/05-monoidal-categorification/monoidal-categorification|Monoidal Categorification]]: $\mathcal C_1$과 cluster algebra의 비교는 simple objects와 cluster monomials를 연결하는 monoidal categorification 관점으로 표현된다.
- [[topics/04-cluster-algebras/quantum-cluster-algebras|Quantum Cluster Algebras]]: 이후 quiver-Hecke/KLR 쪽 categorification에서는 quantum cluster algebra가 더 직접적인 target이 된다.
- [[topics/07-quantum-affine-algebras/quantum-affine-schur-weyl-duality|Quantum Affine Schur-Weyl Duality]]: Hernandez-Leclerc category 쪽 quantum affine category와 quiver-Hecke module category를 monoidal functor로 비교하는 다음 단계이다.
- [[topics/06-quiver-hecke-klr-algebras/quiver-hecke-module-categories|Quiver-Hecke Module Categories]]: Schur-Weyl functor의 source category가 되는 quiver-Hecke module category를 제공한다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/07-quantum-affine-algebras/quantum-affine-algebras|Quantum Affine Algebras]]에서 $U_q(\widehat{\mathfrak g})$, finite-dimensional module category, fundamental representations, spectral parameters를 먼저 읽는다. [[topics/04-cluster-algebras/cluster-algebras|Cluster Algebras]]에서는 cluster variables와 frozen variables의 기본 language를 읽는다.
- 상위 개념: [[topics/07-quantum-affine-algebras/quantum-affine-algebras|Quantum Affine Algebras]]가 ambient representation theory를 제공한다.
- 다음에 읽을 것: [[topics/07-quantum-affine-algebras/quantum-affine-schur-weyl-duality|Quantum Affine Schur-Weyl Duality]]에서 quantum affine category와 quiver-Hecke module category를 비교하는 functor를 읽는다. [[topics/05-monoidal-categorification/monoidal-categorification|Monoidal Categorification]]에서는 Grothendieck ring과 cluster algebra의 비교 방식을 읽는다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/hernandez-leclerc10-cluster-algebras-quantum-affine-algebras|Hernandez-Leclerc 2010]], Sections 3.1-3.8, especially Definition 3.1: ambient finite-dimensional $U_q(\widehat{\mathfrak g})$-module category, Drinfeld polynomials, $\mathcal C_{\mathbb Z}$, and $\mathcal C_\ell$.
- Hernandez-Leclerc 2010, Proposition 3.2: $\mathcal C_\ell$ is abelian monoidal and $R_\ell$ is a polynomial ring in fundamental-module classes.
- Hernandez-Leclerc 2010, Example 3.3: the $\mathcal C_0$ example used in `기본 예시`.
- Hernandez-Leclerc 2010, Conjecture 4.6: the $\ell=1$ monoidal-categorification statement used as a conjecture-level fact.
- Hernandez-Leclerc 2010, Example 4.8: the compact type $A_3$ advanced example in `성질이 작동하는 방식`; the full 14-cluster list and dimension list are intentionally not reproduced.
- [[sources/papers/kkop24-pbw-theory-quantum-affine-algebras|Kashiwara-Kim-Oh-Park 2024]], Section 2.5: later spectral-parameter-quiver formulation of the Hernandez-Leclerc category $\mathcal C_{\mathfrak g}^0$ and its role as a bridge to later quantum affine/quiver-Hecke material.

</details>
