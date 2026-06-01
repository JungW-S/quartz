---
id: r-matrix-renormalization
title: R-Matrix Renormalization
level: advanced
topic_kind: concept
parent_topics:
  - graded-monoidal-categories
  - quiver-hecke-module-categories
prerequisite_topics:
  - graded-monoidal-categories
  - quiver-hecke-module-categories
child_topics:
  - normal-sequences
related_topics:
  - affine-objects-in-monoidal-categories
  - root-objects-in-localized-categories
maturity: example-ready
---

## 개요

R-matrix renormalization은 tensor product의 두 simple objects를 서로 바꾸는 R-matrix를, parameter $z$의 적절한 거듭제곱으로 보정하여 $z=0$에서도 사라지지 않는 morphism을 얻는 과정이다. 이 보정된 morphism은 R-matrix의 degree를 측정하고, localized category에서 root object와 root operator를 정의할 때 쓰이는 수치 $\Lambda$, $\mathfrak d$, $\widetilde\Lambda$를 제공한다.

이 topic에서 중요한 것은 세 level을 구분하는 것이다. 일반 monoidal-category level에서는 simple objects 사이의 R-matrix와 그 degree $\Lambda(M,N)$를 정의한다. Affine-object level에서는 rational center와 parameter $z$를 사용해 renormalized R-matrix를 만든다. Quiver-Hecke level에서는 intertwiner로 universal R-matrix가 정의되고, 이 구조가 일반 affinization/R-matrix framework와 연결된다.

[[topics/root-objects-in-localized-categories|Root Objects in Localized Categories]]의 정의에는 $\mathfrak d(L,\mathscr D^{-1}L)$이 직접 들어간다. [[topics/localized-root-operators|Localized Root Operators]]의 공식에는 $\widetilde\Lambda(X,Y)$가 들어간다. 따라서 R-matrix renormalization은 localized crystal을 읽기 위한 notation prerequisite이다.

## 준비와 notation

$\mathscr C$를 graded monoidal category라고 하자. Tensor product는 $\otimes$로 쓰고, grading shift를 포함한 morphism space를 $\operatorname{HOM}(-,-)$로 쓴다.

$M,N$은 $\mathscr C$ 안의 simple objects라고 한다. 두 simple objects 사이의 R-matrix는
$$
R_{M,N}:M\otimes N\to N\otimes M
$$
꼴의 nonzero morphism이다. 이 morphism은 항상 임의로 존재한다고 가정하지 않는다. Source에서는 해당 Hom-space가 1-dimensional일 때 R-matrix와 그 degree를 정의한다.

Affine-object 쪽에서는 [[topics/affine-objects-in-monoidal-categories|Affine Objects in Monoidal Categories]]의 notation을 사용한다. 즉 $(\widehat M,z)$는 affine object이고, rational center data는 $\widehat M$을 다른 objects와 tensor product 안에서 옮기는 isomorphisms를 제공한다.

Localized category에서는 simple objects $X,Y\in\widetilde{\mathcal C}_w$에 대해 ordinary degree $\Lambda(X,Y)$와 weight pairing을 함께 사용한다. 이때 modified degree를 $\widetilde\Lambda(X,Y)$로 쓴다.

## 정의

Simple pair $(M,N)$이 $\Lambda$-definable이라는 것은
$$
\dim\operatorname{HOM}(M\otimes N,N\otimes M)=1
$$
이라는 뜻이다. 이 경우 nonzero morphism
$$
R_{M,N}:M\otimes N\to N\otimes M
$$
을 $M$과 $N$ 사이의 R-matrix라고 하고,
$$
\Lambda(M,N)=\deg(R_{M,N})
$$
로 둔다.

반대 방향 pair $(N,M)$도 $\Lambda$-definable이면 $(M,N)$은 $\mathfrak d$-definable이고,
$$
\mathfrak d(M,N)
=
\frac{\Lambda(M,N)+\Lambda(N,M)}{2}
$$
로 둔다. 이 값은 양방향 R-matrix degree를 대칭적으로 모은 수치이다.

이제 $(\widehat M,R_{\widehat M})$가 rational center이고 $L\in\mathscr C$라고 하자. Rational center가 주는 isomorphism은 rational affine category 안에 있으므로, 그대로 $z=0$에서 잘 정의되는 morphism이 아닐 수 있다. Renormalized R-matrix는 어떤 정수 $m$을 골라
$$
R^{\mathrm{ren}}_{\widehat M,L}
=
z^m R_{\widehat M}(L)
$$
꼴로 보정한 morphism
$$
R^{\mathrm{ren}}_{\widehat M,L}:
\widehat M\otimes L\to L\otimes\widehat M
$$
이 $\operatorname{Pro}^{\mathrm{coh}}(\mathbf k[z],\mathscr C)$ 안에 있고, 그 specialization at $z=0$이 0이 아니도록 만든 것이다. 반대 방향
$$
R^{\mathrm{ren}}_{L,\widehat M}:L\otimes\widehat M\to\widehat M\otimes L
$$
도 같은 방식으로 정의된다.

Localized category $\widetilde{\mathcal C}_w$에서는 $\Lambda$-definable simple objects $X,Y$에 대해
$$
\widetilde\Lambda(X,Y)
=
\frac{\Lambda(X,Y)+(\operatorname{wt}X,\operatorname{wt}Y)}{2}
$$
를 사용한다. 이 $\widetilde\Lambda$는 localized root operator 공식에 들어가는 modified R-matrix degree이다.

## 기본 예시

Quiver-Hecke module category에서는 intertwiners를 사용해 universal R-matrix
$$
R^{\mathrm{univ}}_{M,N}:M\circ N\to N\circ M
$$
를 만든다. 여기서 $\circ$는 convolution product이다.

Simple module $M$의 quiver-Hecke affinization $(\widehat M,z_{\widehat M})$가 주어지면, universal R-matrix는 일반 monoidal-category sense의 affinization data와 호환된다. 이 호환성 때문에 quiver-Hecke module category에서 쓰는 R-matrix construction을 [[topics/affine-objects-in-monoidal-categories|affine-object]] framework 안에서 다룰 수 있다.

이 예시는 universal R-matrix와 renormalized R-matrix를 구별해야 함을 보여 준다. Universal R-matrix는 quiver-Hecke module 쪽에서 intertwiners로 만들어지는 morphism이고, renormalized R-matrix는 affine/rational center 상황에서 $z$의 거듭제곱을 곱해 $z=0$ specialization이 사라지지 않도록 만든 morphism이다.

검증: 논문 예시

## 핵심 관점

핵심은 R-matrix가 단순히 "tensor factors를 바꾸는 map"이 아니라, degree 정보를 가진다는 점이다.

$$
M\otimes N
\xrightarrow{\;R_{M,N}\;}
N\otimes M
\qquad
\leadsto
\qquad
\Lambda(M,N)=\deg(R_{M,N}).
$$

Affine object가 들어오면 rational center가 주는 R-matrix를 $z$의 거듭제곱으로 보정한다.

$$
R_{\widehat M}(L)
\quad\rightsquigarrow\quad
R^{\mathrm{ren}}_{\widehat M,L}
=z^m R_{\widehat M}(L).
$$

이 보정의 목적은 specialization at $z=0$이 0이 되지 않도록 만드는 것이다. 이렇게 얻은 degree data가 $\mathfrak d$와 $\widetilde\Lambda$를 통해 root-object condition과 localized root-operator formulas에 들어간다.

## 기본 성질

- $\Lambda(M,N)$는 $M\otimes N\to N\otimes M$ 방향 R-matrix의 homogeneous degree이다.
- $\mathfrak d(M,N)$는 양방향 R-matrix degrees의 half-sum이다.
- Rational center가 있으면 $z$의 적절한 거듭제곱을 곱해 renormalized R-matrix를 만들 수 있고, 이 보정된 morphism은 $z=0$에서 사라지지 않는다.
- 두 affine objects의 $z$-degrees가 호환되면 renormalized R-matrix는 $\operatorname{Aff}(\mathscr C)$ 안의 morphism
  $$
  \widehat M\otimes_z\widehat N
  \to
  \widehat N\otimes_z\widehat M
  $$
  을 유도한다.
- Localization functor $Q$는 affinizations와 R-matrix degree 비교에 관여한다. 특히 localized category로 내려가는 argument에서는 localized R-matrix degree가 original degree보다 커지지 않는 방향의 비교가 사용된다.
- $\widetilde\Lambda(X,Y)$는 $\Lambda(X,Y)$에 weight pairing을 더해 localized category에 맞게 조정한 degree이다.

## 다른 topic들과의 관계

- [[topics/affine-objects-in-monoidal-categories|Affine Objects in Monoidal Categories]]는 rational center와 affinization의 source를 제공한다.
- [[topics/quiver-hecke-module-categories|Quiver-Hecke Module Categories]]는 intertwiner로 universal R-matrix가 만들어지는 concrete category setting을 제공한다.
- [[topics/root-objects-in-localized-categories|Root Objects in Localized Categories]]는 $\mathfrak d(L,\mathscr D^{-1}L)$ 조건을 통해 R-matrix degree를 사용한다.
- [[topics/localized-root-operators|Localized Root Operators]]는 $\widetilde\Lambda(\widetilde Q_i,X)$와 $\widetilde\Lambda(X,\widetilde Q_i)$를 사용해 $\varepsilon_i,\varepsilon_i^*$를 정의한다.
- [[topics/normal-sequences|Normal Sequences]]는 R-matrix와 head/socle behavior를 사용하는 후속 topic이다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/graded-monoidal-categories|Graded Monoidal Categories]]에서 grading과 tensor product를 읽고, [[topics/quiver-hecke-module-categories|Quiver-Hecke Module Categories]]에서 convolution과 intertwiners를 읽고, [[topics/affine-objects-in-monoidal-categories|Affine Objects in Monoidal Categories]]에서 $(\widehat M,z)$와 rational center를 읽는다.
- 상위 개념: [[topics/graded-monoidal-categories|Graded Monoidal Categories]]와 [[topics/quiver-hecke-module-categories|Quiver-Hecke Module Categories]]가 더 넓은 setting이다.
- 다음에 읽을 것: [[topics/root-objects-in-localized-categories|Root Objects in Localized Categories]]에서는 $\mathfrak d$ condition을 읽고, [[topics/localized-root-operators|Localized Root Operators]]에서는 $\widetilde\Lambda$를 읽고, [[topics/normal-sequences|Normal Sequences]]에서는 뒤의 R-matrix applications를 읽는다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/kashiwara-nakashima25-crystal-structure-localized-quantum-unipotent-coordinate-category|Kashiwara-Nakashima 2025]], lines 1731-1747 of `inbox/papers/crystal.tex`: $\Lambda$-definable pairs, R-matrix, $\Lambda(M,N)$, and $\mathfrak d(M,N)$.
- Kashiwara-Nakashima 2025, lines 1777-1804: rational centers and affinizations.
- Kashiwara-Nakashima 2025, lines 1806-1834: renormalized R-matrices and induced morphisms in $\operatorname{Aff}(\mathscr C)$.
- Kashiwara-Nakashima 2025, lines 1837-1842 and 1958-2010: real/affreal simple objects and degree control from affinizations.
- Kashiwara-Nakashima 2025, lines 2331-2371: quiver-Hecke universal R-matrix and compatibility with the general affinization framework.
- Kashiwara-Nakashima 2025, lines 2976-3022: localization compatibility for affinizations.
- Kashiwara-Nakashima 2025, lines 3317-3354: localization comparison for $\Lambda$ and definition of $\widetilde\Lambda$.
- Kashiwara-Nakashima 2025, lines 3546-3553 and 3654-3657: use of affinizations and $\mathfrak d$ in root-object arguments.
- Source-location review: `reports/reviews/2026-06-01-affine-r-matrix-prerequisite-source-location-review.md`.

</details>
