---
id: shuffle-lemmas-for-quiver-hecke-modules
title: Shuffle Lemmas for Quiver-Hecke Modules
level: advanced
topic_kind: theorem
parent_topics:
  - quiver-hecke-module-categories
prerequisite_topics:
  - quiver-hecke-module-categories
  - normal-sequences
  - head-simplicity-of-convolutions
child_topics: []
related_topics:
  - determinantial-modules
  - quiver-hecke-subcategories
maturity: definition-ready
---

## 개요

Shuffle lemmas for quiver-Hecke modules는 divided restriction functors
$$
E_i^{(n)},\qquad E_i^{*(n)}
$$
가 convolution product
$$
M\circ N
$$
에 작용할 때 어떤 filtration으로 분해되는지를 말하는 theorem-level topic이다. 핵심은 $n$개의 $\alpha_i$-restriction을 product 전체에서 한 번에 떼어 내면, 그 결과가 $M$에서 $n-k$개를 떼고 $N$에서 $k$개를 떼는 모든 경우를 filtration quotient로 갖는다는 점이다.

이 lemma들은 [[topics/06-quiver-hecke-klr-algebras/quiver-hecke-module-categories|Quiver-Hecke Module Categories]]에서 배운 convolution product와 restriction functor를 동시에 사용한다. [[topics/06-quiver-hecke-klr-algebras/head-simplicity-of-convolutions|Head Simplicity of Convolutions]] 이후에는 head convolution과 restriction functor가 한 식 안에 함께 나타난다. Shuffle lemmas는 이 둘 사이에서 restriction이 어느 factor로 이동했는지를 추적하는 도구이다.

## 준비와 notation

$M\in R(\beta)\text{-gmod}$, $N\in R(\gamma)\text{-gmod}$라고 하자. Convolution product는
$$
M\circ N
$$
으로 쓴다.

$i\in I$와 $n\ge 0$에 대해 $E_i^{(n)}$는 divided restriction functor이다. 이 functor는
$$
E_i^{(n)}M
=
\operatorname{HOM}_{R(n\alpha_i)}
\bigl(P(i^n), e(n\alpha_i,\beta-n\alpha_i)M\bigr)
$$
로 정의된다. 여기서 $M$은 $R(\beta)$-module이고, $P(i^n)$은 head가 $L(i^n)$인 indecomposable projective $R(n\alpha_i)$-module이다.

Starred version $E_i^{*(n)}$는 오른쪽 끝에서 $\alpha_i$-part를 떼는 대응 functor이다. 즉 $E_i^{(n)}$이 idempotent $e(n\alpha_i,\beta-n\alpha_i)$를 사용한다면, $E_i^{*(n)}$는 오른쪽 idempotent $e(\beta-n\alpha_i,n\alpha_i)$를 사용한다.

Grading shift는 $q$로 쓴다. 이 글에서는
$$
\mathsf d_i=\frac{(\alpha_i,\alpha_i)}2
$$
라고 둔다. 또한 $M\in R(\beta)\text{-gmod}$이면
$$
\operatorname{wt}(M)=-\beta
$$
이다.

## 정리의 진술

### $E_i^{(n)}$ shuffle filtration

$M\in R(\beta)\text{-mod}$, $N\in R(\gamma)\text{-mod}$, $i\in I$, $n\ge 0$라고 하자. 그러면 $E_i^{(n)}(M\circ N)$에는 증가 filtration
$$
0=F_{-1}\subset F_0\subset\cdots\subset F_n=E_i^{(n)}(M\circ N)
$$
이 있고, 각 quotient는
$$
F_k/F_{k-1}
\simeq
q^{\,k(n-k)\mathsf d_i-k(\alpha_i,\beta)}
E_i^{(n-k)}(M)\circ E_i^{(k)}(N)
$$
이다.

따라서 $E_i^{(n)}$을 product 전체에 적용한 object는, $n$개의 restriction을 두 factor에 나누어 적용한 pieces를 quotient로 갖는다. Index $k$는 오른쪽 factor $N$에서 몇 개의 $\alpha_i$-restriction을 떼었는지를 나타낸다.

### $E_i^{*(n)}$ shuffle filtration

같은 조건에서 $E_i^{*(n)}(M\circ N)$에도 증가 filtration
$$
0=F_{-1}\subset F_0\subset\cdots\subset F_n=E_i^{*(n)}(M\circ N)
$$
이 있고, 각 quotient는
$$
F_k/F_{k-1}
\simeq
q^{\,k(n-k)\mathsf d_i-k(\alpha_i,\gamma)}
E_i^{*(k)}(M)\circ E_i^{*(n-k)}(N)
$$
이다.

여기서는 starred restriction이 오른쪽 끝을 기준으로 작동한다. 그래서 quotient에서 $M$과 $N$에 붙는 indices의 순서가 $E_i^{(n)}$ case와 mirror form으로 나타난다.

## 핵심 관점

Shuffle lemma는 restriction functor가 convolution product와 단순히 commute한다고 말하지 않는다. Product 전체에 적용한 restriction을 여러 quotient로 나누고, 각 quotient가 두 factor에 restriction을 분배한 형태임을 말한다.

$$
E_i^{(n)}(M\circ N)
\quad\leadsto\quad
\bigl\{
E_i^{(n-k)}(M)\circ E_i^{(k)}(N)
\bigr\}_{0\le k\le n}
$$

이 그림은 Grothendieck group에서 coproduct formula처럼 보인다. 하지만 category-level에서는 equality가 아니라 filtration statement이다. 이 차이가 중요하다. 이후 head, socle, R-matrix degree를 다룰 때는 Grothendieck-ring-level identity만으로는 부족하고, 실제 subquotients와 morphisms가 필요하기 때문이다.

## 기본 성질

### Coproduct formula의 categorification

$E_i^{(n)}$ shuffle filtration은 quantum group 쪽 divided generator의 coproduct formula
$$
\Delta(e_i^{(n)})
=
\sum_{k=0}^n q^{k(n-k)\mathsf d_i}e_i^{(n-k)}t_i^k\otimes e_i^{(k)}
$$
를 category-level에서 반영한다. Grothendieck group으로 내려가면 filtration quotients가 이 합의 terms처럼 보인다.

### Extremal vanishing이 주는 morphisms

$Y,Z\in R\text{-gmod}$와 $y,z\ge 0$를 둔다. $E_i^{y+1}Y\simeq0$이면
$$
E_i^{(y)}Y\circ E_i^{(z)}Z
\longrightarrow
E_i^{(y+z)}(Y\circ Z)
$$
꼴의 monomorphism을 준다. 반대로 $E_i^{z+1}Z\simeq0$이면
$$
E_i^{(y+z)}(Y\circ Z)
\longrightarrow
E_i^{(y)}Y\circ E_i^{(z)}Z
$$
꼴의 epimorphism을 준다.

두 vanishing condition이 모두 성립하면, 이 두 morphism은 서로 inverse인 isomorphisms가 된다. 같은 lemma는 adjacent terms를 연결하는 short exact sequence도 제공한다. 이 exact sequence는 $E_i^{(y+z-1)}(Y\circ Z)$를 restriction 분배가 하나씩 다른 두 term과 비교하는 데 쓰인다.

### Starred version

$E_i^{*(n)}$에 대해서도 같은 형태의 monomorphism, epimorphism, isomorphism, short exact sequence가 있다. 차이는 starred restriction이 오른쪽 끝을 기준으로 하므로, $Y$와 $Z$에 붙는 exponents와 grading shifts가 $E_i^{(n)}$ case와 mirror form으로 바뀐다는 점이다.

### Head convolution과의 연결

이 filtration machinery는 head convolution
$$
L\nabla M=\operatorname{hd}(L\circ M)
$$
와 starred restriction 사이의 관계를 제어한다. Simple modules $L,M$ 중 하나가 affreal인 경우에는 $\varepsilon_i^*$의 subadditivity, R-matrix degree inequality, 그리고 특정 equality 조건 아래에서
$$
\widetilde E_i^*(L\nabla M)
$$
가 $L$과 $M$에 각각 starred restriction을 적용한 뒤의 head convolution과 일치하는 상황을 얻는다.

이 때문에 shuffle lemmas는 단순한 filtration result에 머물지 않는다. Localized crystal construction에서 restriction functor와 head convolution을 함께 움직일 때 필요한 계산 도구가 된다.

## 다른 topic들과의 관계

[[topics/06-quiver-hecke-klr-algebras/quiver-hecke-module-categories|Quiver-Hecke Module Categories]]는 $R(\beta)\text{-gmod}$, convolution product $\circ$, restriction functor의 ambient category를 제공한다. 여기의 notation은 그 category-level setup 위에서 읽어야 한다.

[[topics/06-quiver-hecke-klr-algebras/head-simplicity-of-convolutions|Head Simplicity of Convolutions]]는 $M\nabla N=\operatorname{hd}(M\circ N)$ notation과 simple head/socle behavior를 제공한다. Shuffle lemmas는 이 head convolution에 restriction functor를 적용할 때 필요한 intermediate filtration을 제공한다.

[[topics/06-quiver-hecke-klr-algebras/normal-sequences|Normal Sequences]]는 ordered convolution product의 head를 안정적으로 다루는 R-matrix condition을 제공한다. Shuffle lemmas는 ordered convolution 안에서 restriction이 어느 factor로 분배되는지 추적하는 쪽에 가깝다.

[[topics/08-localization-of-categories/localized-root-operators|Localized Root Operators]]에서는 localized category 안에서 root operators를 정의할 때 head convolution과 restriction behavior가 함께 쓰인다. Shuffle lemmas의 역할은 그 계산으로 넘어가기 전의 theorem machinery를 분리해 두는 것이다.

[[topics/06-quiver-hecke-klr-algebras/determinantial-modules|Determinantial Modules]]와 [[topics/06-quiver-hecke-klr-algebras/quiver-hecke-subcategories|Quiver-Hecke Subcategories]]는 restriction/convolution machinery가 실제 category families 안에서 사용되는 방향을 보여 준다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/06-quiver-hecke-klr-algebras/quiver-hecke-module-categories|Quiver-Hecke Module Categories]]에서 convolution product와 restriction functor를 읽고, [[topics/06-quiver-hecke-klr-algebras/head-simplicity-of-convolutions|Head Simplicity of Convolutions]]에서 head convolution notation을 읽는다.
- 상위 개념: [[topics/06-quiver-hecke-klr-algebras/quiver-hecke-module-categories|Quiver-Hecke Module Categories]]가 이 lemma들이 사는 category-level setting이다.
- 다음에 읽을 것: [[topics/08-localization-of-categories/localized-root-operators|Localized Root Operators]]에서 restriction behavior가 localized crystal operator formulas에 들어가는 방식을 읽는다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/kashiwara-nakashima25-crystal-structure-localized-quantum-unipotent-coordinate-category|Kashiwara-Nakashima 2025]], Section 4.7, lines 2645-2667: shuffle filtration for $E_i^{(n)}(M\circ N)$ and its coproduct interpretation.
- Kashiwara-Nakashima 2025, Section 4.7, lines 2668-2677: starred shuffle filtration for $E_i^{*(n)}(M\circ N)$.
- Kashiwara-Nakashima 2025, Section 4.7, lines 2680-2742: monomorphism, epimorphism, isomorphism, and short exact sequence consequences for $E_i$ and $E_i^*$.
- Kashiwara-Nakashima 2025, Section 4.7, lines 2746-2793: use of the starred shuffle lemma to control $\varepsilon_i^*$, R-matrix degree, and $\widetilde E_i^*$ applied to a head convolution.
- Kashiwara-Nakashima 2025, Lemma 4.24, lines 2797-2802: simple head and socle of $E_i^{(n)}(M)$.

</details>
