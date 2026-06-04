---
id: pro-categories
title: Pro-Categories
level: prerequisite
topic_kind: root
parent_topics:
  - category-theory
prerequisite_topics:
  - category-theory
child_topics:
  - affine-objects-in-monoidal-categories
related_topics:
  - category-localization
maturity: definition-ready
---

## 개요

Pro-category는 어떤 category $\mathscr C$의 objects를 co-directed projective limit 형태로 완성해서 다루는 category이다. 여기서는 일반 pro-category 이론 전체가 아니라, [[topics/03-category-theory/affine-objects-in-monoidal-categories|Affine Objects in Monoidal Categories]]를 읽는 데 필요한 최소한의 $\operatorname{Pro}(\mathscr C)$ language를 정리한다.

Affine object $(\widehat M,z)$는 보통 $\mathscr C$ 안의 하나의 finite object가 아니라, quotients $\widehat M/z^n\widehat M$들의 projective limit로 회수되는 completed object이다. 그래서 affine object의 정의는 먼저 $\mathscr C$를 $\operatorname{Pro}(\mathscr C)$ 안에 넣고, 그 안에서 $z$-adic completion 조건을 말한다.

## 준비와 notation

$\mathscr C$를 category라고 하자. 여기서 $\mathscr C^\vee$는 $\mathscr C^{\operatorname{op}}$에서 $\mathbf{Set}^{\operatorname{op}}$로 가는 functors의 category로 둔다. Yoneda functor는 object $X\in\mathscr C$를
$$
Y\longmapsto \operatorname{Hom}_{\mathscr C}(X,Y)
$$
로 보내며, $\mathscr C$를 $\mathscr C^\vee$ 안에 fully faithfully 넣는다.

Index category $I$가 directed라는 것은 다음 세 조건을 만족한다는 뜻이다.

1. $I$가 비어 있지 않다.
2. 임의의 $i,j\in I$에 대해, 어떤 $k\in I$와 morphisms $i\to k$, $j\to k$가 있다.
3. 평행한 두 morphisms $f,g:i\rightrightarrows j$에 대해, 어떤 $h:j\to k$가 있어서 $h\circ f=h\circ g$가 된다.

$I^{\operatorname{op}}$가 directed이면 $I$를 co-directed라고 한다. Co-directed projective limit은
$$
\varprojlim
$$
으로 쓴다.

## 정의

### Pro-object

$\mathscr C$의 pro-object는 어떤 co-directed category $I$와 functor
$$
\beta:I\to\mathscr C\to\mathscr C^\vee
$$
에 대해 $\varprojlim\beta$와 isomorphic한 $\mathscr C^\vee$의 object이다.

### The category $\operatorname{Pro}(\mathscr C)$

$\operatorname{Pro}(\mathscr C)$는 $\mathscr C^\vee$ 안에서 pro-objects로 이루어진 full subcategory이다. Yoneda embedding을 통해 $\mathscr C$의 object도 $\operatorname{Pro}(\mathscr C)$ 안의 object로 볼 수 있다.

### Coherent pro-objects over $A$

Affine object를 위해서는 coherent pro-object subcategory도 필요하다. $A=\bigoplus_{k\in\mathbb Z}A_k$를 nonnegatively graded commutative $\mathbf k$-algebra라고 하자. $\operatorname{Mod}^{\mathrm{gr}}(A,\operatorname{Pro}(\mathscr C))$는 $\operatorname{Pro}(\mathscr C)$ 안의 graded $A$-modules로 이루어진 category이다.

$\operatorname{Pro}^{\mathrm{coh}}(A,\mathscr C)$는 $\operatorname{Mod}^{\mathrm{gr}}(A,\operatorname{Pro}(\mathscr C))$의 full subcategory로, object $\widehat M$이 다음 조건을 만족할 때 들어간다.

1. Special quotient $\widehat M/A_{>0}\widehat M$가 $\mathscr C$ 안의 object이다.
2. $\widehat M$이 $A$-adic quotients로부터
   $$
   \widehat M\simeq\varprojlim_k \widehat M/A_{\ge k}\widehat M
   $$
   로 복원된다.

## 기본 예시

### 구조 예시

$A=\mathbf k[z]$라면 $A_{\ge k}\widehat M$은 $z^k$ 이상 차수의 부분이 작용해서 생기는 부분 object 역할을 한다. 이때
$$
\widehat M/z\widehat M,\quad
\widehat M/z^2\widehat M,\quad
\widehat M/z^3\widehat M,\quad\ldots
$$
를 모두 기억하고, 이 quotient system의 projective limit으로 $\widehat M$을 회수한다는 것이 $\operatorname{Pro}^{\mathrm{coh}}(\mathbf k[z],\mathscr C)$의 핵심 mechanism이다.

이 예시는 concrete category의 예가 아니라, affine object 정의에서 쓰이는 completion 구조를 설명하는 구조 예시이다.

검증: 논문 예시

## 핵심 관점

Pro-category는 $\mathscr C$ 안에 직접 있지 않을 수 있는 completed object를 다루기 위한 ambient category이다. Affine object의 경우 중요한 그림은 다음과 같다.

$$
\widehat M
\simeq
\varprojlim_n \widehat M/z^n\widehat M,
\qquad
\widehat M/z\widehat M\in\mathscr C.
$$

즉 $\widehat M$ 자체는 pro-object level에 있지만, 첫 quotient는 다시 원래 category $\mathscr C$ 안으로 내려온다. 이 두 level의 구분이 없으면 affine object와 ordinary object $M$의 차이가 사라진다.

## 기본 성질

### Yoneda embedding

$\mathscr C$는 Yoneda functor를 통해 $\operatorname{Pro}(\mathscr C)$ 안에 fully faithfully 들어간다. 따라서 원래 category의 object를 pro-object로도 볼 수 있다.

### Finite-length subcategory

Finite-length graded category 조건 아래에서는 $\mathscr C$가 $\operatorname{Pro}(\mathscr C)$ 안의 full subcategory로 쓰인다. 여기서 필요한 안정성은 subquotients를 취해도 $\mathscr C$ 안에 남는다는 점이다.

### Coherent recovery

$\operatorname{Pro}^{\mathrm{coh}}(A,\mathscr C)$의 object는 special quotient가 $\mathscr C$ 안에 있고, $A$-adic quotients의 projective limit으로 복원된다.

### $z$-adic completion

$A=\mathbf k[z]$인 경우 이 language가 [[topics/03-category-theory/affine-objects-in-monoidal-categories|affine object]]의 $z$-adic completeness condition을 표현한다.

## 다른 topic들과의 관계

**Affine Objects in Monoidal Categories.** [[topics/03-category-theory/affine-objects-in-monoidal-categories|Affine Objects in Monoidal Categories]]는 $\operatorname{Pro}^{\mathrm{coh}}(\mathbf k[z],\mathscr C)$ 안에서 affine object $(\widehat M,z)$를 정의한다. Pro-category language는 $\widehat M$을 completed object로 다루는 데 쓰인다.

**Graded Monoidal Categories.** [[topics/03-category-theory/graded-monoidal-categories|Graded Monoidal Categories]]는 pro-category language 위에 tensor product와 grading shift $q$를 함께 놓는다. Affine objects를 tensor product와 함께 쓰려면 이 추가 structure가 필요하다.

**Localization of Categories.** [[topics/08-localization-of-categories/category-localization|Localization of Categories]]도 category를 더 큰 category로 옮겨서 object와 morphism을 다룬다는 점에서는 관련이 있다. 그러나 pro-category completion은 projective-limit completion이고, localization은 지정한 morphisms나 objects를 invertible하게 만드는 construction이다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/03-category-theory/category-theory|Category Theory]]에서 category, functor, full subcategory, embedding language를 먼저 읽는다.
- 상위 개념: [[topics/03-category-theory/category-theory|Category Theory]]가 일반 category language를 제공한다.
- 다음에 읽을 것: [[topics/03-category-theory/affine-objects-in-monoidal-categories|Affine Objects in Monoidal Categories]]에서는 $\operatorname{Pro}^{\mathrm{coh}}(\mathbf k[z],\mathscr C)$를 읽고, [[topics/03-category-theory/graded-monoidal-categories|Graded Monoidal Categories]]에서는 tensor와 grading structure를 읽는다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/kashiwara-nakashima25-crystal-structure-localized-quantum-unipotent-coordinate-category|Kashiwara-Nakashima 2025]], lines 1526-1548 of `inbox/papers/crystal.tex`: Yoneda functor, directed/co-directed categories, pro-objects, $\operatorname{Pro}(\mathscr C)$, and $\varprojlim$ notation.
- Kashiwara-Nakashima 2025, lines 1550-1577: finite-length graded category assumptions and the embedding of $\mathscr C$ into $\operatorname{Pro}(\mathscr C)$.
- Kashiwara-Nakashima 2025, lines 1578-1621: $\operatorname{Mod}^{\mathrm{gr}}(A,\operatorname{Pro}(\mathscr C))$ and $\operatorname{Pro}^{\mathrm{coh}}(A,\mathscr C)$.
- Kashiwara-Nakashima 2025, lines 1623-1630: the $A=\mathbf k[z]$ specialization and the recovery condition $\widehat M\simeq\varprojlim_n\widehat M/z^n\widehat M$.
- Fillability review: `reports/reviews/2026-06-01-pro-graded-prerequisite-fillability-review.md`.

</details>
