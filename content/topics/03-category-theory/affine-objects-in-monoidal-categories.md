---
id: affine-objects-in-monoidal-categories
title: Affine Objects in Monoidal Categories
level: advanced
topic_kind: object-family
parent_topics:
  - pro-categories
  - graded-monoidal-categories
prerequisite_topics:
  - pro-categories
  - graded-monoidal-categories
child_topics: []
related_topics:
  - r-matrix-renormalization
  - root-objects-in-localized-categories
maturity: example-ready
---

## 개요

Affine object는 graded monoidal category $\mathscr C$의 object를 formal parameter $z$를 가진 completed pro-object로 다루기 위한 장치이다. 기본 형태는 pair $(\widehat M,z)$이며, $\widehat M$은 $\operatorname{Pro}(\mathscr C)$ 안에 있고 $z$로 나눈 quotient
$$
\widehat M/z\widehat M
$$
가 다시 원래 category $\mathscr C$ 안의 object가 되도록 요구한다.

이 개념은 [[topics/08-localization-of-categories/root-objects-in-localized-categories|Root Objects in Localized Categories]]에서 필요하다. Root object의 정의는 real simple object $L$이 affinization $(\widehat L,z)$을 갖는다는 조건을 포함하기 때문이다. 따라서 affine object는 localized crystal의 root direction을 category 안에서 다루기 위한 준비 단계이다.

중요한 구분은 다음과 같다. Affine object는 pair $(\widehat M,z)$ 자체이다. 어떤 object $M$의 affinization은 그 affine object가 special fiber $\widehat M/z\widehat M\simeq M$와 rational-center data를 함께 갖는 경우이다.

## 준비와 notation

$\mathscr C$를 finite-length graded $\mathbf k$-linear category라고 하자. Grading shift functor를 $q$로 쓴다. $\operatorname{Pro}(\mathscr C)$는 $\mathscr C$의 pro-objects로 이루어진 category이고, co-directed projective limit을
$$
\varprojlim
$$
으로 쓴다.

$A$를 nonnegatively graded commutative $\mathbf k$-algebra라고 하자. $\operatorname{Mod}^{\mathrm{gr}}(A,\operatorname{Pro}(\mathscr C))$는 $\operatorname{Pro}(\mathscr C)$ 안의 graded $A$-modules로 이루어진 category이다.

이 안에서 $\operatorname{Pro}^{\mathrm{coh}}(A,\mathscr C)$는 다음 두 조건을 만족하는 objects $\widehat M$으로 이루어진 full subcategory이다.

- $\widehat M/A_{>0}\widehat M$가 $\mathscr C$ 안의 object이다.
- $\widehat M$이 $A$-adic quotients의 projective limit으로 복원된다.

Affine object를 정의할 때는 $A=\mathbf k[z]$를 사용한다. 여기서 $z$는 positive homogeneous degree를 가지는 indeterminate이다.

## 정의

$z$를 positive homogeneous degree $d$를 가지는 indeterminate라고 하자. $\mathscr C$ 안의 affine object는 다음 조건을 만족하는 pair $(\widehat M,z)$이다.

1. $\widehat M\in\operatorname{Pro}(\mathscr C)$이고
   $$
   z\in\operatorname{End}_{\operatorname{Pro}^{\mathrm{coh}}(\mathbf k[z],\mathscr C)}(\widehat M)_d
   $$
   이다.
2. Quotient
   $$
   \widehat M/z\widehat M
   $$
   가 $\mathscr C$ 안의 object이다.
3. $\widehat M$은 $z$-adic quotients로부터
   $$
   \widehat M\simeq \varprojlim_n \widehat M/z^n\widehat M
   $$
   로 복원된다.
4. $z:\widehat M\to\widehat M$는 monomorphism이다.

Affine objects의 category를
$$
\operatorname{Aff}(\mathscr C)
$$
로 쓴다.

어떤 object $M\in\mathscr C$의 affinization은 affine object $(\widehat M,z)$에 rational-center data가 더해져 있고,
$$
\widehat M/z\widehat M\simeq M
$$
을 만족하는 경우이다. 즉 affinization은 $M$ 자체가 아니라, $M$을 special fiber로 갖는 $z$-family이다.

Simple object $M$이 real이라는 것은 $M\otimes M$이 simple이라는 뜻이다. Real simple object가 affinization을 가지면 $M$을 affreal simple object라고 한다.

## 기본 예시

Quiver-Hecke module category에서 simple root에 대응하는 simple module을
$$
L(i)=\langle i\rangle
$$
라고 쓴다. 이 object는 affreal simple module이다.

이 예시는 affine object가 추상적인 pro-category 장치로만 끝나지 않는다는 것을 보여 준다. Quiver-Hecke category에서 simple root object는 affinization을 갖고, 이런 affreal object가 이후 [[topics/08-localization-of-categories/root-objects-in-localized-categories|root object]]와 localized root operator의 입력으로 이어진다.

검증: 논문 예시

## 핵심 관점

Affine object의 핵심은 하나의 object를 $z$-방향으로 두껍게 만든 뒤, 다시 $z=0$ fiber로 원래 object를 회수하는 것이다.

$$
\widehat M
\quad\rightsquigarrow\quad
\widehat M/z\widehat M
\simeq M.
$$

Pro-category가 필요한 이유는 $\widehat M$이 단순히 $\mathscr C$ 안의 하나의 finite object가 아니라, quotients
$$
\widehat M/z^n\widehat M
$$
들의 projective limit로 주어지는 completed object이기 때문이다.

Affinization은 여기에 rational-center data를 더한다. 이 data는 $\widehat M$을 다른 objects와 tensor product 안에서 옮기는 R-matrix-type isomorphisms를 제공하며, 이 부분이 [[topics/06-quiver-hecke-klr-algebras/r-matrix-renormalization|R-Matrix Renormalization]]으로 이어진다.

## 기본 성질

- Category level: $\operatorname{Aff}(\mathscr C)$는 affine objects로 이루어진 category이다.
- Monoidal level: $\mathscr C$가 graded monoidal category이면 $\operatorname{Aff}(\mathscr C)$에도 monoidal product가 정의된다. 두 affine objects의 product는 $z\otimes1-1\otimes z$로 quotient를 취하는 방식으로 만든다.
- Rigidity level: $\mathscr C$가 rigid이면 $\operatorname{Aff}(\mathscr C)$도 rigid monoidal category가 된다.
- Quiver-Hecke specialization: Quiver-Hecke module category에서 정의된 affinization은 일반 monoidal-category sense의 affinization과 호환된다.
- Localization level: $L\in R\text{-gmod}$가 affinization을 가지면, localization functor $Q$를 통해 $Q(L)$도 localized category 안에서 affinization을 갖는다.

## 다른 topic들과의 관계

- [[topics/03-category-theory/pro-categories|Pro-Categories]]는 $\operatorname{Pro}(\mathscr C)$와 projective-limit language를 제공한다.
- [[topics/03-category-theory/graded-monoidal-categories|Graded Monoidal Categories]]는 grading shift $q$, tensor product, rigidity 같은 ambient structure를 제공한다.
- [[topics/06-quiver-hecke-klr-algebras/r-matrix-renormalization|R-Matrix Renormalization]]는 affinization의 rational-center data에서 나오는 renormalized R-matrix를 다룬다.
- [[topics/08-localization-of-categories/root-objects-in-localized-categories|Root Objects in Localized Categories]]는 real simple object가 affinization을 갖는다는 조건을 정의에 사용한다.
- [[topics/08-localization-of-categories/localized-root-operators|Localized Root Operators]]는 root objects를 사용해 localized category의 crystal operators를 만든다.

## 더 읽을 topic

- 먼저 읽을 것: [[topics/03-category-theory/pro-categories|Pro-Categories]]에서 $\operatorname{Pro}(\mathscr C)$를 읽고, [[topics/03-category-theory/graded-monoidal-categories|Graded Monoidal Categories]]에서 $q$와 tensor product setting을 읽는다.
- 상위 개념: [[topics/03-category-theory/pro-categories|Pro-Categories]]와 [[topics/03-category-theory/graded-monoidal-categories|Graded Monoidal Categories]]가 더 넓은 categorical 배경이다.
- 다음에 읽을 것: [[topics/06-quiver-hecke-klr-algebras/r-matrix-renormalization|R-Matrix Renormalization]]에서는 affinization에 붙는 R-matrix data를 읽고, [[topics/08-localization-of-categories/root-objects-in-localized-categories|Root Objects in Localized Categories]]에서는 affine object가 root object 정의에 쓰이는 방식을 읽는다.

## Source notes

<details>
<summary>Sources used</summary>

- [[sources/papers/kashiwara-nakashima25-crystal-structure-localized-quantum-unipotent-coordinate-category|Kashiwara-Nakashima 2025]], lines 1519-1621 of `inbox/papers/crystal.tex`: pro-category, graded category, and $\operatorname{Pro}^{\mathrm{coh}}(A,\mathscr C)$ setup.
- Kashiwara-Nakashima 2025, lines 1623-1642: definition of affine object and $\operatorname{Aff}(\mathscr C)$.
- Kashiwara-Nakashima 2025, lines 1646-1728: graded monoidal category assumptions, rational affine objects, monoidal structure on $\operatorname{Aff}(\mathscr C)$, and rigidity.
- Kashiwara-Nakashima 2025, lines 1777-1804: rational centers and affinizations.
- Kashiwara-Nakashima 2025, lines 1837-1842: real and affreal simple objects.
- Kashiwara-Nakashima 2025, lines 2331-2375: quiver-Hecke specialization and the example $L(i)=\langle i\rangle$.
- Kashiwara-Nakashima 2025, lines 2976-3022: localization compatibility for affinizations.
- Source-location review: `reports/reviews/2026-06-01-affine-r-matrix-prerequisite-source-location-review.md`.

</details>
