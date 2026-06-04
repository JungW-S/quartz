---
id: type-a-klr-segment-modules
title: Type A KLR Segment Modules
level: advanced
topic_kind: object-family
parent_topics:
  - quiver-hecke-module-categories
prerequisite_topics:
  - quiver-hecke-algebras
  - quiver-hecke-module-categories
child_topics:
  - type-a-segment-module-convolutions
related_topics:
  - quantum-affine-r-matrix-denominators
  - quantum-affine-schur-weyl-duality
maturity: example-ready
---

## 개요

Type $A$ KLR segment module은 type $A_\infty$ quiver-Hecke algebra에서 consecutive vertices
$$
a,a+1,\ldots,b
$$
에 붙는 가장 기본적인 one-dimensional graded module이다. 하나의 segment는 하나의 interval이고, 여러 segment를 순서 있게 묶은 ordered multisegment는 finite-dimensional simple graded modules를 분류하는 combinatorial parameter로 쓰인다.

이 topic은 [[topics/07-quantum-affine-algebras/quantum-affine-r-matrix-denominators|Quantum Affine R-Matrix Denominators]]에서 얻은 type $A_\infty$ KLR input을 실제 module objects로 읽기 위한 중간층이다. 그 다음 [[topics/07-quantum-affine-algebras/quantum-affine-schur-weyl-duality|Quantum Affine Schur-Weyl Duality]]에서 이 segment modules가 quantum affine fundamental representations로 가는 예시를 본다. 여기서는 segment modules와 functor image만 다루고, localized category나 Grothendieck-ring comparison은 다루지 않는다.

## 준비와 notation

$J=\mathbb Z$를 type $A_\infty$ vertex set으로 두고, $\epsilon_a-\epsilon_{b+1}$를 consecutive simple roots
$$
\alpha_a+\alpha_{a+1}+\cdots+\alpha_b
$$
에 해당하는 positive root로 읽는다.

Segment는 정수쌍 $(a,b)$이다. $a\le b$이면 length는
$$
\ell=b-a+1
$$
이다. Length $0$ convention으로 $L(a,a-1)$도 $R(0)=\mathbf k$-module로 둔다. $a=b$일 때는 $L(a,a)$ 대신 $L(a)$라고 쓴다.

$R(\epsilon_a-\epsilon_{b+1})$는 이 root에 붙는 type $A_\infty$ KLR algebra이다. Idempotent $e(\nu)$에서 $\nu$는 vertices의 word이고, segment $(a,b)$에 대응하는 word는
$$
(a,a+1,\ldots,b)
$$
이다.

## 정의

### Segment module $L(a,b)$

$a\le b$인 segment $(a,b)$에 대해, segment module $L(a,b)$는 degree $0$ generator $u(a,b)$로 생성되는 one-dimensional graded $R(\epsilon_a-\epsilon_{b+1})$-module이다. KLR generators의 작용은 다음과 같다.

$$
x_m u(a,b)=0,\qquad \tau_k u(a,b)=0,
$$

그리고 idempotent 작용은
$$
e(\nu)u(a,b)=
\begin{cases}
u(a,b) & \text{if }\nu=(a,a+1,\ldots,b),\\
0 & \text{otherwise}
\end{cases}
$$
이다.

### Ordered multisegments

Multisegment는 segment들의 finite sequence이다. Segment들의 순서는
$$
(a_1,b_1)>(a_2,b_2)
$$
를 $a_1>a_2$, 또는 $a_1=a_2$이고 $b_1>b_2$일 때로 정한다. 이 순서에 대해
$$
(a_1,b_1)\ge (a_2,b_2)\ge\cdots\ge(a_t,b_t)
$$
를 만족하는 multisegment를 ordered multisegment라고 한다.

## 기본 예시

### 실제 예시

Length $1$ segment $(a,a)$에 붙는 module은 $L(a)$이다. 이 module은 $R(\alpha_a)$ 위의 one-dimensional graded module이고, generator $u(a)$는 word $(a)$에 대응하는 idempotent에서만 살아남는다.

Type $A_{N-1}^{(1)}$ Schur-Weyl functor $F$는 이 module을
$$
F(L(a))\simeq V(\varpi_1)_{(-q)^{2a}}
$$
로 보낸다. 즉 length $1$ segment module은 spectral parameter $(-q)^{2a}$를 가진 first fundamental representation으로 간다.

예시 검증: 논문에 근거한 예시

## 핵심 관점

Segment module은 type $A_\infty$ KLR side의 interval object이다.

$$
(a,b)
\quad\leadsto\quad
L(a,b)
\quad\leadsto\quad
V(\varpi_\ell)_{(-q)^{a+b}}
$$

첫 번째 화살표는 interval을 one-dimensional KLR module로 바꾸는 object-level construction이다. 두 번째 화살표는 type $A_{N-1}^{(1)}$ Schur-Weyl functor가 segment length $\ell=b-a+1$을 fundamental weight index로 읽는다는 뜻이다.

## 기본 성질

### Proposition-level fact: ordered-multisegment classification

Finite-dimensional simple graded $R(\ell)$-modules는 grading shift를 제외하면 ordered multisegments로 parametrized된다. Ordered multisegment
$$
(a_1,b_1),\ldots,(a_t,b_t)
$$
가 주어지면 corresponding simple module은 convolution product
$$
L(a_1,b_1)\circ\cdots\circ L(a_t,b_t)
$$
의 head로 얻어진다.

### Proposition-level fact: Schur-Weyl image of a segment

Segment $(a,b)$의 length를 $\ell=b-a+1$이라고 하자. Type $A_{N-1}^{(1)}$ Schur-Weyl functor $F$에 대해, $0\le \ell\le N$이면
$$
F(L(a,b))\simeq V(\varpi_\ell)_{(-q)^{a+b}}
$$
이고, $\ell>N$이면
$$
F(L(a,b))\simeq 0
$$
이다. 여기서 $V(\varpi_0)$와 $V(\varpi_N)$은 trivial representation으로 이해된다.

## 다른 topic들과의 관계

**Quiver-Hecke Algebras.** [[topics/06-quiver-hecke-klr-algebras/quiver-hecke-algebras|Quiver-Hecke Algebras]]는 $R(\beta)$, idempotents $e(\nu)$, generators $x_m,\tau_k$의 algebra-level definition을 제공한다. Segment module $L(a,b)$의 definition은 이 algebra presentation 위에서 주어진다.

**Quiver-Hecke Module Categories.** [[topics/06-quiver-hecke-klr-algebras/quiver-hecke-module-categories|Quiver-Hecke Module Categories]]는 $L(a,b)$와 그 convolution products가 사는 category-level ambient space이다.

**Type A Segment Module Convolutions.** [[topics/06-quiver-hecke-klr-algebras/type-a-segment-module-convolutions|Type A Segment Module Convolutions]]는 두 segment modules의 product가 interval positions에 따라 irreducible하게 남는지, exact sequence를 만드는지, R-matrix image가 head와 socle을 어떻게 잡는지를 다룬다.

**Quantum Affine R-Matrix Denominators.** [[topics/07-quantum-affine-algebras/quantum-affine-r-matrix-denominators|Quantum Affine R-Matrix Denominators]]는 type $A_\infty$ KLR data가 quantum affine R-matrix denominator에서 어떻게 나오는지 설명한다.

**Quantum Affine Schur-Weyl Duality.** [[topics/07-quantum-affine-algebras/quantum-affine-schur-weyl-duality|Quantum Affine Schur-Weyl Duality]]는 여기서 정의한 $L(a,b)$를 quantum affine fundamental representations로 보내는 functor를 다룬다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/06-quiver-hecke-klr-algebras/quiver-hecke-algebras|Quiver-Hecke Algebras]]에서 $R(\beta)$의 generators와 idempotents를 읽고, [[topics/06-quiver-hecke-klr-algebras/quiver-hecke-module-categories|Quiver-Hecke Module Categories]]에서 convolution product를 읽는다. Quantum affine 쪽에서 왜 type $A_\infty$ KLR input이 나오는지는 [[topics/07-quantum-affine-algebras/quantum-affine-r-matrix-denominators|Quantum Affine R-Matrix Denominators]]에서 읽는다.
- 상위 개념: [[topics/06-quiver-hecke-klr-algebras/quiver-hecke-module-categories|Quiver-Hecke Module Categories]].
- 다음에 읽을 것: single segment의 Schur-Weyl image가 목적이면 [[topics/07-quantum-affine-algebras/quantum-affine-schur-weyl-duality|Quantum Affine Schur-Weyl Duality]]로 간다. Segment products와 ordered multisegment의 head/socle behavior가 필요하면 [[topics/06-quiver-hecke-klr-algebras/type-a-segment-module-convolutions|Type A Segment Module Convolutions]]를 읽는다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/kang-kashiwara-kim18-symmetric-quiver-hecke-algebras-r-matrices|Kang-Kashiwara-Kim 2018]], Section 4.2, arXiv PDF p.36: segments, multisegments, and the one-dimensional module $L(a,b)$.
- Kang-Kashiwara-Kim 2018, Proposition 4.2.5, arXiv PDF p.39: classification of finite-dimensional simple graded type $A$ KLR modules by ordered multisegments.
- Kang-Kashiwara-Kim 2018, Proposition 4.3.1, arXiv PDF pp.43-44: $F(L(a,b))\simeq V(\varpi_\ell)_{(-q)^{a+b}}$ for $0\le \ell\le N$ and $F(L(a,b))=0$ for $\ell>N$.

</details>
