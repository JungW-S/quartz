---
id: quantum-cluster-algebras
title: Quantum Cluster Algebras
level: advanced
topic_kind: algebra
parent_topics:
  - cluster-algebras
prerequisite_topics:
  - cluster-algebras
  - quantum-groups
child_topics: []
related_topics:
  - monoidal-categorification
  - quantum-coordinate-rings
  - left-and-right-g-vectors
maturity: example-ready
---

## 개요

Quantum cluster algebra는 cluster algebra의 $q$-analogue이다. Classical cluster algebra에서는 cluster variables가 commutative variables로 움직이지만, quantum cluster algebra에서는 variables가 skew-symmetric matrix $L$이 정하는 규칙에 따라 $q$-commute한다.

핵심은 seed에 두 종류의 matrix data가 들어간다는 점이다. Exchange matrix $\widetilde B$는 mutation 방향과 exchange relation을 조절하고, skew-symmetric matrix $L$은 variables 사이의 $q$-commutation을 조절한다.

이 구조는 quantum coordinate ring과 monoidal categorification을 연결할 때 쓰인다. 특히 quiver-Hecke category에서 얻은 Grothendieck ring을 quantum cluster algebra와 비교하고, 그 quantum cluster algebra를 다시 $A_q(\mathfrak n(w))$ 같은 quantum coordinate ring과 비교한다.

## 준비와 notation

먼저 [[topics/04-cluster-algebras/cluster-algebras|Cluster Algebras]]에서 seed, mutation, cluster variables, cluster monomials를 읽는다. Quantum version에서는 여기에 $q$-parameter와 commutation matrix가 추가된다.

$J$를 finite index set이라고 하고
$$
J=J_{\mathrm{ex}}\sqcup J_{\mathrm{fr}}
$$
로 쓴다. $J_{\mathrm{ex}}$는 mutation 방향이고, $J_{\mathrm{fr}}$는 frozen variables의 index set이다.

$L=(\lambda_{ij})_{i,j\in J}$는 skew-symmetric integer matrix이다. 이 matrix는 generators $X_i$ 사이의 relation
$$
X_iX_j=q^{\lambda_{ij}}X_jX_i
$$
를 정한다. 이 relation으로 생성되는 $\mathbb Z[q^{\pm1/2}]$-algebra를 $P(L)$라고 쓰고, 그 skew field of fractions를 $F(L)$라고 쓴다.

Vector $a=(a_i)_{i\in J}\in\mathbb Z^J$에 대해 quantum torus monomial은
$$
X^a
=
q^{\frac12\sum_{i>j}a_i a_j\lambda_{ij}}
\prod_{i\in J}^{\rightarrow} X_i^{a_i}
$$
로 normalized된다. 여기서 ordered product는 $J$의 total order를 하나 고른 뒤 그 순서대로 곱한다. KKKO14의 정의에서는 이 $X^a$가 total order의 선택에 의존하지 않는다.

Exchange matrix는
$$
\widetilde B=(b_{ij})_{i\in J,\ j\in J_{\mathrm{ex}}}
$$
이다. Principal part는 $J_{\mathrm{ex}}\times J_{\mathrm{ex}}$ 부분행렬이며, 여기서는 skew-symmetric인 경우를 기본으로 둔다.

## 정의

### Compatible pair

$(L,\widetilde B)$가 compatible pair라는 것은 어떤 positive integer $d$가 존재해서
$$
\sum_{k\in J}\lambda_{ik}b_{kj}=\delta_{ij}d
\qquad
(i\in J,\ j\in J_{\mathrm{ex}})
$$
를 만족한다는 뜻이다. 이 compatibility는 mutation 뒤에도 quantum commutation data와 exchange matrix가 함께 움직일 수 있게 해 주는 조건이다.

Direction $k\in J_{\mathrm{ex}}$에서 matrix part를 mutate하려면 $J\times J$ matrix $E=(e_{ij})$와 $J_{\mathrm{ex}}\times J_{\mathrm{ex}}$ matrix $F=(f_{ij})$를 다음처럼 둔다.
$$
e_{ij}=
\begin{cases}
\delta_{ij},& j\ne k,\\
-1,& i=j=k,\\
\max(0,-b_{ik}),& i\ne j=k,
\end{cases}
\qquad
f_{ij}=
\begin{cases}
\delta_{ij},& i\ne k,\\
-1,& i=j=k,\\
\max(0,b_{kj}),& i=k\ne j.
\end{cases}
$$
그 다음
$$
\mu_k(L)=E^TLE,
\qquad
\mu_k(\widetilde B)=E\widetilde B F
$$
로 둔다. 이 pair가 mutated compatible pair이다.

### Quantum seed

$A$를 $\mathbb Z[q^{\pm1/2}]$-algebra라고 하자. Quantum seed는 triple
$$
S=(\{x_i\}_{i\in J},L,\widetilde B)
$$
이다. 여기서 $\{x_i\}_{i\in J}$는 $A$ 안의 algebraically independent $L$-commuting family이다. 즉
$$
x_ix_j=q^{\lambda_{ij}}x_jx_i
$$
를 만족하고, $P(L)\to A$, $X_i\mapsto x_i$가 injective이다.

Quantum seed 안의 set $\{x_i\}_{i\in J}$를 cluster라고 하고, 그 원소를 cluster variables라고 부른다. $i\in J_{\mathrm{fr}}$에 해당하는 $x_i$는 frozen variables이다. $a=(a_i)_{i\in J}\in\mathbb Z_{\ge0}^{J}$에 대해 $X_i$를 $x_i$로 바꾼 normalized monomial $x^a$를 만들 수 있고, 이런 $x^a$들을 quantum cluster monomials라고 부른다.

### Quantum seed mutation

Mutation in direction $k\in J_{\mathrm{ex}}$은 compatible pair $(L,\widetilde B)$를 $\mu_k(L,\widetilde B)$로 바꾸고, cluster variable $x_k$를
$$
\mu_k(x)_k=x^{a'}+x^{a''}
$$
로 바꾼다. 여기서
$$
a_i'=
\begin{cases}
-1,& i=k,\\
\max(0,b_{ik}),& i\ne k,
\end{cases}
\qquad
a_i''=
\begin{cases}
-1,& i=k,\\
\max(0,-b_{ik}),& i\ne k.
\end{cases}
$$
다른 $i\ne k$에 대해서는 $\mu_k(x)_i=x_i$이다. 이 mutation은 새 quantum seed를 만든다.

### Quantum cluster algebra

Quantum cluster algebra $A_{q^{1/2}}(S)$는 initial quantum seed $S$에서 mutation을 임의로 반복해서 얻는 모든 quantum cluster variables가 생성하는 $\mathbb Z[q^{\pm1/2}]$-subalgebra이다.

### Extended g-vectors and pointed elements

Initial seed $t_0$를 고정하고 $q^{1/2}\mapsto 1$로 specialize하자. Cluster variable $X_i(t)$의 extended $g$-vector는
$$
\widetilde g_i(t)\in \mathbb Z^J
$$
중에서 commutative specialization이
$$
X_i(t)\big|_{q^{1/2}\mapsto 1}
=
X^{\widetilde g_i(t)}F(Y_1,\ldots,Y_n)
$$
꼴로 쓰이게 하는 vector이다. 여기서 $n=|J_{\mathrm{ex}}|$이고, $F(Y_1,\ldots,Y_n)$는 $F$-polynomial이다. $\widetilde g_i(t)$의 exchangeable components를 $g$-vector라고 부른다. Principal coefficients case에서는 이 $g$-vector가 cluster variable의 grading으로 읽힌다.

Seed $t$마다 degree lattice
$$
D(t)\simeq \mathbb Z^J
$$
가 붙는다. $\eta',\eta\in D(t)$에 대해 dominance order는
$$
\eta'\prec_t\eta
\quad\Longleftrightarrow\quad
\eta'=\eta+\widetilde B(t)v
\ \text{for some }0\ne v\in\mathbb N^{J_{\mathrm{ex}}}
$$
로 정의된다. 여기서 $\widetilde B(t)$는 exchange directions에서 $D(t)$로 가는 integer matrix로 읽는다.

Quantum torus $\mathcal T(t)$ 안의 Laurent polynomial $Z$를 보자. $Z$의 Laurent monomials 중 dominance order에 대해 maximal degree를 갖는 항들을 leading terms라고 한다. Leading term이 하나뿐이고 그 degree가 $\eta$이면 $\deg^t Z=\eta$라고 쓴다. 또한 그 유일한 leading term의 coefficient가 $1$이면 $Z$는 $\eta$-pointed라고 한다.

Subset $\mathcal S\subset \mathcal T(t)$가 $W\subset D(t)$에 대해 $W$-pointed라는 것은 degree map
$$
\deg^t:\mathcal S\to W
$$
가 bijection이라는 뜻이다. 이 language는 triangular bases와 localized-crystal coordinate language에서 basis elements를 seed-dependent degrees로 label할 때 쓰인다.

## 기본 예시

Rank-two quantum seed를 보자. 모든 index가 exchangeable이라고 두고
$$
J=J_{\mathrm{ex}}=\{1,2\}
$$
로 둔다. Exchange matrix와 commutation matrix를
$$
B=
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix},
\qquad
L=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}
$$
로 잡으면
$$
LB=I
$$
이므로 compatible pair이다. 이때 quantum torus generators는
$$
X_1X_2=q^{-1}X_2X_1
$$
을 만족한다.

Direction $1$에서 mutate하면 matrix part는
$$
L'=
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix},
\qquad
B'=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}
$$
로 바뀐다. Mutation exponents는
$$
a'=(-1,0),
\qquad
a''=(-1,1)
$$
이므로 새 variable은
$$
X_1'=X^{(-1,0)}+X^{(-1,1)}
$$
이다. Ordered product notation으로 쓰면
$$
X^{(-1,1)}=q^{-1/2}X_1^{-1}X_2
$$
이므로
$$
X_1'=X_1^{-1}+q^{-1/2}X_1^{-1}X_2
$$
이다.

새 cluster variable $X_1'$과 기존 variable $X_2$는 mutated matrix $L'$에 맞게
$$
X_1'X_2=qX_2X_1'
$$
를 만족한다. 이 한 줄이 quantum seed mutation에서 확인해야 할 핵심이다. 변수만 바뀌는 것이 아니라, 바뀐 variables가 새 commutation matrix와 함께 움직인다.

검증: Sage 계산 `sage scripts/examples/cluster-algebras/quantum_rank2_one_mutation.sage`

## 핵심 관점

Classical seed에서는 exchange matrix가 mutation을 조절한다. Quantum seed에서는 여기에 $L$이 추가되어 variables 사이의 noncommutative multiplication을 조절한다.

$$
\text{quantum seed}
=
\left(
\text{cluster variables},
\text{q-commutation matrix }L,
\text{exchange matrix }\widetilde B
\right).
$$

따라서 quantum mutation은 두 조건을 동시에 보존해야 한다. 새 variables는 새 matrix $\mu_k(L)$에 대해 $q$-commute해야 하고, exchange matrix도 $\mu_k(\widetilde B)$로 바뀌어야 한다.

## 기본 성질

**정의에서 바로 나오는 조건.** Quantum cluster monomial은 하나의 quantum cluster 안에서 만든 normalized monomial $x^a$이다. Classical case처럼 같은 cluster 안에서 만든 monomial이라는 조건이 중요하다.

**정리 수준의 성질.** Quantum Laurent phenomenon에 의해 quantum cluster variables는 mutation으로 얻은 다른 quantum seed의 quantum cluster variables에 대한 quantum Laurent expression 안에 놓인다.

**Categorification 관점.** Quantum monoidal categorification에서는 quantum cluster monomials가 real simple objects의 classes로 나타난다. 이때 $q^{1/2}$의 power는 grading shift와 연결된다.

**Coordinate-ring 연결.** GLS11의 quantum coordinate ring path에서는 $\mathcal C_w$에 붙은 quantum cluster algebra가 $A_q(\mathfrak n(w))$와 isomorphic하게 나타난다.

**Pointed basis 관점.** Triangular-basis language에서는 basis element가 seed $t$에 대해 pointed Laurent polynomial로 나타나고, 그 leading degree가 degree lattice $D(t)$의 point를 준다. 이 관점은 뒤의 topic들에서 $g$-vector coordinate를 basis-element label로 읽는 데 쓰인다.

## 다른 topic들과의 관계

**Cluster Algebras.** [[topics/04-cluster-algebras/cluster-algebras|Cluster Algebras]]는 quantum version에서 바뀌지 않는 seed와 mutation의 기본 틀을 제공한다. Seed와 mutation을 먼저 이해해야 $L$-commutation과 quantum monomial normalization을 읽을 수 있다.

**Monoidal Categorification.** [[topics/05-monoidal-categorification/monoidal-categorification|Monoidal Categorification]]은 quantum cluster variables와 quantum cluster monomials를 category의 object classes로 해석한다.

**Quantum Coordinate Rings.** [[topics/01-quantum-groups/quantum-coordinate-rings|Quantum Coordinate Rings]]는 $A_q(\mathfrak n(w))$ 같은 coordinate-ring-level target을 제공한다.

**Quiver-Hecke Module Categories.** [[topics/06-quiver-hecke-klr-algebras/quiver-hecke-module-categories|Quiver-Hecke Module Categories]]는 quantum monoidal categorification에서 object-level data가 사는 category를 제공한다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/04-cluster-algebras/cluster-algebras|Cluster Algebras]]에서 classical seed와 mutation을 읽고, [[topics/01-quantum-groups/quantum-groups|Quantum Groups]]에서 $q$-deformation language를 읽는다.
- 상위 개념: [[topics/04-cluster-algebras/cluster-algebras|Cluster Algebras]]가 broader classical framework를 제공한다.
- 다음에 읽을 것: [[topics/05-monoidal-categorification/monoidal-categorification|Monoidal Categorification]]에서 quantum cluster monomials가 real simple objects로 나타나는 방식을 읽고, [[topics/01-quantum-groups/quantum-coordinate-rings|Quantum Coordinate Rings]]에서 $A_q(\mathfrak n(w))$와의 comparison을 읽는다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/kkko14-monoidal-categorification-cluster-algebras|KKKO14]], Section 4.1, pp.27-28: quantum torus $P(L)$, $L$-commuting families, compatible pairs, quantum seeds, cluster variables, frozen variables, and quantum cluster monomials.
- KKKO14, Section 4.2 and Definition 4.2, pp.28-29: mutation of compatible pairs, mutation of quantum seeds, and the definition of $A_{q^{1/2}}(S)$.
- Sage verification script `scripts/examples/cluster-algebras/quantum_rank2_one_mutation.sage`: verifies the displayed rank-two compatible pair, mutation exponents, mutated matrices, and relation $X_1'X_2=qX_2X_1'$.
- KKKO14, Introduction, pp.1-2: quantum cluster algebra as a $q$-analogue and the quantum Laurent phenomenon reference.
- KKKO14, Definition 5.8, p.34: quantum monoidal categorification and the interpretation of quantum cluster monomials as real simple object classes up to powers of $q^{1/2}$.
- [[sources/papers/gls11-cluster-structures-quantum-coordinate-rings|GLS11]], Theorem 12.3, pp.43-44: quantum cluster algebra attached to $\mathcal C_w$ is isomorphic to $A_q(\mathfrak n(w))$.
- [[sources/papers/qin17-triangular-bases-quantum-cluster-algebras|Qin17]], Section 2.1, pp.9-10 and Definitions 3.1.1, 3.1.4, 3.1.5, pp.13-15: extended \(g\)-vectors, \(g\)-vectors, dominance order, pointed elements, and pointed sets.

</details>
