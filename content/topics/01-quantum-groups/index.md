---
id: topic-shelf-quantum-groups
title: Quantum Groups
level: overview
---

이 장은 Drinfeld-Jimbo quantum group $U_q(\mathfrak g)$를 중심에 두고 읽는다. Root system, weight lattice, universal enveloping algebra는 출발점에서 필요한 기술적 언어이고, 장의 목적은 이 언어를 써서 quantum group, 그 representations, coordinate-ring side, basis theory, R-matrix direction을 연결하는 것이다.

## 읽는 순서

1. [[topics/01-quantum-groups/universal-enveloping-algebras|Universal Enveloping Algebras]]

   Classical Lie algebra action을 associative algebra의 module action으로 옮기는 배경을 읽는다. Quantum group은 이 classical object를 $q$-deformation한 쪽에서 등장한다.

2. [[topics/01-quantum-groups/root-systems-and-weight-lattices|Root Systems and Weight Lattices]]

   Cartan matrix, simple roots, coroots, weights, Weyl group notation을 고정한다. 이 topic은 기술적 도구이므로, 처음에는 quantum group 정의를 읽는 데 필요한 notation만 잡고 넘어가도 된다.

3. [[topics/01-quantum-groups/lie-algebra-representations|Lie Algebra Representations]]

   Algebra가 vector space 위에 작용한다는 representation language를 먼저 읽는다. 뒤에서 $U_q(\mathfrak g)$-module을 읽을 때 같은 관점을 사용한다.

4. [[topics/01-quantum-groups/quantum-groups|Quantum Groups]]

   이 장의 중심 page이다. $U_q(\mathfrak g)$의 generators와 relations, $U_q(\mathfrak{sl}_2)$ example, Hopf algebra structure, tensor product representations, crystal/canonical-basis direction, R-matrix direction을 한 번에 배치한다.

5. [[topics/01-quantum-groups/weight-modules|Weight Modules]]

   Quantum group representation을 weight spaces로 분해해서 읽는다. 이후 highest-weight modules, characters, crystal bases를 읽기 위한 직접적인 표현론 언어이다.

6. [[topics/01-quantum-groups/highest-weight-modules|Highest-Weight Modules]]

   Highest weight vector 하나가 module을 generate하는 situation을 읽는다. Crystal bases와 Verma modules로 넘어가기 전에 이 topic을 먼저 읽는 것이 좋다.

7. [[topics/01-quantum-groups/characters-of-representations|Characters of Representations]]

   Weight multiplicities를 formal sum으로 기록하는 방법을 읽는다. Demazure character formula, crystal character computations, representation 비교를 읽기 전에 필요한 bookkeeping이다.

8. [[topics/01-quantum-groups/category-o|Quantum Category O]]

   Weight modules 중 finiteness와 boundedness 조건을 만족하는 quantum-group category를 읽는다. 이 topic은 highest-weight representation theory를 category-level로 놓는 자리이다.

9. [[topics/01-quantum-groups/verma-modules|Verma Modules]]

   Quantum Category O 안에서 universal highest-weight module을 읽는다. Irreducible highest-weight modules를 다룰 때 기준점이 되는 construction이다.

## Coordinate-ring and basis direction

[[topics/01-quantum-groups/quantum-coordinate-rings|Quantum Coordinate Rings]]는 quantum group의 coordinate-ring side를 다룬다. 그 다음 [[topics/01-quantum-groups/quantum-unipotent-coordinate-rings|Quantum Unipotent Coordinate Rings]]에서 localized crystal과 determinantial-module direction에 필요한 중간 언어를 따로 둔다.

[[topics/01-quantum-groups/dual-canonical-bases|Dual Canonical Bases]]는 coordinate-ring side와 canonical-basis language를 연결한다. [[topics/01-quantum-groups/pbw-parametrizations-of-quantum-unipotent-coordinate-rings|PBW Parametrizations of Quantum Unipotent Coordinate Rings]]는 reduced expression으로 canonical-basis elements를 coordinate data로 읽는 ordinary PBW layer이다. [[topics/01-quantum-groups/quantum-minors-and-frozen-variables|Quantum Minors and Frozen Variables]]는 quantum minor와 frozen variable의 level 차이를 정리해서 cluster algebra와 localization path로 넘어가는 준비를 한다.

이 coordinate-ring branch는 [[topics/04-cluster-algebras/quantum-cluster-algebras|Quantum Cluster Algebras]], [[topics/05-monoidal-categorification/monoidal-categorification|Monoidal Categorification]], [[topics/06-quiver-hecke-klr-algebras/determinantial-modules|Determinantial Modules]]로 넘어갈 때 중요하다.

Crystal theory는 별도 장으로 읽는다. Quantum group page를 읽은 뒤 [[topics/02-crystal-bases/crystal-bases|Crystal Bases]]로 이동하면 $q\to0$에서 representation이 combinatorial object로 바뀌는 방향을 따라갈 수 있다.

## Specialization and R-matrix direction

[[topics/01-quantum-groups/integral-forms-of-quantum-groups|Integral Forms of Quantum Groups]]와 [[topics/01-quantum-groups/root-of-unity-quantum-groups|Root-of-Unity Quantum Groups]]는 $q$를 specialize할 때 필요한 branch이다. 처음 읽을 때는 건너뛰어도 되지만, root of unity representation theory를 읽으려면 integral form을 먼저 보아야 한다.

[[topics/01-quantum-groups/yang-baxter-equation|Yang-Baxter Equation]]과 [[topics/01-quantum-groups/universal-r-matrix|Universal R-Matrix]]는 tensor product representations의 braid-type symmetry로 이어지는 branch이다. Quiver-Hecke 쪽의 [[topics/06-quiver-hecke-klr-algebras/r-matrix-renormalization|R-Matrix Renormalization]]과 이름은 비슷하지만, 먼저 quantum-group representation category의 R-matrix와 quiver-Hecke module category의 R-matrix technology가 서로 다른 level의 objects를 다룬다는 점을 구분해야 한다.

## 지금은 건너뛰어도 되는 내용

처음 읽는 목적이 crystal bases나 quiver-Hecke categorification으로 가는 것이라면, `Integral Forms`, `Root-of-Unity Quantum Groups`, `Universal R-Matrix`, `Yang-Baxter Equation`은 나중으로 미룰 수 있다. 먼저 `Quantum Groups`, `Weight Modules`, `Highest-Weight Modules`, `Characters of Representations`를 읽고, 그 다음 Crystal Bases 장으로 넘어가는 것이 더 직접적인 경로이다.
