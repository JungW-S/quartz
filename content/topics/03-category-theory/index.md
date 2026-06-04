---
id: topic-shelf-category-theory
title: Category Theory
level: overview
---

이 장은 quiver-Hecke category, monoidal categorification, localized category를 읽기 전에 필요한 category-theoretic language를 모은다. 처음에는 category, functor, natural transformation, universal property만 익히고, 그 다음부터는 각 construction이 실제로 필요한 위치에서 advanced topic으로 넘어간다.

## 읽는 순서

1. [[topics/03-category-theory/category-theory|Category Theory]]

   Objects, morphisms, composition, identity, functor, natural transformation을 먼저 읽는다. 이 page가 뒤의 모든 categorical pages에서 쓰는 기본 언어이다.

2. [[topics/03-category-theory/graded-monoidal-categories|Graded Monoidal Categories]]

   Tensor product가 있는 category와 grading shift가 함께 작동하는 setting으로 넘어간다. Quiver-Hecke module categories, R-matrices, affine objects를 읽기 전에 필요한 category-level 배경이다.

3. [[topics/03-category-theory/pro-categories|Pro-Categories]]

   Completed object나 projective-limit 형태의 object가 등장할 때 필요한 language이다. [[topics/03-category-theory/affine-objects-in-monoidal-categories|Affine Objects in Monoidal Categories]]를 읽기 전에 이 page를 먼저 읽는다.

4. [[topics/08-localization-of-categories/category-localization|Localization of Categories]]

   Category 안의 chosen objects를 invertible하게 만드는 construction을 읽는다. 이 route는 [[topics/08-localization-of-categories/quiver-hecke-category-localization|Quiver-Hecke Category Localization]]으로 이어진다.

## 이 장 안의 advanced topics

[[topics/03-category-theory/affine-objects-in-monoidal-categories|Affine Objects in Monoidal Categories]]는 graded monoidal category와 pro-category language를 함께 사용한다. Ordinary object가 아니라 completed object와 parameter $z$를 가진 object를 다루기 때문에, 앞의 두 prerequisite를 읽고 들어가는 것이 자연스럽다.

[[topics/03-category-theory/quasi-rigid-monoidal-categories|Quasi-Rigid Monoidal Categories]]는 localized root objects와 localized crystals를 읽을 때 필요한 duality language를 제공한다. 일반 rigid category 이론 전체가 아니라, localized category 쪽에서 쓰는 quasi-rigid condition을 분리해 둔 page로 읽는다.

## 다른 장으로 넘어가는 길

- [[topics/06-quiver-hecke-klr-algebras/quiver-hecke-module-categories|Quiver-Hecke Module Categories]]에서는 graded module categories와 convolution product가 실제 algebra representation에서 어떻게 생기는지 읽는다.
- [[topics/05-monoidal-categorification/monoidal-categorification|Monoidal Categorification]]에서는 monoidal category의 Grothendieck ring이 cluster algebra와 연결되는 방식을 읽는다.
- [[topics/08-localization-of-categories/quiver-hecke-category-localization|Quiver-Hecke Category Localization]]에서는 localization construction이 $\mathcal C_w$와 determinantial modules에 적용되는 방식을 읽는다.

## 지금은 건너뛰어도 되는 내용

Yoneda lemma, adjunctions, limits, colimits, monads, Kan extensions는 category theory의 중요한 주제이지만, 현재 독서 경로에서 가장 먼저 필요한 것은 아니다. 이 장에서는 quiver-Hecke와 categorification pages를 읽기 위한 최소 언어를 먼저 고정하고, 더 강한 category theory가 필요해지는 지점에서 별도 topic으로 분리한다.
