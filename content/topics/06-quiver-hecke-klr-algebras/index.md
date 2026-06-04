---
id: topic-shelf-quiver-hecke-klr-algebras
title: Quiver-Hecke / KLR Algebras
level: overview
---

이 장은 quiver-Hecke algebra 자체에서 시작해, 그 module categories와 monoidal subcategories를 거쳐 categorification과 localization으로 이동한다. 핵심은 algebra presentation을 오래 붙잡는 것이 아니라, 그 algebra의 modules가 category-level object가 되고 Grothendieck ring과 localized category로 내려가는 과정을 읽는 것이다.

## 읽는 순서

1. [[topics/06-quiver-hecke-klr-algebras/quiver-hecke-algebras|Quiver-Hecke Algebras]]

   Generators, relations, grading, diagrammatic picture를 먼저 읽는다. 이 page는 뒤의 모든 quiver-Hecke category topic이 사용하는 algebra-level source이다.

2. [[topics/06-quiver-hecke-klr-algebras/quiver-hecke-module-categories|Quiver-Hecke Module Categories]]

   $H_\alpha$의 modules를 모아 category-level object로 보는 단계이다. Convolution product, Grothendieck group, induction/restriction language가 여기서 시작된다.

3. [[topics/06-quiver-hecke-klr-algebras/type-a-klr-segment-modules|Type A KLR Segment Modules]]

   Type $A_\infty$ KLR category에서 segment modules $L(a,b)$와 ordered multisegments를 읽는다. Quantum affine Schur-Weyl duality의 type $A$ 예시를 읽을 때 필요한 짧은 prerequisite이다.

4. [[topics/06-quiver-hecke-klr-algebras/type-a-segment-module-convolutions|Type A Segment Module Convolutions]]

   Segment modules 두 개의 convolution product가 intervals의 상대 위치에 따라 어떻게 달라지는지 읽는다. R-matrix image, irreducibility, exact sequence, head와 socle이 여기서 처음 구체적으로 연결된다.

5. [[topics/06-quiver-hecke-klr-algebras/quiver-hecke-subcategories|Quiver-Hecke Subcategories]]

   $R\text{-gmod}$ 안의 $\mathcal C_w$, $\mathcal C_{*,v}$, $\mathcal C_{w,v}$ 같은 subcategories를 읽는다. Localization과 determinantial modules는 이 subcategory layer 없이는 정확히 놓이지 않는다.

6. [[topics/06-quiver-hecke-klr-algebras/determinantial-modules|Determinantial Modules]]

   $\mathcal C_w$와 $\mathcal C_{w,v}$ 안에서 특별한 module objects가 어떻게 들어오는지 읽는다. 이 objects는 quantum minors, monoidal categorification, category localization 사이를 잇는 중요한 중간층이다.

7. [[topics/06-quiver-hecke-klr-algebras/r-matrix-renormalization|R-Matrix Renormalization]]

   Convolution product에서 simple objects를 서로 바꿀 때 나타나는 R-matrix degree와 renormalized R-matrix를 읽는다. 이 machinery는 normal sequences, head-simplicity statements, localized root operators로 이어진다.

8. [[topics/06-quiver-hecke-klr-algebras/normal-sequences|Normal Sequences]]

   여러 simple objects의 convolution을 제어하기 위해 R-matrix behavior를 순서 있는 sequence로 묶어 읽는다.

9. [[topics/06-quiver-hecke-klr-algebras/head-simplicity-of-convolutions|Head Simplicity of Convolutions]]

   Convolution product의 head와 socle이 언제 simple하게 되는지 theorem-level statement를 읽는다. Localized root operators와 root objects의 formula를 읽기 전에 필요한 category-level 사실이다.

## Crystal and Demazure branch

[[topics/06-quiver-hecke-klr-algebras/demazure-subcategories-of-quiver-hecke-modules|Demazure Subcategories of Quiver-Hecke Modules]]는 [[topics/02-crystal-bases/demazure-crystals|Demazure Crystals]]를 읽은 뒤 들어가는 것이 좋다. 이 page는 ordinary crystal side의 Demazure crystal이 quiver-Hecke module category 안에서 어떤 subcategory로 나타나는지를 다룬다.

[[topics/06-quiver-hecke-klr-algebras/shuffle-lemmas-for-quiver-hecke-modules|Shuffle Lemmas for Quiver-Hecke Modules]]는 theorem machinery에 가까운 topic이다. Normal sequences와 subcategory notation을 읽은 뒤, proof-level arguments가 필요할 때 들어간다.

## 이 장 밖으로 이어지는 길

- [[topics/05-monoidal-categorification/monoidal-categorification|Monoidal Categorification]]에서는 quiver-Hecke module category의 Grothendieck ring이 cluster algebra와 어떻게 비교되는지 읽는다.
- [[topics/08-localization-of-categories/quiver-hecke-category-localization|Quiver-Hecke Category Localization]]에서는 $\mathcal C_w$에서 determinantial objects를 invertible하게 만들어 $\widetilde{\mathcal C}_w$로 이동한다.
- [[topics/08-localization-of-categories/localized-crystals|Localized Crystals]]에서는 localized category의 simple objects 위에 crystal structure를 놓는다.

## 지금은 건너뛰어도 되는 내용

처음 읽을 때는 `R-Matrix Renormalization`, `Normal Sequences`, `Head Simplicity of Convolutions`, `Shuffle Lemmas`를 모두 한 번에 읽을 필요가 없다. 먼저 `Quiver-Hecke Algebras`, `Quiver-Hecke Module Categories`를 읽는다. Quantum affine Schur-Weyl 예시로 가려면 `Type A KLR Segment Modules`를 먼저 읽고, segment products까지 필요할 때만 `Type A Segment Module Convolutions`로 들어간다. Localization 방향으로 가려면 `Quiver-Hecke Subcategories`, `Determinantial Modules`를 읽는 것이 자연스럽다.
