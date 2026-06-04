---
id: category-theory
title: Category Theory
level: prerequisite
topic_kind: root
parent_topics: []
prerequisite_topics: []
child_topics:
  - graded-monoidal-categories
  - pro-categories
  - category-localization
related_topics:
  - monoidal-categorification
maturity: example-ready
---

## 개요

Category theory는 objects와 그 사이의 morphisms를 함께 놓고, composition이 어떻게 작동하는지를 기록하는 언어이다. 여기서는 category theory 전체를 전개하지 않고, 뒤의 topic들에서 반복적으로 쓰이는 category, functor, natural transformation, universal property의 최소 vocabulary를 고정한다.

이 언어가 필요한 이유는 많은 construction이 개별 object 하나가 아니라 category 전체에서 정의되기 때문이다. 예를 들어 [[topics/03-category-theory/graded-monoidal-categories|Graded Monoidal Categories]]에서는 tensor product와 grading shift가 category 위에서 함께 움직이고, [[topics/08-localization-of-categories/category-localization|Localization of Categories]]에서는 monoidal category 자체를 바꾸어 chosen objects를 invertible하게 만든다.

## 준비와 notation

Category는 보통 $\mathcal C,\mathcal D$처럼 쓴다. Objects는 $X,Y,Z\in\mathcal C$로 쓰고, $X$에서 $Y$로 가는 morphisms의 collection은
$$
\mathcal C(X,Y)
$$
로 쓴다.

Morphism $f\in\mathcal C(X,Y)$는
$$
f:X\to Y
$$
라고 쓴다. $f:X\to Y$와 $g:Y\to Z$가 있으면 composite는
$$
g\circ f:X\to Z
$$
이다. Object $X$의 identity morphism은
$$
1_X:X\to X
$$
로 쓴다.

Categories 사이의 functor는 보통
$$
F:\mathcal C\to\mathcal D
$$
로 쓴다. 같은 source와 target을 갖는 두 functors $F,G:\mathcal C\to\mathcal D$ 사이의 natural transformation은
$$
\alpha:F\Rightarrow G
$$
로 쓴다.

## 정의

Category $\mathcal C$는 다음 data로 이루어진다.

1. Objects의 collection $\operatorname{ob}(\mathcal C)$.
2. 각 $X,Y\in\operatorname{ob}(\mathcal C)$에 대한 morphisms의 collection $\mathcal C(X,Y)$.
3. 각 $X,Y,Z$에 대한 composition operation
   $$
   \mathcal C(Y,Z)\times\mathcal C(X,Y)\to\mathcal C(X,Z),
   \qquad
   (g,f)\mapsto g\circ f.
   $$
4. 각 object $X$에 대한 identity morphism $1_X\in\mathcal C(X,X)$.

이 data는 두 가지 axiom을 만족해야 한다. 첫째, composition은 associative이다. 즉 composable morphisms
$$
X\xrightarrow{f}Y\xrightarrow{g}Z\xrightarrow{h}W
$$
에 대해
$$
(h\circ g)\circ f=h\circ(g\circ f)
$$
이다. 둘째, identity morphisms는 identity laws를 만족한다. 즉 $f:X\to Y$이면
$$
f\circ 1_X=f=1_Y\circ f
$$
이다.

Functor $F:\mathcal C\to\mathcal D$는 objects를 objects로, morphisms를 morphisms로 보내는 rule이다. 구체적으로 $F$는 각 $X\in\mathcal C$에 대해 object $F(X)\in\mathcal D$를 주고, 각 morphism $f:X\to Y$에 대해 morphism
$$
F(f):F(X)\to F(Y)
$$
를 준다. 이때
$$
F(g\circ f)=F(g)\circ F(f),
\qquad
F(1_X)=1_{F(X)}
$$
가 성립해야 한다.

Natural transformation $\alpha:F\Rightarrow G$는 각 $X\in\mathcal C$에 대해 morphism
$$
\alpha_X:F(X)\to G(X)
$$
를 하나씩 주는 family이다. 이 family는 모든 morphism $f:X\to Y$에 대해 square
$$
\begin{array}{ccc}
F(X) & \xrightarrow{F(f)} & F(Y)\\
\alpha_X\downarrow & & \downarrow\alpha_Y\\
G(X) & \xrightarrow{G(f)} & G(Y)
\end{array}
$$
가 commute하도록 해야 한다. 즉
$$
G(f)\circ\alpha_X=\alpha_Y\circ F(f)
$$
이다.

## 기본 예시

### 실제 예시: familiar mathematical categories

Leinster의 Examples 1.1.3은 다음 standard categories를 제시한다.

- $\mathbf{Set}$: objects는 sets이고 morphisms는 functions이다.
- $\mathbf{Grp}$: objects는 groups이고 morphisms는 group homomorphisms이다.
- $\mathbf{Ring}$: objects는 rings이고 morphisms는 ring homomorphisms이다.
- $\mathbf{Vect}_k$: objects는 field $k$ 위의 vector spaces이고 morphisms는 linear maps이다.
- $\mathbf{Top}$: objects는 topological spaces이고 morphisms는 continuous maps이다.

이 예시들은 category의 objects가 무엇이고 morphisms가 무엇인지를 먼저 정하면, composition과 identities는 보통 familiar map composition과 identity maps에서 온다는 점을 보여 준다.

검증: 문헌 예시

## 핵심 관점

Category theory에서 핵심은 object 하나의 내부 원소를 보는 것이 아니라, 그 object가 다른 objects와 어떤 morphisms로 연결되는지를 보는 것이다. 따라서 같은 mathematical object라도 어떤 morphisms를 허용하느냐에 따라 다른 category 안에 놓일 수 있다.

또 하나의 핵심 관점은 universal property이다. Universal property는 어떤 object를 내부 construction으로 설명하기보다, 모든 다른 objects와의 morphism 관계로 특징짓는다. 예를 들어 one-point set $1$은 모든 set $X$에서 $1$로 가는 function이 정확히 하나 있다는 성질로 특징지을 수 있다.

여기서는 universal property를 일반 이론으로 전개하지 않는다. 다만 이후 [[topics/08-localization-of-categories/category-localization|Localization of Categories]], [[topics/03-category-theory/pro-categories|Pro-Categories]], [[topics/01-quantum-groups/verma-modules|Verma Modules]] 같은 topic에서 “정의하는 object가 어떤 maps에 대해 universal하다”는 문장을 읽을 준비만 한다.

## 기본 성질

### 긴 composite의 well-definedness

Identity와 associativity axioms 때문에 composable chain
$$
X_0\xrightarrow{f_1}X_1\xrightarrow{f_2}\cdots\xrightarrow{f_n}X_n
$$
에서 괄호를 어떻게 치더라도 같은 composite morphism $X_0\to X_n$을 얻는다. 이 때문에 긴 composite를
$$
f_n\circ\cdots\circ f_1
$$
처럼 괄호 없이 쓸 수 있다.

### Functor의 보존 성질

Functor는 composition과 identities를 보존한다. 따라서 diagram이 category $\mathcal C$에서 commute하면, 그 diagram을 $F$로 보낸 image diagram도 $\mathcal D$에서 commute한다.

### Natural transformation의 commuting square

Natural transformation의 naturality condition은 두 방식의 이동이 같은 morphism을 준다는 commuting-square condition이다. 즉 먼저 $F$를 따라 morphism을 보낸 뒤 $\alpha$로 이동하는 것과, 먼저 $\alpha$로 이동한 뒤 $G$를 따라 morphism을 보내는 것이 같다.

## 다른 topic들과의 관계

- [[topics/03-category-theory/graded-monoidal-categories|Graded Monoidal Categories]]는 category에 tensor product와 grading shift가 추가된 setting이다.
- [[topics/03-category-theory/pro-categories|Pro-Categories]]는 category를 co-directed projective system으로 확장해 completed objects를 다룬다.
- [[topics/08-localization-of-categories/category-localization|Localization of Categories]]는 category 안의 chosen objects를 invertible하게 만들도록 category를 바꾸는 construction이다.
- [[topics/05-monoidal-categorification/monoidal-categorification|Monoidal Categorification]]은 Grothendieck ring과 monoidal category를 연결한다.

## 더 읽을 topic

- 먼저 읽을 것: 이 topic은 category theory로 들어가는 시작점이다. 별도 prerequisite는 두지 않는다.
- 상위 개념: 없음. 이 topic이 category theory의 basic parent topic이다.
- 다음에 읽을 것: [[topics/03-category-theory/graded-monoidal-categories|Graded Monoidal Categories]]를 읽으면 tensor product가 있는 category로 넘어간다. [[topics/03-category-theory/pro-categories|Pro-Categories]]는 completed objects가 필요한 곳에서 읽는다. [[topics/08-localization-of-categories/category-localization|Localization of Categories]]는 localization construction을 읽기 전에 본다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/books/leinster14-basic-category-theory|Leinster 2014/2016]], Definition 1.1.1, printed p.10: category, objects, morphisms, composition, identities, associativity, and identity laws.
- Leinster 2014/2016, Examples 1.1.3, printed p.11: $\mathbf{Set}$, $\mathbf{Grp}$, $\mathbf{Ring}$, $\mathbf{Vect}_k$, and $\mathbf{Top}$ as basic categories.
- Leinster 2014/2016, Definition 1.2.1, printed p.17: functors and their preservation of composition and identities.
- Leinster 2014/2016, Definition 1.3.1, printed pp.27-28: natural transformations and the naturality square.
- Leinster 2014/2016, Introduction, printed pp.1-7: universal-property orientation and the one-point-set example.

</details>
