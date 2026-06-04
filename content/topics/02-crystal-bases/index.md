---
id: topic-shelf-crystal-bases
title: Crystal Bases
level: overview
---

이 장은 quantum group representation을 combinatorial object로 읽는 방법을 순서대로 모은다. 먼저 abstract crystal language를 익히고, tensor product와 highest-weight model을 거쳐 $B(\infty)$와 Demazure crystals로 이동한 뒤, ordinary coordinate parametrization을 거쳐 cellular crystals와 localized-category 쪽 응용으로 넘어간다.

## 읽는 순서

1. [[topics/02-crystal-bases/crystal-bases|Crystal Bases]]

   전체 입구 page이다. Crystal base가 왜 representation theory에서 나오는지, $q\to0$ 관점이 어떤 combinatorial object를 남기는지 먼저 잡는다.

2. [[topics/02-crystal-bases/abstract-crystals|Abstract Crystals]]

   Weight map, Kashiwara operators, $\varepsilon_i$, $\varphi_i$, crystal graph를 정확한 combinatorial data로 읽는다. 이후 모든 crystal topic의 공통 언어이다.

3. [[topics/02-crystal-bases/tensor-products-of-crystals|Tensor Products of Crystals]]

   두 crystals를 tensor product로 합칠 때 Kashiwara convention의 operator rule이 어떻게 작동하는지 읽는다. Tensor notation은 뒤의 cellular/localized crystal comparison에서 계속 필요하다.

4. [[topics/02-crystal-bases/highest-weight-crystals|Highest Weight Crystals]]

   Highest-weight module에서 나오는 crystal $B(\lambda)$를 읽는다. Finite $U_q(\mathfrak{sl}_2)$ string example은 여기서 보는 것이 가장 자연스럽다.

5. [[topics/02-crystal-bases/b-infinity-crystal|The Crystal B(infinity)]]

   Negative half $U_q^-(\mathfrak g)$에서 나오는 universal crystal을 읽는다. Demazure crystals와 cellular crystals로 가는 중간층이다.

6. [[topics/02-crystal-bases/demazure-crystals|Demazure Crystals]]

   Weyl group element $w$가 주어졌을 때 ordinary crystal 안에서 선택되는 Demazure subcrystal을 읽는다. Quiver-Hecke 쪽 Demazure subcategories를 읽기 전에 이 ordinary crystal side를 먼저 보는 것이 좋다.

7. [[topics/02-crystal-bases/string-parametrizations-of-demazure-crystals|String Parametrizations of Demazure Crystals]]

   Demazure-type ordinary crystal의 원소를 reduced expression에 따른 string-coordinate tuple로 읽는다. Localized string parametrization을 읽기 전에 ordinary coordinate extraction을 먼저 분리해서 보는 단계이다.

8. [[topics/02-crystal-bases/cellular-crystals|Cellular Crystals]]

   Cellular crystal은 Kashiwara-Nakashima 2025에서 localized quantum unipotent coordinate category와 비교되는 combinatorial target이다. 이 page는 ordinary crystal language를 advanced bridge로 연결한다.

## 이 장 밖으로 이어지는 길

- [[topics/08-localization-of-categories/localized-crystals|Localized Crystals]]는 localized category의 simple objects 위에 crystal structure를 놓는 방향이다.
- [[topics/08-localization-of-categories/localized-root-operators|Localized Root Operators]]는 localized crystal arrows를 만드는 formula-level operation을 따로 다룬다.
- [[topics/06-quiver-hecke-klr-algebras/demazure-subcategories-of-quiver-hecke-modules|Demazure Subcategories of Quiver-Hecke Modules]]는 Demazure crystal idea가 quiver-Hecke category 쪽에서 어떻게 나타나는지 읽는 advanced page이다.

## 지금은 건너뛰어도 되는 내용

Cellular crystals와 localized crystals는 ordinary crystal definitions만으로 바로 읽기 어렵다. 처음 읽을 때는 `Crystal Bases`, `Abstract Crystals`, `Tensor Products of Crystals`, `Highest Weight Crystals`를 먼저 읽고, $B(\infty)$와 Demazure crystals를 거친 뒤 string parametrization을 통해 coordinate language를 익히고 cellular/localized bridge로 넘어가는 것이 좋다.
