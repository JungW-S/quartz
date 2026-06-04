---
id: lie-algebra-representations
title: Lie Algebra Representations
level: core
topic_kind: root
parent_topics: []
prerequisite_topics:
  - universal-enveloping-algebras
child_topics:
  - weight-modules
related_topics:
  - quantum-groups
maturity: example-ready
---

## 개요

Lie algebra representation은 Lie algebra $L$의 elements를 vector space $V$ 위의 linear operators로 해석하는 구조이다. 같은 구조를 action notation으로 쓰면 $L$이 $V$ 위에 작용한다고 말하고, 이 action을 갖춘 vector space를 $L$-module이라고 부른다.

이 topic의 목표는 두 notation을 분리해서 읽는 것이다. 하나는 homomorphism $\rho:L\to\mathfrak{gl}(V)$이고, 다른 하나는 action $xv$이다. 두 표기는 같은 data를 나타내지만, 이후 [[topics/01-quantum-groups/weight-modules|Weight Modules]]와 [[topics/01-quantum-groups/quantum-groups|Quantum Groups]]에서는 action notation이 더 자주 쓰인다.

## 준비와 notation

$\mathbb F$를 field라고 하자. Lie algebra는 $L$로 쓰고, bracket은
$$
[-,-]:L\times L\to L
$$
로 쓴다. Vector space $V$의 endomorphism algebra는
$$
\mathfrak{gl}(V)=\operatorname{End}_{\mathbb F}(V)
$$
로 쓴다.

$\mathfrak{gl}(V)$는 commutator bracket
$$
[A,B]=AB-BA
$$
를 갖는 Lie algebra이다. 따라서 map $\rho:L\to\mathfrak{gl}(V)$가 Lie algebra homomorphism인지 묻는 것이 의미가 있다.

## 정의

### Representation map

Lie algebra $L$의 representation on $V$는 Lie algebra homomorphism
$$
\rho:L\longrightarrow \mathfrak{gl}(V)
$$
이다. 이 말은 모든 $x,y\in L$에 대해
$$
\rho([x,y])=[\rho(x),\rho(y)]
=\rho(x)\rho(y)-\rho(y)\rho(x)
$$
가 성립한다는 뜻이다.

### Module action

$L$-module은 vector space $V$와 bilinear action
$$
L\times V\longrightarrow V,\qquad (x,v)\longmapsto xv
$$
로 이루어지며, 모든 $x,y\in L$과 $v\in V$에 대해
$$
[x,y]v=x(yv)-y(xv)
$$
를 만족한다.

### 두 notation의 대응

Representation $\rho$가 주어지면 $xv=\rho(x)(v)$로 $L$-module structure를 얻는다. 반대로 $L$-module action이 주어지면 $\rho(x)(v)=xv$로 representation $\rho:L\to\mathfrak{gl}(V)$를 얻는다.

## 기본 예시

### 실제 예시: natural representation of $\mathfrak{gl}(n,\mathbb F)$

$L=\mathfrak{gl}(n,\mathbb F)$이고 $V=\mathbb F^n$이라고 하자. Hong-Kang Example 1.2.2(1)은 $L$이 $V$ 위에 matrix multiplication으로 작용한다고 둔다.
$$
(x,v)\longmapsto xv.
$$

따라서 각 $x\in\mathfrak{gl}(n,\mathbb F)$는 $V$ 위의 linear operator로 작용한다. 이 action에 대응하는 representation map은
$$
\rho:\mathfrak{gl}(n,\mathbb F)\longrightarrow\mathfrak{gl}(V),
\qquad
\rho(x)(v)=xv
$$
로 볼 수 있다.

이 representation은 $\mathfrak{gl}(n,\mathbb F)$의 vector representation 또는 natural representation이다. 여기서는 matrix $x$ 자체가 linear operator로 작용하므로, representation map은 matrix multiplication action을 그대로 기록한다.

검증: 문헌 예시

## 기본 성질

### Bracket 보존

Representation condition은 Lie bracket을 operator commutator로 보존한다. 즉 $L$ 안의 bracket 계산은 $V$ 위의 operators 사이의 commutator 계산과 호환되어야 한다.

### Action notation

$L$-module condition은 같은 compatibility를 action notation으로 쓴 것이다. Formula $[x,y]v=x(yv)-y(xv)$는 bracket $[x,y]$의 action이 $x$와 $y$의 successive actions로부터 정해지는 방식을 나타낸다.

### 두 언어의 동일성

Lie algebra representation과 $L$-module은 같은 data의 두 notation이다. 이후 topic에서는 상황에 따라 $\rho(x)(v)$보다 $xv$ notation을 더 자주 사용한다.

## 다른 topic들과의 관계

**Universal Enveloping Algebras.** [[topics/01-quantum-groups/universal-enveloping-algebras|Universal Enveloping Algebras]]는 Lie algebra action을 associative algebra action으로 옮기는 언어를 제공한다. $L$-module language는 여기서 $U(L)$-module language와 연결된다.

**Weight Modules.** [[topics/01-quantum-groups/weight-modules|Weight Modules]]는 representation에서 Cartan part의 action을 weight spaces로 분해해서 보는 다음 단계이다.

**Quantum Groups.** [[topics/01-quantum-groups/quantum-groups|Quantum Groups]]에서는 $U_q(\mathfrak g)$의 generators가 vector space 위의 operators로 작용한다. Lie algebra representation은 이 관점을 classical case에서 먼저 보여준다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/books/hong-kang02-introduction-quantum-groups-crystal-bases|Hong-Kang 2002]], Chapter 1, Definition 1.2.1, p.3: representation of a Lie algebra and $L$-module.
- Hong-Kang 2002, Chapter 1, Example 1.2.2(1), p.4: the natural representation of $\mathfrak{gl}(n,\mathbb F)$ on $V=\mathbb F^n$ by matrix multiplication.

</details>
