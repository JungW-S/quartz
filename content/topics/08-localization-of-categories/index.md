---
id: topic-shelf-localization-of-categories
title: Localization of Categories
level: overview
---

이 장은 category 안의 chosen objects를 invertible하게 만드는 general construction에서 시작해, quiver-Hecke subcategory $\mathcal C_w$를 localized category $\widetilde{\mathcal C}_w$로 보내는 specialized construction으로 이동한다. 그 다음 $\widetilde{\mathcal C}_w$의 simple objects 위에 crystal structure를 놓는 방향을 읽는다.

## 읽는 순서

1. [[topics/08-localization-of-categories/category-localization|Localization of Categories]]

   Real commuting family of braiders를 사용해 monoidal category를 localize하는 general construction을 읽는다. 이 page는 quiver-Hecke category localization이 무엇을 specialized하는지 설명하는 상위 개념이다.

2. [[topics/08-localization-of-categories/quiver-hecke-category-localization|Quiver-Hecke Category Localization]]

   $\mathcal C_w$에서 determinantial objects를 invertible하게 만들어 $\widetilde{\mathcal C}_w$로 이동하는 construction을 읽는다. 이때 localize되는 것은 quiver-Hecke algebra가 아니라 quiver-Hecke module category 안의 monoidal subcategory이다.

3. [[topics/08-localization-of-categories/localized-crystals|Localized Crystals]]

   $\operatorname{Irr}(\widetilde{\mathcal C}_w)$ 위에 crystal structure를 놓는 목적지를 먼저 읽는다. 이 page는 localized category가 왜 crystal theory와 연결되는지 보여 주는 중심 응용이다.

4. [[topics/08-localization-of-categories/root-objects-in-localized-categories|Root Objects in Localized Categories]]

   Localized root operators를 정의할 때 쓰는 simple-root-type objects를 읽는다. Root objects는 ordinary crystal operator가 아니라 localized category 안의 object-level input이다.

5. [[topics/08-localization-of-categories/localized-root-operators|Localized Root Operators]]

   $\widetilde E_i$와 $\widetilde F_i$가 localized simple objects 위에서 어떻게 정의되는지 읽는다. 이 page는 formula-level operation에 가까우므로, `Localized Crystals`의 목적을 먼저 본 뒤 들어가는 것이 좋다.

6. [[topics/08-localization-of-categories/reverse-equivalence-of-localized-categories|Reverse Equivalence of Localized Categories]]

   Weyl group element를 반대로 보는 localized categories 사이의 equivalence를 읽는다. 이 page는 basic construction보다 뒤에 오는 theorem-level bridge이다.

7. [[topics/08-localization-of-categories/quantum-twist-automorphisms|Quantum Twist Automorphisms]]

   Localized crystal에서 보이는 twist direction을 parent page에서 분리해 두는 advanced bridge이다.

8. [[topics/08-localization-of-categories/localized-pbw-parametrizations|Localized PBW Parametrizations]]

   Localized crystal을 coordinate language로 읽기 위한 PBW-parametrization 자리이다.

9. [[topics/08-localization-of-categories/localized-string-parametrizations|Localized String Parametrizations]]

   PBW-coordinate language와 비교될 string-parametrization 자리이다.

10. [[topics/08-localization-of-categories/left-and-right-g-vectors|Left and Right g-Vectors]]

   Coordinate-formula material을 읽기 전에 필요한 left/right g-vector 자리이다.

11. [[topics/08-localization-of-categories/coordinate-formulas-for-quantum-twist-on-localized-crystals|Coordinate Formulas for Quantum Twist on Localized Crystals]]

   JP25의 formula-level material을 나중에 분리해서 다룰 theorem-level 자리이다.

## 먼저 필요한 다른 장

- [[topics/03-category-theory/category-theory|Category Theory]]와 [[topics/03-category-theory/graded-monoidal-categories|Graded Monoidal Categories]]는 monoidal category와 grading language를 제공한다.
- [[topics/06-quiver-hecke-klr-algebras/quiver-hecke-subcategories|Quiver-Hecke Subcategories]]는 localization input인 $\mathcal C_w$를 제공한다.
- [[topics/06-quiver-hecke-klr-algebras/determinantial-modules|Determinantial Modules]]는 localization에서 invertible하게 만드는 objects를 제공한다.
- [[topics/02-crystal-bases/crystal-bases|Crystal Bases]]와 [[topics/02-crystal-bases/cellular-crystals|Cellular Crystals]]는 localized crystal이 비교되는 crystal-side target을 제공한다.

## 지금은 건너뛰어도 되는 내용

처음에는 `Localization of Categories`, `Quiver-Hecke Category Localization`, `Localized Crystals`만 읽어도 장의 큰 흐름을 잡을 수 있다. `Root Objects`, `Localized Root Operators`, `Reverse Equivalence`는 localized crystal의 operators와 theorem-level comparison을 실제로 계산하거나 증명할 때 필요한 세부 topic이다. `Quantum Twist Automorphisms` 이후의 coordinate topics는 앞의 topic들을 먼저 읽은 뒤에 접근하는 것이 맞다.
