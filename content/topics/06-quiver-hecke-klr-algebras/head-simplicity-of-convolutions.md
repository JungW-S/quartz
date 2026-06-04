---
id: head-simplicity-of-convolutions
title: Head Simplicity of Convolutions
level: advanced
topic_kind: theorem
parent_topics:
  - quiver-hecke-module-categories
  - normal-sequences
prerequisite_topics:
  - normal-sequences
  - r-matrix-renormalization
child_topics: []
related_topics:
  - localized-root-operators
  - root-objects-in-localized-categories
maturity: example-ready
---

## 개요

Head simplicity of convolutions는 quiver-Hecke module category에서 convolution product
$$
M\circ N
$$
의 head와 socle이 언제 simple object가 되는지를 판정하는 theorem-level topic이다. 핵심 상황은 한쪽 factor가 real simple이고 다른 factor가 simple일 때이다. 이때 renormalized R-matrix의 image는 임의의 subquotient가 아니라, 한 방향 convolution의 head와 반대 방향 convolution의 socle을 동시에 식별한다.

이 정리는 [[topics/06-quiver-hecke-klr-algebras/normal-sequences|Normal Sequences]] 뒤에 자연스럽게 나온다. Normal sequence는 여러 simple objects의 ordered convolution을 다루고, head simplicity theorem은 그런 ordered product에서 simple head가 왜 안정적으로 추적되는지를 설명한다.

Localized crystal construction에서는 head convolution notation
$$
M\nabla N:=\operatorname{hd}(M\circ N)
$$
이 반복해서 등장한다. Head simplicity theorem은 $\nabla$가 단순히 quotient를 하나 고르는 기호가 아니라, R-matrix image로 식별되는 simple object를 가리킨다는 배경을 제공한다.

## 준비와 notation

$R(\beta)$를 quiver-Hecke algebra라고 하자. $M\in R(\beta)\text{-mod}$, $N\in R(\gamma)\text{-mod}$일 때 convolution product를
$$
M\circ N
$$
으로 쓴다.

$M\circ N$의 head와 socle은 각각
$$
\operatorname{hd}(M\circ N),
\qquad
\operatorname{soc}(M\circ N)
$$
이다. Head convolution은
$$
M\nabla N:=\operatorname{hd}(M\circ N)
$$
으로 쓴다.

두 modules 사이의 renormalized R-matrix를
$$
r_{M,N}:M\circ N\to N\circ M
$$
로 쓴다. 이 notation의 construction과 degree는 [[topics/06-quiver-hecke-klr-algebras/r-matrix-renormalization|R-Matrix Renormalization]]에서 먼저 읽는다.

Simple module $M$이 real simple이라는 것은 $M\circ M$이 simple이라는 뜻이다. KKKO15 Theorem 3.2는 원래 가정을
$$
r_{M,M}\in \mathbf k\,\operatorname{id}_{M\circ M}
$$
꼴로 둔다. Symmetric quiver-Hecke algebra setting에서는 이 조건이 $M$의 real simplicity와 동치이므로, 아래에서는 이 가정을 real simple condition으로 읽을 수 있다.

KN25 Section 4.5에서는 simple root module $L(i)$와 simple module $M$ 사이의 head convolution을 다룬다. 여기서 $i\in I$이고, $\varepsilon_i(M)$, $\varepsilon_i^*(M)$는 quiver-Hecke crystal notation이며,
$$
d_i(M)=\varepsilon_i(M)+\varepsilon_i^*(M)+\langle h_i,\operatorname{wt}(M)\rangle
$$
로 둔다.

## 정리의 진술

KKKO15 Theorem 3.2의 quiver-Hecke version은 다음과 같다.

$\beta,\gamma\in Q_+$, $M\in R(\beta)\text{-mod}$, $N\in R(\gamma)\text{-mod}$라고 하자. 다음을 가정한다.

- $R(\beta)$는 symmetric이고 $r_{M,M}\in \mathbf k\,\operatorname{id}_{M\circ M}$이다.
- $M$은 zero module이 아니다.
- $N$은 simple $R(\gamma)$-module이다.

그러면 $M\circ N$은 simple socle과 simple head를 가진다. 같은 방식으로 $N\circ M$도 simple socle과 simple head를 가진다.

더 정확히,
$$
\operatorname{Im}(r_{N,M})
$$
은 $M\circ N$의 socle이고, 동시에 $N\circ M$의 head이다. 또한
$$
\operatorname{Im}(r_{M,N})
$$
은 $N\circ M$의 socle이고, 동시에 $M\circ N$의 head이다.

이 정리의 결론에는 $M$이 simple module이라는 사실도 포함된다.

## 기본 예시

### 구조 예시: $L(i)$와 $d_i(M)=0$

simple root module $L(i)$와 simple module $M$을 둔다. $d_i(M)=0$이면, grading shift를 제외하고
$$
L(i)\nabla M\simeq L(i)\circ M\simeq M\circ L(i)\simeq M\nabla L(i)
$$
이다.

이 예시는 head convolution $L(i)\nabla M$이 항상 convolution product를 더 작게 줄이는 연산은 아님을 보여준다. $d_i(M)=0$인 경우에는 head를 취해도 전체 convolution product와 같은 simple object가 남는다.

검증: 논문 예시

## 핵심 관점

핵심 그림은 두 방향 R-matrix의 image가 서로 다른 convolution product의 head와 socle을 교차해서 잡는다는 것이다.

$$
N\circ M
\xrightarrow{\;r_{N,M}\;}
M\circ N
$$

이 morphism의 image를 source 쪽에서 보면 $N\circ M$의 head이고, target 쪽에서 보면 $M\circ N$의 socle이다.

반대로
$$
M\circ N
\xrightarrow{\;r_{M,N}\;}
N\circ M
$$
의 image는 source $M\circ N$의 head이고, target $N\circ M$의 socle이다.

따라서 head simplicity theorem은 category-level statement이다. Grothendieck ring에서는 product $[M][N]$의 distinguished simple constituent를 추적하는 것처럼 보일 수 있지만, 실제 내용은 convolution product 안의 morphism image가 head와 socle을 동시에 식별한다는 것이다.

## 기본 성질

### Real simple 조건의 판정

Symmetric quiver-Hecke algebra $R(\beta)$에서 nonzero $M\in R(\beta)\text{-mod}$에 대해 다음 조건들은 동치이다.

- $M$은 real simple module이다.
- $r_{M,M}\in \mathbf k\,\operatorname{id}_{M\circ M}$이다.
- $\operatorname{End}_{R(2\beta)}(M\circ M)\simeq \mathbf k\,\operatorname{id}_{M\circ M}$이다.

따라서 Theorem 3.2의 R-matrix scalar condition은 symmetric case에서 real simple condition으로 읽을 수 있다.

### Powers of a real simple module

$M$이 real simple이면 모든 $n\ge 1$에 대해
$$
M^{\circ n}=M\circ\cdots\circ M
$$
은 simple module이다. 이 성질은 real simple object가 convolution product 안에서 안정적인 building block으로 쓰일 수 있음을 말한다.

### Simple root module과 head convolution

KN25 Section 4.5에서는 $L(i)$와 simple module $M$의 head convolution을 $d_i(M)$으로 제어한다.

$d_i(M)=0$이면, grading shift를 무시하고
$$
L(i)\nabla M\simeq L(i)\circ M\simeq M\circ L(i)\simeq M\nabla L(i)
$$
이다. 즉 이 경우에는 head convolution이 전체 convolution product와 일치한다.

$d_i(M)>0$이면 $L(i)$를 곱한 뒤 head convolution을 취하는 과정이 $d_i$를 하나 줄인다.
$$
d_i(L(i)\nabla M)=d_i(M\nabla L(i))=d_i(M)-1.
$$
Powers $L(i^n)$에 대해서도 같은 현상이 반복되어
$$
d_i(L(i^n)\nabla M)=d_i(M\nabla L(i^n))=\max(d_i(M)-n,0)
$$
이 된다.

### Divided restriction functor의 head와 socle

KN25 Lemma 4.24는 simple module $M$과 $0\le n\le\varepsilon_i(M)$에 대해 divided functor $E_i^{(n)}(M)$이 simple socle과 simple head를 가진다고 말한다. 둘 다 grading shift를 제외하면 $\widetilde E_i^nM$과 isomorphic이다.

이 결과는 head simplicity가 convolution product에서만 쓰이는 것이 아니라, crystal operator와 연결되는 restriction-type construction에서도 같은 방향으로 나타남을 보여 준다.

## 다른 topic들과의 관계

- [[topics/06-quiver-hecke-klr-algebras/quiver-hecke-module-categories|Quiver-Hecke Module Categories]]는 $R(\beta)\text{-mod}$, convolution product $\circ$, simple modules의 ambient category를 제공한다.
- [[topics/06-quiver-hecke-klr-algebras/r-matrix-renormalization|R-Matrix Renormalization]]은 $r_{M,N}$와 R-matrix degree를 설명한다.
- [[topics/06-quiver-hecke-klr-algebras/normal-sequences|Normal Sequences]]는 head/socle theorem을 여러 factors의 ordered product로 확장해서 쓰는 조건이다.
- [[topics/08-localization-of-categories/localized-root-operators|Localized Root Operators]]는 $\nabla$를 사용해 localized category의 crystal operators를 정의한다.
- [[topics/08-localization-of-categories/root-objects-in-localized-categories|Root Objects in Localized Categories]]는 localized root operator의 input object가 갖추어야 할 R-matrix degree 조건을 다룬다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/06-quiver-hecke-klr-algebras/quiver-hecke-module-categories|Quiver-Hecke Module Categories]]에서 convolution product를 읽고, [[topics/06-quiver-hecke-klr-algebras/r-matrix-renormalization|R-Matrix Renormalization]]에서 renormalized R-matrix를 읽는다.
- 상위 개념: [[topics/06-quiver-hecke-klr-algebras/normal-sequences|Normal Sequences]]는 이 theorem을 ordered convolution product로 확장해서 쓰는 주변 개념이다.
- 다음에 읽을 것: [[topics/08-localization-of-categories/localized-root-operators|Localized Root Operators]]에서 $M\nabla N$ notation이 crystal operator formulas에 들어가는 방식을 읽고, [[topics/06-quiver-hecke-klr-algebras/shuffle-lemmas-for-quiver-hecke-modules|Shuffle Lemmas for Quiver-Hecke Modules]]에서 head/socle와 restriction functor가 함께 쓰이는 다음 단계 lemmas를 읽는다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/kkko15-simplicity-heads-socles-tensor-products|KKKO15]], Theorem 3.2, pp.385-386: simple head/socle theorem for convolution with a real-simple factor, including the R-matrix image identifications.
- KKKO15, Corollary 3.3, p.386: equivalence between real simplicity, scalar self R-matrix, and scalar endomorphism algebra of $M\circ M$ in the symmetric case.
- KKKO15, Corollary 3.4, p.386: simplicity of $M^{\circ n}$ for real simple $M$.
- [[sources/papers/kashiwara-nakashima25-crystal-structure-localized-quantum-unipotent-coordinate-category|Kashiwara-Nakashima 2025]], Definition 4.13, Lemma 4.14, and Proposition 4.15, pp.25-26: $d_i(M)$ and head convolution with $L(i)$.
- Kashiwara-Nakashima 2025, Lemma 4.24, p.29: simple head and socle of $E_i^{(n)}(M)$.

</details>
